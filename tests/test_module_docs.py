"""Null fallback, full explanations and reproducible complete-set rendering."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('module_docs', ROOT/'tools/generate_module_docs.py')
DOCS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(DOCS)


class ModuleDocsTests(unittest.TestCase):
    def test_null_fields_fall_through_to_real_explanation(self):
        self.assertEqual('Real condition and limit.', DOCS.explanation({'answer':None,'behavior':None,'purpose':'Real condition and limit.'}))

    def test_no_contract_is_explicit(self):
        value = DOCS.explanation({'answer':None,'category':None})
        self.assertIn('No standalone body contract',value)
        self.assertNotIn('None',value)

    def test_long_explanation_is_not_cut_mid_condition(self):
        value = 'If enabled, '+('retain the condition; '*300)+'otherwise leave it unresolved.'
        self.assertEqual(value,DOCS.explanation({'answer':value}))

    def test_entire_document_set_matches_generator(self):
        for entry in DOCS.load(ROOT/'provenance/module-index.json')['modules']:
            with self.subTest(path=entry['documentation']):
                for path,expected in DOCS.render_pages(ROOT,entry).items():
                    actual=(ROOT/path).read_text(encoding='utf-8')
                    self.assertEqual(expected,actual)
                    self.assertLess(len(actual.encode('utf-8')),2000000)
                    self.assertNotRegex(actual,r'(?m)^- .*: None\s*$')
