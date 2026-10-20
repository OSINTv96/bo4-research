# Local verification tools

`check_repository.py` validates local paths, links, file types/sizes, source
identities, import/output hashes, reversible original-source bytes, review state
and explicit sharing uncertainty. It permits honest pending local imports in
the explicit v2 schema; it does not invent independent reviews or licenses.

`recovered_tokens.py` reuses the project-authored V3 literal scanner. It ignores
comments/external whitespace while preserving literals and operators. It is not
a complete language grammar or VM equivalence checker.

`t8_formats.py` is a new bounded reader for the assigned T8 0x36 script tables.
Layout facts are attributed to ACTS `gsc_data_t8.hpp` at revision
`5d4d1ee6f7676f4529b99fc89c2382dde8b856b7`. Export flags are data, not proof of
invocation or missing functions. No third-party tool implementation is vendored.

The repaired C# Lua decoder, saved captures, binaries and internal logs stay in
the private research run. They are not included in this publication repository.

The repaired import validator explicitly accepts v2 and empty historical v1 only.
Unknown/missing schemas and nonempty v1 fail. Formatting restoration also compares
literal tokens without newline normalization; original strings remain byte-sensitive.

An approved import requires `hmh-exact-output-review-v1`: `decision: ACCEPT`, no
competing `verdict` field, `subject` with exact `path`, `sha256` and (for recovered
source) `original_sha256`; `scope` with `kind: whole_output`, `complete: true`,
integer `unreviewed_units: 0` and empty `unresolved_required`; distinct nonempty
`author` and `reviewer` matching the sidecar identities. The sidecar must pin the
report hash and reviewed output hash. This only approves exact static output.
Historical span/inventory reports remain provenance and cannot satisfy whole-output
approval. All current real imports remain pending; accepting reports in tests are
explicitly synthetic fixtures, not project approvals.

Pending imports also require nonempty review-tracking records bound to their
exact output and review state, plus the original-source hash for recovered code.
The project-original sharing
state is reserved for original project work with an explicit unselected-license
record; recovered imports retain explicit unresolved sharing records.

`generate_module_docs.py` renders all saved modules and complete explanatory
projections. Null fields cannot become None bullets, and summaries are not sliced.
`dependency_records.py` verifies and reads every hashed dependency shard. These tools
operate locally and grant no semantic/runtime/legal acceptance.

`dependency_records.py` also checks and reads every source-path graph shard. Graph nodes are candidate static paths with exact predecessor witnesses; they do not prove feasible execution or HMH runtime admission.

`check_release.py` validates the complete public manifest, every present file and reachable Git history for publication privacy. `build_release.py` creates a deterministic archive from exactly that manifest; use a new output path outside the repository. These checks do not grant independent research approval.
