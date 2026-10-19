# scripts/mp_common/gametypes/globallogic_spawn.gsc

Project-added notes. See the [code](../../src/scripts/mp_common/gametypes/globallogic_spawn.gsc).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `f4b9a51f8b7fcfcb6d158303d3fd5fff2fcfb6ac`. Original SHA-256: `0f052c72c1cee0a93247999ec35265855e28b04fbd26538c4acf8a7dd55ba7c1`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/fcf6ae908acba8a6.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh-combat:HMH-DAMAGE-DOWNED-01:admission` (original lines 885-916, 1058-1064, 1542-1577, 1586-1589, 1705-1711, 1149-1185, 1149-1185, 1548-1572, 885-916, 1058-1064, 1542-1577, 1586-1589, 1705-1711, 1149-1185, 1548-1572): The new connection is a phase-aware input map, not another reconstruction of the old damage predicate. Ordinary spawn writes sessionteam=self.team and sessionstate=playing and refreshes spawntime before later on_player_spawned/insertion work. A redeploy batch merely threads the spawnclient route, whose admission/queue branches mean selection is not proof of a fresh spawn clock. Spectator camera/sessionstate and spectator sessionteam are distinct; should_do_player_damage vetoes only the latter. No explicit candocombat writer is present in the 2,632 frozen GSC/CSC references; its effective producer and original value remain unknown. Insertion holds, begin/teleport flags and HMH doublejump/fallheight branches do not directly write those inputs in the cited spans. Spawn protection is the script elapsed<=cached-ms comparison, checked here only with bit 8; equality counts. Native invulnerability is a separate earlier callback veto, with a visible warzonestaging value-registry chain to enable/disableinvulnerability but unresolved native effects and stacked resets. End_round writes postgame before onendround and the table/server-notify/clientfield end channels. Warzone's later game_ended matchflag pulse does not change that state and therefore does not reopen ordinary admission. Finally, ordinary game-over rejection does not erase the earlier postgame hook: allowed trigger-hurt/crush paths may already call finishplayerdamage as MOD_POST_GAME. All remaining old vetoes/returns are reused unchanged; none of these connections proves HMH runtime behavior or closes the native down-versus-kill decision.

  unknowns: &#91;"Original HMH playlist values for spawnprotectiontime, wzheavymetalheroes, wzplayerinsertiontypeindex, deathcirclerespawn and infectionMode are not supplied by this packet. Source defaults are not effective-session values.", "Actual per-player candocombat, native invulnerability and complete value-stack contents during transport, freefall, redeploy and end transitions are unknown.", "Whether a selected redeploy player passes mayspawn/queue gates and when native spawn/callback delivery completes remain unproved; isalive for downed players retains the d3/native gap.", "No equality/clock example in branch_matrix was executed in the game or in the GSC VM. They are literal source condition cases only.", "The scoped candocombat search does not cover external/unavailable services, engine code, dynamically indexed aliases or unlisted source."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/fcf6ae908acba8a6-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fcf6ae908acba8a6.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00108` at JSON pointer ``; file SHA-256 `c1b5ed194ab6a598e2bbd1b763b0f82947e4eb944b7ad973ec466d1957b7e8e5`; selected record SHA-256 `6bf774a6e502a0a9d7123d402bb953ae59260f8b1aac3378fdb81ac9617f8300`.

- `hmh-health:HMH-HEALTH-RECOVERY-01:heal-policy` (original lines 1058-1064): The conditional HMH producer-to-consumer connection is now pinned: init_heal creates the exact enabled/rate/delay-mode/cap fields only when the table is absent; the value setter and gadget write enabled, the gadget builds rate/cap, and healthoverlay consumes them. Stored rate0 selects a default-rate path when enabled, while enabled0 blocks the ordinary rate path. The separate var_44d52546 force branch bypasses that rate block but still follows delay/cap/tick admission. Stored cap0 means use var_66cb03ad, including after exempt damage drains the stored cap to0. Spawn and completion reset only their shown fields; no guaranteed automatic re-enable on revive is established. These are recovered-source conditions, not effective HMH settings or original PS4 behavior. &#91;init-fields, value-writes, gadget-build, rate-consumer, cap-consumer, consumer-delay, consumer-force-write, force-producer, gadget-damage, gadget-spawn, gadget-stop, revive-state, revive-tail&#93;

  unknowns: &#91;"Declared defaults (new_health_model1, health_regen1, delay-control0, preamble dvar0, revive-health source write50) are not confirmed effective HMH values. No producer policy precedence or callback order was selected.", "Gadget helper function_820a63e9 may have side effects that affect pending preambles; the direct source reset only emits healing_disabled if heal_end is reached. No cancellation guarantee or observed defect is claimed.", "Rates use the exact source arithmetic. Neither weapon.var_4465ef1e units nor fallback role/n_regen inputs, quickrevive multiplier dvar, optional additions or missing rate multiplier are resolved here. A fallback rate of0 can still be changed by the later switch; enabled==0 returns before that switch.", "Cap0 is a sentinel, including a cap drained to0. Actual tick ordering and delay after damage remain damage_gate-owned; no resulting healing observation is asserted.", "The force producer does not set enabled1 in its cited span. Actual caller selection, normal completion delivery, death/abnormal exit cleanup and cross-spawn force-flag lifetime remain unknown. No automatic restart or recovery was attempted.", "h4 saved398/503, all27 health-gadget records were already present in frozen PRIOR-BODIES; the105 unrelated missing records remain missing. Old h4 wording such as time-unit labels and opaque helper status remains unchanged and unreviewed; this report states only its newly pinned source connections."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/fcf6ae908acba8a6-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fcf6ae908acba8a6.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00117` at JSON pointer ``; file SHA-256 `4550cea524030c60c76b94ec05f8597ddf3a1872bf37e4b3bbdeb9ec3d4df887`; selected record SHA-256 `c6cda09d8523852c6011163076f258a265467c60eb1fbeae0bdb63cf8a8848ec`.

