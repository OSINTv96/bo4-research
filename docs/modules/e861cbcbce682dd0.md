# hashed/23edb9528637b4c0.lua

Project-added notes. See the [code](../../src/lua/hashed/23edb9528637b4c0.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `f4967e52abb79758a3d4043422727003c923e2139bfcde9a19b2b85c4afa3d7f`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/e861cbcbce682dd0.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua:052` (original lines 67-67, 67-67): Queries HasDoubleLootXP first; only a falsey result falls back to hasTierBoost on the supplied element. Returns the resulting value, potentially nil. No tier grant/persistence action is implemented here.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/e861cbcbce682dd0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/e861cbcbce682dd0.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/51`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `3fd081720974381c5b22b3cd66d10e20d64144415bb4beedef6009ca8d2c3d72`.

- `hmh07-lua-follow1:188` (original lines 12-12, 12-12, 11-105, 107-107, 107-111): UIHorizontalList.new forwards eight layout arguments to UIElement.new, sets supplied spacing, ID and native resizing behavior, installs spacer/add/remove helpers and stores __ignoreFirstElement from argument9, then returns self. This selected body does not explicitly call setClass. Preserve that source difference and the base constructor's recovered failure/fallthrough behavior.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/e861cbcbce682dd0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/e861cbcbce682dd0.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00036` at JSON pointer `/units/187`; file SHA-256 `279ba12c6a1d4cfd1fb6c7e030a47694d4ee3982256bb21a0b3aa6909aef143b`; selected record SHA-256 `bf0586d95c2e393a455519923ecbd52c4b9e93e079613a93ece235c4ffc8d301`.

- `hmh07-lua:051` (original lines 31-31, 31-31): Queries MainModeHasDoubleWeaponXP with optional element mode/playlist; only a falsey result falls back to the element hasDoubleWeaponXP model. Returns that value with possible nil when no element. Main-mode reward backend remains outside this callable.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/e861cbcbce682dd0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/e861cbcbce682dd0.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/50`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `9bb753d7ae2fc71db95661caa0ccb1801adfbafc574dcf8b5fb58fe4a01bcc5c`.

- `hmh07-lua:207` (original lines 62-62, 58-66): Common XP container constructs this tier-boost icon and can replace its Visible condition. Own Visible calls IsTierBoostActive(controller); through the named setState override shows current Visible, hides otherwise. No XP award or storage mutation. No model subscription/close hook inside this primary span; external caller owns reevaluation. Optional postload then self return. Exact boost eligibility/service state remains open.

  unknowns: &#91;"Original Lua-to-PS4 CUSA11100 build binding and bytecode/VM/decompiler fidelity unverified.", "Effective HMH settings, enum values, model/data production, LUI state arbitration, event delivery/ordering/cancellation, assets, storage/DDL, networking/service behavior remain explicit gaps where called.", "External helper bodies not selected here are dependencies only; no nil/error recovery assumed beyond visible source. Named LUI override APIs are preserved; no original/new callback ordering is guaranteed without their source contract.", "No independent correctness review, retail execution or function completion credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/e861cbcbce682dd0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/e861cbcbce682dd0.json) at JSON pointer `/claims/3`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/206`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `14edefca98dcd36127af8f36289ab445fb82bf7160d449f96fa8b54a7d99d410`.

- `lua:hashed/23edb9528637b4c0.lua::lua-structural:fd5c6fcbe600cde5643bd2bccc8e29c8057f74c84c022cfcbd7f0554c6c1693d` (original lines 47-55): sub DataSources.AutoEvents.getModel(ctrl).cycled -> updateElementState(WeaponXPIcon)

  unknowns: &#91;"Prior compact rows did not serialize unit-specific unknowns separately. Preserve the limitations in archived-record-00041 and contracts.json; independent review remains deferred."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/e861cbcbce682dd0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/e861cbcbce682dd0.json) at JSON pointer `/claims/4`.

  Archived evidence ID: `archived-record-00042` at JSON pointer `/units/321`; file SHA-256 `fdf7af40c2eaf24fcd6988029e873508f76b8c2efff146c2af2f935c6e320dce`; selected record SHA-256 `83ae25e037bc0fe95d8f979c061e1d37867623bff0d8b79ec7e90ed52e52983e`.

- `lua:hashed/23edb9528637b4c0.lua::lua-structural:991caf49ecdebe829e8d70b01e2d7cfc48ef9d7efd9fbe66eba5f7a18b33d313` (original lines 107-111): __onClose: DoubleXPIcon+WeaponXPIcon+TierBoost close

  unknowns: &#91;"Prior compact rows did not serialize unit-specific unknowns separately. Preserve the limitations in archived-record-00041 and contracts.json; independent review remains deferred."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/e861cbcbce682dd0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/e861cbcbce682dd0.json) at JSON pointer `/claims/5`.

  Archived evidence ID: `archived-record-00042` at JSON pointer `/units/327`; file SHA-256 `fdf7af40c2eaf24fcd6988029e873508f76b8c2efff146c2af2f935c6e320dce`; selected record SHA-256 `4f4e91f29a2cc1f667452a04f935738f39579818329410cceaa95d7e31651e17`.

- `lua:hashed/23edb9528637b4c0.lua::lua-structural:191ac0ade4716388a912c75a95a7ef6b200754e4521acb2a9530da26796cdfe5` (original lines 35-43): cb link WeaponXPIcon hasDoubleWeaponXP -> updateElementState(WeaponXPIcon)

  unknowns: &#91;"Prior compact rows did not serialize unit-specific unknowns separately. Preserve the limitations in archived-record-00041 and contracts.json; independent review remains deferred."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/e861cbcbce682dd0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/e861cbcbce682dd0.json) at JSON pointer `/claims/6`.

  Archived evidence ID: `archived-record-00042` at JSON pointer `/units/320`; file SHA-256 `fdf7af40c2eaf24fcd6988029e873508f76b8c2efff146c2af2f935c6e320dce`; selected record SHA-256 `3dc02e183af4562d52d76a36cb091e26e70f4af5bb5e2e43a187ab18ab8a8b81`.

- `hmh07-lua:193` (original lines 8-8, 4-12): InheritFrom is executed at the cited class assignments, not merely imported. Missing/falsy base throws explicit LUI Error. Otherwise makes a new table with super=base, sets its metatable __index=base, creates a fresh m_eventHandlers table with __index=base.m_eventHandlers, then returns the new class. It shares fallback handlers while permitting per-class handler writes. Does not instantiate widgets, invoke inherited callbacks or close anything. Metatable/native VM behavior and base fields are assumed, no further validation.

  unknowns: &#91;"Original Lua-to-PS4 CUSA11100 build binding and bytecode/VM/decompiler fidelity unverified.", "Effective HMH settings, enum values, model/data production, LUI state arbitration, event delivery/ordering/cancellation, assets, storage/DDL, networking/service behavior remain explicit gaps where called.", "External helper bodies not selected here are dependencies only; no nil/error recovery assumed beyond visible source. Named LUI override APIs are preserved; no original/new callback ordering is guaranteed without their source contract.", "No independent correctness review, retail execution or function completion credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/e861cbcbce682dd0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/e861cbcbce682dd0.json) at JSON pointer `/claims/7`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/192`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `28096b9a20c988def77f03e8d965db4759673d7a552db8efd9d89c53725de88c`.

- `hmh07-lua:027` (original lines 19-19, 19-19): Constructs ordinary XP and promotional XP displays, linking their models to self. Ordinary visible states use HasDoubleXP, including a WZ+mode variant; promotional state uses HasPromotionalDoubleXP. HasDoubleXP and daily promotional-time changes revalidate. Its setState hook adjusts presentation outside Visible/Promotional; frozen reset/clips/close retain the exact two-child effects. Promotional eligibility remains the MP/arena gate from its own selected helper, not assumed true in HMH.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/e861cbcbce682dd0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/e861cbcbce682dd0.json) at JSON pointer `/claims/8`.

  Archived evidence ID: `archived-record-00043` at JSON pointer ``; file SHA-256 `13be9da74034345aef0ea33f206b23ddfc9787ede31eb11de70de6cc142d895e`.

