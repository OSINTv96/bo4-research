# scripts/core_common/healthoverlay.gsc

Project-added notes. See the [code](../../src/scripts/core_common/healthoverlay.gsc).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `f4b9a51f8b7fcfcb6d158303d3fd5fff2fcfb6ac`. Original SHA-256: `000ee8fa1c8c2b74b78844e2b068bb235fbfb4d0442c54a94989021e620c62ea`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/af5cfb2c8115dd0a.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `scripts/core_common/healthoverlay.gsc::__init__` (original lines 27-59): No standalone body contract is available in this selected summary. Available classification: registered_system_pre_or_post_initializer.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/af5cfb2c8115dd0a-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/af5cfb2c8115dd0a.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/336`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `6ada508187e1f056327c51daa0a0c8751d70b4b749c78ca4e48bc730f8844bdd`.

- `hmh-health:HMH-HEALTH-RECOVERY-01:damage-gates` (original lines 625-668, 565-583, 328-360, 704-705, 670-690, 704-705, 467-500, 366-389, 505-525, 340-360, 646-679, 340-360, 625-690, 605-619, 565-583, 646-690, 704-705, 605-619, 625-690, 625-690, 704-705, 670-690, 704-705, 366-389, 491-525, 467-493, 366-389, 366-389, 675-683, 366-389, 491-500, 625-658, 340-347, 328-334, 349-352, 653-679, 704-705, 354-357, 653-679, 565-583, 646-668, 328-334, 447-460, 646-679, 704-705, 340-389, 605-619, 625-690, 328-389, 447-460, 467-525, 565-583, 605-619, 625-705): The added connection is a conditional sampled-health contract. Once the saved tick's earlier gates pass, health lower than old_health records the current polling time in var_ba47a7a3 and skips heal for that call; equal or higher health goes to heal instead (healthoverlay.gsc:625-690,704). Damage table callbacks, laststand_damage notify, local health++ and the later finishplayerdamage boundary are separate channels, so a damage notification does not by itself establish this timestamp or net health loss (player_damage.gsc:132-156,625-644). Downed/remote-control gates normally leave the old sample and delay marker untouched; full-health return refreshes old_health, while a lower-cap return writes health without refreshing old_health (healthoverlay.gsc:340-360,565-583,646-668). After revive clears laststand, the next eligible call can therefore see restored health against an older pre-down sample unless the owning lifecycle route has replaced the table; revive does not itself reset these fields in its cited transition (laststand_warzone.gsc:2007-2056; healthoverlay.gsc:605-619,675-704). For positive regen_delay, exact elapsed==delay passes the time gate, but positive delay and health below var_66cb03ad are still required. ignore_health_regen_delay skips only the elapsed comparison; disable_health_regen_delay writes marker=1, which is not an unconditional bypass for every clock/delay pair (healthoverlay.gsc:366-389). These are recovered-source conditions, not PS4 outcomes, event ordering, an effective HMH setting or a new whole-body reconstruction.

  unknowns: &#91;"No read-order winner is assumed between damage callbacks, their listeners, native health writes, laststand clear, revive wait/native return and polling.", "A damage event can be rejected, deferred, reflected, offset or health-gated; its payload and fatal return do not establish this tick's H<O branch. Exact damage accounting/engine event posting is outside this bounded connection.", "Same-table post-revive examples are conditional. Root decides source init/restart reachability; this record does not assert that every revive, spawn or redeploy replaces or preserves the table.", "Source asserts do not establish valid runtime ranges. Numeric cases use explicitly defined finite positive baselines/caps/delays except the stated zero/negative boundary; undefined values, invalid cap, numeric coercion and native failure behavior are not guessed.", "Prior author records and labels remain unchanged and awaiting independent review. New exact comparisons are dependency algebra only, not a retrospective correctness review or a runtime defect finding.", "Passing the delay gate does not prove healing: amount0/later clamp or native field behavior can prevent an observed increase; heal_policy owns the producer/rate conditions.", "Whole-HMH, original online/server behavior and whole-function completion are not established by this one bounded answer."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/af5cfb2c8115dd0a-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/af5cfb2c8115dd0a.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00145` at JSON pointer ``; file SHA-256 `9ff1715c882c68ccb33c6af9dda00843abb62fe15f4cad1d9bdf8ea4d63870ff`; selected record SHA-256 `fb968c0f12c9658788af3adab15bf810bbdd2b5e8748b9d1c24a408f6d3febe5`.