- `hmh-life:HMH-LIFE-JOIN:spawn-hook` (original lines 885-916): Branch ladder of the wz spawn hook (262-302), applied to source-visible flags, grace and queued respawn, and what start_warzone changes: (1) 264 usingobj = undefined; (2) 266-269 var_63af7f75 default -1 if missing (the definedness test at266 is an actual source read: missing field gets default -1 at268; a defined prior value skips that default. The conditional deathcircleindex store at273 can overwrite either. Field meaning and further consumers remain unresolved), 271-274 overwritten with level.deathcircleindex when defined (producer: death_circle.gsc:504 inside the per-collapse loop of death_circle::start's continuation - i.e. the slot tracks which collapse circle the player is spawning under); (3) 276-279 the start-spawn clearing rule level.usestartspawns = 0 fired only when usestartspawns && !ingraceperiod && !playerqueuedrespawn (producers: globallogic.gsc 4928 usestartspawns = 1 and 4932 playerqueuedrespawn = getgametypesetting(#"playerqueuedrespawn"); level.ingraceperiod = 1 at globallogic.gsc 5109 in the prematch init and = 0 at 2364 game-end and warzone.gsc:706 start_warzone); (4) 281 var_c5134737 = 0 (connect field cleared); (5) 282 spawning::onspawnplayer( predictedspawn ) - the actual placement delegation to the unit-3 routing (undefined predictedspawn through the wz wrapper); (6) 284-287 streamer hint StreamerSetSpawnHintIndex = var_25fe2d03 when defined (producer override_spawn:170); (7) FIRST-SPAWN DEFER/FINISH BRANCH 289-299, keyed on self.pers&#91; #"spawns" &#93; == 1: if ( var_7070a94c && !player_insertion::function_e5d4df1c() ) (the alt/air flag set by override_spawn under wz_alt_spawn && !isbot AND no insertion currently holds flagsys hash_122f326d72f4c884 per player_insertion.gsc 2977-2990) -> self thread function_c263fd97() (293): the HELD spawn - endon start_warzone/disconnect (349-350), unlink, spawn_anchor at resurrect_origin + playerlinkto + setplayerangles, weapon HUD hidden + ghost (351-356), freeze/disable gadgets via hash_5bb0dd6b277fc20c val keys (357-358), streamer-load loop with dvar windows (stability threshold hash_78198bd3a356f650 0.5; first window hash_24ce936622303dc1 4000ms; second window hash_6e24885f4fa8a2a2 10000ms, added to first4000ms for a default outer deadline starttime+14000ms (373), subject to sampling/waits; required stable samples hash_723f28907e9e4cd0 3; 365-414), then unlink + function_8cef1872 + setorigin(resurrect_origin) + show + forcefreefall( 1, var_df8c6469, 0 ) (416-420), and a pregame LUI timer arm (423-432); ELSE function_8cef1872() (297): the IMMEDIATE finish (spawn_anchor delete 329-333, hudItems.wzLoadFinished = 1 / streamerLoadFraction = 1 / ClearStreamerLoadingHints = 1 clientfields 335-337, val resets of freezecontrols/disablegadgets 338-339, callback hash_4fca7a48128c4741 340); (8) 301 function_ea62f5af() kit stats always. Which branch can finish or defer a JOINING player: the defer arm is exactly branch 7's threaded function_c263fd97 (first spawn only, alt/air, no insertion flag) - the defer branch requests linked/ghost/frozen setup. Its ordinary loop can exit independently when now > starttime+both window values385-388, before the readiness/stability test398 and required sample test409; it can also exit through the qualifying sample-count condition409-412. Either normal break reaches unlink416, cleanup417, setorigin418, show419 and forcefreefall420 requests if execution continues, including a timeout with no ready/stable samples. The registered start_warzone/disconnect endons349-350 are separate cancellation requests; cancellation is not proof that the normal post-loop cleanup ran. The immediate alternative requests function_8cef1872 at297. Actual native effects, clock units, sampling, notification delivery and scheduling remain unproved. What changes once start_warzone releases staging (677-727): level notify start_warzone679 is a cancellation request matching the level endon(#"start_warzone") in actual function_c263fd97 at349. No additional function_c23600e7d identity is established; actual notification delivery/termination and other independently registered holders remain outside this statement; start_insertion (705) sets level flagsys spawning_allowed (648) and runs player_insertion::function_8dcd8623 (603-644: insertions allowed-gate, per-type drivers, waits flagsys insertion_begin_completed); 706 level.ingraceperiod = 0; 710-724 per CURRENT player spawn::function_8cef1872() + val::reset(#"warzonestaging", "takedamage") - the same staging keys the pregame block in on_player_spawned set (warzone.gsc 891); 726 spawn::function_cb5864fc() cleanup. After start_warzone, the pregame staging predicate is false (function_cc47bb2f = game.state == "pregame", warzone.gsc 809-817), so that callback staging block no longer applies. The separate hook hold at spawn.gsc289-293 has NO game.state/pregame guard: a late first spawn with alt flag and no insertion flag can still enter function_c263fd97; an earlier start_warzone notification is not proof of cancelling a newly armed waiter.

  unknowns: &#91;"death-circle module internals (collapse cadence/wave interplay) out of packet; only the index producer line was read", "Whether the ordinary game.state/defined-field LUI prematch-timer arms in function_bb9099b9 at246-255 and function_c263fd97 at423-432 execute on the original build, and their native delivery/outcomes. They are outside the saved source dev-delimited block67-77; no dev-only classification is established.", "Native reason hash_4fca7a48128c4741 callback consumers (registered elsewhere; not traced here - no self-selected extension)", "Effective grace period value for wz (graceperiod 15 vs 5 arm globallogic.gsc 5100-5107 depends on numlives/wavedelay/playerqueuedrespawn settings)"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/fcf6ae908acba8a6-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fcf6ae908acba8a6.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00109` at JSON pointer ``; file SHA-256 `5caf1aa1356542ae7981a711c73f6a03880844387879894c3ecc4615d1002b21`.

- `scripts/mp_common/gametypes/globallogic_spawn.gsc::__init__` (original lines 57-76): No standalone body contract is available in this selected summary. Available classification: registered_system_pre_or_post_initializer.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/fcf6ae908acba8a6-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fcf6ae908acba8a6.json) at JSON pointer `/claims/3`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/561`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `c53c551b0c1e5d10a9e07ffbe2a2a46fb4fc3812bb20de349dbe60fcaacf5191`.

- `hmh-link:HMH-HEALTH-LINKS-01:02-health-baseline` (original lines 885-950, 1058-1064, 1542-1577, 1705-1710): Connected the baseline producer to the saved health equip/unequip/reset and spawn/redeploy boundaries. The source baseline is gadget_health_regen: equip requests baseline-to-selected replacement, unequip requests selected-to-baseline replacement, and a reached warzone reset loadout rewrites that shared value before blank inventory initialization. The shared weapon value, player possession/native slot, slot10 record and count remain different states. Pointer installation/final-writer order and native grant/event success are conditional; all conclusions remain source-only drafts.

  unknowns: &#91;"No guarantee that a defined shared baseline is non-none, a valid resolved asset, distinct from the selected weapon, possessed by the invoking player or assigned a native gadget slot in the original session.", "No proved baseline writer-before-consumer ordering across separately delivered initialization, spawn, reset and health cleanup threads. The exact-name reference scan is limited to the frozen recovered-source spellings and cannot exclude native/alias/missing-script writers.", "No guaranteed tail after death/disconnect, prefix failure, native predicate wait or wrapper error. Normal return/UI/debug/busy0 and slot blanking are separate from successful weapon/health effects.", "Historical body and mapping statuses/wording are retained; this connection does not independently review, repair or promote earlier records. The unpinned original binding-contracts.json was not needed or read."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/fcf6ae908acba8a6-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fcf6ae908acba8a6.json) at JSON pointer `/claims/4`.

  Archived evidence ID: `archived-record-00302` at JSON pointer ``; file SHA-256 `bb5c1d791612007ce03e15db335b61b2ea4c9ac819165865ceacc043682c6591`; selected record SHA-256 `c9f803435422444ba53d14c27da4daac1b9a547f35db3e18ed402c1583e455ed`.

- `scripts/mp_common/gametypes/globallogic_spawn.gsc::function_8acd9309` (original lines 413-467): No standalone body contract is available in this selected summary. Available classification: bounded_first_section_synchronous_descendant.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/fcf6ae908acba8a6-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fcf6ae908acba8a6.json) at JSON pointer `/claims/5`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/1109`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `2eae199f364519f2b5b74d52752836ce5e3c79614aa6c72aee64553410b195e8`.

- `hmh-life:HMH-LIFE-JOIN:override-routing` (original lines 754-770, 885-916): Compared source route (pinned named dispatcher/body witnesses, without exhaustive caller coverage): override_spawn is requested through the dynamic pointer level.resurrect_override_spawn, installed at warzone.gsc::main:117 (the compared wz registration; ct_* gametypemaps bind their own ct_utils twin - outside wz scope), from spawning_shared.gsc::onspawnplayer(predictedspawn = 0) 411-530: spawnresurrect = self &#91;&#91; level.resurrect_override_spawn &#93;&#93;( predictedspawn ) at 416-419, and its result has FIRST priority: spawn_origin/angles = self.resurrect_origin/angles (431-435), ahead of tacticalinsertion::overridespawn (413/436-444), use_start_spawns (445-493) and getspawnpoint (495-504); missing spawn_origin aborts (callback::abort_level 506-510); predictedspawn short-circuits to function_e1a7c3d9 + return without spawn (512-516); an actual spawn is self spawn( spawn_origin, spawn_angles ) (518) with influencers only when neither resurrect nor override won (526-529). STATE MATRIX on actual producer fields (level.var_7767cea8 from unit 2; self fields written by connect/hook/insertion): &#91;A&#93; Infected (infection::function_74650d7() && self infection::is_infected(), 139-143) -> infection::function_f488681f(); return true (infection-config-gated helper request: infection.gsc115-133 may return early117-120; otherwise it obtains a spawn candidate122 and, only when defined124, requests a trace127 and writes resurrect_origin129 from the trace position and resurrect_angles130 from the candidate. Actual helper/native results and resulting values remain conditional; preservation of earlier origin/angles is not established). &#91;B&#93; Queue undefined (before/without on_start_game_type install, or install returned early on empty map data) -> function_8cef1872(); return FALSE (145-149) - spawning_shared falls through to spawnoverride/start-spawns/getspawnpoint: the false-return branch in this compared hook matrix; other callers/providers remain unresolved. &#91;C&#93; Queue size < 1 -> resurrect_origin/angles = (0,0,0); function_8cef1872(); return TRUE (151-157) - degenerate spawn-at-zero arm, no guard (bounded as-is). &#91;D&#93; Queue >= 1 (normal wz): teammask->teamindex (159-164); destindex = teamindex % queue size (166); slot = int(teamindex/size) * level.maxteamplayers % dest.spawns.size (168-169); var_25fe2d03 = dest.globalindex streamer hint (170); ispredictedspawn -> take slot without stamping (174-177); actual -> stamp spawntime, or scan at most maxteamplayers cyclic slots for unused, else oldest-visited (178-211; no global oldest guarantee, prior claim reused); wz_alt_spawn dvar default 1 && !isbot -> function_f468d9a5 hold info (origin/angles/freefall from dvar defaults 4350/5000/1760, spawn.gsc 23-36) + var_7070a94c = 1 (213-220); else direct point + var_7070a94c = 0 + function_8cef1872 + thread function_bb9099b9 prematch LUI timer (221-228); return true (231). CALLER CLASSES (source-visible): (i) staging/prediction: player_connect.gsc 337-340 oneshot spawning::onspawnplayer( 1 ) (non-alive non-spectator at connect) and globallogic_spawn::spawnplayerprediction 754-770 0.5s loop (death-side, from player_killed.gsc:968); (ii) the named actual-spawn source path (the supplied first-join/death/reinsertion witnesses): thread &#91;&#91; level.spawnplayer &#93;&#93;() -> globallogic_spawn::spawnplayer 885 -> &#91;&#91; level.onspawnplayer &#93;&#93;( 0 ) 916 -> warzone.gsc::on_spawn_player 208-223 (no args; infection platoon extra) -> spawn.gsc::on_spawn_player 262 (predictedspawn undefined) -> spawning::onspawnplayer(predictedspawn=undefined) 282 - these supplied source edges join the same dispatcher for the listed insertion/death/reinsertion paths, without claiming exhaustive caller or native admission coverage; the first-insertion/reinsertion separations live in the hook (pers&#91;#"spawns"&#93; == 1 first-spawn branch, spawn.gsc 289-299) and in player_insertion::function_e5d4df1c (2977-2990, any insertion flagsys hash_122f326d72f4c884), not in override_spawn. Native admission remains a separate boundary: whether any native path spawns without this chain, and self spawn() acceptance at hold/zero origin are unobserved; no live-join claim.

  unknowns: &#91;"infection::function_74650d7()/is_infected effective truth for HMH playlists (settings-producer gap shared with g1)", "Whether matrix B (queue undefined) is reachable in practice for wz (conditional: requires on_start_game_type order N2)", "var_7070a94c readers beyond spawn.gsc:291 (none further found; native/hashed unknown)", "isbot()/getteammask builtin acceptance (opaque)"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/fcf6ae908acba8a6-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fcf6ae908acba8a6.json) at JSON pointer `/claims/6`.

  Archived evidence ID: `archived-record-00111` at JSON pointer ``; file SHA-256 `b57edf7bac107f345bfd6aa5a340d936abc1e69e0ea99e7bac2043f7dafc189f`.

- `hmh-life:HMH-LIFE-JOIN:may-spawn` (original lines 664-692, 624-658, 1542-1580, 1396-1455, 1263-1322, 1769-1780, 664-692): Exact predicate state (664-692) applied ONLY to the wz join/spawn callers, with each input's producer: &#91;IN1&#93; dynamic level.mayspawn override (666-669) - the ONLY corpus writer is ct_bots.gsc:34; no literal Warzone writer was found in the pinned lookup; effective delegate presence remains conditional, with computed/native/hashed writers unresolved (if defined and the delegate returns false -> deny). &#91;IN2&#93; queued-respawn deny (671-674): level.playerqueuedrespawn (producer getgametypesetting(#"playerqueuedrespawn") globallogic.gsc:4932; effective value for wz playlists unknown) && self.allowqueuespawn undefined (cleared by spawnclient at 1565; set only by spawnqueuedclientonteam:1415 when a queued dead player is released) && !level.ingraceperiod (globallogic.gsc 5109 set; warzone.gsc 706 cleared in start_warzone) && !level.usestartspawns (globallogic.gsc 4928 set; cleared in wz spawn.gsc::on_spawn_player 276-279 and by spawning_shared use_start_spawns 386-401) -> return false (spawnclient defers only if !mayspawn AND !(isdefined(usedresurrect)&&usedresurrect); a defined-truthy resurrection flag bypasses this denial). &#91;IN3&#93; elimination deny (676-679): game.state == "playing" && level.var_c2cc011f (producer getgametypesetting(hash_4bdd1bd86b610871) spawning_shared.gsc:35; effective value unknown; consumer family warzone.gsc 1979/2131) && level.aliveplayers&#91; self.team &#93;.size == 0 -> false. &#91;IN4&#93; deadline deny (681-684): level.var_75db41a7 defined && gettime() >= it -> false (producer wave_spawn.gsc:120 gettime() + (time - level.waverespawndelay)*1000 - wz wave module only; no literal plain-wz writer was found; effective definedness is unresolved). &#91;IN5&#93; elimination deny (686-689): self.iseliminated defined && truthy -> false (sole corpus writer svz.gsc:313; no literal wz writer found; runtime value and computed/native writers remain unresolved). Else (691) return function_38527849() (624-658): lives-based arms (numlives && !pers&#91;"lives"&#93; -> false; !level.numlives && level.numteamlives && game.lives&#91;self.team&#93; <=0 -> false) and the var_60507c71 arm (647-653: gamehasstarted && defined-truthy && !level.ingraceperiod && !self.hasspawned -> false) - var_60507c71 writers are bounty.gsc:64 / prop.gsc:84 / sd.gsc:75 ONLY, so no literal wz writer was identified; its effective state remains conditional with native/hashed writers unresolved. mayspawn ALLOWED = passes666-689 and the complete624-658 lives tail including628/632; spawnclient can still bypass denial via defined-truthy usedresurrect. wz join/spawn CALLERS (do-not-generalize set): globallogic_spawn::spawnclient 1548 (the join/respawn request gate: !mayspawn && !(defined-truthy usedresurrect) -> showspawnmessage + spectator thread + return; defined-truthy usedresurrect bypasses mayspawn denial), kickifdontspawninternal 1315 (the join-timeout kick guard: !mayspawn && pers&#91;"time_played_total"&#93; > 0 -> no kick; mayspawn true -> kick EXE/PLAYERKICKED_NOTSPAWNED path 1320-1321), globallogic.gsc 4004 (deadplayers iteration -> level.playerlives&#91;team&#93;++ when mayspawn), wz warzone.gsc:1787 (spawn-tags gate), player_killed.gsc 1265 (direct function_38527849 - wz-relevant shared tail). RESET/LEAVE source paths: permission-denied1548-1555 and already-waiting1558-1561 requests return before1565. Only the admitted path writes waitingtospawn1 at1564 and clears allowqueuespawn1565. waitingtospawn is cleared1576 only after waitandspawnclient returns normally and self remains defined. No reset on error/cancellation/disconnect is guaranteed. Endon registrations and the cited disconnect death-notify1202 are source cancellation links; actual termination/teardown remains a native scheduling boundary. f2 tie-in: unlike flagsys/flag waits, mayspawn reads plain level fields - NO flagsys spawning_allowed involvement here (that gate lives in player_insertion/start_insertion); the predicate is request-time, not registration-time (registration-as-invocation excluded). Native/unknown: game.state, getgametypesetting values, and level.aliveplayers maintenance are native/framework-fed; original-build permission semantics unobserved. Not generalized beyond the listed wz-relevant caller set; ct_/prop/sd/bounty writers and the zm twin are out of scope.

  unknowns: &#91;"Effective playerqueuedrespawn / var_c2cc011f settings values for warzone_heavy_metal_heroes playlists (no recovered producer rows; g1 standing)", "game.state native transition semantics (inferred only via comparisons; N2 retained)", "Whether any native/hashed wz code writes level.mayspawn or var_c2cc011f consumers beyond found lines (unobserved, not claimed)"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/fcf6ae908acba8a6-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fcf6ae908acba8a6.json) at JSON pointer `/claims/7`.

  Archived evidence ID: `archived-record-00335` at JSON pointer ``; file SHA-256 `d33f41f5173a18ecfa355125edac7344be660195c9fe92cbeb79f84c4609e8b9`.

- `scripts/mp_common/gametypes/globallogic_spawn.gsc::addspawnsforteamname` (original lines 237-280): No standalone body contract is available in this selected summary. Available classification: bounded_first_section_synchronous_descendant.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/fcf6ae908acba8a6-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fcf6ae908acba8a6.json) at JSON pointer `/claims/8`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/1122`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `091b4ee63a6c0fc1994cfee6b60d340ecefd1bb5fd3f4485c4466fc10aa1a121`.

- `hmh-item:HMH-ITEM-LIFETIME-10:10-reset-respawn` (original lines 1058-1064): The reset connection is a conditional cross-phase replacement, not an atomic respawn cleanup. It disables offhands and sets a reset flag before a native-use wait; early return or receiver cancellation can bypass its clear/reenable tail. A normal path requests item removal, optionally calls the current loadout pointer, replaces inventory with31 blank slots and dispatches inventory_reset after clearing its flag. It does not join older health/debit/removal threads or directly clear all health readiness fields. Spawn only conditionally initializes missing inventory in its own callback, and the world flag barrier is not a child-thread join. Old captured numeric IDs and object references therefore retain explicit cross-reset identity/scheduling gaps. All claims are bounded recovered-source drafts; original HMH build/settings/native behavior remains unproved.

  unknowns: &#91;"No guaranteed cleanup after early return, death/disconnect termination, opaque pointer failure or a nonterminating native-use wait. External cleanup is neither proved nor excluded.", "No generation-token guarantee or original network-ID uniqueness/recycling proof across inventory replacement; previous references may outlive the receiver-field assignment under unknown VM semantics.", "Reset/init directly leave the separately named busy and type23 markers alone in cited spans. Native callbacks or other source paths may clear them; global absence is not claimed.", "The world barrier has independent player snapshots, alive/defined filters and no explicit reset-thread join. Original scheduler interleaving and actual HMH route selection remain open."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/fcf6ae908acba8a6-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fcf6ae908acba8a6.json) at JSON pointer `/claims/9`.

  Archived evidence ID: `archived-record-00147` at JSON pointer ``; file SHA-256 `8bdf1a1ba2c5632297381c45f59fe319116b70c48b5811fd3e5812e5c93fae04`.

- `hmh-health:HMH-HEALTH-RECOVERY-01:pump-lifecycle` (original lines 1058-1064, 1058-1064): The missing connection is a shared level pump with finite per-player state initialization. healthoverlay registers its preinit, chooses a model-specific spawn/restart target, then launches the pump in both branches. New-model initialization arms and replaces the player state; selected visits require a defined table and run the existing gated tick, then stamp the visit time after any normal tick return. Player stop events disarm without clearing the table or killing the level pump. T7 retains its separate entity loop and end_healthregen channel. Downed/revived state can pause/resume eligibility without a new initialization; a fresh delivered spawn or explicit restart replaces it. The server-level game_ended notify is the loop cancellation channel, separate from table callbacks, native matchflag and clientfields. Exact HMH effective model, build binding, VM scheduling/native clocks and event delivery remain unproved. The pump has no saved prior full-body contract, so this is a narrow source-only dependency answer with zero function-completion credit.

  unknowns: &#91;"Active HMH new_health_model and specialisthealspeed values; fallback defaults do not prove selected settings.", "Whether callbacks deliver multiple initializations or interleave with restart/tick; no order beyond same-thread source statements is established.", "A game-ended notification before pump arms may be missed; restart/reload timing outside this body remains unresolved.", "A stale defined state under legacy selection is not excluded; no dynamic-model switch policy is inferred.", "Pump is only a source anchor, not a prior/new complete-body contract; older h4 missing105 records remain missing and unrelated to root scope."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/fcf6ae908acba8a6-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fcf6ae908acba8a6.json) at JSON pointer `/claims/10`.

  Archived evidence ID: `archived-record-00079` at JSON pointer ``; file SHA-256 `664c81b121b2b160b3bb470e284111bd4e498075ed26f8e57a21838a239d1228`; selected record SHA-256 `01737d9ae7828078f6aa94480620e2868896473774fef754a1a65a5f8b652b05`.

- `hmh-life:HMH-LIFE-JOIN:wait-and-spawn` (original lines 1586-1711, 1542-1580, 1717-1744, 1750-1780, 535-735, 1094-1108, 1286-1322, 1586-1711): Bounded HMH use of the waiting orchestration (1586-1711): ENTRY/OWNERSHIP: reached from globallogic_spawn::spawnclient 1572 (self waitandspawnclient( timealreadypassed )) after mayspawn passed OR defined-truthy self.usedresurrect bypassed !mayspawn denial at1548; shared team-lives denial632 additionally requires !level.numlives && level.numteamlives && game.lives&#91;self.team&#93;<=0 - the join/respawn request thread from player_connect.gsc:326 or player_killed routes; and threaded after death from laststand paths: laststand_warzone::respawn_player_after_time 1241-1259 (waits spawned_spectator + n_time_seconds; still sessionstate == spectator -> thread waitandspawnclient()) and laststand.gsc:934. QUEUE OWNERSHIP: waitingtospawn set 1 by spawnclient (1564) before the wait, cleared at 1705 (and 1576 after return; both writers exist and cancellation skips the tail); allowqueuespawn cleared 1565; spawnqueuedclientonteam skips waitingtospawn players (1404) - no double-request. CANCELLATION: endon( disconnect, end_respawn ) 1588 + level endon( game_ended ) 1589; helper waits arm the same keys (waitrespawnorsafespawnbutton 1752; b2 teardown: disconnect death-notify 1202 kills player-owned waits while level entries persist). WAIT BRANCHES: (W1) teamkillpunish 1598-1622: penalty player::function_821200bb (1600), split vs timealreadypassed (1602-1611), positive remainder -> friendly-fire message + thread respawn_asspectator( self.origin + 60Z, angles ) + spawnedasspectator = 1 + wait remainder (1613-1619), clear punish (1621); respawn_asspectator 1105-1108 -> in_spawnspectator 1149+ (spectator state). (W2) wave index 1624-1628. (W3) delay 1630-1641: timeuntilspawn( 0 ) (535-596: grace + never-spawned -> 0; hasspawned -> onrespawndelay/playerrespawndelay/incremental/suicide/teamkilled arms; deathcirclerespawn -> function_ac5b273c 698-708 keyed on level.var_56baa802 (death_circle.gsc 31/423/467, set only after level flagsys wait_till insertion_teleport_completed at 466) - wz reinsertion waits are COLLAPSE-CLOCK timed; wavebased -> timeuntilwavespawn 714-735 with 50ms/index stagger; usedresurrect -> 0). (W4) positive remainder 1643-1688: spectator hud only when NOT sessionmodeiswarzonegame() (1645-1655), thread respawn_asspectator unless already spawned (1657-1674) with the conditional intermission hook (no literal writer found does not prove runtime inactivity) level.useintermissionpointsonwavespawn (1662; no corpus writer), then the warzone arm: self globallogic_utils::waitfortimeornotify( timeuntilspawn, "force_spawn" ) (1684 = self endon( notifyname ); wait time; globallogic_utils.gsc 535-539), notify stop_wait_safe_spawn_button 1687 (NO corpus waiter - new bounded observation), non-warzone arm function_6c23d45b countdown (1680/1717-1744). (W5) manual wait 1690-1703: wavebased = waverespawndelay > 0; if !playerforcerespawn && hasspawned && !wavebased && !wantsafespawn && !playerqueuedrespawn -> press_to_spawn + spectator + waitrespawnorsafespawnbutton (use-button polling 1750-1762). TAIL 1705-1710: clears waitingtospawn/message/wavespawnindex/respawntimerstarttime, pers&#91; #"spawns" &#93;++, thread &#91;&#91; level.spawnplayer &#93;&#93;() -> globallogic_spawn::spawnplayer 885 -> wz chain (units 3-5). FAILURES: (F1) spawnclient defers to spectator only for !mayspawn AND !(isdefined(self.usedresurrect)&&self.usedresurrect); defined-truthy usedresurrect bypasses that denial (1553); (F2) notify(force_spawn) has NO wz poster in corpus (only koth.gsc:511 across mp; userspawnselection posts an LUI force_spawn_selection only, 585) -> no literal wz poster was found; computed/hash/native/frontend notification remains unresolved, so full-duration waiting is conditional (unobserved - not claimed); (F3) never-spawned joiner kick: kickifidontspawninternal 1263-1322 (waits streamer-ready then 90s/scr_kick_time; kicks EXE/PLAYERKICKED_NOTSPAWNED when unspawned, not private, not spectator, and !( !mayspawn && pers&#91;"time_played_total"&#93; > 0 )); (F4) no spawnpoint -> spawning_shared abort_level (506-510); (F5) waitinspawnqueue (1769-1780) waits queue_respawn with NO corpus poster AND no caller - no literal caller/poster found in the pinned source lookup; dynamic/hashed/native reachability unresolved. b2/p3 lifetime reuse: entity-owned waits die at disconnect without cleanup (b2); insertion transport flags/timeouts use the same flagsys wait_till_timeout family (fec68e5c 723-725). Native thread/notify/admission unproved: no claim a wait completes against a live server.

  unknowns: &#91;"Whether any native/frontend mechanism posts force_spawn during wz waits (poster bounded absent in corpus; unobserved)", "stop_wait_safe_spawn_button consumer absent in corpus - native/hashed consumer possible: unobserved", "function_821200bb (teamkill penalty) body outside packet; wantsafespawn/playerforcerespawn writers out of packet", "Synchronous-call endon cancellation stack semantics (retained prior unknown; N4)"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/fcf6ae908acba8a6-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fcf6ae908acba8a6.json) at JSON pointer `/claims/11`.

  Archived evidence ID: `archived-record-00448` at JSON pointer ``; file SHA-256 `e03136d70826aa2604bf9ca1eb5abfa73d5cf068f7746b8446fc4581383ec584`.

- `scripts/mp_common/gametypes/globallogic_spawn.gsc::function_82ca1565` (original lines 100-180): No standalone body contract is available in this selected summary. Available classification: bounded_first_section_synchronous_descendant.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/fcf6ae908acba8a6-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fcf6ae908acba8a6.json) at JSON pointer `/claims/12`.

  Archived evidence ID: `archived-record-00838` at JSON pointer ``; file SHA-256 `be0c871f2d8e334560c3e4b614e4011e299e477c98809444516ddbc3726e99f1`.

- `scripts/mp_common/gametypes/globallogic_spawn.gsc::__init__` (original lines 57-76): No standalone body contract is available in this selected summary. Available classification: conditional_autoexec_or_registration_candidate_with_unproven_load_reachability.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/fcf6ae908acba8a6-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fcf6ae908acba8a6.json) at JSON pointer `/claims/13`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/971`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `cafe10edf4461d2e8f746ecd4b86786beef48ac091fe7aa67c45c377004add44`.

