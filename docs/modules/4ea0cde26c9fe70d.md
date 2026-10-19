# scripts/core_common/flagsys_shared.csc

Project-added notes. See the [code](../../src/scripts/core_common/flagsys_shared.csc).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `f4b9a51f8b7fcfcb6d158303d3fd5fff2fcfb6ac`. Original SHA-256: `9b8c6b3443a9d0f1fb54bbb094dcbdadd3f7b318be9c4d2b8a68ebdaa8e20778`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/4ea0cde26c9fe70d.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh-gap:HMH-GAP-STARTUP:run_post_systems@system_shared.csc` (original lines 9-18): Source-visible answer: the batch postinit driver, the terminal point of the ordering graph. It iterates the whole registry: for each entry run the requirement resolver (88) and spawn exec_post_system (89); after iterating set the level flag system_init_complete (92) - the signal every system::wait_till blocks on - and destroy the registry (93), without a join proving postfunc completion. register can recreate the cleared table; clearing does not prove lifetime inactivity. Its single caller is the native level_finalizeinit event handler codecallback_finalizeinitialization (callbacks_shared.gsc 1095 / csc 502). Sequence inside one native event: run_post_systems() THEN callback(#on_finalize_initialization) (1096) - so wz_open_skyscrapers gsc/csc on_finalize_initialization handlers (registered at wz_open_skyscrapers.gsc 47 / .csc 27; bodies gsc 129-133 / csc 81-85 leading to the wzheavymetalheroes-gated hmh_ramp dynent enable function_7276b578 gsc 160-175) are dispatched after the driver has spawned its batch, set the flag and cleared the registry; this does not establish that all spawned postfuncs have completed. Exact native-entry boundary: the event name and handler annotation event_handler&#91;level_finalizeinit&#93; (callbacks_shared.gsc 1093) are source-recorded; the engine call site and event order are not - recorded as the exact minimum evidence request.

  unknowns: &#91;"Engine call site/order of level_finalizeinit (native)", "Completion guarantee of spawned postinits before the finalize callback dispatch (native scheduler)", "Retail behavior after registry clear (any register() call would recreate level.system_funcs)"&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/4ea0cde26c9fe70d-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/4ea0cde26c9fe70d.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00072` at JSON pointer ``; file SHA-256 `5dd83a6f593ad1f1423431c250f4d6a2cb8958980f51650c6b73221c44d88ef2`; selected record SHA-256 `76cfd3b6723685a7f77307c35a90363a293e7c7b600190611b4a16cf398acd2e`.

- `hmh07-deps7:012` (original lines 3-3, 76-76): Developer-block namespace scene helper accepts str_scene. Either exact placeholder <dev string:x38> or <dev string:x1e7> skips querying and yields integer 0. Other values query level flagsys::get(str_scene+<dev string:x1f9>); return integer 1 only on a truthy result, otherwise integer 0. Preserve its suffix as distinct from is_scene_playing. This reads source flag state, not independently verified scene initialization.

  unknowns: &#91;"developer block inclusion and runtime activation", "opaque developer-string content", "effective level flags and actual initialization"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/4ea0cde26c9fe70d-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/4ea0cde26c9fe70d.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00445` at JSON pointer `/units/11`; file SHA-256 `a7bb2e5aea8ad75c41ab65ff86c473160dd796a9f767c1cb89e03414cd2434a5`; selected record SHA-256 `0fbe145eaf5a680b6af0982d82dfc66927023be4ffa860f64e44fbbb220d5512`.

- `scripts/core_common/flagsys_shared.csc::wait_till_clear` (original lines 186-194): No standalone body contract is available in this selected summary. Available classification: conditional_autoexec_or_registration_candidate_with_unproven_load_reachability.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/4ea0cde26c9fe70d-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/4ea0cde26c9fe70d.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/862`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `32a2533a244aa1f8ddda4824cc82dc4d7afb6667c251fcdb3272d3215a72ae64`.

- `hmh07-deps7:011` (original lines 3-3, 76-76): Developer-block namespace scene helper accepts str_scene. For either literal recovered placeholder <dev string:x38> or <dev string:x1e7>, skip the flag query and return integer 0. Otherwise query flagsys::get on level using str_scene+<dev string:x1ee>. A truthy query returns integer 1; a false result falls through to integer 0. This is a flag predicate rather than proof that a scene is actually playing. Opaque dev strings are retained verbatim and no shipping-build exclusion is inferred.

  unknowns: &#91;"developer block presence/activation in original build", "real values of recovered dev strings", "actual level flags and engine/VM flag semantics"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/4ea0cde26c9fe70d-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/4ea0cde26c9fe70d.json) at JSON pointer `/claims/3`.

  Archived evidence ID: `archived-record-00445` at JSON pointer `/units/10`; file SHA-256 `a7bb2e5aea8ad75c41ab65ff86c473160dd796a9f767c1cb89e03414cd2434a5`; selected record SHA-256 `5ac8b57d25c9227e415c9b883aefd1e8c626850063fa0b10bf9ed34e4c567ea8`.

- `scripts/core_common/flagsys_shared.csc::set` (original lines 9-18): No standalone body contract is available in this selected summary. Available classification: available_first_section_synchronous_helper.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/4ea0cde26c9fe70d-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/4ea0cde26c9fe70d.json) at JSON pointer `/claims/4`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/861`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `ad705c7f47ba7166a16d582f52defe9225d3c03f6351ffb6d6a2afdcb2e4082b`.

