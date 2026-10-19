# hashed/130ff13ac753aef9.lua

Project-added notes. See the [code](../../src/lua/hashed/130ff13ac753aef9.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `c0a9c62b6426439d403febd858f4f744f637a41d658ef9efadffc0ecc7b82634`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/bfb23bbefa1a3e3f.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua:008` (original lines 75-75, 75-75): Constructs NoiseBacking and a tiled shader image, applies fixed visual properties, optionally invokes PostLoadFunc, and returns self. There are no local model/event/state predicates or explicit close hooks in the selected body. Shared callers can change its material, alpha and color after construction; those caller writes are not an invocation of a hidden gameplay routine.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/bfb23bbefa1a3e3f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/bfb23bbefa1a3e3f.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/7`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `0716f0c96bec29734ad290ec1c979c5919490d10598fa80ec8ea027994d843c4`.

- `hmh07-lua:215` (original lines 106-106, 102-110, 118-118, 114-122): Returns Engine.toupper(Engine localization(arg0)); the nested localization finishes before uppercasing. Used for labels and model-driven text in the cited common menus. No validation or nil fallback; no subscription, persistence or cleanup.

  unknowns: &#91;"Original Lua-to-PS4 CUSA11100 build binding and bytecode/VM/decompiler fidelity unverified.", "Effective HMH settings, enum values, model/data production, LUI state arbitration, event delivery/ordering/cancellation, assets, storage/DDL, networking/service behavior remain explicit gaps where called.", "External helper bodies not selected here are dependencies only; no nil/error recovery assumed beyond visible source. Named LUI override APIs are preserved; no original/new callback ordering is guaranteed without their source contract.", "No independent correctness review, retail execution or function completion credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/bfb23bbefa1a3e3f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/bfb23bbefa1a3e3f.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/214`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `021dadb9180d2be8bae3648293f913e9c483952d2fe58405e2eb68f4dd74bdc2`.

- `hmh07-lua:085` (original lines 154-154, 154-154): Dispatches lose_focus with controller, then sets _readyForCustomFocus=false. If event dispatch throws the reset is not reached; no error protection or explicit return exists.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/bfb23bbefa1a3e3f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/bfb23bbefa1a3e3f.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/84`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `321df77fe252482281445a2e1a3c0b5a6c5120079820cad13bba09d483cbe359`.

- `hmh07-lua:227` (original lines 40-40, 36-44): Cited common buttons call this decorative constructor directly. Builds four focus-bracket corner image fields, optionally invokes PostLoadFunc and returns self. No model subscription, state predicate, key/button action or explicit close override occurs in this span. The selected constructor has no local visibility/motion dispatch. The six cited immediate caller contexts preserve their exact construction/attachment requests; four explicitly request FocusBrackets:setAlpha(0), while two attach/store without that immediate alpha request. Other parent clips, ownership and actual rendering remain unresolved. Do not infer a callback or gameplay action from focus art.

  unknowns: &#91;"Original Lua-to-PS4 CUSA11100 build binding and bytecode/VM/decompiler fidelity unverified.", "Effective HMH settings, enum values, model/data production, LUI state arbitration, event delivery/ordering/cancellation, assets, storage/DDL, networking/service behavior remain explicit gaps where called.", "External helper bodies not selected here are dependencies only; no nil/error recovery assumed beyond visible source. Named LUI override APIs are preserved; no original/new callback ordering is guaranteed without their source contract.", "No independent correctness review, retail execution or function completion credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/bfb23bbefa1a3e3f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/bfb23bbefa1a3e3f.json) at JSON pointer `/claims/3`.

  Archived evidence ID: `archived-record-00161` at JSON pointer ``; file SHA-256 `e95f0732a64ee40f4f281e712a2478cf158c85657eceb29b4c332c55168c5b8b`.

- `hmh07-lua:182` (original lines 11-164, 26-26, 36-36, 41-41, 47-47, 56-56, 66-66, 77-77, 79-79, 85-85, 95-95, 96-96, 106-106, 117-117, 118-118, 131-131, 144-144, 152-152, 157-157, 178-178, 180-180, 183-183, 185-185, 188-188, 191-191, 192-192, 193-193, 195-195, 198-198, 213-213, 216-216, 220-220, 222-222, 225-225, 227-227, 228-228, 233-233, 236-236, 241-241, 244-244, 248-248, 254-254, 256-256, 263-263, 266-266, 267-267, 270-270, 273-273, 274-274, 275-275, 281-281, 284-284, 285-285, 286-286, 287-287, 291-291, 294-294, 295-295, 296-296, 297-297, 301-301, 304-304, 305-305, 306-306, 307-307, 311-311, 314-314, 315-315, 317-317, 318-318, 326-326, 327-327, 328-328, 329-329, 334-334, 337-337, 338-338, 339-339, 340-340, 344-344, 347-347, 349-349, 350-350, 357-357, 358-358, 359-359, 360-360, 364-364, 371-371, 372-372, 373-373, 374-374, 380-380, 383-383, 384-384, 385-385, 386-386, 390-390, 393-393, 394-394, 395-395, 396-396, 400-400, 403-403, 404-404, 405-405, 406-406, 410-410, 413-413, 414-414, 416-416, 417-417, 425-425, 426-426, 427-427, 428-428, 433-433, 436-436, 437-437, 438-438, 439-439, 443-443, 446-446, 448-448, 449-449, 456-456, 457-457, 458-458, 459-459, 463-463, 475-475, 480-480, 486-486, 498-498, 503-503, 509-509, 513-513, 524-524, 527-527, 528-528, 531-531, 534-534, 535-535, 536-536, 542-542, 547-547, 553-553, 556-556, 557-557, 558-558, 559-559, 564-564, 574-574, 575-575, 576-576, 577-577, 583-583, 588-588, 594-594, 597-597, 598-598, 599-599, 600-600, 605-605, 617-617, 621-621, 633-633, 637-637, 640-640, 652-652, 656-656, 659-659, 663-663, 674-674, 677-677, 678-678, 681-681, 684-684, 685-685, 686-686, 692-692, 696-696, 699-699, 702-702, 703-703, 704-704, 705-705, 710-710, 720-720, 721-721, 722-722, 723-723, 729-729, 733-733, 736-736, 739-739, 740-740, 741-741, 742-742, 747-747, 756-756, 760-760, 766-766, 778-778, 782-782, 788-788, 792-792, 800-800, 803-803, 804-804, 807-807, 810-810, 811-811, 812-812, 818-818, 822-822, 828-828, 831-831, 832-832, 833-833, 834-834, 839-839, 846-846, 847-847, 848-848, 849-849, 855-855, 859-859, 865-865, 868-868, 869-869, 870-870, 871-871, 876-876, 882-882, 883-883, 884-884, 153-153, 159-159, 163-163, 11-164, 166-166, 166-199, 11-164, 201-201, 203-206, 11-164, 201-201, 207-257, 11-164, 201-201, 258-366, 11-164, 201-201, 367-465, 11-164, 201-201, 468-488, 11-164, 201-201, 489-515, 11-164, 201-201, 516-566, 11-164, 201-201, 567-607, 11-164, 201-201, 610-623, 11-164, 201-201, 626-642, 11-164, 201-201, 643-665, 11-164, 201-201, 666-712, 11-164, 201-201, 713-749, 11-164, 201-201, 752-771, 11-164, 201-201, 772-794, 11-164, 201-201, 795-841, 11-164, 201-201, 842-878, 11-164, 881-881, 881-885, 40-40, 35-45, 75-75, 70-80, 137-137, 132-142, 157-157, 152-162, 12-12, 7-17, 20-20, 15-25, 28-28, 23-33, 49-49, 44-54, 58-58, 53-63, 68-68, 63-73, 76-76, 71-81, 87-87, 82-92, 108-108, 103-113, 120-120, 115-125, 146-146, 141-151, 18-18, 13-23, 25-25, 20-30, 34-34, 29-39, 45-45, 40-50, 55-55, 50-60, 65-65, 60-70, 84-84, 79-89, 130-130, 125-135, 142-142, 137-147, 93-93, 88-98, 104-104, 99-109, 115-115, 110-120, 106-106, 101-111, 118-118, 113-123, 153-153, 148-158, 160-160, 155-165, 27-27, 22-32, 48-48, 43-53, 57-57, 52-62, 67-67, 62-72, 86-86, 81-91, 133-133, 128-138, 145-145, 140-150, 154-154, 149-159, 201-201, 201-880, 13-13, 11-164, 11-164): Constructed directly by three cited common button wrappers; they merge Disabled/Locked/TrialLocked conditions, so this constructor alone cannot decide their HMH feasibility. Builds visual layers, focus brackets/pixel backing/lines and normal/focus labels. Global lobbyNav notification calls SetLoseFocusToSelf only when ParentHasChildFocus. No selection button callback is installed here. CallOriginalSecond close invokes linked __onClose; exact child close calls retained. Class-linked state clips reset before focus/locked/disabled visual changes, schedule keyframes and register interrupted/transition handlers; scheduling does not prove completion. Optional postload then self return.

  unknowns: &#91;"Original Lua-to-PS4 CUSA11100 build binding and bytecode/VM/decompiler fidelity unverified.", "Effective HMH settings, enum values, model/data production, LUI state arbitration, event delivery/ordering/cancellation, assets, storage/DDL, networking/service behavior remain explicit gaps where called.", "External helper bodies not selected here are dependencies only; no nil/error recovery assumed beyond visible source. Named LUI override APIs are preserved; no original/new callback ordering is guaranteed without their source contract.", "No independent correctness review, retail execution or function completion credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/bfb23bbefa1a3e3f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/bfb23bbefa1a3e3f.json) at JSON pointer `/claims/4`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/181`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `8973e84dcce42bd5794acd46f8ef603d7941c96b279e5c7d7509db9e24bc3deb`.

- `hmh07-lua-follow1:123` (original lines 201-880, 201-880, 13-13, 13-13, 203-206, 203-203, 207-257, 207-207, 218-229, 218-218, 219-223, 219-219, 258-366, 258-258, 261-276, 261-261, 262-268, 262-262, 283-288, 283-283, 293-298, 293-293, 303-308, 303-303, 313-319, 313-313, 325-330, 325-325, 336-341, 336-336, 346-351, 346-346, 356-361, 356-356, 367-465, 367-367, 370-375, 370-370, 382-387, 382-382, 392-397, 392-392, 402-407, 402-402, 412-418, 412-412, 424-429, 424-424, 435-440, 435-435, 445-450, 445-445, 455-460, 455-455, 468-488, 468-468, 489-515, 489-489, 516-566, 516-516, 522-537, 522-522, 523-529, 523-523, 555-560, 555-555, 567-607, 567-567, 573-578, 573-573, 596-601, 596-596, 610-623, 610-610, 626-642, 626-626, 643-665, 643-643, 666-712, 666-666, 672-687, 672-672, 673-679, 673-673, 701-706, 701-701, 713-749, 713-713, 719-724, 719-719, 738-743, 738-738, 752-771, 752-752, 772-794, 772-772, 795-841, 795-795, 798-813, 798-798, 799-805, 799-799, 830-835, 830-830, 842-878, 842-842, 845-850, 845-845, 867-872, 867-867, 201-880, 11-164, 166-166, 166-199, 11-164, 201-201, 203-206, 11-164, 201-201, 207-257, 11-164, 201-201, 258-366, 11-164, 201-201, 367-465, 11-164, 201-201, 468-488, 11-164, 201-201, 489-515, 11-164, 201-201, 516-566, 11-164, 201-201, 567-607, 11-164, 201-201, 610-623, 11-164, 201-201, 626-642, 11-164, 201-201, 643-665, 11-164, 201-201, 666-712, 11-164, 201-201, 713-749, 11-164, 201-201, 752-771, 11-164, 201-201, 772-794, 11-164, 201-201, 795-841, 11-164, 201-201, 842-878, 11-164, 881-881, 881-885, 201-880): Installs the mini director button focus, gain/loss, locked and disabled presentation callbacks. Focus changes brackets, glow, highlight, text, lock image and backing; gain/loss slots animate their exact recorded baselines with independent completion chains. Focus can request itself through nextClip. The stopped constructor182 supplies state predicates/reset context; neither all table states nor actual focus delivery are proved HMH-visible.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/bfb23bbefa1a3e3f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/bfb23bbefa1a3e3f.json) at JSON pointer `/claims/5`.

  Archived evidence ID: `archived-record-00751` at JSON pointer ``; file SHA-256 `7c364ad54921215d9333fe5e3b364c1083a927ef2fe8be1ef849ca576b319d38`; selected record SHA-256 `ef2f46441d9b44c9655e177c0dfea39898a954db53e3368a430fcf66351db6d6`.