- `scripts/mp_common/gametypes/globallogic_spawn.gsc::calculate_map_center` (original lines 502-529): No standalone body contract is available in this selected summary. Available classification: bounded_first_section_synchronous_descendant.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/fcf6ae908acba8a6-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fcf6ae908acba8a6.json) at JSON pointer `/claims/14`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/1110`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `65169e5850a7c3762bff3ca5507fddfeb1d38eb9600b8e91884f9ddc005aa248`.

- `hmh-life:HMH-LIFE-JOIN:warzone-spawned` (original lines 1049-1063): Existing full body connected to lifecycle phases, with settings kept conditional. Delivery into the body: globallogic_spawn::spawnplayer tail (1062-1063) notifies spawned_player and dispatches callback::callback( #"on_player_spawned" ) (level+self dual-table per f2 record 10) to the wz registration warzone.gsc:152 callback::on_spawned( &on_player_spawned ) (store add_callback "on_player_spawned" callbacks_shared.gsc:329). Phases in the body 823-930: &#91;P1 gates&#93; 825-826 endon death/game_ended; &#91;P2 HMH perk gate&#93; 828-832 getgametypesetting(#"wzheavymetalheroes") defined-truthy -> setperk specialty_doublejump/specialty_fallheight - the named source reads wzheavymetalheroes here; its producer and effective value remain unresolved. Old g1/g2 producerless/zero-match labels are preserved as historical context only and do not establish current absence; the same setting feeds item_inventory 1112-1116 / player_insertion 497-506 / player_reinsertion 441-447 per the g1 equipment record; &#91;P3 state capture&#93; 834-836 var_1ab1ec0c = origin; laststand_warzone::function_7e714b6a; level function_22df4165() count-refresh (same dirty flag the connect body raises, warzone.gsc 1993-1996/1995); &#91;P4 appearance&#93; 837-851 character fields, hidepart tag_ability_hero/tag_equipment_hero; &#91;P5 lives/redeploy flags 853-883&#93; only defined pers/lives updates UI: spawn::function_1390f875( lives ) (855; spawn.gsc 476-486 pers&#91;"lives"&#93;-1 clamped >= 0 into hudItems.playerLivesRemaining - UI request, not a permission grant, prior claim reused); infected route (857-868): function_47851c07() (1899-1922: 0 unless game.state == "playing", 1 for infection, death_circle::function_d66a3de1() (1152-1177: deny at final circle var_78442886 >= final or >= var_245d4af9) under deathcirclerespawn, wave_spawn deny past level.var_75db41a7 (wave_spawn.gsc:120 producer)) truthy -> showReinsertionPassengerCount = 1 + playerCanRedeploy = 1 + var_874448e8 = 1, else playerCanRedeploy = 0; normal route (870-882): lives != 1 && flag not set -> playerCanRedeploy = 1 + var_874448e8 = 1; lives == 1 -> playerCanRedeploy = 0 (flag not cleared) - all clientfield UI requests; &#91;P6 staging early-return 885-899&#93; menu pointer WaypointPlaced registered (885), then function_cc47bb2f() (= game.state == "pregame", 809-817): resets spawn_player freezecontrols/disablegadgets (889-890), warzonestaging takedamage = 0 (891 - the staging keys start_warzone later resets globally at 713), optional start gate if level.var_79219af4 (startplayers setting, main:84) > 0 and activeplayers.size + 1 >= it -> level function_73b0f715() (893-896; 1877-1893: pregame-only, dedicated sv_wznostartever guard, notifies hash_78e53817cafb5265), then RETURN - a joining player spawned during pregame stops here (staged, not inserted); &#91;P7 insertion-type dispatch 901-928&#93; infected helper exit (901-905); dev scr_disable_infiltration menu exit (907-913); else var_7eb8f61a = getgametypesetting(#"wzplayerinsertiontypeindex") defined-or-0 (915 - effective value unknown; same setting read player_reinsertion.gsc 682 and player_insertion 627), clientfield realtime_multiplay = 1 (916), switch: case 0 -> thread player_reinsertion::function_584c9f1() (921), case 1 -> function_39a51e47() (924), case 2 -> function_3c4884f1() (927); other values -> no thread (switch has no default). Reinsertion callees read: 584c9f1 (635-657: no level.reinsertion.vehicle -> player_insertion::function_77132caf; else function_f9348c1d + function_564e0871 + player_insertion::function_f795bf83( level.insertion, vehicle, angle ) + setplayerangles + function_acdf637e); 39a51e47 (557-579: warp_portal_vehicles missing -> function_77132caf; function_5425f45d portal positioning 761-811 true -> function_acdf637e + function_f2867466, else function_77132caf); 3c4884f1 (585-629: nonempty living-teammate array assigns random targetplayer602, but origin603 and angles604 read the foreach variable player, not targetplayer. Preserve this variable mismatch; VM loop-variable lifetime/value is unknown. Empty-array path uses lastdeathpos(+deathcircle bearing), spawnorigin = target - fwd*1000 + 500Z, setorigin + player_insertion::start_freefall( fwd*1000, 0 )); the three bodies arm disconnect endon at559/587/637, respectively. Their continuations differ: function_584c9f1 missing-vehicle arm646-649 threads the fallback and returns without function_acdf637e; its vehicle arm reaches the call656 only on normal continuation. function_39a51e47 requests function_acdf637e at564/572/578 in its respective arms; function_3c4884f1 requests it628 on normal continuation. The exact function_acdf637e body439-448 uses its OR-composed settings guard441, then a defined-pointer guard443 before requesting the pointer thread445. That request and actual native/VM delivery remain conditional;419-433 is the different function_564e0871. The late-arriving/queued-player spawnclient driver is player_reinsertion::function_fec68e5c (680-754) with its var_c5134737 = 1 + &#91;&#91; level.spawnclient &#93;&#93; loop (716-721) - reached from the death-circle reinsertion cycle function_77319881 (warzone.gsc 2649-2676), not from this body. Event order and effective settings stay conditional (native delivery order g2 N2/g3 A.1-A.4; startplayers/wzplayerinsertiontypeconfig effective values unknown).

  unknowns: &#91;"Effective values of wzheavymetalheroes / wzplayerinsertiontypeindex / startplayers in an original HMH session (producer identity and effective native/online settings remain unresolved; the old g1 absence label is historical context only)", "The other named laststand/player_insertion callee implementations are not established by this record alone; reuse their separate exact reviews where present. function_acdf637e439-448 has been read here as guarded source pointer-thread requests, with native/VM delivery unresolved.", "The direct895 call is outside the separate developer192 call site. The complete threshold helper1877-1893 has been inspected: non-pregame returns, dedicated sv_wznostartever can return, otherwise it requests the release notification1892. Effective runtime state/dvars and notification delivery remain unknown.", "Native ordering between on_player_spawned dispatch and any native spawn finalization (retained)"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/fcf6ae908acba8a6-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fcf6ae908acba8a6.json) at JSON pointer `/claims/15`.

  Archived evidence ID: `archived-record-00323` at JSON pointer ``; file SHA-256 `a6b9d3cd48314b4e9a4549400cb2ea0b709b0b056c53d93554bf5202bbb4e412`.

- `scripts/mp_common/gametypes/globallogic_spawn.gsc::addsupportedspawnpointtype` (original lines 186-202): No standalone body contract is available in this selected summary. Available classification: synchronous_startup_shared_callee.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/fcf6ae908acba8a6-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fcf6ae908acba8a6.json) at JSON pointer `/claims/16`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/563`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `c60eae6557e3b031a9e1c8b5935df55e71a6fc8edc02cb9e3b27c99f57340aa7`.