- `lua:hashed/23edb9528637b4c0.lua::lua-structural:465f6f8ffdf8fbd1d5232ebb1de240d212a6012b240ce07717b06f376a254825` (original lines 20-22): cb link(self,nil) DoubleXPIcon:setModel(model,ctrl)

  unknowns: &#91;"Prior compact rows did not serialize unit-specific unknowns separately. Preserve the limitations in archived-record-00041 and contracts.json; independent review remains deferred."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/e861cbcbce682dd0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/e861cbcbce682dd0.json) at JSON pointer `/claims/9`.

  Archived evidence ID: `archived-record-00042` at JSON pointer `/units/318`; file SHA-256 `fdf7af40c2eaf24fcd6988029e873508f76b8c2efff146c2af2f935c6e320dce`; selected record SHA-256 `344e20de98bca06c85e028bad8dfcc3df30d58abf71c85bf379be3ad4e2d0574`.

- `hmh07-lua-follow1:146` (original lines 98-98, 98-98, 11-105, 107-107, 107-111): CallOriginalFirst appends the supplied callback to the table returned by OverrideFunction_GetFunctionTable. CallOriginalSecond inserts its callback at index1. Neither wrapper directly calls the original or callback or returns a value. The naming does not prove runtime order independently of the dispatcher, which remains a reusable available dependency.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/e861cbcbce682dd0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/e861cbcbce682dd0.json) at JSON pointer `/claims/10`.

  Archived evidence ID: `archived-record-00044` at JSON pointer ``; file SHA-256 `46ecb6cfe8fa919ec918f489610848dcd8b393e632706abbfd898ba7b2a05c62`.

