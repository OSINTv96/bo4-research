# ui/uieditor/widgets/lobby/mapvote/mapvoteitem.lua

Project-added notes. See the [code](../../src/ui/uieditor/widgets/lobby/mapvote/mapvoteitem.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `f3cb4b0d37e506e61b4078add144f87c366142ef8ee574f138504af8e82bc338`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/7d706ede76b1bbba.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua:003` (original lines 93-93, 93-93): Builds focus glow, brackets, lines and border; queues state updates and hooks the same-class close method. Frozen class clips reset animation properties before presenting DefaultState focus/gain/lose and Disabled clips. GainFocus chains bracket animations; interruption and transition handlers complete distinct clip paths. There is no local Disabled predicate in the constructor, so an external state request is still needed.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7d706ede76b1bbba-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7d706ede76b1bbba.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/2`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `5e5e526a248d8f7162ab5a5a5aaf5daecb64b054658f6883d1af955a00b47980`.

- `hmh07-lua:006` (original lines 28-28, 28-28): Builds game-mode and map-name text with separate backings and fixed initial values. It returns a visual layout after optional PostLoadFunc. No local model binding, vote action or mode gate is present; MapVoteItem.new constructs and retains the nested layout at28-30. The enclosing MapVote.new in hashed/114b49e336ed83f6.lua installs map/game-type subscriptions37-48 whose nonnil-value callbacks request updates to the nested MapName/GameMode text; actual callback delivery and UI effects remain unproved. This constructor alone does not select or submit a map vote.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7d706ede76b1bbba-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7d706ede76b1bbba.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00637` at JSON pointer ``; file SHA-256 `2a9eb4fb20e53331a4c521edeb4e5fe98385c853f414a1868330e8ef911626a5`.

- `hmh07-lua:193` (original lines 8-8, 4-12): InheritFrom is executed at the cited class assignments, not merely imported. Missing/falsy base throws explicit LUI Error. Otherwise makes a new table with super=base, sets its metatable __index=base, creates a fresh m_eventHandlers table with __index=base.m_eventHandlers, then returns the new class. It shares fallback handlers while permitting per-class handler writes. Does not instantiate widgets, invoke inherited callbacks or close anything. Metatable/native VM behavior and base fields are assumed, no further validation.

  unknowns: &#91;"Original Lua-to-PS4 CUSA11100 build binding and bytecode/VM/decompiler fidelity unverified.", "Effective HMH settings, enum values, model/data production, LUI state arbitration, event delivery/ordering/cancellation, assets, storage/DDL, networking/service behavior remain explicit gaps where called.", "External helper bodies not selected here are dependencies only; no nil/error recovery assumed beyond visible source. Named LUI override APIs are preserved; no original/new callback ordering is guaranteed without their source contract.", "No independent correctness review, retail execution or function completion credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7d706ede76b1bbba-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7d706ede76b1bbba.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/192`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `28096b9a20c988def77f03e8d965db4759673d7a552db8efd9d89c53725de88c`.

- `hmh07-lua-follow1:146` (original lines 114-114, 114-114, 11-121, 123-123, 123-148, 11-121, 150-150, 152-155, 11-121, 150-150, 156-171, 11-121, 150-150, 172-215, 11-121, 150-150, 216-259, 11-121, 150-150, 262-268, 11-121, 150-150, 271-304, 11-121, 307-307, 307-311): CallOriginalFirst appends the supplied callback to the table returned by OverrideFunction_GetFunctionTable. CallOriginalSecond inserts its callback at index1. Neither wrapper directly calls the original or callback or returns a value. The naming does not prove runtime order independently of the dispatcher, which remains a reusable available dependency.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7d706ede76b1bbba-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7d706ede76b1bbba.json) at JSON pointer `/claims/3`.

  Archived evidence ID: `archived-record-00044` at JSON pointer ``; file SHA-256 `46ecb6cfe8fa919ec918f489610848dcd8b393e632706abbfd898ba7b2a05c62`.

