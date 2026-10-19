# hashed/92e2bf6a2ad004f.lua

Project-added notes. See the [code](../../src/lua/hashed/92e2bf6a2ad004f.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `8b010ff2b9b2f6bb95a3efc37e54a897a43277e8086ea14a585ddc2606523b30`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/d6490f2ccdb6a7bf.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua-follow1:133` (original lines 19-19, 19-19): Constructs the perk feedback image and registers ordered FlakJacket, Armor, TacMask and Resistance predicates against damageFeedbackState flags. The model-link callback requests state validation. After optional PostLoadFunc it sets ignoreCurrentStateCheck true and returns self. The damage flag/enum values, predicate precedence and actual feedback delivery remain conditional.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/d6490f2ccdb6a7bf-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/d6490f2ccdb6a7bf.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00036` at JSON pointer `/units/132`; file SHA-256 `279ba12c6a1d4cfd1fb6c7e030a47694d4ee3982256bb21a0b3aa6909aef143b`; selected record SHA-256 `804995310e422f0ea121732e852b7ab23fcf377666e2b94f2d6fba3f40269cd2`.

- `hmh07-lua-follow1:200` (original lines 52-52, 52-52): Constructs the predicted-feedback indicator, registers its exact damage-feedback flag predicate and links damageFeedbackState to state validation. It optionally calls PostLoadFunc and returns self. The predicted flag's meaning/native value and actual feedback delivery remain conditional; no damage calculation occurs in this body.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/d6490f2ccdb6a7bf-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/d6490f2ccdb6a7bf.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00036` at JSON pointer `/units/199`; file SHA-256 `279ba12c6a1d4cfd1fb6c7e030a47694d4ee3982256bb21a0b3aa6909aef143b`; selected record SHA-256 `64ebb394d1dcc39fe0357c0bcd9c9b75f9325c841008d9b597cc13d1c6a69707`.

- `hmh07-lua-follow1:146` (original lines 148-148, 148-148, 151-151, 151-151): CallOriginalFirst appends the supplied callback to the table returned by OverrideFunction_GetFunctionTable. CallOriginalSecond inserts its callback at index1. Neither wrapper directly calls the original or callback or returns a value. The naming does not prove runtime order independently of the dispatcher, which remains a reusable available dependency.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/d6490f2ccdb6a7bf-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/d6490f2ccdb6a7bf.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00044` at JSON pointer ``; file SHA-256 `46ecb6cfe8fa919ec918f489610848dcd8b393e632706abbfd898ba7b2a05c62`.

- `hmh07-lua-follow1:203` (original lines 44-44, 44-44): Constructs friendly-feedback death/damage/down-arrow images and ordered state predicates. Preserve the recovered Stage2 predicate checking damage_feedback_state_1, the same enum used by Stage1; do not repair it to state2. Downed/death use their exact flags and Stage5 comparisons. A damageFeedbackState model link validates state; optional PostLoadFunc precedes self return.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/d6490f2ccdb6a7bf-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/d6490f2ccdb6a7bf.json) at JSON pointer `/claims/3`.

  Archived evidence ID: `archived-record-00036` at JSON pointer `/units/202`; file SHA-256 `279ba12c6a1d4cfd1fb6c7e030a47694d4ee3982256bb21a0b3aa6909aef143b`; selected record SHA-256 `2d9f5a1a52f86965b8bb0f3f3d30ee8a853d4a66b796dd65c1c316e52a1feebd`.

- `hmh07-lua:056` (original lines 11-158, 11-158, 20-22, 46-48, 53-55, 62-64, 68-70, 74-76, 80-82, 86-88, 92-94, 98-100, 104-106, 110-112, 116-118, 122-124, 128-130, 134-136, 139-147, 148-150, 149-149, 44-44, 19-19, 52-52, 148-148, 151-151, 12-12, 33-33, 40-40, 26-26, 31-31, 37-37, 986-990, 151-151, 11-158, 186-204, 207-226, 227-256, 259-269, 270-290, 293-322, 323-366, 369-381, 382-414, 417-428, 429-460, 463-475, 476-495, 498-523, 524-560, 563-588, 589-625, 628-653, 654-690, 693-718, 719-755, 758-805, 806-853, 856-881, 882-918, 921-946, 947-983, 160-182, 986-990): Constructs perk/friendly/predicted hit feedback children bound to self. Ordered state predicates use exact feedback flags and stages for vehicle, alternate, friendly, downed, death and stages1..5; unknown hashed flags are retained. damageFeedbackState changes revalidate, and the CallOriginalFirst setState hook calls OnDamageFeedbackSetState with the requested state. No health/damage producer or native flag definition is reconstructed here.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used.", "Source-ready close body exists outside frozen allowed companion range; exact locator is retained in new_dependencies. Other class clip bodies not frozen were not authored.", "Additional same-class reset/clip/close body ranges are available but outside the frozen author scope; exact locators are in unfrozen_same_class_body_locators and source-frontier.json. No body authoring or completion credit for them.", "Relative original/custom execution order of OverrideFunction_CallOriginalFirst/Second requires the available helper source contract; names are preserved without deriving order from naming alone."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/d6490f2ccdb6a7bf-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/d6490f2ccdb6a7bf.json) at JSON pointer `/claims/4`.

  Archived evidence ID: `archived-record-00533` at JSON pointer ``; file SHA-256 `6eed7876f407c64a55355164e98b539f746c27ca3dd7e67a2cbe0add5dd7bc5c`.

- `hmh07-lua-follow1:008` (original lines 26-26, 31-31, 37-37, 33-33, 40-40, 26-26, 31-31, 37-37, 26-26, 11-158, 31-31, 11-158, 37-37, 11-158, 33-33, 40-40, 33-33, 11-158, 40-40, 11-158): UIImage.new forwards all eight layout arguments to UIElement.new, sets UIImage class, calls setupUIImage and returns self. GetCachedMaterial indexes Materials by requested key; only a nil cache entry calls RegisterMaterial and writes its return to the cache, then returns the cached value. False is a cache hit; a nil RegisterMaterial result can be retried next call. No image/native/material ownership or original runtime contract is supplied.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/d6490f2ccdb6a7bf-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/d6490f2ccdb6a7bf.json) at JSON pointer `/claims/5`.

  Archived evidence ID: `archived-record-00036` at JSON pointer `/units/7`; file SHA-256 `279ba12c6a1d4cfd1fb6c7e030a47694d4ee3982256bb21a0b3aa6909aef143b`; selected record SHA-256 `7329bd99e083ca457a54272bf2df1457c445a3fb2e8a07aa636d127734ffcbbf`.

- `hmh07-lua-follow1:125` (original lines 12-12, 12-12): UIElement.new tries ConstructLUIElement with eight supplied layout arguments when the first is truthy, then sets initial class and returns only on a truthy constructed value. Otherwise it calls ConstructLUIElement with m_defaultAnimationState and falls through without an explicit return or setInitialClass in this recovered text. Preserve that fidelity defect. createFake returns a fresh empty table with fakeElemMetaTable; fake operations and native construction remain separate contracts.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/d6490f2ccdb6a7bf-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/d6490f2ccdb6a7bf.json) at JSON pointer `/claims/6`.

  Archived evidence ID: `archived-record-00047` at JSON pointer ``; file SHA-256 `0a2ed5281f322b9558d79fcfa95c412c52c1a5b3106117496e96cceee9304688`.

- `hmh07-lua-follow1:033` (original lines 11-158, 11-158): Creates Hud_MP_Codcaster menu, safe-area child and MP HUD components, current-weapon damage model binding, score notifications and spectator/profile state consumers. On score_event it prioritizes bounty score, then combat-efficiency score when spawn selection is inactive, then normal score. Objective ShowNotification predicates are AlwaysFalse here. HideAllButScoreboard is killcam/final/round/stage visibility union; SpeedBoost uses exact gadget id/state; HideForCodCaster requires spectator profile. X input is blocked only while AreXButtonPressesDisallowed; player_spawned outside draft disallows X400ms. Menu_loaded sizes PC to HUD area and console to safe area, dispatches to children when unhandled; then focus/state restoration, close registration, postload, back-button preservation, grenade warnings and cursor disable occur in literal order. Menu selection into this MP codcaster path remains conditional; no universal HMH requirement is inferred.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/d6490f2ccdb6a7bf-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/d6490f2ccdb6a7bf.json) at JSON pointer `/claims/7`.

  Archived evidence ID: `archived-record-00141` at JSON pointer ``; file SHA-256 `ddad7dbd01ea8649b951264dc42cba35d6d9601b1a529d9f54126cea9955928d`; selected record SHA-256 `c56ebf9c608a15c79d23ec0f75faaafe8069aa9ead3cd0db39b2bea6006b294a`.

- `hmh07-lua-follow1:233` (original lines 149-149, 149-149): The27 HUD helpers preserve exact waypoint/objective/model setup, client/actor/grenade/armblade loops, blood cache, focus routing, timers and wheel input/choice behavior. Waypoint setup is reached only in the recovered nonempty resolved-path arm; active/done widgets use exact state callbacks and removal order. Positive SetXFractionByModel starts a16-duration updater without closing an existing positive-path timer or clamping its ratio. Damage state uses a600-duration reset timer. Wheel length uses0.5/0.9 hysteresis; disabling can recover the previous wedge then pulses chosen true/false before _onChooseWedge. Right-stick close unlock and exact spray/callout notifications remain deferred/native requests, not game proof.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/d6490f2ccdb6a7bf-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/d6490f2ccdb6a7bf.json) at JSON pointer `/claims/8`.

  Archived evidence ID: `archived-record-00377` at JSON pointer ``; file SHA-256 `30cb806d53a0d0955d80e44bd206fbfa5f894b67f35afe44ac545e1b01c1037c`; selected record SHA-256 `1543f963dd1e2812c6a553e6cf8c93c3cf7dacd572f3fdec15c3d39ffff6cbf0`.

- `hmh07-lua-follow1:213` (original lines 160-182, 186-204, 207-226, 227-256, 259-269, 270-290, 293-322, 323-366, 369-381, 382-414, 417-428, 429-460, 463-475, 476-495, 498-523, 524-560, 563-588, 589-625, 628-653, 654-690, 693-718, 719-755, 758-805, 806-853, 856-881, 882-918, 921-946, 947-983, 986-990, 160-182, 13-13, 13-13, 160-182, 160-160, 186-204, 13-13, 184-184, 13-13, 184-184, 186-204, 186-186, 207-226, 13-13, 184-184, 13-13, 184-184, 207-226, 207-207, 210-215, 210-210, 227-256, 13-13, 184-184, 13-13, 184-184, 227-256, 227-227, 233-245, 233-233, 234-238, 234-234, 259-269, 13-13, 184-184, 13-13, 184-184, 259-269, 259-259, 270-290, 13-13, 184-184, 13-13, 184-184, 270-290, 270-270, 276-281, 276-276, 293-322, 13-13, 184-184, 13-13, 184-184, 293-322, 293-293, 306-316, 306-306, 307-310, 307-307, 323-366, 13-13, 184-184, 13-13, 184-184, 323-366, 323-323, 326-331, 326-326, 336-343, 336-336, 355-360, 355-355, 369-381, 13-13, 184-184, 13-13, 184-184, 369-381, 369-369, 382-414, 13-13, 184-184, 13-13, 184-184, 382-414, 382-382, 385-390, 385-385, 395-402, 395-395, 417-428, 13-13, 184-184, 13-13, 184-184, 417-428, 417-417, 429-460, 13-13, 184-184, 13-13, 184-184, 429-460, 429-429, 432-437, 432-432, 442-449, 442-442, 463-475, 13-13, 184-184, 13-13, 184-184, 463-475, 463-463, 476-495, 13-13, 184-184, 13-13, 184-184, 476-495, 476-476, 485-490, 485-485, 498-523, 13-13, 184-184, 13-13, 184-184, 498-523, 498-498, 501-511, 501-501, 502-506, 502-502, 524-560, 13-13, 184-184, 13-13, 184-184, 524-560, 524-524, 527-532, 527-527, 537-542, 537-537, 549-553, 549-549, 563-588, 13-13, 184-184, 13-13, 184-184, 563-588, 563-563, 566-576, 566-566, 567-571, 567-567, 589-625, 13-13, 184-184, 13-13, 184-184, 589-625, 589-589, 592-597, 592-592, 602-607, 602-602, 614-618, 614-614, 628-653, 13-13, 184-184, 13-13, 184-184, 628-653, 628-628, 631-641, 631-631, 632-636, 632-632, 654-690, 13-13, 184-184, 13-13, 184-184, 654-690, 654-654, 657-662, 657-657, 667-672, 667-667, 679-683, 679-679, 693-718, 13-13, 184-184, 13-13, 184-184, 693-718, 693-693, 696-706, 696-696, 697-701, 697-697, 719-755, 13-13, 184-184, 13-13, 184-184, 719-755, 719-719, 722-727, 722-722, 732-737, 732-732, 744-748, 744-744, 758-805, 13-13, 184-184, 13-13, 184-184, 758-805, 758-758, 766-776, 766-766, 767-770, 767-767, 783-799, 783-783, 784-793, 784-784, 785-788, 785-785, 806-853, 13-13, 184-184, 13-13, 184-184, 806-853, 806-806, 809-814, 809-809, 819-823, 819-819, 830-835, 830-830, 842-847, 842-842, 856-881, 13-13, 184-184, 13-13, 184-184, 856-881, 856-856, 864-874, 864-864, 865-868, 865-865, 882-918, 13-13, 184-184, 13-13, 184-184, 882-918, 882-882, 885-890, 885-885, 895-899, 895-895, 906-911, 906-906, 921-946, 13-13, 184-184, 13-13, 184-184, 921-946, 921-921, 924-934, 924-924, 925-929, 925-925, 947-983, 13-13, 184-184, 13-13, 184-184, 947-983, 947-947, 950-955, 950-950, 960-965, 960-960, 972-976, 972-972, 986-990, 151-151, 151-151, 151-151, 13-13, 151-151, 13-13, 986-990, 986-986, 160-182, 186-204, 207-226, 227-256, 259-269, 270-290, 293-322, 323-366, 369-381, 382-414, 417-428, 429-460, 463-475, 476-495, 498-523, 524-560, 563-588, 589-625, 628-653, 654-690, 693-718, 719-755, 758-805, 806-853, 856-881, 882-918, 921-946, 947-983, 986-990, 172-172, 221-221, 251-251, 264-264, 285-285, 301-301, 350-350, 376-376, 409-409, 423-423, 455-455, 160-182, 186-204, 207-226, 227-256, 259-269, 270-290, 293-322, 323-366, 369-381, 382-414, 417-428, 429-460, 463-475, 476-495, 498-523, 524-560, 563-588, 589-625, 628-653, 654-690, 693-718, 719-755, 758-805, 806-853, 856-881, 882-918, 921-946, 947-983, 986-990): Adds damage-feedback reset, the selected DefaultState/vehicle/alternate/friendly/stage1..5/downed/death clips and three-child close. Every slot preserves its exact image/color/scale/alpha baseline and timed return-to-default chains; nested completion/interruption callbacks are owned once. Reuse constructor056 predicates, flag interpretation and model paths without expanding unlisted helpers or claiming damage gameplay/runtime proof.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/d6490f2ccdb6a7bf-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/d6490f2ccdb6a7bf.json) at JSON pointer `/claims/9`.

  Archived evidence ID: `archived-record-00777` at JSON pointer ``; file SHA-256 `76b25ed0a7a6706db38d160bd9acce1fec5002eec8dd5ce0b98b255faba406ac`; selected record SHA-256 `1d31b52dc075cd548a39555665b7c617019f5b5d7f7a1ed048c1ba368a47ede4`.
