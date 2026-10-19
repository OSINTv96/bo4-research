# scripts/mp_common/player/player_killed.gsc

Project-added notes. See the [code](../../src/scripts/mp_common/player/player_killed.gsc).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `f4b9a51f8b7fcfcb6d158303d3fd5fff2fcfb6ac`. Original SHA-256: `f8459953cfcad346edbc5d9552ac9f509c20660ab741fc7d8b406977196af6a5`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/1e7d3cc6f2afb84f.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh-life:HMH-LIFE-JOIN:override-routing` (original lines 949-968): Compared source route (pinned named dispatcher/body witnesses, without exhaustive caller coverage): override_spawn is requested through the dynamic pointer level.resurrect_override_spawn, installed at warzone.gsc::main:117 (the compared wz registration; ct_* gametypemaps bind their own ct_utils twin - outside wz scope), from spawning_shared.gsc::onspawnplayer(predictedspawn = 0) 411-530: spawnresurrect = self &#91;&#91; level.resurrect_override_spawn &#93;&#93;( predictedspawn ) at 416-419, and its result has FIRST priority: spawn_origin/angles = self.resurrect_origin/angles (431-435), ahead of tacticalinsertion::overridespawn (413/436-444), use_start_spawns (445-493) and getspawnpoint (495-504); missing spawn_origin aborts (callback::abort_level 506-510); predictedspawn short-circuits to function_e1a7c3d9 + return without spawn (512-516); an actual spawn is self spawn( spawn_origin, spawn_angles ) (518) with influencers only when neither resurrect nor override won (526-529). STATE MATRIX on actual producer fields (level.var_7767cea8 from unit 2; self fields written by connect/hook/insertion): &#91;A&#93; Infected (infection::function_74650d7() && self infection::is_infected(), 139-143) -> infection::function_f488681f(); return true (infection-config-gated helper request: infection.gsc115-133 may return early117-120; otherwise it obtains a spawn candidate122 and, only when defined124, requests a trace127 and writes resurrect_origin129 from the trace position and resurrect_angles130 from the candidate. Actual helper/native results and resulting values remain conditional; preservation of earlier origin/angles is not established). &#91;B&#93; Queue undefined (before/without on_start_game_type install, or install returned early on empty map data) -> function_8cef1872(); return FALSE (145-149) - spawning_shared falls through to spawnoverride/start-spawns/getspawnpoint: the false-return branch in this compared hook matrix; other callers/providers remain unresolved. &#91;C&#93; Queue size < 1 -> resurrect_origin/angles = (0,0,0); function_8cef1872(); return TRUE (151-157) - degenerate spawn-at-zero arm, no guard (bounded as-is). &#91;D&#93; Queue >= 1 (normal wz): teammask->teamindex (159-164); destindex = teamindex % queue size (166); slot = int(teamindex/size) * level.maxteamplayers % dest.spawns.size (168-169); var_25fe2d03 = dest.globalindex streamer hint (170); ispredictedspawn -> take slot without stamping (174-177); actual -> stamp spawntime, or scan at most maxteamplayers cyclic slots for unused, else oldest-visited (178-211; no global oldest guarantee, prior claim reused); wz_alt_spawn dvar default 1 && !isbot -> function_f468d9a5 hold info (origin/angles/freefall from dvar defaults 4350/5000/1760, spawn.gsc 23-36) + var_7070a94c = 1 (213-220); else direct point + var_7070a94c = 0 + function_8cef1872 + thread function_bb9099b9 prematch LUI timer (221-228); return true (231). CALLER CLASSES (source-visible): (i) staging/prediction: player_connect.gsc 337-340 oneshot spawning::onspawnplayer( 1 ) (non-alive non-spectator at connect) and globallogic_spawn::spawnplayerprediction 754-770 0.5s loop (death-side, from player_killed.gsc:968); (ii) the named actual-spawn source path (the supplied first-join/death/reinsertion witnesses): thread &#91;&#91; level.spawnplayer &#93;&#93;() -> globallogic_spawn::spawnplayer 885 -> &#91;&#91; level.onspawnplayer &#93;&#93;( 0 ) 916 -> warzone.gsc::on_spawn_player 208-223 (no args; infection platoon extra) -> spawn.gsc::on_spawn_player 262 (predictedspawn undefined) -> spawning::onspawnplayer(predictedspawn=undefined) 282 - these supplied source edges join the same dispatcher for the listed insertion/death/reinsertion paths, without claiming exhaustive caller or native admission coverage; the first-insertion/reinsertion separations live in the hook (pers&#91;#"spawns"&#93; == 1 first-spawn branch, spawn.gsc 289-299) and in player_insertion::function_e5d4df1c (2977-2990, any insertion flagsys hash_122f326d72f4c884), not in override_spawn. Native admission remains a separate boundary: whether any native path spawns without this chain, and self spawn() acceptance at hold/zero origin are unobserved; no live-join claim.

  unknowns: &#91;"infection::function_74650d7()/is_infected effective truth for HMH playlists (settings-producer gap shared with g1)", "Whether matrix B (queue undefined) is reachable in practice for wz (conditional: requires on_start_game_type order N2)", "var_7070a94c readers beyond spawn.gsc:291 (none further found; native/hashed unknown)", "isbot()/getteammask builtin acceptance (opaque)"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/1e7d3cc6f2afb84f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/1e7d3cc6f2afb84f.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00111` at JSON pointer ``; file SHA-256 `b57edf7bac107f345bfd6aa5a340d936abc1e69e0ea99e7bac2043f7dafc189f`.

