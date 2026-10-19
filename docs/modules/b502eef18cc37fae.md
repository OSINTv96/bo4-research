# scripts/mp_common/laststand_warzone.csc

Project-added notes. See the [code](../../src/scripts/mp_common/laststand_warzone.csc).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `f4b9a51f8b7fcfcb6d158303d3fd5fff2fcfb6ac`. Original SHA-256: `bdcf96dbc87e89442b045aa4ef0a383742068ccfe73103de1dc85c823e51baba`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/b502eef18cc37fae.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `scripts/mp_common/laststand_warzone.csc::__init__system__` (original lines 13-16): No standalone body contract is available in this selected summary. Available classification: conditional_autoexec_or_registration_candidate_with_unproven_load_reachability.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/b502eef18cc37fae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b502eef18cc37fae.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/996`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `25ccd18a8759fa861857046e96ea92362f6f6952b261c328297d7fb5d8709858`.

- `hmh-player:HMH-PLAYER-LASTSTAND:revive-success` (original lines 33-93): SOURCE-ONLY ANCHOR (like unit 4): unit-context/0006 prior_body_records = &#91;&#93;; SOURCE-ONLY-ANCHORS.json lists the 1630 (function_55f6978f) and 1336 (dev) connection sites; a narrow transition trace of the exact recovered source only - no reused body contract and no new full-body completion is claimed; zero function credit. CALLERS (source, with delivery condition): recovery route function_55f6978f:1622-1633 - the attempt revive_do_revive returned truthy (timer >= revivetime) for a teammate holding use inside this trigger; THEN self thread revive_success(reviver) (1630) runs on the DOWNED player, plus function_2907ce7a (1631) immediately clears progress/beingRevived UI and the think loop returns true (1632; also ends via stop_revive_trigger/level.gameended at 1308/1313); DEV-only recovered callers: revive_trigger_think:1333-1340 self-revive behind dvar lastand_selfrevive, auto_revive_on_notify:1957-1962 (dev block, waittill auto_revive then thread revive_success(waitresult.reviver)); hud_shared.gsc:1700-1703 posts auto_revive to downed players but the only wz waiters are dev-gated - scoped no-op condition, not an exclusion. BODY TRACE: var_156bf46e = undefined (1985; clears the vehicle flag); !isplayer(self) -> notify player_revived{reviver} + return (1987-1991, non-player guard); function_102748f8 (1993 -> 863-868: takeweapon(level.laststandweapon 'downed'); requests giveweapon(level.var_e273f858) then switchtoweaponimmediate(level.var_e273f858,1); level.var_e273f858 is initialized by getweapon(#"notdowned") at62, with native effects unproved); friendly reviver stats (1995-2000: stats::function_d40764f3/b7f80d87 'revives' + pers increments - sinks are native per l3); enemy downs_revived stat on laststandparams.attacker (2002-2005); SELF VAR_D887A4AD = 1 (2007) - the bleedout timer's UI-write suppression (1060) and silent exit (1081-1084) markers; wait revive_wait_time = getdvarint(hash_77107267fe87b359, 350)/1000 (2008-2009, ~0.35 s in observed units; native dvar semantics open); isdefined(self) gates (2011-2014); demo/potm player_revived bookmarks when b_track_stats default 1 (2016-2020); allowjump(1) (2022-2025, restoring playerlaststand:773); attacker read from laststandparams (2027-2030); laststandparams = undefined + SELF.LASTSTAND = UNDEFINED (2032-2033) - player_is_in_laststand false, the successful-revive clear (contrast the spawn reset at player_shared.gsc:73 and the death paths); SELF NOTIFY(#'player_revived', { #reviver:reviver }) (2034) - consumed by: the bleedout timer endon registered at1014, a conditional cancellation path only if that invocation is still running and the native notification/endon provider delivers it; the separate explicit return1081-1083 can already have ended it, function_263a2944 prompt closer multi-argument waittill288, which resumes into close/reset-clientnum/terminated-notify290-294; this is not an endon. Separate updater function_c025efba arms its endon323; multi-key native semantics remain unresolved, and NOT by the callbacks_shared table (a separate callback::callback fires at 2072); laststand_enable_player_weapons (2035 -> 874-888: endon disconnect, sig_blade 0.03 wait, takeweapon(notdowned), enable cycling/offhands/usability, weapons::function_d571ac59(self.var_60956d6) restore from the cached downing weapon 659); defined(self) gate (2037-2040); SELF REVIVEPLAYER() NATIVE (2042 - the native restoration stays opaque); var_d887a4ad = undefined (2043 - window closed); HEALTH: health = getdvarint(player_laststandrevivehealth, 0) - warzone main:162 SETS THIS DVAR TO 50 (the recovered wz config producer) - overridden when reviver function_15098882() > 0 (2046-2054; no corpus definition) then self.health = health (2056; native health write semantics open); function_b1303a37 (2057 -> 1970-1977: revivetrigger delete + undefined - the same cleanup bleed_out/suicide uses); clientfield::set(laststand_bleed, 0) (2058 -> client FX stop in laststand_warzone.csc 38/89-92); function_2907ce7a (2059 -> 1265-1269: progress/beingRevived UI 0); lui::screen_close_menu (2060); val::reset(last_stand, show_weapon_hud) (2061, undoing 783); function_1e8018b0 (2062 -> 2103-2113: telemetry end_time + function_92d1707f bb sink hash_1df8d9815fc22893 - bb/match_record sinks native per l3); pers&#91;'timesrevived'&#93; init/++ (2064-2069); voiceevent('player_revived', ...) (2070); callback::callback(#'on_player_revived', { #reviver, #attacker }) (2072 - table fan-out; registrants via on_revived wrapper callbacks_shared.gsc 741-744; handler set/order not supplied). INTEGRATION DOWNSTREAM: the source has two distinct conditional timer exits: a still-running invocation may receive player_revived through its registered1014 endon, while an invocation that reaches1081 with var_d887a4ad===1 returns silently at1083, including a possible window after the countdown loop has ended and before2034. Revive sets the flag2007 before its wait2009 and does not prove a positive remaining bleedout_time. Actual interleaving, notification delivery and native cancellation remain unproved; the interrupted bleedout-damage thread resets its takedamage gate via endoncallback function_99fa3916 (929/984-987); a later death + spawn cycle then resets the remaining fields (spawn resets enumerated in unit 2: laststand/health player_shared.gsc:73/78-79, laststandcount warzone.gsc:835, var_d887a4ad/var_156bf46e/beingFinished UI anchor 120-128); reviveprogress is not explicitly re-zeroed here beyond the UI clears (the next attempt loop writes it from 0 each time).

  unknowns: &#91;"Native reviveplayer/startrevive/stoprevive restoration semantics (animation/positioning/weapon state) remain opaque; no inference made.", "function_15098882 (reviver health modifier) has no corpus definition - dynamic_unresolved.", "on_player_revived registrant set/order and its difference from the 2034 entity-notify audience (table vs prompt-closer waittill continuation and separate cancelling endon watchers; multi-key native semantics unresolved) at runtime (g3 draft + native delivery).", "The 350 ms wait's unit semantics (dvar default 350 -> /1000) and its effect on the timer's silent-return window are design-shaped but native-timed (f2 N4).", "laststandparams.attacker may be undefined when isdefined(b_track_stats)... the 2029 attacker read is taken BEFORE the 2032 clear only from an existing struct; function_6da86ae is called in playerlaststand immediate-elimination branch749, not normal downed761-829. Snapshot446 can retain undefined attacker; revive_success captures it only when params and attacker are defined2027-2030. Undefined attacker can therefore reach the later callback on a normal downed/revive source path too; other elimination/bleedout fallback callers do not guarantee this path - bounded alternative; callback arg may carry undefined attacker."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b502eef18cc37fae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b502eef18cc37fae.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00149` at JSON pointer ``; file SHA-256 `334a7f9aaf8a1d9a612626b56fbf633f1237ae63a07912d29001a12c71069f4f`.

