"""Adversarial imports and valid controls; all source here is synthetic."""
import copy
import hashlib
import json
import unittest
import test_repository as fixtures

CHECK = fixtures.CHECK


class ImportGuardTests(unittest.TestCase):
    setUp = fixtures.RepositoryCheckTests.setUp
    imported_fixture = fixtures.RepositoryCheckTests.imported_fixture
    write_import = fixtures.RepositoryCheckTests.write_import

    def put(self, name, value):
        (self.root/name).write_text(json.dumps(value), encoding='utf-8')

    def test_schema_guards(self):
        item = self.imported_fixture()
        for schema in [None, '', {}, [], 2, 'unrecognized-schema', 'hmh-imports-v1']:
            with self.subTest(schema=schema):
                document = {'imports':[item]}
                if schema is not None:
                    document['schema'] = schema
                self.put('provenance/imports.json', document)
                self.assertTrue(any('schema' in e or 'legacy' in e for e in CHECK.check_repository(self.root)))

    def test_schema_downgrade_cannot_hide_other_bad_metadata(self):
        item=self.imported_fixture()
        item.pop('review_status')
        item.update(classification='unknown_origin',original_sha256='0'*64,permission_status='permission_granted_without_evidence')
        self.write_import(item)
        self.put('provenance/imports.json',{'schema':'unrecognized-schema','imports':[item]})
        errors=CHECK.check_repository(self.root)
        for message in ['schema','origin classification','sharing state','altered original source']:
            self.assertTrue(any(message in e for e in errors),errors)

    def test_empty_historical_manifest_has_explicit_validator(self):
        self.put('provenance/imports.json', {'schema':'hmh-imports-v1', 'imports':[]})
        self.assertEqual([], CHECK.check_repository(self.root))
        for schema in [None, 'future-format']:
            self.put('provenance/imports.json', {'schema':schema, 'imports':[]})
            self.assertTrue(CHECK.check_repository(self.root))

    def accepted_fixture(self):
        item = self.imported_fixture()
        item['review_status'] = 'independently_reviewed_exact_version'
        self.write_import(item)
        report = {'schema':'hmh-exact-output-review-v1', 'decision':'ACCEPT',
                  'subject':{'path':item['path'], 'sha256':item['sha256'], 'original_sha256':item['original_sha256']},
                  'scope':{'kind':'whole_output', 'complete':True, 'unreviewed_units':0, 'unresolved_required':[]},
                  'author':'fixture author', 'reviewer':'fixture reviewer'}
        scope = json.loads((self.root/'provenance/scope.json').read_text())
        scope.update(review_status=item['review_status'], author='fixture author',
                     independent_review={'record':'provenance/review.json','reviewer':'fixture reviewer','reviewed_sha256':item['sha256']})
        self.save_review(report, scope)
        return report, scope

    def save_review(self, report, scope):
        self.put('provenance/review.json', report)
        scope['independent_review']['sha256'] = hashlib.sha256((self.root/'provenance/review.json').read_bytes()).hexdigest()
        self.put('provenance/scope.json', scope)

    def test_explicit_exact_output_acceptance_passes(self):
        self.accepted_fixture()
        self.assertEqual([], CHECK.check_repository(self.root))

    def test_valid_hash_is_not_a_review_decision(self):
        report, scope = self.accepted_fixture()
        mutations = [
            ('decision','REJECT'), ('decision',None), ('schema','unknown-review'),
            ('schema',None), ('author','someone else'), ('reviewer','fixture author'),
            ('reviewer','another reviewer'), ('subject',{'path':'other.gsc','sha256':'0'*64}),
            ('subject',None), ('scope',{'kind':'span_only','complete':True}),
            ('scope',{'kind':'whole_output','complete':False,'unreviewed_units':1,'unresolved_required':[]}),
            ('scope',{'kind':'whole_output','complete':True,'unreviewed_units':0,'unresolved_required':['missing body']}),
            ('verdict','REJECT')]
        for key, value in mutations:
            with self.subTest(key=key,value=value):
                changed = copy.deepcopy(report); changed[key] = value
                self.save_review(changed, scope)
                self.assertTrue(any('review decision' in e for e in CHECK.check_repository(self.root)))

    def test_exact_review_subject_fields_cannot_change(self):
        report, scope = self.accepted_fixture()
        for key in ['sha256','original_sha256','path']:
            with self.subTest(key=key):
                changed = copy.deepcopy(report); changed['subject'][key] = 'wrong'
                self.save_review(changed, scope)
                self.assertTrue(CHECK.check_repository(self.root))

    def test_review_missing_or_sidecar_identity_mismatch_fails(self):
        report, scope = self.accepted_fixture()
        scope['independent_review']['reviewer'] = 'different reviewer'
        self.save_review(report, scope)
        self.assertTrue(CHECK.check_repository(self.root))
        (self.root/'provenance/review.json').unlink()
        self.assertTrue(CHECK.check_repository(self.root))

    def whitespace_fixture(self, original, body, mapping, lua=True):
        prior = self.root/'src/scripts/fixture.lua'
        if prior.exists():
            prior.unlink()
        item = self.imported_fixture()
        old = self.root/item['path']
        old.unlink()
        item['path'] = 'src/scripts/fixture.lua' if lua else 'src/scripts/fixture.gsc'
        header = (b'-- ' if lua else b'// ')+b'HMH RESEARCH: fixture\n'+(b'-- ' if lua else b'// ')+b'END HMH PROJECT HEADER\n'
        data = header+body
        (self.root/item['path']).write_bytes(data)
        item.update(sha256=hashlib.sha256(data).hexdigest(), original_sha256=hashlib.sha256(original).hexdigest(),
                    added_header_bytes=len(header), classification='modified_comments_and_whitespace', formatting_record='provenance/format.json')
        self.put('provenance/format.json', mapping)
        self.put('provenance/scope.json', {'output':item['path'], 'output_sha256':item['sha256'], 'original_sha256':item['original_sha256'], 'review_status':item['review_status']})
        self.write_import(item)

    def test_spaces_inside_literals_fail_even_with_restored_hash(self):
        cases = [(True,b'return [[value \n]]\n',b'return [[value\n]]\n'),
                 (True,b'return [==[value \r\n]==]\n',b'return [==[value\r\n]==]\n'),
                 (True,b'return "value \nend"\n',b'return "value\nend"\n'),
                 (True,b'return "escaped \\\nend"\n',b'return "escaped\\\nend"\n'),
                 (False,b'return "value \r\nend";\n',b'return "value\r\nend";\n')]
        for lua, original, body in cases:
            with self.subTest(original=original):
                self.whitespace_fixture(original, body, {'trailing_blanks':[{'line':1,'suffix':' '}],'removed_final_lines':[]}, lua)
                errors = CHECK.check_repository(self.root)
                self.assertTrue(any('literal tokens' in e for e in errors), errors)

    def test_external_cleanup_with_literals_and_comments_passes(self):
        for lua in [True, False]:
            with self.subTest(lua=lua):
                body = b'return "a \\" b";\n' if not lua else b'return [=[value \r\n]=], "quote \\" b"\n'
                original = body.rstrip(b'\n')+b' \t\n\n'
                line = len(body.splitlines())
                self.whitespace_fixture(original, body, {'trailing_blanks':[{'line':line,'suffix':' \t'}],'removed_final_lines':['\n']}, lua)
                self.assertEqual([], CHECK.check_repository(self.root))

    def test_newline_difference_in_literal_fails_byte_restoration(self):
        self.whitespace_fixture(b'return [[a\r\nb]]\n',b'return [[a\nb]]\n',{'trailing_blanks':[],'removed_final_lines':[]})
        self.assertTrue(any('altered original source' in e for e in CHECK.check_repository(self.root)))

    def test_multiline_literal_cannot_be_hidden_in_comment_header(self):
        item = self.imported_fixture()
        p = self.root/item['path']; data = p.read_bytes().replace(b'// HMH',b'/* HMH')
        p.write_bytes(data); item['sha256'] = hashlib.sha256(data).hexdigest(); self.write_import(item)
        record = json.loads((self.root/'provenance/scope.json').read_text());record['output_sha256']=item['sha256'];self.put('provenance/scope.json',record)
        self.assertTrue(any('noncomment text' in e for e in CHECK.check_repository(self.root)))

    def test_header_cannot_split_original_code_using_a_fake_bom(self):
        item=self.imported_fixture();item['original_bom_bytes']=3;self.write_import(item)
        self.assertTrue(any('annotation boundary' in e for e in CHECK.check_repository(self.root)))
