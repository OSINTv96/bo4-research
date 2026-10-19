# scripts/mp_common/laststand.gsc

Project-added notes. See the [code](../../src/scripts/mp_common/laststand.gsc).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `f4b9a51f8b7fcfcb6d158303d3fd5fff2fcfb6ac`. Original SHA-256: `a139f9a335ea089e376752ac7143379039136c92d19fe90052d415180f599029`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/f5012bfeafcb9a18.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh-life:HMH-LIFE-JOIN:wait-and-spawn` (original lines 934-934): Bounded HMH use of the waiting orchestration (1586-1711): ENTRY/OWNERSHIP: reached from globallogic_spawn::spawnclient 1572 (self waitandspawnclient( timealreadypassed )) after mayspawn passed OR defined-truthy self.usedresurrect bypassed !mayspawn denial at1548; shared team-lives denial632 additionally requires !level.numlives && level.numteamlives && game.lives&#91;self.team&#93;<=0 - the join/respawn request thread from player_connect.gsc:326 or player_killed routes; and threaded after death from laststand paths: laststand_warzone::respawn_player_after_time 1241-1259 (waits spawned_spectator + n_time_seconds; still sessionstate == spectator -> thread waitandspawnclient()) and laststand.gsc:934. QUEUE OWNERSHIP: waitingtospawn set 1 by spawnclient (1564) before the wait, cleared at 1705 (and 1576 after return; both writers exist and cancellation skips the tail); allowqueuespawn cleared 1565; spawnqueuedclientonteam skips waitingtospawn players (1404) - no double-request. CANCELLATION: endon( disconnect, end_respawn ) 1588 + level endon( game_ended ) 1589; helper waits arm the same keys (waitrespawnorsafespawnbutton 1752; b2 teardown: disconnect death-notify 1202 kills player-owned waits while level entries persist). WAIT BRANCHES: (W1) teamkillpunish 1598-1622: penalty player::function_821200bb (1600), split vs timealreadypassed (1602-1611), positive remainder -> friendly-fire message + thread respawn_asspectator( self.origin + 60Z, angles ) + spawnedasspectator = 1 + wait remainder (1613-1619), clear punish (1621); respawn_asspectator 1105-1108 -> in_spawnspectator 1149+ (spectator state). (W2) wave index 1624-1628. (W3) delay 1630-1641: timeuntilspawn( 0 ) (535-596: grace + never-spawned -> 0; hasspawned -> onrespawndelay/playerrespawndelay/incremental/suicide/teamkilled arms; deathcirclerespawn -> function_ac5b273c 698-708 keyed on level.var_56baa802 (death_circle.gsc 31/423/467, set only after level flagsys wait_till insertion_teleport_completed at 466) - wz reinsertion waits are COLLAPSE-CLOCK timed; wavebased -> timeuntilwavespawn 714-735 with 50ms/index stagger; usedresurrect -> 0). (W4) positive remainder 1643-1688: spectator hud only when NOT sessionmodeiswarzonegame() (1645-1655), thread respawn_asspectator unless already spawned (1657-1674) with the conditional intermission hook (no literal writer found does not prove runtime inactivity) level.useintermissionpointsonwavespawn (1662; no corpus writer), then the warzone arm: self globallogic_utils::waitfortimeornotify( timeuntilspawn, "force_spawn" ) (1684 = self endon( notifyname ); wait time; globallogic_utils.gsc 535-539), notify stop_wait_safe_spawn_button 1687 (NO corpus waiter - new bounded observation), non-warzone arm function_6c23d45b countdown (1680/1717-1744). (W5) manual wait 1690-1703: wavebased = waverespawndelay > 0; if !playerforcerespawn && hasspawned && !wavebased && !wantsafespawn && !playerqueuedrespawn -> press_to_spawn + spectator + waitrespawnorsafespawnbutton (use-button polling 1750-1762). TAIL 1705-1710: clears waitingtospawn/message/wavespawnindex/respawntimerstarttime, pers&#91; #"spawns" &#93;++, thread &#91;&#91; level.spawnplayer &#93;&#93;() -> globallogic_spawn::spawnplayer 885 -> wz chain (units 3-5). FAILURES: (F1) spawnclient defers to spectator only for !mayspawn AND !(isdefined(self.usedresurrect)&&self.usedresurrect); defined-truthy usedresurrect bypasses that denial (1553); (F2) notify(force_spawn) has NO wz poster in corpus (only koth.gsc:511 across mp; userspawnselection posts an LUI force_spawn_selection only, 585) -> no literal wz poster was found; computed/hash/native/frontend notification remains unresolved, so full-duration waiting is conditional (unobserved - not claimed); (F3) never-spawned joiner kick: kickifidontspawninternal 1263-1322 (waits streamer-ready then 90s/scr_kick_time; kicks EXE/PLAYERKICKED_NOTSPAWNED when unspawned, not private, not spectator, and !( !mayspawn && pers&#91;"time_played_total"&#93; > 0 )); (F4) no spawnpoint -> spawning_shared abort_level (506-510); (F5) waitinspawnqueue (1769-1780) waits queue_respawn with NO corpus poster AND no caller - no literal caller/poster found in the pinned source lookup; dynamic/hashed/native reachability unresolved. b2/p3 lifetime reuse: entity-owned waits die at disconnect without cleanup (b2); insertion transport flags/timeouts use the same flagsys wait_till_timeout family (fec68e5c 723-725). Native thread/notify/admission unproved: no claim a wait completes against a live server.

  unknowns: &#91;"Whether any native/frontend mechanism posts force_spawn during wz waits (poster bounded absent in corpus; unobserved)", "stop_wait_safe_spawn_button consumer absent in corpus - native/hashed consumer possible: unobserved", "function_821200bb (teamkill penalty) body outside packet; wantsafespawn/playerforcerespawn writers out of packet", "Synchronous-call endon cancellation stack semantics (retained prior unknown; N4)"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/f5012bfeafcb9a18-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/f5012bfeafcb9a18.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00448` at JSON pointer ``; file SHA-256 `e03136d70826aa2604bf9ca1eb5abfa73d5cf068f7746b8446fc4581383ec584`.

