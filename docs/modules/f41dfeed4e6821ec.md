# ui/uieditor/widgets/footer/footerbutton_partycount.lua

Project-added notes. See the [code](../../src/ui/uieditor/widgets/footer/footerbutton_partycount.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `4a46e40ee56a198bf43309a1e36fae9acc1149fa4f0baeb3123a4950e1968bf0`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/f41dfeed4e6821ec.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua-follow5:129` (original lines 51-51, 7-104, 38-38, 7-104, 51-51, 7-104, 38-38, 7-104, 7-104): Create/read lobbyRoot.lobbyList playerCount and maxPlayers models, default each value to0. The >1 arm assigns hash_A8276D01F6CFB14 and returns its localization only through the shown truthy branch. The singular/default path assigns hash_1733142924212699 but has no return in recovered text. Do not invent the omitted localization. Read private client lobby count and max clients. The >1 branch can return localization of hash_A8276D01F6CFB14. The remaining path only assigns hash_1733142924212699 and implicitly returns no value. The missing return is retained. Register square-button callback on arg0 for controller arg2. On delivery, ProcessListAction(list,list.activeWidget,controller,menu) only when ShowDirectorSelect, activeWidget and not m_disableNavigation all pass; callback always returns true. No registration removal in this body.

  unknowns: {"provider_or_lexical": &#91;&#93;, "source_fidelity": &#91;{"symbol": "CoD.DirectorUtility.LobbyListPlayerCountAndMax", "limit": "Singular/default hash assignment lacks a return/localization call."}, {"symbol": "CoD.DirectorUtility.PrivateLobbyListPlayerCountAndMax", "limit": "Singular/default hash assignment lacks a return/localization call."}&#93;, "original_build": "Recovered source is not matched to original PS4 bytecode/build; @0 is not a native address.", "VM_native": "Lua dialect, metatables, native/UI API execution, model dispatch/cancellation and input timing remain unverified.", "data_settings_assets": "Literal references do not supply effective model values, settings, data tables, localization or asset availability.", "server_service": "Online, stats, progression, marketing, lobby and backend behavior are unavailable service boundaries when requested by these exact bodies.", "runtime": "No game, console, account, router, save, native tool or independent review was run."}

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/f41dfeed4e6821ec-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/f41dfeed4e6821ec.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00441` at JSON pointer ``; file SHA-256 `24846d511031634cfd7c5aecdf878f45e4ac5ee611fb8b7f41db2730a516a32b`; selected record SHA-256 `6b61c10d8ce7fed398776d5f87e5c13a8accb2f91617447e6c9071e10e090265`.

- `hmh07-lua-follow5:112` (original lines 138-141, 138-138, 97-97, 7-104, 10-10, 138-141, 138-138, 97-97, 7-104, 10-10, 7-104, 138-141): On close callback invocation, execute in exact order: f9_arg0.PartyCount:close(); f9_arg0.MatchmakingCount:close(). Fall through with no explicit return. Members and close/helper availability are unguarded; no rollback, idempotence or recovery is shown.

  unknowns: {"provider_or_lexical": &#91;&#93;, "source_fidelity": &#91;&#93;, "original_build": "Recovered source is not matched to original PS4 bytecode/build; @0 is not a native address.", "VM_native": "Lua dialect, metatables, native/UI API execution, model dispatch/cancellation and input timing remain unverified.", "data_settings_assets": "Literal references do not supply effective model values, settings, data tables, localization or asset availability.", "server_service": "Online, stats, progression, marketing, lobby and backend behavior are unavailable service boundaries when requested by these exact bodies.", "runtime": "No game, console, account, router, save, native tool or independent review was run."}

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/f41dfeed4e6821ec-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/f41dfeed4e6821ec.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00034` at JSON pointer `/units/111`; file SHA-256 `781c1c1aee59bfc36951652bab7a837686810fc0aebaac4cb4ddfe8fe782f24f`; selected record SHA-256 `b0a8e0e5bb30308b641bd8cdb0fcff7531e3c77786e325ed07c62a315ef1ea15`.

- `hmh07-lua-follow4:122` (original lines 7-104, 7-104, 37-39, 50-52, 80-82, 88-96, 7-104, 7-104, 7-104, 7-104, 8-8, 15-15, 17-17, 24-24, 26-26, 30-30, 32-32, 36-36, 38-38, 38-38, 48-48, 51-51, 81-81, 97-97, 138-141, 97-97, 100-100, 63-63, 67-67, 71-71, 75-75, 87-87, 7-104, 7-104): Builds a party-count footer. Defines and immediately invokes both private-count and matchmaking-count text functions, then subscribes those same functions to private/game client updates. Matchmaking state tests publicLobby.stage against INVALID and is separately revalidated on stage changes. No party membership changes are implied. Creates self via LUI.UIHorizontalList.new, Label via LUI.UIText.new, Spacer2 via LUI.UIImage.new, Spacer via LUI.UIImage.new, PartyCount via LUI.UIText.new, MatchmakingCount via LUI.UIText.new. Stores state predicates Matchmaking; their body effects require state-system evaluation.

  unknowns: &#91;{"kind": "original_build", "gap": "Recovered-source revision is pinned; original PS4 build/byte/VM/native binding remains unverified."}, {"kind": "effective_data_settings_assets", "gap": "Engine/model/Dvar/asset/data requests do not supply effective runtime values, contents or ownership."}, {"kind": "server_service_persistence", "gap": "Unavailable authoritative server/service/provider code and successful persistence remain unavailable; not reconstructed or counted as completed."}, {"kind": "runtime_callback_lifetime", "gap": "Original loading, table overwrites, callback delivery/order, timings, state selection and UI cleanup are not runtime-proven."}&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/f41dfeed4e6821ec-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/f41dfeed4e6821ec.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00004` at JSON pointer `/units/121`; file SHA-256 `52df95eaa9f17f90427f6313acbc648c9bdffa0602f6444566bbe8fa1a54ba59`; selected record SHA-256 `82b15c03fa31f039d5734ead3fbd7f5e95ae2b0b39700556179430889cac2d2f`.
