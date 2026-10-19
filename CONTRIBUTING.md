# Contributing

The current focus is HMH and its evidenced shared dependencies. The repository is intended to grow toward the whole game through later selected research scopes. Share one copy of a shared implementation and explain its callers and conditions. See [the roadmap](ROADMAP.md).

For a new discovery:

1. Start with the [finding template](docs/templates/finding.md). State the exact
   question, source/build identity and the claim being made.
2. Check [existing sources](provenance/sources.json) and findings before repeating
   work. Preserve original names, paths, unresolved hashes and prior attributions.
3. Provide bounded evidence and reproducible checks. Separate source observations,
   recovered-code meaning, build matches and actual runtime observations.
4. Obtain review by someone who did not author the claim. Record the exact reviewed
   file hashes, reviewer, method, result and remaining limits. An author check or
   passing CI run is not independent research review.
5. Record imports and permission evidence before adding any third-party file.
   Keep original copyright/license notices and identify modifications.
6. Update the finding index, relevant notes and [changelog](CHANGELOG.md), then run
   the local checks. Never turn a missing value into an assumed answer.

Comments should explain purpose, inputs, outputs, side effects, dependencies and
uncertainty. Distinguish recovered names from later descriptive labels. Keep
long evidence discussions in linked documents rather than obscuring the code.

Do not commit account data, credentials, console addresses, packet captures,
executables, game assets, private research logs or unrecorded recovered dumps.
Local experiments belong outside this repository or in ignored `.local/`.
The checker is a limited aid, not a complete secret or copyright scanner.

Publication is ongoing. Correct or extend an older claim with a new reviewed
version, preserve why it changed, and release another snapshot when useful.


Current imports use explicit v2 provenance and review states. Keep original hashes, reversible formatting maps and upstream source paths. State unresolved sharing terms factually without adding private requests or approval messages. Preserve old span-review limits.

Before release, run both repository and release checks. Keep personal information, screenshots, transcripts and local machine details out of new files and commit metadata. Use public attribution only with consent. Changes to this frozen candidate require refreshed hashes and exact package review.
