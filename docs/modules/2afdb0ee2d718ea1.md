# hashed/e9ea260741b7624.lua

Project-added notes. See the [code](../../src/lua/hashed/e9ea260741b7624.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `9ba23824e112e0b47ab58090a2557074ad32b28e3831db73ef936e9d761c93a3`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/2afdb0ee2d718ea1.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua-follow3:274` (original lines 9-44, 9-44, 10-10, 16-16, 28-28, 35-35, 9-44): Creates CoD.SpawnSelectTeamStatus using LUI.UIElement.new( f1_arg2, f1_arg3, f1_arg4, f1_arg5, f1_arg6, f1_arg7, f1_arg8, f1_arg9 ). Initializes and attaches children in source order: TeamStatusList. Defines 2 separate closure scopes; their model/event/table bindings and their own ordered writes/returns are retained, not flattened into construction. TeamStatusList uses Clients; clientCount and showSpawnSelect callbacks refresh its data source. Returns self after the shown optional hooks and setup. Native UI/model/asset effects and callback delivery are external contracts.

  unknowns: &#91;"Original PS4/source match, original Lua bytecode and VM/decompiler fidelity remain unverified.", "Effective enum/dvar/settings, assets/localization/model/DDL/storage/playlist data remain exact external inputs; requested persistence/network/service effects are not successful execution proof.", "A field/method/import/spelling or other-file local alone does not bind a provider. Unknown identities remain unresolved rather than declared unavailable.", "Native model/event/timer/wrapper invocation, delivery, error/cleanup/lifetime and unavailable original server behavior are outside this source packet.", "No independent correctness review, acceptance, original-build or function-completion credit is recorded."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/2afdb0ee2d718ea1-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/2afdb0ee2d718ea1.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00003` at JSON pointer `/units/273`; file SHA-256 `a63852530df9189721a410c240a42967af6648aa0fca4e70325b17a1e677ebb7`; selected record SHA-256 `8db149e0244e5ce17663f3ed954fbe52041b82e3e450e6fcb5d44ed7a0b3d5e1`.
