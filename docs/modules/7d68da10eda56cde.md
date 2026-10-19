# ui/uieditor/widgets/common/common_tabbar_center.lua

Project-added notes. See the [code](../../src/ui/uieditor/widgets/common/common_tabbar_center.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `dacf6c58c44016878d126db52e667667531975f15b7599f51b47a4eb7c8c3abb`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/7d68da10eda56cde.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua-follow1:188` (original lines 13-13, 13-13): UIHorizontalList.new forwards eight layout arguments to UIElement.new, sets supplied spacing, ID and native resizing behavior, installs spacer/add/remove helpers and stores __ignoreFirstElement from argument9, then returns self. This selected body does not explicitly call setClass. Preserve that source difference and the base constructor's recovered failure/fallthrough behavior.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7d68da10eda56cde-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7d68da10eda56cde.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00036` at JSON pointer `/units/187`; file SHA-256 `279ba12c6a1d4cfd1fb6c7e030a47694d4ee3982256bb21a0b3aa6909aef143b`; selected record SHA-256 `bf0586d95c2e393a455519923ecbd52c4b9e93e079613a93ece235c4ffc8d301`.

- `hmh07-lua:265` (original lines 90-90, 86-94): Ignores arg0; reads global CommonCurrentActiveTabIndex and arg1.grid.itemCount. Returns true only when itemCount>1 AND current index==itemCount. A one-tab row is false even at its last index. No model/grid nil guard, mutation or cleanup.

  unknowns: &#91;"Original Lua-to-PS4 CUSA11100 build binding and bytecode/VM/decompiler fidelity unverified.", "Effective HMH settings, enum values, model/data production, LUI state arbitration, event delivery/ordering/cancellation, assets, storage/DDL, networking/service behavior remain explicit gaps where called.", "External helper bodies not selected here are dependencies only; no nil/error recovery assumed beyond visible source. Named LUI override APIs are preserved; no original/new callback ordering is guaranteed without their source contract.", "No independent correctness review, retail execution or function completion credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7d68da10eda56cde-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7d68da10eda56cde.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/264`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `7b592ecbe721b844387bce283455be611c440d90e371775ff58b0585098b0c37`.

- `hmh07-lua:252` (original lines 15-15, 11-19): Creates a global model at path arg0 then sets its value to arg1. Does not return a handle. Existing-path behavior belongs to Engine.createmodel. No callback, persistence guarantee or cleanup.

  unknowns: &#91;"Original Lua-to-PS4 CUSA11100 build binding and bytecode/VM/decompiler fidelity unverified.", "Effective HMH settings, enum values, model/data production, LUI state arbitration, event delivery/ordering/cancellation, assets, storage/DDL, networking/service behavior remain explicit gaps where called.", "External helper bodies not selected here are dependencies only; no nil/error recovery assumed beyond visible source. Named LUI override APIs are preserved; no original/new callback ordering is guaranteed without their source contract.", "No independent correctness review, retail execution or function completion credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7d68da10eda56cde-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7d68da10eda56cde.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/251`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `2ab6847f4fee7672497d9656695863a5c38f4e2ab4dda647c2b80534f3400fe6`.

- `hmh07-lua:250` (original lines 73-73, 69-77): Common tabbar constructs this wrapper directly. Builds6-column grid of basicTabWidget. gain_focus calls own/super gainFocus then refreshes confirm state, returning that handler result. Confirm calls SelectItemIfPossible then list_right sound and returns true; label sets hash_0 but returns false. After original grid setWidth, wrapper scales to child width. PositionDraft.stage notification refreshes datasource only when controller model compares equal to5; this is a conditional common UI callback, not authority to reconstruct draft gameplay. Registers CallOriginalSecond close to qualified __onClose(grid close); optional postload then AddBumperNavigation(menu,grid,controller), returns self. Original input/datasource/callback cancellation remain external.

  unknowns: &#91;"Original Lua-to-PS4 CUSA11100 build binding and bytecode/VM/decompiler fidelity unverified.", "Effective HMH settings, enum values, model/data production, LUI state arbitration, event delivery/ordering/cancellation, assets, storage/DDL, networking/service behavior remain explicit gaps where called.", "External helper bodies not selected here are dependencies only; no nil/error recovery assumed beyond visible source. Named LUI override APIs are preserved; no original/new callback ordering is guaranteed without their source contract.", "No independent correctness review, retail execution or function completion credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7d68da10eda56cde-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7d68da10eda56cde.json) at JSON pointer `/claims/3`.

  Archived evidence ID: `archived-record-00213` at JSON pointer ``; file SHA-256 `fafafd2b2af3c1646d9b8f70e8ca554262dc51de64b5d330bfc9b000d6a718ea`.

- `hmh07-lua:185` (original lines 31-31, 27-35, 85-85, 81-89): Common tabbar constructs both arrow instances directly without a platform if around the shown calls; the PC name alone cannot exclude PS4 construction. Builds Arrow and initially hidden ArrowFocus. Own Disabled predicate is AlwaysFalse; callers merge edge-of-tab Disabled tests (first/last row checks in units264/265), so caller qualification matters. Class clips set normal/focus/disabled alpha and reset before transitions; no button action or explicit close hook here. Optional postload then self return. Input source/platform and native state precedence remain boundaries.

  unknowns: &#91;"Original Lua-to-PS4 CUSA11100 build binding and bytecode/VM/decompiler fidelity unverified.", "Effective HMH settings, enum values, model/data production, LUI state arbitration, event delivery/ordering/cancellation, assets, storage/DDL, networking/service behavior remain explicit gaps where called.", "External helper bodies not selected here are dependencies only; no nil/error recovery assumed beyond visible source. Named LUI override APIs are preserved; no original/new callback ordering is guaranteed without their source contract.", "No independent correctness review, retail execution or function completion credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7d68da10eda56cde-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7d68da10eda56cde.json) at JSON pointer `/claims/4`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/184`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `c048f0f348cd53f36b1cdf4c5196284a40111ac1bc8f2db6fcc1051099c5ade1`.

- `hmh07-lua:193` (original lines 9-9, 5-13): InheritFrom is executed at the cited class assignments, not merely imported. Missing/falsy base throws explicit LUI Error. Otherwise makes a new table with super=base, sets its metatable __index=base, creates a fresh m_eventHandlers table with __index=base.m_eventHandlers, then returns the new class. It shares fallback handlers while permitting per-class handler writes. Does not instantiate widgets, invoke inherited callbacks or close anything. Metatable/native VM behavior and base fields are assumed, no further validation.

  unknowns: &#91;"Original Lua-to-PS4 CUSA11100 build binding and bytecode/VM/decompiler fidelity unverified.", "Effective HMH settings, enum values, model/data production, LUI state arbitration, event delivery/ordering/cancellation, assets, storage/DDL, networking/service behavior remain explicit gaps where called.", "External helper bodies not selected here are dependencies only; no nil/error recovery assumed beyond visible source. Named LUI override APIs are preserved; no original/new callback ordering is guaranteed without their source contract.", "No independent correctness review, retail execution or function completion credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7d68da10eda56cde-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7d68da10eda56cde.json) at JSON pointer `/claims/5`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/192`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `28096b9a20c988def77f03e8d965db4759673d7a552db8efd9d89c53725de88c`.

- `hmh07-lua:161` (original lines 64-64, 119-119, 64-64, 119-119): Calls DoBumperGridButtonAction(menu,controller,"bumpers",direction). It does not return a navigation result. The exact direction value is supplied by the caller.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7d68da10eda56cde-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7d68da10eda56cde.json) at JSON pointer `/claims/6`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/160`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `5fbea76d01ffd9846563935aa95ab0a4ee68b45c84a8013fb85e36a57bcab209`.

- `hmh07-lua:162` (original lines 138-138, 138-138): Returns false outside PC; on PC returns true only for a present grid whose hCount<itemCount. It does not count pages, compare selection or consult gamepad input itself.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7d68da10eda56cde-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7d68da10eda56cde.json) at JSON pointer `/claims/7`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/161`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `5b96e77486f686f8848d4fc7429ab7decc1e71945b159609391a481e1fe6bb3a`.

