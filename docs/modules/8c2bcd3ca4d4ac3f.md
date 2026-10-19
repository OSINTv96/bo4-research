# hashed/38a84b11249a3d27.lua

Project-added notes. See the [code](../../src/lua/hashed/38a84b11249a3d27.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `3b114d26295869c43ec134f2c419fea171626df1ef916fa9f855585842857ede`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/8c2bcd3ca4d4ac3f.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua-follow7:065` (original lines 576-576, 7-7, 12-12, 400-400, 400-400, 400-400, 10-407, 576-581, 576-581, 576-576, 7-7, 12-12, 400-400, 400-400, 400-400, 577-577, 578-578, 579-579, 580-580, 576-581): Takes the exact-class instance as its sole argument. Calls close() with each child as implicit self in this order: Clip, ClipDual, ClipHero, TotalAmmoLabel. No guard, branch, loop, explicit return, field reset, timer cancellation or protected error handling appears. A missing/already-closed child or provider error is not checked and can interrupt later closes. The constructor's setClass plus self.__onClose storage supplies the source pointer qualification; CallOriginalSecond owns wrapper ordering and actual delivery.

  unknowns: &#91;"Pinned recovered source only; no originating Lua bytecode, exact PS4 build/loader/overwrite/VM/native binding, effective HMH settings, resource availability, service/server behavior or runtime delivery proof. Author checks are not independent correctness review. Source defects and unguarded accesses remain literal."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/8c2bcd3ca4d4ac3f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/8c2bcd3ca4d4ac3f.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00106` at JSON pointer `/units/64`; file SHA-256 `18e061e5ee7b1c2bc739ab68607b07765f3b9de61ca899283d64f04ffa0fc469`; selected record SHA-256 `c72b9c18e15f4601fa64b80ce9a86931b4252389e479f92a8fd7edbaf66e5763`.