- `hmh07-lua:035` (original lines 11-164): Creates the mini play-button child; its Disabled predicate is not private host. Parent Visible is locally always true, but the director-public caller supplies stricter WZ/session/stage/host predicates. Private-client updates revalidate the child. Default focus is the mini child; frozen clips/reset/close belong to this exact class. This constructor alone does not launch matchmaking.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/bfb23bbefa1a3e3f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/bfb23bbefa1a3e3f.json) at JSON pointer `/claims/6`.

  Archived evidence ID: `archived-record-00657` at JSON pointer ``; file SHA-256 `e9cb7394fbffdb5c73ff3b0a2b4e6fb1f9e75098494843b8b3ca7c063018bd46`.

- `hmh07-lua:193` (original lines 8-8, 4-12): InheritFrom is executed at the cited class assignments, not merely imported. Missing/falsy base throws explicit LUI Error. Otherwise makes a new table with super=base, sets its metatable __index=base, creates a fresh m_eventHandlers table with __index=base.m_eventHandlers, then returns the new class. It shares fallback handlers while permitting per-class handler writes. Does not instantiate widgets, invoke inherited callbacks or close anything. Metatable/native VM behavior and base fields are assumed, no further validation.

  unknowns: &#91;"Original Lua-to-PS4 CUSA11100 build binding and bytecode/VM/decompiler fidelity unverified.", "Effective HMH settings, enum values, model/data production, LUI state arbitration, event delivery/ordering/cancellation, assets, storage/DDL, networking/service behavior remain explicit gaps where called.", "External helper bodies not selected here are dependencies only; no nil/error recovery assumed beyond visible source. Named LUI override APIs are preserved; no original/new callback ordering is guaranteed without their source contract.", "No independent correctness review, retail execution or function completion credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/bfb23bbefa1a3e3f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/bfb23bbefa1a3e3f.json) at JSON pointer `/claims/7`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/192`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `28096b9a20c988def77f03e8d965db4759673d7a552db8efd9d89c53725de88c`.

