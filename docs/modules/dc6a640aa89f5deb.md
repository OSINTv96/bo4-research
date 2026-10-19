# hashed/470d4f45560b4be1.lua

Project-added notes. See the [code](../../src/lua/hashed/470d4f45560b4be1.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `9e76233d669e339c3f554cdd2df0dd4d39073fc389ca265f92ada31d50b38fbb`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/dc6a640aa89f5deb.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua-follow2:182` (original lines 96-96, 96-96, 101-101, 289-289, 293-293, 101-101, 289-289, 293-293): The constructor requests the team-ranking panel and PlaceLabel:setText with the result of Engine&#91;@"hash_4F9F1239CFD921FE"&#93;(@"ui/you_placed"). It registers a GameScore.teamRanking subscription. Only when that callback is delivered, model:get() returns a nonnil value (including false), and earlier evaluation succeeds does it request LocalizeStringWithParameter(@"ui/warzone_placement",value), then TeamRank:setText with the result. The supplied helper576–578 forwards those arguments to the same opaque Engine hash. Actual returned text, formatting, localization, rendering, provider behavior and delivery remain unknown; a literal displayed YOU PLACED label is not established.

  unknowns: &#91;"Original PS4/source exact-version and original Lua/VM binding remain unverified.", "Effective enum/mode/platform/settings and asset/model/storage data are unavailable.", "Native/LUI event/subscription/timer dispatch, cleanup guarantees and errors not shown in selected source remain open.", "Unavailable service/server code is not reconstructed or counted."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/dc6a640aa89f5deb-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/dc6a640aa89f5deb.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00546` at JSON pointer ``; file SHA-256 `1362fea991c6c6ffc8a9d0c3a1a314d5230eac32b9b05b3955fe88f84f424d7c`.

- `hmh07-lua-follow1:045` (original lines 10-294, 101-101, 289-289, 293-293, 10-294, 10-294, 90-92, 100-102, 10-294, 10-294, 101-101, 88-88, 287-287, 403-406, 96-96, 290-290, 19-19, 27-27, 35-35, 41-41, 47-47, 53-53, 63-63, 72-72, 81-81, 112-112, 120-120, 128-128, 136-136, 144-144, 152-152, 160-160, 168-168, 176-176, 184-184, 192-192, 200-200, 208-208, 216-216, 224-224, 232-232, 240-240, 247-247, 252-252, 257-257, 262-262, 267-267, 273-273, 278-278, 283-283, 10-294, 287-287, 11-11, 20-20, 28-28, 54-54, 64-64, 73-73, 82-82, 113-113, 129-129, 137-137, 145-145, 153-153, 161-161, 169-169, 177-177, 185-185, 193-193, 201-201, 209-209, 217-217, 225-225, 233-233, 241-241, 18-18, 25-25, 33-33, 39-39, 45-45, 51-51, 60-60, 70-70, 79-79, 109-109, 118-118, 124-124, 134-134, 142-142, 150-150, 158-158, 166-166, 174-174, 182-182, 190-190, 198-198, 206-206, 214-214, 222-222, 230-230, 238-238, 246-246, 251-251, 256-256, 261-261, 266-266, 271-271, 277-277, 282-282): Builds decorative result backings/grid/frames/arrows and player identity/team-ranking children in exact source order. Identity subscribes the entire PerClient model and calls setModel without a nil filter. TeamRanking Squad predicate is not IsSoloTeamGame. Registers close, optional PostLoadFunc and returns self. No award/rank calculation or authoritative result data is implemented here; all assets, model providers and child close behavior remain external.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/dc6a640aa89f5deb-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/dc6a640aa89f5deb.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00535` at JSON pointer ``; file SHA-256 `54366e6e4444224f79afd0da0df8fad675cdce8f486e4c7a0b62672c2e54541d`.

- `hmh07-lua:186` (original lines 10-10, 10-294): Hud_WZ directly constructs this result widget. SetupGameEndScoreWidget and DisableAutoButtonCallback run first; demo.processedKeyframeJump and lobbyRoot.publicLobby.stage are initialized to0 (real model writes, not backend stage proof). Builds result/outcome/eliminator/status/timer/deathcam/VOIP/quit/placement/killer/weapon/AAR/director/crosshair children. The constructor requests a GameScore/titleString subscription. Only if its callback is delivered and model:get() is nonnil, it requests LocalizeToUpperString with that value and passes the unknown result to Outcome:setText, if earlier accesses/calls succeed; nil takes no explicit setText arm. Callback delivery, localization/case result and displayed effect remain unresolved; aliveTeammateCount drives DownNotOut art; GameScore model forwarded to eliminator/challenge/killer/weapon displays. Victory controls challenge coin visibility. meansOfDeath>0 hides killer/weapon displays and inversely reveals self-caused/means-of-death displays. Attacker identity model rebinding first removes and nils old per-field subscription, dereferences new attackerClientModel, then subscribes xuid/clientNum/rank/rankIcon; analogous clientModel rebinding populates MistakesWereMade identity. Calling card receives full client model; nonnil callbacks update emblem/name/cleaned clan/rank/icon. No nil update clears old displayed text explicitly. VOIP HudStart has a recovered early-return/branch shape (exact trace) and ShowForCodCaster AlwaysFalse; do not replace it with an assumed visibility formula. Outcome state family: ShowOutcomeTransition with no killcam -> Victory/PC; defeat/team_elimination with no killcam -> Defeat/GameOver variants; elimination -> Elimination. Platoon variants additionally platoonCount!=0; PC variants additionally IsPC. Non-PC named states do not themselves contain not-IsPC, so do not assume exclusivity; LUI arbitration stays external. State/current/visibility/profile/lobby/teammate/AAR/input subscriptions reevaluate state/buttons. Square prioritizes console spectate (hide AAR/send skip_deathcam/clear transition/location/hide occluder), then console online AAR close under ui_showWZAAR/noncustom/not-spectate. Triangle redeploy requires private host, all members can redeploy, no matchmaking, redeploy_enabled and noncustom. Cross console deathcam requires eligibility, non-PC, not alternate killcam button, not UI-active/demo/default and viewed report; sends play_deathcam, sets hasPlayedDeathCam, plays alias/music. Circle console hold-finished quits; PC branches quit on non-held conditions; contextual2 handles PC exit. Each action returns true when taken, label callbacks often return false despite valid action, exact source retained. setState CallOriginalFirst hook branches demo/console/PC-occluded focus/intro/cursor/chat behavior; keyframeJump clears transition only during demo. Close is registered via CallOriginalSecond to an unselected __onClose; optional postload then focus/safe-area setup and return. Assets, backend result/rank/AAR provenance, hook order/cleanup outside scope, native menu response and actual execution remain open.

  unknowns: &#91;"Original Lua-to-PS4 CUSA11100 build binding and bytecode/VM/decompiler fidelity unverified.", "Effective HMH settings, enum values, model/data production, LUI state arbitration, event delivery/ordering/cancellation, assets, storage/DDL, networking/service behavior remain explicit gaps where called.", "External helper bodies not selected here are dependencies only; no nil/error recovery assumed beyond visible source. Named LUI override APIs are preserved; no original/new callback ordering is guaranteed without their source contract.", "No independent correctness review, retail execution or function completion credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/dc6a640aa89f5deb-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/dc6a640aa89f5deb.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00142` at JSON pointer ``; file SHA-256 `b0d33370bc53b6d610906b9981c296de28bdc07228c9f239705a7c6393a02db3`.

- `hmh07-lua-follow2:167` (original lines 403-406, 403-406, 287-287, 403-406, 287-287, 101-101, 289-289, 293-293, 101-101, 289-289, 293-293, 404-404, 405-405, 403-406): Closes PlayerIndentity (source spelling) then TeamRanking; the selected direct statements contain no statistics reset. Child close providers are opaque and their transitive effects remain unknown.

  unknowns: &#91;"Original PS4/source exact-version and original Lua/VM binding remain unverified.", "Effective enum/mode/platform/settings and asset/model/storage data are unavailable.", "Native/LUI event/subscription/timer dispatch, cleanup guarantees and errors not shown in selected source remain open.", "Unavailable service/server code is not reconstructed or counted."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/dc6a640aa89f5deb-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/dc6a640aa89f5deb.json) at JSON pointer `/claims/3`.

  Archived evidence ID: `archived-record-00786` at JSON pointer ``; file SHA-256 `95d1d625073efbf92033c6ff8b0a01f09c92d0a7b9b3c07e7949a05eb2b20ef6`.
