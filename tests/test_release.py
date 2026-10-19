"""Publication contamination cases in tiny disposable folders."""
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('release_check',ROOT/'tools/check_release.py')
CHECK=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(CHECK)


class ReleasePrivacyTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='hmh-release-')
        self.addCleanup(self.temp.cleanup);self.root=Path(self.temp.name)
        (self.root/'README.md').write_text('Research fixture.\n',encoding='utf-8')
        self.seal()

    def seal(self):
        rows=[]
        for p in sorted(self.root.rglob('*')):
            if p.is_file() and p.relative_to(self.root).as_posix()!=CHECK.MANIFEST:
                data=p.read_bytes();rows.append({'path':p.relative_to(self.root).as_posix(),'sha256':CHECK.sha(data),'bytes':len(data)})
        p=self.root/CHECK.MANIFEST;p.parent.mkdir(exist_ok=True)
        p.write_text(json.dumps({'schema':'hmh-release-manifest-v1','files':rows}),encoding='utf-8')

    def reasons(self):return {row['reason'] for row in CHECK.check(self.root,include_git=False)['errors']}

    def inject(self,text):
        (self.root/'README.md').write_text(text,encoding='utf-8');self.seal()

    def test_clean_fixture(self):self.assertEqual(set(),self.reasons())

    def test_ignored_screenshot_is_still_rejected(self):
        (self.root/'example.png').write_bytes(b'image fixture')
        self.assertIn('nonrelease file type',self.reasons())
        self.assertIn('unexpected file, including ignored local files',self.reasons())

    def test_screenshot_cannot_be_added_by_editing_manifest(self):
        (self.root/'example.png').write_bytes(b'image fixture');self.seal()
        self.assertIn('nonrelease file type',self.reasons())

    def test_missing_and_changed_files(self):
        (self.root/'README.md').write_text('changed')
        self.assertIn('manifest content differs',self.reasons())
        (self.root/'README.md').unlink()
        self.assertIn('manifest file missing',self.reasons())

    def test_private_environment_file(self):
        (self.root/('.en'+'v')).write_text('fixture');self.seal()
        self.assertIn('private directory or configuration file',self.reasons())

    def test_windows_path_and_json_escaped_path(self):
        for sep in ['\\','\\\\','/']:
            self.inject('Q:'+sep+'Us'+'ers'+sep+'example'+sep+'notes.txt')
            self.assertIn('machine path',self.reasons())

    def test_unix_home(self):
        self.inject('/ho'+'me/example/notes.txt')
        self.assertIn('machine path',self.reasons())

    def test_internal_reference(self):
        self.inject('ru'+'ns/blackout/private/record.json')
        self.assertIn('private archive locator',self.reasons())

    def test_session_route(self):
        self.inject('current '+'Co'+'dex session /'+'root')
        self.assertIn('private session metadata',self.reasons())

    def test_chat_instruction(self):
        self.inject('Direct '+'human '+'instruction: publish this')
        self.assertIn('conversation instruction',self.reasons())

    def test_structured_chat(self):
        self.inject(json.dumps({'ro'+'le':'us'+'er','content':'fixture'}))
        self.assertIn('structured conversation',self.reasons())

    def test_personal_email(self):
        self.inject('someone'+'@'+'example.net')
        self.assertIn('email address',self.reasons())

    def test_device_and_network_details(self):
        self.inject('192'+'.168'+'.1'+'.20')
        self.assertIn('IP address',self.reasons())
        self.inject(':'.join(['a1','b2','c3','d4','e5','f6']))
        self.assertIn('device address',self.reasons())

    def test_live_token(self):
        self.inject('gh'+'p_'+'a'*30)
        self.assertIn('access token',self.reasons())

    def test_private_key(self):
        self.inject('-----BEGIN '+'RSA '+'PRIVATE '+'KEY-----')
        self.assertIn('private key',self.reasons())

    def test_source_symbols_and_https_are_not_private_paths(self):
        self.inject('main@warzone.gsc https://github.com/example/project')
        self.assertEqual(set(),self.reasons())

    def test_root_as_a_technical_noun_is_not_a_home_path(self):
        self.inject('Args are map/root and the free-cursor/root/waiting guards.')
        self.assertEqual(set(),self.reasons())

    def test_bad_manifest_path(self):
        p=self.root/CHECK.MANIFEST;d=json.loads(p.read_text());d['files'][0]['path']='../outside.md';p.write_text(json.dumps(d))
        self.assertIn('missing or invalid complete manifest',self.reasons())

    def test_duplicate_manifest_path(self):
        p=self.root/CHECK.MANIFEST;d=json.loads(p.read_text());d['files'].append(d['files'][0]);p.write_text(json.dumps(d))
        self.assertIn('missing or invalid complete manifest',self.reasons())

    def test_utf8_text_required(self):
        (self.root/'README.md').write_bytes(bytes([255,254,0,0]));self.seal()
        self.assertIn('non-UTF-8 content',self.reasons())

    def git(self,*args):
        return subprocess.run(['git','-C',str(self.root),*args],check=True,capture_output=True,
                              env=dict(os.environ,GIT_AUTHOR_DATE='2026-10-19T00:00:00+0000',GIT_COMMITTER_DATE='2026-10-19T00:00:00+0000'))

    def initialize_history(self):
        self.git('init','--initial-branch=main')
        self.git('config','user.name',CHECK.PROJECT_NAME)
        self.git('config','user.email',CHECK.PROJECT_EMAIL)
        self.git('config','commit.gpgsign','false')

    def commit(self):
        self.git('add','--all');self.git('commit','--no-verify','--no-gpg-sign','-m','Research fixture')

    def test_clean_multiple_commit_history(self):
        self.initialize_history();self.commit()
        self.inject('Safe second version.');self.commit()
        errors,info=CHECK.git_findings(self.root)
        self.assertEqual([],errors);self.assertEqual(2,info['commit_count'])

    def test_deleted_private_content_is_still_found_in_history(self):
        self.initialize_history();self.inject('someone'+'@'+'example.net');self.commit()
        self.inject('Clean current file.');self.commit()
        errors,_=CHECK.git_findings(self.root)
        self.assertIn('private pattern in reachable historical file',{row['reason'] for row in errors})

    def test_personal_commit_identity_is_rejected(self):
        self.initialize_history();self.git('config','user.email','someone'+'@'+'example.net');self.commit()
        errors,_=CHECK.git_findings(self.root)
        self.assertIn('nonproject commit identity or time-zone metadata',{row['reason'] for row in errors})


if __name__=='__main__':unittest.main()
