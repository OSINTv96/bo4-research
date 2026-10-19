# ui/uieditor/widgets/director/directorplaylistoptioninternal.lua

Project-added notes. See the [code](../../src/ui/uieditor/widgets/director/directorplaylistoptioninternal.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `052ced432d93fd03b40d341456e36007d13fbf15570b73df8fad90e9672648e4`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/b5be58c2be6c9ac8.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua:008` (original lines 46-46, 46-46): Constructs NoiseBacking and a tiled shader image, applies fixed visual properties, optionally invokes PostLoadFunc, and returns self. There are no local model/event/state predicates or explicit close hooks in the selected body. Shared callers can change its material, alpha and color after construction; those caller writes are not an invocation of a hidden gameplay routine.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b5be58c2be6c9ac8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b5be58c2be6c9ac8.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/7`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `0716f0c96bec29734ad290ec1c979c5919490d10598fa80ec8ea027994d843c4`.

- `hmh07-lua:052` (original lines 228-228): Queries HasDoubleLootXP first; only a falsey result falls back to hasTierBoost on the supplied element. Returns the resulting value, potentially nil. No tier grant/persistence action is implemented here.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b5be58c2be6c9ac8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b5be58c2be6c9ac8.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/51`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `3fd081720974381c5b22b3cd66d10e20d64144415bb4beedef6009ca8d2c3d72`.

- `hmh07-lua:042` (original lines 230-230, 231-231, 248-248, 254-254): Builds the heal ability icon/meter/empty indicator and controller-dependent prompts. Model count/state/powerRatio choose Hidden, InUse, empty charging, charging or PowerBased; Deployed is explicitly false. Preference and visibility bits gate prompts; ordinary keyboard variants are false while WZ keyboard variant is enabled. Health stack count binds HUDItems separately. SetState/ammo updates may play Pulse, id changes may FadeIn when cycling inventory. Close is registered before tail PreLoadFunc and empty-health-flash property; PC hides the non-PC hold string. Original prompt alpha helper and unfrozen class bodies stay explicit source/native boundaries.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used.", "Source-ready close body exists outside frozen allowed companion range; exact locator is retained in new_dependencies. Other class clip bodies not frozen were not authored.", "Additional same-class reset/clip/close body ranges are available but outside the frozen author scope; exact locators are in unfrozen_same_class_body_locators and source-frontier.json. No body authoring or completion credit for them."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/b5be58c2be6c9ac8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b5be58c2be6c9ac8.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00246` at JSON pointer ``; file SHA-256 `37135b040b8cf189a40cac9d5604e099f11e3e5c7108858144ef67a45d44c75f`.

- `hmh07-lua:215` (original lines 113-113, 109-117): Returns Engine.toupper(Engine localization(arg0)); the nested localization finishes before uppercasing. Used for labels and model-driven text in the cited common menus. No validation or nil fallback; no subscription, persistence or cleanup.

  unknowns: &#91;"Original Lua-to-PS4 CUSA11100 build binding and bytecode/VM/decompiler fidelity unverified.", "Effective HMH settings, enum values, model/data production, LUI state arbitration, event delivery/ordering/cancellation, assets, storage/DDL, networking/service behavior remain explicit gaps where called.", "External helper bodies not selected here are dependencies only; no nil/error recovery assumed beyond visible source. Named LUI override APIs are preserved; no original/new callback ordering is guaranteed without their source contract.", "No independent correctness review, retail execution or function completion credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b5be58c2be6c9ac8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b5be58c2be6c9ac8.json) at JSON pointer `/claims/3`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/214`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `021dadb9180d2be8bae3648293f913e9c483952d2fe58405e2eb68f4dd74bdc2`.

- `hmh07-lua:051` (original lines 228-228): Queries MainModeHasDoubleWeaponXP with optional element mode/playlist; only a falsey result falls back to the element hasDoubleWeaponXP model. Returns that value with possible nil when no element. Main-mode reward backend remains outside this callable.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b5be58c2be6c9ac8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b5be58c2be6c9ac8.json) at JSON pointer `/claims/4`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/50`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `9bb753d7ae2fc71db95661caa0ccb1801adfbafc574dcf8b5fb58fe4a01bcc5c`.

- `hmh07-lua-follow1:222` (original lines 313-789, 313-789, 13-13, 13-13, 315-321, 315-315, 322-337, 322-322, 338-381, 338-338, 341-346, 341-341, 351-356, 351-351, 361-366, 361-361, 371-376, 371-371, 382-425, 382-382, 385-390, 385-385, 395-400, 395-395, 405-410, 405-405, 415-420, 415-415, 428-448, 428-428, 449-472, 449-449, 473-510, 473-473, 481-486, 481-481, 500-505, 500-500, 511-548, 511-511, 519-524, 519-519, 538-543, 538-538, 551-569, 551-551, 572-592, 572-572, 593-616, 593-593, 617-647, 617-617, 625-630, 625-625, 648-678, 648-648, 656-661, 656-656, 681-701, 681-681, 702-725, 702-702, 726-756, 726-726, 734-739, 734-734, 757-787, 757-757, 765-770, 765-765, 313-789, 11-285, 287-287, 287-311, 11-285, 313-313, 315-321, 11-285, 313-313, 322-337, 11-285, 313-313, 338-381, 11-285, 313-313, 382-425, 11-285, 313-313, 428-448, 11-285, 313-313, 449-472, 11-285, 313-313, 473-510, 11-285, 313-313, 511-548, 11-285, 313-313, 551-569, 11-285, 313-313, 572-592, 11-285, 313-313, 593-616, 11-285, 313-313, 617-647, 11-285, 313-313, 648-678, 11-285, 313-313, 681-701, 11-285, 313-313, 702-725, 11-285, 313-313, 726-756, 11-285, 313-313, 757-787, 11-285, 790-790, 790-801, 433-433, 454-454, 478-478, 516-516, 577-577, 598-598, 622-622, 653-653, 686-686, 707-707, 731-731, 762-762, 313-789): Adds playlist-option presentation for default, Locked, Disabled, Upsell and Download states, including each listed child-focus gain/loss transition. Reset precedes exact lock/text/backing/icon/animation changes and independent completion handlers. Reuse constructor244 entitlement/state predicates and data. Table slots do not prove download, purchase, entitlement or HMH-visible use.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b5be58c2be6c9ac8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b5be58c2be6c9ac8.json) at JSON pointer `/claims/5`.

  Archived evidence ID: `archived-record-00746` at JSON pointer ``; file SHA-256 `63bd7f67b66f4d35c7e943f6abceaa53032f9f297a415ee9c902054dd6054436`; selected record SHA-256 `7b47a3dd2dae32dc246f62499894dfb9b9ba874bf92585b96c4492cb49f88aac`.

- `hmh07-lua:023` (original lines 228-228): Binds item image/description/name from DirectorZMLoadoutPreview. Restriction icon/text can become visible only outside director pregame and public WZ lobby, and when the restricted model flag is true. Thus this restriction-display path is source-excluded under IsPublicWZLobby, despite common construction. Whole widget Invisible follows info-shown false; TraditionalChinesePC has a distinct predicate/clip. No ZM loadout gameplay semantics are inferred.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b5be58c2be6c9ac8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b5be58c2be6c9ac8.json) at JSON pointer `/claims/6`.

  Archived evidence ID: `archived-record-00241` at JSON pointer ``; file SHA-256 `28e89d13900cc7ee88f2917181aa43d70f21a8e5fc9531e78172e97e94129572`.

- `hmh07-lua:217` (original lines 193-193, 189-197): Returns Engine.toupper(arg0), without localization or a nil check. Cited model callbacks invoke it when text changes; callback ownership remains with each caller. No local state or cleanup.

  unknowns: &#91;"Original Lua-to-PS4 CUSA11100 build binding and bytecode/VM/decompiler fidelity unverified.", "Effective HMH settings, enum values, model/data production, LUI state arbitration, event delivery/ordering/cancellation, assets, storage/DDL, networking/service behavior remain explicit gaps where called.", "External helper bodies not selected here are dependencies only; no nil/error recovery assumed beyond visible source. Named LUI override APIs are preserved; no original/new callback ordering is guaranteed without their source contract.", "No independent correctness review, retail execution or function completion credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b5be58c2be6c9ac8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b5be58c2be6c9ac8.json) at JSON pointer `/claims/7`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/216`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `2b2815ce109f8f160c9613b489d52f540e21c786bb3e72ab9d8c56529a053a7e`.

