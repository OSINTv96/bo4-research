# Black Ops 4 research

An ongoing reverse-engineering research project for **Call of Duty: Black Ops 4**. The long-term goal is to document the whole game. The current checkpoint focuses on **Blackout Heavy Metal Heroes (HMH)** and its evidenced shared dependencies.

The repository will grow through reviewed findings and later releases. This first snapshot is not the end of the project. See the [research roadmap](ROADMAP.md).

This research snapshot contains **289 GSC files, 88 CSC files and 1,203 Lua modules**, plus two configuration tables and one explanatory native model: **1,583 imports**. File counts describe the collection, not complete HMH coverage. This is a research reference, not a playable game or mod installer.

**Research status: PARTIAL.** Three of seven saved code-proof scopes are verified at their written static limits. Four remain unproved and deferred: SCRIPT-RAW-STATE, LUA-OBSERVATION, LUA-REPRESENTATION and SETTINGS. Conditional code findings do not prove actual game execution. See [current results and limits](docs/known-gaps.md).

## Start here

1. Read [getting started](docs/getting-started.md) and the [build identity](docs/build-target.md).
2. Open the [HMH entry points and architecture](docs/architecture.md), then follow the [module map](provenance/module-index.json).
3. Use [source settings](docs/source-settings.md), [dependencies](docs/dependencies.md) and [original/output hashes](provenance/imports.json) to trace a bounded claim.

Python **3.13** is the tested version. The checks use its standard library; no package install, game installation or network connection is needed. From this folder:

```sh
python -B tools/check_repository.py
python -B tools/check_release.py
python -B -m unittest discover -s tests -p "test_*.py"
```

These commands inspect the collection and test local helpers. They do not run the game, connect to a console, or establish missing runtime facts.

## Release contents

| Folder | Contents |
| --- | --- |
| `src/` | Recovered scripts and Lua, two tables, and a bounded native model |
| `docs/` | Entry points, module explanations, results and known limits |
| `provenance/` | Pinned sources, hashes, dependency records and anonymous archived-evidence IDs |
| `tools/`, `tests/` | Offline checks and their regression cases |

Screenshots, captures, personal information, chat transcripts, machine paths and private research files are excluded. Public upstream credits and original source identifiers remain. See [release privacy](docs/privacy.md).

Read the [release notes](RELEASE-NOTES.md), [credits](CREDITS.md), [license scope](LICENSE-SCOPE.md) and [contribution guide](CONTRIBUTING.md). Original game redistribution permission and an original-project license remain unresolved. Each release identifies its reviewed commit, validation results and remaining limits on GitHub. Package review does not prove the whole game.
