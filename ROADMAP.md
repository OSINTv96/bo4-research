# Research roadmap

This is a continuing project toward reverse engineering and documenting the whole of Black Ops 4. Releases preserve useful checkpoints as the work develops.

## Current scope

The first public collection focuses on Blackout Heavy Metal Heroes and its evidenced shared dependencies: lifecycle, players/combat, world/circle, settings, UI and selected native interfaces. Included whole files retain context; every function is not automatically an HMH requirement.

Three of seven saved code-proof scopes are verified only at their written static limits. Four remain unproved and deferred: SCRIPT-RAW-STATE, LUA-OBSERVATION, LUA-REPRESENTATION and SETTINGS. See [the current limits](docs/known-gaps.md). Whole HMH is not complete.

## How the project grows

- Add supported findings with exact source identities, evidence and independent review.
- Extend HMH and Blackout coverage by following their actual dependencies.
- Add other game systems and modes as later research scopes are selected and supported.
- Keep unknown original VM, engine, asset and online-service behavior visible instead of replacing it with assumed implementations.
- Preserve earlier public checkpoints, explain changed conclusions and publish later snapshots.

There is no whole-game completion percentage or promised finish date. An unavailable online/server implementation remains a gap; a client-only reconstruction would not prove the whole game. This roadmap describes the repository's direction, not completed coverage or authorization for live testing.

Every update must keep personal data and private research records out of public files, commit metadata and release assets. Follow [contributing](CONTRIBUTING.md) and [the release process](docs/release-process.md).