- `hmh07-lua:115` (original lines 74-74, 74-74): Builds common and ZM tab presentation layers and links every name label to the same model. Breadcrumb child becomes Visible only for breadcrumbCount>0, receives breadcrumb model when nonnil. Unavailable precedes PC/Zombies variants; available and lobby navigation changes revalidate. Frozen reset/clip bodies include focus/active/transition animations; ZM variants retain IsZombies conditions and PC variants retain IsPC. Same class identity is not HMH execution proof.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7d68da10eda56cde-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7d68da10eda56cde.json) at JSON pointer `/claims/8`.

  Archived evidence ID: `archived-record-00304` at JSON pointer ``; file SHA-256 `cf69715b56544b7a638460020f768940256fc3ed17da7a848f5baf663bd6d407`.

- `hmh07-lua-follow2:111` (original lines 60-60, 115-115, 60-60, 12-175, 115-115, 12-175, 67-67, 122-122, 67-67, 12-175, 122-122, 12-175): Reuse both historical exact semantic contracts: IsBitwiseAndNonZero tests bitwise intersection~=0 with original VM width/precedence limits. ClearBit subtracts1<<index only when IsBitSet; empty else falls through nil. Do not add an unchanged-value fallback. This file question has zero new draft credit because both bodies are reused.

  unknowns: &#91;"Exact original PS4/source version matching, recovered Lua/VM fidelity and global/native/LUI provider identity remain unverified.", "Model/storage/DDL/assets/localization/dvar/enum values, callback delivery/cancellation/error behavior, native networking and unavailable service/server code are separate inputs.", "Other-file locals are not providers by spelling. Exact qualified global declarations are source candidates until loader/table identity and caller conditions bind them.", "No implicit nil/type checks, exception recovery, timer/model disposal, idempotence or guarantee that later effects run after an error is added."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7d68da10eda56cde-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7d68da10eda56cde.json) at JSON pointer `/claims/9`.

  Archived evidence ID: `archived-record-00028` at JSON pointer `/units/110`; file SHA-256 `2f4ecc3aabb5072135e148ef5782181882bd3b940908913a20bf258d3754185e`; selected record SHA-256 `4567dbac7e486de026370682511823da51e716f72ad4ef365b647f4796b1fe40`.

