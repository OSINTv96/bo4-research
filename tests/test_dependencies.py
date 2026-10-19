"""Cross-record checks for the bounded available-source dependency decisions."""
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('dependency_records',ROOT/'tools/dependency_records.py')
DEPENDENCIES=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(DEPENDENCIES)
def load(name):return json.loads((ROOT/name).read_text(encoding='utf-8'))


class DependencyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest=load('provenance/dependencies.json')
        cls.modules=list(DEPENDENCIES.load_modules(ROOT))
        cls.decisions=load('provenance/dependency-decisions.json')
        cls.imports={r['path']:r for r in load('provenance/imports.json')['imports']}

    def test_every_reviewed_available_reference_has_an_honest_decision(self):
        rows=self.decisions['decisions']
        self.assertEqual(537,len(rows))
        self.assertEqual(537,len({r['id'] for r in rows}))
        for row in rows:
            with self.subTest(id=row['id']):
                decision=load(row['record'])
                self.assertEqual('exact_pinned_local',decision['availability'])
                self.assertEqual('awaiting_independent_review',decision['review_status'])
                self.assertEqual(0,decision['runtime_credit'])
                self.assertEqual(row['decision'],decision['decision'])
                if decision['decision']=='include_conditional_source':
                    item=self.imports[decision['output']]
                    self.assertEqual(item['original_sha256'],decision['source']['sha256'])
                    self.assertTrue(decision['selected_reference_lines'])
                    self.assertEqual('conditional',decision['relevance'])
                else:
                    self.assertEqual('relevance_unresolved',decision['decision'])
                    self.assertEqual('unresolved',decision['relevance'])
                    self.assertTrue(decision['reason'])

    def test_availability_and_inclusion_are_separate_from_relevance(self):
        unresolved=0
        self.assertGreater(len(self.modules),1381)
        for module in self.modules:
            item=self.imports[module['module']]
            scope=load(item['review_record'])
            self.assertEqual(module['dependencies'],scope['dependencies'])
            for edge in module['dependencies']:
                if edge['status']=='included':self.assertIn(edge['output'],self.imports)
                if edge['source_availability']['state']=='exact_pinned_local':
                    self.assertRegex(edge['source_availability']['sha256'],r'^[0-9a-f]{64}$')
                if edge['status']=='unresolved_collection_dependency' and edge['source_availability']['state']=='exact_pinned_local':unresolved+=1
        self.assertGreater(unresolved,0)

    def test_concrete_gameadvertisement_source_and_startup_edge_are_retained(self):
        item=self.imports['src/scripts/mp_common/gameadvertisement.gsc']
        self.assertEqual('cf5b35841dbffe4f377051fd8fd88aa5248cc80800d82cc086000b22b7bd1008',item['original_sha256'])
        row=next(r for r in self.decisions['decisions'] if r['module']=='src/scripts/wz_common/gametypes/warzone.gsc' and r['identity']=='scripts/mp_common/gameadvertisement.gsc')
        decision=load(row['record'])
        call=next(w for w in decision['witnesses'] if w['caller']=='start_warzone' and w['callee']=='setadvertisedstatus')
        self.assertEqual(688,call['line'])  # reviewed output 694 includes six header lines
        self.assertEqual([],call['lexical_enclosing_blocks'])
        self.assertEqual([[36,43]],call['callee_spans'])
        self.assertEqual('include_conditional_source',decision['decision'])

    def test_extended_source_imports_have_complete_candidate_parent_paths(self):
        graph=DEPENDENCIES.load_source_paths(ROOT)
        nodes={n['id']:n for n in graph['nodes']}
        sources={(i['source_id'],i['source_path']):i for i in self.imports.values()}
        self.assertEqual(len(nodes),len(graph['nodes']))
        for node in nodes.values():
            self.assertEqual(sources[(node['source_id'],node['source_path'])]['original_sha256'],node['original_sha256'])
            seen=set();current=node
            while current['parent']:
                self.assertNotIn(current['id'],seen)
                seen.add(current['id']);current=nodes[current['parent']]
            self.assertTrue(current['entry'])
        for row in self.decisions['extension_decisions']:
            decision=load(row['record'])
            self.assertTrue(decision['incoming_graph_edges'])
            for edge in decision['incoming_graph_edges']:
                self.assertIn(edge['from'],nodes)
                target=nodes[edge['to']]
                self.assertEqual(decision['source']['source_path'],target['source_path'])