- `hmh-gap:HMH-GAP-STARTUP:wait_till@system_shared.csc` (original lines 85-93, 9-18): The selected wait_till(required_systems) helper160-163 never reads its argument and only requests level flagsys::wait_till("system_init_complete"). This API therefore does not select a named per-system dependency. The compared run_post_systems84-94 driver launches exec_post_system threads during88-93, then requests the system_init_complete flag and clears the registry without joining those workers. That flag is a post-driver launch-iteration signal, not proof every postfunc completed. The flagsys helper85-93 checks get(str_flag), waits while falsey and rechecks; a truthy flag at entry avoids the local wait. Exact native wake/death/error handling and scheduling remain unknown. Observed bounded callers include util_shared.gsc __main__45, mp_common/load.gsc35 and load.csc37; the latter are called from wz_open_skyscrapers.gsc53 / csc30. zm_common/load.csc76 and zm/load.gsc59 are context-only callers. The util postfunc itself waits at45 and still has function_3cb7a62d46 to execute after it resumes; no author-intent or all-postfunc-completion inference follows. The load callers request load_main_complete at their following36/38 statements if control reaches them after the observed flag. A persistent falsey flag with no cancellation/other exit can retain the wait; there is no local timeout. Missing level_finalizeinit is a possible unmet-producer condition, not proof that no dynamic/other writer or native exit can exist.

  unknowns: &#91;"Original retail level_finalizeinit delivery, actual flag producers and native scheduling/wakeup/cancellation behavior; unmet flag can retain a wait but no universal hang outcome is proved.", "Level 'death' endon semantics on level-owned waits (native)", "This selected API ignores required_systems and observes only the shared flag; any finer dependency/completion requirement needs separately evidenced support."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/4ea0cde26c9fe70d-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/4ea0cde26c9fe70d.json) at JSON pointer `/claims/5`.

  Archived evidence ID: `archived-record-00006` at JSON pointer ``; file SHA-256 `97bf508b7c3b1f9a42326e062eea6be8f2ec56919b5d8f245894e4cfcbe0c54b`.

- `scripts/core_common/flagsys_shared.csc::set` (original lines 9-18): No standalone body contract is available in this selected summary. Available classification: synchronous_startup_shared_callee.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/4ea0cde26c9fe70d-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/4ea0cde26c9fe70d.json) at JSON pointer `/claims/6`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/320`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `c88e7b06bc2af67fde6107e7ccfe27155b0fa1a114fb7a68c7070188ecc4fffb`.

- `scripts/core_common/flagsys_shared.csc::wait_till_clear` (original lines 186-194): No standalone body contract is available in this selected summary. Available classification: synchronous_startup_shared_callee.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/4ea0cde26c9fe70d-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/4ea0cde26c9fe70d.json) at JSON pointer `/claims/7`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/322`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `1e5c6c1cff0a9040343d679e7c10ef273e9596a1df6d342e366b05d0e779ec85`.