- `hmh07-lua:264` (original lines 36-36, 32-40): Ignores arg0; returns global CommonCurrentActiveTabIndex:get()==1. No missing-model guard. Used by left PC tab arrow state; count is not checked. No mutation or cleanup.

  unknowns: &#91;"Original Lua-to-PS4 CUSA11100 build binding and bytecode/VM/decompiler fidelity unverified.", "Effective HMH settings, enum values, model/data production, LUI state arbitration, event delivery/ordering/cancellation, assets, storage/DDL, networking/service behavior remain explicit gaps where called.", "External helper bodies not selected here are dependencies only; no nil/error recovery assumed beyond visible source. Named LUI override APIs are preserved; no original/new callback ordering is guaranteed without their source contract.", "No independent correctness review, retail execution or function completion credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7d68da10eda56cde-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7d68da10eda56cde.json) at JSON pointer `/claims/10`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/263`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `fb097cf0920b345fbb9b0392ce667e8f10d275a68d1779f043a167184c7f29e7`.

- `hmh07-lua-follow1:146` (original lines 169-169, 169-169): CallOriginalFirst appends the supplied callback to the table returned by OverrideFunction_GetFunctionTable. CallOriginalSecond inserts its callback at index1. Neither wrapper directly calls the original or callback or returns a value. The naming does not prove runtime order independently of the dispatcher, which remains a reusable available dependency.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7d68da10eda56cde-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7d68da10eda56cde.json) at JSON pointer `/claims/11`.

  Archived evidence ID: `archived-record-00044` at JSON pointer ``; file SHA-256 `46ecb6cfe8fa919ec918f489610848dcd8b393e632706abbfd898ba7b2a05c62`.

- `hmh07-lua:037` (original lines 138-138): Creates ready/custom-start controls, timer and progress fills. Ordered states cover hide-on-start, countdown, insufficient players, inability to ready up/down, false Hidden and Ready. Cancel/mouse/confirm/held-button paths separately test input type, ready stage, party limit and DLC, then toggle local ready state or show the exact warning popup. Audio progress callbacks stop/start the fill sound; success plays done. Button-label callbacks intentionally return false for mouse bindings even when setting labels. The class clips/reset/close are exact owned presentation bodies; ready transport and actual match start remain native/service gaps.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7d68da10eda56cde-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7d68da10eda56cde.json) at JSON pointer `/claims/12`.

  Archived evidence ID: `archived-record-00351` at JSON pointer ``; file SHA-256 `59114a5dd692ba0333ba3376174a7af7608f44370c81b9c41974ef8b348758d2`.

