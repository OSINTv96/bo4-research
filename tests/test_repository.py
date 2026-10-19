"""Exercise publication mistakes in disposable copies, never real evidence."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("repository_check", ROOT / "tools/check_repository.py")
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


class RepositoryCheckTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="hmh-layout-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo"
        self.root.mkdir()
        # Tiny disposable fixture: copying the full game collection per negative
        # test would obscure the checker mistake each case is meant to exercise.
        for name in ["README.md", "CREDITS.md", "LICENSE-SCOPE.md", "CONTRIBUTING.md", "CHANGELOG.md"]:
            (self.root / name).write_text("fixture\n", encoding="utf-8")
        (self.root / "provenance").mkdir()
        source = json.loads((ROOT / "provenance/sources.json").read_text())["sources"][0]
        (self.root / "provenance/sources.json").write_text(json.dumps({"sources": [source]}))
        audit = {"record_count": 1, "counts_by_observation": {source["license_observation"]: 1}, "pinned_revision_count": 1, "third_party_files_imported": 0}
        (self.root / "provenance/license-audit.json").write_text(json.dumps(audit))
        (self.root / "provenance/imports.json").write_text(json.dumps({"schema": "hmh-imports-v2", "imports": []}))
        (self.root / "provenance/findings.json").write_text(json.dumps({"findings": []}))
        (self.root / "src/scripts").mkdir(parents=True)

    def test_clean_snapshot_passes(self):
        self.assertEqual([], CHECK.check_repository(self.root))

    def test_actual_collection_passes(self):
        self.assertEqual([], CHECK.check_repository(ROOT))

    def imported_fixture(self):
        import hashlib
        original=b"function test() {}\n"
        header=b"// HMH RESEARCH: fixture\n// END HMH PROJECT HEADER\n"
        data=header+original
        sha=lambda value:hashlib.sha256(value).hexdigest()
        (self.root/"src/scripts/fixture.gsc").write_bytes(data)
        (self.root/"notes.md").write_text("fixture")
        record={"output":"src/scripts/fixture.gsc","output_sha256":sha(data),"original_sha256":sha(original),"review_status":"awaiting_independent_review"}
        (self.root/"provenance/scope.json").write_text(json.dumps(record))
        permission={"decision":"Synthetic fixture only", "rights_holder_license":False,"original_game_permission":"not_established"}
        (self.root/"provenance/permission.json").write_text(json.dumps(permission))
        source=json.loads((self.root/"provenance/sources.json").read_text())["sources"][0]
        item={"path":"src/scripts/fixture.gsc","sha256":sha(data),"original_sha256":sha(original),"source_id":source["id"],"source_revision":source["revision"],"source_path":"fixture.gsc","classification":"modified_comments_only","original_bom_bytes":0,"added_header_bytes":len(header),"review_status":"awaiting_independent_review","review_record":"provenance/scope.json","permission_status":"not_established","permission_record":"provenance/permission.json","notices":["CREDITS.md"],"documentation":"notes.md"}
        self.write_import(item)
        return item

    def write_import(self,item):
        (self.root/"provenance/imports.json").write_text(json.dumps({"schema":"hmh-imports-v2","imports":[item]}))
        path=self.root/"provenance/license-audit.json";audit=json.loads(path.read_text());audit["third_party_files_imported"]=int(item.get("classification")!="original_project_reconstruction");path.write_text(json.dumps(audit))

    def test_pending_local_inclusion_is_honest_and_allowed(self):
        self.imported_fixture();self.assertEqual([],CHECK.check_repository(self.root))

    def test_old_review_cannot_approve_new_output(self):
        item=self.imported_fixture();item["review_status"]="independently_reviewed_exact_version";self.write_import(item)
        self.assertTrue(any("independent review" in x or "exact output/state" in x for x in CHECK.check_repository(self.root)))

    def test_comment_only_record_rejects_changed_game_logic(self):
        item=self.imported_fixture();item["original_sha256"]="1"*64;self.write_import(item)
        self.assertTrue(any("altered original source" in x for x in CHECK.check_repository(self.root)))

    def test_false_license_claim_is_rejected(self):
        self.imported_fixture();p=self.root/"provenance/permission.json";v=json.loads(p.read_text());v["rights_holder_license"]=True;p.write_text(json.dumps(v))
        self.assertTrue(any("explicit unresolved sharing" in x for x in CHECK.check_repository(self.root)))

    def test_recovered_code_cannot_be_relabelled_original(self):
        item=self.imported_fixture();item["classification"]="original_project_reconstruction";self.write_import(item)
        self.assertTrue(any("relabeled project-original" in x for x in CHECK.check_repository(self.root)))

    def test_comment_header_cannot_hide_executable_code(self):
        import hashlib
        item=self.imported_fixture();p=self.root/item['path'];old=p.read_bytes();injected=b'function hidden() {}\n';data=injected+old;p.write_bytes(data)
        item['added_header_bytes']+=len(injected);item['sha256']=hashlib.sha256(data).hexdigest();self.write_import(item)
        p=self.root/item['review_record'];v=json.loads(p.read_text());v['output_sha256']=item['sha256'];p.write_text(json.dumps(v))
        self.assertTrue(any('noncomment text' in x for x in CHECK.check_repository(self.root)))

    def test_false_whitespace_map_cannot_change_source(self):
        item=self.imported_fixture();item['classification']='modified_comments_and_whitespace';item['formatting_record']='provenance/format.json';self.write_import(item)
        (self.root/'provenance/format.json').write_text(json.dumps({'trailing_blanks':[{'line':1,'suffix':'EXECUTABLE'}],'removed_final_lines':[]}))
        self.assertTrue(any('invalid reversible formatting' in x for x in CHECK.check_repository(self.root)))

    def test_changed_claim_shard_is_rejected(self):
        item=self.imported_fixture();p=self.root/item['review_record'];v=json.loads(p.read_text());v['claim_shards']=[{'path':'provenance/claims.json','sha256':'1'*64}];p.write_text(json.dumps(v));(self.root/'provenance/claims.json').write_text('{}')
        self.assertTrue(any('shard hash mismatch' in x for x in CHECK.check_repository(self.root)))

    def test_unregistered_source_is_rejected(self):
        (self.root / "src/scripts/unapproved.gsc").write_text("// disposable test fixture\n", encoding="utf-8")
        self.assertTrue(any("lacks an import" in e for e in CHECK.check_repository(self.root)))

    def test_broken_document_link_is_rejected(self):
        with (self.root / "README.md").open("a", encoding="utf-8") as handle:
            handle.write("\n[missing](missing-document.md)\n")
        self.assertTrue(any("broken/escaping Markdown link" in e for e in CHECK.check_repository(self.root)))

    def test_changed_revision_cannot_keep_old_notice_identity(self):
        path = self.root / "provenance/sources.json"
        value = json.loads(path.read_text(encoding="utf-8"))
        value["sources"][0]["revision"] = "0" * 40
        path.write_text(json.dumps(value), encoding="utf-8")
        self.assertTrue(any("notice URL does not match" in e for e in CHECK.check_repository(self.root)))

    def test_binary_input_is_rejected_even_if_gitignored(self):
        (self.root / "accidental.elf").write_bytes(b"fixture")
        self.assertTrue(any("private/binary input" in e for e in CHECK.check_repository(self.root)))

    def test_escape_in_import_record_is_rejected(self):
        path = self.root / "provenance/imports.json"
        path.write_text(json.dumps({"imports": [{"path": "../outside.txt"}]}), encoding="utf-8")
        self.assertTrue(any("path escapes" in e for e in CHECK.check_repository(self.root)))

    def test_machine_home_path_is_rejected(self):
        path = "Q:" + "/Us" + "ers/example/private.txt"
        (self.root / "accidental.md").write_text(path, encoding="utf-8")
        self.assertTrue(any("machine-specific home path" in e for e in CHECK.check_repository(self.root)))


if __name__ == "__main__":
    unittest.main()
