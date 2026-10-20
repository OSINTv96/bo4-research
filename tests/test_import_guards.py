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

    def test_pending_scope_requires_nonempty_object(self):
        self.imported_fixture()
        for value in [{}, None, [], 'scope', 1, False]:
            with self.subTest(value=value):
                self.put('provenance/scope.json', value)
                self.assertTrue(CHECK.check_repository(self.root))

    def test_pending_scope_missing_file_or_reference_fails(self):
        item = self.imported_fixture()
        (self.root/'provenance/scope.json').unlink()
        self.assertTrue(CHECK.check_repository(self.root))
        for value in [None, '', [], {}]:
            with self.subTest(value=value):
                item['review_record'] = value
                self.write_import(item)
                self.assertTrue(CHECK.check_repository(self.root))

    def test_pending_scope_binds_every_required_field(self):
        self.imported_fixture()
        scope = json.loads((self.root/'provenance/scope.json').read_text())
        for field in ['output', 'output_sha256', 'review_status', 'original_sha256']:
            for value in [None, '', 'wrong', {}, []]:
                with self.subTest(field=field, value=value):
                    changed = copy.deepcopy(scope)
                    if value is None:
                        changed.pop(field)
                    else:
                        changed[field] = value
                    self.put('provenance/scope.json', changed)
                    errors = CHECK.check_repository(self.root)
                    self.assertTrue(any('review scope' in e for e in errors), errors)

    def test_scope_shard_fields_reject_bad_types(self):
        self.imported_fixture()
        scope = json.loads((self.root/'provenance/scope.json').read_text())
        for field in ['claim_shards', 'documentation_projections']:
            for value in [None, {}, 'bad', 1, [None], ['bad'], [[]]]:
                with self.subTest(field=field, value=value):
                    changed = copy.deepcopy(scope)
                    changed[field] = value
                    self.put('provenance/scope.json', changed)
                    errors = CHECK.check_repository(self.root)
                    self.assertTrue(any('review scope' in e for e in errors), errors)

    def test_import_review_state_rejects_wrong_types(self):
        item = self.imported_fixture()
        for value in [None, '', [], {}, 1, False]:
            with self.subTest(value=value):
                item['review_status'] = value
                self.write_import(item)
                self.assertTrue(any('review state' in e for e in CHECK.check_repository(self.root)))

    def test_recovered_import_cannot_use_project_original_sharing_state(self):
        item = self.imported_fixture()
        item['permission_status'] = 'project_original_license_not_selected'
        self.write_import(item)
        for permission in [{}, {'original_project_license':'not_selected', 'decision':'Synthetic project decision'}]:
            with self.subTest(permission=permission):
                self.put('provenance/permission.json', permission)
                errors = CHECK.check_repository(self.root)
                self.assertTrue(any('requires original project reconstruction' in e for e in errors), errors)

    def original_project_fixture(self):
        item = self.imported_fixture()
        fingerprint = hashlib.sha256((self.root/'notes.md').read_bytes()).hexdigest()
        sources = json.loads((self.root/'provenance/sources.json').read_text())
        source = sources['sources'][0]
        source.update(kind='original_work', revision=None, identity='Synthetic original project fixture',
                      fingerprint_sha256=fingerprint,
                      evidence=[{'record':'notes.md', 'sha256':fingerprint}])
        self.put('provenance/sources.json', sources)
        audit = json.loads((self.root/'provenance/license-audit.json').read_text())
        audit['pinned_revision_count'] = 0
        self.put('provenance/license-audit.json', audit)
        item.update(classification='original_project_reconstruction', source_revision=None,
                    source_fingerprint_sha256=fingerprint,
                    permission_status='project_original_license_not_selected')
        item.pop('original_sha256')
        self.write_import(item)
        scope = json.loads((self.root/'provenance/scope.json').read_text())
        scope.pop('original_sha256')
        self.put('provenance/scope.json', scope)
        self.put('provenance/permission.json',
                 {'original_project_license':'not_selected', 'decision':'Synthetic project license remains unselected.'})
        return item

    def test_original_project_with_explicit_unselected_license_passes(self):
        self.original_project_fixture()
        self.assertEqual([], CHECK.check_repository(self.root))

    def test_original_project_needs_explicit_license_record(self):
        self.original_project_fixture()
        valid = json.loads((self.root/'provenance/permission.json').read_text())
        for field in ['original_project_license', 'decision']:
            for value in [None, '', ' ', [], {}, 1, False]:
                with self.subTest(field=field, value=value):
                    changed = copy.deepcopy(valid)
                    if value is None:
                        changed.pop(field)
                    else:
                        changed[field] = value
                    self.put('provenance/permission.json', changed)
                    errors = CHECK.check_repository(self.root)
                    self.assertTrue(any('explicit unselected license record' in e for e in errors), errors)
        for value in [{}, None, [], 'permission', 1, False]:
            with self.subTest(record=value):
                self.put('provenance/permission.json', value)
                self.assertTrue(CHECK.check_repository(self.root))
        (self.root/'provenance/permission.json').unlink()
        self.assertTrue(CHECK.check_repository(self.root))

    def test_unresolved_sharing_decision_must_be_nonempty_text(self):
        self.imported_fixture()
        permission = json.loads((self.root/'provenance/permission.json').read_text())
        for value in [None, '', ' ', [], {}, 1, True]:
            with self.subTest(value=value):
                permission['decision'] = value
                self.put('provenance/permission.json', permission)
                self.assertTrue(any('explicit unresolved sharing' in e for e in CHECK.check_repository(self.root)))

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