- `hmh07-lua-follow1:146` (original lines 157-157, 157-157, 11-164, 166-166, 166-199, 11-164, 201-201, 203-206, 11-164, 201-201, 207-257, 11-164, 201-201, 258-366, 11-164, 201-201, 367-465, 11-164, 201-201, 468-488, 11-164, 201-201, 489-515, 11-164, 201-201, 516-566, 11-164, 201-201, 567-607, 11-164, 201-201, 610-623, 11-164, 201-201, 626-642, 11-164, 201-201, 643-665, 11-164, 201-201, 666-712, 11-164, 201-201, 713-749, 11-164, 201-201, 752-771, 11-164, 201-201, 772-794, 11-164, 201-201, 795-841, 11-164, 201-201, 842-878, 11-164, 881-881, 881-885): CallOriginalFirst appends the supplied callback to the table returned by OverrideFunction_GetFunctionTable. CallOriginalSecond inserts its callback at index1. Neither wrapper directly calls the original or callback or returns a value. The naming does not prove runtime order independently of the dispatcher, which remains a reusable available dependency.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/bfb23bbefa1a3e3f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/bfb23bbefa1a3e3f.json) at JSON pointer `/claims/8`.

  Archived evidence ID: `archived-record-00044` at JSON pointer ``; file SHA-256 `46ecb6cfe8fa919ec918f489610848dcd8b393e632706abbfd898ba7b2a05c62`.

