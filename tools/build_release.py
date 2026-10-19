"""Build a deterministic ZIP from the exact checked release file list."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import zipfile

from check_release import check, MANIFEST


def build(root, output):
    root=Path(root).resolve();output=Path(output).resolve()
    if output.is_relative_to(root) or output.exists():
        raise ValueError('Choose a new archive path outside the release folder.')
    result=check(root)
    if result['status']!='PASS':
        raise ValueError('Release checks failed; no archive was written.')
    manifest=json.loads((root/MANIFEST).read_text(encoding='utf-8'))
    paths=sorted([row['path'] for row in manifest['files']]+[MANIFEST])
    output.parent.mkdir(parents=True,exist_ok=True)
    partial=output.with_suffix(output.suffix+'.partial')
    if partial.exists():raise ValueError('A previous partial archive already exists.')
    # Mode x prevents replacing another archive. Timestamps and permissions are
    # release constants; no host file paths, user IDs or filesystem times leak.
    with zipfile.ZipFile(partial,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
        for relative in paths:
            data=(root/relative).read_bytes()
            info=zipfile.ZipInfo('bo4-hmh-research/'+relative,date_time=(2026,10,19,0,0,0))
            info.create_system=3;info.external_attr=0o100644<<16
            info.compress_type=zipfile.ZIP_DEFLATED
            archive.writestr(info,data,compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
    os.rename(partial,output)
    digest=hashlib.sha256(output.read_bytes()).hexdigest()
    return {'archive':output.name,'sha256':digest,'files':len(paths),'bytes':output.stat().st_size}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    print(json.dumps(build(args.root,args.output),indent=2))