- `scripts/mp_common/laststand_warzone.csc::__init__` (original lines 22-40): No standalone body contract is available in this selected summary. Available classification: registered_system_pre_or_post_initializer.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/b502eef18cc37fae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b502eef18cc37fae.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/616`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `7937a15be9e19b353fc7f547322d1f252e223a919a47d4c8f58e9462bfae6d05`.

- `scripts/mp_common/laststand_warzone.csc::__init__system__` (original lines 13-16): No standalone body contract is available in this selected summary. Available classification: autoexec_registration_inventory; native invocation/load order unverified.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/b502eef18cc37fae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b502eef18cc37fae.json) at JSON pointer `/claims/3`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/617`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `0b41373e4cfad5c009fa247377bca00431ddc6310d6735347fa24fffb3bd9ae7`.

- `scripts/mp_common/laststand_warzone.csc::__init__` (original lines 22-40): No standalone body contract is available in this selected summary.

  unknowns: &#91;"Source statements only; VM native loader/event/order/assert/getter/object semantics are not verified.", "Exact originating retail build, PS4 binary/asset mapping, native/server implementation and gameplay execution remain open.", "Conditional/dev candidate: source review does not establish HMH load reachability or execution.", "Opaque source hashes and field/function names are preserved; no hash-name recovery is claimed.", "Stored callbacks and launched threads are later-body boundaries; this review does not execute or reconstruct them.", "Unresolved/opaque callsites are retained exactly; source availability versus native identity needs manager reconciliation."&#93;

  status: source_semantic_contract_ready_for_manager_review

  Complete explanatory fields: [exact projection](../../provenance/documentation/b502eef18cc37fae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b502eef18cc37fae.json) at JSON pointer `/claims/4`.

  Archived evidence ID: `archived-record-00002` at JSON pointer `/contracts/204`; file SHA-256 `14d82864f03d391c58ddc8caaf6f84c482f72ea05ab80940d42da35eabc0a97e`; selected record SHA-256 `7c177a937c19bd0650982679f677291624e4a0e384742e37c22df61490e7ff9b`.

- `scripts/mp_common/laststand_warzone.csc::__init__` (original lines 22-40): No standalone body contract is available in this selected summary.

  unknowns: &#91;"Source statements only; VM native loader/event/order/assert/getter/object semantics are not verified.", "Exact originating retail build, PS4 binary/asset mapping, native/server implementation and gameplay execution remain open.", "Conditional/dev candidate: source review does not establish HMH load reachability or execution.", "Opaque source hashes and field/function names are preserved; no hash-name recovery is claimed.", "Stored callbacks and launched threads are later-body boundaries; this review does not execute or reconstruct them.", "Unresolved/opaque callsites are retained exactly; source availability versus native identity needs manager reconciliation."&#93;

  status: source_semantic_contract_ready_for_manager_review

  Complete explanatory fields: [exact projection](../../provenance/documentation/b502eef18cc37fae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b502eef18cc37fae.json) at JSON pointer `/claims/5`.

  Archived evidence ID: `archived-record-00002` at JSON pointer `/contracts/204`; file SHA-256 `14d82864f03d391c58ddc8caaf6f84c482f72ea05ab80940d42da35eabc0a97e`; selected record SHA-256 `7c177a937c19bd0650982679f677291624e4a0e384742e37c22df61490e7ff9b`.