- `hmh07-lua:037` (original lines 11-164): Creates ready/custom-start controls, timer and progress fills. Ordered states cover hide-on-start, countdown, insufficient players, inability to ready up/down, false Hidden and Ready. Cancel/mouse/confirm/held-button paths separately test input type, ready stage, party limit and DLC, then toggle local ready state or show the exact warning popup. Audio progress callbacks stop/start the fill sound; success plays done. Button-label callbacks intentionally return false for mouse bindings even when setting labels. The class clips/reset/close are exact owned presentation bodies; ready transport and actual match start remain native/service gaps.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/bfb23bbefa1a3e3f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/bfb23bbefa1a3e3f.json) at JSON pointer `/claims/9`.

  Archived evidence ID: `archived-record-00351` at JSON pointer ``; file SHA-256 `59114a5dd692ba0333ba3376174a7af7608f44370c81b9c41974ef8b348758d2`.

- `hmh07-lua-follow8:003` (original lines 8-8, 4-12): Assign the supplied widget type to the receiver field, then request receiver:clearLayout(). The source setter does not call the widget constructor.

  unknowns: &#91;"Exact selected recovered Lua source only, conditional module/caller bindings. Original loader/global overwrite/VM/native/DDL/settings/assets/service/server/PS4 behavior remain unverified. No independent review, acceptance, function completion or runtime credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/bfb23bbefa1a3e3f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/bfb23bbefa1a3e3f.json) at JSON pointer `/claims/10`.

  Archived evidence ID: `archived-record-00045` at JSON pointer `/units/2`; file SHA-256 `0c981d5eb446fe3dd44845673b101548cf36172da6abd92475497ba0faf30ce0`; selected record SHA-256 `3843c6aed3c88d59e0c2b91a3eb9d0e61ecd93d8a7660df06791bae7e79e7153`.

