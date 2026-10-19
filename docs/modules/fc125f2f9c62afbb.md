# hashed/script/script_71e26f08f03b7a7a.gsc

Project-added notes. See the [code](../../src/scripts/hashed/script/script_71e26f08f03b7a7a.gsc).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `f4b9a51f8b7fcfcb6d158303d3fd5fff2fcfb6ac`. Original SHA-256: `fcf098bbbf663d223b9eaafad37f0042a8bc2856f47be5ae88dc613c21dcc5cb`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/fc125f2f9c62afbb.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh-gap:HMH-GAP-STARTUP:function_5095b2c6@system_shared.gsc` (original lines 12-14): Server twin of unit 3 (gsc 58-78 identical). Source-visible: post requirement resolver with predone||ignore assert at 60 (post presupposes completed preinit or ignored record), array/scalar req spawning without join (64-76), registry-existence assert for scalar reqs. Sole exec_post_system-driven caller (46/88 loop). HMH linkage: the wz-relevant server registry entries with reqs (script_71e26f08f03b7a7a hash_280fe2667ed2d300 -> #item_supply_drop at 14; killstreaks/mp/supplydrop.gsc 44 and uav.gsc 28 -> #killstreaks) resolve here at post time - provided the bundles load (open).

  unknowns: &#91;"Spawn interleaving", "retail assert fidelity", "retail use of array reqs in loaded bundles"&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/fc125f2f9c62afbb-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fc125f2f9c62afbb.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00073` at JSON pointer ``; file SHA-256 `a5137b109631fd666051d263d96d7abd6603f736cce5e61050a4ee3bfb5ecf01`.

- `hashed/script/script_71e26f08f03b7a7a.gsc::__init__system__` (original lines 12-15): No standalone body contract is available in this selected summary. Available classification: conditional_autoexec_or_registration_candidate_with_unproven_load_reachability.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/fc125f2f9c62afbb-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fc125f2f9c62afbb.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/802`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `220973284e507531d3614d57f216780a2ef952664a35d683f892057384274836`.

- `hmh-gap:HMH-GAP-STARTUP:function_8dfa23e0@system_shared.csc` (original lines 14-14): Source-visible answer: the preinit requirement resolver; the pre-side twin of function_5095b2c6 WITHOUT the predone||ignore assert. If func.reqs is defined: array case asserts each element then thread-spawns exec_pre_system(level.system_funcs&#91;req&#93;) per element and returns (129-135); scalar case asserts the registry entry exists (138) and thread-spawns exec_pre_system for it (139). No waiting: dependency scheduling is asynchronous spawn-only; ordering between requirement and dependent preinits is scheduler-dependent, each spawned call re-checks undefined/ignore/predone before running, duplicates after completed predone are suppressed, but there is no in-progress guard for reentrant/yielding calls; VM scheduling remains unresolved. Two direct callers: exec_pre_system111 and run_pre_systems151. Driver resolution at151 is followed by executor spawn152; executor can resolve requirements again before predone is set. HMH linkage: registry entries loaded into the HMH VMs with reqs - observed wz-relevant scalar reqs: hash_280fe2667ed2d300 requires #item_supply_drop (script_71e26f08f03b7a7a.gsc 14), killstreaks supplydrop/uav require #killstreaks (supplydrop.gsc 44, uav.gsc 28) - these exact records are resolved by this function during level_preinit, provided the bundles load (open native boundary).

  unknowns: &#91;"Thread spawn ordering vs dependent (native VM scheduler)", "Retail assert handling", "Array-form reqs use in retail HMH bundles (unobserved)"&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/fc125f2f9c62afbb-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fc125f2f9c62afbb.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00074` at JSON pointer ``; file SHA-256 `09ca5f24279cde5f0c717290725b25bfb7d4223b6e5c600d11db11255dd18945`.

