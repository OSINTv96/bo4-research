# Collection architecture

The source entry candidates include
[HMH item fixups](../src/scripts/wz_common/wz_common_mode_heavy_metal_heroes_fixup.gsc),
[the client fixup](../src/scripts/wz_common/wz_common_mode_heavy_metal_heroes_fixup.csc),
[shared Heavy Metal rules](../src/scripts/wz_common/wz_common_mode_heavy_metal_fixup.gsc)
and [Warzone lifecycle](../src/scripts/wz_common/gametypes/warzone.gsc).
The HMH fixup checks the named `wzheavymetalheroes` setting and changes item
replacement lists. Its autoexec entry registers source behavior; this is not
proof that the exact retail VM executed that path.

The collection follows the exact accepted HMH08 claim selections into lifecycle,
players/combat, inventory, world/circle, shared systems and UI/model callbacks.
The current collection contains 289 GSC files and 88 CSC files (377 script
modules), plus 1203 Lua modules: 1580 code modules total. Two recovered
configuration tables and one project-authored native data-path model bring the
total to 1583 imports. The original selected collection contained 1381 code
modules (202 GSC, 76 CSC and 1103 Lua); 199 later conditional source additions
account for the increase. Inclusion does not establish HMH invocation or runtime
coverage.
Each module's project header links to its notes. The
[module index](../provenance/module-index.json) maps paths to the exact source,
original hash, annotated output and bounded claim/review references.

| Folder | Material and mapping |
| --- | --- |
| `src/scripts` | Paths below original `scripts/`; unresolved `hashed/script` paths are preserved explicitly below this root |
| `src/lua` | Paths below original `lua/`; unresolved original `hashed/` modules retain that directory |
| `src/ui` | Paths below original `ui/`, with no extra `ui` or `lua` wrapper |
| `src/config` | Original textual gametype-table paths |
| `src/native` | Newly authored, explicitly bounded executable model |
| `docs/native` | Native explanation and limits, separate from game implementations |

Complete modules preserve classes, imports, callback registration, original
comments and lexical context. Only exact listed spans/claims reuse old review.
Other-mode and excluded branches remain context; file inclusion does not promote
them to HMH behavior. No shared original identity is copied into several mode
folders. The identical sound GSC/CSC pair retains its two original execution-side
identities; identical bytes alone do not merge server and client loading.

The [dependency manifest](../provenance/dependencies.json) inventories syntactic
includes/requires, not a complete HMH runtime graph. Unincluded whole-file imports
remain context dependencies, not automatically missing required HMH behavior.
Accepted per-unit records retain callback, caller, gate and opaque-provider limits.
Unavailable engine, VM, assets and services are not replaced with empty stubs.

New comment headers are marked. External trailing blanks were removed with exact
reversible maps; literal tokens were checked unchanged in all 1580 current code
modules. The 1381 original code outputs also retain their earlier output hashes.
Original hashes are separate from output hashes. Source/provenance Git attributes
preserve hashed newline bytes while retaining normal whitespace checks. This lets
the checker reconstruct original source without changing original strings.
