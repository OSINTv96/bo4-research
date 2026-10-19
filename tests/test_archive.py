"""Archive integrity, fixed metadata and publication-race controls."""
import datetime
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import build_release as BUILDER


class ArchiveTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='hmh-archive-');self.addCleanup(self.temp.cleanup)
        self.base=Path(self.temp.name);self.root=self.base/'repo';self.root.mkdir()
        data=b'Research fixture.\n';(self.root/'README.md').write_bytes(data)
        (self.root/'provenance').mkdir()
        self.manifest=self.root/BUILDER.MANIFEST
        self.manifest.write_text(json.dumps({'schema':'hmh-release-manifest-v1','release_date':'2026-10-19','files':[{'path':'README.md','sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}]}),encoding='utf-8')

    def test_reproducible_archive_contents_and_metadata(self):
        a=self.base/'one.zip';b=self.base/'two.zip'
        first=BUILDER.build(self.root,a);second=BUILDER.build(self.root,b)
        self.assertEqual(first['sha256'],second['sha256'])
        with zipfile.ZipFile(a) as z:
            self.assertEqual(['bo4-research/README.md','bo4-research/provenance/release-manifest.json'],z.namelist())
            for info in z.infolist():
                self.assertEqual((2026,10,19,0,0,0),info.date_time)
                self.assertEqual(b'',info.extra);self.assertEqual(b'',info.comment)

    def test_existing_output_is_preserved(self):
        out=self.base/'existing.zip';out.write_bytes(b'existing')
        with self.assertRaises(ValueError):BUILDER.build(self.root,out)
        self.assertEqual(b'existing',out.read_bytes())

    def test_change_after_check_cannot_enter_archive(self):
        original=BUILDER.check
        def change(root):
            result=original(root);(self.root/'README.md').write_text('Unexpected replacement.');return result
        with patch.object(BUILDER,'check',side_effect=change):
            with self.assertRaisesRegex(ValueError,'changed after validation'):
                BUILDER.build(self.root,self.base/'out.zip')
        self.assertFalse((self.base/'out.zip').exists())

    def test_manifest_change_during_check_is_rejected(self):
        original=BUILDER.check
        def change(root):
            result=original(root);d=json.loads(self.manifest.read_text());d['release_date']='2026-10-20';self.manifest.write_text(json.dumps(d));return result
        with patch.object(BUILDER,'check',side_effect=change):
            with self.assertRaisesRegex(ValueError,'manifest changed'):
                BUILDER.build(self.root,self.base/'out.zip')

    def test_concurrent_output_is_not_overwritten(self):
        original=BUILDER.os.link;out=self.base/'out.zip'
        def collide(source,target):
            Path(target).write_bytes(b'other writer');return original(source,target)
        with patch.object(BUILDER.os,'link',side_effect=collide):
            with self.assertRaises(FileExistsError):BUILDER.build(self.root,out)
        self.assertEqual(b'other writer',out.read_bytes())


if __name__=='__main__':unittest.main()