- `scripts/core_common/flagsys_shared.csc::wait_till` (original lines 85-93): No standalone body contract is available in this selected summary. Available classification: synchronous_startup_shared_callee.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/4ea0cde26c9fe70d-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/4ea0cde26c9fe70d.json) at JSON pointer `/claims/8`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/321`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `6a93d8de0efc60a2b6a8811dde5cc73a8a4dcd1e1007249ec4cba7b8f6268d38`.

- `hmh-gap:HMH-GAP-STARTUP:exec_post_system@system_shared.gsc` (original lines 85-93): Server twin of unit 2 (identical text, gsc lines 35-52). Source-visible: ignore/undefined skip, postdone=1 BEFORE synchronous &#91;&#91;postfunc&#93;&#93;(), req-resolver call first; reached solely from run_post_systems (89) and function_5095b2c6 (69/76) within the same file. Server-side post ordering: level_finalizeinit -> codecallback_finalizeinitialization (callbacks_shared.gsc 1093-1097, the server copy) -> run_post_systems -> spawned exec_post_system per entry -> flag system_init_complete + registry clear (84-94) -> callback(#on_finalize_initialization). No per-requirement join anywhere - requirement postinits are fire-and-forget spawns re-guarded here (37-42). Native-entry boundary unchanged from unit 2 (event pump order/ordering unproven).

  unknowns: &#91;"Server VM spawn interleaving", "level_finalizeinit engine order", "retail assert fidelity"&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/4ea0cde26c9fe70d-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/4ea0cde26c9fe70d.json) at JSON pointer `/claims/9`.

  Archived evidence ID: `archived-record-00035` at JSON pointer `/units/10`; file SHA-256 `6e442cbb5b6ce45aecb61bedd9a68f4a1a0abcc1cab9f330838bba82fb68b263`; selected record SHA-256 `060eec5e0796e66514cb9f5da2567ccec4e13f15f10a8c7d5211a92cb06cf4c6`.

- `scripts/core_common/flagsys_shared.csc::get` (original lines 76-79): No standalone body contract is available in this selected summary. Available classification: synchronous_startup_shared_callee.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/4ea0cde26c9fe70d-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/4ea0cde26c9fe70d.json) at JSON pointer `/claims/10`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/319`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `e899e8b102abe2e2b14d684b46517ed43d42e2db4c7a7cb764c8f63402d5726d`.

- `hmh-gap:HMH-GAP-STARTUP:wait_till@system_shared.gsc` (original lines 85-93): Server twin of unit 8 (gsc 160-163 identical). Source-visible: sole blocking primitive; argument discarded; blocks on level flag system_init_complete produced only by run_post_systems (gsc 92). Server-side callers: util_shared.gsc __main__ 45 (util postfunc, yields inside the post phase until the driver sets the flag, without a join of spawned postfuncs) and mp_common/load.gsc main 35 (load::main called by wz_open_skyscrapers.gsc 53) which then sets load_main_complete (36). HMH lifecycle coupling: the HMH map main (level_init) therefore cannot proceed past load::main until system_init_complete is set after the spawn loop; statement order is &#91;spawn batch; set flag&#93; -> &#91;wait returns; load_main_complete&#93;, not proof that every postfunc completed -> subsequent wz loader steps (later lifecycle owner's dependency). Deadlock shape retained: if level_finalizeinit never fires in a session, load::main never completes (no timeout in source).

  unknowns: &#91;"level_finalizeinit retail delivery guarantee (hang condition)", "level death/shutdown interaction", "other retail flag writers outside corpus"&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/4ea0cde26c9fe70d-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/4ea0cde26c9fe70d.json) at JSON pointer `/claims/11`.

  Archived evidence ID: `archived-record-00008` at JSON pointer ``; file SHA-256 `8114fe3123c21b780c27d038cc05193cca5ed4fa5ddc0e46b2a1aea92899d43a`; selected record SHA-256 `945d7100cef89afce95c9d0de3a6daf05ebb901766a80fb896804cb3c4e84b32`.

- `hmh-gap:HMH-GAP-STARTUP:exec_post_system@system_shared.csc` (original lines 9-17): Source-visible answer: postinit invocation body; skips undefined, ignored or already-postdone entries; an eligible !postdone branch resolves requirements before setting the marker, with no recheck after that resolver and no proved prereq-stage scheduling or exactly-once guarantee, sets postdone BEFORE invoking postfunc (49-50), and the bounded literal caller query finds run_post_systems (89) and the post-requirement resolver function_5095b2c6 (69/76) in the supplied twins; this does not prove absence of indirect, dynamically selected or native callers. Dependency 'wait' is fire-and-forget thread spawn, not a join. Ordering graph: level_finalizeinit -> run_post_systems -> foreach &#91;function_5095b2c6 asserts predone||ignore, thread exec_post_system(func)&#93; -> postfunc bodies run as spawned threads; run_post_systems requests the flag, without joining postfunc completion, by setting flag system_init_complete (92) AFTER all threads are spawned, then the registry is cleared (93). HMH linkage: wz/HMH postfuncs (e.g. util_shared __main__ via system::wait_till, load consumers) synchronize on that flag; wz_open_skyscrapers on_finalize_initialization (hmh_ramp dynent enable) is dispatched only after this phase by codecallback_finalizeinitialization callbacks_shared.gsc 1096. Ignore/duplicate/error: returns silently for undefined entries and ignore-flagged records (37-40); retail assert semantics unresolved.

  unknowns: &#91;"VM thread scheduling of the spawned exec_post_system calls relative to each other and to the foreach (native scheduler)", "level_finalizeinit vs level_init/gametype_init native order (conditional: for wz_open_skyscrapers registration to be delivered the level_init main must precede level_finalizeinit; not proven)", "assert evaluation in retail"&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/4ea0cde26c9fe70d-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/4ea0cde26c9fe70d.json) at JSON pointer `/claims/12`.

  Archived evidence ID: `archived-record-00179` at JSON pointer ``; file SHA-256 `ef863dfba5d638b1ce484c4b76eecd0d217f648b932a91590fd230a785841f41`.