- `lua:hashed/23edb9528637b4c0.lua::lua-structural:d2f0b3ef217493b1cca8fa203d3fe45178428ab92e2230c259d973f17169af49` (original lines 11-105): f14 new: UIHorizontalList center 216x72; ch DoubleXPIcon(DoubleXPPromotionalIcon H)+WeaponXPIcon(out Notification2xpWeaponReward)+TierBoost(Notification2xpBlackMarketReward H); cb links m319/m323/m327; conds m320 HasDoubleWeaponXP+hasTierBoost; subs AutoEvents.cycled x2; close<-m328; PostLoadFunc H

  unknowns: &#91;"Prior compact rows did not serialize unit-specific unknowns separately. Preserve the limitations in archived-record-00041 and contracts.json; independent review remains deferred."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/e861cbcbce682dd0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/e861cbcbce682dd0.json) at JSON pointer `/claims/11`.

  Archived evidence ID: `archived-record-00042` at JSON pointer `/units/317`; file SHA-256 `fdf7af40c2eaf24fcd6988029e873508f76b8c2efff146c2af2f935c6e320dce`; selected record SHA-256 `7e344e5aaee32a35546aa01194bdb21b6c3de53d15cdb9b03ab1aa50eda27216`.

- `lua:hashed/23edb9528637b4c0.lua::lua-structural:12dbefa4f5027b43db9040413502175c5ed0c75b75ef5ffc8161df86bc652aa1` (original lines 83-91): AutoEvents.cycled subscription callback calls menu:updateElementState(TierBoost,{name=model_validation,menu=menu,controller=controller,modelValue=callback_model:get(),modelName=cycled}); separate self-model linkage/setModel is outside this callback.

  unknowns: &#91;"Prior compact rows did not serialize unit-specific unknowns separately. Preserve the limitations in archived-record-00041 and contracts.json; independent review remains deferred."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/e861cbcbce682dd0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/e861cbcbce682dd0.json) at JSON pointer `/claims/12`.

  Archived evidence ID: `archived-record-00813` at JSON pointer ``; file SHA-256 `b09e177c81c17a85382a8935cfe7931dd985f236969316f0d2d61899b2b7b291`; selected record SHA-256 `f7bcd78391bd23f12a3d3a7050d813f3f2dbfd579ba94bce698ced46bc3cb462`.

