# hashed/42403f299e185fb0.lua

Project-added notes. See the [code](../../src/lua/hashed/42403f299e185fb0.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `eed18e93be4e0a9a1274d39c83e9d88621d9056bc68f46ea560bbd36d3bda82c`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/e4ce8bcbc32cff6d.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua-follow3:041` (original lines 337-337, 337-337, 337-337): Obtains the element owner, removes the first matching element from the shortcut-lock list and breaks. If the resulting list is empty it sets that owner's LockUIShortcutInput model to false. It does not clear another owner's nonempty locks. The displayed f14_local1 assignment has no local keyword; retain that source scope rather than silently correcting it. For CoD.PCUtility.ClearLockUIShortcutInputInternal, evaluate the displayed formal inputs and captured values. Its exact paths are 158: for f14_local4, f14_local5 in pairs( CoD.PCUtility.__lockUIShortcutInputList ) do; 159: if f14_local5 == f14_arg0 then; 161: break; 164: if table.getn( CoD.PCUtility.__lockUIShortcutInputList ) == 0 then. Its writes/requests begin 165: f14_local1 = Engine&#91;@"getmodelforcontroller"&#93;( f14_local0 ); 166: f14_local1.LockUIShortcutInput:set( false ). The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior. For CoD.PCUtility.UnlockUIShortcutInput, evaluate the displayed formal inputs and captured values. The exact ordered provider request below is the entire visible wrapper behavior; no opaque provider effects are invented. The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior. For CoD.PCUtility.SetForceMouseEventDispatch, evaluate the displayed formal inputs and captured values. Its writes/requests begin 3037: f295_arg0:setForceMouseEventDispatch( f295_arg1 ). The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior. For CoD.PCUtility.ActivateListPCSelectionBehavior, evaluate the displayed formal inputs and captured values. Its writes/requests begin 3070: f301_arg0.__enablePCListSelectionBehavior = true. The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior. Calls the exact hashed Engine request with the supplied argument. Its truthy result is stripped to a BattleTag name for a localized game-event success message; false/nil uses the alternate localized message. The hashed request's account/service effect is unavailable and was not executed. For CoD.PCUtility.AcceptFriendRequestWrapper, evaluate the displayed formal inputs and captured values. Its exact paths are 3143: if f313_local0 then. The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior. Gets the input text model, then evaluates the outer Engine-gate conjunction. When both gates are truthy, it reads channel data; a nonnil/nonempty channel computes name/color locals only and shows no prompt-model write. This whole outer branch returns at3832 even for nil/empty channel. The elseif3833/3836/else3839 paths are alternatives to that OUTER Engine conjunction: they request disabled/unavailable prompts and return, or request the normal prompt and then force subscription notification. No backend/provider/UI success or local recovery is proved. For CoD.PCUtility.ChatClientInputTextFieldUpdatePrompt, evaluate the displayed formal inputs and captured values. Its exact paths are 3825: if Engine&#91;@"hash_27272CF98D12ADE1"&#93;( f376_arg2 ) and Engine&#91;@"hash_189364092E497C4D"&#93;( f376_arg2 ) then; 3828: if f376_local2 ~= nil and f376_local2 ~= "" then; 3832: return; 3833: elseif not ChatClientEnabled( f376_arg2 ) then; 3835: return; 3836: elseif not ChatClientIsAvailable( f376_arg0, f376_arg1, f376_arg2 ) then; 3838: return. The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior. For CoD.PCUtility.SetupXCamMouseControlWidget, evaluate the displayed formal inputs and captured values. Its writes/requests begin 3941: f390_arg0:setupXCamMouseControl(); 3942: f390_arg0:setHandleMouse( true ). The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior. For CoD.PCUtility.SetTextFromTelemetryModel, evaluate the displayed formal inputs and captured values. Its exact paths are 4210: if not f430_arg0.Label then; 4211: return; 4214: if f430_local0 and f430_local0 > 0 then; 4216: elseif f430_arg4 and f430_arg4 ~= @"hash_0" then. Its writes/requests begin 4215: f430_arg0.Label:setText( Engine&#91;@"hash_4F9F1239CFD921FE"&#93;( f430_arg3, f430_local0 ) ); 4217: f430_arg0.Label:setText( Engine&#91;@"hash_4F9F1239CFD921FE"&#93;( f430_arg4 ) ). The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior.

  unknowns: &#91;"Original source-to-PS4/VM/native/loader identity and bytecode fidelity are unverified.", "Effective settings, assets/tables/model schemas, server/service implementation and callback delivery/lifetime are unverified.", "Exact source request semantics do not prove rendering, networking, persistence, progression or game behavior.", "Public reuse is the frozen manager audit only; no worker web/repository discovery was performed."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/e4ce8bcbc32cff6d-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/e4ce8bcbc32cff6d.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00180` at JSON pointer ``; file SHA-256 `b8837b44c23c630ca8a66476138c140ed906ff8a6f3faa928a1d2aa8f0f310db`.

- `hmh07-lua-follow8:012` (original lines 324-324, 324-324, 324-324): Exact selected canonical immediate source contracts saved below; all owned inline bodies are separate and all old units remain reused unchanged.

  unknowns: &#91;"Pinned recovered source only. No originating bytecode, source-to-PS4 match, loader/overwrite/metatable/native/VM/settings/assets/services/server or runtime-delivery proof. Author checks are not independent correctness review.", "No min/max gaps, unlisted other-file bodies, new data/writers or held OIC constructor were authored."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/e4ce8bcbc32cff6d-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/e4ce8bcbc32cff6d.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00045` at JSON pointer `/units/11`; file SHA-256 `0c981d5eb446fe3dd44845673b101548cf36172da6abd92475497ba0faf30ce0`; selected record SHA-256 `33efdacdbd074c7e905ce4807c3f0a6f86b222e49d15484a868c5242c47d13a6`.

- `hmh07-lua-follow1:156` (original lines 308-317, 375-436, 442-445, 308-317, 308-317, 308-308, 312-314, 312-312, 375-436, 375-436, 375-375, 376-378, 376-376, 380-384, 380-380, 386-393, 386-386, 394-401, 394-394, 405-423, 405-405, 427-435, 427-427, 442-445, 442-445, 442-442, 308-317, 375-436, 442-445, 308-317, 380-384, 386-393, 394-401, 405-423, 427-435, 442-445, 310-310, 300-306, 313-313, 315-315, 376-376, 380-380, 270-284, 377-377, 286-298, 382-382, 386-386, 394-394, 319-340, 388-388, 430-430, 342-355, 396-396, 432-432, 414-414, 417-417, 420-420, 309-309, 404-404, 408-408, 426-426, 443-443, 406-406, 308-317, 375-436, 442-445): PreSetup prepares CurrentNotification and sticky ownership, adding safe-area handling outside frontend. PrepareNotificationContainer attaches cooldown and100-duration polling timers, registers accept/decline actions, processes each notification-event subtype and hides a matching party invite, then subscribes to inviteResponseEvent. A visible response accepts only the literal accept string; other responses decline. IsNotificationWidgetVisible returns the raw visibility model value. Preserve opaque local polling functions and timer/native/service/cancellation gaps.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/e4ce8bcbc32cff6d-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/e4ce8bcbc32cff6d.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00452` at JSON pointer ``; file SHA-256 `f4a794d565e4edf2abf1b54c1ad0a4e93a187468b3d53abd757ed6ca6e8f891a`; selected record SHA-256 `cd7dc68471e165ce91eab038d8ebb1710f91b1c9a83a5dbc2bf8b18bf9593039`.

- `hmh07-lua-follow4:037` (original lines 202-202, 202-202, 202-202): When a menu exists it registers MOUSE1 and confirm callbacks. A busy spinner suppresses simulation; otherwise the callbacks read Button/KeyShortcut when a model exists, play DefaultClip and simulate a press. Confirm returns false for an actual cross-button binding. keyPrompt adds Button-based resizing. footerTooltip adds shortcut text conversion and a KeybindMessages.isBindingKey subscription. All callback gates and returns are retained in the nested traces; installing them does not press a button. Returns immediately off PC. On PC stores __focusNavigationElementCallback; when invoked it returns activeWidget only when present and focusable, else nil. It does not select/focus a widget during installation. Walks StickyElements with ipairs and calls MigrateSingleStickyElementsBackward with the original first argument, each element and the original second argument. It does not define migration or rollback internals. Requests Engine flashwindow with literal arguments 5, 0, 3. No platform behavior or return is demonstrated.

  unknowns: &#91;{"kind": "original_build", "gap": "Recovered-source revision is pinned; original PS4 build/byte/VM/native binding remains unverified."}, {"kind": "effective_data_settings_assets", "gap": "Engine/model/Dvar/asset/data requests do not supply effective runtime values, contents or ownership."}, {"kind": "server_service_persistence", "gap": "Unavailable authoritative server/service/provider code and successful persistence remain unavailable; not reconstructed or counted as completed."}, {"kind": "runtime_callback_lifetime", "gap": "Original loading, table overwrites, callback delivery/order, timings, state selection and UI cleanup are not runtime-proven."}&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/e4ce8bcbc32cff6d-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/e4ce8bcbc32cff6d.json) at JSON pointer `/claims/3`.

  Archived evidence ID: `archived-record-00501` at JSON pointer ``; file SHA-256 `bc30c7434fcae913d2a64dc058e37901febf93a4cad3a2a40f3c7d95dce38a39`; selected record SHA-256 `550ef0e34f3745e2d6cc745a24385af8bed3eeef72ab88c7c220da2bcfafd79a`.

- `hmh07-lua:020` (original lines 442-445, 308-317, 375-436): Starts sticky registration, prepares notification state and constructs PCNotif. Invisible is the negation of notification visibility. A CallOriginalFirst setState hook plays Out, clears __wasOpen and loses focus only when entering Invisible after being open; default state plays In and sets __wasOpen. It prepares the container, disables keyboard navigation and ends sticky registration. PC naming is not an exclusion proof; actual platform membership is conditional on caller and native availability.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used.", "Source-ready close body exists outside frozen allowed companion range; exact locator is retained in new_dependencies. Other class clip bodies not frozen were not authored.", "Additional same-class reset/clip/close body ranges are available but outside the frozen author scope; exact locators are in unfrozen_same_class_body_locators and source-frontier.json. No body authoring or completion credit for them.", "Relative original/custom execution order of OverrideFunction_CallOriginalFirst/Second requires the available helper source contract; names are preserved without deriving order from naming alone."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/e4ce8bcbc32cff6d-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/e4ce8bcbc32cff6d.json) at JSON pointer `/claims/4`.

  Archived evidence ID: `archived-record-00453` at JSON pointer ``; file SHA-256 `cde3fcdf26280f446f93c235eaf5ea2f09ab3b2d7967d0d091ff01a307d7629c`.
