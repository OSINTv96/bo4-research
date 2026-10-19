# hashed/388b315302d997d5.lua

Project-added notes. See the [code](../../src/lua/hashed/388b315302d997d5.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `a69653f48b9aa01f49b5683cce572c79e73cf6a0c850554acb9ac4a327cda50d`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/e2fcf9484ece2cbc.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua-follow5:168` (original lines 77-79, 23-23, 9-30, 11-11, 77-79, 77-79, 78-78, 77-79, 23-23): On delivery of this class close hook, invoke in exact order: f9_arg0.ClanTag:close(). No receiver/child nil guard, parent close, exception recovery or successful-cleanup assertion is added; no explicit return.

  unknowns: &#91;{"kind": "unknown_receiver_or_VM_delivery", "receiver": "f9_arg0.ClanTag", "method": "close", "caller": {"unit_id": "hmh07-lua-follow5:168", "source_symbol": "CoD.AbilityCallout.__onClose", "citation": {"area": "references", "path": "lua/hashed/388b315302d997d5.lua", "line_start": 78, "line_end": 78, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "a69653f48b9aa01f49b5683cce572c79e73cf6a0c850554acb9ac4a327cda50d", "line_span_sha256": "ace534c928c9409276a1294bbd3d9cdb216a56d680e56954daff91f7d9aae5d3", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tf9_arg0.ClanTag:close() --&#91;&#91; @ 0&#93;&#93;", "scope_id": "lua/hashed/388b315302d997d5.lua:77", "guards_and_loops": &#91;&#93;, "limit": "Observed source call/reference only. Owned callback bodies execute only on invocation; inherited caller gates and loading remain conditional."}, "limit": "No generic method-name/get/close lookup. Receiver allocation may be visible in exact body, but its VM/class/provider implementation and actual callback delivery are not established by this call."}, {"kind": "original_VM_build_and_runtime", "limit": "Source-to-original bytecode/PS4 loading, original VM dialect, effective settings, actual asset/data values and runtime behavior are unverified."}, {"kind": "unavailable_online_server_service", "limit": "Online service/server implementations and real account/progression/persistence/network responses remain unavailable/unverified; not reconstructed or counted complete."}&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/e2fcf9484ece2cbc-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/e2fcf9484ece2cbc.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00034` at JSON pointer `/units/167`; file SHA-256 `781c1c1aee59bfc36951652bab7a837686810fc0aebaac4cb4ddfe8fe782f24f`; selected record SHA-256 `946ca7518a36b7558d07abf2b0dd1f8221794ddb32aee6e3a435b17162e6cec3`.

- `hmh07-lua-follow4:042` (original lines 9-30, 9-30, 17-19, 9-30, 9-30, 9-30, 9-30, 10-10, 16-16, 23-23, 77-79, 23-23, 26-26, 9-30, 9-30): Constructs CoD.AbilityCallout with the supplied menu/controller/layout values; its exact visual/data fields, condition closures, hook requests and return are retained below. Creates self via LUI.UIElement.new, ClanTag via CoD.AbilityCallout_Internal.new.

  unknowns: &#91;{"kind": "original_build", "gap": "Recovered-source revision is pinned; original PS4 build/byte/VM/native binding remains unverified."}, {"kind": "effective_data_settings_assets", "gap": "Engine/model/Dvar/asset/data requests do not supply effective runtime values, contents or ownership."}, {"kind": "server_service_persistence", "gap": "Unavailable authoritative server/service/provider code and successful persistence remain unavailable; not reconstructed or counted as completed."}, {"kind": "runtime_callback_lifetime", "gap": "Original loading, table overwrites, callback delivery/order, timings, state selection and UI cleanup are not runtime-proven."}&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/e2fcf9484ece2cbc-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/e2fcf9484ece2cbc.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00004` at JSON pointer `/units/41`; file SHA-256 `52df95eaa9f17f90427f6313acbc648c9bdffa0602f6444566bbe8fa1a54ba59`; selected record SHA-256 `6923a675a5e9a4e4448d817c06e5c11fb2f25f3daa97790cf17c723b296602b8`.