- `lua:hashed/23edb9528637b4c0.lua::lua-structural:abf18b8e9c6789a9c3bfea3b4fedb1c4c470864e8c763ca1c5cb0a788efc97b4` (original lines 30-32): cond Visible WeaponXPIcon: DoubleXPUtility.HasDoubleWeaponXP(ctrl,element); + hasTierBoost cond

  unknowns: &#91;"Prior compact rows did not serialize unit-specific unknowns separately. Preserve the limitations in archived-record-00041 and contracts.json; independent review remains deferred."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/e861cbcbce682dd0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/e861cbcbce682dd0.json) at JSON pointer `/claims/13`.

  Archived evidence ID: `archived-record-00042` at JSON pointer `/units/319`; file SHA-256 `fdf7af40c2eaf24fcd6988029e873508f76b8c2efff146c2af2f935c6e320dce`; selected record SHA-256 `2c020c80a198f1390a4c6068a3dc132efe6812885c7040028e06c32871fc785c`.

- `lua:hashed/23edb9528637b4c0.lua::lua-structural:7f6a2d6cbffe6fb486479880d696e3a2409eea7c69522ebdd9ba95705579edec` (original lines 56-58): cb link(self,nil) weapon row: DoubleWeaponXPIcon:setModel(model,ctrl)

  unknowns: &#91;"Prior compact rows did not serialize unit-specific unknowns separately. Preserve the limitations in archived-record-00041 and contracts.json; independent review remains deferred."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/e861cbcbce682dd0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/e861cbcbce682dd0.json) at JSON pointer `/claims/14`.

  Archived evidence ID: `archived-record-00042` at JSON pointer `/units/322`; file SHA-256 `fdf7af40c2eaf24fcd6988029e873508f76b8c2efff146c2af2f935c6e320dce`; selected record SHA-256 `ebd17e9971a8fc6fc06751e618f812343494c33d8e714e00add8706c50a5e668`.

- `hmh07-lua-follow8:003` (original lines 8-8, 4-12): Assign the supplied widget type to the receiver field, then request receiver:clearLayout(). The source setter does not call the widget constructor.

  unknowns: &#91;"Exact selected recovered Lua source only, conditional module/caller bindings. Original loader/global overwrite/VM/native/DDL/settings/assets/service/server/PS4 behavior remain unverified. No independent review, acceptance, function completion or runtime credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/e861cbcbce682dd0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/e861cbcbce682dd0.json) at JSON pointer `/claims/15`.

  Archived evidence ID: `archived-record-00045` at JSON pointer `/units/2`; file SHA-256 `0c981d5eb446fe3dd44845673b101548cf36172da6abd92475497ba0faf30ce0`; selected record SHA-256 `3843c6aed3c88d59e0c2b91a3eb9d0e61ecd93d8a7660df06791bae7e79e7153`.

- `lua:hashed/23edb9528637b4c0.lua::FILE_TOP_LEVEL` (original lines 1-112): f14 F TOP: req x64:5683120446682173+x64:148e413a7c2e7936 (H)+notification2xpweaponreward (OUT); class DoubleXPIconsCenterAligned L8; 216x72; no reset/clips; PostLoadFunc H

  unknowns: &#91;"Prior compact rows did not serialize unit-specific unknowns separately. Preserve the limitations in archived-record-00041 and contracts.json; independent review remains deferred."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/e861cbcbce682dd0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/e861cbcbce682dd0.json) at JSON pointer `/claims/16`.

  Archived evidence ID: `archived-record-00042` at JSON pointer `/units/328`; file SHA-256 `fdf7af40c2eaf24fcd6988029e873508f76b8c2efff146c2af2f935c6e320dce`; selected record SHA-256 `6533268485f07465884911170f3dd0e8a61b44832741725941e7ddb355f03123`.

- `lua:hashed/23edb9528637b4c0.lua::lua-structural:cb298b708f438be51cf0e3e6e27c7853387840d65678188abaf09422dc0fc910` (original lines 71-79): TierBoost:linkToElementModel(TierBoost,hasTierBoost,true,callback); callback calls menu:updateElementState(TierBoost,{name=model_validation,menu=menu,controller=controller,modelValue=model:get(),modelName=hasTierBoost}).

  unknowns: &#91;"Prior compact rows did not serialize unit-specific unknowns separately. Preserve the limitations in archived-record-00041 and contracts.json; independent review remains deferred."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/e861cbcbce682dd0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/e861cbcbce682dd0.json) at JSON pointer `/claims/17`.

  Archived evidence ID: `archived-record-00814` at JSON pointer ``; file SHA-256 `ac96a0f5b8b286e008b05dd5fe5608734e884a684564b99adb82a0214c4efb14`; selected record SHA-256 `ae959accce15de6f5703133674b71bfd3099251a4433bf3a62d4805717182903`.

