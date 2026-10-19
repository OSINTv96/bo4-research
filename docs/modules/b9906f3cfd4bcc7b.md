# ui/utility/teamutility.lua

Project-added notes. See the [code](../../src/ui/utility/teamutility.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `5c4977630b142f700aaa7c0d5c28f2fd5eb0e5de9d6c58c4f6fdfc1eb48c26b8`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/b9906f3cfd4bcc7b.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua-follow1:236` (original lines 13-19, 86-94): UpdatePositionDraftClients sorts and filters frontend lobby clients, fills up to five position models and recreates the ZM list; in-game it selects the team/caster counterpart, remaps splitscreen positions, has a four-client campaign ordering branch, and clears models only in its explicit absent-team arm. Preserve missing fallback writes and comparator/local-scope defects. UpdatePositionDraftCharacters counts team roles, hides arena roles and writes unavailable/playerName by exact per-role limit. ChooseSpecialistMidMatch guards existing overlay/demo/bounty, then installs parent/child close hooks to close/clear the stored overlay. Native character/UI delivery remains conditional.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b9906f3cfd4bcc7b-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b9906f3cfd4bcc7b.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00530` at JSON pointer ``; file SHA-256 `5aa0abaeb8ed1fb78cba607772195bb56e4255db55b4868b2bd03689661cda2b`.

- `hmh07-lua-follow1:056` (original lines 130-132): IsShoutcaster returns true for demo-shoutcaster, or outside demo when model truth (default true if absent) and spectator-team/native shoutcaster hold; otherwise false. ExeProfileVarBool requires existing common profile/key with get()==1. VectorComponent parses string components with bounds1..count, otherwise only index1 returns original scalar, else0. SafeGetModelValue preserves short-circuit false/nil rather than normalizing. GetScriptNotifyData fetches numArgs, creates table only when positive, but the numeric for-loop still uses numArgs unguarded; absent count can fail and zero returns nil. Each argument is read via SafeGetModelValue and table.insert, so absent values are not assigned a synthetic placeholder. No VM/native/provider semantics are repaired.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b9906f3cfd4bcc7b-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b9906f3cfd4bcc7b.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00036` at JSON pointer `/units/55`; file SHA-256 `279ba12c6a1d4cfd1fb6c7e030a47694d4ee3982256bb21a0b3aa6909aef143b`; selected record SHA-256 `db57867b670b20da9813f48d2c5a00456bdc9dd75340aa1c604f3c1fa9c94197`.

- `hmh07-lua-follow5:274` (original lines 58-64, 58-64, 58-64, 60-60, 62-62, 58-64): Literal team2 returns its localized hash; every other input returns the other localized team-name hash. No team validation or lookup.

  unknowns: &#91;{"kind": "original_VM_build_and_runtime", "limit": "Source-to-original bytecode/PS4 loading, original VM dialect, effective settings, actual asset/data values and runtime behavior are unverified."}, {"kind": "unavailable_online_server_service", "limit": "Online service/server implementations and real account/progression/persistence/network responses remain unavailable/unverified; not reconstructed or counted complete."}&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b9906f3cfd4bcc7b-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b9906f3cfd4bcc7b.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00034` at JSON pointer `/units/273`; file SHA-256 `781c1c1aee59bfc36951652bab7a837686810fc0aebaac4cb4ddfe8fe782f24f`; selected record SHA-256 `7e8fc926e26090cd21ff92091e9d1b1e179290aa5d2377e435ee7abd3b7f5eb9`.

- `hmh07-lua-follow8:018` (original lines 103-103, 121-121): Exact selected canonical immediate source contracts saved below; all owned inline bodies are separate and all old units remain reused unchanged.

  unknowns: &#91;"Pinned recovered source only. No originating bytecode, source-to-PS4 match, loader/overwrite/metatable/native/VM/settings/assets/services/server or runtime-delivery proof. Author checks are not independent correctness review.", "No min/max gaps, unlisted other-file bodies, new data/writers or held OIC constructor were authored."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b9906f3cfd4bcc7b-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b9906f3cfd4bcc7b.json) at JSON pointer `/claims/3`.

  Archived evidence ID: `archived-record-00045` at JSON pointer `/units/17`; file SHA-256 `0c981d5eb446fe3dd44845673b101548cf36172da6abd92475497ba0faf30ce0`; selected record SHA-256 `8c4df5f516a9a2fe52a4e23cc803bbfcbf64892f34b05e5c302e29ccf31db2db`.

- `hmh07-lua-follow7:002` (original lines 274-274, 37-37, 49-49, 274-274, 37-37, 49-49): Only a truthy DDL-like first argument triggers two ClearDDLKeysAndArrays requests, in literal source sequence. The second request follows the first return and has no rollback. Return immediately for a falsey row list or destination. Otherwise traverse ipairs rows, write destination&#91;index-1&#93; using a native hash conversion of row&#91;key&#93; or EmptyItemIndex. A truthy destination and truthy item hash can produce a conversion, optional fallback conversion, set request and explicit result. The recovered trailing assignment is outside the local declaration scope; it does not set the destination or return EmptyItemIndex. Populate primary/secondary attachment and item fields, then grenade; additional ZM and MP branches use literal mode guards. Preserve duplicate secondary write, optional fourth-argument arithmetic and possible nil comparisons/returns. Request the hashed storage buffer. Nil buffer returns false; otherwise a nested StatValue:get greater than zero returns true and all other comparable results return false. Return the direct result of Dvar hash_20997C814ED4B7ED:get without existence test, coercion or default. Use the specialized DLC query only when the dvar exists, its value is truthy and main mode is MP or WZ; otherwise request getdlcbits with no forwarded arguments. Make a fresh result list; for nonnil/nonempty input, append converted tokens matched by &#91;^%s;&#93;+ in iteration order and return the list. For nonnil/nonempty blacklist text, return true at the first nonempty token whose native converted hash equals arg0; otherwise return false. Assign a fresh outer table whose keys field is a fresh ordered string array: killstreak1, killstreak2, killstreak3, killstreak4. It does not set actual loadout slots or grant anything. Top-level source assignment of numeric literal0 to the local module table field EmptyItemIndex. No original DDL invalid-item semantics or native conversion meaning is inferred from the name.

  unknowns: &#91;"Exact selected recovered Lua source only, conditional module/caller bindings. Original loader/global overwrite/VM/native/DDL/settings/assets/service/server/PS4 behavior remain unverified. No independent review, acceptance, function completion or runtime credit.", "Local at649 is scoped inside648..662; trailing663 reads/writes a global spelling. Preserve as recovered; do not hoist or insert a missing set/return. Original bytecode/VM fidelity remains missing.", "Potential nil>1 when ZM and fourth arg falsey; do not invent a default variant.", "updateItemIndexFromLoadoutHash can fall through without a returned empty marker;687 still requests a secondary set of its returned value."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/b9906f3cfd4bcc7b-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b9906f3cfd4bcc7b.json) at JSON pointer `/claims/4`.

  Archived evidence ID: `archived-record-00106` at JSON pointer `/units/1`; file SHA-256 `18e061e5ee7b1c2bc739ab68607b07765f3b9de61ca899283d64f04ffa0fc469`; selected record SHA-256 `d983452a945b56a8ddaaed414ca9f87e8b280662103e224975214f9b9fd2e98a`.

- `hmh07-lua-follow1:237` (original lines 302-323, 287-300, 256-285): ShowScoreboard forwards its sole argument; HideScoreboard forwards argument1, preserving the different signatures. Show/hide permission tests retain scoreboard-open/spawn-select, multiplayer/game-ended and WZ-map gates. SetScoreboardUIModels initializes local/controller0 fields, writes team summaries for multiplayer and conditionally player score, then writes all five column headers again unconditionally. Preserve duplicate header writes and absent native/model guards; no scoreboard or match was opened by this author.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b9906f3cfd4bcc7b-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b9906f3cfd4bcc7b.json) at JSON pointer `/claims/5`.

  Archived evidence ID: `archived-record-00250` at JSON pointer ``; file SHA-256 `0035cf029d406dfbafc9c7f578f9846a20bb958143151ad62c77b5abbe7a7c21`.

