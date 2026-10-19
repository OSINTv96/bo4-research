# ui/uieditor/widgets/freecursor/infopanelsubwidgets/freecursorheaderlabel.lua

Project-added notes. See the [code](../../src/ui/uieditor/widgets/freecursor/infopanelsubwidgets/freecursorheaderlabel.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `cc0b7ab43cbd8d5e5aec903abea616782316798c557064633af0d7cfcaa92d29`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/eac4d1e43fd4a23f.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua-follow8:050` (original lines 37-42, 37-42, 37-37, 37-37, 37-37, 37-37, 7-115, 38-38, 39-39, 40-40, 41-41, 39-39, 37-42, 43-48, 43-48, 43-43, 43-43, 43-43, 43-43, 7-115, 44-44, 45-45, 46-46, 47-47, 44-44, 43-48, 55-57, 55-57, 55-55, 55-55, 55-55, 55-55, 7-115, 61-61, 56-56, 56-56, 55-57, 61-63, 61-63, 61-61, 61-61, 61-61, 61-61, 7-115, 62-62, 62-62, 61-63, 66-74, 66-74, 66-66, 66-66, 66-66, 66-66, 7-115, 67-67, 68-68, 69-69, 70-70, 71-71, 72-72, 73-73, 66-74, 78-86, 78-86, 78-78, 78-78, 78-78, 78-78, 7-115, 79-79, 80-80, 81-81, 82-82, 83-83, 84-84, 85-85, 78-86, 87-95, 87-95, 87-87, 87-87, 87-87, 87-87, 7-115, 88-88, 89-89, 90-90, 91-91, 92-92, 93-93, 94-94, 87-95, 96-103, 96-103, 96-96, 96-96, 96-96, 96-96, 7-115, 97-97, 98-98, 99-99, 100-100, 101-101, 102-102, 97-97, 100-100, 96-103, 231-235, 231-235, 231-231, 104-104, 104-104, 231-231, 232-232, 233-233, 234-234, 231-235, 232-232, 233-233, 234-234, 37-42, 38-38, 39-39, 40-40, 41-41, 43-48, 44-44, 45-45, 46-46, 47-47, 55-57, 56-56, 61-63, 62-62, 66-74, 67-67, 68-68, 69-69, 70-70, 71-71, 72-72, 73-73, 78-86, 79-79, 80-80, 81-81, 82-82, 83-83, 84-84, 85-85, 87-95, 88-88, 89-89, 90-90, 91-91, 92-92, 93-93, 94-94, 96-103, 97-97, 98-98, 99-99, 100-100, 101-101, 102-102, 231-235, 232-232, 233-233, 234-234, 39-39, 44-44, 56-56, 62-62, 97-97, 100-100, 37-42, 43-48, 55-57, 61-63, 66-74, 78-86, 87-95, 96-103, 231-235): Read title model; non-nil LocalizeToUpperString and set title text. title setText hook: only when supplied element text is nonempty scale self to self.title with5 then set container width to supplied element text with5. Empty text does nothing. Visible condition returns IsTooltipTitleVisible(supplied element,captured controller). VisibleDetailed condition returns AlwaysFalse() helper result; do not replace helper call with a constant. Read the supplied model without a nil guard and call captured menu:updateElementState with the exact captured widget and model_validation table in source_trace (menu, controller, modelValue and literal modelName preserved). No explicit return; state dispatcher effects remain opaque. Read the supplied model without a nil guard and call captured menu:updateElementState with the exact captured widget and model_validation table in source_trace (menu, controller, modelValue and literal modelName preserved). No explicit return; state dispatcher effects remain opaque. Read the supplied model without a nil guard and call captured menu:updateElementState with the exact captured widget and model_validation table in source_trace (menu, controller, modelValue and literal modelName preserved). No explicit return; state dispatcher effects remain opaque. setState hook: if self is default collapse self then parent; else expand self. No direct return or guard on parent. Close backingDetailed, backing and title in that order without nil checks.

  unknowns: &#91;"Exact source-to-PS4/bytecode/build match unverified.", "Original loader/VM/native/model/asset/settings/service and runtime delivery gaps remain open.", "HMH relevance is conditional on preserved caller gates; source definition alone proves no live reachability."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/eac4d1e43fd4a23f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/eac4d1e43fd4a23f.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00045` at JSON pointer `/units/49`; file SHA-256 `0c981d5eb446fe3dd44845673b101548cf36172da6abd92475497ba0faf30ce0`; selected record SHA-256 `de364fc64d065490806f485a29f036f654d67984876c9b635b811f4ee98a22ce`.

- `hmh07-lua-follow7:081` (original lines 7-7, 4-4, 106-106, 114-114, 7-115, 7-115, 7-7, 4-4, 8-8, 9-9, 10-10, 11-11, 12-12, 14-14, 15-15, 16-16, 17-17, 18-18, 19-19, 20-20, 21-21, 22-22, 23-23, 24-24, 26-26, 27-27, 28-28, 29-29, 31-31, 32-32, 33-33, 34-34, 35-35, 36-36, 37-37, 43-43, 49-49, 50-50, 52-52, 53-53, 54-54, 55-55, 58-58, 59-59, 60-60, 61-61, 64-64, 65-65, 66-66, 75-75, 76-76, 77-77, 78-78, 87-87, 96-96, 104-104, 106-106, 107-107, 108-108, 110-110, 111-111, 112-112, 113-113, 114-114, 106-106, 114-114, 37-42, 43-48, 55-57, 61-63, 66-74, 78-86, 87-95, 96-103, 37-42, 43-48, 55-57, 61-63, 66-74, 78-86, 87-95, 96-103, 231-235, 37-42, 43-48, 55-57, 61-63, 66-74, 78-86, 87-95, 96-103, 7-115): Constructs/queues exact-class default-sound element. Adds/stores transparent shader-configured backingDetailed, plain backing and gold title with ttmussels_regular/spacing6/left alignment. Registers title model link and title setText original-first callback, two state condition pointers, title/ButtonBits.rtrig/detailedViewPC validation callbacks and self setState original-first callback. Registers close pointer, calls truthy PostLoadFunc, marks both backing children ignored by horizontal layout, sets inCompactView=true, returns self. All nested callable semantics remain outside this selected immediate-body contract.

  unknowns: &#91;"Pinned recovered source only; no originating Lua bytecode, exact PS4 build/loader/overwrite/VM/native binding, effective HMH settings, resource availability, service/server behavior or runtime delivery proof. Author checks are not independent correctness review. Source defects and unguarded accesses remain literal.", "Only the selected callable's immediate statements are authored. Each unlisted nested callable is excluded from semantic authoring, including returned/local/condition/model/timer callbacks. Its exact lexical pointer and delivery site are metadata for later scope selection; containing its text does not authorize its body."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/eac4d1e43fd4a23f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/eac4d1e43fd4a23f.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00106` at JSON pointer `/units/80`; file SHA-256 `18e061e5ee7b1c2bc739ab68607b07765f3b9de61ca899283d64f04ffa0fc469`; selected record SHA-256 `e0035f001bdbc8a3b924a5bb979c6fc977c0711df16018bc5d359d3250ad7a84`.