- `hmh07-lua:193` (original lines 8-8, 4-12): InheritFrom is executed at the cited class assignments, not merely imported. Missing/falsy base throws explicit LUI Error. Otherwise makes a new table with super=base, sets its metatable __index=base, creates a fresh m_eventHandlers table with __index=base.m_eventHandlers, then returns the new class. It shares fallback handlers while permitting per-class handler writes. Does not instantiate widgets, invoke inherited callbacks or close anything. Metatable/native VM behavior and base fields are assumed, no further validation.

  unknowns: &#91;"Original Lua-to-PS4 CUSA11100 build binding and bytecode/VM/decompiler fidelity unverified.", "Effective HMH settings, enum values, model/data production, LUI state arbitration, event delivery/ordering/cancellation, assets, storage/DDL, networking/service behavior remain explicit gaps where called.", "External helper bodies not selected here are dependencies only; no nil/error recovery assumed beyond visible source. Named LUI override APIs are preserved; no original/new callback ordering is guaranteed without their source contract.", "No independent correctness review, retail execution or function completion credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b5be58c2be6c9ac8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b5be58c2be6c9ac8.json) at JSON pointer `/claims/8`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/192`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `28096b9a20c988def77f03e8d965db4759673d7a552db8efd9d89c53725de88c`.