- `hmh-health:HMH-HEALTH-RECOVERY-01:heal-policy` (original lines 27-59, 467-494, 366-389, 395-441, 447-461, 496-546, 340-359, 670-684): The conditional HMH producer-to-consumer connection is now pinned: init_heal creates the exact enabled/rate/delay-mode/cap fields only when the table is absent; the value setter and gadget write enabled, the gadget builds rate/cap, and healthoverlay consumes them. Stored rate0 selects a default-rate path when enabled, while enabled0 blocks the ordinary rate path. The separate var_44d52546 force branch bypasses that rate block but still follows delay/cap/tick admission. Stored cap0 means use var_66cb03ad, including after exempt damage drains the stored cap to0. Spawn and completion reset only their shown fields; no guaranteed automatic re-enable on revive is established. These are recovered-source conditions, not effective HMH settings or original PS4 behavior. &#91;init-fields, value-writes, gadget-build, rate-consumer, cap-consumer, consumer-delay, consumer-force-write, force-producer, gadget-damage, gadget-spawn, gadget-stop, revive-state, revive-tail&#93;

  unknowns: &#91;"Declared defaults (new_health_model1, health_regen1, delay-control0, preamble dvar0, revive-health source write50) are not confirmed effective HMH values. No producer policy precedence or callback order was selected.", "Gadget helper function_820a63e9 may have side effects that affect pending preambles; the direct source reset only emits healing_disabled if heal_end is reached. No cancellation guarantee or observed defect is claimed.", "Rates use the exact source arithmetic. Neither weapon.var_4465ef1e units nor fallback role/n_regen inputs, quickrevive multiplier dvar, optional additions or missing rate multiplier are resolved here. A fallback rate of0 can still be changed by the later switch; enabled==0 returns before that switch.", "Cap0 is a sentinel, including a cap drained to0. Actual tick ordering and delay after damage remain damage_gate-owned; no resulting healing observation is asserted.", "The force producer does not set enabled1 in its cited span. Actual caller selection, normal completion delivery, death/abnormal exit cleanup and cross-spawn force-flag lifetime remain unknown. No automatic restart or recovery was attempted.", "h4 saved398/503, all27 health-gadget records were already present in frozen PRIOR-BODIES; the105 unrelated missing records remain missing. Old h4 wording such as time-unit labels and opaque helper status remains unchanged and unreviewed; this report states only its newly pinned source connections."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/af5cfb2c8115dd0a-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/af5cfb2c8115dd0a.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00117` at JSON pointer ``; file SHA-256 `4550cea524030c60c76b94ec05f8597ddf3a1872bf37e4b3bbdeb9ec3d4df887`; selected record SHA-256 `c6cda09d8523852c6011163076f258a265467c60eb1fbeae0bdb63cf8a8848ec`.

- `hmh-health:HMH-HEALTH-RECOVERY-01:pump-lifecycle` (original lines 18-21, 27-68, 605-619, 625-657, 711-739, 625-668, 675-689, 74-106, 784-787, 824-828, 711-739, 340-360, 27-59, 711-739, 18-21, 27-68, 605-619, 625-657, 711-739, 625-668, 675-689, 74-106, 784-787, 824-828, 711-739, 340-360, 27-59, 711-739): The missing connection is a shared level pump with finite per-player state initialization. healthoverlay registers its preinit, chooses a model-specific spawn/restart target, then launches the pump in both branches. New-model initialization arms and replaces the player state; selected visits require a defined table and run the existing gated tick, then stamp the visit time after any normal tick return. Player stop events disarm without clearing the table or killing the level pump. T7 retains its separate entity loop and end_healthregen channel. Downed/revived state can pause/resume eligibility without a new initialization; a fresh delivered spawn or explicit restart replaces it. The server-level game_ended notify is the loop cancellation channel, separate from table callbacks, native matchflag and clientfields. Exact HMH effective model, build binding, VM scheduling/native clocks and event delivery remain unproved. The pump has no saved prior full-body contract, so this is a narrow source-only dependency answer with zero function-completion credit.

  unknowns: &#91;"Active HMH new_health_model and specialisthealspeed values; fallback defaults do not prove selected settings.", "Whether callbacks deliver multiple initializations or interleave with restart/tick; no order beyond same-thread source statements is established.", "A game-ended notification before pump arms may be missed; restart/reload timing outside this body remains unresolved.", "A stale defined state under legacy selection is not excluded; no dynamic-model switch policy is inferred.", "Pump is only a source anchor, not a prior/new complete-body contract; older h4 missing105 records remain missing and unrelated to root scope."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/af5cfb2c8115dd0a-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/af5cfb2c8115dd0a.json) at JSON pointer `/claims/3`.

  Archived evidence ID: `archived-record-00079` at JSON pointer ``; file SHA-256 `664c81b121b2b160b3bb470e284111bd4e498075ed26f8e57a21838a239d1228`; selected record SHA-256 `01737d9ae7828078f6aa94480620e2868896473774fef754a1a65a5f8b652b05`.

