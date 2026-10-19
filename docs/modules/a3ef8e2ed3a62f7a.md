# ui/utility/videostreamingutility.lua

Project-added notes. See the [code](../../src/ui/utility/videostreamingutility.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `91366bb20a71335d5cb7c483027660de50ff3e8bfbc8a8bcc70fb978b17213ab`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/a3ef8e2ed3a62f7a.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua-follow4:140` (original lines 153-159, 153-159, 181-184, 181-184, 153-159, 153-159, 181-184, 181-184, 153-159, 153-159, 153-159, 181-184, 229-231, 182-182, 182-182, 154-154, 155-155, 153-159, 181-184, 153-159, 181-184): Returns featured_levenabled when that dvar exists; otherwise true. Reads stream from LiveEventViewer using SafeGetModelValue and returns stream and stream~=empty string. The result may be nil/falsy rather than a normalized Boolean.

  unknowns: &#91;{"kind": "original_build", "gap": "Recovered-source revision is pinned; original PS4 build/byte/VM/native binding remains unverified."}, {"kind": "effective_data_settings_assets", "gap": "Engine/model/Dvar/asset/data requests do not supply effective runtime values, contents or ownership."}, {"kind": "server_service_persistence", "gap": "Unavailable authoritative server/service/provider code and successful persistence remain unavailable; not reconstructed or counted as completed."}, {"kind": "runtime_callback_lifetime", "gap": "Original loading, table overwrites, callback delivery/order, timings, state selection and UI cleanup are not runtime-proven."}&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/a3ef8e2ed3a62f7a-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/a3ef8e2ed3a62f7a.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00710` at JSON pointer ``; file SHA-256 `b7810b1a59ac82a919e3a6e8e13d94c0eb836363c92740392ef3d5434634d312`.

- `hmh07-lua:061` (original lines 46-48): Locks input and marks UI active for every controller, starts video-event setup and builds main menu. It tracks reload-close children, closes them before reload setup, builds toast/spinner/optional warning/free cursor/overlay, polls UI3D readiness and cancels that timer when ready. Music subscription removes the previous subscription, replaces/closes delay timers, and plays only a nonempty state name. Debug reload clears children then rebuilds. Its close hook references element.toastNotification although the local toast is not assigned to that field in the selected text; preserve this external/fidelity assumption.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used.", "Selected recovered source has an explicit scope/control-flow/field assumption described in answer; original executable semantics are not guessed or repaired."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/a3ef8e2ed3a62f7a-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/a3ef8e2ed3a62f7a.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/60`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `97ac882a03c4f62c2a1485ba1e243dc9701726304323a891d61ddf473b0e18cb`.

- `hmh07-lua-follow3:155` (original lines 229-231, 229-231, 229-231, 229-231, 229-231, 229-231): Builds a comma-separated parameter string using a default first enum, empty second field and tostring of the third/fourth fields defaulted with or false. It does not escape commas in field values. Lua 0 is truthy and is retained; nil/false trigger the displayed defaults. No stream is started here. For CoD.VideoStreamingUtility.GetMoviePlayerParams, evaluate the displayed formal inputs and captured values. Its exact paths are 230: return "" .. (f19_arg0 or Enum&#91;@"hash_6C47FC1BD2E5CCEE"&#93;&#91;@"hash_390B07394D69C5F4"&#93;) .. "," .. (f19_arg1 or "") .. "," .. tostring( f19_arg2 or false ) .. "," .. tostring( f19_arg3 or false ). The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior.

  unknowns: &#91;"Original source-to-PS4/VM/native/loader identity and bytecode fidelity are unverified.", "Effective settings, assets/tables/model schemas, server/service implementation and callback delivery/lifetime are unverified.", "Exact source request semantics do not prove rendering, networking, persistence, progression or game behavior.", "Public reuse is the frozen manager audit only; no worker web/repository discovery was performed."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/a3ef8e2ed3a62f7a-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/a3ef8e2ed3a62f7a.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00003` at JSON pointer `/units/154`; file SHA-256 `a63852530df9189721a410c240a42967af6648aa0fca4e70325b17a1e677ebb7`; selected record SHA-256 `75a4dbf3b70dcbf1a5b13aa8951c3fac1c67294f2628842c2c5b50f118e14d23`.

- `hmh07-lua-follow8:012` (original lines 47-47, 47-47, 47-47): Exact selected canonical immediate source contracts saved below; all owned inline bodies are separate and all old units remain reused unchanged.

  unknowns: &#91;"Pinned recovered source only. No originating bytecode, source-to-PS4 match, loader/overwrite/metatable/native/VM/settings/assets/services/server or runtime-delivery proof. Author checks are not independent correctness review.", "No min/max gaps, unlisted other-file bodies, new data/writers or held OIC constructor were authored."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/a3ef8e2ed3a62f7a-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/a3ef8e2ed3a62f7a.json) at JSON pointer `/claims/3`.

  Archived evidence ID: `archived-record-00045` at JSON pointer `/units/11`; file SHA-256 `0c981d5eb446fe3dd44845673b101548cf36172da6abd92475497ba0faf30ce0`; selected record SHA-256 `33efdacdbd074c7e905ce4807c3f0a6f86b222e49d15484a868c5242c47d13a6`.

- `hmh07-lua-follow1:240` (original lines 46-48, 46-48, 46-48, 46-46, 46-48, 47-47, 46-48): StartLiveEventFromData delegates StartLiveEvent with the input table's controller and liveEventStreamerIndex fields. It has no validation, explicit return, local cancellation or response handling. The bare StartLiveEvent provider and unavailable original service/network/runtime behavior stay unresolved; no live event or network action was executed.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/a3ef8e2ed3a62f7a-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/a3ef8e2ed3a62f7a.json) at JSON pointer `/claims/4`.

  Archived evidence ID: `archived-record-00036` at JSON pointer `/units/239`; file SHA-256 `279ba12c6a1d4cfd1fb6c7e030a47694d4ee3982256bb21a0b3aa6909aef143b`; selected record SHA-256 `4eecf2e565f9053e943434dad1c72dffb359610a41522621b14dc9560df4d544`.

- `hmh07-lua-follow8:018` (original lines 229-229): Exact selected canonical immediate source contracts saved below; all owned inline bodies are separate and all old units remain reused unchanged.

  unknowns: &#91;"Pinned recovered source only. No originating bytecode, source-to-PS4 match, loader/overwrite/metatable/native/VM/settings/assets/services/server or runtime-delivery proof. Author checks are not independent correctness review.", "No min/max gaps, unlisted other-file bodies, new data/writers or held OIC constructor were authored."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/a3ef8e2ed3a62f7a-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/a3ef8e2ed3a62f7a.json) at JSON pointer `/claims/5`.

  Archived evidence ID: `archived-record-00045` at JSON pointer `/units/17`; file SHA-256 `0c981d5eb446fe3dd44845673b101548cf36172da6abd92475497ba0faf30ce0`; selected record SHA-256 `8c4df5f516a9a2fe52a4e23cc803bbfcbf64892f34b05e5c302e29ccf31db2db`.