- `hmh07-lua-follow4:060` (original lines 247-247, 247-247, 247-247, 58-64, 134-149): Defaults an absent mode to currentsessionmode. Returns a gamedata/stats cp/mp/zm/wz statsmilestones path containing the supplied suffix and .csv for the four explicit modes. Preserve the recovered fallback exactly; the data table contents and effective mode are not supplied by this body. Returns Engine sessionmode_ispubliconlinegame unchanged. The engine predicate and live session are not established here. Gets the controller Customization datasource, creates the requested model path and returns its Engine model value. Creation and value semantics remain external. An assigned caster requesting spectator is mapped to allies. Allies/axis choose team1/team2 profile-name keys. A nonnil empty profile string returns the default caster name; a nonempty one returns unchanged. Other cases localize GetDefaultTeamName. This concerns display text, not team membership changes. Reads lobby gametype, obtains gametype info and returns its image field with no nil guard. Calls BaseSetMouseFocus first. Under usingfreecursor it writes hasFocus from GetMouseFocus and prepares FreeCursor.setupContext. The recovered nested branch calls setupContext only when the supplied element and its model exist, and the debug dvar clearing is nested inside that path. The final local nil assignment does not add a missing setupContext(nil) call. Returns 0 when CoD.isFrontend is true; otherwise forwards the controller to Engine getlocalclientnum.

  unknowns: &#91;{"kind": "original_build", "gap": "Recovered-source revision is pinned; original PS4 build/byte/VM/native binding remains unverified."}, {"kind": "effective_data_settings_assets", "gap": "Engine/model/Dvar/asset/data requests do not supply effective runtime values, contents or ownership."}, {"kind": "server_service_persistence", "gap": "Unavailable authoritative server/service/provider code and successful persistence remain unavailable; not reconstructed or counted as completed."}, {"kind": "runtime_callback_lifetime", "gap": "Original loading, table overwrites, callback delivery/order, timings, state selection and UI cleanup are not runtime-proven."}&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b9906f3cfd4bcc7b-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b9906f3cfd4bcc7b.json) at JSON pointer `/claims/6`.

  Archived evidence ID: `archived-record-00059` at JSON pointer ``; file SHA-256 `233a017594c54b6c63816380c134f260068e0b23fc06b0286fb8428dc505765f`; selected record SHA-256 `3a9973abfbe6217883acd9b6ae40d0aa3c03564be3046a07e673863fc994aa1a`.