- `hmh07-lua-follow1:008` (original lines 18-18, 25-25, 34-34, 45-45, 55-55, 65-65, 84-84, 130-130, 142-142, 20-20, 28-28, 49-49, 58-58, 68-68, 76-76, 87-87, 108-108, 120-120, 146-146, 18-18, 25-25, 34-34, 45-45, 55-55, 65-65, 84-84, 130-130, 142-142, 18-18, 11-164, 25-25, 11-164, 34-34, 11-164, 45-45, 11-164, 55-55, 11-164, 65-65, 11-164, 84-84, 11-164, 130-130, 11-164, 142-142, 11-164, 20-20, 28-28, 49-49, 58-58, 68-68, 76-76, 87-87, 108-108, 120-120, 146-146, 20-20, 11-164, 28-28, 11-164, 49-49, 11-164, 58-58, 11-164, 68-68, 11-164, 76-76, 11-164, 87-87, 11-164, 108-108, 11-164, 120-120, 11-164, 146-146, 11-164): UIImage.new forwards all eight layout arguments to UIElement.new, sets UIImage class, calls setupUIImage and returns self. GetCachedMaterial indexes Materials by requested key; only a nil cache entry calls RegisterMaterial and writes its return to the cache, then returns the cached value. False is a cache hit; a nil RegisterMaterial result can be retried next call. No image/native/material ownership or original runtime contract is supplied.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/bfb23bbefa1a3e3f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/bfb23bbefa1a3e3f.json) at JSON pointer `/claims/11`.

  Archived evidence ID: `archived-record-00036` at JSON pointer `/units/7`; file SHA-256 `279ba12c6a1d4cfd1fb6c7e030a47694d4ee3982256bb21a0b3aa6909aef143b`; selected record SHA-256 `7329bd99e083ca457a54272bf2df1457c445a3fb2e8a07aa636d127734ffcbbf`.