- `scripts/mp_common/gametypes/globallogic_spawn.gsc::function_68312709` (original lines 325-407): No standalone body contract is available in this selected summary. Available classification: bounded_first_section_synchronous_descendant.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/fcf6ae908acba8a6-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fcf6ae908acba8a6.json) at JSON pointer `/claims/17`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/1108`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `c33c301ac5ec83174ddc36a8b8b7e3fc4de6b63b501d4c87ce58aaed8bed4dd3`.

- `scripts/mp_common/gametypes/globallogic_spawn.gsc::addspawns` (original lines 473-496): No standalone body contract is available in this selected summary. Available classification: additional_first_section_synchronous_helper.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/fcf6ae908acba8a6-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fcf6ae908acba8a6.json) at JSON pointer `/claims/18`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/1095`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `11815be5b8caa1a4067d1e0ac28197ccd3c2f488f3298cb6e9c4b1511c8439df`.

- `scripts/mp_common/gametypes/globallogic_spawn.gsc::__init__system__` (original lines 48-51): No standalone body contract is available in this selected summary. Available classification: autoexec_registration_inventory; native invocation/load order unverified.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/fcf6ae908acba8a6-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fcf6ae908acba8a6.json) at JSON pointer `/claims/19`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/562`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `a6d60932ce497a3266959ba14a3db1482215c603635a2712cbf9121618f75d10`.

- `hmh-player:HMH-PLAYER-LASTSTAND:spawn-reset` (original lines 1058-1064): DELIVERY VS REGISTRATION separated. REGISTRATION: laststand_warzone.__init__:73 callback::on_spawned(&on_player_spawned) = callbacks_shared.gsc:327-330 add_callback(#"on_player_spawned", func, obj) into the level callback table; warzone main:152 registers the wz twin &on_player_spawned on the SAME key (warzone.gsc 140-167). DELIVERY: globallogic_spawn::spawnplayer (885) tail: notify spawned_player (1062) then callback::callback(#"on_player_spawned") (1063) -> the callbacks_shared table dispatcher skips nonarray entries, returns on an invalid function pointer and otherwise issues util-wrapper thread requests for reached valid entries; actual callback execution/order remains unknown; no name string or direct call links the sides besides the table key. L2 CONNECTION: the dispatch is inside the same spawn chain l2 bounded (spawnclient -> spawnplayer 885 -> player::spawn_player at 890) and requests this script callback when execution reaches the shown spawnplayer tail; native entry, admission and invocation frequency remain unproved. RESET HERE (anchor 120-128): self.var_d887a4ad = undefined (the revive-completion-window marker read by the bleedout timer at 1060/1081 and by laststop_bleedout_damage at 938); revivingClientNum UI to sentinel int(min(getdvarint('com_maxclients',0),pow(2,7)))-1 (123); playerCleanUps/playerKills UI copies of self.cleanups/self.kills without defaults (124-125; undefined copied, not zeroed - prior unknown kept); hudItems.beingFinished = 0 (126); self.var_156bf46e = undefined (vehicle flag consulted by the elimination gate at 619). RESET ELSEWHERE (exact sites): self.laststand = undefined plus health/maxhealth restored to spawnhealth in player::spawn_player (player_shared.gsc 73, 78-79); self.laststandcount = undefined via wz on_player_spawned -> laststand_warzone::function_7e714b6a (warzone.gsc:835 -> 2142-2151); self.revivetrigger deleted by bleed_out (1142), revive_success (2057), and on disconnect by laststand_shared.gsc:146-152; Not written by this local 120-128 callback (no whole-spawn nonreset claim): bleedout_time/last_bleedout_time/var_969fabf4/var_2d19ce3c/var_1cc38de0/reviveprogress/is_reviving_any/var_5c574004/var_a1d415ee/var_22002c3b/laststandparams (other native, opaque or dynamic spawn work may affect them; no actual stale-field outcome is established). LATE/DUPLICATE/MISSING (conditional only): a late spawn re-fires and re-clears these markers; a missing spawn for a player still dead/spectating leaves death-path cleanup state in force (native respawn admission is the standing l2/l3 negative boundary); duplicate delivery double-writes the constants (idempotent) and could erase an in-progress revive marker if a spawn coincided with revive - no such co-occurrence established, bounded alternative only. The historical boundary (cross-packet-reconciliation delivery_audit_rows/327, in unit-context/0002) is retained: consumer callsites have no additional accepted setup delivery path in that frozen audit; aliases/overwritten pointers/native triggering remain open.

  unknowns: &#91;"Delivery order between wz and laststand_warzone registrations on the on_player_spawned key (native table order; g2 N2).", "Native event posting and per-spawn firing frequency in an original session (g3 A.1/A.2 standing).", "Stale non-reset fields when a life ends without the recorded death/bleedout cleanup paths - conditional on the native death pipeline, unobserved."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/fcf6ae908acba8a6-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fcf6ae908acba8a6.json) at JSON pointer `/claims/20`.

  Archived evidence ID: `archived-record-00151` at JSON pointer ``; file SHA-256 `fb3d4811b0e64cfe4de3361225be438a6b8333fe4dfccedeed96762b60019694`.

- `scripts/mp_common/gametypes/globallogic_spawn.gsc::__init__system__` (original lines 48-51): No standalone body contract is available in this selected summary.

  unknowns: &#91;"Source statements only; VM native loader/event/order/assert/getter/object semantics are not verified.", "Exact originating retail build, PS4 binary/asset mapping, native/server implementation and gameplay execution remain open.", "Conditional/dev candidate: source review does not establish HMH load reachability or execution."&#93;

  status: source_semantic_contract_ready_for_manager_review

  Complete explanatory fields: [exact projection](../../provenance/documentation/fcf6ae908acba8a6-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fcf6ae908acba8a6.json) at JSON pointer `/claims/21`.

  Archived evidence ID: `archived-record-00002` at JSON pointer `/contracts/180`; file SHA-256 `14d82864f03d391c58ddc8caaf6f84c482f72ea05ab80940d42da35eabc0a97e`; selected record SHA-256 `4912f6c8aa9c2d1c7b64a5284e7a41852addf987460c5ca81203aa9d7e4b6f60`.

- `scripts/mp_common/gametypes/globallogic_spawn.gsc::addsupportedspawnpointtype` (original lines 186-202): No standalone body contract is available in this selected summary.

  unknowns: &#91;"Source statements only; VM native loader/event/order/assert/getter/object semantics are not verified.", "Exact originating retail build, PS4 binary/asset mapping, native/server implementation and gameplay execution remain open.", "Unresolved/opaque callsites are retained exactly; source availability versus native identity needs manager reconciliation."&#93;

  status: source_semantic_contract_ready_for_manager_review

  Complete explanatory fields: [exact projection](../../provenance/documentation/fcf6ae908acba8a6-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fcf6ae908acba8a6.json) at JSON pointer `/claims/22`.

  Archived evidence ID: `archived-record-00002` at JSON pointer `/contracts/181`; file SHA-256 `14d82864f03d391c58ddc8caaf6f84c482f72ea05ab80940d42da35eabc0a97e`; selected record SHA-256 `e28fca9064898abfc42616c980b14a26ffb70f5e073b9abb6761c65fda3c3b9a`.

- `scripts/mp_common/util.gsc::getotherteam` (original lines not specified): No standalone body contract is available in this selected summary. Available classification: required_initialization_callee_or_exact_import_candidate.

  calls: &#91;{"line": 306, "namespace": null, "symbol": "assertmsg", "statement": "assertmsg( \"<dev string:x38>\" + team );", "dev_delimited": false}&#93;

  status: source_contract_ready_for_Astra_review

  Complete explanatory fields: [exact projection](../../provenance/documentation/fcf6ae908acba8a6-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fcf6ae908acba8a6.json) at JSON pointer `/claims/23`.

  Archived evidence ID: `archived-record-00140` at JSON pointer `/contracts/5`; file SHA-256 `fe991f3c3925027bd6044541a1776f3f762cca0c3a659fbe3e0018e62f5c4006`; selected record SHA-256 `85031bc4a7a4d3bdd285a3824454a0c6457cea0315b3787c8de05ef79870e4a9`.

- `scripts/mp_common/gametypes/globallogic_spawn.gsc::addsupportedspawnpointtype` (original lines 186-202): No standalone body contract is available in this selected summary.

  unknowns: &#91;"Source statements only; VM native loader/event/order/assert/getter/object semantics are not verified.", "Exact originating retail build, PS4 binary/asset mapping, native/server implementation and gameplay execution remain open.", "Unresolved/opaque callsites are retained exactly; source availability versus native identity needs manager reconciliation."&#93;

  status: source_semantic_contract_ready_for_manager_review

  Complete explanatory fields: [exact projection](../../provenance/documentation/fcf6ae908acba8a6-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fcf6ae908acba8a6.json) at JSON pointer `/claims/24`.

  Archived evidence ID: `archived-record-00002` at JSON pointer `/contracts/181`; file SHA-256 `14d82864f03d391c58ddc8caaf6f84c482f72ea05ab80940d42da35eabc0a97e`; selected record SHA-256 `e28fca9064898abfc42616c980b14a26ffb70f5e073b9abb6761c65fda3c3b9a`.

- `scripts/mp_common/gametypes/globallogic_spawn.gsc::__init__system__` (original lines 48-51): No standalone body contract is available in this selected summary.

  unknowns: &#91;"Source statements only; VM native loader/event/order/assert/getter/object semantics are not verified.", "Exact originating retail build, PS4 binary/asset mapping, native/server implementation and gameplay execution remain open.", "Conditional/dev candidate: source review does not establish HMH load reachability or execution."&#93;

  status: source_semantic_contract_ready_for_manager_review

  Complete explanatory fields: [exact projection](../../provenance/documentation/fcf6ae908acba8a6-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fcf6ae908acba8a6.json) at JSON pointer `/claims/25`.

  Archived evidence ID: `archived-record-00002` at JSON pointer `/contracts/180`; file SHA-256 `14d82864f03d391c58ddc8caaf6f84c482f72ea05ab80940d42da35eabc0a97e`; selected record SHA-256 `4912f6c8aa9c2d1c7b64a5284e7a41852addf987460c5ca81203aa9d7e4b6f60`.

Dependency decisions: [exact edge records](../../provenance/dependency-decisions.json). Included callees remain at the bounded static scopes recorded there.

- [AV0084](../../provenance/dependency-decisions/AV0084.json): `src/scripts/mp_common/gametypes/globallogic_spawn.gsc` to `scripts/core_common/hostmigration_shared.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `waitlongdurationwithhostmigrationpause`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0085](../../provenance/dependency-decisions/AV0085.json): `src/scripts/mp_common/gametypes/globallogic_spawn.gsc` to `scripts/core_common/hud_util_shared.gsc`; relevance_unresolved.

  All found qualified references are inside /# #/ developer regions. Those calls are excluded from the production call slice only. Include/loader and any autoexec relevance remain unresolved; no whole-file exclusion.

