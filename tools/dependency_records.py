"""Load the complete hashed dependency inventory without duplicating large files."""
import hashlib
import json


def load_modules(root):
    manifest=json.loads((root/'provenance/dependencies.json').read_text(encoding='utf-8'))
    if manifest.get('schema')!='hmh-module-dependencies-v2':
        raise ValueError('Unsupported dependency inventory schema')
    for ref in manifest['module_shards']:
        path=(root/ref['path']).resolve()
        if not path.is_relative_to(root.resolve()):
            raise ValueError('Escaping dependency shard')
        data=path.read_bytes()
        if hashlib.sha256(data).hexdigest()!=ref['sha256']:
            raise ValueError('Changed dependency shard')
        shard=json.loads(data)
        if shard.get('schema')!='hmh-dependency-shard-v1' or len(shard['modules'])!=ref['modules']:
            raise ValueError('Malformed dependency shard')
        yield from shard['modules']


def load_source_paths(root):
    manifest=json.loads((root/'provenance/source-paths.json').read_text(encoding='utf-8'))
    if manifest.get('schema')!='hmh-candidate-source-paths-v1':
        raise ValueError('Unsupported source-path schema')
    result={'nodes':[],'edges':[]}
    for ref in manifest['shards']:
        path=(root/ref['path']).resolve()
        if not path.is_relative_to(root.resolve()):raise ValueError('Escaping source-path shard')
        data=path.read_bytes()
        if hashlib.sha256(data).hexdigest()!=ref['sha256']:raise ValueError('Changed source-path shard')
        shard=json.loads(data);kind=ref['kind']
        if shard.get('schema')!='hmh-source-path-shard-v1' or kind not in result or len(shard[kind])!=ref['records']:
            raise ValueError('Malformed source-path shard')
        result[kind]+=shard[kind]
    if any(len(result[k])!=manifest[k] for k in result):raise ValueError('Incomplete source-path inventory')
    return result
