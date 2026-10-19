# hashed/4c7729aa022f61a6.lua

Project-added notes. See the [code](../../src/lua/hashed/4c7729aa022f61a6.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `4c304c536b0c9ec0f6049f71cc361e713b1005c6bf797c9f49e3a646efd26fba`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/ebea20dbec75746f.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua:041` (original lines 7-313): Builds the WZ back HUD children including team/player/ammo/inventory/compass/collapse/reinsertion/death notifications. Spawn selection hides deployable notifications; dead+not hacked+not spawn-select gates DeathCamContainer. KilledBy is locally always hidden; killer identity is hidden outside killcam, binds Attacker and updates emblem/name/rank views only for nonnil data. Overall caster-profile/spawn-select hides are separate predicates. The constructor wires child source contracts; it does not reconstruct every child, event producer or server state.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used.", "Source-ready close body exists outside frozen allowed companion range; exact locator is retained in new_dependencies. Other class clip bodies not frozen were not authored.", "Additional same-class reset/clip/close body ranges are available but outside the frozen author scope; exact locators are in unfrozen_same_class_body_locators and source-frontier.json. No body authoring or completion credit for them."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/ebea20dbec75746f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/ebea20dbec75746f.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00334` at JSON pointer ``; file SHA-256 `d7b01efaff174a0a14ed475e48e08a33c016b6923722ae27d3d1cba3b746a1d0`.

- `hmh07-lua-follow2:113` (original lines 71-71, 60-60, 67-67, 69-69, 70-70, 72-72, 77-77, 83-83, 90-90, 91-91, 93-93, 97-97, 103-103, 110-110, 111-111, 113-113, 117-117, 123-123, 308-308, 312-312, 92-92, 60-60, 67-67, 69-69, 70-70, 72-72, 77-77, 83-83, 90-90, 91-91, 93-93, 97-97, 103-103, 110-110, 111-111, 113-113, 117-117, 123-123, 308-308, 312-312, 112-112, 60-60, 67-67, 69-69, 70-70, 72-72, 77-77, 83-83, 90-90, 91-91, 93-93, 97-97, 103-103, 110-110, 111-111, 113-113, 117-117, 123-123, 308-308, 312-312, 7-313, 71-71, 92-92, 112-112): EnabledAndProfile comparison short-circuits IsShoutcaster before exact equality of profile boolean with supplied value. Aerial camera returns visibility flag when truthy, otherwise native aerial-cam result. IsCodCasterOrAssigned returns IsCodCaster when truthy else assigned-state helper. No model producer, spectator assignment or actual camera transition is reconstructed.

  unknowns: &#91;"Exact original PS4/source version matching, recovered Lua/VM fidelity and global/native/LUI provider identity remain unverified.", "Model/storage/DDL/assets/localization/dvar/enum values, callback delivery/cancellation/error behavior, native networking and unavailable service/server code are separate inputs.", "Other-file locals are not providers by spelling. Exact qualified global declarations are source candidates until loader/table identity and caller conditions bind them.", "No implicit nil/type checks, exception recovery, timer/model disposal, idempotence or guarantee that later effects run after an error is added."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/ebea20dbec75746f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/ebea20dbec75746f.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00052` at JSON pointer ``; file SHA-256 `3408409cff40bee6f3712fa7a758e88917c8bbf1e8bbc73683c49e932cc2d04c`.

- `hmh07-lua-follow1:052` (original lines 7-313, 60-60, 67-67, 69-69, 70-70, 72-72, 77-77, 83-83, 90-90, 91-91, 93-93, 97-97, 103-103, 110-110, 111-111, 113-113, 117-117, 123-123, 308-308, 312-312, 7-313, 7-313, 59-61, 65-78, 82-84, 88-98, 102-104, 108-118, 122-124, 130-138, 142-150, 154-162, 166-174, 178-186, 190-198, 202-210, 214-222, 226-234, 238-246, 250-258, 262-270, 274-282, 286-294, 298-306, 7-313, 7-313, 71-71, 92-92, 112-112, 141-141, 153-153, 309-309, 17-17, 35-35, 48-48, 7-313, 66-66, 68-68, 83-83, 89-89, 103-103, 109-109, 123-123, 60-60, 8-8, 18-18, 27-27, 36-36, 49-49, 14-14, 24-24, 32-32, 45-45): Creates grid/background images for quick-inventory vignette. Hidden tests not quick inventory open. HealthAndEquipment/Health/Equipment predicates test available counts>0; EMP variants add exact EMP/HUD visibility and codcaster inventory-profile guards. Non-EMP count states do not themselves negate EMP, so retain external priority arbitration. Inventory/count/visibility changes only request reevaluation. Optional PostLoadFunc then returns self; no explicit close hook is selected in this constructor, and no inventory state producer is inferred.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/ebea20dbec75746f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/ebea20dbec75746f.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00057` at JSON pointer ``; file SHA-256 `eb1bac22e9eb7ace176fbad88e6aa33f5ceedf5d46502faf6b86cd26edff0c84`.
