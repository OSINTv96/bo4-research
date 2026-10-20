# Release process

The candidate freezes a useful research snapshot with explicit limits. New supported discoveries can be added in later updates.

## Current candidate

The first release uses a separate public tree and fresh project Git history. Publish only that checked tree or the ZIP built from its exact manifest. The full research archive and earlier private Git history are not release inputs.

Run the commands in [getting started](getting-started.md). Review [credits](../CREDITS.md), [license scope](../LICENSE-SCOPE.md), [known limits](known-gaps.md) and [privacy](privacy.md). Test the same files from a fresh checkout and a fresh archive extraction.

Each release receives independent package review before publication. Record the exact reviewed commit, scope and remaining limits in its GitHub release notes. Publish only the approved tree and verified assets. A local fresh-copy test is not a verified download from a remote release. Once uploaded, test an actual download and compare its contents to the same manifest.

The repository is intended to grow toward the whole game while the current checkpoint remains focused on HMH. Use lightweight version tags such as `v0.1.0`: they carry no personal tagger identity or message. Annotated tags require additional review and are rejected by the current privacy checker.

## Later updates

Pull-request checks inspect the submitted head commit. GitHub's temporary merge
record is excluded from that checkout; the submitted history still receives the
full privacy check. Published history continues to require the neutral project
identity and UTC commit timestamps.

Give each finding an ID, pin the changed source and evidence, obtain review of its precise claims, and describe new proof and remaining limits in the changelog. Preserve public superseded technical conclusions without importing private conversations or records.

Regenerate affected provenance hashes, complete review subjects and the release manifest after intentional changes. Check every file and all reachable Git history before making the next archive. Removing a file from the latest tree does not remove it from earlier commits.

Publication does not prove the game, close unavailable-source gaps or authorize console testing.