- `hashed/script/script_71e26f08f03b7a7a.gsc::__init__system__` (original lines 12-15): No standalone body contract is available in this selected summary. Available classification: autoexec_registration_inventory; native invocation/load order unverified.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/fc125f2f9c62afbb-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fc125f2f9c62afbb.json) at JSON pointer `/claims/3`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/182`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `408a97ccd0c6434c6369606b84ece8b9b6372d5d26a80eddd92fac04ae2d4926`.

- `hmh-gap:HMH-GAP-STARTUP:register@system_shared.gsc` (original lines 21-30): Server-VM twin of unit 1: byte-level answer identical (file scripts/core_common/system_shared.gsc sha bf6d03b7..., lines 9-29 textually equal to the csc). Everything recorded for unit 1 holds with the gsc file as the anchor: existing ignore=1 permits repeated duplicate-call early returns without clearing ignore, whether the record began as a placeholder or real registration later marked by ignore (11-15), pure state store with predone/postdone from pointer presence, ignore=0 (17-28). Server-VM-specific registrant evidence observed: mp_common/callbacks.gsc 23-26 (callback), util_shared.gsc 21-24, hashed gsc systems script_34e49e82e2f499e1.gsc (hash_18ce058ad321248f with extra autoexec __init reading wz setting pairs hash_3778ec3bd924f17c combos at 22-27), script_5f3e7d348fbc5283.gsc, script_71e26f08f03b7a7a.gsc (req item_supply_drop), script_7611295950bc2c87.gsc, killstreaks/mp/*.gsc. Ordering graph, dependency-wait facts and native-entry boundary are per unit 1; this record pins the SERVER (gsc) copy that the HMH rotation's gametype/map server VM would execute per the m1 unknown-#1 bundle question.

  unknowns: &#91;"Retail server VM registrant set (bundle loading)", "Separate per-VM registries (structural inference)", "Retail assert/bytecode fidelity"&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/fc125f2f9c62afbb-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fc125f2f9c62afbb.json) at JSON pointer `/claims/4`.

  Archived evidence ID: `archived-record-00075` at JSON pointer ``; file SHA-256 `0c2aa3a5450daa444e6e2fd941aa6d5e2db152ff06bc780ae838a57ea44107e4`.

- `hmh-gap:HMH-GAP-STARTUP:function_5095b2c6@system_shared.csc` (original lines 12-15): Source-visible answer: the post-phase requirement resolver. Ordering facts: (1) it asserts the function's preinit already completed (predone) or the system is ignore-flagged - post execution presupposes pre phase completion; (2) it walks reqs and thread-spawns exec_post_system for each required system without waiting; (3) array form asserts each requirement value is defined, not registry-entry existence; a defined absent name spawns exec_post_system(undefined), which returns at37-39. Only scalar form asserts registry-entry existence at75. Because both the array and single-req paths spawn and return, the requirement/dependent postinit ordering is scheduler-dependent, not synchronized - pre-phase completeness is asserted, with original VM assertion behavior still unknown. exec_post_system skips calls that observe ignore or postdone. It checks postdone before requirement resolution, then sets postdone after that resolution and before postfunc. There is no second postdone check after resolution, so once-only behavior across invocations admitted before the mark and unproved interleavings is not established. HMH linkage: this is the shared dependency-scheduling core the six HMH root candidates participate in via the registry; wz-side registries (e.g. hash_280fe2667ed2d300 reqs #item_supply_drop, script_71e26f08f03b7a7a.gsc 12-15; killstreak req chains supplydrop.gsc 44/uav.gsc 28) route through exactly this code. Missing native original-build facts are listed in native_gaps.

  unknowns: &#91;"Thread-interleaving of spawned requirement postinits vs dependent postinit (native scheduler)", "Retail assert handling", "No observed wz/HMH use of multi-element req arrays; whether any loaded system uses them in retail is a bundle-level question"&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/fc125f2f9c62afbb-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fc125f2f9c62afbb.json) at JSON pointer `/claims/5`.

  Archived evidence ID: `archived-record-00078` at JSON pointer ``; file SHA-256 `f26ffda8a43182c03e36846cc022f3a6e7204eeadf2cbf2586adfd37758b4fa6`.

- `hashed/script/script_71e26f08f03b7a7a.gsc::function_f0297225` (original lines 65-86): No standalone body contract is available in this selected summary. Available classification: synchronous_startup_shared_callee.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/fc125f2f9c62afbb-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fc125f2f9c62afbb.json) at JSON pointer `/claims/6`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/183`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `54a707211e0d447143dfec06c6209aed28999734fcfe0990ff9d6f1c4de17a6d`.

