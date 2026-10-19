# Getting started

Extract the release ZIP into an empty folder and open `README.md`. The archive has one `bo4-hmh-research` folder. A Git checkout has the same public files. No game binaries, compiled payloads or personal captures are included.

Use Python 3.13 for the tested checks. All dependencies are from the Python standard library. On Windows, `py -3.13` can replace `python` when the Python launcher is installed.

```sh
python -B tools/check_repository.py
python -B tools/check_release.py
python -B -m unittest discover -s tests -p "test_*.py"
```

Run these commands from the extracted repository folder. The first checks provenance, links and preserved source bytes. The second checks the complete file manifest and publication privacy patterns; in a Git checkout it also checks commit history. The tests exercise the local parsers, models and validators. A successful run does not prove the game or unresolved original-VM behavior.

Start reading at [the HMH entry points](architecture.md). Each recovered module has a marked project header linking to its notes. [The module index](../provenance/module-index.json) maps code, notes and records. Source paths are paths in the original game/source repositories, not paths on a researcher's computer.

An `archived-record-...` value identifies evidence that is not distributed. Its original hash and selected-claim pointer may be retained. It is not a URL or a file to look for in this download. The public notes contain excerpts; unavailable originals limit independent reproduction.

To create another ZIP of this exact candidate, choose a new output path outside the repository:

```sh
python -B tools/build_release.py --output ../hmh-research-candidate.zip
```

The builder checks the manifest first and includes only its exact files. It uses fixed archive metadata and omits Git internals. It refuses to overwrite an existing archive. After extracting a ZIP, rerun the three checks above.
