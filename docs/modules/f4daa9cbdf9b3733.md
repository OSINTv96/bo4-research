# hashed/3114c870ee1d3fdb.lua

Project-added notes. See the [code](../../src/lua/hashed/3114c870ee1d3fdb.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `f1ff9067e01483d68a549a4c3344ef3b9a971a0c43c12e636f1a3effecae6133`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/f4daa9cbdf9b3733.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua-follow9:003` (original lines 632-643, 634-634, 636-636, 632-643, 632-643, 632-643, 632-632, 658-658, 632-632, 632-632, 658-658, 632-632, 633-633, 634-634, 635-635, 636-636, 637-637, 638-638, 639-639, 640-640, 641-641, 642-642, 643-643, 633-633, 634-634, 635-635, 636-636, 637-637, 638-638, 639-639, 640-640, 641-641, 642-642, 643-643, 632-632): {"scope": "Exact selected callable immediate bodies and explicitly owned lexical inline children only.", "selected_outer_bodies": 1, "canonical_immediate_body_contracts": 1, "source_membership": "Literal conditional caller/provider identity qualified before source semantics; class close slots retain dispatch limits.", "not_stage_completion": true}

  unknowns: {"original_build": &#91;"Original exact PS4 source/bytecode-to-recovered-source match and target build binding remain unverified."&#93;, "native": &#91;"Engine entry implementations, ABI, original bytes and native return/effect contracts not established by Lua text."&#93;, "VM": &#91;"Recovered Lua dialect, lexical scopes, xhash operations, bitwise/numeric behavior and target VM bindings remain unverified."&#93;, "receiver_loader": &#91;"Effective global/table values, class/metatable lookup, method dispatch, import/load order, overwrites and callback delivery not proved."&#93;, "settings": &#91;"Effective CoD.isPC/input/platform gates, Dvar values, enum values and HMH settings not established."&#93;, "assets": &#91;"Materials, sounds, UI widget assets and underlying localization/task bundles remain unverified."&#93;, "data": &#91;"Model handles/values, controller entries, loot/reticle/calling/contract/outfit tables and saved account data are not acquired or reconstructed."&#93;, "services_server": &#91;"Original online progression, persistence, networking and unavailable service/server code stay explicit missing inputs."&#93;, "runtime": &#91;"No live game/PS4/account/router/save action, game test, independent review or runtime proof."&#93;, "exact_unqualified_source_providers_or_receivers": &#91;&#93;, "partial_reused_dependencies": &#91;&#93;}

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/f4daa9cbdf9b3733-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/f4daa9cbdf9b3733.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00375` at JSON pointer `/units/2`; file SHA-256 `52e6ec303d361fa43aaee6831980530d68068868e918f14a34338eca144f4467`; selected record SHA-256 `7e8d18ad51d2c8780ed3c25bf372d7148288e61df59a85c104786bfecd1ff5d2`.

- `hmh07-lua-follow5:022` (original lines 190-192, 190-190, 704-712, 704-704, 715-715, 714-716, 719-719, 718-720, 190-192, 190-190, 704-712, 704-704, 715-715, 714-716, 719-719, 718-720, 714-716, 718-720, 191-191, 186-188, 191-191, 175-184, 190-192, 704-712): Pass all six arguments, in order, to CreateWeaponOptionsTable, pass its result to GetWeaponOptionsStringFromTable, and return that result. No local fallback or recovery. Start with hash_6B0DA2DF6A22B400; use hash_35338AAC90E615E8 for mode_zombies or hash_353D7FAC90EE57BC for mode_warzone; return the chosen enum field. The spelling CAmo is retained.

  unknowns: {"provider_or_lexical": &#91;&#93;, "source_fidelity": &#91;&#93;, "original_build": "Recovered source is not matched to original PS4 bytecode/build; @0 is not a native address.", "VM_native": "Lua dialect, metatables, native/UI API execution, model dispatch/cancellation and input timing remain unverified.", "data_settings_assets": "Literal references do not supply effective model values, settings, data tables, localization or asset availability.", "server_service": "Online, stats, progression, marketing, lobby and backend behavior are unavailable service boundaries when requested by these exact bodies.", "runtime": "No game, console, account, router, save, native tool or independent review was run."}

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/f4daa9cbdf9b3733-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/f4daa9cbdf9b3733.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00034` at JSON pointer `/units/21`; file SHA-256 `781c1c1aee59bfc36951652bab7a837686810fc0aebaac4cb4ddfe8fe782f24f`; selected record SHA-256 `af1c72c989193b83613391a4f4126024fb49863dc7356c54248d790b39c86f7f`.

- `hmh07-lua-follow3:192` (original lines 587-603, 605-608, 587-603, 605-608, 593-593, 714-714, 589-589, 595-595, 606-606, 587-603, 605-608): Starts result as supplied camo options index. If CamoOptionsTable resolves a camo reference, replaces result with attachment-table lookup; only a false/missing lookup attempts active-camo reference, asset stages&#91;1&#93;.camooption and a second attachment lookup. Returns final result or -1, so no initial camo reference leaves the supplied index as result. No numeric conversion or live-camo effect is added. Looks up the weapon-option camo category and returns the retrieved value and its equality to active; a missing value can remain nil rather than false.

  unknowns: &#91;"Original PS4/source match, original Lua bytecode and VM/decompiler fidelity remain unverified.", "Effective enum/dvar/settings, assets/localization/model/DDL/storage/playlist data remain exact external inputs; requested persistence/network/service effects are not successful execution proof.", "A field/method/import/spelling or other-file local alone does not bind a provider. Unknown identities remain unresolved rather than declared unavailable.", "Native model/event/timer/wrapper invocation, delivery, error/cleanup/lifetime and unavailable original server behavior are outside this source packet.", "No independent correctness review, acceptance, original-build or function-completion credit is recorded."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/f4daa9cbdf9b3733-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/f4daa9cbdf9b3733.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00003` at JSON pointer `/units/191`; file SHA-256 `a63852530df9189721a410c240a42967af6648aa0fca4e70325b17a1e677ebb7`; selected record SHA-256 `f1a8724e358918f83fc5e2b42739ad7aa4f191332fcb44bdd2f8fdb608c7d680`.

- `hmh07-lua-follow8:022` (original lines 657-664, 657-664, 657-664, 657-657, 657-657, 657-657, 657-657, 657-657, 658-658, 659-659, 660-660, 661-661, 662-662, 663-663, 664-664, 659-659, 660-660, 661-661, 662-662, 657-657, 657-664, 657-664, 659-659, 660-660, 661-661, 662-662): Authored 1 exact immediate-body contracts; prior source units remain full unchanged reuse. No original-build or runtime conclusion is added.

  unknowns: &#91;"Runtime loading/overwrite and actual HMH invocation remain unproved.", "All inherited prior partial/fidelity/excluded-nested/reviewer/report limits persist in reuse-preserved.json."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/f4daa9cbdf9b3733-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/f4daa9cbdf9b3733.json) at JSON pointer `/claims/3`.

  Archived evidence ID: `archived-record-00045` at JSON pointer `/units/21`; file SHA-256 `0c981d5eb446fe3dd44845673b101548cf36172da6abd92475497ba0faf30ce0`; selected record SHA-256 `387ae6739865179deab246a29073d29beb56c50faaf1b766e10caa0ce1afa40e`.

- `hmh07-lua-follow6:014` (original lines 175-184, 175-175, 191-191, 191-191, 175-175, 177-177, 178-178, 179-179, 180-180, 181-181, 182-182, 175-175, 176-176, 177-177, 178-178, 179-179, 180-180, 181-181, 182-182, 183-183, 184-184, 176-176, 175-175, 176-176, 186-188, 186-186, 191-191, 191-191, 186-186, 187-187, 186-186, 187-187, 188-188, 187-187, 186-186, 187-187, 175-184, 186-188, 176-176, 187-187, 175-184, 186-188): Return a new table mapping args0..5 to camoIndex, reticleIndex, showPaintshop, weaponModelSlot, robStage, charmIndex in that order; no coercion, defaults or mutation of an input table. Read the six fields from the sole table argument in camo/reticle/paintshop/model-slot/rob-stage/charm order, replace each false-or-nil field with numeric 0 using or, and concatenate with commas. No nil-table guard; truthy non-concatenable values remain an error/fidelity boundary.

  unknowns: &#91;"Exact original source/build match and loader/table/global overwrite order", "Effective settings/storage/table/profile/model values", "Native render/model/event/timer lifetime and delivery", "Unavailable service/server behavior and final HMH membership"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/f4daa9cbdf9b3733-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/f4daa9cbdf9b3733.json) at JSON pointer `/claims/4`.

  Archived evidence ID: `archived-record-00836` at JSON pointer ``; file SHA-256 `aa0239e54de83a0316780e442b78ee27d13816b6b32a85496007e323f8f44e26`; selected record SHA-256 `3595f15229d4bb0dd026b45b0df4e3ed17adc62b677fb7782ec331969c9f35db`.

- `hmh07-lua-follow4:168` (original lines 714-716, 593-593, 718-720, 714-716, 718-720, 593-593, 715-715, 704-712, 719-719, 704-712, 714-716, 718-720): Preserves the exact direct source forwarding contract: return Engine&#91;@"tablelookup"&#93;( CoD.CACUtility.CamoOptionsTable, CoD.WeaponOptionsUtility.GetActiveCAmoColumnForMode( f25_arg0 ), Enum&#91;@"hash_25DD5CC8AEA7314B"&#93;&#91;@"hash_3AA94CABDA68EB21"&#93;, f25_arg1 ). Other ordered reads/writes below occur before this return; callee/native effects and missing-input error behavior remain external. Preserves the exact direct source forwarding contract: return Engine&#91;@"tablelookup"&#93;( CoD.CACUtility.CamoOptionsTable, CoD.WeaponOptionsUtility.GetActiveCAmoColumnForMode( f26_arg0 ), Enum&#91;@"hash_25DD5CC8AEA7314B"&#93;&#91;@"hash_6B79D07B3744EA1A"&#93;, "camo", Enum&#91;@"hash_25DD5CC8AEA7314B"&#93;&#91;@"hash_6A6342D60A0D5AAE"&#93;, f26_arg1 ). Other ordered reads/writes below occur before this return; callee/native effects and missing-input error behavior remain external.

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/f4daa9cbdf9b3733-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/f4daa9cbdf9b3733.json) at JSON pointer `/claims/5`.

  Archived evidence ID: `archived-record-00004` at JSON pointer `/units/167`; file SHA-256 `52df95eaa9f17f90427f6313acbc648c9bdffa0602f6444566bbe8fa1a54ba59`; selected record SHA-256 `29c2362183ce7429076ff90cd66822cc6ed58b79631749bf61bd6b5110cf3f5f`.

- `hmh07-lua-follow4:263` (original lines 190-192): cacRoot requests the hashed native root directly; otherwise chooses three-argument storagegetbuffer when arg2 is nonnil or the two-argument version. Returns the requested root/buffer. Weapon0 calls ClearDisplay then returns. Otherwise requests paintjob setup and a CustomClass_update local-client notify carrying the shown slot, converted weapon, empty attachments, camera and options fields. No network/persistence result is proved. Sends CustomClass_remove plus adjusted local-client number with an empty payload; no local cleanup completion is asserted. Returns editorMode != none from GetEmblemEditorProperties. Ends native edits; chooses paintshop/emblem customization and model notify; clears four per-controller selection fields; sets editor/color none and clipboard EMPTY; requests profile commit, optional paintjob invalidation and grid-size0. No rollback or commit success guard is added. Only uploadProfile==true clears the flag first and requests execnow uploadprofile. No retry/success notification or server implementation is supplied. For a supplied name matching an entitlement record and storage type, returns true at the first owned entitlement, else false for that matching record. No matching record or absent name defaults true. Both numeric loop headers are explicit: start1, step1, outer terminal #CoD.CraftUtility.EmblemEntitlements and inner terminal #f398_local3.entitlementRefs. Effective table contents, entitlement results and original VM execution remain unverified.

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/f4daa9cbdf9b3733-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/f4daa9cbdf9b3733.json) at JSON pointer `/claims/6`.

  Archived evidence ID: `archived-record-00505` at JSON pointer ``; file SHA-256 `050e7d2024d1f401dac7dca9759cc520a2deaa5a0797a2593994f2e7a11dd16b`; selected record SHA-256 `549fc51ec12820091d422cd9eb6660fd48ef8ca597a44b88cbeb052b9ce9bc98`.
