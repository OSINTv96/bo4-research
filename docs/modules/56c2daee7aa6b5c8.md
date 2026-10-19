# scripts/wz_common/wz_common_mode_heavy_metal_heroes_fixup.gsc

Project-added notes. See the [code](../../src/scripts/wz_common/wz_common_mode_heavy_metal_heroes_fixup.gsc).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `f4b9a51f8b7fcfcb6d158303d3fd5fff2fcfb6ac`. Original SHA-256: `6c8c6e5a759729df12dd6266fa41b71c667e0eb1ae3202256b046f4c4cb694f7`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/56c2daee7aa6b5c8.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh-gap:HMH-GAP-SETTINGS:equipment` (original lines 28-53): equipment/weapons/jetpack/vehicle configuration for HMH, reusing prior contracts. PRIMARY SWITCH: wzheavymetalheroes (no recovered producer â€” unit 2) drives the heroes-specific equipment set: on spawn/perk stores setperk specialty_doublejump + specialty_fallheight (the heroes double-jump mobility) at warzone.gsc:828-831, item_inventory.gsc:1112-1116 and player_insertion.gsc:497-506 (the latter also threads level.var_618194f7, an insertion hook pointer whose writer is outside this pass); loadout suppliers wz_loadouts.gsc:31-50 â€” hash_7d8c969e384dd1c9 arms level.var_5c14d2e6, hash_4149d5d65eb07138 arms level.var_317fb13c, and wzheavymetalheroes overwrites BOTH with &function_9de0644f (proved last-true-wins); consumers item_world.gsc:519-528 (threads var_5c14d2e6 per player when either key truthy) and player_reinsertion.gsc:441-447 (reinsertion same for var_317fb13c). EQUIPMENT RE-FLOW (fixups): wz_common_mode_heavy_metal_heroes_fixup.gsc:28-53 builds item_replacer sets: per-stash gun lists (array_list_guns_dlc1, asylum, boxing_gym, clearing, construction, diner, dockyard, estate, factory, farm, farmtown, firing_range, fracking, ghosttown, graveyard, hijacked, hydro, lighthouse, nuketown, rivertown, hash_5295664b3252e2a7, support_structure, train_station, wind_turbine) every call appending the replacement list #heavy_metal_heroes_list_guns_dlc1 (and .csc:28 twin); wz_open_skyscrapers.gsc:60-64 sets level.var_2089aa11 = supply_drop_stash_parent_dlc1_heroes and registers heroes flare-gun stash replacement/count data via function_f0297225(supply_drop_stash_parent_dlc1_flare_gun_heroes,2,4); this registration does not spawn the stash; hashed script_71e26f08f03b7a7a.gsc:256-259 uses level.var_2089aa11 only when that parent is defined, var_6ed927a6 replacement is undefined and heroes is defined/truthy. Explicit replacement wins. start first waits for its flag and applies timing/count gates before threading function_2d47ee1e; heroes truth alone does not prove spawning. FLARE GUNS: wz_open_skyscrapers_fixup.gsc:30-33 enables the base stash parent dlc1 flare guns only when wzenableflareguns && !wzheavymetalheroes (explicit NOT-and; #wzenableflareguns is itself absent from all recovered HMH layers). RAMPS: hmh_ramp dynent array enable/disable (gsc 160-172, csc 91-128 both sites read wzheavymetalheroes). VEHICLES: wz_common/vehicle.gsc:3397 keeps self.deathmodel when NOT heroes; function_32607cfc (4094-4121) returns true immediately when wzheavymetalheroes (vehicle-availability/air distance bypass; stats-gated otherwise); death circle tank vehicles only when setting hash_6eb44149a8ac6dd1 truthy inside the mode-identity branch (wz_open_skyscrapers_death_circle.gsc:69-76; that hash appears ONLY in the neighboring base-warzone playlist entry at categories 2631-2644 value 0, not in any HMH layer â†’ value for HMH unknown). TABLE RULE VALUES that select equipment/vehicles (def-only, all conditional on the native store): wzenablebowieknife=1, wzenableoperatorweapons=1, wzenablecoinbag=1, wzenablemusclecar=1, wzenablesuv=1, wzenablehomewrecker=1, wzenablevendetta=1, wzenablereplacercar=0, wzenablepurifier=0 mask2; wzenableatv/wzenablemotorcycle appear ONLY in the neighboring base-warzone entry (8286-8313, value 0) not in HMH layers; the vehicle fixup switch wz_common_vehicles_fixup.gsc/.csc:102/127/163 reads wzenablemusclecar/enableatv/enablemotorcycle/enablesuv combinations â€” for HMH the atv/motorcycle keys are unset, so those branches are absent-key dependent. JETPACK: no recovered HMH-specific jetpack setting exists; the mobility change is the two perk grants above. FURTHER EXACT DEPENDENCIES: function_9de0644f body (heroes loadout supplier) and function_3fed57dd/a9b8fa06 alternatives; level.var_618194f7 writer; heavy_metal_heroes_list_guns_dlc1 and supply_drop stash asset bundles; hvolist bundle contents (m1); vehiclecustomsettings per vehicle (m2); native wzheavymetalheroes producer (units 2/4).

  unknowns: &#91;"wzheavymetalheroes and hash_6eb44149a8ac6dd1 effective values (no recovered producer; native settings contract gap)", "function_9de0644f/function_3fed57dd/function_a9b8fa06 body behavior (heroes loadout suppliers)", "heavy_metal_heroes_list_guns_dlc1 and stash/vehicle data-asset contents", "Which VMs execute the fixup scripts in an HMH session (HMH-GAP-STARTUP owner)"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/56c2daee7aa6b5c8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/56c2daee7aa6b5c8.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00525` at JSON pointer ``; file SHA-256 `5fdb685117c6f91037c09cbe25a97cbbcac7735d1641702427826245e9ea78b9`; selected record SHA-256 `b7d8bd83bf160418c28ec7af4d60fc7116e9e5324ff3a52963515e1a6758d276`.

