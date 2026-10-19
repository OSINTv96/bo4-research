# hashed/3fc37a7c0deebbb7.lua

Project-added notes. See the [code](../../src/lua/hashed/3fc37a7c0deebbb7.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `a634b5c72789f16a0e1b723d5453657a473c7a54a03a4c84016472cee2f5fbf5`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/86edb9daddb04c93.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua:027` (original lines 7-65): Constructs ordinary XP and promotional XP displays, linking their models to self. Ordinary visible states use HasDoubleXP, including a WZ+mode variant; promotional state uses HasPromotionalDoubleXP. HasDoubleXP and daily promotional-time changes revalidate. Its setState hook adjusts presentation outside Visible/Promotional; frozen reset/clips/close retain the exact two-child effects. Promotional eligibility remains the MP/arena gate from its own selected helper, not assumed true in HMH.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/86edb9daddb04c93-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/86edb9daddb04c93.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00043` at JSON pointer ``; file SHA-256 `13be9da74034345aef0ea33f206b23ddfc9787ede31eb11de70de6cc142d895e`.

- `hmh07-lua-follow1:037` (original lines 67-69, 67-69, 58-58, 67-69, 67-69, 67-69, 58-58, 58-58, 7-65, 67-69): DirectorFindGamePlaylistInfoTimed2xp.__onClose closes f4_arg0.Time in that order, without nil guard, catch or extra cleanup. Per-function ordered operations below preserve all intermediate geometry/colors/materials, counter/reset order, closure bindings, explicit returns and nested completion/interrupt handlers. A nextClip assignment requests repetition; no runtime timing or cancellation guarantee is inferred. Constructor/state predicates are reused, not re-authored. No gameplay state/model producer is added by table membership.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/86edb9daddb04c93-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/86edb9daddb04c93.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00036` at JSON pointer `/units/36`; file SHA-256 `279ba12c6a1d4cfd1fb6c7e030a47694d4ee3982256bb21a0b3aa6909aef143b`; selected record SHA-256 `4c262dfedd9c78708b912ab25038a49cf8797c0f34e56ddf2756971086f02e1e`.

- `hmh07-lua-follow1:146` (original lines 58-58, 58-58): CallOriginalFirst appends the supplied callback to the table returned by OverrideFunction_GetFunctionTable. CallOriginalSecond inserts its callback at index1. Neither wrapper directly calls the original or callback or returns a value. The naming does not prove runtime order independently of the dispatcher, which remains a reusable available dependency.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/86edb9daddb04c93-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/86edb9daddb04c93.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00044` at JSON pointer ``; file SHA-256 `46ecb6cfe8fa919ec918f489610848dcd8b393e632706abbfd898ba7b2a05c62`.

- `hmh07-lua-follow1:008` (original lines 14-14, 19-19, 32-32, 14-14, 19-19, 32-32, 14-14, 7-65, 19-19, 7-65, 32-32, 7-65): UIImage.new forwards all eight layout arguments to UIElement.new, sets UIImage class, calls setupUIImage and returns self. GetCachedMaterial indexes Materials by requested key; only a nil cache entry calls RegisterMaterial and writes its return to the cache, then returns the cached value. False is a cache hit; a nil RegisterMaterial result can be retried next call. No image/native/material ownership or original runtime contract is supplied.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/86edb9daddb04c93-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/86edb9daddb04c93.json) at JSON pointer `/claims/3`.

  Archived evidence ID: `archived-record-00036` at JSON pointer `/units/7`; file SHA-256 `279ba12c6a1d4cfd1fb6c7e030a47694d4ee3982256bb21a0b3aa6909aef143b`; selected record SHA-256 `7329bd99e083ca457a54272bf2df1457c445a3fb2e8a07aa636d127734ffcbbf`.

- `hmh07-lua-follow1:125` (original lines 8-8, 8-8): UIElement.new tries ConstructLUIElement with eight supplied layout arguments when the first is truthy, then sets initial class and returns only on a truthy constructed value. Otherwise it calls ConstructLUIElement with m_defaultAnimationState and falls through without an explicit return or setInitialClass in this recovered text. Preserve that fidelity defect. createFake returns a fresh empty table with fakeElemMetaTable; fake operations and native construction remain separate contracts.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/86edb9daddb04c93-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/86edb9daddb04c93.json) at JSON pointer `/claims/4`.

  Archived evidence ID: `archived-record-00047` at JSON pointer ``; file SHA-256 `0a2ed5281f322b9558d79fcfa95c412c52c1a5b3106117496e96cceee9304688`.

- `hmh07-lua:199` (original lines 7-65, 25-25, 41-41, 44-44, 58-58, 43-43, 52-52, 54-54, 60-60, 64-64, 67-67, 67-69, 58-58, 54-54, 49-59, 58-58, 53-63, 8-8, 3-13, 14-14, 9-19, 19-19, 14-24, 32-32, 27-37, 24-24, 19-29, 36-36, 31-41, 44-44, 39-49, 61-61, 56-66, 15-15, 10-20, 7-65): Cited playlist info constructor creates this text presentation child directly. PromotionalDoubleXP.dailyDoubleXPTimeLeft nonnil updates Time through LocalizeIntoString with exact hash_6ACC0A2311E2A5EA. Own french state delegates IsCurrentLanguageFrench; does not grant XP or control the countdown producer. CallOriginalSecond close registers self.__onClose, outside selected body remains a dependency. Optional postload then self return; language/backend clock/localization unknown.

  unknowns: &#91;"Original Lua-to-PS4 CUSA11100 build binding and bytecode/VM/decompiler fidelity unverified.", "Effective HMH settings, enum values, model/data production, LUI state arbitration, event delivery/ordering/cancellation, assets, storage/DDL, networking/service behavior remain explicit gaps where called.", "External helper bodies not selected here are dependencies only; no nil/error recovery assumed beyond visible source. Named LUI override APIs are preserved; no original/new callback ordering is guaranteed without their source contract.", "No independent correctness review, retail execution or function completion credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/86edb9daddb04c93-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/86edb9daddb04c93.json) at JSON pointer `/claims/5`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/198`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `0852ffdc5671e08ca8f13ede71c70230f818dbea2a1087cb465bea251090adbd`.

- `hmh07-lua-follow1:167` (original lines 24-24, 36-36, 24-24, 36-36): UIText.new passes the eight supplied layout arguments to UIElement.new, sets UIText class, calls setupUIText and returns the resulting receiver. It has no explicit nil guard or rollback if base/native setup fails. Reuse the separate UIElement constructor contract including its recovered fallthrough defect; no working retail text object is proved.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/86edb9daddb04c93-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/86edb9daddb04c93.json) at JSON pointer `/claims/6`.

  Archived evidence ID: `archived-record-00089` at JSON pointer ``; file SHA-256 `bc1ff14cac27ee3b461ef85a9adbe0f0a3b83007a9a3a7b175927aac3abe67a4`.
