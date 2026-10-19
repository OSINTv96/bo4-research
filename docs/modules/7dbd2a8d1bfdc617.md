# hashed/122e4ff7e027aab8.lua

Project-added notes. See the [code](../../src/lua/hashed/122e4ff7e027aab8.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `f5c045a58146cbef24632d33c9aac10020d3ded4c7ca24cf3493c2b4764d2016`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/7dbd2a8d1bfdc617.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua-follow2:232` (original lines 265-278): Requests emblem profile, validates its current background ID, then validates the equipped emblem, in order. Validation providers and original user-content data remain external; the selected direct statements contain no UGC upload request. Transitive effects of the validation providers remain unknown.

  unknowns: &#91;"Original PS4/source exact-version and original Lua/VM binding remain unverified.", "Effective enum/mode/platform/settings and asset/model/storage data are unavailable.", "Native/LUI event/subscription/timer dispatch, cleanup guarantees and errors not shown in selected source remain open.", "Unavailable service/server code is not reconstructed or counted."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7dbd2a8d1bfdc617-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7dbd2a8d1bfdc617.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00536` at JSON pointer ``; file SHA-256 `8d284be97077d57ec8178175781ceb9a7a4ca5986a123eeea2cce4e99bf46165`; selected record SHA-256 `ecc77fb15ebd354ae34dbd64d01b1dcc5eaee55c753b36bbbee7b10b6852dcd3`.

- `hmh07-lua-follow3:158` (original lines 265-278, 265-278, 272-272, 266-266, 270-270, 265-278): Evaluate Engine&#91;@"isemblembackgroundlocked"&#93;(controller,background). If its result is truthy, set the local return value to0 and request SetEmblemBackground_Internal(controller,0); then a falsey IsLive() result selects Engine&#91;@"commitprofilechanges"&#93;(controller), otherwise request CoD.CraftUtility.UploadPublicProfile(nil,controller), before returning0. If the lock-query result is falsey, return the supplied background unchanged. SetEmblemBackground_Internal and IsLive provider identity and meanings remain unresolved here. No completed background mutation, commit/upload success, offline/live mode interpretation, original VM/build binding or runtime outcome is proved.

  unknowns: &#91;"Original PS4/source match, original Lua bytecode and VM/decompiler fidelity remain unverified.", "Effective enum/dvar/settings, assets/localization/model/DDL/storage/playlist data remain exact external inputs; requested persistence/network/service effects are not successful execution proof.", "A field/method/import/spelling or other-file local alone does not bind a provider. Unknown identities remain unresolved rather than declared unavailable.", "Native model/event/timer/wrapper invocation, delivery, error/cleanup/lifetime and unavailable original server behavior are outside this source packet.", "No independent correctness review, acceptance, original-build or function-completion credit is recorded."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7dbd2a8d1bfdc617-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7dbd2a8d1bfdc617.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00266` at JSON pointer ``; file SHA-256 `570190c79411d41fd789b1d9c98874de68719dff3f064fac363a0add4737b3c8`.

- `hmh07-lua-follow4:146` (original lines 60-68, 60-68, 60-60, 60-68, 60-68): Defaults a false/nil stat offset to the written enum, then a false/nil mode to current session mode; returns the native item-description request with all three values.

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7dbd2a8d1bfdc617-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7dbd2a8d1bfdc617.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00004` at JSON pointer `/units/145`; file SHA-256 `52df95eaa9f17f90427f6313acbc648c9bdffa0602f6444566bbe8fa1a54ba59`; selected record SHA-256 `b35b47296033509b6cdfa0b1af3506d41012116bbb69bdd0355f946dcdb3ea0e`.

- `hmh07-lua-follow4:263` (original lines 272-272, 272-272): cacRoot requests the hashed native root directly; otherwise chooses three-argument storagegetbuffer when arg2 is nonnil or the two-argument version. Returns the requested root/buffer. Weapon0 calls ClearDisplay then returns. Otherwise requests paintjob setup and a CustomClass_update local-client notify carrying the shown slot, converted weapon, empty attachments, camera and options fields. No network/persistence result is proved. Sends CustomClass_remove plus adjusted local-client number with an empty payload; no local cleanup completion is asserted. Returns editorMode != none from GetEmblemEditorProperties. Ends native edits; chooses paintshop/emblem customization and model notify; clears four per-controller selection fields; sets editor/color none and clipboard EMPTY; requests profile commit, optional paintjob invalidation and grid-size0. No rollback or commit success guard is added. Only uploadProfile==true clears the flag first and requests execnow uploadprofile. No retry/success notification or server implementation is supplied. For a supplied name matching an entitlement record and storage type, returns true at the first owned entitlement, else false for that matching record. No matching record or absent name defaults true. Both numeric loop headers are explicit: start1, step1, outer terminal #CoD.CraftUtility.EmblemEntitlements and inner terminal #f398_local3.entitlementRefs. Effective table contents, entitlement results and original VM execution remain unverified.

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/7dbd2a8d1bfdc617-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/7dbd2a8d1bfdc617.json) at JSON pointer `/claims/3`.

  Archived evidence ID: `archived-record-00505` at JSON pointer ``; file SHA-256 `050e7d2024d1f401dac7dca9759cc520a2deaa5a0797a2593994f2e7a11dd16b`; selected record SHA-256 `549fc51ec12820091d422cd9eb6660fd48ef8ca597a44b88cbeb052b9ce9bc98`.