- `scripts/wz_common/wz_common_mode_heavy_metal_heroes_fixup.gsc::function_b35b2850` (original lines 19-58): No standalone body contract is available in this selected summary.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/56c2daee7aa6b5c8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/56c2daee7aa6b5c8.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/1`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `c54850565089f9f3ce526d067e72adde1af3d69c73371f1eb08f41278ddfd2b2`.

- `scripts/wz_common/wz_common_mode_heavy_metal_heroes_fixup.gsc::__init__` (original lines 10-13): No standalone body contract is available in this selected summary. Available classification: autoexec_registration_inventory; native invocation/load order unverified.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/56c2daee7aa6b5c8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/56c2daee7aa6b5c8.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/765`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `24057f662cbaadf0316d4874d43860a980c2647a77c3def4772154b6a41c6228`.

- `scripts/wz_common/wz_common_mode_heavy_metal_heroes_fixup.gsc::__init__` (original lines 10-13): No standalone body contract is available in this selected summary.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/56c2daee7aa6b5c8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/56c2daee7aa6b5c8.json) at JSON pointer `/claims/3`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/0`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `2e8fbd682e5bbd01765c9e02741626db55920889455ac4a4f54277fbe98606dc`.

- `hmh-gap:HMH-GAP-SETTINGS:activation` (original lines 28-53): wzheavymetalheroes has no explicit assignment in the three selected HMH rule objects/anchor; the literal consumer lookup has bounded scope. A historical broad script/tables producer-absence claim remains unverified because its complete exact table-corpus membership and hashes are unavailable for this comparison. No corpus-wide absence or effective value follows. Only the selected-layer/anchor absence is established here: none of the three recovered HMH rule layers sets it â€” frontend playlist 17 rules (warzone.json 8360-8592), TU23 playlist 19 rules (8719-8980), gametype def 28 rules (playlists_online/gametypes.json 8244-8639); the anchor table bundle (rows 1-341) has no such key either. The effective value of getgametypesetting(#wzheavymetalheroes) is therefore unprovable from recovered data; the selected objects do not explicitly set it; computed names, hash aliases, other script calls and unavailable layers are not excluded; effective value stays unknown, not asserted false. Literal consumer map (each exact per-site predicate applies separately, including the independent alternate keys in the two OR gates below; effective store values and dynamic accesses remain open): wz_open_skyscrapers.gsc:60-64 (heroes supply-drop stash: level.var_2089aa11=supply_drop_stash_parent_dlc1_heroes; registration call function_f0297225(supply_drop_stash_parent_dlc1_flare_gun_heroes,2,4), which validates input and appends replacement/count data; actual spawn work is later in start after flag/timing/count gates); wz_open_skyscrapers.gsc:160-172 and 185 (hmh_ramp dynent enable via setdynentenabled); wz_open_skyscrapers.csc:94,116 (client-side ramp enable); warzone.gsc:828-831 (on_player_spawned: setperk specialty_doublejump + specialty_fallheight); wz_loadouts.gsc:46-50 (overwrites level.var_5c14d2e6 and level.var_317fb13c with pointer function_9de0644f); item_inventory.gsc:1112-1116 (same two perks at inventory load); item_world.gsc:519-528 (if hash_7d8c969e384dd1c9 OR wzheavymetalheroes, threads level.var_5c14d2e6 for all players); player_insertion.gsc:497-506 (threads level.var_618194f7, re-grants both perks); player_reinsertion.gsc:441-447 (if hash_4149d5d65eb07138 OR wzheavymetalheroes, threads level.var_317fb13c); vehicle.gsc:3397 (keep vehicle deathmodel when NOT heroes) and 4108-4111 (function_32607cfc returns true when heroes); wz_common_mode_heavy_metal_heroes_fixup.gsc:28-53 and .csc:28 (item_replacer replaces per-stash gun lists with #heavy_metal_heroes_list_guns_dlc1); wz_open_skyscrapers_fixup.gsc:30 and .csc:30 (NEGATED gate: wzenableflareguns AND NOT wzheavymetalheroes); hashed script_71e26f08f03b7a7a.gsc:256-259 (uses level.var_2089aa11 only when that parent is defined, current replacement is undefined and heroes setting is defined/truthy; an explicit replacement takes precedence). Conditional consequence limits: a truthy heroes value can admit the positive heroes predicates only together with their other per-site guards and actual invocation; it does not prove native effects, delivered perks, spawning or pointer execution. Falsy/undefined heroes does not admit those particular positive heroes terms, but cannot rule out all listed dispatches: item_world may pass via hash_7d8c969e384dd1c9 and player_reinsertion via hash_4149d5d65eb07138, then thread the respective pointer only when defined. No actual alternate-key value or pointer identity is established. The negated-heroes flare-gun predicate additionally requires its wzenableflareguns term; original native/store/VM outcomes remain unknown. No registration-as-invocation and no mode-name-implies-value claims are made; the separate always-true identity path (get_game_type equality, warzone.gsc:2770) is distinct from this setting path.

  unknowns: &#91;"Effective value of getgametypesetting(#wzheavymetalheroes) for HMH sessions (no recovered producer)", "Native default for absent getgametypesetting keys (undefined vs 0)", "Whether the online/original-build playlist layer sets wzheavymetalheroes", "Which VMs load wz_open_skyscrapers_fixup and wz_common_mode_heavy_metal_heroes_fixup (HMH-GAP-STARTUP owner)"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/56c2daee7aa6b5c8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/56c2daee7aa6b5c8.json) at JSON pointer `/claims/4`.

  Archived evidence ID: `archived-record-00526` at JSON pointer ``; file SHA-256 `4ee4af11116628ba5b7ba5189de2a2ab85ffdfeb0b48b559fab42e0aea051f0d`.

- `hmh-gap:HMH-GAP-STARTUP:__init__@wz_common_mode_heavy_metal_heroes_fixup.gsc` (original lines 1-59, 10-13): Source-visible answer for root candidate 5 (server-side HMH fixup): entry is function autoexec __init__ (eflags 0x2 annotation) whose single action is calling function_b35b2850 (10-13). function_b35b2850 (19-58) assigns six item_world_fixup function pointer locals, then evaluates isdefined(getgametypesetting(#wzheavymetalheroes)) and, only if that test passes, a second getgametypesetting(#wzheavymetalheroes) truthiness query. An undefined first query or falsey second query suppresses the26 item_replacer requests and separate stash-parent request. The six preceding pointer-local bindings21-26 and reached queries remain source operations; their native-visible effects and failure behavior are unproved. When the gate passes it requests 26 wz_common_fixup::item_replacer calls (list-name pairs -> heavy_metal_heroes_list_guns_dlc1, plus ammo rocket double and world_base_event_parent -> guns_launchers_dlc1) and item_world_fixup::function_e70fa91c(supply_stash_parent_dlc1 -> supply_stash_parent_heavy_metal_heroes, 20). Loading boundary evidence: NO #using importer of this script exists anywhere in the corpus (search returned only its own namespace strings); SOURCE-LOAD-INVENTORY.json records it as a forced-script row: tables/scriptparsetreeforced/wz_common_script.csv row 61, vm server (SOURCE-LOAD-INVENTORY.json 5449-5456). Native gaps: whether retail CUSA11100 loads the wz_common_script.csv forced set into the HMH server VM (and when autoexec executes vs level.gametype/getgametypesetting availability at autoexec time) is the exact minimum evidence request; the setting value/producer itself is g1's settings scope (recorded, not claimed).

  unknowns: &#91;" Retail load of wz_common_mode_heavy_metal_heroes_fixup.gsc into the HMH server VM (unproven)", "autoexec timing vs setting/gametype availability (unproven)", "wzheavymetalheroes effective value + producing playlist rule (data, g1 scope)", "Native-visible effects or failures of the preceding pointer bindings and reached setting queries remain unknown. A false/absent gate omits the26 replacement requests and separate stash-parent request, not every source operation."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/56c2daee7aa6b5c8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/56c2daee7aa6b5c8.json) at JSON pointer `/claims/5`.

  Archived evidence ID: `archived-record-00527` at JSON pointer ``; file SHA-256 `2cfcf424432166b7e29460cd432433fd2a7c19053acbf6bc7488092eb15a4c3f`.

- `scripts/wz_common/wz_common_mode_heavy_metal_heroes_fixup.gsc::__init__` (original lines 10-13): No standalone body contract is available in this selected summary.

  unknowns: &#91;"Source statements only; VM native loader/event/order/assert/getter/object semantics are not verified.", "Exact originating retail build, PS4 binary/asset mapping, native/server implementation and gameplay execution remain open.", "Conditional/dev candidate: source review does not establish HMH load reachability or execution."&#93;

  status: source_semantic_contract_ready_for_manager_review

  Complete explanatory fields: [exact projection](../../provenance/documentation/56c2daee7aa6b5c8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/56c2daee7aa6b5c8.json) at JSON pointer `/claims/6`.

  Archived evidence ID: `archived-record-00002` at JSON pointer `/contracts/273`; file SHA-256 `14d82864f03d391c58ddc8caaf6f84c482f72ea05ab80940d42da35eabc0a97e`; selected record SHA-256 `8b64f648c893fe61b8e3a5f6f2c23e143664207f05261be5bbffddbd9b87492d`.

- `scripts/wz_common/wz_common_mode_heavy_metal_heroes_fixup.gsc::__init__` (original lines 10-13): No standalone body contract is available in this selected summary.

  unknowns: &#91;"Source statements only; VM native loader/event/order/assert/getter/object semantics are not verified.", "Exact originating retail build, PS4 binary/asset mapping, native/server implementation and gameplay execution remain open.", "Conditional/dev candidate: source review does not establish HMH load reachability or execution."&#93;

  status: source_semantic_contract_ready_for_manager_review

  Complete explanatory fields: [exact projection](../../provenance/documentation/56c2daee7aa6b5c8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/56c2daee7aa6b5c8.json) at JSON pointer `/claims/7`.

  Archived evidence ID: `archived-record-00002` at JSON pointer `/contracts/273`; file SHA-256 `14d82864f03d391c58ddc8caaf6f84c482f72ea05ab80940d42da35eabc0a97e`; selected record SHA-256 `8b64f648c893fe61b8e3a5f6f2c23e143664207f05261be5bbffddbd9b87492d`.