- `hmh07-lua:048` (original lines 228-228): Calls MainModeHasDoubleXP with optional element mode/playlist, then only if falsey consults the element hasDoubleXP model. Returns the resulting value, including a possible nil when no element exists. The unassigned MainMode helper is a source-ready dependency, not reauthored.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b5be58c2be6c9ac8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b5be58c2be6c9ac8.json) at JSON pointer `/claims/9`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/47`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `2d11ea2b6c89f98d4e9921ecfba25ffa668c5e0ad618d13c8fbfa621d7d7c22e`.

- `hmh07-lua-follow1:146` (original lines 278-278, 278-278, 11-285, 287-287, 287-311, 11-285, 313-313, 315-321, 11-285, 313-313, 322-337, 11-285, 313-313, 338-381, 11-285, 313-313, 382-425, 11-285, 313-313, 428-448, 11-285, 313-313, 449-472, 11-285, 313-313, 473-510, 11-285, 313-313, 511-548, 11-285, 313-313, 551-569, 11-285, 313-313, 572-592, 11-285, 313-313, 593-616, 11-285, 313-313, 617-647, 11-285, 313-313, 648-678, 11-285, 313-313, 681-701, 11-285, 313-313, 702-725, 11-285, 313-313, 726-756, 11-285, 313-313, 757-787, 11-285, 790-790, 790-801): CallOriginalFirst appends the supplied callback to the table returned by OverrideFunction_GetFunctionTable. CallOriginalSecond inserts its callback at index1. Neither wrapper directly calls the original or callback or returns a value. The naming does not prove runtime order independently of the dispatcher, which remains a reusable available dependency.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b5be58c2be6c9ac8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b5be58c2be6c9ac8.json) at JSON pointer `/claims/10`.

  Archived evidence ID: `archived-record-00044` at JSON pointer ``; file SHA-256 `46ecb6cfe8fa919ec918f489610848dcd8b393e632706abbfd898ba7b2a05c62`.

- `hmh07-lua:213` (original lines 146-146, 142-150): Passes format/key arg0 and substitution arg1 directly to Engine hash_4F9F1239CFD921FE and returns its result. The exact cited caller subscribes PercentInstalled to LobbyRoot.percentInstalled; a delivered nonnil value is supplied to LocalizeIntoString with hash_40643A70B24A36F6 and its result to PercentInstalled:setText. The wrapper has no model mutation, callback, local guard or cleanup. Native localization/model/text behavior and callback delivery remain external; there is no local error recovery.

  unknowns: &#91;"Original Lua-to-PS4 CUSA11100 build binding and bytecode/VM/decompiler fidelity unverified.", "Effective HMH settings, enum values, model/data production, LUI state arbitration, event delivery/ordering/cancellation, assets, storage/DDL, networking/service behavior remain explicit gaps where called.", "External helper bodies not selected here are dependencies only; no nil/error recovery assumed beyond visible source. Named LUI override APIs are preserved; no original/new callback ordering is guaranteed without their source contract.", "No independent correctness review, retail execution or function completion credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b5be58c2be6c9ac8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b5be58c2be6c9ac8.json) at JSON pointer `/claims/11`.

  Archived evidence ID: `archived-record-00549` at JSON pointer ``; file SHA-256 `a19f9695f1df35ab47974c5a72095b8e417c1ba35ca5c8215aaf16f19a3d44e3`.

- `hmh07-lua:244` (original lines 11-285, 29-29, 38-38, 48-48, 54-54, 64-64, 67-67, 77-77, 78-78, 89-89, 94-94, 103-103, 112-112, 113-113, 123-123, 128-128, 131-131, 139-139, 143-143, 146-146, 153-153, 163-163, 164-164, 174-174, 175-175, 190-190, 193-193, 200-200, 206-206, 207-207, 215-215, 258-258, 267-267, 278-278, 299-299, 302-302, 308-308, 309-309, 310-310, 326-326, 342-342, 343-343, 344-344, 345-345, 349-349, 352-352, 354-354, 355-355, 362-362, 364-364, 365-365, 372-372, 374-374, 375-375, 386-386, 387-387, 388-388, 389-389, 393-393, 396-396, 398-398, 399-399, 406-406, 408-408, 409-409, 416-416, 418-418, 419-419, 446-446, 458-458, 470-470, 482-482, 483-483, 484-484, 485-485, 489-489, 501-501, 502-502, 503-503, 504-504, 508-508, 520-520, 521-521, 522-522, 523-523, 527-527, 539-539, 540-540, 541-541, 542-542, 546-546, 555-555, 590-590, 602-602, 614-614, 626-626, 627-627, 628-628, 629-629, 633-633, 645-645, 657-657, 658-658, 659-659, 660-660, 664-664, 676-676, 699-699, 711-711, 723-723, 735-735, 736-736, 737-737, 738-738, 742-742, 754-754, 766-766, 767-767, 768-768, 769-769, 773-773, 785-785, 791-791, 792-792, 793-793, 794-794, 795-795, 796-796, 797-797, 798-798, 799-799, 800-800, 69-69, 80-80, 130-130, 145-145, 155-155, 166-166, 192-192, 226-226, 229-229, 230-230, 236-236, 240-240, 242-242, 246-246, 248-248, 252-252, 254-254, 280-280, 284-284, 11-285, 287-287, 287-311, 11-285, 313-313, 315-321, 11-285, 313-313, 322-337, 11-285, 313-313, 338-381, 11-285, 313-313, 382-425, 11-285, 313-313, 428-448, 11-285, 313-313, 449-472, 11-285, 313-313, 473-510, 11-285, 313-313, 511-548, 11-285, 313-313, 551-569, 11-285, 313-313, 572-592, 11-285, 313-313, 593-616, 11-285, 313-313, 617-647, 11-285, 313-313, 648-678, 11-285, 313-313, 681-701, 11-285, 313-313, 702-725, 11-285, 313-313, 726-756, 11-285, 313-313, 757-787, 11-285, 790-790, 790-801, 242-242, 237-247, 193-193, 188-198, 220-220, 215-225, 46-46, 41-51, 173-173, 168-178, 278-278, 273-283, 12-12, 7-17, 22-22, 17-27, 31-31, 26-36, 40-40, 35-45, 56-56, 51-61, 65-65, 60-70, 95-95, 90-100, 105-105, 100-110, 125-125, 120-130, 183-183, 178-188, 304-304, 299-309, 433-433, 428-438, 454-454, 449-459, 478-478, 473-483, 516-516, 511-521, 577-577, 572-582, 598-598, 593-603, 622-622, 617-627, 653-653, 648-658, 686-686, 681-691, 707-707, 702-712, 731-731, 726-736, 762-762, 757-767, 20-20, 15-25, 27-27, 22-32, 37-37, 32-42, 53-53, 48-58, 63-63, 58-68, 76-76, 71-81, 87-87, 82-92, 93-93, 88-98, 102-102, 97-107, 152-152, 147-157, 162-162, 157-167, 199-199, 194-204, 214-214, 209-219, 111-111, 106-116, 121-121, 116-126, 137-137, 132-142, 180-180, 175-185, 205-205, 200-210, 146-146, 141-151, 113-113, 108-118, 281-281, 276-286, 30-30, 25-35, 39-39, 34-44, 55-55, 50-60, 70-70, 65-75, 81-81, 76-86, 104-104, 99-109, 156-156, 151-161, 167-167, 162-172, 201-201, 196-206, 216-216, 211-221, 193-193, 188-198, 313-313, 313-789, 13-13, 11-285, 11-285): PlaylistOption outer wrapper directly calls this constructor. Binds iconBackground/iconBackgroundFocus/icon to registered images, descriptionText to text, name through LocalizeIfXHash+ToUpper, and percentInstalled to exact localized format. Forwards whole model to XP child. Locked requires locked=true but excludes lockState pls_required_dlc_not_available and opaque hash_4BDEB566326AC98. Upsell is that opaque lockState; Download is pls_required_dlc_not_available; Disabled defaults AlwaysFalse. locked/lockState links reevaluate. Source-linked reset and focus/lock/upsell/download clips alter art/text/alpha with scheduled keyframes and interruption handlers, but no purchase/download/action call is installed here. Qualified __onClose closes constructed child widgets through CallOriginalSecond. Optional postload then self return. Actual lock enum/data, platform assets and animation completion remain unknown.

  unknowns: &#91;"Original Lua-to-PS4 CUSA11100 build binding and bytecode/VM/decompiler fidelity unverified.", "Effective HMH settings, enum values, model/data production, LUI state arbitration, event delivery/ordering/cancellation, assets, storage/DDL, networking/service behavior remain explicit gaps where called.", "External helper bodies not selected here are dependencies only; no nil/error recovery assumed beyond visible source. Named LUI override APIs are preserved; no original/new callback ordering is guaranteed without their source contract.", "No independent correctness review, retail execution or function completion credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b5be58c2be6c9ac8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b5be58c2be6c9ac8.json) at JSON pointer `/claims/12`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/243`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `2e660bda765e8c6c327fdcc1f6d2429e6b148f29c9ae75ce4707d5cf4434393f`.

