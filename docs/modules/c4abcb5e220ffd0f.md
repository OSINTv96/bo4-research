# hashed/51c61918e91d914e.lua

Project-added notes. See the [code](../../src/lua/hashed/51c61918e91d914e.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `2df981f352277733c7b8c42c217279513b7935d0988c0820ea189c1de4a5a05e`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/c4abcb5e220ffd0f.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua-follow4:039` (original lines 17-17, 17-17, 17-17): Builds the power-weapon drain visuals. Visible calls AlwaysFalse. After optional PostLoadFunc it calls InitWeaponPowerDrainBar for ReadyGlow1b/Fill2/Fill/Fill3 with duration 200 and flags false/true/true/true, then returns. Creates self via LUI.UIElement.new, ReadyGlow1b via LUI.UIImage.new, Empty via LUI.UIImage.new, Fill2 via LUI.UIImage.new, Fill via LUI.UIImage.new, Fill3 via LUI.UIImage.new. Stores state predicates Visible; their body effects require state-system evaluation.

  unknowns: &#91;{"kind": "original_build", "gap": "Recovered-source revision is pinned; original PS4 build/byte/VM/native binding remains unverified."}, {"kind": "effective_data_settings_assets", "gap": "Engine/model/Dvar/asset/data requests do not supply effective runtime values, contents or ownership."}, {"kind": "server_service_persistence", "gap": "Unavailable authoritative server/service/provider code and successful persistence remain unavailable; not reconstructed or counted as completed."}, {"kind": "runtime_callback_lifetime", "gap": "Original loading, table overwrites, callback delivery/order, timings, state selection and UI cleanup are not runtime-proven."}&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/c4abcb5e220ffd0f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/c4abcb5e220ffd0f.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00004` at JSON pointer `/units/38`; file SHA-256 `52df95eaa9f17f90427f6313acbc648c9bdffa0602f6444566bbe8fa1a54ba59`; selected record SHA-256 `5839ac114f61e803a5677b5f1876bb127c836767c4eb946cf50b3fb0c60bc1d7`.

- `hmh07-lua-follow2:007` (original lines 10-70, 10-70): Constructs WeaponImage and WeaponAmmoCount/ClipInfo, binding each to the entire parent model. dwGrappleWeapon updates the image only on nonnil values via GetHudImageFromItemIndex and RegisterImage. Nil does not clear the previous image. Registers close, optional PostLoadFunc, then returns self.

  unknowns: &#91;"Exact original PS4/source version matching, recovered Lua/VM fidelity and global/native/LUI provider identity remain unverified.", "Model/storage/DDL/assets/localization/dvar/enum values, callback delivery/cancellation/error behavior, native networking and unavailable service/server code are separate inputs.", "Other-file locals are not providers by spelling. Exact qualified global declarations are source candidates until loader/table identity and caller conditions bind them.", "No implicit nil/type checks, exception recovery, timer/model disposal, idempotence or guarantee that later effects run after an error is added."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/c4abcb5e220ffd0f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/c4abcb5e220ffd0f.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00028` at JSON pointer `/units/6`; file SHA-256 `2f4ecc3aabb5072135e148ef5782181882bd3b940908913a20bf258d3754185e`; selected record SHA-256 `492a731fb7f7ed10e3edfe848be710ef3570f4d6d5033cf0da0cd170039273fc`.

- `hmh07-lua-follow4:062` (original lines 72-77, 63-63, 10-70, 72-77, 72-77, 63-63, 10-70, 72-77, 63-63, 10-70, 72-77, 10-70, 72-77, 72-77): On invocation requests these child closes in exact order: f6_arg0.PowerWeaponDrainGadget3:close(); f6_arg0.PowerWeaponDrainGadget2:close(); f6_arg0.WeaponImage:close(); f6_arg0.HeroAbilityUseString:close(). No nil guard, protected call, timer cancellation, field clearing or explicit return is added.

  unknowns: &#91;{"kind": "original_build", "gap": "Recovered-source revision is pinned; original PS4 build/byte/VM/native binding remains unverified."}, {"kind": "effective_data_settings_assets", "gap": "Engine/model/Dvar/asset/data requests do not supply effective runtime values, contents or ownership."}, {"kind": "server_service_persistence", "gap": "Unavailable authoritative server/service/provider code and successful persistence remain unavailable; not reconstructed or counted as completed."}, {"kind": "runtime_callback_lifetime", "gap": "Original loading, table overwrites, callback delivery/order, timings, state selection and UI cleanup are not runtime-proven."}&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/c4abcb5e220ffd0f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/c4abcb5e220ffd0f.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00004` at JSON pointer `/units/61`; file SHA-256 `52df95eaa9f17f90427f6313acbc648c9bdffa0602f6444566bbe8fa1a54ba59`; selected record SHA-256 `b3277cd272171262a8a919924b8eeebe362e78e07b9006ba3ae72159acf510b6`.

- `hmh07-lua-follow4:002` (original lines 57-57, 57-57, 57-57, 57-57, 57-57, 57-57): Saved exact contracts for 9 qualified source bodies; 0 reuse historical bounded facts. Each body contract preserves its own branches, order and fidelity; enclosing gaps remain unauthored.

  unknowns: &#91;"Original source-to-PS4 match, VM/native/LUI semantics, effective settings/platform/global binding and callback delivery remain unverified.", "Data/assets/localization/DDL/storage/network/server code remain explicit gaps; current source does not prove their contents or behavior.", "No inferred nil guards, exception recovery, cleanup, dispatch or whole-file semantic coverage."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/c4abcb5e220ffd0f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/c4abcb5e220ffd0f.json) at JSON pointer `/claims/3`.

  Archived evidence ID: `archived-record-00004` at JSON pointer `/units/1`; file SHA-256 `52df95eaa9f17f90427f6313acbc648c9bdffa0602f6444566bbe8fa1a54ba59`; selected record SHA-256 `0e74bd198a0076304418fd817645840dba294dd7e4122d6d487d2e3e1f563594`.

- `hmh07-lua-follow4:070` (original lines 53-53, 53-53, 53-53): Constructs CoD.AmmoWidgetWZ_WeaponName with the supplied menu/controller/layout values; its exact visual/data fields, condition closures, hook requests and return are retained below. Creates self via LUI.UIElement.new, HeroAbilityUseString via LUI.UIText.new.

  unknowns: &#91;{"kind": "original_build", "gap": "Recovered-source revision is pinned; original PS4 build/byte/VM/native binding remains unverified."}, {"kind": "effective_data_settings_assets", "gap": "Engine/model/Dvar/asset/data requests do not supply effective runtime values, contents or ownership."}, {"kind": "server_service_persistence", "gap": "Unavailable authoritative server/service/provider code and successful persistence remain unavailable; not reconstructed or counted as completed."}, {"kind": "runtime_callback_lifetime", "gap": "Original loading, table overwrites, callback delivery/order, timings, state selection and UI cleanup are not runtime-proven."}&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/c4abcb5e220ffd0f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/c4abcb5e220ffd0f.json) at JSON pointer `/claims/4`.

  Archived evidence ID: `archived-record-00004` at JSON pointer `/units/69`; file SHA-256 `52df95eaa9f17f90427f6313acbc648c9bdffa0602f6444566bbe8fa1a54ba59`; selected record SHA-256 `c1198ee19f57e4a7dd90d32799e126fdcc544061e96aa452863955aa05a0dd10`.

- `hmh07-lua-follow3:064` (original lines 10-70, 10-70, 10-70, 10-70, 10-70, 10-70, 10-70, 10-70, 17-17, 47-47, 53-53, 57-57, 57-57, 57-57, 63-63, 72-77, 11-11, 41-41, 42-42, 63-63, 47-47, 66-66, 10-70, 11-11, 12-12, 17-17, 18-18, 19-19, 20-20, 21-21, 22-22, 23-23, 24-24, 26-26, 29-29, 30-30, 31-31, 32-32, 33-33, 34-34, 35-35, 36-36, 38-38, 41-41, 42-42, 43-43, 44-44, 47-47, 50-50, 53-53, 54-54, 57-57, 60-60): Constructs CoD.AmmoWidgetWZ_WeaponImage from the displayed menu/controller/layout arguments. Creates PowerWeaponDrainGadget3 as CoD.AmmoWidget_PowerWeaponDrain.new, PowerWeaponDrainGadget2 as CoD.AmmoWidget_PowerWeaponDrain.new, WeaponImage as LUI.UIFixedAspectRatioImage.new, HeroAbilityUseString as CoD.AmmoWidgetWZ_WeaponName.new. Connects 4 model/path references; the model subscription effects below specify which receiver changes and under which nil/value guard. Installs 1 event/action/override bindings; each callback keeps its captured controller/menu/widget references and executes only on its bound delivery. The ordered effect contract retains every property, model, visual, navigation, callback and return mutation in source order; returning self is not proof the original game loads this widget.

  unknowns: &#91;"Original source-to-PS4/VM/native/loader identity and bytecode fidelity are unverified.", "Effective settings, assets/tables/model schemas, server/service implementation and callback delivery/lifetime are unverified.", "Exact source request semantics do not prove rendering, networking, persistence, progression or game behavior.", "Public reuse is the frozen manager audit only; no worker web/repository discovery was performed."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/c4abcb5e220ffd0f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/c4abcb5e220ffd0f.json) at JSON pointer `/claims/5`.

  Archived evidence ID: `archived-record-00003` at JSON pointer `/units/63`; file SHA-256 `a63852530df9189721a410c240a42967af6648aa0fca4e70325b17a1e677ebb7`; selected record SHA-256 `181d4f2c521be974d70fa1bb8620507f50b0a3c895f12a920969a93e0b14f875`.