- `hashed/script/script_71e26f08f03b7a7a.gsc::__init__` (original lines 21-30): No standalone body contract is available in this selected summary. Available classification: registered_system_pre_or_post_initializer.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/fc125f2f9c62afbb-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fc125f2f9c62afbb.json) at JSON pointer `/claims/7`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/181`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `af438e1c0c8a70682e96c865257390e1ec32328d55ecea58c7e13ebe0eb73533`.

- `hmh-gap:HMH-GAP-STARTUP:register@system_shared.csc` (original lines 12-15): Source-visible answer: registration is state-only (no invocation); when an existing record has ignore=1, every repeated register call asserts that ignore flag and returns without clearing it; the record may be a placeholder or a previously real record marked by ignore (register assert only on .ignore, csc 11-15; ignore() sets ignore=1, csc 169-179). Ordering graph produced (see source_trace): autoexec __init__system__ -> register -> native level_preinit -> codecallback_preinitialization -> run_pre_systems -> exec_pre_system per entry; native level_finalizeinit -> codecallback_finalizeinitialization -> run_post_systems -> exec_post_system per entry -> set system_init_complete -> registry cleared -> on_finalize_initialization dispatch. Dependency waits: NONE - req-resolution spawns threads without joining (69/76), the only synchronization is the whole-batch flag "system_init_complete" (92) consumed by wait_till (162). Error behavior: all failures are assert() with dev strings; retail evaluation of assert is a native/build fact. HMH root/registrant linkage: the HMH map script wz_open_skyscrapers.gsc::main joins this mechanism by load::main -> system::wait_till("all") (wz_open_skyscrapers.gsc 53; load.gsc 35) and by callback::on_finalize_initialization registration (47) delivered inside codecallback_finalizeinitialization after run_post_systems; the mechanism therefore conditions the whole HMH map startup; the exact set of registrant systems loaded into the HMH server VM is the unresolved native bundle boundary (m1 unknowns #1).

  unknowns: &#91;"Which registrant script set and order the retail CUSA11100 HMH VM bundle actually loads (native bundle manifest question; m1 unknowns section 1)", "Whether retail script bytecode contains/executes assert() in system_shared (dev strings present; original bytecode fidelity unverified)", "Iteration order of foreach over level.system_funcs hash-keyed array (VM implementation detail, not in dump)", "Whether an early assert failure in retail aborts registration or is skipped (assert implementation native)"&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/fc125f2f9c62afbb-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fc125f2f9c62afbb.json) at JSON pointer `/claims/8`.

  Archived evidence ID: `archived-record-00082` at JSON pointer ``; file SHA-256 `7f1194dc637637a7eff664f35255ad2a4c198946028d8cba1ee8ff3697b24f3f`.

- `hashed/script/script_71e26f08f03b7a7a.gsc::__init__` (original lines 21-30): No standalone body contract is available in this selected summary.

  unknowns: &#91;"Source statements only; VM native loader/event/order/assert/getter/object semantics are not verified.", "Exact originating retail build, PS4 binary/asset mapping, native/server implementation and gameplay execution remain open.", "Conditional/dev candidate: source review does not establish HMH load reachability or execution.", "Unresolved/opaque callsites are retained exactly; source availability versus native identity needs manager reconciliation."&#93;

  status: source_semantic_contract_ready_for_manager_review

  Complete explanatory fields: [exact projection](../../provenance/documentation/fc125f2f9c62afbb-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fc125f2f9c62afbb.json) at JSON pointer `/claims/9`.

  Archived evidence ID: `archived-record-00002` at JSON pointer `/contracts/6`; file SHA-256 `14d82864f03d391c58ddc8caaf6f84c482f72ea05ab80940d42da35eabc0a97e`; selected record SHA-256 `2f04aeb1fa727ce3f9ac387d185546cb81cf9317652ee9f3455865d7af5991f1`.

- `hashed/script/script_71e26f08f03b7a7a.gsc::__init__` (original lines 21-30): No standalone body contract is available in this selected summary.

  unknowns: &#91;"Source statements only; VM native loader/event/order/assert/getter/object semantics are not verified.", "Exact originating retail build, PS4 binary/asset mapping, native/server implementation and gameplay execution remain open.", "Conditional/dev candidate: source review does not establish HMH load reachability or execution.", "Unresolved/opaque callsites are retained exactly; source availability versus native identity needs manager reconciliation."&#93;

  status: source_semantic_contract_ready_for_manager_review

  Complete explanatory fields: [exact projection](../../provenance/documentation/fc125f2f9c62afbb-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/fc125f2f9c62afbb.json) at JSON pointer `/claims/10`.

  Archived evidence ID: `archived-record-00002` at JSON pointer `/contracts/6`; file SHA-256 `14d82864f03d391c58ddc8caaf6f84c482f72ea05ab80940d42da35eabc0a97e`; selected record SHA-256 `2f04aeb1fa727ce3f9ac387d185546cb81cf9317652ee9f3455865d7af5991f1`.

Dependency decisions: [exact edge records](../../provenance/dependency-decisions.json). Included callees remain at the bounded static scopes recorded there.

- [AV0264](../../provenance/dependency-decisions/AV0264.json): `src/scripts/hashed/script/script_71e26f08f03b7a7a.gsc` to `scripts/mp_common/item_supply_drop.gsc`; relevance_unresolved.

  Available and inspected. Found caller/functions and lexical gates are recorded, but no matched non-dev reference has both a selected behavior-summary span and an identified callee body. A citation or namespace match alone cannot establish HMH admission. Missing exact root/callback-to-caller admission or bounded source contract stays explicit.
