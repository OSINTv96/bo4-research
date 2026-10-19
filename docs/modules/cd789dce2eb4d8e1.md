# scripts/mp_common/gametypes/globallogic_actor.gsc

Project-added notes. See the [code](../../src/scripts/mp_common/gametypes/globallogic_actor.gsc).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `f4b9a51f8b7fcfcb6d158303d3fd5fff2fcfb6ac`. Original SHA-256: `cdf23937cdf26b529584dc8eb227a78f30dfdd5f301d660454a5a72e8d7e084e`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/cd789dce2eb4d8e1.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh-combat:HMH-DAMAGE-DOWNED-01:admission` (original lines 50-59, 50-59): The new connection is a phase-aware input map, not another reconstruction of the old damage predicate. Ordinary spawn writes sessionteam=self.team and sessionstate=playing and refreshes spawntime before later on_player_spawned/insertion work. A redeploy batch merely threads the spawnclient route, whose admission/queue branches mean selection is not proof of a fresh spawn clock. Spectator camera/sessionstate and spectator sessionteam are distinct; should_do_player_damage vetoes only the latter. No explicit candocombat writer is present in the 2,632 frozen GSC/CSC references; its effective producer and original value remain unknown. Insertion holds, begin/teleport flags and HMH doublejump/fallheight branches do not directly write those inputs in the cited spans. Spawn protection is the script elapsed<=cached-ms comparison, checked here only with bit 8; equality counts. Native invulnerability is a separate earlier callback veto, with a visible warzonestaging value-registry chain to enable/disableinvulnerability but unresolved native effects and stacked resets. End_round writes postgame before onendround and the table/server-notify/clientfield end channels. Warzone's later game_ended matchflag pulse does not change that state and therefore does not reopen ordinary admission. Finally, ordinary game-over rejection does not erase the earlier postgame hook: allowed trigger-hurt/crush paths may already call finishplayerdamage as MOD_POST_GAME. All remaining old vetoes/returns are reused unchanged; none of these connections proves HMH runtime behavior or closes the native down-versus-kill decision.

  unknowns: &#91;"Original HMH playlist values for spawnprotectiontime, wzheavymetalheroes, wzplayerinsertiontypeindex, deathcirclerespawn and infectionMode are not supplied by this packet. Source defaults are not effective-session values.", "Actual per-player candocombat, native invulnerability and complete value-stack contents during transport, freefall, redeploy and end transitions are unknown.", "Whether a selected redeploy player passes mayspawn/queue gates and when native spawn/callback delivery completes remain unproved; isalive for downed players retains the d3/native gap.", "No equality/clock example in branch_matrix was executed in the game or in the GSC VM. They are literal source condition cases only.", "The scoped candocombat search does not cover external/unavailable services, engine code, dynamically indexed aliases or unlisted source."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/cd789dce2eb4d8e1-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/cd789dce2eb4d8e1.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00108` at JSON pointer ``; file SHA-256 `c1b5ed194ab6a598e2bbd1b763b0f82947e4eb944b7ad973ec466d1957b7e8e5`; selected record SHA-256 `6bf774a6e502a0a9d7123d402bb953ae59260f8b1aac3378fdb81ac9617f8300`.

Dependency decisions: [exact edge records](../../provenance/dependency-decisions.json). Included callees remain at the bounded static scopes recorded there.

- [AV0099](../../provenance/dependency-decisions/AV0099.json): `src/scripts/mp_common/gametypes/globallogic_actor.gsc` to `scripts/core_common/ai/systems/destructible_character.gsc`; include_conditional_source.

  The extended candidate source graph supplies an exact local/qualified call or stored-pointer path from a selected source entry. Callee source is now included conditionally; feasibility, loader/callback delivery, original binding and runtime behavior remain unproved. The earlier local-only decision is retained below.

  Selected callee candidates: `copydestructstate`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0100](../../provenance/dependency-decisions/AV0100.json): `src/scripts/mp_common/gametypes/globallogic_actor.gsc` to `scripts/core_common/ai/systems/gib.gsc`; relevance_unresolved.

  Available and inspected. The caller has a #using but no literal namespace-qualified reference to this target. Loader/autoexec, dynamic references and HMH admission are not established by the include; no absence or exclusion inferred.

- [AV0101](../../provenance/dependency-decisions/AV0101.json): `src/scripts/mp_common/gametypes/globallogic_actor.gsc` to `scripts/core_common/globallogic/globallogic_player.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `giveattackerandinflictorownerassist`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0102](../../provenance/dependency-decisions/AV0102.json): `src/scripts/mp_common/gametypes/globallogic_actor.gsc` to `scripts/core_common/scoreevents_shared.gsc`; relevance_unresolved.

  Available and inspected. The caller has a #using but no literal namespace-qualified reference to this target. Loader/autoexec, dynamic references and HMH admission are not established by the include; no absence or exclusion inferred.

- [AV0103](../../provenance/dependency-decisions/AV0103.json): `src/scripts/mp_common/gametypes/globallogic_actor.gsc` to `scripts/core_common/spawner_shared.gsc`; include_conditional_source.

  The extended candidate source graph supplies an exact local/qualified call or stored-pointer path from a selected source entry. Callee source is now included conditionally; feasibility, loader/callback delivery, original binding and runtime behavior remain unproved. The earlier local-only decision is retained below.

  Selected callee candidates: `spawn_think`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0104](../../provenance/dependency-decisions/AV0104.json): `src/scripts/mp_common/gametypes/globallogic_actor.gsc` to `scripts/weapons/weapon_utils.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `ismeleemod`. Source-only conditional selection; refer to the full edge record for caller lines and gates.
