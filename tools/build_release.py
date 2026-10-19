"""Build a deterministic ZIP from the exact checked release file list."""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import os
import zipfile

from check_release import check, MANIFEST


def build(root, output):
    root=Path(root).resolve();output=Path(output).resolve()
    if output.is_relative_to(root) or output.exists():
        raise ValueError('Choose a new archive path outside the release folder.')
    manifest_bytes=(root/MANIFEST).read_bytes()
    result=check(root)
    if result['status']!='PASS':
        raise ValueError('Release checks failed; no archive was written.')
    if (root/MANIFEST).read_bytes()!=manifest_bytes:
        raise ValueError('The manifest changed during validation.')
    manifest=json.loads(manifest_bytes)
    expected={row['path']:row for row in manifest['files']}
    expected[MANIFEST]={'sha256':hashlib.sha256(manifest_bytes).hexdigest(),'bytes':len(manifest_bytes)}
    day=datetime.date.fromisoformat(manifest['release_date'])
    if not 1980<=day.year<=2107:raise ValueError('Release date is outside the ZIP date range.')
    paths=sorted([row['path'] for row in manifest['files']]+[MANIFEST])
    output.parent.mkdir(parents=True,exist_ok=True)
    partial=output.with_suffix(output.suffix+'.partial')
    if partial.exists():raise ValueError('A previous partial archive already exists.')
    # Mode x prevents replacing another archive. Timestamps and permissions are
    # release constants; no host file paths, user IDs or filesystem times leak.
    with zipfile.ZipFile(partial,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
        for relative in paths:
            data=(root/relative).read_bytes()
            if len(data)!=expected[relative]['bytes'] or hashlib.sha256(data).hexdigest()!=expected[relative]['sha256']:
                raise ValueError('A release file changed after validation: '+relative)
            info=zipfile.ZipInfo('bo4-research/'+relative,date_time=(day.year,day.month,day.day,0,0,0))
            info.create_system=3;info.external_attr=0o100644<<16
            info.compress_type=zipfile.ZIP_DEFLATED
            archive.writestr(info,data,compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
    # Linking fails if another process created the final path; never replace it.
    os.link(partial,output)
    partial.unlink()
    digest=hashlib.sha256(output.read_bytes()).hexdigest()
    return {'archive':output.name,'sha256':digest,'files':len(paths),'bytes':output.stat().st_size}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    print(json.dumps(build(args.root,args.output),indent=2))