- `hmh07-lua-follow8:003` (original lines 8-8, 4-12): Assign the supplied widget type to the receiver field, then request receiver:clearLayout(). The source setter does not call the widget constructor.

  unknowns: &#91;"Exact selected recovered Lua source only, conditional module/caller bindings. Original loader/global overwrite/VM/native/DDL/settings/assets/service/server/PS4 behavior remain unverified. No independent review, acceptance, function completion or runtime credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b5be58c2be6c9ac8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b5be58c2be6c9ac8.json) at JSON pointer `/claims/13`.

  Archived evidence ID: `archived-record-00045` at JSON pointer `/units/2`; file SHA-256 `0c981d5eb446fe3dd44845673b101548cf36172da6abd92475497ba0faf30ce0`; selected record SHA-256 `3843c6aed3c88d59e0c2b91a3eb9d0e61ecd93d8a7660df06791bae7e79e7153`.

- `hmh07-lua:183` (original lines 173-173, 169-177): The saved playlist-option constructor requests this horizontal-list child173 and registers linkToElementModel174-176; only on callback delivery does its body request DoubleXPCardIconsLeftAligned:setModel(model,f1_arg1) using the delivered model argument. The child constructor separately registers linkToElementModel19-21 on DoubleXPCardIconsInternal with self; only on that callback delivery does its body request DoubleXPCardIconsInternal:setModel(model,f1_arg1). These registrations do not establish delivery or equality of their delivered arguments. The child constructor registers the Visible condition whose body returns AlwaysTrue(); external parent visibility remains unknown. The separately linked reset/default/visible clip bodies request the written child alpha values when invoked. Constructor33 requests the CallOriginalSecond close registration; the saved wrapper208-210 inserts the supplied function into its function table. Separately, __onClose67-69 requests the child close method when invoked; registration does not prove invocation or lifetime ordering. Constructor34-38 calls truthy PostLoadFunc and returns self if preceding requests return normally. Bonus data, provider/native effects, callback delivery, original build/VM and runtime behavior remain unresolved.

  unknowns: &#91;"Original Lua-to-PS4 CUSA11100 build binding and bytecode/VM/decompiler fidelity unverified.", "Effective HMH settings, enum values, model/data production, LUI state arbitration, event delivery/ordering/cancellation, assets, storage/DDL, networking/service behavior remain explicit gaps where called.", "External helper bodies not selected here are dependencies only; no nil/error recovery assumed beyond visible source. Named LUI override APIs are preserved; no original/new callback ordering is guaranteed without their source contract.", "No independent correctness review, retail execution or function completion credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b5be58c2be6c9ac8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b5be58c2be6c9ac8.json) at JSON pointer `/claims/14`.

  Archived evidence ID: `archived-record-00594` at JSON pointer ``; file SHA-256 `28fdf6bcbec14ec2bb4ca0d580f7b80a823632c7c06b04bf4347144a2cb9e52f`.