- `hmh07-lua-follow4:259` (original lines 245-245, 245-245, 243-254): Lazily initializes ColorList, then finds controller TeamIdentity.ColorList/color_<id>/<field>; missing color or field returns nil, otherwise the model value. Lazily initializes LogoList, then finds controller TeamIdentity.LogoList/logo_<id>/<field>; missing logo or field returns nil, otherwise the model value. Queries host controlling-session clients and returns true for the first spectator-team client; returns false after the scan. This does not assign a caster.

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b9906f3cfd4bcc7b-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b9906f3cfd4bcc7b.json) at JSON pointer `/claims/7`.

  Archived evidence ID: `archived-record-00004` at JSON pointer `/units/258`; file SHA-256 `52df95eaa9f17f90427f6313acbc648c9bdffa0602f6444566bbe8fa1a54ba59`; selected record SHA-256 `90557c24220b9cee44e732a8f75465c26f48e1f6a617afc979c2b3489ddb8a79`.

- `hmh07-lua-follow3:225` (original lines 260-260, 260-260, 197-197, 260-260): Maps allies to team1 and axis to team2; if a mapped profile color lookup returns nonnil, returns it. All other cases return the default team faction color. Unknown team IDs use the default provider. Passes controller and the opaque current-stats selector returned by hash_508E494FC6037B54 to GetPlayerStats and returns its result. Passes controller and the opaque before-match selector returned by hash_4E038E13929C6347 to GetPlayerStats and returns its result. Returns getplayerstats(controller,selector) when selector is truthy, otherwise getplayerstats(controller). No snapshot contents, schema, or persistence success is inferred. Reads the online shoutcaster profile storage buffer and returns true only when buffer, named field, and field value1 are present; every other path returns false. Nil controller defaults0 and optionally prints warning outside frontend; reads currentMouseFocus&#91;controller+1&#93;; false sentinel returns nil, other values returned. No controller bounds validation.

  unknowns: &#91;"Original PS4/source match, original Lua bytecode and VM/decompiler fidelity remain unverified.", "Effective enum/dvar/settings, assets/localization/model/DDL/storage/playlist data remain exact external inputs; requested persistence/network/service effects are not successful execution proof.", "A field/method/import/spelling or other-file local alone does not bind a provider. Unknown identities remain unresolved rather than declared unavailable.", "Native model/event/timer/wrapper invocation, delivery, error/cleanup/lifetime and unavailable original server behavior are outside this source packet.", "No independent correctness review, acceptance, original-build or function-completion credit is recorded."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b9906f3cfd4bcc7b-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b9906f3cfd4bcc7b.json) at JSON pointer `/claims/8`.

  Archived evidence ID: `archived-record-00003` at JSON pointer `/units/224`; file SHA-256 `a63852530df9189721a410c240a42967af6648aa0fca4e70325b17a1e677ebb7`; selected record SHA-256 `dc3ed924f4a36239222d9147dc9d00867ba0d0a4042caa73ad862dc78b48b9dc`.

