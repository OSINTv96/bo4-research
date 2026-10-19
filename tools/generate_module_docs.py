"""Render saved module summaries without inventing or cutting explanations.

Only local module/index/claim records are read. Historical contracts are not
edited. These are explicitly excerpts, with full-record identities and hashes.
"""
import argparse
import hashlib
import json
from pathlib import Path


def load(path):
    return json.loads(path.read_text(encoding='utf-8'))


def text(value):
    if isinstance(value, str):
        result = value.replace('`', "'").replace('\n', ' ')
    else:
        result = json.dumps(value, ensure_ascii=True).replace('`', "'")
    # Excerpts are source text, never interpreted as Markdown links.
    return result.replace('[', '&#91;').replace(']', '&#93;')


def explanation(summary):
    for key in ('answer', 'behavior', 'purpose'):
        if summary.get(key):
            return text(summary[key])
    result = 'No standalone body contract is available in this selected summary.'
    if summary.get('category'):
        result += ' Available classification: '+text(summary['category'])+'.'
    return result


def claims(root, module, record_path):
    for number, claim in enumerate(module.get('claims', [])):
        yield claim, record_path, f'/claims/{number}'
    for shard in module.get('claim_shards', []):
        path = root/shard['path']
        if hashlib.sha256(path.read_bytes()).hexdigest() != shard['sha256']:
            raise ValueError('Changed claim shard: '+shard['path'])
        for number, claim in enumerate(load(path)['claims']):
            yield claim, shard['path'], f'/claims/{number}'


def render(root, entry):
    module = load(root/entry['record'])
    projections = {}
    for reference in module.get('documentation_projections', []):
        path=root/reference['path']
        if hashlib.sha256(path.read_bytes()).hexdigest()!=reference['sha256']:
            raise ValueError('Changed documentation projection: '+reference['path'])
        for row in load(path)['claims']:
            key=(row['claim_record'],row['claim_pointer'])
            if key in projections:
                raise ValueError('Duplicate documentation projection')
            projections[key]=(row,reference['path'])
    lines = ['# '+module['original_path'], '',
             'Project-added notes. See the [code](../../'+entry['path']+').', '',
             'The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.', '',
             'Original revision: `'+str(module['source_revision'])+'`. Original SHA-256: `'+module['original_sha256']+'`.', '',
             'Exact source spans, dependencies and bounded review evidence: [module record](../../'+entry['record']+').', '',
             'New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.', '',
             'Selected source notes (excerpts; full records remain authoritative):', '']
    for claim, path, pointer in claims(root, module, entry['record']):
        projection=projections.get((path,pointer))
        if projection:
            row,projection_path=projection
            if row['selection_id']!=claim['selection_id'] or row['subject']!=claim['subject']:
                raise ValueError('Documentation projection does not bind the exact claim')
            summary=row['summary']
        else:
            summary = claim.get('summary') or {}
        label = summary.get('unit_id') or summary.get('id') or claim['selection_id']
        spans = ', '.join(str(c.get('line_start', '?'))+'-'+str(c.get('line_end','?')) for c in claim.get('citations',[]) if c.get('line_start')) or 'not specified'
        lines += ['- `'+str(label).replace('`','')+'` (original lines '+spans+'): '+explanation(summary), '']
        for field in ('inputs','outputs','side_effects','branches','lifecycle','calls','dependencies','ordered_state_changes','unknowns','limitations','limit','status'):
            if summary.get(field):
                lines += ['  '+field.replace('_',' ')+': '+text(summary[field]), '']
        subject = claim.get('subject', {})
        if projection:
            lines += ['  Complete explanatory fields: [exact projection](../../'+projection_path+'). Older compact summaries and original evidence remain unchanged.', '']
        lines += ['  Exact excerpt: [saved claim](../../'+path+') at JSON pointer `'+pointer+'`.', '',
                  '  Archived evidence ID: `'+str(subject.get('evidence_id','not recorded'))+'` at JSON pointer `'+str(subject.get('pointer',''))+'`; file SHA-256 `'+str(subject.get('sha256','not recorded'))+'`'+('; selected record SHA-256 `'+subject['record_sha256']+'`.' if subject.get('record_sha256') else '.'), '']
    if module.get('dependency_decisions'):
        lines += ['Dependency decisions: [exact edge records](../../provenance/dependency-decisions.json). Included callees remain at the bounded static scopes recorded there.', '']
        for identity in module['dependency_decisions']:
            decision_path='provenance/dependency-decisions/'+identity+'.json'
            decision=load(root/decision_path)
            lines += ['- ['+identity+'](../../'+decision_path+'): `'+decision['module']+'` to `'+decision['identity']+'`; '+decision['decision']+'.', '',
                      '  '+decision['reason'], '']
            if decision.get('required_callee_functions'):
                lines += ['  Selected callee candidates: '+', '.join('`'+name+'`' for name in decision['required_callee_functions'])+'. Source-only conditional selection; refer to the full edge record for caller lines and gates.', '']
    return '\n'.join(lines).rstrip()+'\n'


def render_pages(root, entry):
    rendered=render(root,entry)
    # Bound file size by whole claim blocks, never by cutting an explanation.
    parts=rendered.split('\n- `')
    intro=parts[0]
    blocks=['\n- `'+part for part in parts[1:]]
    chunks=[];chunk=''
    for block in blocks:
        if len((intro+block).encode('utf-8'))>1800000:
            raise ValueError('A single claim needs a separately bounded presentation')
        if chunk and len((intro+chunk+block).encode('utf-8'))>1600000:
            chunks.append(chunk);chunk=''
        chunk+=block
    chunks.append(chunk)
    base=Path(entry['documentation'])
    paths=[base if n==0 else base.with_name(base.stem+f'-page-{n+1:03d}.md') for n in range(len(chunks))]
    pages={}
    for n,(path,chunk) in enumerate(zip(paths,chunks)):
        navigation=''
        if len(paths)>1:
            navigation='\n\nPages: '+' | '.join(f'[{i+1}]({p.name})' for i,p in enumerate(paths))+f'. This is page {n+1}; claims continue at complete record boundaries.\n'
        pages[path.as_posix()]=(intro+navigation+chunk).rstrip()+'\n'
    return pages


def generate(root):
    entries = load(root/'provenance/module-index.json')['modules']
    for entry in entries:
        for path,content in render_pages(root,entry).items():
            (root/path).write_text(content, encoding='utf-8', newline='\n')
    return len(entries)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    print('Generated', generate(args.root), 'module documents; no summary text sliced.')
