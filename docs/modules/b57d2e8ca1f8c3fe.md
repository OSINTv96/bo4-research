# hashed/594eb41daa294dc8.lua

Project-added notes. See the [code](../../src/lua/hashed/594eb41daa294dc8.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `8637e06d2bc40c14993318b547f2e8287241869582cbc08cc4a70ca864988640`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/b57d2e8ca1f8c3fe.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua-follow5:059` (original lines 242-247, 242-242, 154-154, 11-163, 13-13, 242-247, 242-242, 154-154, 11-163, 13-13, 11-163, 242-247): On close callback invocation, execute in exact order: f21_arg0.InventoryEquipmentLarge:close(); f21_arg0.InventoryEquipmentSmall:close(); f21_arg0.ArrowR:close(); f21_arg0.ArrowL:close(). Fall through with no explicit return. Members and close/helper availability are unguarded; no rollback, idempotence or recovery is shown.

  unknowns: {"provider_or_lexical": &#91;&#93;, "source_fidelity": &#91;&#93;, "original_build": "Recovered source is not matched to original PS4 bytecode/build; @0 is not a native address.", "VM_native": "Lua dialect, metatables, native/UI API execution, model dispatch/cancellation and input timing remain unverified.", "data_settings_assets": "Literal references do not supply effective model values, settings, data tables, localization or asset availability.", "server_service": "Online, stats, progression, marketing, lobby and backend behavior are unavailable service boundaries when requested by these exact bodies.", "runtime": "No game, console, account, router, save, native tool or independent review was run."}

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b57d2e8ca1f8c3fe-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b57d2e8ca1f8c3fe.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00034` at JSON pointer `/units/58`; file SHA-256 `781c1c1aee59bfc36951652bab7a837686810fc0aebaac4cb4ddfe8fe782f24f`; selected record SHA-256 `3c0bc4d140a6b561c322ae1c233d126f78ab350b8a75990ee83f2e1bfa08d7e0`.

- `hmh07-lua-follow4:076` (original lines 11-163, 11-163, 26-31, 48-50, 53-56, 58-60, 68-70, 73-76, 79-81, 88-90, 94-96, 100-102, 108-116, 120-128, 129-132, 136-144, 11-163, 11-163, 11-163, 11-163, 11-163, 11-163, 12-12, 20-20, 28-28, 29-29, 35-35, 44-44, 49-49, 49-49, 58-58, 59-59, 64-64, 69-69, 69-69, 79-79, 80-80, 89-89, 95-95, 101-101, 154-154, 242-247, 154-154, 160-160, 161-161, 156-156, 107-107, 119-119, 135-135, 11-163, 11-163): Builds Warzone contextual extra items; exact child constructors, current item models and conditional prompt/state callbacks are retained below. This is UI construction, not an inventory grant. Creates self via LUI.UIElement.new, InventoryEquipmentLarge via LUI.UIList.new, InventoryEquipmentSmall via LUI.GridLayout.new, ArrowR via CoD.WarzoneContextualExtraItemsArrow.new, ArrowL via CoD.WarzoneContextualExtraItemsArrow.new. Stores state predicates Visible, Visible, InventoryOpen, HiddenPreference, KBM; their body effects require state-system evaluation.

  unknowns: &#91;{"kind": "original_build", "gap": "Recovered-source revision is pinned; original PS4 build/byte/VM/native binding remains unverified."}, {"kind": "effective_data_settings_assets", "gap": "Engine/model/Dvar/asset/data requests do not supply effective runtime values, contents or ownership."}, {"kind": "server_service_persistence", "gap": "Unavailable authoritative server/service/provider code and successful persistence remain unavailable; not reconstructed or counted as completed."}, {"kind": "runtime_callback_lifetime", "gap": "Original loading, table overwrites, callback delivery/order, timings, state selection and UI cleanup are not runtime-proven."}&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b57d2e8ca1f8c3fe-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b57d2e8ca1f8c3fe.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00004` at JSON pointer `/units/75`; file SHA-256 `52df95eaa9f17f90427f6313acbc648c9bdffa0602f6444566bbe8fa1a54ba59`; selected record SHA-256 `5fbf3f682d84751313bed045746efeedcdc1a7393b39fd4bd1c2a79b027587b0`.
