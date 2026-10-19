# scripts/core_common/player/player_stats.gsc

Project-added notes. See the [code](../../src/scripts/core_common/player/player_stats.gsc).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `f4b9a51f8b7fcfcb6d158303d3fd5fff2fcfb6ac`. Original SHA-256: `29c421d5b1d48f74b6fa242eddf3ab0527eec228e8d1e21bae06f13479b7ae42`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/158ad74a7febabed.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

Dependency decisions: [exact edge records](../../provenance/dependency-decisions.json). Included callees remain at the bounded static scopes recorded there.

- [AV0026](../../provenance/dependency-decisions/AV0026.json): `src/scripts/core_common/healthoverlay.gsc` to `scripts/core_common/player/player_stats.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `function_dad108fa`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0046](../../provenance/dependency-decisions/AV0046.json): `src/scripts/mp_common/player/player_damage.gsc` to `scripts/core_common/player/player_stats.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `function_b7f80d87`, `function_bb7eedf0`, `function_dad108fa`, `function_e24eec31`, `get_stat`, `set_stat`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0054](../../provenance/dependency-decisions/AV0054.json): `src/scripts/mp_common/laststand_warzone.gsc` to `scripts/core_common/player/player_stats.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `function_b7f80d87`, `function_d40764f3`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0057](../../provenance/dependency-decisions/AV0057.json): `src/scripts/wz_common/gametypes/warzone.gsc` to `scripts/core_common/player/player_stats.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `function_7a850245`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0061](../../provenance/dependency-decisions/AV0061.json): `src/scripts/mp_common/challenges.gsc` to `scripts/core_common/player/player_stats.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `function_dad108fa`, `function_e24eec31`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0067](../../provenance/dependency-decisions/AV0067.json): `src/scripts/wz_common/wz_contracts.gsc` to `scripts/core_common/player/player_stats.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `get_stat_global`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0071](../../provenance/dependency-decisions/AV0071.json): `src/scripts/mp_common/gametypes/globallogic.gsc` to `scripts/core_common/player/player_stats.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `function_7a850245`, `function_dad108fa`, `inc_stat`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0093](../../provenance/dependency-decisions/AV0093.json): `src/scripts/mp_common/player/player_connect.gsc` to `scripts/core_common/player/player_stats.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `function_6d50f14b`, `function_7a850245`, `function_ed81f25e`, `get_stat_global`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0145](../../provenance/dependency-decisions/AV0145.json): `src/scripts/mp_common/gametypes/globallogic_score.gsc` to `scripts/core_common/player/player_stats.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `function_baa25a23`, `function_bb7eedf0`, `function_dad108fa`, `function_e24eec31`, `function_ed81f25e`, `function_eec52333`, `get_stat`, `get_stat_global`, `set_stat`, `set_stat_global`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0149](../../provenance/dependency-decisions/AV0149.json): `src/scripts/mp_common/item_inventory.gsc` to `scripts/core_common/player/player_stats.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `get_stat_global`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0154](../../provenance/dependency-decisions/AV0154.json): `src/scripts/wz_common/vehicle.gsc` to `scripts/core_common/player/player_stats.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `get_stat_global`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0163](../../provenance/dependency-decisions/AV0163.json): `src/scripts/mp_common/player/player_loadout.gsc` to `scripts/core_common/player/player_stats.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `get_stat`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0176](../../provenance/dependency-decisions/AV0176.json): `src/scripts/wz_common/wz_progression.gsc` to `scripts/core_common/player/player_stats.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `function_62b271d8`, `function_7a850245`, `function_b7f80d87`, `function_baa25a23`, `function_d40764f3`, `function_dad108fa`, `function_ed81f25e`, `function_f94325d3`, `get_stat`, `get_stat_global`, `set_stat`, `set_stat_global`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0188](../../provenance/dependency-decisions/AV0188.json): `src/scripts/hashed/script/script_34e49e82e2f499e1.gsc` to `scripts/core_common/player/player_stats.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `function_d40764f3`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0213](../../provenance/dependency-decisions/AV0213.json): `src/scripts/mp_common/scoreevents.gsc` to `scripts/core_common/player/player_stats.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `function_af5584ca`, `function_dad108fa`, `function_e24eec31`, `function_eec52333`, `get_stat_global`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0232](../../provenance/dependency-decisions/AV0232.json): `src/scripts/core_common/death_circle.gsc` to `scripts/core_common/player/player_stats.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `function_d40764f3`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0246](../../provenance/dependency-decisions/AV0246.json): `src/scripts/wz_common/wz_array_broadcast.gsc` to `scripts/core_common/player/player_stats.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `function_d40764f3`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0251](../../provenance/dependency-decisions/AV0251.json): `src/scripts/abilities/mp/gadgets/gadget_smart_cover.gsc` to `scripts/core_common/player/player_stats.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `function_e24eec31`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0265](../../provenance/dependency-decisions/AV0265.json): `src/scripts/core_common/rank_shared.gsc` to `scripts/core_common/player/player_stats.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `get_stat`, `get_stat_global`, `set_stat_global`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0310](../../provenance/dependency-decisions/AV0310.json): `src/scripts/mp_common/player/player_killed.gsc` to `scripts/core_common/player/player_stats.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `function_baa25a23`, `function_e24eec31`, `function_eec52333`, `get_stat_global`, `set_stat_global`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0320](../../provenance/dependency-decisions/AV0320.json): `src/scripts/wz_common/wz_jukebox.gsc` to `scripts/core_common/player/player_stats.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `function_d40764f3`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0332](../../provenance/dependency-decisions/AV0332.json): `src/scripts/killstreaks/mp/supplydrop.gsc` to `scripts/core_common/player/player_stats.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `function_e24eec31`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0345](../../provenance/dependency-decisions/AV0345.json): `src/scripts/killstreaks/mp/uav.gsc` to `scripts/core_common/player/player_stats.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `function_e24eec31`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0359](../../provenance/dependency-decisions/AV0359.json): `src/scripts/wz_common/wz_blast_doors.gsc` to `scripts/core_common/player/player_stats.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `function_d40764f3`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0400](../../provenance/dependency-decisions/AV0400.json): `src/scripts/core_common/potm_shared.gsc` to `scripts/core_common/player/player_stats.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `get_stat`, `inc_stat`, `set_stat`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0443](../../provenance/dependency-decisions/AV0443.json): `src/scripts/wz_common/killstreaks/ultimate_turret.gsc` to `scripts/core_common/player/player_stats.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `function_dad108fa`, `function_e24eec31`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0521](../../provenance/dependency-decisions/AV0521.json): `src/scripts/killstreaks/ultimate_turret_shared.gsc` to `scripts/core_common/player/player_stats.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `function_dad108fa`, `function_e24eec31`. Source-only conditional selection; refer to the full edge record for caller lines and gates.