- `hmh07-lua-follow4:139` (original lines 103-119, 126-126, 103-119, 103-119, 134-149, 249-249, 134-149, 361-369, 361-369, 371-379, 371-379, 103-119, 126-126, 103-119, 103-119, 134-149, 249-249, 134-149, 361-369, 361-369, 371-379, 371-379, 103-119, 103-119, 103-119, 103-119, 134-149, 134-149, 134-149, 134-149, 134-149, 134-149, 361-369, 361-369, 371-379, 371-379, 126-126, 103-119, 103-119, 249-249, 134-149, 361-369, 371-379, 13-19, 86-94, 130-132, 256-285, 287-300, 302-323, 34-44, 46-56, 121-128, 197-215, 217-230, 243-254, 325-337, 343-355, 135-135, 141-141, 363-363, 366-366, 373-373, 376-376, 104-104, 108-108, 112-112, 103-119, 134-149, 361-369, 371-379, 103-119, 134-149, 361-369, 371-379): Returns a truthy engine getteamidbyxuid result. Otherwise scans game-session clients for the controller XUID and returns that row team; no match returns team_bad. Multiplayer allies/axis use mpui keys; campaign allies/axis use the two exact hashed keys. Other cases return TeamName&#91;team&#93; or hash_0. No mode or team-data repair occurs. Returns CodCasterFactionAllies for a shoutcaster; otherwise the controller color-blind FriendlyBlue color. Returns CodCasterFactionAxis for a shoutcaster; otherwise the controller color-blind EnemyOrange color.

  unknowns: &#91;{"kind": "original_build", "gap": "Recovered-source revision is pinned; original PS4 build/byte/VM/native binding remains unverified."}, {"kind": "effective_data_settings_assets", "gap": "Engine/model/Dvar/asset/data requests do not supply effective runtime values, contents or ownership."}, {"kind": "server_service_persistence", "gap": "Unavailable authoritative server/service/provider code and successful persistence remain unavailable; not reconstructed or counted as completed."}, {"kind": "runtime_callback_lifetime", "gap": "Original loading, table overwrites, callback delivery/order, timings, state selection and UI cleanup are not runtime-proven."}&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b9906f3cfd4bcc7b-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b9906f3cfd4bcc7b.json) at JSON pointer `/claims/9`.

  Archived evidence ID: `archived-record-00255` at JSON pointer ``; file SHA-256 `f6fdc21e49e6a8184d0e15b45f135ec71f5c9f84800301f751231561b811b34e`; selected record SHA-256 `aa9208229ee1a50031c4a57da97fe25781a670efcd80539ede612c0571b0af9b`.

- `hmh07-lua-follow8:002` (original lines 274-274, 37-37, 49-49, 274-274, 37-37, 49-49): Reject an item index <= EmptyItemIndex or a falsey attachment list; otherwise build and return a fresh ordered list of converted attachment indices >= EmptyItemIndex. Create mode-to-slot-order table. Symbolic ZM->LoadoutSlotOrderZM, MP->LoadoutSlotOrderMP, CP->LoadoutSlotOrderCP, WZ->LoadoutSlotOrderMP. Create LoadoutPaintjobSlots.structs.primary.keys and .secondary.keys as separate nested tables, each with the one literal string paintjobSlot. Assign symbolic hash literal default_specialist_equipment to DefaultSpecialistEquipment.

  unknowns: &#91;"Exact selected recovered Lua source only, conditional module/caller bindings. Original loader/global overwrite/VM/native/DDL/settings/assets/service/server/PS4 behavior remain unverified. No independent review, acceptance, function completion or runtime credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b9906f3cfd4bcc7b-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b9906f3cfd4bcc7b.json) at JSON pointer `/claims/10`.

  Archived evidence ID: `archived-record-00045` at JSON pointer `/units/1`; file SHA-256 `0c981d5eb446fe3dd44845673b101548cf36172da6abd92475497ba0faf30ce0`; selected record SHA-256 `0e0b8ac6edf15d211b52dba253d709535489834d466af86a7c2510c9a3d58db6`.

