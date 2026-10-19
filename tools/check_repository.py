"""Check repository structure and provenance without executing research code.

This is a bounded record/hygiene check. It cannot decide legal sufficiency,
semantic correctness, complete secret absence, or behavior of the real game.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys
from urllib.parse import unquote, urlsplit

EXCLUDED = {".git", ".local", ".venv", "__pycache__", ".pytest_cache"}
FORBIDDEN = {".bin", ".elf", ".self", ".sprx", ".prx", ".pkg", ".pup", ".dmp",
             ".pcap", ".pcapng", ".gscc", ".cscc", ".luac", ".zip", ".7z"}
STATUSES = {"declared_mit", "declared_gpl_v3", "declared_dual_with_dependencies",
            "declared_apache_with_notice", "no_explicit_grant_found",
            "ambiguous_notice", "conflicting_notices", "identity_unresolved"}
SHA256 = re.compile(r"[0-9a-f]{64}\Z")
COMMIT = re.compile(r"[0-9a-f]{40}\Z")
LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")
PRIVATE_PATH = re.compile(r"(?i)(?:[a-z]:[\\/](?:users|documents and settings)[\\/]|/(?:Users|home)/)[a-z0-9_.-]+[\\/]")

# Load the checked-in scanner beside this tool, including when tests import this
# file by absolute path. Never load code from the --root evidence fixture.
_token_spec = importlib.util.spec_from_file_location(
    "hmh_source_tokens", Path(__file__).with_name("recovered_tokens.py"))
_token_module = importlib.util.module_from_spec(_token_spec)
_token_spec.loader.exec_module(_token_module)


def accepting_review(report: dict, item: dict, scope: dict) -> bool:
    """Only the explicit full-output review format can approve a new import.

    Historical span/claim reviews remain provenance, never whole-output approval.
    An ACCEPT here concerns the exact static output, not runtime or legal rights.
    """
    evidence = scope.get("independent_review")
    if not isinstance(evidence, dict):
        return False
    author, reviewer = report.get("author"), report.get("reviewer")
    subject, coverage = report.get("subject"), report.get("scope")
    return (
        report.get("schema") == "hmh-exact-output-review-v1"
        and report.get("decision") == "ACCEPT"
        and "verdict" not in report  # no competing decision fields
        and isinstance(author, str) and bool(author.strip())
        and isinstance(reviewer, str) and bool(reviewer.strip())
        and author.strip().casefold() != reviewer.strip().casefold()
        and author == scope.get("author")
        and reviewer == evidence.get("reviewer")
        and isinstance(subject, dict)
        and subject.get("path") == item.get("path")
        and subject.get("sha256") == item.get("sha256")
        and (item.get("classification") == "original_project_reconstruction"
             or subject.get("original_sha256") == item.get("original_sha256"))
        and isinstance(coverage, dict)
        and coverage.get("kind") == "whole_output"
        and coverage.get("complete") is True
        and type(coverage.get("unreviewed_units")) is int
        and coverage.get("unreviewed_units") == 0
        and coverage.get("unresolved_required") == []
    )


def check_repository(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []

    def fail(message: str) -> None:
        errors.append(message)

    def local(value: object, label: str) -> Path | None:
        if not isinstance(value, str) or not value or "\\" in value:
            fail(f"{label}: expected a nonempty POSIX relative path")
            return None
        posix = PurePosixPath(value)
        if posix.is_absolute() or ".." in posix.parts or ":" in value:
            fail(f"{label}: path escapes the repository or uses a nonlocal scheme")
            return None
        path = root.joinpath(*posix.parts)
        if not path.resolve().is_relative_to(root) or not path.is_file():
            fail(f"{label}: missing or escaping file: {value}")
            return None
        return path

    def read_json(path: Path) -> dict | None:
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(value, dict):
                raise ValueError("top level must be an object")
            return value
        except (ValueError, OSError) as exc:
            fail(f"{path.name}: invalid JSON: {exc}")
            return None

    files: list[Path] = []
    # Never follow links/reparse directories into a private evidence archive.
    for current, dirs, names in os.walk(root, followlinks=False):
        base = Path(current)
        for name in list(dirs):
            child = base / name
            if name in EXCLUDED:
                dirs.remove(name)
            elif child.is_symlink() or (hasattr(child, "is_junction") and child.is_junction()):
                fail(f"linked directory is not allowed: {child.relative_to(root)}")
                dirs.remove(name)
        for name in names:
            path = base / name
            relative = path.relative_to(root).as_posix()
            if path.is_symlink():
                fail(f"linked file is not allowed: {relative}")
                continue
            files.append(path)
            if path.suffix.lower() in FORBIDDEN or name == ".env" or name.startswith(".env.") and name != ".env.example":
                fail(f"private/binary input is not allowed: {relative}")
                continue
            if path.stat().st_size > 2 * 1024 * 1024:
                fail(f"file exceeds 2 MiB review limit: {relative}")
                continue
            try:
                content = path.read_text(encoding="utf-8")
            except (UnicodeError, OSError):
                fail(f"file is not readable UTF-8 text: {relative}")
                continue
            if "\x00" in content or PRIVATE_PATH.search(content):
                fail(f"binary content or machine-specific home path: {relative}")
            if path.suffix == ".json":
                read_json(path)
            if path.suffix == ".md":
                for match in LINK.finditer(content):
                    target = match.group(1).strip().strip("<>")
                    if target.startswith("#") or urlsplit(target).scheme:
                        continue
                    parsed = unquote(urlsplit(target).path)
                    resolved = (path.parent / parsed).resolve()
                    if not resolved.is_relative_to(root) or not resolved.exists():
                        fail(f"broken/escaping Markdown link in {relative}: {target}")

    required = ["README.md", "CREDITS.md", "LICENSE-SCOPE.md", "CONTRIBUTING.md",
                "CHANGELOG.md", "provenance/sources.json", "provenance/license-audit.json",
                "provenance/imports.json", "provenance/findings.json"]
    for name in required:
        local(name, "required file")
    if errors:
        return errors
    sources_doc = read_json(root / "provenance/sources.json")
    audit = read_json(root / "provenance/license-audit.json")
    imports_doc = read_json(root / "provenance/imports.json")
    findings_doc = read_json(root / "provenance/findings.json")
    if any(value is None for value in (sources_doc, audit, imports_doc, findings_doc)):
        return errors
    sources = sources_doc.get("sources")
    imports = imports_doc.get("imports")
    findings = findings_doc.get("findings")
    if not all(isinstance(items, list) for items in (sources, imports, findings)):
        fail("sources, imports and findings must be arrays")
        return errors
    schema = imports_doc.get("schema")
    if not isinstance(schema, str) or schema not in {"hmh-imports-v1", "hmh-imports-v2"}:
        fail("unsupported or missing import schema; explicit v2 records required")
    elif schema == "hmh-imports-v1" and imports:
        fail("nonempty legacy imports require explicit migration to validated v2 records")
    source_map = {}
    for source in sources:
        if not isinstance(source, dict):
            fail("source entries must be objects")
            continue
        identity = source.get("id")
        if not isinstance(identity, str) or not re.fullmatch(r"SRC-\d{3}", identity) or identity in source_map:
            fail(f"invalid or duplicate source ID: {identity}")
            continue
        source_map[identity] = source
        revision = source.get("revision")
        observation = source.get("license_observation")
        if observation not in STATUSES:
            fail(f"{identity}: unknown license observation")
        kind = source.get("kind", "github")
        if kind not in {"github", "local_evidence", "original_work"}:
            fail(f"{identity}: unknown source kind")
        if kind != "github":
            if revision is not None or not SHA256.fullmatch(str(source.get("fingerprint_sha256", ""))) or not source.get("attribution") or not source.get("identity"):
                fail(f"{identity}: local/original source needs identity, fingerprint, attribution and null Git revision")
            for item in source.get("evidence", []):
                p = local(item.get("record"), "local source evidence")
                if p and hashlib.sha256(p.read_bytes()).hexdigest() != item.get("sha256"):
                    fail(f"{identity}: local evidence hash mismatch")
            if not source.get("evidence"):
                fail(f"{identity}: local/original source lacks evidence")
            continue
        if revision is None:
            if observation != "identity_unresolved":
                fail(f"{identity}: missing revision without an unresolved status")
        elif not isinstance(revision, str) or not COMMIT.fullmatch(revision):
            fail(f"{identity}: revision must be an exact commit")
        repo_url = "https://github.com/" + str(source.get("repository", ""))
        if source.get("url") != repo_url or not source.get("attribution"):
            fail(f"{identity}: missing repository identity or attribution")
        evidence = source.get("evidence")
        if not isinstance(evidence, list):
            fail(f"{identity}: evidence must be an array")
            continue
        if revision is not None and not evidence:
            fail(f"{identity}: a pinned source needs evidence")
        for item in evidence:
            if not isinstance(item, dict):
                fail(f"{identity}: evidence entries must be objects")
                continue
            expected = f"{repo_url}/blob/{revision}/{item.get('upstream_path', '')}"
            if item.get("permalink") != expected:
                fail(f"{identity}: notice URL does not match its exact source identity")
            if not SHA256.fullmatch(str(item.get("sha256", ""))) or not COMMIT.fullmatch(str(item.get("expected_git_blob_sha", ""))):
                fail(f"{identity}: evidence hashes are missing or malformed")
    actual_counts = dict(Counter(s.get("license_observation") for s in source_map.values()))
    if audit.get("record_count") != len(sources) or audit.get("counts_by_observation") != actual_counts:
        fail("license audit counts do not match the source register")
    if audit.get("pinned_revision_count") != sum(s.get("revision") is not None for s in source_map.values()):
        fail("pinned revision count does not match the source register")
    third_party = sum(i.get("classification") != "original_project_reconstruction" for i in imports)
    if audit.get("third_party_files_imported") != third_party:
        fail("import count does not match the license audit")
    history = audit.get("original_preparation_audit")
    if history:
        p=local(history.get("record"), "original license audit")
        if p and hashlib.sha256(p.read_bytes()).hexdigest() != history.get("sha256"):
            fail("original license audit hash mismatch")
    imported_paths = set()
    for item in imports:
        if not isinstance(item, dict):
            fail("import entries must be objects")
            continue
        relative = item.get("path")
        path = local(relative, "import")
        if path is None:
            continue
        if relative in imported_paths:
            fail(f"duplicate import path: {relative}")
        imported_paths.add(relative)
        if hashlib.sha256(path.read_bytes()).hexdigest() != item.get("sha256"):
            fail(f"import hash mismatch: {relative}")
        source = source_map.get(item.get("source_id"))
        if not source or not item.get("source_path"):
            fail(f"import source identity is incomplete: {relative}")
        elif source.get("kind", "github") == "github":
            if not source.get("revision") or source["revision"] != item.get("source_revision"):
                fail(f"import source identity is incomplete: {relative}")
        elif item.get("source_revision") is not None or item.get("source_fingerprint_sha256") != source.get("fingerprint_sha256"):
            fail(f"local source fingerprint mismatch: {relative}")
        review_path = local(item.get("review_record"), "review scope record")
        permission_path = local(item.get("permission_record"), "sharing status record")
        # Apply the guarantees even after reporting an invalid schema. There is
        # no weaker per-record fallback for unknown or nonempty legacy formats.
        state = item.get("review_status")
        if state not in {"awaiting_independent_review", "independently_reviewed_exact_version"}:
            fail(f"invalid review state: {relative}")
        record = read_json(review_path) if review_path else None
        if record and (record.get("output") != relative or record.get("output_sha256") != item.get("sha256") or record.get("review_status") != state):
            fail(f"review scope does not bind this exact output/state: {relative}")
        if record and item.get("classification") != "original_project_reconstruction" and record.get("original_sha256") != item.get("original_sha256"):
            fail(f"review scope original hash differs: {relative}")
        if record:
            for shard in record.get("claim_shards", []) + record.get("documentation_projections", []):
                part = local(shard.get("path"), "claim shard")
                if part and hashlib.sha256(part.read_bytes()).hexdigest() != shard.get("sha256"):
                    fail(f"claim shard hash mismatch: {relative}")
        if state == "independently_reviewed_exact_version":
            evidence = record.get("independent_review", {}) if record else {}
            if not isinstance(evidence, dict):
                evidence = {}
            p = local(evidence.get("record"), "independent review")
            if not record or not record.get("author") or not evidence.get("reviewer") or evidence.get("reviewer") == record.get("author") or evidence.get("reviewed_sha256") != item.get("sha256") or not p or hashlib.sha256(p.read_bytes()).hexdigest() != evidence.get("sha256"):
                fail(f"exact independent review evidence missing: {relative}")
            report = read_json(p) if p else None
            if not report or not record or not accepting_review(report, item, record):
                fail(f"independent review decision/subject/scope/identities insufficient: {relative}")
        permission = read_json(permission_path) if permission_path else None
        if item.get("permission_status") == "not_established":
            if not permission or permission.get("rights_holder_license") is not False or permission.get("original_game_permission") != "not_established" or not permission.get("decision"):
                fail(f"unresolved sharing status needs an explicit unresolved sharing record: {relative}")
        elif item.get("permission_status") != "project_original_license_not_selected":
            fail(f"unsupported sharing state: {relative}")
        classification = item.get("classification")
        if classification not in {"modified_comments_only", "modified_comments_and_whitespace", "recovered_unmodified", "original_project_reconstruction"}:
            fail(f"invalid origin classification: {relative}")
        if classification == "original_project_reconstruction" and source and source.get("kind", "github") == "github":
            fail(f"GitHub recovered code cannot be relabeled project-original: {relative}")
        if classification != "original_project_reconstruction":
            if not SHA256.fullmatch(str(item.get("original_sha256", ""))):
                fail(f"original source hash missing: {relative}")
            elif classification == "recovered_unmodified":
                if item.get("original_sha256") != item.get("sha256"):
                    fail(f"unmodified source hash differs: {relative}")
            else:
                data = path.read_bytes()
                bom, count = item.get("original_bom_bytes"), item.get("added_header_bytes")
                if type(bom) is not int or bom not in (0, 3) or (bom == 3 and data[:3] != b"\xef\xbb\xbf") or type(count) is not int or count <= 0 or bom+count > len(data):
                    fail(f"invalid annotation boundary: {relative}")
                else:
                    header=data[bom:bom+count]
                    if b"HMH RESEARCH:" not in header or not header.endswith(b"END HMH PROJECT HEADER\n"):
                        fail(f"annotation marker missing: {relative}")
                    prefix = b"-- " if path.suffix == ".lua" else b"// "
                    if not all(line.startswith(prefix) for line in header.splitlines()):
                        fail(f"annotation contains executable/noncomment text: {relative}")
                    body=data[bom+count:]
                    delivered_body = body
                    if classification == "modified_comments_and_whitespace":
                        formatting_path=local(item.get("formatting_record"), "reversible source formatting")
                        formatting=read_json(formatting_path) if formatting_path else None
                        if formatting:
                            try:
                                lines=body.decode("utf-8").splitlines(keepends=True)
                                seen_lines=set()
                                for row in formatting["trailing_blanks"]:
                                    number=row["line"];suffix=row["suffix"]
                                    if not isinstance(number,int) or number<1 or number>len(lines) or number in seen_lines or not isinstance(suffix,str) or not re.fullmatch(r"[ \t]+",suffix):
                                        raise ValueError("bad whitespace restoration")
                                    seen_lines.add(number);line=lines[number-1];content=line.rstrip("\r\n");lines[number-1]=content+suffix+line[len(content):]
                                final=formatting["removed_final_lines"]
                                if not isinstance(final,list) or not all(isinstance(line,str) and not line.strip() for line in final):raise ValueError("bad final-line restoration")
                                body=("".join(lines)+"".join(final)).encode("utf-8")
                            except (KeyError,TypeError,ValueError,UnicodeError):
                                fail(f"invalid reversible formatting: {relative}")
                        else:
                            fail(f"reversible formatting missing: {relative}")
                    if hashlib.sha256(data[:bom]+body).hexdigest() != item["original_sha256"]:
                        fail(f"comment-only change altered original source: {relative}")
                    if classification == "modified_comments_and_whitespace":
                        try:
                            language = "lua" if path.suffix == ".lua" else "gsc"
                            if _token_module.tokens(body.decode("utf-8"), language) != _token_module.tokens(delivered_body.decode("utf-8"), language):
                                fail(f"formatting changed literal tokens: {relative}")
                        except (UnicodeError, ValueError):
                            fail(f"source literal preservation could not be checked: {relative}")
        local(item.get("documentation"), "module documentation")
        notices = item.get("notices")
        if not isinstance(notices, list) or not notices:
            fail(f"import needs applicable notice records: {relative}")
        else:
            for notice in notices:
                local(notice, "import notice")
    for path in files:
        relative = path.relative_to(root).as_posix()
        if relative.startswith("src/") and path.name != "README.md" and relative not in imported_paths:
            fail(f"source file lacks an import/provenance record: {relative}")
    subjects_path=root/"provenance/review-ready-files.json"
    if subjects_path.is_file():
        subjects=read_json(subjects_path)
        subject_paths=set()
        if subjects:
            for item in subjects.get("files", []):
                p=local(item.get("path"), "review-ready subject")
                subject_paths.add(item.get("path"))
                if p and hashlib.sha256(p.read_bytes()).hexdigest() != item.get("sha256"):
                    fail(f"review-ready subject hash mismatch: {item.get('path')}")
            if not imported_paths.issubset(subject_paths):
                fail("review-ready subjects omit imported code")
    finding_ids = set()
    for finding in findings:
        if not isinstance(finding, dict) or not isinstance(finding.get("id"), str):
            fail("finding entries need an ID")
            continue
        if finding["id"] in finding_ids:
            fail(f"duplicate finding ID: {finding['id']}")
        finding_ids.add(finding["id"])
        local(finding.get("record"), "finding record")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = check_repository(args.root)
    if errors:
        print("FAIL")
        for error in errors:
            print("- " + error)
        return 1
    print("PASS: repository records, local links and bounded hygiene checks")
    print("No game-behavior or legal-permission verdict is implied.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