- `hmh07-lua:190` (original lines 11-105, 20-20, 21-21, 35-35, 56-56, 57-57, 71-71, 92-92, 93-93, 98-98, 108-108, 109-109, 110-110, 29-29, 31-31, 65-65, 67-67, 100-100, 104-104, 11-105, 107-107, 107-111, 19-19, 14-24, 31-31, 26-36, 67-67, 62-72, 62-62, 57-67, 26-26, 21-31, 46-46, 41-51, 82-82, 77-87, 98-98, 93-103, 12-12, 7-17, 101-101, 96-106, 11-105): Description-panel caller constructs this horizontal XP icon list and initially sets its alpha0. Builds promotional XP icon, weapon-XP icon and tier-boost icon, forwarding parent model to all three. Weapon visibility delegates HasDoubleWeaponXP, tier visibility HasTierBoost; own hasDoubleWeaponXP/hasTierBoost links and AutoEvents.cycled notifications reevaluate corresponding child state. No award or progression update occurs. Linked __onClose closes all three child widgets through CallOriginalSecond through the named close override according to the external override helper contract; optional postload then self return. Callback delivery, actual bonus values and service data remain unknown.

  unknowns: &#91;"Original Lua-to-PS4 CUSA11100 build binding and bytecode/VM/decompiler fidelity unverified.", "Effective HMH settings, enum values, model/data production, LUI state arbitration, event delivery/ordering/cancellation, assets, storage/DDL, networking/service behavior remain explicit gaps where called.", "External helper bodies not selected here are dependencies only; no nil/error recovery assumed beyond visible source. Named LUI override APIs are preserved; no original/new callback ordering is guaranteed without their source contract.", "No independent correctness review, retail execution or function completion credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/e861cbcbce682dd0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/e861cbcbce682dd0.json) at JSON pointer `/claims/18`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/189`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `e14f2f4f9bae78110f88ce65d8662ffb9687e039de668d68e3f26b512e792d7e`.

- `lua:hashed/23edb9528637b4c0.lua::lua-structural:95549d0d6256e447e44f284eb674a5e62a8b3f28b8a77db49f117df256f4c658` (original lines 92-94): inner continuation tier link (same model push)

  unknowns: &#91;"Prior compact rows did not serialize unit-specific unknowns separately. Preserve the limitations in archived-record-00041 and contracts.json; independent review remains deferred."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/e861cbcbce682dd0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/e861cbcbce682dd0.json) at JSON pointer `/claims/19`.

  Archived evidence ID: `archived-record-00042` at JSON pointer `/units/326`; file SHA-256 `fdf7af40c2eaf24fcd6988029e873508f76b8c2efff146c2af2f935c6e320dce`; selected record SHA-256 `79baab2e2c56adef815d6d8f46c6bc38ec3d5f1797bacdb217270a93256b6860`.

- `lua:hashed/23edb9528637b4c0.lua::lua-structural:18c89e8e5641257058a081d9008f2471fdc714380275eced07cb491f0da314d1` (original lines 66-68): Visible condition returns CoD.DoubleXPUtility.HasTierBoost(controller,element); provider effects/return semantics remain outside this callback.

  unknowns: &#91;"Prior compact rows did not serialize unit-specific unknowns separately. Preserve the limitations in archived-record-00041 and contracts.json; independent review remains deferred."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/e861cbcbce682dd0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/e861cbcbce682dd0.json) at JSON pointer `/claims/20`.

  Archived evidence ID: `archived-record-00815` at JSON pointer ``; file SHA-256 `0d1ca87f5ff416c348fa36ef6964a7cefdefb9f56f368dc1ad061c1f9a44859e`; selected record SHA-256 `ba57178359a919af15b57515e86bcedf12efee10776c4f2cd82b373a6b75a74b`.
