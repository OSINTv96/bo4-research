# scripts/mp_common/gametypes/ct_bots.gsc

Project-added notes. See the [code](../../src/scripts/mp_common/gametypes/ct_bots.gsc).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `f4b9a51f8b7fcfcb6d158303d3fd5fff2fcfb6ac`. Original SHA-256: `8d251ce28c386d35b7bf376dc3ae56faf829aa7399d1fbce0b77a9ac7f4669e2`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/fa6b881d3efd6ac9.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh-life:HMH-LIFE-JOIN:may-spawn` (original lines 30-34): Exact predicate state (664-692) applied ONLY to the wz join/spawn callers, with each input's producer: &#91;IN1&#93; dynamic level.mayspawn override (666-669) - the ONLY corpus writer is ct_bots.gsc:34; no literal Warzone writer was found in the pinned lookup; effective delegate presence remains conditional, with computed/native/hashed writers unresolved (if defined and the delegate returns false -> deny). &#91;IN2&#93; queued-respawn deny (671-674): level.playerqueuedrespawn (producer getgametypesetting(#"playerqueuedrespawn") globallogic.gsc:4932; effective value for wz playlists unknown) && self.allowqueuespawn undefined (cleared by spawnclient at 1565; set only by spawnqueuedclientonteam:1415 when a queued dead player is released) && !level.ingraceperiod (globallogic.gsc 5109 set; warzone.gsc 706 cleared in start_warzone) && !level.usestartspawns (globallogic.gsc 4928 set; cleared in wz spawn.gsc::on_spawn_player 276-279 and by spawning_shared use_start_spawns 386-401) -> return false (spawnclient defers only if !mayspawn AND !(isdefined(usedresurrect)&&usedresurrect); a defined-truthy resurrection flag bypasses this denial). &#91;IN3&#93; elimination deny (676-679): game.state == "playing" && level.var_c2cc011f (producer getgametypesetting(hash_4bdd1bd86b610871) spawning_shared.gsc:35; effective value unknown; consumer family warzone.gsc 1979/2131) && level.aliveplayers&#91; self.team &#93;.size == 0 -> false. &#91;IN4&#93; deadline deny (681-684): level.var_75db41a7 defined && gettime() >= it -> false (producer wave_spawn.gsc:120 gettime() + (time - level.waverespawndelay)*1000 - wz wave module only; no literal plain-wz writer was found; effective definedness is unresolved). &#91;IN5&#93; elimination deny (686-689): self.iseliminated defined && truthy -> false (sole corpus writer svz.gsc:313; no literal wz writer found; runtime value and computed/native writers remain unresolved). Else (691) return function_38527849() (624-658): lives-based arms (numlives && !pers&#91;"lives"&#93; -> false; !level.numlives && level.numteamlives && game.lives&#91;self.team&#93; <=0 -> false) and the var_60507c71 arm (647-653: gamehasstarted && defined-truthy && !level.ingraceperiod && !self.hasspawned -> false) - var_60507c71 writers are bounty.gsc:64 / prop.gsc:84 / sd.gsc:75 ONLY, so no literal wz writer was identified; its effective state remains conditional with native/hashed writers unresolved. mayspawn ALLOWED = passes666-689 and the complete624-658 lives tail including628/632; spawnclient can still bypass denial via defined-truthy usedresurrect. wz join/spawn CALLERS (do-not-generalize set): globallogic_spawn::spawnclient 1548 (the join/respawn request gate: !mayspawn && !(defined-truthy usedresurrect) -> showspawnmessage + spectator thread + return; defined-truthy usedresurrect bypasses mayspawn denial), kickifdontspawninternal 1315 (the join-timeout kick guard: !mayspawn && pers&#91;"time_played_total"&#93; > 0 -> no kick; mayspawn true -> kick EXE/PLAYERKICKED_NOTSPAWNED path 1320-1321), globallogic.gsc 4004 (deadplayers iteration -> level.playerlives&#91;team&#93;++ when mayspawn), wz warzone.gsc:1787 (spawn-tags gate), player_killed.gsc 1265 (direct function_38527849 - wz-relevant shared tail). RESET/LEAVE source paths: permission-denied1548-1555 and already-waiting1558-1561 requests return before1565. Only the admitted path writes waitingtospawn1 at1564 and clears allowqueuespawn1565. waitingtospawn is cleared1576 only after waitandspawnclient returns normally and self remains defined. No reset on error/cancellation/disconnect is guaranteed. Endon registrations and the cited disconnect death-notify1202 are source cancellation links; actual termination/teardown remains a native scheduling boundary. f2 tie-in: unlike flagsys/flag waits, mayspawn reads plain level fields - NO flagsys spawning_allowed involvement here (that gate lives in player_insertion/start_insertion); the predicate is request-time, not registration-time (registration-as-invocation excluded). Native/unknown: game.state, getgametypesetting values, and level.aliveplayers maintenance are native/framework-fed; original-build permission semantics unobserved. Not generalized beyond the listed wz-relevant caller set; ct_/prop/sd/bounty writers and the zm twin are out of scope.

  unknowns: &#91;"Effective playerqueuedrespawn / var_c2cc011f settings values for warzone_heavy_metal_heroes playlists (no recovered producer rows; g1 standing)", "game.state native transition semantics (inferred only via comparisons; N2 retained)", "Whether any native/hashed wz code writes level.mayspawn or var_c2cc011f consumers beyond found lines (unobserved, not claimed)"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/fa6b881d3efd6ac9-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fa6b881d3efd6ac9.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00335` at JSON pointer ``; file SHA-256 `d33f41f5173a18ecfa355125edac7344be660195c9fe92cbeb79f84c4609e8b9`.