- `hmh07-lua-follow1:008` (original lines 20-20, 27-27, 37-37, 53-53, 63-63, 76-76, 87-87, 93-93, 102-102, 152-152, 162-162, 199-199, 214-214, 22-22, 31-31, 40-40, 56-56, 65-65, 95-95, 105-105, 125-125, 183-183, 304-304, 433-433, 454-454, 478-478, 516-516, 577-577, 598-598, 622-622, 653-653, 686-686, 707-707, 731-731, 762-762, 20-20, 27-27, 37-37, 53-53, 63-63, 76-76, 87-87, 93-93, 102-102, 152-152, 162-162, 199-199, 214-214, 20-20, 11-285, 27-27, 11-285, 37-37, 11-285, 53-53, 11-285, 63-63, 11-285, 76-76, 11-285, 87-87, 11-285, 93-93, 11-285, 102-102, 11-285, 152-152, 11-285, 162-162, 11-285, 199-199, 11-285, 214-214, 11-285, 22-22, 31-31, 40-40, 56-56, 65-65, 95-95, 105-105, 125-125, 183-183, 304-304, 433-433, 454-454, 478-478, 516-516, 577-577, 598-598, 622-622, 653-653, 686-686, 707-707, 731-731, 762-762, 22-22, 11-285, 31-31, 11-285, 40-40, 11-285, 56-56, 11-285, 65-65, 11-285, 95-95, 11-285, 105-105, 11-285, 125-125, 11-285, 183-183, 11-285, 304-304, 301-307, 433-433, 430-436, 454-454, 451-457, 478-478, 475-481, 516-516, 513-519, 577-577, 574-580, 598-598, 595-601, 622-622, 619-625, 653-653, 650-656, 686-686, 683-689, 707-707, 704-710, 731-731, 728-734, 762-762, 759-765): UIImage.new forwards all eight layout arguments to UIElement.new, sets UIImage class, calls setupUIImage and returns self. GetCachedMaterial indexes Materials by requested key; only a nil cache entry calls RegisterMaterial and writes its return to the cache, then returns the cached value. False is a cache hit; a nil RegisterMaterial result can be retried next call. No image/native/material ownership or original runtime contract is supplied.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b5be58c2be6c9ac8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b5be58c2be6c9ac8.json) at JSON pointer `/claims/15`.

  Archived evidence ID: `archived-record-00036` at JSON pointer `/units/7`; file SHA-256 `279ba12c6a1d4cfd1fb6c7e030a47694d4ee3982256bb21a0b3aa6909aef143b`; selected record SHA-256 `7329bd99e083ca457a54272bf2df1457c445a3fb2e8a07aa636d127734ffcbbf`.

