# hashed/24d5c2648fd17f7d.lua

Project-added notes. See the [code](../../src/lua/hashed/24d5c2648fd17f7d.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `74e42b3f27e4e37a52f9c1f2d6153ba457c0fe495b0684f7b42903e9e829d75d`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/b49ccea03c1caca0.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua-follow1:058` (original lines 10-86): Creates shared Director select screen with extra-home left/right filtered lists, featured playlists, mode list, safe-area/description and PC/Korea/tier-notification children. List callbacks refresh labels on lock/trial/lobby changes and descriptions on focus. Extra/mode trial-store branches containing AlwaysFalse are retained as inactive source predicates; unlocked/show-for-all/not-trial actions process the list and return true. Featured prioritizes trial store, unlocked action, missing-DLC overlay, ZM store, season-pass upsell and locked action. Mode locked action is PC-gated. Focus/lose-focus shows/hides tier notification. Safe-area menu_loaded sizes console and dispatches when unhandled. Korea event controls use exact active-event branches. State predicates distinguish live online demo/arena/default and LAN demo/arena/default. Close/postload precede pass-custom-function, UGC validation, WZ trial-video and PC redirect navigation setup. No effective playlist choice, store action, account state or native loader/runtime is asserted.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b49ccea03c1caca0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b49ccea03c1caca0.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00134` at JSON pointer ``; file SHA-256 `330362e6d7cecec92b0a68c59eacaf0e34ebedba0defd2c9c013ead274d52557`; selected record SHA-256 `62f2ac27c8417dc6be68fbf5a5a1eb6ee6b3f3e101a01cf619a0e8327c8cddf0`.

- `hmh07-lua-follow3:005` (original lines 23-23, 23-23, 23-23): Builds a focusable footer with backing/title and six perk entries. Text is localized directly for two entries and filled by bonus-credit, XP, gun-XP and merit injectors for the other four. It registers its class close callback, runs PostLoadFunc only when present, then returns the assembled widget. No purchase, grant or entitlement change is performed by these displayed text requests. Constructs CoD.Footer_IGRPerksList from the displayed menu/controller/layout arguments. Creates Backing as CoD.IGRPerksListBacking.new, Title as CoD.IGRPerksListTitle.new, IGRPerk4 as CoD.IGRPerkElement.new, IGRPerk as CoD.IGRPerkElement.new, IGRPerk3 as CoD.IGRPerkElement.new, IGRPerk2 as CoD.IGRPerkElement.new, IGRPerk6 as CoD.IGRPerkElement.new, IGRPerk5 as CoD.IGRPerkElement.new. Installs 1 event/action/override bindings; each callback keeps its captured controller/menu/widget references and executes only on its bound delivery. The ordered effect contract retains every property, model, visual, navigation, callback and return mutation in source order; returning self is not proof the original game loads this widget.

  unknowns: &#91;"Original source-to-PS4/VM/native/loader identity and bytecode fidelity are unverified.", "Effective settings, assets/tables/model schemas, server/service implementation and callback delivery/lifetime are unverified.", "Exact source request semantics do not prove rendering, networking, persistence, progression or game behavior.", "Public reuse is the frozen manager audit only; no worker web/repository discovery was performed."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b49ccea03c1caca0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b49ccea03c1caca0.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00003` at JSON pointer `/units/4`; file SHA-256 `a63852530df9189721a410c240a42967af6648aa0fca4e70325b17a1e677ebb7`; selected record SHA-256 `d92dfca218bdae60dd88e07b28c6a0c678ca5b1257a5ebdf3aca3e764d2c50ea`.

- `hmh07-lua-follow3:041` (original lines 84-84, 84-84, 84-84): Obtains the element owner, removes the first matching element from the shortcut-lock list and breaks. If the resulting list is empty it sets that owner's LockUIShortcutInput model to false. It does not clear another owner's nonempty locks. The displayed f14_local1 assignment has no local keyword; retain that source scope rather than silently correcting it. For CoD.PCUtility.ClearLockUIShortcutInputInternal, evaluate the displayed formal inputs and captured values. Its exact paths are 158: for f14_local4, f14_local5 in pairs( CoD.PCUtility.__lockUIShortcutInputList ) do; 159: if f14_local5 == f14_arg0 then; 161: break; 164: if table.getn( CoD.PCUtility.__lockUIShortcutInputList ) == 0 then. Its writes/requests begin 165: f14_local1 = Engine&#91;@"getmodelforcontroller"&#93;( f14_local0 ); 166: f14_local1.LockUIShortcutInput:set( false ). The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior. For CoD.PCUtility.UnlockUIShortcutInput, evaluate the displayed formal inputs and captured values. The exact ordered provider request below is the entire visible wrapper behavior; no opaque provider effects are invented. The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior. For CoD.PCUtility.SetForceMouseEventDispatch, evaluate the displayed formal inputs and captured values. Its writes/requests begin 3037: f295_arg0:setForceMouseEventDispatch( f295_arg1 ). The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior. For CoD.PCUtility.ActivateListPCSelectionBehavior, evaluate the displayed formal inputs and captured values. Its writes/requests begin 3070: f301_arg0.__enablePCListSelectionBehavior = true. The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior. Calls the exact hashed Engine request with the supplied argument. Its truthy result is stripped to a BattleTag name for a localized game-event success message; false/nil uses the alternate localized message. The hashed request's account/service effect is unavailable and was not executed. For CoD.PCUtility.AcceptFriendRequestWrapper, evaluate the displayed formal inputs and captured values. Its exact paths are 3143: if f313_local0 then. The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior. Gets the input text model, then evaluates the outer Engine-gate conjunction. When both gates are truthy, it reads channel data; a nonnil/nonempty channel computes name/color locals only and shows no prompt-model write. This whole outer branch returns at3832 even for nil/empty channel. The elseif3833/3836/else3839 paths are alternatives to that OUTER Engine conjunction: they request disabled/unavailable prompts and return, or request the normal prompt and then force subscription notification. No backend/provider/UI success or local recovery is proved. For CoD.PCUtility.ChatClientInputTextFieldUpdatePrompt, evaluate the displayed formal inputs and captured values. Its exact paths are 3825: if Engine&#91;@"hash_27272CF98D12ADE1"&#93;( f376_arg2 ) and Engine&#91;@"hash_189364092E497C4D"&#93;( f376_arg2 ) then; 3828: if f376_local2 ~= nil and f376_local2 ~= "" then; 3832: return; 3833: elseif not ChatClientEnabled( f376_arg2 ) then; 3835: return; 3836: elseif not ChatClientIsAvailable( f376_arg0, f376_arg1, f376_arg2 ) then; 3838: return. The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior. For CoD.PCUtility.SetupXCamMouseControlWidget, evaluate the displayed formal inputs and captured values. Its writes/requests begin 3941: f390_arg0:setupXCamMouseControl(); 3942: f390_arg0:setHandleMouse( true ). The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior. For CoD.PCUtility.SetTextFromTelemetryModel, evaluate the displayed formal inputs and captured values. Its exact paths are 4210: if not f430_arg0.Label then; 4211: return; 4214: if f430_local0 and f430_local0 > 0 then; 4216: elseif f430_arg4 and f430_arg4 ~= @"hash_0" then. Its writes/requests begin 4215: f430_arg0.Label:setText( Engine&#91;@"hash_4F9F1239CFD921FE"&#93;( f430_arg3, f430_local0 ) ); 4217: f430_arg0.Label:setText( Engine&#91;@"hash_4F9F1239CFD921FE"&#93;( f430_arg4 ) ). The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior.

  unknowns: &#91;"Original source-to-PS4/VM/native/loader identity and bytecode fidelity are unverified.", "Effective settings, assets/tables/model schemas, server/service implementation and callback delivery/lifetime are unverified.", "Exact source request semantics do not prove rendering, networking, persistence, progression or game behavior.", "Public reuse is the frozen manager audit only; no worker web/repository discovery was performed."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b49ccea03c1caca0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b49ccea03c1caca0.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00180` at JSON pointer ``; file SHA-256 `b8837b44c23c630ca8a66476138c140ed906ff8a6f3faa928a1d2aa8f0f310db`.

- `hmh07-lua-follow3:173` (original lines 71-71, 65-65, 71-71, 65-65, 71-71, 65-65): Returns the literal false. This excludes a positive result only from this exact source definition; it does not exclude other Korea utility consumers or prove the retail platform branch. Returns the opaque engine hash_2343E1D78ABC6BF1 result without converting it to a Boolean or validating its provider.

  unknowns: &#91;"Original PS4/source match, original Lua bytecode and VM/decompiler fidelity remain unverified.", "Effective enum/dvar/settings, assets/localization/model/DDL/storage/playlist data remain exact external inputs; requested persistence/network/service effects are not successful execution proof.", "A field/method/import/spelling or other-file local alone does not bind a provider. Unknown identities remain unresolved rather than declared unavailable.", "Native model/event/timer/wrapper invocation, delivery, error/cleanup/lifetime and unavailable original server behavior are outside this source packet.", "No independent correctness review, acceptance, original-build or function-completion credit is recorded."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b49ccea03c1caca0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b49ccea03c1caca0.json) at JSON pointer `/claims/3`.

  Archived evidence ID: `archived-record-00003` at JSON pointer `/units/172`; file SHA-256 `a63852530df9189721a410c240a42967af6648aa0fca4e70325b17a1e677ebb7`; selected record SHA-256 `214fb8ba6d28692d91d69025e790b23edd3321cd115ee3d940e6b99c8cece084`.