Dependency decisions: [exact edge records](../../provenance/dependency-decisions.json). Included callees remain at the bounded static scopes recorded there.

- [AV0302](../../provenance/dependency-decisions/AV0302.json): `src/scripts/mp_common/player/player_killed.gsc` to `scripts/core_common/activecamo_shared.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `function_896ac347`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0303](../../provenance/dependency-decisions/AV0303.json): `src/scripts/mp_common/player/player_killed.gsc` to `scripts/core_common/audio_shared.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `function_30d4f8c4`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0304](../../provenance/dependency-decisions/AV0304.json): `src/scripts/mp_common/player/player_killed.gsc` to `scripts/core_common/globallogic/globallogic_player.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `allowedassistweapon`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0305](../../provenance/dependency-decisions/AV0305.json): `src/scripts/mp_common/player/player_killed.gsc` to `scripts/core_common/globallogic/globallogic_score.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `givekillstats`, `inctotalkills`, `processassist`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0306](../../provenance/dependency-decisions/AV0306.json): `src/scripts/mp_common/player/player_killed.gsc` to `scripts/core_common/globallogic/globallogic_vehicle.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `vehiclecrush`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0307](../../provenance/dependency-decisions/AV0307.json): `src/scripts/mp_common/player/player_killed.gsc` to `scripts/core_common/hostmigration_shared.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `waittillhostmigrationcountdown`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0308](../../provenance/dependency-decisions/AV0308.json): `src/scripts/mp_common/player/player_killed.gsc` to `scripts/core_common/medals_shared.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `setlastkilledby`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0309](../../provenance/dependency-decisions/AV0309.json): `src/scripts/mp_common/player/player_killed.gsc` to `scripts/core_common/player/player_role.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `get`, `is_valid`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0310](../../provenance/dependency-decisions/AV0310.json): `src/scripts/mp_common/player/player_killed.gsc` to `scripts/core_common/player/player_stats.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `function_baa25a23`, `function_e24eec31`, `function_eec52333`, `get_stat_global`, `set_stat_global`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0311](../../provenance/dependency-decisions/AV0311.json): `src/scripts/mp_common/player/player_killed.gsc` to `scripts/core_common/scoreevents_shared.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `decrementlastobituaryplayercountafterfade`, `isregisteredevent`, `processscoreevent`, `uninterruptedobitfeedkills`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0312](../../provenance/dependency-decisions/AV0312.json): `src/scripts/mp_common/player/player_killed.gsc` to `scripts/core_common/weapons_shared.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `detach_carry_object_model`, `getbaseweapon`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0313](../../provenance/dependency-decisions/AV0313.json): `src/scripts/mp_common/player/player_killed.gsc` to `scripts/killstreaks/killstreak_bundles.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `function_48e9536e`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0314](../../provenance/dependency-decisions/AV0314.json): `src/scripts/mp_common/player/player_killed.gsc` to `scripts/killstreaks/killstreaks_util.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `function_e3a30c69`, `is_killstreak_weapon`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0315](../../provenance/dependency-decisions/AV0315.json): `src/scripts/mp_common/player/player_killed.gsc` to `scripts/mp_common/player/player_record.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `record_special_move_data_for_life`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0316](../../provenance/dependency-decisions/AV0316.json): `src/scripts/mp_common/player/player_killed.gsc` to `scripts/weapons/weapon_utils.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `ismeleemod`. Source-only conditional selection; refer to the full edge record for caller lines and gates.