- `hmh07-lua-follow5:260` (original lines 366-366, 361-369, 376-376, 371-379, 366-366, 376-376): Returns ColorSet indexed by the colorblind-name helper(controller,color name). No fallback or RGB conversion is shown here. Returns three values r,g,b from the supplied table. No nil/type/channel normalization guards.

  unknowns: &#91;{"kind": "original_VM_build_and_runtime", "limit": "Source-to-original bytecode/PS4 loading, original VM dialect, effective settings, actual asset/data values and runtime behavior are unverified."}, {"kind": "unavailable_online_server_service", "limit": "Online service/server implementations and real account/progression/persistence/network responses remain unavailable/unverified; not reconstructed or counted complete."}&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b9906f3cfd4bcc7b-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b9906f3cfd4bcc7b.json) at JSON pointer `/claims/11`.

  Archived evidence ID: `archived-record-00034` at JSON pointer `/units/259`; file SHA-256 `781c1c1aee59bfc36951652bab7a837686810fc0aebaac4cb4ddfe8fe782f24f`; selected record SHA-256 `ac6bf1aa5d91f1dedc86add4152583fd5205f3c53113db705e47a8ca7a673912`.

- `hmh07-lua-follow3:138` (original lines 293-293, 293-293, 295-295, 295-295, 293-293, 295-295): For CoD.CodCasterUtility.GetCodCasterFactionIcon, evaluate the displayed formal inputs and captured values. Its exact paths are 90: if f6_arg1 == Enum&#91;@"team_t"&#93;&#91;@"team_allies"&#93; then; 92: elseif f6_arg1 == Enum&#91;@"team_t"&#93;&#91;@"team_axis"&#93; then; 95: if f6_local0 then; 97: if f6_local1 ~= nil then; 98: return f6_local1; 101: return CoD.CodCasterUtility.GetDefaultCodCasterFactionIcon( f6_arg1 ). Its writes/requests begin 91: f6_local0 = "team1"; 93: f6_local0 = "team2". The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior. For CoD.CodCasterUtility.GetDefaultCodCasterFactionIcon, evaluate the displayed formal inputs and captured values. Its exact paths are 105: if f7_arg0 == Enum&#91;@"team_t"&#93;&#91;@"team_allies"&#93; then; 106: return "uie_t7_codcaster_faction1"; 107: elseif f7_arg0 == Enum&#91;@"team_t"&#93;&#91;@"team_axis"&#93; then; 108: return "uie_t7_codcaster_faction2"; 110: return "". The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior.

  unknowns: &#91;"Original source-to-PS4/VM/native/loader identity and bytecode fidelity are unverified.", "Effective settings, assets/tables/model schemas, server/service implementation and callback delivery/lifetime are unverified.", "Exact source request semantics do not prove rendering, networking, persistence, progression or game behavior.", "Public reuse is the frozen manager audit only; no worker web/repository discovery was performed."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b9906f3cfd4bcc7b-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b9906f3cfd4bcc7b.json) at JSON pointer `/claims/12`.

  Archived evidence ID: `archived-record-00003` at JSON pointer `/units/137`; file SHA-256 `a63852530df9189721a410c240a42967af6648aa0fca4e70325b17a1e677ebb7`; selected record SHA-256 `fa37f5915534e18904bfa317529fbe97b4bed7878e1e513eee5f8bfa026febf9`.

- `hmh07-lua-follow7:001` (original lines 274-274, 37-37, 49-49, 274-274, 37-37, 49-49): Look up the item-name hash in the first loot table; query the second only when the first result is falsey or the hash_0 sentinel. Return the second/first truthy result or hash_0. Assign a fresh outer table with hash-key ar_galil_t8 mapping to a fresh two-element sequence of symbolic mode_zombies then mode_warzone enum reads. This is a source default list, not proof of an actual unlock or original enum/item hash value.

  unknowns: &#91;"Exact selected recovered Lua source only, conditional module/caller bindings. Original loader/global overwrite/VM/native/DDL/settings/assets/service/server/PS4 behavior remain unverified. No independent review, acceptance, function completion or runtime credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/b9906f3cfd4bcc7b-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/b9906f3cfd4bcc7b.json) at JSON pointer `/claims/13`.

  Archived evidence ID: `archived-record-00106` at JSON pointer `/units/0`; file SHA-256 `18e061e5ee7b1c2bc739ab68607b07765f3b9de61ca899283d64f04ffa0fc469`; selected record SHA-256 `240cd20f30f7a067ffb93b31bd68cb0c77174f19422db3e4ccf183017f353064`.