- `scripts/core_common/flagsys_shared.csc::wait_till` (original lines 85-93): No standalone body contract is available in this selected summary.

  unknowns: &#91;"Source statements only; VM native loader/event/order/assert/getter/object semantics are not verified.", "Exact originating retail build, PS4 binary/asset mapping, native/server implementation and gameplay execution remain open.", "Unresolved/opaque callsites are retained exactly; source availability versus native identity needs manager reconciliation."&#93;

  status: source_semantic_contract_ready_for_manager_review

  Complete explanatory fields: [exact projection](../../provenance/documentation/4ea0cde26c9fe70d-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/4ea0cde26c9fe70d.json) at JSON pointer `/claims/13`.

  Archived evidence ID: `archived-record-00002` at JSON pointer `/contracts/71`; file SHA-256 `14d82864f03d391c58ddc8caaf6f84c482f72ea05ab80940d42da35eabc0a97e`; selected record SHA-256 `37242ef426ba72be85a4b0ca2b8b1182a0f579450d82cc9c098e6b87aa2e28de`.

- `scripts/core_common/flagsys_shared.csc::get` (original lines 76-79): No standalone body contract is available in this selected summary.

  unknowns: &#91;"Source statements only; VM native loader/event/order/assert/getter/object semantics are not verified.", "Exact originating retail build, PS4 binary/asset mapping, native/server implementation and gameplay execution remain open.", "Unresolved/opaque callsites are retained exactly; source availability versus native identity needs manager reconciliation."&#93;

  status: source_semantic_contract_ready_for_manager_review

  Complete explanatory fields: [exact projection](../../provenance/documentation/4ea0cde26c9fe70d-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/4ea0cde26c9fe70d.json) at JSON pointer `/claims/14`.

  Archived evidence ID: `archived-record-00002` at JSON pointer `/contracts/70`; file SHA-256 `14d82864f03d391c58ddc8caaf6f84c482f72ea05ab80940d42da35eabc0a97e`; selected record SHA-256 `27003be60383cf73dff904a06f7513a17425dfc772ae2891b4d4320d3617af02`.

- `scripts/core_common/flagsys_shared.csc::get` (original lines 76-79): No standalone body contract is available in this selected summary.

  unknowns: &#91;"Source statements only; VM native loader/event/order/assert/getter/object semantics are not verified.", "Exact originating retail build, PS4 binary/asset mapping, native/server implementation and gameplay execution remain open.", "Unresolved/opaque callsites are retained exactly; source availability versus native identity needs manager reconciliation."&#93;

  status: source_semantic_contract_ready_for_manager_review

  Complete explanatory fields: [exact projection](../../provenance/documentation/4ea0cde26c9fe70d-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/4ea0cde26c9fe70d.json) at JSON pointer `/claims/15`.

  Archived evidence ID: `archived-record-00002` at JSON pointer `/contracts/70`; file SHA-256 `14d82864f03d391c58ddc8caaf6f84c482f72ea05ab80940d42da35eabc0a97e`; selected record SHA-256 `27003be60383cf73dff904a06f7513a17425dfc772ae2891b4d4320d3617af02`.

- `scripts/core_common/flagsys_shared.csc::wait_till` (original lines 85-93): No standalone body contract is available in this selected summary.

  unknowns: &#91;"Source statements only; VM native loader/event/order/assert/getter/object semantics are not verified.", "Exact originating retail build, PS4 binary/asset mapping, native/server implementation and gameplay execution remain open.", "Unresolved/opaque callsites are retained exactly; source availability versus native identity needs manager reconciliation."&#93;

  status: source_semantic_contract_ready_for_manager_review

  Complete explanatory fields: [exact projection](../../provenance/documentation/4ea0cde26c9fe70d-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/4ea0cde26c9fe70d.json) at JSON pointer `/claims/16`.

  Archived evidence ID: `archived-record-00002` at JSON pointer `/contracts/71`; file SHA-256 `14d82864f03d391c58ddc8caaf6f84c482f72ea05ab80940d42da35eabc0a97e`; selected record SHA-256 `37242ef426ba72be85a4b0ca2b8b1182a0f579450d82cc9c098e6b87aa2e28de`.
