# scripts/core_common/globallogic/globallogic_player.gsc

Project-added notes. See the [code](../../src/scripts/core_common/globallogic/globallogic_player.gsc).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `f4b9a51f8b7fcfcb6d158303d3fd5fff2fcfb6ac`. Original SHA-256: `a60e3878dd087a22bd7ec6d0635b05817106730f1aeaeec17cec1608f040b452`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/1d8bf5c3c9b2bcb9.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

Dependency decisions: [exact edge records](../../provenance/dependency-decisions.json). Included callees remain at the bounded static scopes recorded there.

- [AV0044](../../provenance/dependency-decisions/AV0044.json): `src/scripts/mp_common/player/player_damage.gsc` to `scripts/core_common/globallogic/globallogic_player.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `function_efd02c1d`, `giveattackerandinflictorownerassist`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0101](../../provenance/dependency-decisions/AV0101.json): `src/scripts/mp_common/gametypes/globallogic_actor.gsc` to `scripts/core_common/globallogic/globallogic_player.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `giveattackerandinflictorownerassist`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0304](../../provenance/dependency-decisions/AV0304.json): `src/scripts/mp_common/player/player_killed.gsc` to `scripts/core_common/globallogic/globallogic_player.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `allowedassistweapon`. Source-only conditional selection; refer to the full edge record for caller lines and gates.
