# Available-source dependency decisions

The review found537 named references to197 distinct exact local files. These are
references and files, not proved HMH requirements. Every one of those537 references
has a [decision and source witnesses](../provenance/dependency-decisions.json).

308 edges justify conditional source inclusion through an exact caller function,
a local call/pointer chain from a selected source entry, or an executable Lua require.
The first local-trace pass added115 files; the complete candidate source graph adds84 more, for199 new files total.
The complete file is lexical context; only enumerated callees/load operations are selected.
Pointer storage does not prove delivery. Branch feasibility, settings, earlier returns,
loader behavior and actual HMH invocation remain conditional.

The other229 original edges retain unresolved relevance. Each records its available source,
namespace references, caller spans, lexical blocks, selected-claim pointers and any
local candidate trace. An include without a qualified reference cannot establish
loader/autoexec relevance. References outside a qualified entry, ambiguous local
names, unbound callees and developer regions are not promoted to requirements.
Developer-region exclusions apply only to those call slices, never the whole file.

All new whole-file includes are also inventoried. The [complete dependency inventory](../provenance/dependencies.json)
uses hashed shards; `tools/dependency_records.py` reads them. Availability is
reported separately as exact pinned local, not located in the assigned pins, or
hashed identity unresolved. Remaining exact-local includes are context/admission
questions, not evidence that engine, VM or server source is missing.

## Concrete Warzone advertisement path

The HMH recovered table names base game type `warzone`. In the recovered
`scripts/wz_common/gametypes/warzone.gsc`, `main` is annotated as a gametype-init
event handler. It registers `start_warzone` through `callback::on_game_playing`.
The source call to `gameadvertisement::setadvertisedstatus(0)` is at original688,
reviewed output694, after the infection block has closed. The call is not guarded
by that preceding infection condition. Its admission still needs the registered
game-playing callback to run; actual VM loading/delivery is not proved here.

The other calls are at original455/output461 in `function_23600e7d` (startup
population/wait-loop conditions) and original611/output617 in `function_3b0db3c2`
(stored in `level.var_86513cd0`, after the named wait). Their exact function
spans, local caller chains and blocks are retained in the edge record. Stored
pointer invocation and wait delivery remain open.

The added [callee](../src/scripts/mp_common/gameadvertisement.gsc), original36-43,
has SHA-256 `cf5b35841dbffe4f377051fd8fd88aa5248cc80800d82cc086000b22b7bd1008`.
It conditionally writes the developer diagnostic field and calls the opaque native
`changeadvertisedstatus(onoff)`. That native implementation, advertisement outcome,
original build binding and runtime effects remain unproved. Other functions in the
same module are context. No new source or runtime approval is claimed.

The [extended source graph](../provenance/source-paths.json) closes available literal
source paths from the selected static entries:5991 candidate nodes and12755 source
edges. Every added source has a recorded predecessor path to a selected entry.
All199 additions remain conditional, not199 proved HMH requirements.
All ordinary uniquely resolved non-dev source callees on this candidate graph are
included. Dynamic feasibility, constructors/classes, global/native binding,
include/autoexec and actual pointer/callback delivery remain outside that proof.
There are97 specifically recorded unresolved qualified bindings and126 exact-local
context includes without an established selected ordinary-call/load path. Their
source availability was checked; they are not relabeled missing source.