- `scripts/core_common/healthoverlay.gsc::__init__system__` (original lines 18-21): No standalone body contract is available in this selected summary. Available classification: autoexec_registration_inventory; native invocation/load order unverified.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/af5cfb2c8115dd0a-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/af5cfb2c8115dd0a.json) at JSON pointer `/claims/4`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/337`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `b554b292b33634ebf0ffeb27d7b33feb15419d7c2ff3cf81664e047afdd4d2d1`.

- `hmh-use:HMH-HEAL-ACTIVATION-01:health-item-debit` (original lines 491-539, 505-517, 340-359, 395-402): Connected enable_healing to the conditional self-owned inventory hook and its asynchronous slot10 debit. The hook captures the current network ID, not the activation weapon. Count1→0 can schedule deferred removal; count0 underflows to a clamped0 and exits before that removal. The passed third0 does not suppress the use body. Health mutation and completion occur through separate admitted paths, so item spending is not proof of health gained. Narrow slot/weapon mutation edges are cited with helper/native limits; all claims remain source-only drafts. &#91;enable-prehook, slot-debit-hook, use-item, deferred-empty-removal, remove-slot, health-weapon-edge, health-write-completion&#93;

  unknowns: &#91;"No frozen full-body record for get_inventory_item, function_c48cd17f, remove_inventory_item, function_d019bf1d, function_520b16d6 or function_8214f1b6 was used. Only the narrow referenced identity/slot10/health-weapon edges needed to connect the old use and deferred-removal records are stated; their full contracts remain unassigned.", "The wrapper discards the first lookup and the thread resolves again. Original-build identity uniqueness, object alias lifetime and races with replacement/count replenishment/death are not proven.", "The code does not validate the captured slot10 item type or count at the wrapper. Invalid/malformed native inputs, assertion behavior and missing itementry/weapon fields are not normalized or guessed.", "Completion and interruption snippets show no direct inventory refund, but optional hooks, on_item_use listeners and other registered type23 audiences remain open. No claim that this is the only cost or that later callbacks cannot change count is made.", "The latest downed/damage/tick drafts remain unreviewed. A squad laststand branch does not enter enable_healing for that recipient; ordinary health admission rejects laststand. Revive does not establish automatic healing re-enable, effective settings or guaranteed normal-completion cleanup."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/af5cfb2c8115dd0a-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/af5cfb2c8115dd0a.json) at JSON pointer `/claims/5`.

  Archived evidence ID: `archived-record-00148` at JSON pointer ``; file SHA-256 `e811933533734e17e3889337d369401d19d30271c5dc1ef6ca7cfe49fbcc5809`; selected record SHA-256 `cf7c7000941f9a965bbb4ed57b10238159fa263110ae0956d966bf24ba885b17`.

- `scripts/core_common/healthoverlay.gsc::__init__system__` (original lines 18-21): No standalone body contract is available in this selected summary.

  unknowns: &#91;"Source statements only; VM native loader/event/order/assert/getter/object semantics are not verified.", "Exact originating retail build, PS4 binary/asset mapping, native/server implementation and gameplay execution remain open.", "Conditional/dev candidate: source review does not establish HMH load reachability or execution."&#93;

  status: source_semantic_contract_ready_for_manager_review

  Complete explanatory fields: [exact projection](../../provenance/documentation/af5cfb2c8115dd0a-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/af5cfb2c8115dd0a.json) at JSON pointer `/claims/6`.

  Archived evidence ID: `archived-record-00002` at JSON pointer `/contracts/79`; file SHA-256 `14d82864f03d391c58ddc8caaf6f84c482f72ea05ab80940d42da35eabc0a97e`; selected record SHA-256 `3df4bd1cb3cdc615b3680fe31e6ff09bfbfc7bf0b00b02abaeec9a8407ab3597`.

- `scripts/core_common/healthoverlay.gsc::__init__` (original lines 27-59): No standalone body contract is available in this selected summary.

  unknowns: &#91;"Source statements only; VM native loader/event/order/assert/getter/object semantics are not verified.", "Exact originating retail build, PS4 binary/asset mapping, native/server implementation and gameplay execution remain open.", "Conditional/dev candidate: source review does not establish HMH load reachability or execution.", "Opaque source hashes and field/function names are preserved; no hash-name recovery is claimed.", "Stored callbacks and launched threads are later-body boundaries; this review does not execute or reconstruct them.", "Unresolved/opaque callsites are retained exactly; source availability versus native identity needs manager reconciliation."&#93;

  status: source_semantic_contract_ready_for_manager_review

  Complete explanatory fields: [exact projection](../../provenance/documentation/af5cfb2c8115dd0a-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/af5cfb2c8115dd0a.json) at JSON pointer `/claims/7`.

  Archived evidence ID: `archived-record-00002` at JSON pointer `/contracts/80`; file SHA-256 `14d82864f03d391c58ddc8caaf6f84c482f72ea05ab80940d42da35eabc0a97e`; selected record SHA-256 `3d68093149d090c12e6261aaa22afdeedee62a855ed0d606c170362a15a1415f`.

- `scripts/core_common/healthoverlay.gsc::__init__system__` (original lines 18-21): No standalone body contract is available in this selected summary.

  unknowns: &#91;"Source statements only; VM native loader/event/order/assert/getter/object semantics are not verified.", "Exact originating retail build, PS4 binary/asset mapping, native/server implementation and gameplay execution remain open.", "Conditional/dev candidate: source review does not establish HMH load reachability or execution."&#93;

  status: source_semantic_contract_ready_for_manager_review

  Complete explanatory fields: [exact projection](../../provenance/documentation/af5cfb2c8115dd0a-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/af5cfb2c8115dd0a.json) at JSON pointer `/claims/8`.

  Archived evidence ID: `archived-record-00002` at JSON pointer `/contracts/79`; file SHA-256 `14d82864f03d391c58ddc8caaf6f84c482f72ea05ab80940d42da35eabc0a97e`; selected record SHA-256 `3df4bd1cb3cdc615b3680fe31e6ff09bfbfc7bf0b00b02abaeec9a8407ab3597`.

- `scripts/core_common/healthoverlay.gsc::__init__` (original lines 27-59): No standalone body contract is available in this selected summary.

  unknowns: &#91;"Source statements only; VM native loader/event/order/assert/getter/object semantics are not verified.", "Exact originating retail build, PS4 binary/asset mapping, native/server implementation and gameplay execution remain open.", "Conditional/dev candidate: source review does not establish HMH load reachability or execution.", "Opaque source hashes and field/function names are preserved; no hash-name recovery is claimed.", "Stored callbacks and launched threads are later-body boundaries; this review does not execute or reconstruct them.", "Unresolved/opaque callsites are retained exactly; source availability versus native identity needs manager reconciliation."&#93;

  status: source_semantic_contract_ready_for_manager_review

  Complete explanatory fields: [exact projection](../../provenance/documentation/af5cfb2c8115dd0a-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/af5cfb2c8115dd0a.json) at JSON pointer `/claims/9`.

  Archived evidence ID: `archived-record-00002` at JSON pointer `/contracts/80`; file SHA-256 `14d82864f03d391c58ddc8caaf6f84c482f72ea05ab80940d42da35eabc0a97e`; selected record SHA-256 `3d68093149d090c12e6261aaa22afdeedee62a855ed0d606c170362a15a1415f`.

Dependency decisions: [exact edge records](../../provenance/dependency-decisions.json). Included callees remain at the bounded static scopes recorded there.

- [AV0026](../../provenance/dependency-decisions/AV0026.json): `src/scripts/core_common/healthoverlay.gsc` to `scripts/core_common/player/player_stats.gsc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `function_dad108fa`. Source-only conditional selection; refer to the full edge record for caller lines and gates.

- [AV0027](../../provenance/dependency-decisions/AV0027.json): `src/scripts/core_common/healthoverlay.gsc` to `scripts/core_common/status_effects/status_effect_explosive_damage.gsc`; relevance_unresolved.

  Available and inspected. The caller has a #using but no literal namespace-qualified reference to this target. Loader/autoexec, dynamic references and HMH admission are not established by the include; no absence or exclusion inferred.