- `hmh07-lua-follow1:125` (original lines 12-12, 12-12, 11-285, 287-287, 287-311, 11-285, 313-313, 315-321, 11-285, 313-313, 322-337, 11-285, 313-313, 338-381, 11-285, 313-313, 382-425, 11-285, 313-313, 428-448, 11-285, 313-313, 449-472, 11-285, 313-313, 473-510, 11-285, 313-313, 511-548, 11-285, 313-313, 551-569, 11-285, 313-313, 572-592, 11-285, 313-313, 593-616, 11-285, 313-313, 617-647, 11-285, 313-313, 648-678, 11-285, 313-313, 681-701, 11-285, 313-313, 702-725, 11-285, 313-313, 726-756, 11-285, 313-313, 757-787, 11-285, 790-790, 790-801): UIElement.new tries ConstructLUIElement with eight supplied layout arguments when the first is truthy, then sets initial class and returns only on a truthy constructed value. Otherwise it calls ConstructLUIElement with m_defaultAnimationState and falls through without an explicit return or setInitialClass in this recovered text. Preserve that fidelity defect. createFake returns a fresh empty table with fakeElemMetaTable; fake operations and native construction remain separate contracts.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b5be58c2be6c9ac8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b5be58c2be6c9ac8.json) at JSON pointer `/claims/16`.

  Archived evidence ID: `archived-record-00047` at JSON pointer ``; file SHA-256 `0a2ed5281f322b9558d79fcfa95c412c52c1a5b3106117496e96cceee9304688`.

