# ui/uieditor/widgets/debug/lobbyprocessqueuedebug.lua

Project-added notes. See the [code](../../src/ui/uieditor/widgets/debug/lobbyprocessqueuedebug.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `1e75150f66fc673f20473d5e16f146cca312fca9ee6a4e797a82e3c01397cf68`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/5cdf43dfbd2e08ec.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua-follow2:099` (original lines 9-34, 9-34): Constructs CoD.LobbyDebugOverlay.new from its exact supplied layout/controller/menu arguments; creates/attaches LobbyProcessQueueDebug. Registers close ownership; calls PostLoadFunc only if truthy; returns self only at the displayed return. Callback/state/clip bodies are deferred, and the exact source effects below define their receiver, data and branch contracts.

  unknowns: &#91;"Exact original PS4/source version matching, recovered Lua/VM fidelity and global/native/LUI provider identity remain unverified.", "Model/storage/DDL/assets/localization/dvar/enum values, callback delivery/cancellation/error behavior, native networking and unavailable service/server code are separate inputs.", "Other-file locals are not providers by spelling. Exact qualified global declarations are source candidates until loader/table identity and caller conditions bind them.", "No implicit nil/type checks, exception recovery, timer/model disposal, idempotence or guarantee that later effects run after an error is added."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/5cdf43dfbd2e08ec-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/5cdf43dfbd2e08ec.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00028` at JSON pointer `/units/98`; file SHA-256 `2f4ecc3aabb5072135e148ef5782181882bd3b940908913a20bf258d3754185e`; selected record SHA-256 `57c396e41a4b8e992dbaac6a5e4bc2682b0418badf29f21d98187402872eb964`.

- `hmh07-lua-follow3:277` (original lines 9-34, 9-34, 10-10, 16-16, 27-27, 9-34): Creates CoD.LobbyProcessQueueDebug using LUI.UIElement.new( f1_arg2, f1_arg3, f1_arg4, f1_arg5, f1_arg6, f1_arg7, f1_arg8, f1_arg9 ). Initializes and attaches children in source order: List. Creates a debug UIList using LobbyProcessQueueInfo. Debug path naming alone is not proof exclusion from the target build. Returns self after the shown optional hooks and setup. Native UI/model/asset effects and callback delivery are external contracts.

  unknowns: &#91;"Original PS4/source match, original Lua bytecode and VM/decompiler fidelity remain unverified.", "Effective enum/dvar/settings, assets/localization/model/DDL/storage/playlist data remain exact external inputs; requested persistence/network/service effects are not successful execution proof.", "A field/method/import/spelling or other-file local alone does not bind a provider. Unknown identities remain unresolved rather than declared unavailable.", "Native model/event/timer/wrapper invocation, delivery, error/cleanup/lifetime and unavailable original server behavior are outside this source packet.", "No independent correctness review, acceptance, original-build or function-completion credit is recorded."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/5cdf43dfbd2e08ec-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/5cdf43dfbd2e08ec.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00003` at JSON pointer `/units/276`; file SHA-256 `a63852530df9189721a410c240a42967af6648aa0fca4e70325b17a1e677ebb7`; selected record SHA-256 `5930610242429384b46f3e2996102487a768ee2683ffe6db6fe872b12e64e9f3`.

Dependency decisions: [exact edge records](../../provenance/dependency-decisions.json). Included callees remain at the bounded static scopes recorded there.

- [AV0413](../../provenance/dependency-decisions/AV0413.json): `src/ui/uieditor/widgets/debug/lobbyprocessqueuedebug.lua` to `lua/ui/uieditor/widgets/debug/lobbyprocessqueuedebugitem.lua`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.
