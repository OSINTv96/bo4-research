"""Validate the exact release file list, privacy patterns and fresh Git history.

This is a bounded publication check, not a guarantee that every possible secret
or identifying fact can be recognized. Reports contain file names, never values.
"""
from __future__ import annotations

import argparse
import hashlib
import ipaddress
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess

MANIFEST = 'provenance/release-manifest.json'
PROJECT_NAME = 'HMH Research'
PROJECT_EMAIL = 'maintainer@' + 'example.invalid'
ALLOWED_SUFFIXES = {'.md', '.json', '.py', '.lua', '.gsc', '.csc', '.yml'}
ALLOWED_DOTFILES = {'.editorconfig', '.gitattributes', '.gitignore'}
PRIVATE_PARTS = {'private', 'captures', 'screenshots', 'sessions', 'conversations',
                 'logs', 'dumps', '.local', '.env', '.co'+'dex', '.ssh', '.aws'}
PATTERNS = {
    'machine path': re.compile(r'(?i)\b[a-z]:[\\/]|/(?:Users|home|Volumes|mnt|media)/'),
    'private archive locator': re.compile(r'\bruns/(?:blackout|hmh)/|\b(?:inputs|workspace|registry)/'),
    'private session metadata': re.compile(r'(?i)\b(?:' + 'Co' + 'dex|' + 'Chat' + 'GPT)\b|(?<![A-Za-z0-9_])/' + r'root\b'),
    'conversation instruction': re.compile(r'(?i)\b(?:direct (?:human|user) instruction|human ' + r'said|user ' + r'said|we will ' + r'upload)\b'),
    'structured conversation': re.compile(r'"role"\s*:\s*"(?:user|assistant|system)"'),
    'private key': re.compile(r'-----BEGIN [A-Z ]*PRIVATE KEY-----'),
    'access token': re.compile(r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-(?:proj-)?[A-Za-z0-9_-]{20,}|AKIA[A-Z0-9]{16})\b'),
    'credential URL': re.compile(r'(?i)https?://[^/\s:@]+:[^/\s@]+@'),
    'bearer credential': re.compile(r'(?i)\bBearer\s+[A-Za-z0-9._~-]{20,}'),
    'phone number': re.compile(r'(?<!\d)(?:\+1[ .-]?)?\(\d{3}\)[ .-]?\d{3}[ .-]\d{4}(?!\d)'),
}
EMAIL = re.compile(r'(?<![A-Za-z0-9._%+-])[A-Za-z0-9._%+-]{1,64}@[A-Za-z0-9.-]{1,253}\.[A-Za-z]{2,24}\b')
IPV4 = re.compile(r'(?<![\d.])(?:\d{1,3}\.){3}\d{1,3}(?![\d.])')
MAC = re.compile(r'(?i)(?<![0-9a-f:])(?:[0-9a-f]{2}:){5}[0-9a-f]{2}(?![0-9a-f:])')
UUID = re.compile(r'(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b')
BUSINESS_CONTACT_FILE = 'src/lua/hashed/c11c5ddf96912e7.lua'
BUSINESS_CONTACT = 'codcoreonline@' + 'treyarch.com'


def safe_relative(value):
    if not isinstance(value, str) or not value or '\\' in value or ':' in value:
        return False
    p = PurePosixPath(value)
    return not p.is_absolute() and all(x not in ('', '.', '..') for x in value.split('/'))


def sha(data):
    return hashlib.sha256(data).hexdigest()


def text_findings(text, relative):
    issues = [label for label, pattern in PATTERNS.items() if pattern.search(text)]
    if '\x00' in text:
        issues.append('binary content')
    if '@' in text:
        for match in EMAIL.finditer(text):
            address = match.group()
            # Function@source-file identifiers are not email addresses.
            if address.endswith(('.gsc', '.csc', '.lua')):
                continue
            # This business contact is a literal in exact recovered game source.
            if relative == BUSINESS_CONTACT_FILE and address == BUSINESS_CONTACT:
                continue
            if relative in {'tools/check_release.py', 'tests/test_release.py'} and address == PROJECT_EMAIL:
                continue
            issues.append('email address'); break
    for match in IPV4.finditer(text):
        try:
            address = ipaddress.ip_address(match.group())
        except ValueError:
            continue
        if address.is_unspecified or address.is_loopback:
            continue
        issues.append('IP address'); break
    if MAC.search(text):
        issues.append('device address')
    if UUID.search(text):
        issues.append('session identifier')
    return sorted(set(issues))