- [AV0086](../../provenance/dependency-decisions/AV0086.json): `src/scripts/mp_common/gametypes/globallogic_spawn.gsc` to `scripts/core_common/player/player_role.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `clear`, `get`, `is_valid`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0087](../../provenance/dependency-decisions/AV0087.json): `src/scripts/mp_common/gametypes/globallogic_spawn.gsc` to `scripts/mp_common/armor.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `setlightarmor`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0088](../../provenance/dependency-decisions/AV0088.json): `src/scripts/mp_common/gametypes/globallogic_spawn.gsc` to `scripts/mp_common/gametypes/hostmigration.gsc`; relevance_unresolved.

  Available and inspected. Found caller/functions and lexical gates are recorded, but no matched non-dev reference has both a selected behavior-summary span and an identified callee body. A citation or namespace match alone cannot establish HMH admission. Missing exact root/callback-to-caller admission or bounded source contract stays explicit.

- [AV0089](../../provenance/dependency-decisions/AV0089.json): `src/scripts/mp_common/gametypes/globallogic_spawn.gsc` to `scripts/mp_common/gametypes/hud_message.gsc`; relevance_unresolved.

  Available and inspected. Found caller/functions and lexical gates are recorded, but no matched non-dev reference has both a selected behavior-summary span and an identified callee body. A citation or namespace match alone cannot establish HMH admission. Missing exact root/callback-to-caller admission or bounded source contract stays explicit.
