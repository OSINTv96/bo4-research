# hashed/394487af02b60952.lua

Project-added notes. See the [code](../../src/lua/hashed/394487af02b60952.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `e90cb4bdcb830f08dddb24748bfb0d1e244d7b394518c9dd8fc9c301493c76d2`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/c98b88edd4edfb02.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua-follow6:019` (original lines 105-111, 105-105, 72-72, 11-11, 13-13, 72-72, 106-106, 107-107, 108-108, 109-109, 110-110, 105-105, 106-106, 107-107, 108-108, 109-109, 110-110, 111-111, 105-105, 106-106, 107-107, 108-108, 109-109, 110-110, 105-111, 105-111): Using its sole argument as the owning instance, close these child fields in this exact order: WeaponImage, WeaponAmmoCount2, WeaponAmmoCount, grappleWeapon, AmmoHeal_Prompt. No nil check, reset, explicit return, error recovery or retry occurs in this body; a failed child close can prevent later calls.

  unknowns: &#91;"Exact original source/build match and loader/table/global overwrite order", "Effective settings/storage/table/profile/model values", "Native render/model/event/timer lifetime and delivery", "Unavailable service/server behavior and final HMH membership"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/c98b88edd4edfb02-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/c98b88edd4edfb02.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00056` at JSON pointer `/units/18`; file SHA-256 `9b5470295d8bc5b945061358d29d8430f5da2392ccde6abf20deb11b8b9c027f`; selected record SHA-256 `eece7748bbf3a81e07ab4ea43f35d1775bff6440fb5ced19555f4b78ee0e9c28`.

- `hmh07-lua-follow4:015` (original lines 11-79): Builds the MP ammo display, initializes tankState only if unset, and links CurrentWeapon into its four ammo children. OneInChamber and GoldenBullet are stored state conditions. After registering close, optional PreLoadFunc runs at the recovered late position, then the OIC child is replaced with a fake outside oic. Creates self via LUI.UIElement.new, Blur via LUI.UIImage.new, EnemyFlagHeld via CoD.AmmoWidgetMP_HeldItem.new, Backer via LUI.UIImage.new, PanelDark via LUI.UIImage.new, PanelLight via LUI.UIImage.new, AmmoWidgetOneInTheChamber via CoD.AmmoWidget_OneInTheChamber.new, Frame via LUI.UIImage.new, FrameGolden via LUI.UIImage.new, FrameGoldenGlow via LUI.UIImage.new, GlowWeapon via LUI.UIImage.new, WeaponAmmoCount via CoD.AmmoWidget_WeaponInfo.new, StockAmmoWidget via CoD.AmmoWidget_StockAmmo.new, StockAmmoWidget2 via CoD.AmmoWidget_StockAmmo.new, LEDgraph via LUI.UIImage.new, LEDscreen via LUI.UIImage.new, Sheen via LUI.UIImage.new, GoldenAmmoSounds via LUI.UIElement.new, goldenBullet via LUI.UIImage.new, GlowImage via LUI.UIImage.new, GlowImage2 via LUI.UIImage.new, GlowTop via LUI.UIImage.new, GlowBtm via LUI.UIImage.new. Stores state predicates OneInChamber, GoldenBullet; their body effects require state-system evaluation.

  unknowns: &#91;{"kind": "original_build", "gap": "Recovered-source revision is pinned; original PS4 build/byte/VM/native binding remains unverified."}, {"kind": "effective_data_settings_assets", "gap": "Engine/model/Dvar/asset/data requests do not supply effective runtime values, contents or ownership."}, {"kind": "server_service_persistence", "gap": "Unavailable authoritative server/service/provider code and successful persistence remain unavailable; not reconstructed or counted as completed."}, {"kind": "runtime_callback_lifetime", "gap": "Original loading, table overwrites, callback delivery/order, timings, state selection and UI cleanup are not runtime-proven."}&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/c98b88edd4edfb02-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/c98b88edd4edfb02.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00004` at JSON pointer `/units/14`; file SHA-256 `52df95eaa9f17f90427f6313acbc648c9bdffa0602f6444566bbe8fa1a54ba59`; selected record SHA-256 `895edd2444134ef98ddb09df783c4cf2cc789d7466dba05341f4e44396131ef1`.