- `hmh-combat:HMH-DAMAGE-DOWNED-01:fatal-handoff` (original lines 37-60, 1832-1840): The saved damage and return value belong to the actual final-damage receiver. A normal return from finishplayerdamage supplies an initial fatal value; after the optional status helper the source re-reads laststand. If laststand is true it replaces that value with either the installed pointer result (and then clears saved damage) or literal1 when either required field is absent. The three final-damage callsites include a reflected friendly-fire call on the attacker: a second result can overwrite the first victim result. The outer callback passes its resulting fatal variable into damage feedback; the shown override/feedback code does not itself call the native downing or killing operation. Actual native damage/death effects already lie across finishplayerdamage and remain unknown.

  unknowns: &#91;"No actual runtime source/build binding or effective HMH friendly-fire/playlist settings established.", "The source does not guard denominator zero/undefined, stale saved damage or pointer callability; native/VM handling cannot be invented.", "The reflected call reads attacker state and its own saved field; when/how an older field survives a skipped/aborted call is conditional, not an observed game defect.", "Damage notifications and timer updates may occur in different orders; no selected scheduler ordering or exact health effect.", "Prior mapping92 labels predicate outcomes as death/starting laststand. This new source handoff traces a return into feedback and retains the prior wording for project-end reconciliation without changing or reviewing it."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/f5012bfeafcb9a18-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/f5012bfeafcb9a18.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00412` at JSON pointer ``; file SHA-256 `47430e32ca57c8ef06ac19e097873e34b05140d6ba34295e6640eb3b070a306b`; selected record SHA-256 `194efb98b660634a6b04c88d4f3bfb008ac97ec2ad6e157cbfc5726fbfb1295f`.

Dependency decisions: [exact edge records](../../provenance/dependency-decisions.json). Included callees remain at the bounded static scopes recorded there.

- [AV0483](../../provenance/dependency-decisions/AV0483.json): `src/scripts/mp_common/laststand.gsc` to `scripts/autogenerated/luielems/core/revive_hud.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `register`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0484](../../provenance/dependency-decisions/AV0484.json): `src/scripts/mp_common/laststand.gsc` to `scripts/autogenerated/luielems/mp/laststand/mp_revive_prompt.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `register`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0485](../../provenance/dependency-decisions/AV0485.json): `src/scripts/mp_common/laststand.gsc` to `scripts/core_common/scoreevents_shared.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `processscoreevent`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0486](../../provenance/dependency-decisions/AV0486.json): `src/scripts/mp_common/laststand.gsc` to `scripts/core_common/weapons_shared.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `detach_all_weapons`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0487](../../provenance/dependency-decisions/AV0487.json): `src/scripts/mp_common/laststand.gsc` to `scripts/weapons/weapon_utils.gsc`; relevance_unresolved.

  Available and inspected. The caller has a #using but no literal namespace-qualified reference to this target. Loader/autoexec, dynamic references and HMH admission are not established by the include; no absence or exclusion inferred.
