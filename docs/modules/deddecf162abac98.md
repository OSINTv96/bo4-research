# hashed/46a457d23cdffbb7.lua

Project-added notes. See the [code](../../src/lua/hashed/46a457d23cdffbb7.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `9bde3616d442c601e7ba382ad01df7a9d2067281225a759ff78f615dbcd11032`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/deddecf162abac98.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua-follow2:165` (original lines 208-238): Builds an Arena team-name/emblem display. Arena.currentTeamName, currentTeamId, and storage-file links update presentation; TeamComplete requires IsInTeam. Native emblem setup and team membership are not proved by constructing the element.

  unknowns: &#91;"Original PS4/source exact-version and original Lua/VM binding remain unverified.", "Effective enum/mode/platform/settings and asset/model/storage data are unavailable.", "Native/LUI event/subscription/timer dispatch, cleanup guarantees and errors not shown in selected source remain open.", "Unavailable service/server code is not reconstructed or counted."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/deddecf162abac98-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/deddecf162abac98.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00172` at JSON pointer ``; file SHA-256 `2b15eb1c323383d317281b58f621ba0d493f46526b6cc6ac524d3c4bbff27dac`; selected record SHA-256 `9f22a30b57058e632bcef93fd5804f61920ed9b241d0a305b1d93aa292624040`.

- `hmh07-lua-follow7:002` (original lines 210-210, 209-209, 208-238, 41-41): Only a truthy DDL-like first argument triggers two ClearDDLKeysAndArrays requests, in literal source sequence. The second request follows the first return and has no rollback. Return immediately for a falsey row list or destination. Otherwise traverse ipairs rows, write destination&#91;index-1&#93; using a native hash conversion of row&#91;key&#93; or EmptyItemIndex. A truthy destination and truthy item hash can produce a conversion, optional fallback conversion, set request and explicit result. The recovered trailing assignment is outside the local declaration scope; it does not set the destination or return EmptyItemIndex. Populate primary/secondary attachment and item fields, then grenade; additional ZM and MP branches use literal mode guards. Preserve duplicate secondary write, optional fourth-argument arithmetic and possible nil comparisons/returns. Request the hashed storage buffer. Nil buffer returns false; otherwise a nested StatValue:get greater than zero returns true and all other comparable results return false. Return the direct result of Dvar hash_20997C814ED4B7ED:get without existence test, coercion or default. Use the specialized DLC query only when the dvar exists, its value is truthy and main mode is MP or WZ; otherwise request getdlcbits with no forwarded arguments. Make a fresh result list; for nonnil/nonempty input, append converted tokens matched by &#91;^%s;&#93;+ in iteration order and return the list. For nonnil/nonempty blacklist text, return true at the first nonempty token whose native converted hash equals arg0; otherwise return false. Assign a fresh outer table whose keys field is a fresh ordered string array: killstreak1, killstreak2, killstreak3, killstreak4. It does not set actual loadout slots or grant anything. Top-level source assignment of numeric literal0 to the local module table field EmptyItemIndex. No original DDL invalid-item semantics or native conversion meaning is inferred from the name.

  unknowns: &#91;"Exact selected recovered Lua source only, conditional module/caller bindings. Original loader/global overwrite/VM/native/DDL/settings/assets/service/server/PS4 behavior remain unverified. No independent review, acceptance, function completion or runtime credit.", "Local at649 is scoped inside648..662; trailing663 reads/writes a global spelling. Preserve as recovered; do not hoist or insert a missing set/return. Original bytecode/VM fidelity remains missing.", "Potential nil>1 when ZM and fourth arg falsey; do not invent a default variant.", "updateItemIndexFromLoadoutHash can fall through without a returned empty marker;687 still requests a secondary set of its returned value."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/deddecf162abac98-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/deddecf162abac98.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00106` at JSON pointer `/units/1`; file SHA-256 `18e061e5ee7b1c2bc739ab68607b07765f3b9de61ca899283d64f04ffa0fc469`; selected record SHA-256 `d983452a945b56a8ddaaed414ca9f87e8b280662103e224975214f9b9fd2e98a`.

- `hmh07-lua-follow8:002` (original lines 210-210, 209-209, 208-238, 41-41): Reject an item index <= EmptyItemIndex or a falsey attachment list; otherwise build and return a fresh ordered list of converted attachment indices >= EmptyItemIndex. Create mode-to-slot-order table. Symbolic ZM->LoadoutSlotOrderZM, MP->LoadoutSlotOrderMP, CP->LoadoutSlotOrderCP, WZ->LoadoutSlotOrderMP. Create LoadoutPaintjobSlots.structs.primary.keys and .secondary.keys as separate nested tables, each with the one literal string paintjobSlot. Assign symbolic hash literal default_specialist_equipment to DefaultSpecialistEquipment.

  unknowns: &#91;"Exact selected recovered Lua source only, conditional module/caller bindings. Original loader/global overwrite/VM/native/DDL/settings/assets/service/server/PS4 behavior remain unverified. No independent review, acceptance, function completion or runtime credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/deddecf162abac98-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/deddecf162abac98.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00045` at JSON pointer `/units/1`; file SHA-256 `0c981d5eb446fe3dd44845673b101548cf36172da6abd92475497ba0faf30ce0`; selected record SHA-256 `0e0b8ac6edf15d211b52dba253d709535489834d466af86a7c2510c9a3d58db6`.

- `hmh07-lua-follow7:001` (original lines 210-210, 209-209, 208-238, 41-41): Look up the item-name hash in the first loot table; query the second only when the first result is falsey or the hash_0 sentinel. Return the second/first truthy result or hash_0. Assign a fresh outer table with hash-key ar_galil_t8 mapping to a fresh two-element sequence of symbolic mode_zombies then mode_warzone enum reads. This is a source default list, not proof of an actual unlock or original enum/item hash value.

  unknowns: &#91;"Exact selected recovered Lua source only, conditional module/caller bindings. Original loader/global overwrite/VM/native/DDL/settings/assets/service/server/PS4 behavior remain unverified. No independent review, acceptance, function completion or runtime credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/deddecf162abac98-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/deddecf162abac98.json) at JSON pointer `/claims/3`.

  Archived evidence ID: `archived-record-00106` at JSON pointer `/units/0`; file SHA-256 `18e061e5ee7b1c2bc739ab68607b07765f3b9de61ca899283d64f04ffa0fc469`; selected record SHA-256 `240cd20f30f7a067ffb93b31bd68cb0c77174f19422db3e4ccf183017f353064`.