- `hmh07-lua:018` (original lines 220-220, 220-220): Builds focus glow/brackets/lines/border and revalidates on lobby navigation. Disabled is always false; ZombiesState uses the selected IsZombies predicate. Frozen class reset/clip bodies define focus transitions and direct property changes, with nested animation completion/interruption callbacks. The source removes DefaultState Active-family clips when not CoD.isPC. Zombies-only presentation cannot be promoted to HMH merely because the same outline is shared.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b5be58c2be6c9ac8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b5be58c2be6c9ac8.json) at JSON pointer `/claims/17`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/17`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `7b4d2c851ccbd6f45d81c1259f788caece2c9fafb8f48c7e06a1f82034d3f7ca`.

- `hmh07-lua:090` (original lines 242-242, 242-242): Returns false unconditionally, providing a source proof that the attached predicate cannot select a state through this condition alone.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b5be58c2be6c9ac8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b5be58c2be6c9ac8.json) at JSON pointer `/claims/18`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/89`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `101ca4cbf310a20bbc095a1688a99133387e50b3bc4f7e558c5c78128289880a`.

- `hmh07-lua-follow1:167` (original lines 111-111, 121-121, 137-137, 180-180, 205-205, 111-111, 121-121, 137-137, 180-180, 205-205, 11-285, 287-287, 287-311, 11-285, 313-313, 315-321, 11-285, 313-313, 322-337, 11-285, 313-313, 338-381, 11-285, 313-313, 382-425, 11-285, 313-313, 428-448, 11-285, 313-313, 449-472, 11-285, 313-313, 473-510, 11-285, 313-313, 511-548, 11-285, 313-313, 551-569, 11-285, 313-313, 572-592, 11-285, 313-313, 593-616, 11-285, 313-313, 617-647, 11-285, 313-313, 648-678, 11-285, 313-313, 681-701, 11-285, 313-313, 702-725, 11-285, 313-313, 726-756, 11-285, 313-313, 757-787, 11-285, 790-790, 790-801): UIText.new passes the eight supplied layout arguments to UIElement.new, sets UIText class, calls setupUIText and returns the resulting receiver. It has no explicit nil guard or rollback if base/native setup fails. Reuse the separate UIElement constructor contract including its recovered fallthrough defect; no working retail text object is proved.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b5be58c2be6c9ac8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b5be58c2be6c9ac8.json) at JSON pointer `/claims/19`.

  Archived evidence ID: `archived-record-00089` at JSON pointer ``; file SHA-256 `bc1ff14cac27ee3b461ef85a9adbe0f0a3b83007a9a3a7b175927aac3abe67a4`.

- `hmh07-lua:256` (original lines 193-193, 189-197): Only type(arg0)==xhash invokes and returns Engine hash_4F9F1239CFD921FE(arg0); all other types return unchanged. Thus strings are not relocalized here. No state or cleanup; native localization fidelity unresolved.

  unknowns: &#91;"Original Lua-to-PS4 CUSA11100 build binding and bytecode/VM/decompiler fidelity unverified.", "Effective HMH settings, enum values, model/data production, LUI state arbitration, event delivery/ordering/cancellation, assets, storage/DDL, networking/service behavior remain explicit gaps where called.", "External helper bodies not selected here are dependencies only; no nil/error recovery assumed beyond visible source. Named LUI override APIs are preserved; no original/new callback ordering is guaranteed without their source contract.", "No independent correctness review, retail execution or function completion credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b5be58c2be6c9ac8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b5be58c2be6c9ac8.json) at JSON pointer `/claims/20`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/255`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `24a6ef3cdcb79742c74ea30b6f9553b959b3fba616f7d6e96a1c422ecaa906a2`.