def list_files(root):
    files = {}; errors = []
    for current, dirs, names in os.walk(root, followlinks=False):
        base = Path(current)
        for name in list(dirs):
            p = base/name
            rel = p.relative_to(root).as_posix()
            if p.is_symlink() or (hasattr(p, 'is_junction') and p.is_junction()):
                errors.append({'file': rel, 'reason': 'linked directory'}); dirs.remove(name)
            elif base == root and name == '.git':
                dirs.remove(name)
        for name in names:
            p = base/name; rel = p.relative_to(root).as_posix()
            if p.is_symlink() or not p.is_file():
                errors.append({'file': rel, 'reason': 'linked or nonregular file'}); continue
            files[rel] = p
    return files, errors


def git_findings(root, known_blobs=None):
    if not (root/'.git').exists():
        return [], None
    errors = []
    def fail(reason):errors.append({'file': '.git', 'reason': reason})
    if not (root/'.git').is_dir():
        return [{'file': '.git', 'reason': 'external Git directory is not a release history'}], None
    known_blobs=set(known_blobs or ())
    env=dict(os.environ,GIT_NO_LAZY_FETCH='1')
    def git(*args):
        return subprocess.check_output(['git', '--no-replace-objects', '-C', str(root), *args], stderr=subprocess.DEVNULL,env=env)
    try:
        if any((root/'.git'/name).exists() for name in ['shallow','objects/info/alternates','info/grafts']):
            fail('incomplete or external Git object history')
        commits = git('rev-list', '--all').decode().splitlines()
        if not commits:
            fail('Git history has no frozen release commit')
        if git('for-each-ref', '--format=%(refname)', 'refs/tags', 'refs/replace', 'refs/notes').strip():
            fail('unreviewed tag, replacement or note metadata')
        for commit in commits:
            data = git('cat-file', 'commit', commit).decode('utf-8')
            for role in ['author', 'committer']:
                lines = [line for line in data.splitlines() if line.startswith(role+' ')]
                if len(lines) != 1 or not re.fullmatch(re.escape(role+' '+PROJECT_NAME+' <'+PROJECT_EMAIL+'>')+r' \d+ \+0000', lines[0]):
                    fail('nonproject commit identity or time-zone metadata')
            message = data.split('\n\n', 1)[-1]
            if text_findings(message, 'commit-message'):
                fail('private pattern in commit message')
        # Inspect every reachable historical tree and every distinct blob. A
        # current-tree deletion cannot hide private content in an older commit.
        historical={}
        for commit in commits:
            for row in git('ls-tree','-r','-z',commit).split(b'\0'):
                if not row:continue
                metadata,name=row.split(b'\t',1)
                mode,kind,object_id=metadata.decode('ascii').split()
                relative=name.decode('utf-8');parts=PurePosixPath(relative).parts
                if mode not in {'100644','100755'} or kind!='blob' or not safe_relative(relative):
                    fail('linked or unsafe historical tree entry');continue
                if any(part.lower() in PRIVATE_PARTS or part.lower().startswith('.env') for part in parts):
                    fail('private filename in reachable history')
                if PurePosixPath(relative).suffix.lower() not in ALLOWED_SUFFIXES and relative not in ALLOWED_DOTFILES:
                    fail('nonrelease file type in reachable history')
                if object_id not in known_blobs:historical.setdefault(object_id,relative)
        for object_id,relative in historical.items():
            blob=git('cat-file','blob',object_id)
            if len(blob)>2*1024*1024:
                fail('historical blob exceeds review size bound');continue
            try:content=blob.decode('utf-8')
            except UnicodeError:
                fail('binary content in reachable history');continue
            if text_findings(content,relative):
                fail('private pattern in reachable historical file')
        if git('status', '--porcelain').strip():
            fail('release worktree differs from the frozen commit')
        p = subprocess.run(['git','--no-replace-objects','-C',str(root),'fsck','--full','--no-reflogs','--unreachable'],capture_output=True,env=env)
        if p.returncode or p.stdout.strip():
            fail('unreachable or invalid Git objects')
        return errors, {'commit_count': len(commits), 'historical_extra_blobs_checked':len(historical), 'head': git('rev-parse','HEAD').decode().strip(), 'identity':'neutral_project_alias'}
    except (OSError, subprocess.CalledProcessError, UnicodeError):
        fail('Git history could not be verified')
        return errors, None