- `hmh07-lua-follow8:003` (original lines 9-9, 5-13): Assign the supplied widget type to the receiver field, then request receiver:clearLayout(). The source setter does not call the widget constructor.

  unknowns: &#91;"Exact selected recovered Lua source only, conditional module/caller bindings. Original loader/global overwrite/VM/native/DDL/settings/assets/service/server/PS4 behavior remain unverified. No independent review, acceptance, function completion or runtime credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7d68da10eda56cde-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7d68da10eda56cde.json) at JSON pointer `/claims/13`.

  Archived evidence ID: `archived-record-00045` at JSON pointer `/units/2`; file SHA-256 `0c981d5eb446fe3dd44845673b101548cf36172da6abd92475497ba0faf30ce0`; selected record SHA-256 `3843c6aed3c88d59e0c2b91a3eb9d0e61ecd93d8a7660df06791bae7e79e7153`.

- `hmh07-lua-follow1:084` (original lines 60-60, 115-115, 67-67, 122-122, 60-60, 115-115, 60-60, 12-175, 115-115, 12-175, 67-67, 122-122, 67-67, 12-175, 122-122, 12-175): NewFromState errors for nil menu name, creates UIElement, optionally captures DEV model count and binds ModelToUse, applies overwrite name, initializes callback/pending lists, registers opened/menu name and cursor snapping; missing controller falls back to primary, cursor support adds focus-paths/subscription. NewForUIEditor creates button prompts and PC/shoutcaster key prompts, returns menu. DebugClose invokes close. UpdateButtonShownState scans condition-function rows, enables at first truthy result, otherwise preserves menu/element disabled states, then disables enabled prompt for animated occluder and writes final state. SetButtonLabel updates existing label/flags, handles one overlay-label hash, clears contextual flag outside free cursor, updates PC key flags after stripping two bits and refreshes cursor prompts. GetNavigationForMenu scans navigation groups/entries backward, returns first matching pair, otherwise no values. No callback registration alone proves button delivery; nil/native/lifetime limits are literal.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7d68da10eda56cde-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7d68da10eda56cde.json) at JSON pointer `/claims/14`.

  Archived evidence ID: `archived-record-00036` at JSON pointer `/units/83`; file SHA-256 `279ba12c6a1d4cfd1fb6c7e030a47694d4ee3982256bb21a0b3aa6909aef143b`; selected record SHA-256 `f166f3d0ac206847a0ec4bbc3c4cb28fe076b4dd678e2d9838838f5e65337d0e`.

- `hmh07-lua:090` (original lines 132-132, 132-132): Returns false unconditionally, providing a source proof that the attached predicate cannot select a state through this condition alone.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7d68da10eda56cde-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7d68da10eda56cde.json) at JSON pointer `/claims/15`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/89`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `101ca4cbf310a20bbc095a1688a99133387e50b3bc4f7e558c5c78128289880a`.

- `hmh07-lua:113` (original lines 12-175, 177-188, 192-195, 198-210, 213-228, 231-237, 12-175, 35-37, 43-51, 53-62, 63-66, 66-69, 89-91, 97-105, 108-117, 118-121, 121-124, 131-133, 137-139, 142-145, 146-149, 153-161, 177-188, 192-195, 198-210, 213-228, 231-237, 177-188, 192-195, 198-210, 213-228, 231-237, 15-15, 36-36, 90-90, 67-67, 122-122, 60-60, 115-115, 31-31, 85-85, 73-73, 169-169, 13-13, 138-138, 23-23, 78-78, 12-175, 177-188, 192-195, 198-210, 213-228, 231-237): Initializes CommonCurrentActiveTabIndex to1, constructs bumpers, basic tab list and two PC arrows. Arrow Disabled predicates test first/last tab; activation calls DoBumperGridButton with true/false respectively and consumes. ArrowShown requires ShowTabArrows and not gamepad; Hidden is locally false. Grid/input/model events revalidate. Frozen class reset/clips/close own presentation and disposal; no tab backend is reconstructed.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7d68da10eda56cde-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7d68da10eda56cde.json) at JSON pointer `/claims/16`.

  Archived evidence ID: `archived-record-00286` at JSON pointer ``; file SHA-256 `dcc2dee3a438b2235aea15810b19a07ef0f89481d895ed2deca6bfaebd4f10e9`.