Dependency decisions: [exact edge records](../../provenance/dependency-decisions.json). Included callees remain at the bounded static scopes recorded there.

- [AV0395](../../provenance/dependency-decisions/AV0395.json): `src/scripts/mp_common/gametypes/ct_bots.gsc` to `scripts/core_common/ai_shared.gsc`; relevance_unresolved.

  Available and inspected. Found caller/functions and lexical gates are recorded, but no matched non-dev reference has both a selected behavior-summary span and an identified callee body. A citation or namespace match alone cannot establish HMH admission. Missing exact root/callback-to-caller admission or bounded source contract stays explicit.

- [AV0396](../../provenance/dependency-decisions/AV0396.json): `src/scripts/mp_common/gametypes/ct_bots.gsc` to `scripts/core_common/player/player_role.gsc`; relevance_unresolved.

  Available and inspected. Found caller/functions and lexical gates are recorded, but no matched non-dev reference has both a selected behavior-summary span and an identified callee body. A citation or namespace match alone cannot establish HMH admission. Missing exact root/callback-to-caller admission or bounded source contract stays explicit.

- [AV0397](../../provenance/dependency-decisions/AV0397.json): `src/scripts/mp_common/gametypes/ct_bots.gsc` to `scripts/killstreaks/killstreaks_util.gsc`; relevance_unresolved.

  Available and inspected. The caller has a #using but no literal namespace-qualified reference to this target. Loader/autoexec, dynamic references and HMH admission are not established by the include; no absence or exclusion inferred.

- [AV0398](../../provenance/dependency-decisions/AV0398.json): `src/scripts/mp_common/gametypes/ct_bots.gsc` to `scripts/mp_common/gametypes/ct_core.gsc`; relevance_unresolved.

  Available and inspected. The caller has a #using but no literal namespace-qualified reference to this target. Loader/autoexec, dynamic references and HMH admission are not established by the include; no absence or exclusion inferred.

- [AV0399](../../provenance/dependency-decisions/AV0399.json): `src/scripts/mp_common/gametypes/ct_bots.gsc` to `scripts/mp_common/gametypes/ct_utils.gsc`; relevance_unresolved.

  Available and inspected. Found caller/functions and lexical gates are recorded, but no matched non-dev reference has both a selected behavior-summary span and an identified callee body. A citation or namespace match alone cannot establish HMH admission. Missing exact root/callback-to-caller admission or bounded source contract stays explicit.