def check(root, include_git=True):
    root = Path(root).resolve()
    files, errors = list_files(root)
    try:
        manifest = json.loads((root/MANIFEST).read_text(encoding='utf-8'))
        if manifest.get('schema') != 'hmh-release-manifest-v1' or not isinstance(manifest.get('files'), list):
            raise ValueError('manifest schema')
        expected = {}
        for row in manifest['files']:
            if not isinstance(row, dict) or not safe_relative(row.get('path')) or row['path'] in expected or row['path'] == MANIFEST:
                raise ValueError('manifest path')
            if not re.fullmatch(r'[0-9a-f]{64}', str(row.get('sha256'))) or type(row.get('bytes')) is not int or row['bytes'] < 0:
                raise ValueError('manifest fingerprint')
            expected[row['path']] = row
    except (OSError, ValueError, KeyError, TypeError):
        return {'status':'FAIL','errors':[{'file':MANIFEST,'reason':'missing or invalid complete manifest'}]}
    for rel in sorted(set(expected)-set(files)):
        errors.append({'file':rel,'reason':'manifest file missing'})
    for rel in sorted(set(files)-set(expected)-{MANIFEST}):
        errors.append({'file':rel,'reason':'unexpected file, including ignored local files'})
    total = 0;known_blobs=set()
    for rel,p in sorted(files.items()):
        parts = PurePosixPath(rel).parts
        if any(part.lower() in PRIVATE_PARTS or part.lower().startswith('.env') for part in parts):
            errors.append({'file':rel,'reason':'private directory or configuration file'})
        if p.suffix.lower() not in ALLOWED_SUFFIXES and rel not in ALLOWED_DOTFILES:
            errors.append({'file':rel,'reason':'nonrelease file type'})
        data = p.read_bytes(); total += len(data)
        known_blobs.add(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest())
        if len(data) > 2*1024*1024:
            errors.append({'file':rel,'reason':'file exceeds review size bound'})
        if rel in expected and (sha(data) != expected[rel]['sha256'] or len(data) != expected[rel]['bytes']):
            errors.append({'file':rel,'reason':'manifest content differs'})
        try:
            text = data.decode('utf-8')
        except UnicodeError:
            errors.append({'file':rel,'reason':'non-UTF-8 content'}); continue
        for issue in text_findings(text,rel):
            errors.append({'file':rel,'reason':issue})
    history = None
    if include_git:
        found,history=git_findings(root,known_blobs);errors.extend(found)
    return {'status':'FAIL' if errors else 'PASS','files_checked':len(files),'bytes_checked':total,
            'images_in_manifest':sum(PurePosixPath(p).suffix.lower() in {'.png','.jpg','.jpeg','.webp','.gif'} for p in expected),
            'git':history,'errors':errors,'limit':'Specified pattern, file, hash and Git checks; no game correctness or universal privacy guarantee.'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument('--report',type=Path)
    args=parser.parse_args();result=check(args.root)
    if args.report:
        report=args.report.resolve()
        if report.is_relative_to(args.root.resolve()):
            parser.error('Save execution reports outside the frozen release.')
        report.parent.mkdir(parents=True,exist_ok=True)
        report.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    return 0 if result['status']=='PASS' else 1


if __name__=='__main__':raise SystemExit(main())