- `hmh07-lua-follow1:125` (original lines 12-12, 12-12, 11-164, 166-166, 166-199, 11-164, 201-201, 203-206, 11-164, 201-201, 207-257, 11-164, 201-201, 258-366, 11-164, 201-201, 367-465, 11-164, 201-201, 468-488, 11-164, 201-201, 489-515, 11-164, 201-201, 516-566, 11-164, 201-201, 567-607, 11-164, 201-201, 610-623, 11-164, 201-201, 626-642, 11-164, 201-201, 643-665, 11-164, 201-201, 666-712, 11-164, 201-201, 713-749, 11-164, 201-201, 752-771, 11-164, 201-201, 772-794, 11-164, 201-201, 795-841, 11-164, 201-201, 842-878, 11-164, 881-881, 881-885): UIElement.new tries ConstructLUIElement with eight supplied layout arguments when the first is truthy, then sets initial class and returns only on a truthy constructed value. Otherwise it calls ConstructLUIElement with m_defaultAnimationState and falls through without an explicit return or setInitialClass in this recovered text. Preserve that fidelity defect. createFake returns a fresh empty table with fakeElemMetaTable; fake operations and native construction remain separate contracts.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/bfb23bbefa1a3e3f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/bfb23bbefa1a3e3f.json) at JSON pointer `/claims/12`.

  Archived evidence ID: `archived-record-00047` at JSON pointer ``; file SHA-256 `0a2ed5281f322b9558d79fcfa95c412c52c1a5b3106117496e96cceee9304688`.

- `hmh07-lua-follow1:167` (original lines 93-93, 104-104, 115-115, 93-93, 104-104, 115-115, 11-164, 166-166, 166-199, 11-164, 201-201, 203-206, 11-164, 201-201, 207-257, 11-164, 201-201, 258-366, 11-164, 201-201, 367-465, 11-164, 201-201, 468-488, 11-164, 201-201, 489-515, 11-164, 201-201, 516-566, 11-164, 201-201, 567-607, 11-164, 201-201, 610-623, 11-164, 201-201, 626-642, 11-164, 201-201, 643-665, 11-164, 201-201, 666-712, 11-164, 201-201, 713-749, 11-164, 201-201, 752-771, 11-164, 201-201, 772-794, 11-164, 201-201, 795-841, 11-164, 201-201, 842-878, 11-164, 881-881, 881-885): UIText.new passes the eight supplied layout arguments to UIElement.new, sets UIText class, calls setupUIText and returns the resulting receiver. It has no explicit nil guard or rollback if base/native setup fails. Reuse the separate UIElement constructor contract including its recovered fallthrough defect; no working retail text object is proved.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/bfb23bbefa1a3e3f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/bfb23bbefa1a3e3f.json) at JSON pointer `/claims/13`.

  Archived evidence ID: `archived-record-00089` at JSON pointer ``; file SHA-256 `bc1ff14cac27ee3b461ef85a9adbe0f0a3b83007a9a3a7b175927aac3abe67a4`.

- `hmh07-lua:095` (original lines 153-153, 153-153): Reads element.parent; returns its __hasChildFocus when parent is nonnil, otherwise false. A present parent with missing flag can return nil; no normalization or parent search occurs.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/bfb23bbefa1a3e3f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/bfb23bbefa1a3e3f.json) at JSON pointer `/claims/14`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/94`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `504d3e4f193e7a29cbebe8d9d98952250d737bf9d9293417fbf121b7ca8e1d18`.