- `hmh07-lua-follow1:226` (original lines 150-306, 150-306, 13-13, 13-13, 152-155, 152-152, 156-171, 156-156, 172-215, 172-172, 175-180, 175-175, 185-190, 185-185, 195-200, 195-195, 205-210, 205-205, 216-259, 216-216, 219-224, 219-219, 229-234, 229-229, 239-244, 239-239, 249-254, 249-249, 262-268, 262-262, 271-304, 271-271, 150-306, 11-121, 123-123, 123-148, 11-121, 150-150, 152-155, 11-121, 150-150, 156-171, 11-121, 150-150, 172-215, 11-121, 150-150, 216-259, 11-121, 150-150, 262-268, 11-121, 150-150, 271-304, 11-121, 307-307, 307-311, 150-306): Adds MapVoteItem default/child-focus/gain/loss, Selected and Unselectable clips. Reset establishes baseline; focus transitions retain exact bracket/map-name/backing property changes, durations and completion order. Reuse stopped constructor248 vote predicates and selection models. Neither a Selected slot nor source definition proves an original vote was accepted.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7d706ede76b1bbba-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7d706ede76b1bbba.json) at JSON pointer `/claims/4`.

  Archived evidence ID: `archived-record-00638` at JSON pointer ``; file SHA-256 `ad8eb2b4ad31e2bffcb611a4e3bdef595a601dd79d8fd8bfa913973d011ab7ac`; selected record SHA-256 `d231cb9148fbdaddddd1b992b54334af8b564dad29a94ffc39bd86b905780dc2`.

- `hmh07-lua-follow8:003` (original lines 8-8, 4-12): Assign the supplied widget type to the receiver field, then request receiver:clearLayout(). The source setter does not call the widget constructor.

  unknowns: &#91;"Exact selected recovered Lua source only, conditional module/caller bindings. Original loader/global overwrite/VM/native/DDL/settings/assets/service/server/PS4 behavior remain unverified. No independent review, acceptance, function completion or runtime credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7d706ede76b1bbba-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7d706ede76b1bbba.json) at JSON pointer `/claims/5`.

  Archived evidence ID: `archived-record-00045` at JSON pointer `/units/2`; file SHA-256 `0c981d5eb446fe3dd44845673b101548cf36172da6abd92475497ba0faf30ce0`; selected record SHA-256 `3843c6aed3c88d59e0c2b91a3eb9d0e61ecd93d8a7660df06791bae7e79e7153`.

- `hmh07-lua-follow1:008` (original lines 19-19, 32-32, 37-37, 67-67, 76-76, 86-86, 21-21, 52-52, 61-61, 70-70, 80-80, 19-19, 32-32, 37-37, 67-67, 76-76, 86-86, 19-19, 11-121, 32-32, 11-121, 37-37, 11-121, 67-67, 11-121, 76-76, 11-121, 86-86, 11-121, 21-21, 52-52, 61-61, 70-70, 80-80, 21-21, 11-121, 52-52, 11-121, 61-61, 11-121, 70-70, 11-121, 80-80, 11-121): UIImage.new forwards all eight layout arguments to UIElement.new, sets UIImage class, calls setupUIImage and returns self. GetCachedMaterial indexes Materials by requested key; only a nil cache entry calls RegisterMaterial and writes its return to the cache, then returns the cached value. False is a cache hit; a nil RegisterMaterial result can be retried next call. No image/native/material ownership or original runtime contract is supplied.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7d706ede76b1bbba-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7d706ede76b1bbba.json) at JSON pointer `/claims/6`.

  Archived evidence ID: `archived-record-00036` at JSON pointer `/units/7`; file SHA-256 `279ba12c6a1d4cfd1fb6c7e030a47694d4ee3982256bb21a0b3aa6909aef143b`; selected record SHA-256 `7329bd99e083ca457a54272bf2df1457c445a3fb2e8a07aa636d127734ffcbbf`.

- `hmh07-lua-follow1:125` (original lines 12-12, 12-12, 11-121, 123-123, 123-148, 11-121, 150-150, 152-155, 11-121, 150-150, 156-171, 11-121, 150-150, 172-215, 11-121, 150-150, 216-259, 11-121, 150-150, 262-268, 11-121, 150-150, 271-304, 11-121, 307-307, 307-311): UIElement.new tries ConstructLUIElement with eight supplied layout arguments when the first is truthy, then sets initial class and returns only on a truthy constructed value. Otherwise it calls ConstructLUIElement with m_defaultAnimationState and falls through without an explicit return or setInitialClass in this recovered text. Preserve that fidelity defect. createFake returns a fresh empty table with fakeElemMetaTable; fake operations and native construction remain separate contracts.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7d706ede76b1bbba-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7d706ede76b1bbba.json) at JSON pointer `/claims/7`.

  Archived evidence ID: `archived-record-00047` at JSON pointer ``; file SHA-256 `0a2ed5281f322b9558d79fcfa95c412c52c1a5b3106117496e96cceee9304688`.

