# hashed/4ca2e217b30e8afd.lua

Project-added notes. See the [code](../../src/lua/hashed/4ca2e217b30e8afd.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `9eb2beca69857bce828acf0ed67faf7a1d9cfc6df3cab4554005c9760d9886f8`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/752ef1faad5c5b8a.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua-follow6:125` (original lines 136-139, 136-136, 104-104, 6-6, 12-12, 136-139, 136-136, 137-137, 138-138, 139-139, 137-137, 138-138, 136-139, 137-137, 138-138, 136-139): Takes the CoD.WZObituaryVictim instance as f13_arg0. Calls close() with each child as implicit self, in this exact order: Icon, Name. There are no guards, branches, loops, explicit return values, field resets, timer cancellation or protected error handling in this body. Missing/already-closed children are not checked; an earlier receiver/provider error may prevent later closes. The same constructor sets this exact class and registers self.__onClose with CallOriginalSecond. That helper controls wrapping/order/invocation; registration alone does not prove game-time delivery.

  unknowns: &#91;"Effective HMH settings/data/assets, true load/overwrite/class lookup order, original recovered-text fidelity, native callback delivery and service/server implementations remain open.", "Independent correctness review and final game tests remain deferred."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/752ef1faad5c5b8a-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/752ef1faad5c5b8a.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00056` at JSON pointer `/units/124`; file SHA-256 `9b5470295d8bc5b945061358d29d8430f5da2392ccde6abf20deb11b8b9c027f`; selected record SHA-256 `c2ba424ba1ddca33b484ca08e37b7ce363e9bd2eba664bb2af384b4b8de52067`.

- `hmh07-lua-follow6:113` (original lines 17-17): Takes menu f1_arg0, controller f1_arg1 and eight layout bounds f1_arg2..f1_arg9; calls LUI.UIElement.new and sets the literal class/id/sound. Creates a feather-edged tinted backer followed by a TeamNumber text label initialized to numeric 1. It does not read an actual team-number model here. The exact placeholder, layout, font and alignment remain literal source values. Exact child order: Backer, TeamNumber. All layout/property/asset values and each callback body are retained in the ordered trace. Calls the optional same-file-or-unresolved PostLoadFunc at its exact source position, then returns self; a same name in another file supplies no binding. Base/child lifetime, model/event/animation delivery and native asset behavior remain external unless a reused exact provider contract explicitly supplies the bounded fact.

  unknowns: &#91;"Effective HMH settings/data/assets, true load/overwrite/class lookup order, original recovered-text fidelity, native callback delivery and service/server implementations remain open.", "Independent correctness review and final game tests remain deferred."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/752ef1faad5c5b8a-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/752ef1faad5c5b8a.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00056` at JSON pointer `/units/112`; file SHA-256 `9b5470295d8bc5b945061358d29d8430f5da2392ccde6abf20deb11b8b9c027f`; selected record SHA-256 `282f86bf771f91b215cf3a794bd40199741d20a4943e3fa5a026e8c924cfac14`.

- `hmh07-lua-follow4:068` (original lines 9-111): Constructs CoD.WZObituaryEntry with the supplied menu/controller/layout values; its exact visual/data fields, condition closures, hook requests and return are retained below. Creates self via LUI.UIHorizontalList.new, Blur via LUI.UIImage.new, Attacker via CoD.WZObituaryAttacker.new, FixedAspectRatioImage via LUI.UIFixedAspectRatioImage.new, Victim via CoD.WZObituaryVictim.new.

  unknowns: &#91;{"kind": "original_build", "gap": "Recovered-source revision is pinned; original PS4 build/byte/VM/native binding remains unverified."}, {"kind": "effective_data_settings_assets", "gap": "Engine/model/Dvar/asset/data requests do not supply effective runtime values, contents or ownership."}, {"kind": "server_service_persistence", "gap": "Unavailable authoritative server/service/provider code and successful persistence remain unavailable; not reconstructed or counted as completed."}, {"kind": "runtime_callback_lifetime", "gap": "Original loading, table overwrites, callback delivery/order, timings, state selection and UI cleanup are not runtime-proven."}&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/752ef1faad5c5b8a-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/752ef1faad5c5b8a.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00004` at JSON pointer `/units/67`; file SHA-256 `52df95eaa9f17f90427f6313acbc648c9bdffa0602f6444566bbe8fa1a54ba59`; selected record SHA-256 `df1e2a20b2194264097c800066f68c0939d9bf6350077e00b2563e75357db19f`.
