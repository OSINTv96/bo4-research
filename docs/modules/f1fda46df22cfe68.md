# scripts/core_common/scoreevents_shared.gsc

Project-added notes. See the [code](../../src/scripts/core_common/scoreevents_shared.gsc).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `f4b9a51f8b7fcfcb6d158303d3fd5fff2fcfb6ac`. Original SHA-256: `b6e72beebaa342a154e9feac98dab7e954a696d2462243dabd0a6342f7eac4c8`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/f1fda46df22cfe68.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

Dependency decisions: [exact edge records](../../provenance/dependency-decisions.json). Included callees remain at the bounded static scopes recorded there.

- [AV0024](../../provenance/dependency-decisions/AV0024.json): `src/scripts/abilities/gadgets/gadget_smart_cover.gsc` to `scripts/core_common/scoreevents_shared.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `processscoreevent`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0047](../../provenance/dependency-decisions/AV0047.json): `src/scripts/mp_common/player/player_damage.gsc` to `scripts/core_common/scoreevents_shared.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `processscoreevent`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0055](../../provenance/dependency-decisions/AV0055.json): `src/scripts/mp_common/laststand_warzone.gsc` to `scripts/core_common/scoreevents_shared.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `processscoreevent`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0146](../../provenance/dependency-decisions/AV0146.json): `src/scripts/mp_common/gametypes/globallogic_score.gsc` to `scripts/core_common/scoreevents_shared.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `isregisteredevent`, `processscoreevent`, `shouldaddrankxp`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0177](../../provenance/dependency-decisions/AV0177.json): `src/scripts/wz_common/wz_progression.gsc` to `scripts/core_common/scoreevents_shared.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `processscoreevent`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0184](../../provenance/dependency-decisions/AV0184.json): `src/scripts/wz_common/wz_medals.gsc` to `scripts/core_common/scoreevents_shared.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `processscoreevent`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0311](../../provenance/dependency-decisions/AV0311.json): `src/scripts/mp_common/player/player_killed.gsc` to `scripts/core_common/scoreevents_shared.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `decrementlastobituaryplayercountafterfade`, `isregisteredevent`, `processscoreevent`, `uninterruptedobitfeedkills`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0334](../../provenance/dependency-decisions/AV0334.json): `src/scripts/killstreaks/mp/supplydrop.gsc` to `scripts/core_common/scoreevents_shared.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `givecratecapturemedal`, `processscoreevent`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0346](../../provenance/dependency-decisions/AV0346.json): `src/scripts/killstreaks/mp/uav.gsc` to `scripts/core_common/scoreevents_shared.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `processscoreevent`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0358](../../provenance/dependency-decisions/AV0358.json): `src/scripts/abilities/gadgets/gadget_jammer_shared.gsc` to `scripts/core_common/scoreevents_shared.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `processscoreevent`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0485](../../provenance/dependency-decisions/AV0485.json): `src/scripts/mp_common/laststand.gsc` to `scripts/core_common/scoreevents_shared.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `processscoreevent`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0518](../../provenance/dependency-decisions/AV0518.json): `src/scripts/weapons/sensor_dart.gsc` to `scripts/core_common/scoreevents_shared.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `processscoreevent`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0530](../../provenance/dependency-decisions/AV0530.json): `src/scripts/weapons/trophy_system.gsc` to `scripts/core_common/scoreevents_shared.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `processscoreevent`. Source-only conditional selection; refer to the full edge record for caller lines and gates.
