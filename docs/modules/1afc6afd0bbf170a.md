# ui/uieditor/widgets/pc/freecursor/freecursorheaderlabelpc.lua

Project-added notes. See the [code](../../src/ui/uieditor/widgets/pc/freecursor/freecursorheaderlabelpc.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `3425078823a783576732cd7f2cb644d4f7d9b3c881ca785ecc441d72f1478c01`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/1afc6afd0bbf170a.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua-follow7:083` (original lines 7-7, 4-4, 100-100, 104-104, 7-105, 7-105, 7-7, 4-4, 8-8, 9-9, 10-10, 11-11, 12-12, 14-14, 15-15, 16-16, 17-17, 18-18, 20-20, 21-21, 22-22, 23-23, 24-24, 25-25, 26-26, 27-27, 28-28, 29-29, 30-30, 31-31, 37-37, 43-43, 44-44, 46-46, 47-47, 48-48, 49-49, 52-52, 53-53, 54-54, 55-55, 58-58, 59-59, 60-60, 69-69, 70-70, 71-71, 72-72, 81-81, 90-90, 98-98, 100-100, 101-101, 102-102, 104-104, 100-100, 104-104, 31-36, 37-42, 49-51, 55-57, 60-68, 72-80, 81-89, 90-97, 31-36, 37-42, 49-51, 55-57, 60-68, 72-80, 81-89, 90-97, 153-155, 31-36, 37-42, 49-51, 55-57, 60-68, 72-80, 81-89, 90-97, 7-105): Constructs/queues exact-class default-sound element. Adds/stores initially transparent dark backing and gold title with ttmussels_regular/spacing4/left alignment plus literal backing type/color/alpha/padding. Registers title model link, title setText original-first callback, two state condition pointers, title/ButtonBits.rtrig/detailedViewPC validation callbacks and self setState original-first callback. Registers close pointer, calls truthy PostLoadFunc, returns self. No platform gate occurs in the selected immediate body and no nested condition semantics are authored.

  unknowns: &#91;"Pinned recovered source only; no originating Lua bytecode, exact PS4 build/loader/overwrite/VM/native binding, effective HMH settings, resource availability, service/server behavior or runtime delivery proof. Author checks are not independent correctness review. Source defects and unguarded accesses remain literal.", "Only the selected callable's immediate statements are authored. Each unlisted nested callable is excluded from semantic authoring, including returned/local/condition/model/timer callbacks. Its exact lexical pointer and delivery site are metadata for later scope selection; containing its text does not authorize its body."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/1afc6afd0bbf170a-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/1afc6afd0bbf170a.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00106` at JSON pointer `/units/82`; file SHA-256 `18e061e5ee7b1c2bc739ab68607b07765f3b9de61ca899283d64f04ffa0fc469`; selected record SHA-256 `175de3b503065488538bf390800d9e2a8531b7894eaac9f10fbf29189a4379f3`.

- `hmh07-lua-follow8:031` (original lines 31-36, 31-36, 31-36, 7-105, 7-105, 31-31, 31-31, 7-105, 31-31, 32-32, 33-33, 34-34, 35-35, 36-36, 33-33, 31-31, 7-105, 31-36, 37-42, 49-51, 55-57, 60-68, 72-80, 81-89, 90-97, 37-42, 37-42, 37-42, 7-105, 7-105, 37-37, 37-37, 7-105, 37-37, 38-38, 39-39, 40-40, 41-41, 42-42, 38-38, 37-37, 7-105, 31-36, 37-42, 49-51, 55-57, 60-68, 72-80, 81-89, 90-97, 49-51, 49-51, 49-51, 7-105, 7-105, 49-49, 49-49, 7-105, 49-49, 50-50, 51-51, 50-50, 49-49, 7-105, 31-36, 37-42, 49-51, 55-57, 60-68, 72-80, 81-89, 90-97, 55-57, 55-57, 55-57, 7-105, 7-105, 55-55, 55-55, 7-105, 55-55, 56-56, 57-57, 56-56, 55-55, 7-105, 31-36, 37-42, 49-51, 55-57, 60-68, 72-80, 81-89, 90-97, 60-68, 60-68, 60-68, 7-105, 7-105, 60-60, 60-60, 7-105, 60-60, 61-61, 62-62, 63-63, 64-64, 65-65, 66-66, 67-67, 68-68, 60-60, 7-105, 31-36, 37-42, 49-51, 55-57, 60-68, 72-80, 81-89, 90-97, 72-80, 72-80, 72-80, 7-105, 7-105, 72-72, 72-72, 7-105, 72-72, 73-73, 74-74, 75-75, 76-76, 77-77, 78-78, 79-79, 80-80, 72-72, 7-105, 31-36, 37-42, 49-51, 55-57, 60-68, 72-80, 81-89, 90-97, 81-89, 81-89, 81-89, 7-105, 7-105, 81-81, 81-81, 7-105, 81-81, 82-82, 83-83, 84-84, 85-85, 86-86, 87-87, 88-88, 89-89, 81-81, 7-105, 31-36, 37-42, 49-51, 55-57, 60-68, 72-80, 81-89, 90-97, 90-97, 90-97, 90-97, 7-105, 7-105, 90-90, 90-90, 7-105, 90-90, 91-91, 92-92, 93-93, 94-94, 95-95, 96-96, 97-97, 91-91, 94-94, 90-90, 7-105, 31-36, 37-42, 49-51, 55-57, 60-68, 72-80, 81-89, 90-97, 153-155, 153-155, 153-155, 153-153, 98-98, 153-153, 154-154, 155-155, 153-153, 31-36, 37-42, 49-51, 55-57, 60-68, 72-80, 81-89, 90-97, 153-155, 31-36, 37-42, 49-51, 55-57, 60-68, 72-80, 81-89, 90-97, 153-155, 33-33, 38-38, 50-50, 56-56, 91-91, 94-94): Authored 9 exact immediate-body contracts; prior source units remain full unchanged reuse. No original-build or runtime conclusion is added.

  unknowns: &#91;"Runtime loading/overwrite and actual HMH invocation remain unproved.", "All inherited prior partial/fidelity/excluded-nested/reviewer/report limits persist in reuse-preserved.json."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/1afc6afd0bbf170a-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/1afc6afd0bbf170a.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00045` at JSON pointer `/units/30`; file SHA-256 `0c981d5eb446fe3dd44845673b101548cf36172da6abd92475497ba0faf30ce0`; selected record SHA-256 `daa23019bcef22bd92d558c36bfc9e97c4bec6c93bf3aa4996b3892261c59c35`.
