# hashed/6b66155f91d2abd0.lua

Project-added notes. See the [code](../../src/lua/hashed/6b66155f91d2abd0.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `068a527eeedf1b245c366ee98febf36b712e75d87e0c85728d7590cfe9f86d3a`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/be4be2a2ab98c8fd.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua-follow7:080` (original lines 7-74): Constructs a UIHorizontalList with arguments2-9,0,false and left alignment; IsPC() gates UseFirstElementAsBacking only. Sets class/id/default sound/children-focus/update flags and queues self. Adds BG followed by Xbtn,Abtn,Bbtn,OptionsBtn,Ybtn,LTbtn,RTbtn,LeftStick,PCKey2,PCKeyBack at the literal rectangles. Each button registration/model link is retained without nested-body semantics. BG and both PCKey children are constructed unconditionally; CoD.isPC separately gates only the two PCKey id writes. Registers two state condition pointers, global lobbyNav/controller description/LastInput model callbacks and input_source_changed event callback. Assigns main button ids, registers close pointer, calls truthy PostLoadFunc, then UseVisibleChildrenWidth and UseMaxVisibleChildHeight and returns self. IsPC() and CoD.isPC are preserved as distinct source expressions.

  unknowns: &#91;"Pinned recovered source only; no originating Lua bytecode, exact PS4 build/loader/overwrite/VM/native binding, effective HMH settings, resource availability, service/server behavior or runtime delivery proof. Author checks are not independent correctness review. Source defects and unguarded accesses remain literal.", "Only the selected callable's immediate statements are authored. Each unlisted nested callable is excluded from semantic authoring, including returned/local/condition/model/timer callbacks. Its exact lexical pointer and delivery site are metadata for later scope selection; containing its text does not authorize its body."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/be4be2a2ab98c8fd-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/be4be2a2ab98c8fd.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00106` at JSON pointer `/units/79`; file SHA-256 `18e061e5ee7b1c2bc739ab68607b07765f3b9de61ca899283d64f04ffa0fc469`; selected record SHA-256 `1752ce2aa14cc266965c2134868857ee24d707396156d7c2a6da949590465d02`.

- `hmh07-lua-follow8:012` (original lines 7-74): Exact selected canonical immediate source contracts saved below; all owned inline bodies are separate and all old units remain reused unchanged.

  unknowns: &#91;"Pinned recovered source only. No originating bytecode, source-to-PS4 match, loader/overwrite/metatable/native/VM/settings/assets/services/server or runtime-delivery proof. Author checks are not independent correctness review.", "No min/max gaps, unlisted other-file bodies, new data/writers or held OIC constructor were authored."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/be4be2a2ab98c8fd-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/be4be2a2ab98c8fd.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00045` at JSON pointer `/units/11`; file SHA-256 `0c981d5eb446fe3dd44845673b101548cf36172da6abd92475497ba0faf30ce0`; selected record SHA-256 `33efdacdbd074c7e905ce4807c3f0a6f86b222e49d15484a868c5242c47d13a6`.

- `hmh07-lua-follow8:009` (original lines 7-7, 7-7, 7-74, 7-7, 8-8, 9-9, 10-10, 11-11, 12-12, 13-13, 14-14, 15-15, 16-16, 17-17, 18-18, 19-19, 20-20, 21-21, 22-22, 23-23, 24-24, 25-25, 26-26, 27-27, 28-28, 29-29, 30-30, 31-31, 32-32, 33-33, 34-34, 35-35, 36-36, 37-37, 38-38, 39-39, 40-40, 41-41, 42-42, 43-43, 44-44, 45-45, 46-46, 47-47, 48-48, 49-51, 52-52, 53-53, 54-54, 55-55, 56-56, 57-65, 66-66, 67-67, 68-68, 69-69, 70-70, 71-71, 72-72, 73-73, 74-74, 49-49, 7-74, 49-51, 49-49, 50-50, 51-51, 57-57, 7-74, 57-65, 57-57, 58-58, 59-59, 60-60, 61-61, 62-62, 63-63, 64-64, 65-65, 7-74, 7-74, 49-51, 57-65, 7-7, 7-7, 7-7, 8-8, 9-9, 10-10, 11-11, 12-12, 13-13, 14-14, 15-15, 16-16, 17-17, 18-18, 19-19, 20-20, 21-21, 22-22, 23-23, 24-24, 25-25, 26-26, 27-27, 28-28, 29-29, 30-30, 31-31, 32-32, 33-33, 34-34, 35-35, 36-36, 37-37, 38-38, 39-39, 40-40, 41-41, 42-42, 43-43, 44-44, 45-45, 46-46, 47-47, 48-48, 49-51, 52-52, 53-53, 54-54, 55-55, 56-56, 57-65, 66-66, 67-67, 68-68, 69-69, 70-70, 71-71, 72-72, 73-73, 74-74, 7-7, 8-8, 9-9, 10-10, 11-11, 12-12, 13-13, 14-14, 15-15, 16-16, 17-17, 18-18, 19-19, 20-20, 21-21, 22-22, 23-23, 24-24, 25-25, 26-26, 27-27, 28-28, 29-29, 30-30, 31-31, 32-32, 33-33, 34-34, 35-35, 36-36, 37-37, 38-38, 39-39, 40-40, 41-41, 42-42, 43-43, 44-44, 45-45, 46-46, 47-47, 48-48, 49-51, 52-52, 53-53, 54-54, 55-55, 56-56, 57-65, 66-66, 67-67, 68-68, 69-69, 70-70, 71-71, 72-72, 73-73, 74-74, 67-67, 73-73, 49-51, 57-65, 49-51, 49-51, 7-74, 7-74, 49-49, 7-74, 49-49, 50-50, 51-51, 49-49, 50-50, 51-51, 50-50, 57-65, 57-65, 7-74, 7-74, 57-57, 7-74, 57-57, 58-58, 59-59, 60-60, 61-61, 62-62, 63-63, 64-64, 65-65, 57-57, 58-58, 59-59, 60-60, 61-61, 62-62, 63-63, 64-64, 65-65, 7-74, 67-67, 73-73, 50-50, 7-74, 49-51, 57-65): Exact selected canonical immediate source contracts saved below; all owned inline bodies are separate and all old units remain reused unchanged.

  unknowns: &#91;"Pinned recovered source only. No originating bytecode, source-to-PS4 match, loader/overwrite/metatable/native/VM/settings/assets/services/server or runtime-delivery proof. Author checks are not independent correctness review.", "No min/max gaps, unlisted other-file bodies, new data/writers or held OIC constructor were authored."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/be4be2a2ab98c8fd-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/be4be2a2ab98c8fd.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00045` at JSON pointer `/units/8`; file SHA-256 `0c981d5eb446fe3dd44845673b101548cf36172da6abd92475497ba0faf30ce0`; selected record SHA-256 `657d8ae2935374193a0fefe7fe8825e0d2cc1b7927068a78283714a73fb4e811`.