- `hmh07-lua:090` (original lines 103-103, 109-109, 103-103, 109-109): Returns false unconditionally, providing a source proof that the attached predicate cannot select a state through this condition alone.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7d706ede76b1bbba-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7d706ede76b1bbba.json) at JSON pointer `/claims/8`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/89`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `101ca4cbf310a20bbc095a1688a99133387e50b3bc4f7e558c5c78128289880a`.

- `hmh07-lua-follow1:167` (original lines 47-47, 57-57, 47-47, 57-57, 11-121, 123-123, 123-148, 11-121, 150-150, 152-155, 11-121, 150-150, 156-171, 11-121, 150-150, 172-215, 11-121, 150-150, 216-259, 11-121, 150-150, 262-268, 11-121, 150-150, 271-304, 11-121, 307-307, 307-311): UIText.new passes the eight supplied layout arguments to UIElement.new, sets UIText class, calls setupUIText and returns the resulting receiver. It has no explicit nil guard or rollback if base/native setup fails. Reuse the separate UIElement constructor contract including its recovered fallthrough defect; no working retail text object is proved.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7d706ede76b1bbba-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7d706ede76b1bbba.json) at JSON pointer `/claims/9`.

  Archived evidence ID: `archived-record-00089` at JSON pointer ``; file SHA-256 `bc1ff14cac27ee3b461ef85a9adbe0f0a3b83007a9a3a7b175927aac3abe67a4`.

- `hmh07-lua:248` (original lines 11-121, 33-33, 39-39, 49-49, 50-50, 59-59, 68-68, 77-77, 87-87, 95-95, 114-114, 136-136, 138-138, 140-140, 141-141, 166-166, 169-169, 176-176, 178-178, 179-179, 186-186, 188-188, 189-189, 196-196, 197-197, 198-198, 199-199, 203-203, 206-206, 207-207, 208-208, 209-209, 213-213, 220-220, 222-222, 223-223, 230-230, 232-232, 233-233, 240-240, 241-241, 242-242, 243-243, 247-247, 250-250, 251-251, 252-252, 253-253, 257-257, 266-266, 287-287, 308-308, 309-309, 310-310, 101-101, 103-103, 107-107, 109-109, 116-116, 120-120, 11-121, 123-123, 123-148, 11-121, 150-150, 152-155, 11-121, 150-150, 156-171, 11-121, 150-150, 172-215, 11-121, 150-150, 216-259, 11-121, 150-150, 262-268, 11-121, 150-150, 271-304, 11-121, 307-307, 307-311, 103-103, 98-108, 109-109, 104-114, 93-93, 88-98, 28-28, 23-33, 43-43, 38-48, 114-114, 109-119, 12-12, 7-17, 21-21, 16-26, 52-52, 47-57, 61-61, 56-66, 70-70, 65-75, 80-80, 75-85, 19-19, 14-24, 32-32, 27-37, 37-37, 32-42, 67-67, 62-72, 76-76, 71-81, 86-86, 81-91, 47-47, 42-52, 57-57, 52-62, 117-117, 112-122, 20-20, 15-25, 69-69, 64-74, 79-79, 74-84, 89-89, 84-94, 150-150, 150-306, 13-13, 11-121, 11-121): MapVote directly constructs decided/random/previous/next entries. Builds image, name/mode layout, overlay/backing, vote text/count, brackets/marker/button outline. Selected and Unselectable defaults are AlwaysFalse; MapVote parent merges Selected=true on decided entry and Previous-selectability condition on previous. Thus exact caller override matters; own default false does not exclude those states globally. Qualified reset/state/focus clips change selection/disable visuals and exact timing; __onClose closes layout/backing/button-outline through CallOriginalSecond. No confirm/network vote call here; parent unit179 owns it. Optional postload then self return.

  unknowns: &#91;"Original Lua-to-PS4 CUSA11100 build binding and bytecode/VM/decompiler fidelity unverified.", "Effective HMH settings, enum values, model/data production, LUI state arbitration, event delivery/ordering/cancellation, assets, storage/DDL, networking/service behavior remain explicit gaps where called.", "External helper bodies not selected here are dependencies only; no nil/error recovery assumed beyond visible source. Named LUI override APIs are preserved; no original/new callback ordering is guaranteed without their source contract.", "No independent correctness review, retail execution or function completion credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7d706ede76b1bbba-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7d706ede76b1bbba.json) at JSON pointer `/claims/10`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/247`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `764a3e3d131f24c33f4a6f6018800eccb3b4da2fefc9f8defcf53fea4c8e5564`.
