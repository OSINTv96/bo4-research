# Provenance records

`sources.json` preserves the 35 original audited third-party source/version rows
and adds one explicit local-evidence/model row. Git revisions are never fabricated
for local evidence. `imports.json` v2 separates recovered, annotated and original
work, original/output hashes, pending review and sharing status.

`modules/` records exact source spans, subject/report hashes and bounded note
excerpts. Large claim sets use hashed shards under the same directory. Full
original contracts/reviews remain in the private archive and are represented here by anonymous evidence IDs and original hashes;
their exact historical selection is pinned in `evidence-index.json`.
An excerpt is not a new independent correctness decision.

`formatting/` stores reversible external-whitespace changes. No source logic,
literal value or original archived byte was changed. `module-index.json`,
`dependencies.json`, `settings-read-sites.json` and `gap-dispositions.json` give
the file, import, setting and technical-result maps. Context-only edges remain
distinct from proved required HMH dependencies.

The repair adds per-edge records in `dependency-decisions/`, a sharded complete
include/require inventory, and hashed `documentation/` projections of complete
explanatory fields from exact historical subjects. Original compact summaries and
full subjects/reviews remain unchanged. Availability and HMH relevance are separate.

[The release manifest](release-manifest.json) pins every public file except itself. [The proof summary](proof-status.json) carries current static results and four deferred limits. Private paths, author sessions and approval messages are excluded.
