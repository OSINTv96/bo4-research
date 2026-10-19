# ui/uieditor/widgets/scoreboard/tabbedscoreboardheaderscores.lua

Project-added notes. See the [code](../../src/ui/uieditor/widgets/scoreboard/tabbedscoreboardheaderscores.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `5d7fc1f077132f5b38089d5c0ef8116817933bcdbd8cdf6c8261db0e68feac54`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/fd10c0f28dfcf0ea.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua-follow6:172` (original lines 187-192, 187-187, 130-130, 8-8, 14-14, 187-192, 187-187, 188-188, 189-189, 190-190, 191-191, 192-192, 188-188, 189-189, 190-190, 191-191, 187-192, 188-188, 189-189, 190-190, 191-191, 187-192): Takes the CoD.TabbedScoreboardHeaderScores instance as f16_arg0. Calls close() with each child as implicit self, in this exact order: FriendlyKills, FriendlyControlRoundPips, EnemyControlRoundPips, EnemyKills. There are no guards, branches, loops, explicit return values, field resets, timer cancellation or protected error handling in this body. Missing/already-closed children are not checked; an earlier receiver/provider error may prevent later closes. The same constructor sets this exact class and registers self.__onClose with CallOriginalSecond. That helper controls wrapping/order/invocation; registration alone does not prove game-time delivery.

  unknowns: &#91;"Effective HMH settings/data/assets, true load/overwrite/class lookup order, original recovered-text fidelity, native callback delivery and service/server implementations remain open.", "Independent correctness review and final game tests remain deferred."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/fd10c0f28dfcf0ea-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fd10c0f28dfcf0ea.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00056` at JSON pointer `/units/171`; file SHA-256 `9b5470295d8bc5b945061358d29d8430f5da2392ccde6abf20deb11b8b9c027f`; selected record SHA-256 `80a031af8eefc795d6a258a1e201e68173fdf9af760cb2994e38468af2bf15e8`.

- `hmh07-lua-follow4:010` (original lines 11-137): Builds the tabbed scoreboard header with team/enemy backings, faction colors/icons, names, game timer and scores. Each nonnil model callback updates its own visual field. FFAType and Codcaster are stored state predicates; factions.isCoDCaster delivery requests state validation. Creates self via LUI.UIElement.new, BlurBG via LUI.UIImage.new, TintBot via LUI.UIImage.new, TintBody via LUI.UIImage.new, TintTop via LUI.UIImage.new, EnemyBacking via CoD.TabbedScoreboardHeaderEnemy.new, TeamBacking via CoD.TabbedScoreboardHeaderTeam.new, YourTeamTopBar via CoD.TabbedScoreboardHeaderTopbar.new, EnemyTeamTopBar via CoD.TabbedScoreboardHeaderTopbar02.new, EnemyTeamLine via LUI.UIImage.new, YourTeamLine via LUI.UIImage.new, GameTimer00 via LUI.UIText.new, EnemyIcon via LUI.UIImage.new, CodcasterTeam2Logo via LUI.UIImage.new, YourTeamIcon via LUI.UIImage.new, CodcasterTeam1Logo via LUI.UIImage.new, VS via LUI.UIText.new, GameTypeText via LUI.UIText.new, TimeText via LUI.UIText.new, TabbedScoreboardHeaderScores via CoD.TabbedScoreboardHeaderScores.new, GameType via CoD.TabbedScoreboardHeaderTitle.new, CodCasterTeam1Name via LUI.UIText.new, CodCasterTeam2Name via LUI.UIText.new. Stores state predicates FFAType, Codcaster; their body effects require state-system evaluation.

  unknowns: &#91;{"kind": "original_build", "gap": "Recovered-source revision is pinned; original PS4 build/byte/VM/native binding remains unverified."}, {"kind": "effective_data_settings_assets", "gap": "Engine/model/Dvar/asset/data requests do not supply effective runtime values, contents or ownership."}, {"kind": "server_service_persistence", "gap": "Unavailable authoritative server/service/provider code and successful persistence remain unavailable; not reconstructed or counted as completed."}, {"kind": "runtime_callback_lifetime", "gap": "Original loading, table overwrites, callback delivery/order, timings, state selection and UI cleanup are not runtime-proven."}&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/fd10c0f28dfcf0ea-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fd10c0f28dfcf0ea.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00004` at JSON pointer `/units/9`; file SHA-256 `52df95eaa9f17f90427f6313acbc648c9bdffa0602f6444566bbe8fa1a54ba59`; selected record SHA-256 `360ecebb4fc8675e15b3464fcf181389fb3dd64e8932a26ec708ee094f0e9b54`.

- `hmh07-lua-follow6:073` (original lines 20-20, 20-20): Create self using LUI.UIElement.new( f1_arg2, f1_arg3, f1_arg4, f1_arg5, f1_arg6, f1_arg7, f1_arg8, f1_arg9 ) --&#91;&#91; @ 0&#93;&#93;. Set its exact class/id/sound and attach the child fields in source order: FriendlyKills. Create right-aligned FriendlyKills stencil text, width157. Nonnil factionScore link updates its text; close hook then optional PostLoadFunc. The ordered source statements, branch matrix and callback records below preserve each geometry, material, model path and guard. Return self after the literal final setup; native rendering and callback delivery remain open.

  unknowns: &#91;"Exact original source/build match and loader/table/global overwrite order", "Effective settings/storage/table/profile/model values", "Native render/model/event/timer lifetime and delivery", "Unavailable service/server behavior and final HMH membership"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/fd10c0f28dfcf0ea-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fd10c0f28dfcf0ea.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00056` at JSON pointer `/units/72`; file SHA-256 `9b5470295d8bc5b945061358d29d8430f5da2392ccde6abf20deb11b8b9c027f`; selected record SHA-256 `31b90e80add3015dc13b3812227189fe373dcda84107295a4b9a190027c83ffa`.

- `hmh07-lua-follow6:090` (original lines 118-118, 118-118, 124-124, 124-124): Read native roundWinLimit setting and return true only for nonnil value >0 and <=4; otherwise false. The actual HMH setting remains unknown. Return true if HUDUtility.IsGameTypeEqualToString("escort") or, after short circuit, "ctf"; otherwise false. No HMH exclusion follows from the name alone.

  unknowns: &#91;"Exact original source/build match and loader/table/global overwrite order", "Effective settings/storage/table/profile/model values", "Native render/model/event/timer lifetime and delivery", "Unavailable service/server behavior and final HMH membership"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/fd10c0f28dfcf0ea-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fd10c0f28dfcf0ea.json) at JSON pointer `/claims/3`.

  Archived evidence ID: `archived-record-00056` at JSON pointer `/units/89`; file SHA-256 `9b5470295d8bc5b945061358d29d8430f5da2392ccde6abf20deb11b8b9c027f`; selected record SHA-256 `1d4873b7902935c56f580945e3bc0fffedd5218a9b01b4f30217561fafcd0b3c`.

- `hmh07-lua-follow6:072` (original lines 104-104, 104-104): Create self using LUI.UIElement.new( f1_arg2, f1_arg3, f1_arg4, f1_arg5, f1_arg6, f1_arg7, f1_arg8, f1_arg9 ) --&#91;&#91; @ 0&#93;&#93;. Set its exact class/id/sound and attach the child fields in source order: EnemyKills. Create left-aligned EnemyKills stencil text. Nonnil factionScore model updates its text; close hook then optional PostLoadFunc. The selected direct statements contain no score-calculation or remote-synchronization request. Child/provider and optional unresolved PostLoadFunc effects remain unknown. The ordered source statements, branch matrix and callback records below preserve each geometry, material, model path and guard. Return self after the literal final setup; native rendering and callback delivery remain open.

  unknowns: &#91;"Exact original source/build match and loader/table/global overwrite order", "Effective settings/storage/table/profile/model values", "Native render/model/event/timer lifetime and delivery", "Unavailable service/server behavior and final HMH membership"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/fd10c0f28dfcf0ea-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fd10c0f28dfcf0ea.json) at JSON pointer `/claims/4`.

  Archived evidence ID: `archived-record-00492` at JSON pointer ``; file SHA-256 `dc504dfb664a416f5199380f59ed2828a4300e2c83099f8226f5c43a5967c328`; selected record SHA-256 `a5d4fbc24d2f33cd5f952c79b1a6aceb5a60de9794b0a27943d899129ad56723`.

Dependency decisions: [exact edge records](../../provenance/dependency-decisions.json). Included callees remain at the bounded static scopes recorded there.

- [AV0391](../../provenance/dependency-decisions/AV0391.json): `src/ui/uieditor/widgets/scoreboard/tabbedscoreboardheaderscores.lua` to `lua/ui/uieditor/widgets/hud/gameendscore/gameendscoreroundpip.lua`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.
