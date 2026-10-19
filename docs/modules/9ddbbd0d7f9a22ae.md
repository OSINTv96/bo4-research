# ui/utility/directorutility.lua

Project-added notes. See the [code](../../src/ui/utility/directorutility.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `d8e4f3ea3b1089b685d89179393903a1b00a443b97004b47bd4d7d95622b62b7`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/9ddbbd0d7f9a22ae.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua-follow5:129` (original lines 3287-3303, 3287-3287, 3288-3288, 3289-3289, 3290-3290, 3291-3291, 3292-3292, 3299-3299, 3305-3318, 3305-3305, 3306-3306, 3307-3307, 3314-3314, 4939-4946, 4939-4939, 4940-4945, 3287-3303, 3287-3287, 3305-3318, 3305-3305, 4939-4946, 4939-4939, 4941-4941, 2962-2975, 2962-2975, 4942-4942, 3288-3288, 3289-3289, 3290-3290, 3291-3291, 3292-3292, 3299-3299, 3306-3306, 3307-3307, 3314-3314, 3287-3303, 3305-3318, 4939-4946): Create/read lobbyRoot.lobbyList playerCount and maxPlayers models, default each value to0. The >1 arm assigns hash_A8276D01F6CFB14 and returns its localization only through the shown truthy branch. The singular/default path assigns hash_1733142924212699 but has no return in recovered text. Do not invent the omitted localization. Read private client lobby count and max clients. The >1 branch can return localization of hash_A8276D01F6CFB14. The remaining path only assigns hash_1733142924212699 and implicitly returns no value. The missing return is retained. Register square-button callback on arg0 for controller arg2. On delivery, ProcessListAction(list,list.activeWidget,controller,menu) only when ShowDirectorSelect, activeWidget and not m_disableNavigation all pass; callback always returns true. No registration removal in this body.

  unknowns: {"provider_or_lexical": &#91;&#93;, "source_fidelity": &#91;{"symbol": "CoD.DirectorUtility.LobbyListPlayerCountAndMax", "limit": "Singular/default hash assignment lacks a return/localization call."}, {"symbol": "CoD.DirectorUtility.PrivateLobbyListPlayerCountAndMax", "limit": "Singular/default hash assignment lacks a return/localization call."}&#93;, "original_build": "Recovered source is not matched to original PS4 bytecode/build; @0 is not a native address.", "VM_native": "Lua dialect, metatables, native/UI API execution, model dispatch/cancellation and input timing remain unverified.", "data_settings_assets": "Literal references do not supply effective model values, settings, data tables, localization or asset availability.", "server_service": "Online, stats, progression, marketing, lobby and backend behavior are unavailable service boundaries when requested by these exact bodies.", "runtime": "No game, console, account, router, save, native tool or independent review was run."}

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00441` at JSON pointer ``; file SHA-256 `24846d511031634cfd7c5aecdf878f45e4ac5ee611fb8b7f41db2730a516a32b`; selected record SHA-256 `6b61c10d8ce7fed398776d5f87e5c13a8accb2f91617447e6c9071e10e090265`.

- `hmh07-lua-follow1:236` (original lines 4954-4962): UpdatePositionDraftClients sorts and filters frontend lobby clients, fills up to five position models and recreates the ZM list; in-game it selects the team/caster counterpart, remaps splitscreen positions, has a four-client campaign ordering branch, and clears models only in its explicit absent-team arm. Preserve missing fallback writes and comparator/local-scope defects. UpdatePositionDraftCharacters counts team roles, hides arena roles and writes unavailable/playerName by exact per-role limit. ChooseSpecialistMidMatch guards existing overlay/demo/bounty, then installs parent/child close hooks to close/clear the stored overlay. Native character/UI delivery remains conditional.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00530` at JSON pointer ``; file SHA-256 `5aa0abaeb8ed1fb78cba607772195bb56e4255db55b4868b2bd03689661cda2b`.

- `hmh07-lua:134` (original lines 3352-3399, 3352-3399, 3403-3403, 3354-3354, 3352-3399, 3403-3403): Request GetPlaylists3354. The featured traversal3358-3371 is guarded by the IsMainMode(arg1, MP enum) request; that helper2957-2960 ignores its first argument and compares LobbyData.GetCurrentMenuTarget().mainmode with its second argument. Matching MP groups request Featured filters3362; preserve the exact accumulation behavior and its recorded card-builder limits. The ordinary traversal3377-3396 admits groups with hidden ~= true and then either a nil mode mapping or a display-name request result unequal to hash_0. It has no requested-mode equality test. CreateFilter3382 forwards the group lobbyMainMode and arg2; its source2428-2443 stores that mode in mainMode and forwards card construction. Only when the featured object is truthy and its cards length is positive are truthy ordinary cards assigned featured=false3383-3388. Nonempty ordinary groups are appended3390-3393, and the constructed list is returned3398. Exact playlist/mode/provider values, inherited card-builder defects, opaque native effects and original VM/build/runtime behavior remain unresolved.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00629` at JSON pointer ``; file SHA-256 `8a237c8fcceceef91ead96af15de02f0dda828c580a1a67e975aa2523ccf71d9`.

- `hmh07-lua-follow5:044` (original lines 3679-3679, 3677-3681, 3679-3679, 3677-3681, 3677-3681, 1557-1563, 1557-1563, 4225-4231, 4225-4231, 2157-2168, 2157-2168): Delegate arg0 to SetZMOfflineScreenStateToCustomGame, with no explicit return. This is an already selected shared UI edge, not a new Zombies investigation. Create an output list and get the current menu and playlist groups. Walk nonhidden groups whose mode is available (or has no EMode) and matches the menu mainmode. Walk entries; FEATURED accepts featured nonexcluded entries, PUBLIC accepts nonfeatured nonexcluded entries, ztutorial checks the first rotation gametype asset, and other nonnil tabs require a single excluded-public rotation, the zclassic difficulty condition and matching grouped gametype. Reject unavailable quickplay cards after those tests, append accepted entries, return the list. Data and first-rotation indexing remain unguarded.

  unknowns: {"provider_or_lexical": &#91;&#93;, "source_fidelity": &#91;&#93;, "original_build": "Recovered source is not matched to original PS4 bytecode/build; @0 is not a native address.", "VM_native": "Lua dialect, metatables, native/UI API execution, model dispatch/cancellation and input timing remain unverified.", "data_settings_assets": "Literal references do not supply effective model values, settings, data tables, localization or asset availability.", "server_service": "Online, stats, progression, marketing, lobby and backend behavior are unavailable service boundaries when requested by these exact bodies.", "runtime": "No game, console, account, router, save, native tool or independent review was run."}

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/3`.

  Archived evidence ID: `archived-record-00121` at JSON pointer ``; file SHA-256 `ac2b7a81426a0d72dedb5ceff7fa28618a9104781823bda62e5aba92df6645ae`; selected record SHA-256 `b365f70ce841f679ca834824f3653584f73546441c7d39ba5ff9d92aa0d4f5e7`.

- `hmh07-lua:138` (original lines 4087-4166, 4087-4166, 2485-2485, 4126-4126, 4139-4139, 3561-3578, 4105-4105, 4135-4135, 4154-4154, 4163-4163, 4130-4130, 4138-4138, 4087-4166, 2485-2485): Reads card model/mode/playlist and routes Live theater/valid-playlist/custom or LAN navigation. WZ valid-playlist path checks party count<=playlist maxPartySize before proceeding; existing target updates playlist/quickplay/saved selection and emits server-data-update for WZ, while a different target navigates. Arena is separate; CP/ZM branches retain mode gates. Recovered early model dereference and undefined theater/custom-arena target variables are explicit fidelity/lookup hazards, not corrected behavior. Native lobby transitions are not proved.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used.", "Selected recovered source has an explicit scope/control-flow/field assumption described in answer; original executable semantics are not guessed or repaired."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/4`.

  Archived evidence ID: `archived-record-00223` at JSON pointer ``; file SHA-256 `d4c980046a63f518e020a6f552ebd00fab45dba35aeebd9e659c1be5d002e567`.

- `hmh07-lua-follow1:010` (original lines 4469-4490, 4469-4490, 3048-3057, 3048-3057): Stopped Director constructs this child directly; its Arena name does not exclude construction. Builds map vote plus PC vote view, ready/blackmarket buttons, overhead names and arena event/progress views. MapVote model notifications update source state predicates; BlackMarket Hidden tests loot_enableBlackMarket while its action opens QuarterMaster and returns true. Ready model binds the exact cross button bits. IsPC state is a source predicate, not an inferred universal platform gate. Lobby client-data/character/lobbyNav callbacks update position-draft models only when ShowDirectorArenaMatchmaking(controller). Registers close, optional postload, initializes overhead names, returns self. The detailed conditional vote/callback contracts below do not prove arena gameplay or backend execution in HMH.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/5`.

  Archived evidence ID: `archived-record-00096` at JSON pointer ``; file SHA-256 `e6f7a611b40c536912c9d55fa7abdf162321fd9d6fa1d7303d21ce4bd461a4d0`; selected record SHA-256 `8dec324e716e484146d8de9ce7720fc3de05cb5ddf48cf7c0fc189dabeeca0b5`.

- `hmh07-lua:128` (original lines 2957-2960, 2957-2960, 2957-2960): Compares current-menu mainmode with argument2 and returns equality. Argument1 is unused; target is assumed nonnil.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/6`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/127`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `9bd4ba5c6b99240c592b8dc20c740a9d137f7a6e99ab158e3413b8188393ecb9`.

- `hmh07-lua:135` (original lines 3401-3423, 3401-3423, 3405-3416, 3411-3413, 3419-3421, 3426-3426, 3401-3423, 3426-3426): Resets Filters, obtains selected mode filters, and registers one DirectorCardList provider per filter. Each provider adds a private-client-update subscription once per list element, whose callback rebuilds that datasource, then returns CreateCardListDataSource. Arena registers an empty news provider. Closure delivery/capture/lifetime is retained in the source body; no server refresh is assumed.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/7`.

  Archived evidence ID: `archived-record-00630` at JSON pointer ``; file SHA-256 `5a72673ebd103d1b8548e582317a16590a2e670866df6ad642145539378a29df`.

- `hmh07-lua:141` (original lines 4469-4490, 4469-4490, 4469-4490): Creates lobbyRoot.publicLobby and resets stage INVALID, stageTitle hash_0, stageDetails empty, loaded fraction0, estimate35, elapsed0, start5, intermission votinginterval/1000 and waitingAnimation=false. There is no native matchmaking call or explicit return. These are local initialization defaults, not measured times or search results.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/8`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/140`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `ac6063303357e6f1e625e16f9f52c7990d73c287565d8b03d4240c8c7711a2ff`.

- `CoD.DirectorUtility.GetPlaylists` (original lines 1557-1563): No standalone body contract is available in this selected summary. Available classification: shared_Blackout_or_BO4.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/9`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/69`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `07323026fd47656791bd7f7ef228cf5c2ec267b8591e591b21513b4769f25907`.

- `hmh07-lua-follow6:124` (original lines 3683-3686, 3683-3686): Takes a game-type identifier and optional grouping selector. Calls Engine hash_1F2CD89B3C345FD3 on the identifier. If the selector is non-nil and differs from ztcm, returns that result's gametype. Otherwise calls Engine hash_48D4B2F88BB8D5E7 on that gametype and returns converttoxhash(groupName). Both returned objects are indexed without nil guards. This is only the selected conditional shared-source dependency; it authorizes no separate Zombies work. For the supplied controller, first resets game-type settings, creates/reads global lobbyRoot.selectedGameType, then iterates pairs(GameTypeTable). Collects names only from groupName zclassic; on a hash match to the current type it sets the found flag and breaks. If no match and at least one name was collected, calls SetGameType(controller, collected&#91;1&#93;); pairs ordering is not fixed by this source. Calls CreateOfflineScreenState, assigns its result to non-local f103_local3 and sets CUSTOM_GAME through that variable. Preserve the global write rather than adding local. No original settings, online behavior or separate Zombies work is established.

  unknowns: &#91;"Effective HMH settings/data/assets, true load/overwrite/class lookup order, original recovered-text fidelity, native callback delivery and service/server implementations remain open.", "Independent correctness review and final game tests remain deferred.", "f103_local3 assignment/use at1414..1415 is non-local. Preserve its exact global side effect. pairs order does not establish which first zclassic type is used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/10`.

  Archived evidence ID: `archived-record-00056` at JSON pointer `/units/123`; file SHA-256 `9b5470295d8bc5b945061358d29d8430f5da2392ccde6abf20deb11b8b9c027f`; selected record SHA-256 `e09340a050da8698ab6741fa1d3a22dbe91bcd180bb073e2c812c3b5005d98db`.

- `hmh07-lua:155` (original lines 4887-4891, 4887-4891, 4890-4890, 4893-4914, 4887-4891): Returns native readyup AND InReadyStage for current menu lobbytype and host/client module. This is a short-circuit value, not necessarily normalized; no ready-state mutation.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/11`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/154`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `add178b5663767aa5671deae7ae50dc4b12aa01fac904084120350a513057016`.

- `hmh07-lua-follow1:177` (original lines 4469-4490, 4976-4980, 4784-4799, 4271-4281, 4801-4808, 3037-3046, 3037-3046, 1059-1065, 2952-2955): Builds arena pregame after common lobby/draft/quickplay setup and Arena model preparation. Find-match is gated by party leadership, leaver lockout and client count; custom game, rank banner, arena-event buttons and host activity remain separate predicates/actions. Lobby and event model watchers update state/prompts/header/draft, with PC redirect navigation at the end. Arena naming does not settle original HMH membership; all branch-specific enum/settings/provider limits remain conditional.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/12`.

  Archived evidence ID: `archived-record-00171` at JSON pointer ``; file SHA-256 `77b3e773fc1b86268b7c213ab9d2de6e87d4eeae0781ebfbd53d2e91e02e29b2`; selected record SHA-256 `5a13eec58218e84af259a11196bc05fc88c333ef37706c55fc3b2300efa3b4e7`.

- `hmh07-lua:144` (original lines 4500-4502, 4500-4502, 4500-4502): Returns localization menu/timeremaining_s with the supplied value. No countdown update, rounding or runtime timer proof.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/13`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/143`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `76b0dae593b6933ce4f130bc49fdd17bc2ad40c0d90e7335ef0d096f8829925b`.

- `hmh07-lua-follow1:207` (original lines 4750-4758, 4504-4506, 946-969, 1005-1022, 991-1003, 971-989, 3669-3671, 3021-3030, 4948-4952): Builds the private director after clearing QuickPlay and updating draft models. It constructs shared header/readiness/playlist plus ZM pose/settings children, preserving unconditional recovered construction and explicit mode-specific state predicates. Playlist/network changes refresh distinct images/titles; spinner/client/lobby notifications conditionally run quickplay/draft/focus helpers. Close and optional PreLoadFunc precede PC/default-focus and solo-title setup. A WZ state slot does not make all ZM callbacks HMH-required.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/14`.

  Archived evidence ID: `archived-record-00091` at JSON pointer ``; file SHA-256 `a30f8555182e75a179c32e014284fc9252ec817ac254fa07121076b9f9f60d1e`; selected record SHA-256 `b34ad1fe171419e4422a8a5e769deb89909805b41243a35c2d33f4ae90127ea2`.

- `hmh07-lua-follow1:058` (original lines 1742-1748, 4750-4758, 4770-4778, 3216-3227, 5042-5049): Creates shared Director select screen with extra-home left/right filtered lists, featured playlists, mode list, safe-area/description and PC/Korea/tier-notification children. List callbacks refresh labels on lock/trial/lobby changes and descriptions on focus. Extra/mode trial-store branches containing AlwaysFalse are retained as inactive source predicates; unlocked/show-for-all/not-trial actions process the list and return true. Featured prioritizes trial store, unlocked action, missing-DLC overlay, ZM store, season-pass upsell and locked action. Mode locked action is PC-gated. Focus/lose-focus shows/hides tier notification. Safe-area menu_loaded sizes console and dispatches when unhandled. Korea event controls use exact active-event branches. State predicates distinguish live online demo/arena/default and LAN demo/arena/default. Close/postload precede pass-custom-function, UGC validation, WZ trial-video and PC redirect navigation setup. No effective playlist choice, store action, account state or native loader/runtime is asserted.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/15`.

  Archived evidence ID: `archived-record-00134` at JSON pointer ``; file SHA-256 `330362e6d7cecec92b0a68c59eacaf0e34ebedba0defd2c9c013ead274d52557`; selected record SHA-256 `62f2ac27c8417dc6be68fbf5a5a1eb6ee6b3f3e101a01cf619a0e8327c8cddf0`.

- `CoD.DirectorUtility.CreateCardListDataSource` (original lines 94-140): No standalone body contract is available in this selected summary. Available classification: shared_Blackout_or_BO4.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/16`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/70`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `95423392307d23cb34b9fe3faa0c86d97c1163993031d0f742f80c78347fc97e`.

- `CoD.DirectorUtility.SetupDirectorFiltersCards` (original lines 3425-3427): No standalone body contract is available in this selected summary. Available classification: shared_Blackout_or_BO4.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/17`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/75`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `4a1144bdfd2ed217c84f466e8e3057abacfb4964162005d88f8126c5fac00f42`.

- `hmh07-lua-follow3:149` (original lines 3645-3645, 3645-3645, 3645-3645): For CoD.RankUtility.GetRankCap, evaluate the displayed formal inputs and captured values. Its exact paths are 16: if not f1_arg0 then; 19: return Engine&#91;@"getrankcap"&#93;( f1_arg0 ). Its writes/requests begin 17: f1_arg0 = Engine&#91;@"currentsessionmode"&#93;(). The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior. For CoD.RankUtility.ForceStreamRankIcons, evaluate the displayed formal inputs and captured values. Its exact paths are 34: if not (f3_arg0 ~= Enum&#91;@"emodes"&#93;&#91;@"mode_invalid"&#93; or not LuaUtils.OnlineOnlyDemo()) or LuaUtils.OfflineOnlyDemo() then; 38: if LuaUtils.GetDisplayNameForEMode( f3_arg0 ) ~= @"hash_0" then; 40: if f3_local1 then; 41: for f3_local5, f3_local6 in ipairs( f3_local1 ) do. Its writes/requests begin 35: f3_arg0 = Enum&#91;@"emodes"&#93;&#91;@"mode_multiplayer"&#93;; 42: f3_local0&#91;f3_local6&#93; = true; 46: CoD.RankUtility.ForceStreamedRankIcons = CoD.BaseUtility.ForceStreamHelper( CoD.RankUtility.ForceStreamedRankIcons, f3_local0 ). The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior.

  unknowns: &#91;"Original source-to-PS4/VM/native/loader identity and bytecode fidelity are unverified.", "Effective settings, assets/tables/model schemas, server/service implementation and callback delivery/lifetime are unverified.", "Exact source request semantics do not prove rendering, networking, persistence, progression or game behavior.", "Public reuse is the frozen manager audit only; no worker web/repository discovery was performed."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/18`.

  Archived evidence ID: `archived-record-00003` at JSON pointer `/units/148`; file SHA-256 `a63852530df9189721a410c240a42967af6648aa0fca4e70325b17a1e677ebb7`; selected record SHA-256 `2864363d47b5ff5f437dd241a30e5606b81a23c6047c2a6ec8e7e81a0914e26a`.

- `hmh07-lua-follow1:098` (original lines 2957-2960, 2957-2960): Builds StartMenu_Main, initializes data and absent WZ-start/draft models, panels/tab frame/safe area/PC quit/Korea descriptors. TabWidget model changes changeFrameWidget only when nonnil. State order is frontend, zombies, campaign, WZ in-game, generic in-game. Menu-loaded delegates local/super, plays entry, fetches fileshare slots and sets heading; close-all/migration go back. PC WZ occlusion closes splitter. Circle/back branches preserve frontend cleanup, console/PC and demo resume paths; Triangle/weapnext/weapprev and PC slot bindings use exact WZ/in-game/non-demo gates; F1 class action is AlwaysFalse; Start always refreshes/goes back; square stats filter, PC contextual quit and PC start-Warzone remain individually guarded. Label callbacks can return false for working actions. Close first-hook clears saved state; spectator changes refresh tabs. menu_loaded/state restoration precedes same-class close hook/postload, optional MP class-slideout and safe-area sizing, then returns self. No quit/weapon request was executed during this work.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/19`.

  Archived evidence ID: `archived-record-00155` at JSON pointer ``; file SHA-256 `cd1fa3f4247464fcba144bac4797828cfe9de5c9b4183ac87fa5137b44f6100d`; selected record SHA-256 `043bd05a037263640608edf72edda482a0ed4c212dd6cf6c23b6d2311c4433c4`.

- `hmh07-lua:137` (original lines 3673-3675, 3673-3675, 3674-3674, 3673-3675): Evaluates CoD.ZombieUtility and CoD.ZombieUtility.IsZMOfflineScreenStateCustomGame() or false in that order. A missing/false table skips the helper and returns false. A truthy table calls the helper; a truthy helper result is returned unchanged, while a nil or false result becomes false. Table existence is the source gate; it does not prove HMH custom-game state, and helper internals stay outside scope.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/20`.

  Archived evidence ID: `archived-record-00123` at JSON pointer ``; file SHA-256 `55dc992dafdb1272bf80255c6cea6258e3dd19a657650d0b6e33b9aa190b23c8`; selected record SHA-256 `54bd1610e40a45ac741b49b9575496f209549954c4afe54b15731691401efc38`.

- `hmh07-lua-follow1:056` (original lines 5038-5038, 5038-5038, 5038-5038, 5037-5040): IsShoutcaster returns true for demo-shoutcaster, or outside demo when model truth (default true if absent) and spectator-team/native shoutcaster hold; otherwise false. ExeProfileVarBool requires existing common profile/key with get()==1. VectorComponent parses string components with bounds1..count, otherwise only index1 returns original scalar, else0. SafeGetModelValue preserves short-circuit false/nil rather than normalizing. GetScriptNotifyData fetches numArgs, creates table only when positive, but the numeric for-loop still uses numArgs unguarded; absent count can fail and zero returns nil. Each argument is read via SafeGetModelValue and table.insert, so absent values are not assigned a synthetic placeholder. No VM/native/provider semantics are repaired.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/21`.

  Archived evidence ID: `archived-record-00036` at JSON pointer `/units/55`; file SHA-256 `279ba12c6a1d4cfd1fb6c7e030a47694d4ee3982256bb21a0b3aa6909aef143b`; selected record SHA-256 `db57867b670b20da9813f48d2c5a00456bdc9dd75340aa1c604f3c1fa9c94197`.

- `hmh07-lua-follow4:129` (original lines 1750-1760, 1813-1813, 1750-1760, 3070-3080, 3070-3080, 3677-3681, 3677-3681, 4225-4231, 4225-4231, 4614-4627, 4614-4627, 4614-4627, 4614-4627, 4629-4633, 4629-4633, 4629-4633, 4629-4633, 5491-5493, 5491-5493, 5495-5497, 5495-5497, 1750-1760, 1813-1813, 1750-1760, 3070-3080, 3070-3080, 3677-3681, 3677-3681, 4225-4231, 4225-4231, 4614-4627, 4614-4627, 4614-4627, 4614-4627, 4629-4633, 4629-4633, 4629-4633, 4629-4633, 5491-5493, 5491-5493, 5495-5497, 5495-5497, 1750-1760, 1750-1760, 1750-1760, 1750-1760, 3070-3080, 3070-3080, 3070-3080, 3677-3681, 4225-4231, 4225-4231, 4614-4627, 4614-4627, 4614-4627, 1813-1813, 1750-1760, 3070-3080, 3677-3681, 4225-4231, 4614-4627, 4614-4627, 4614-4627, 4629-4633, 4629-4633, 4629-4633, 5491-5493, 5495-5497, 946-969, 971-989, 991-1003, 1005-1022, 1315-1322, 1557-1563, 1612-1732, 1742-1748, 2192-2219, 2221-2231, 2699-2707, 2952-2955, 3216-3227, 3320-3326, 3328-3350, 3503-3534, 3536-3548, 3642-3650, 3653-3659, 3661-3667, 3669-3671, 3710-3727, 3729-3740, 4237-4239, 4271-4281, 4327-4330, 4332-4335, 4504-4506, 4740-4748, 4750-4758, 4770-4778, 4824-4829, 4948-4952, 4954-4962, 4976-4980, 5042-5049, 5067-5073, 5075-5081, 5148-5158, 5171-5180, 917-932, 934-944, 1024-1039, 1806-1818, 2170-2190, 3186-3214, 3229-3248, 3429-3442, 3630-3640, 4216-4223, 4856-4867, 4916-4922, 5144-5146, 1753-1753, 1755-1755, 3071-3071, 3059-3068, 3073-3073, 2957-2960, 3074-3074, 3021-3030, 3679-3679, 1755-1755, 4229-4229, 5492-5492, 5496-5496, 4226-4226, 4623-4623, 4630-4630, 1750-1760, 3070-3080, 3677-3681, 4225-4231, 4614-4627, 4629-4633, 5491-5493, 5495-5497, 1750-1760, 3070-3080, 3677-3681, 4225-4231, 4614-4627, 4629-4633, 5491-5493, 5495-5497): Returns false for a non-arena entry; true for the disabling dvar or non-LAN without an arena season; otherwise false. This is a menu gate, not a whole-mode relevance exclusion. Starts with IsMatchmakingInProgress. Only while true does it check the main mode: Warzone forces false, other modes use not ShowDirectorPrivate(nil,controller). Returns the resulting value. Calls ZombieUtility.ZMOfflineNavigateToCustomGames with the second argument only when the ZombieUtility table exists. The actual call is preserved as a shared helper boundary, not authoring unrelated-mode internals. If either hashed engine predicate is true, only mode_warzone is available. Otherwise availability means GetDisplayNameForEMode is not hash_0. Traverses the supplied widget model→info get value→selectedCharacterType. When that child exists, requests update_frozen_moment_character with its index get value; absent links do nothing. Requests update_frozen_moment_character for the supplied controller with literal index=-1. Receiver delivery and presentation assets are external. Returns whether GetBOPassTierBoost(controller) differs from numeric zero; it does not grant or fetch entitlement itself. Returns whether GetBOPassPartyTierBoost(controller) differs from numeric zero.

  unknowns: &#91;{"kind": "original_build", "gap": "Recovered-source revision is pinned; original PS4 build/byte/VM/native binding remains unverified."}, {"kind": "effective_data_settings_assets", "gap": "Engine/model/Dvar/asset/data requests do not supply effective runtime values, contents or ownership."}, {"kind": "server_service_persistence", "gap": "Unavailable authoritative server/service/provider code and successful persistence remain unavailable; not reconstructed or counted as completed."}, {"kind": "runtime_callback_lifetime", "gap": "Original loading, table overwrites, callback delivery/order, timings, state selection and UI cleanup are not runtime-proven."}&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/22`.

  Archived evidence ID: `archived-record-00004` at JSON pointer `/units/128`; file SHA-256 `52df95eaa9f17f90427f6313acbc648c9bdffa0602f6444566bbe8fa1a54ba59`; selected record SHA-256 `99ab6ce6be279d06bc44edb140fd1fa7de860ecc3eff40f298e73dd434a687e2`.

- `hmh07-lua:158` (original lines 5037-5040, 5037-5040, 5038-5038, 5037-5040): Safely reads the supplied model key, then returns value AND opaque native bot-XUID predicate. Missing/false value propagates; no identity classification beyond that native call is assumed.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/23`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/157`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `d23cfe093398b9e1f7a875c66b0a047e45b318f3e5514b1d1f0ff28a47787b48`.

- `hmh07-lua-follow4:140` (original lines 3239-3239, 3237-3237, 3239-3239, 3237-3237, 3239-3239, 3237-3237): Returns featured_levenabled when that dvar exists; otherwise true. Reads stream from LiveEventViewer using SafeGetModelValue and returns stream and stream~=empty string. The result may be nil/falsy rather than a normalized Boolean.

  unknowns: &#91;{"kind": "original_build", "gap": "Recovered-source revision is pinned; original PS4 build/byte/VM/native binding remains unverified."}, {"kind": "effective_data_settings_assets", "gap": "Engine/model/Dvar/asset/data requests do not supply effective runtime values, contents or ownership."}, {"kind": "server_service_persistence", "gap": "Unavailable authoritative server/service/provider code and successful persistence remain unavailable; not reconstructed or counted as completed."}, {"kind": "runtime_callback_lifetime", "gap": "Original loading, table overwrites, callback delivery/order, timings, state selection and UI cleanup are not runtime-proven."}&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/24`.

  Archived evidence ID: `archived-record-00710` at JSON pointer ``; file SHA-256 `b7810b1a59ac82a919e3a6e8e13d94c0eb836363c92740392ef3d5434634d312`.

- `hmh07-lua:125` (original lines 2287-2294, 2287-2294, 2287-2294): Creates/reads lobbyRoot.lobbyMainMode, then calls OpenOverlay with requested overlay/controller/menu and properties _mainMode plus mapped _sessionMode. It does not return the overlay. Model validity and loaded menu mapping remain assumptions.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/25`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/124`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `8405cf86784d82e9d3bcf2601f216a755d5107008c233be3f218e0c9bfe3b096`.

- `hmh07-lua-follow1:114` (original lines 2551-2551, 2551-2551, 2551-2551, 2480-2678): Map getters hash name and return nonnil table field (localized in localized getter), otherwise caller default. AllMembersHaveDLCMask scans clients in ipairs order; optional MP dvar branch checks native aggregate mask/override flag, then checks each present dlcBits mask with MP override exception; returns false on first failing check and true after all, including empty list. IsDLCMapFromName returns false for dev/original indices; otherwise returns short-circuit truth of retrieved pack and true, retaining nil/false when input/pack absent. No entitlement or backend truth is inferred.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/26`.

  Archived evidence ID: `archived-record-00036` at JSON pointer `/units/113`; file SHA-256 `279ba12c6a1d4cfd1fb6c7e030a47694d4ee3982256bb21a0b3aa6909aef143b`; selected record SHA-256 `a1a48f8320aea8aa02a8c2bbeb87bd2b922285976e754109fdcb7cdc74287346`.

- `hmh07-lua-follow1:042` (original lines 4824-4829, 4504-4506, 4750-4758, 2699-2707, 2287-2294, 2287-2294, 1059-1065, 1059-1065, 3673-3675, 3673-3675, 4831-4833, 4831-4833, 3012-3019, 3012-3019): Stopped Director constructs this shared custom lobby child. Initializes selected gametype/map/update/player-count and local ZM models, builds party/map/setup/start/header/preview/lab controls. Map selection requires host and no countdown; offline-ZM-private opens a different chooser, otherwise generic map/game chooser. Host Start launches only if every client owns DLC, else opens maps-not-enabled popup; both action branches return true while label callbacks return false. CustomGames action chooses ZM custom mutation or non-ZM custom-games overlay. State family preserves ZM live/LAN/host/offline predicates, WZ IsWarzone, and PC variant. Model/session/focus callbacks refresh state/labels/descriptions/draft models; the repeated ShowDirectorCustom elseif is retained literally. LobbyNav focus changes prioritize ZM custom host tutorial, then custom host StartButton, then ZM custom nonhost home. Close registration/postload precede platform-specific preGameType and default-focus update. Every nested function/return/guard remains below; no ZM-only gameplay or real launch is claimed.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/27`.

  Archived evidence ID: `archived-record-00094` at JSON pointer ``; file SHA-256 `b7bc897872c9d1f0e13fa377f6ce9790d674551ff1a9a1e06a12be723cb2014c`; selected record SHA-256 `1869abf568bc2ec05339bbeeab4867bfc96dae74546e4ecc60186659eb44c367`.

- `hmh07-lua:123` (original lines 900-915, 900-915, 900-915): Outside Live or without playlist info returns blacktransparent. Otherwise returns imageTileSideInfo, else imageBackground, else blacktransparent. No asset availability or original native playlist-data guarantee.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/28`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/122`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `bf1274b2d47bf1536b6fdacf4f24d86b8b430dd7b904c1e4d9a6507f94c5b8c9`.

- `hmh07-lua:143` (original lines 4496-4498, 4496-4498, 4496-4498): Returns localization of hash_2498E6569F77AEBA with the supplied elapsed value. Formatting/units are native localization inputs, not verified measurements.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/29`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/142`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `b531de33a952408459dea78595d47cff90b4705d91631b700cc9ca9189478aac`.

- `hmh07-lua:060` (original lines 105-105, 105-105): Looks up LobbyMainModeData&#91;input&#93; and forwards its eMode, or nil, into GetDisplayNameForEMode. It returns that helper result. The selected helper's recovered-scope issue is inherited as a dependency; this wrapper does not repair it.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/30`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/59`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `9afc6db3f961b4f3c6d2d5d3a6cc263be3c80e04256b5f4f8ec3d242986a8544`.

- `hmh07-lua:059` (original lines 3381-3381, 3381-3381): Returns hash_0 for a disabled Warzone/Zombies/MP mode. Recovered text then declares table/name locals only inside an elseif block but refers to them after the block; it also dereferences EModeData&#91;input&#93; before guarding the entry. Preserve the lexical-scope/decompiler-fidelity defect and conditional failure rather than silently rewriting an intended lookup.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used.", "Selected recovered source has an explicit scope/control-flow/field assumption described in answer; original executable semantics are not guessed or repaired."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/31`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/58`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `1477094fcedb5701488c3d771b52a3015bc6b6aae00a93f6daa7c223544280b1`.

- `hmh07-lua-follow12:001` (original lines 3814-3814, 5038-5038, 5038-5038, 5037-5040, 3814-3814): Parse a3-value color, preserve literal whole-vector multiplication by0 when any channel>1, and return a fresh r/g/b table.

  unknowns: &#91;"Conditional exact recovered Lua source only. No original loader/global overwrite/class/metatable/VM/native/model/data/settings/assets/service/server/PS4 proof, independent review, acceptance, function completion or runtime credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/32`.

  Archived evidence ID: `archived-record-00050` at JSON pointer `/units/0`; file SHA-256 `05636d274435ca2d7bd16f6843fff25c77b43c0e3ae89869b99037291a2835ad`; selected record SHA-256 `59f1a1c316928fabdad0193c7c7d8a843460eed5edafbb3e6eace677abadd747`.

- `hmh07-lua-follow4:244` (original lines 4939-4946): Constructs CoD.DirectorFeaturedAccentCarousel.new with the exact receiver/menu/controller/layout arguments below. Creates self as LUI.UIHorizontalList.new, LB as CoD.BumperButtonWithKeyMouseText.new, LeftArrow as CoD.BumperButtonWithKeyMouse.new, PipsGrid as LUI.GridLayout.new, RightArrow as CoD.BumperButtonWithKeyMouse.new, RB as CoD.BumperButtonWithKeyMouseText.new. Stores source state predicates in order Gamepad, Gamepad, Invisible, ShowTriggers. Owns 17 nested callable scopes, each with its separate delivery/invocation contract. Registers LUI.OverrideFunction_CallOriginalSecond( self, "close", self.__onClose ). Runs PostLoadFunc( self, f1_arg1, f1_arg0 ) only under its exact guard and at its original source position. All property/asset/model/state/navigation/return effects remain in the ordered statement contract; construction and storing callbacks do not prove the original game displays or loads this widget.

  unknowns: &#91;{"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "self:setAlignment", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 13, "line_end": 13, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "64286cac8e4c434661eeb7a0817716d710274ada5336ccadfcc6196419eec2ee", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tself:setAlignment( LUI.Alignment.Center )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "self:setClass", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 14, "line_end": 14, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "7dfa8d245dff8fdd16b990ba0b773bf4afca78e10990cbfe0b2f2dfd97cbf336", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tself:setClass( CoD.DirectorFeaturedAccentCarousel )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "f1_arg0:addElementToPendingUpdateStateList", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 19, "line_end": 19, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "425e1262ec83d277f60ab9e68572fad43783709fae6c81dcf3c6d19d52731d76", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tf1_arg0:addElementToPendingUpdateStateList( self )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "CoD.BumperButtonWithKeyMouseText.new", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 21, "line_end": 21, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "5a463f6c5b39aa5efe4d8b94b0cd5718186d78273137aa1f040c5761fc1e473f", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tlocal LB = CoD.BumperButtonWithKeyMouseText.new( f1_arg0, f1_arg1, 0, 0, -161, 39, 0, 0, 0, 34 )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "LB:setRGB", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 22, "line_end": 22, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "873bbec61a44fa7a750099893c8126949322df40f265329cad5344388b2ffe7e", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tLB:setRGB( 0.66, 0.63, 0.52 )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "LB:setAlpha", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 23, "line_end": 23, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "c439792b2afe5aa42cc8f3e23ff8330c684cdc7d8918a5595bfc341dc37e2f8b", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tLB:setAlpha( 0.45 )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "LB.GamepadPrompt:setText", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 24, "line_end": 24, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "89a96663d6266b087ff3a8aec775c4a7cfb3f9ae10f68e6e2c56e38abc9febec", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tLB.GamepadPrompt:setText( Engine&#91;@\"hash_4F9F1239CFD921FE\"&#93;( @\"hash_5BDCD5292604F434\" ) )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "LB.GamepadPrompt:setAlignment", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 25, "line_end": 25, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "55dab31d1ec3e4c85f292635dfd95834944b419c22fc0c0cabefa5a26066f755", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tLB.GamepadPrompt:setAlignment( Enum&#91;@\"luialignment\"&#93;&#91;@\"lui_alignment_right\"&#93; )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "self:addElement", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 26, "line_end": 26, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "68f0d7837fe072d07219506243abd44fdf368b80b04316a661d3bdda8f835828", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tself:addElement( LB )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "CoD.BumperButtonWithKeyMouse.new", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 31, "line_end": 31, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "55c4e19131e106769e71f860409d9f8096d8bb5d0e3b7a6dfff5139728f59fa5", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tLeftArrow = CoD.BumperButtonWithKeyMouse.new( f1_arg0, f1_arg1, 0.5, 0.5, -251.5, -184.5, 0, 0, -4, 41 )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "LeftArrow:mergeStateConditions", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 32, "line_end": 32, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "802a24be1a48b6561bf55a3c8ebb39bbc78e76e3309e43a4d7c0e3c4a9c6f9c1", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tLeftArrow:mergeStateConditions( {", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "LeftArrow:appendEventHandler", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 40, "line_end": 40, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "8c5ac0a6d6e985b77f035d61297ae9029d3e5e6ff12fb0c8a6ce9d9c55f406b4", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tLeftArrow:appendEventHandler( \"input_source_changed\", function ( f3_arg0, f3_arg1 )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "f1_arg0:updateElementState", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 42, "line_end": 42, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "254c8cd20319d6fa314010437cb30435eb6ef854c3c24a2d57cafe0d75f2d76b", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\t\tf1_arg0:updateElementState( LeftArrow, f3_arg1 )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:40-43", "scope_role": "registered_callback", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "PipsGrid", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 47, "line_end": 47, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "3bee31ccb77e4d2529fca8b774b57432e408a396d66fcbf23c7e6f1955ba7b46", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tPipsGrid( RightArrow, RB.LastInput, function ( f4_arg0 )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "f1_arg0:updateElementState", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 48, "line_end": 48, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "2a4120b8e39a59702c30872efb20ead4aa5079087ccda5c2f72ded1b3a13f6ae", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\t\tf1_arg0:updateElementState( LeftArrow, {", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:47-55", "scope_role": "passed_callable_or_aliased_registration", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "f4_arg0:get", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 52, "line_end": 52, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "ef63085bebb8eb5834784febbdc151474c9c9ca95f8d88c255c837489e81572a", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\t\t\tmodelValue = f4_arg0:get(),", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:47-55", "scope_role": "passed_callable_or_aliased_registration", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "LeftArrow:setZRot", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 56, "line_end": 56, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "c49d44edbb660233bf0eb18ab46526e611e438b4def064cbefcd16ab4abe977b", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tLeftArrow:setZRot( 180 )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "LeftArrow.KeyMouseImage:setImage", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 57, "line_end": 57, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "3cd08d66e470f30b82a035adf20c5e6a91465c7db031f2b9b8fe670e57aa9c4c", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tLeftArrow.KeyMouseImage:setImage( RegisterImage( @\"uie_optionswidgets_arrow\" ) )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "LeftArrow.ControllerImage:setImage", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 58, "line_end": 58, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "87a95c83fa03e6023006b1dc42a733faf560651abe25e5fe877f994f4a8962a2", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tLeftArrow.ControllerImage:setImage( RegisterImage( @\"uie_optionswidgets_arrow\" ) )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "LeftArrow:registerEventHandler", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 59, "line_end": 59, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "f900ff73dc413b045a9f4c56e758a9bdff9919def37770fa2c905c97444b53db", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tLeftArrow:registerEventHandler( \"gain_focus\", function ( element, event )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "element:gainFocus", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 62, "line_end": 62, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "efd4706bf6a135c1e93f2edc0c44f69fcba25c2cfd7d95e2a181c5ebeceb7b35", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\t\t\tf5_local0 = element:gainFocus( event )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:59-68", "scope_role": "registered_callback", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "element.super:gainFocus", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 64, "line_end": 64, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "2d9166a92f5627dcc4acecfc30c86678b5f6e3926de8632bd8012d0e359df419", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\t\t\tf5_local0 = element.super:gainFocus( event )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:59-68", "scope_role": "registered_callback", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "f1_arg0:AddButtonCallbackFunction", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 69, "line_end": 69, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "5b0602f897c0e5ba1b841c05afc2cf5164763bc83c733d5c7508cbfa773eb7bb", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tf1_arg0:AddButtonCallbackFunction( LeftArrow, f1_arg1, Enum&#91;@\"luibutton\"&#93;&#91;@\"lui_key_none\"&#93;, \"MOUSE1\", function ( element, menu, controller, model )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "self:addElement", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 76, "line_end": 76, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "90ade20f48ad2c930ba0d26969078db991e8f1565d0e3cd46255f1bac37a7cd3", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tself:addElement( LeftArrow )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "PipsGrid:setLeftRight", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 80, "line_end": 80, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "3a610bc5b23790d73729290023b0a44f239ea6cd0e9aaa2f45877a08855a996f", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tPipsGrid:setLeftRight( 0, 0, 106, 475 )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "PipsGrid:setTopBottom", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 81, "line_end": 81, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "aef52ef18bba28b23c935edf73f3d12f2bbfffeee7f4174d4946eb01eaf06b39", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tPipsGrid:setTopBottom( 0, 0, 8, 30 )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "PipsGrid:setWidgetType", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 82, "line_end": 82, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "49edd6f5db086cc02049c71ba0af55469da7e1f86d4eef1f922da1aeee10f659", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tPipsGrid:setWidgetType( CoD.DirectorFeaturedPip )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "PipsGrid:setHorizontalCount", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 83, "line_end": 83, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "05a56d207ed656e8998eec1af751feaf6c454e9f4ae38b1468aedab878738dd0", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tPipsGrid:setHorizontalCount( 10 )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "PipsGrid:setSpacing", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 84, "line_end": 84, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "25c90437bed2b1f7e13847530146270f1f567e6a21dd61146131de0fb77870fd", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tPipsGrid:setSpacing( -19 )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "PipsGrid:setAlignment", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 85, "line_end": 85, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "2cfcad4634247162732d82c469b9f298133ac01fb6e4daedb9cdcde28b7d6d3e", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tPipsGrid:setAlignment( Enum&#91;@\"luialignment\"&#93;&#91;@\"lui_alignment_left\"&#93; )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "PipsGrid:setDataSource", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 86, "line_end": 86, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "72078e33d5a6666fbaf9477e6a6ebead46ec7a7a6659fbf49b57e5364c72ec8f", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tPipsGrid:setDataSource( \"DirectorHomeButtons\" )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "PipsGrid:registerEventHandler", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 87, "line_end": 87, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "a308dcb6db2867bd1b664bbbb190dfcfc2b88399b1a398ba9bfaa38ee6817f05", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tPipsGrid:registerEventHandler( \"list_active_changed\", function ( element, event )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "self:addElement", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 92, "line_end": 92, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "61413288df7af4ecaa81d3a09b025375c06d49d4d93b45ba65c5601718f2a64a", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tself:addElement( PipsGrid )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "CoD.BumperButtonWithKeyMouse.new", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 97, "line_end": 97, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "f992ecfa378cee68cf5bf17acaeca97804b08e12000d23a7b2aae3a8909a3b8e", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tRightArrow = CoD.BumperButtonWithKeyMouse.new( f1_arg0, f1_arg1, 0.5, 0.5, 184.5, 251.5, 0, 0, -4, 41 )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "RightArrow:mergeStateConditions", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 98, "line_end": 98, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "8a8b2292fc4ad5110446966b48d2cfe3224c055a0bf60e82d0ba22efd57b3684", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tRightArrow:mergeStateConditions( {", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "RightArrow:appendEventHandler", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 106, "line_end": 106, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "676a89bcaf5b801e2d2f465b6d0b758f35926a01f3d9853318f45314232ea83d", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tRightArrow:appendEventHandler( \"input_source_changed\", function ( f10_arg0, f10_arg1 )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "f1_arg0:updateElementState", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 108, "line_end": 108, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "fbbd6f23c61f243bcc6c3ab906a3d9f1adf7843dee4ab6eb7a02724dd61c92e5", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\t\tf1_arg0:updateElementState( RightArrow, f10_arg1 )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:106-109", "scope_role": "registered_callback", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "RB", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 113, "line_end": 113, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "fd5edec6e15f69bb35ee272b31dc321557d83ac22c39a74ec07681b28278c5c7", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tRB( f1_local6, f1_local7.LastInput, function ( f11_arg0 )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "f1_arg0:updateElementState", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 114, "line_end": 114, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "570342ebf9e675cf07359eebfdc0c3c860a3129402f1e369eb618fb099785d25", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\t\tf1_arg0:updateElementState( RightArrow, {", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:113-121", "scope_role": "passed_callable_or_aliased_registration", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "f11_arg0:get", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 118, "line_end": 118, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "d3802ccd3cc10b03f4112867516e7c17a88886c0770fd79e0a4963bff392b5f3", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\t\t\tmodelValue = f11_arg0:get(),", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:113-121", "scope_role": "passed_callable_or_aliased_registration", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "RightArrow.KeyMouseImage:setImage", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 122, "line_end": 122, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "cebb8b40d9d67d38d002ede0ecd8ab0a92e78a52b6f8d57b157a11c47b540a4c", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tRightArrow.KeyMouseImage:setImage( RegisterImage( @\"uie_optionswidgets_arrow\" ) )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "RightArrow.ControllerImage:setImage", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 123, "line_end": 123, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "240df0d0807df7bae3ca6e84e9e88f7f062216ae22a5f3e4e43137157ae99fb9", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tRightArrow.ControllerImage:setImage( RegisterImage( @\"uie_optionswidgets_arrow\" ) )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "RightArrow:registerEventHandler", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 124, "line_end": 124, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "5e54da746409dfd45ceb75f6e4ef9b079a89175503b21eda78abb717412bc48d", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tRightArrow:registerEventHandler( \"gain_focus\", function ( element, event )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "element:gainFocus", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 127, "line_end": 127, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "4f358e74c08731337b5c0e2f8ac3c996e4b22e1373db145a2649a73843c937a7", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\t\t\tf12_local0 = element:gainFocus( event )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:124-133", "scope_role": "registered_callback", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "element.super:gainFocus", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 129, "line_end": 129, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "f326020122515af9e04b3543206b11d69726141cafbc457e8cae7ffb5c562d5c", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\t\t\tf12_local0 = element.super:gainFocus( event )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:124-133", "scope_role": "registered_callback", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "f1_arg0:AddButtonCallbackFunction", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 134, "line_end": 134, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "9e8288b1b43741a52ceb02a47cfc29230727c44c9d2b1d5ccf836c87316c6083", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tf1_arg0:AddButtonCallbackFunction( RightArrow, f1_arg1, Enum&#91;@\"luibutton\"&#93;&#91;@\"lui_key_none\"&#93;, \"MOUSE1\", function ( element, menu, controller, model )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "self:addElement", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 141, "line_end": 141, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "d3d330d0b918a68cbff085fc6cb08d7a998753cc4cc85f50a53f1291ac3e958a", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tself:addElement( RightArrow )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "CoD.BumperButtonWithKeyMouseText.new", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 144, "line_end": 144, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "c15162382289efa4d024913fcab91bf55cc44af90d6caa136b35945120b20f92", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tRB = CoD.BumperButtonWithKeyMouseText.new( f1_arg0, f1_arg1, 0, 0, 542, 742, 0, 0, 0, 34 )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "RB:setRGB", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 145, "line_end": 145, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "f7a25c4e89a79d713163a7f2725f3a2f50cd5c549fb39702bddd1187dbab388a", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tRB:setRGB( 0.66, 0.63, 0.52 )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "RB:setAlpha", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 146, "line_end": 146, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "046b7468a20eb17af6e6e7ea018553de24d309b4d4d6ad29a933266879fea8f3", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tRB:setAlpha( 0.45 )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "RB.GamepadPrompt:setText", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 147, "line_end": 147, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "4b5ca570e45626e9656dc8c9351839ff57ca7943015b0a515929faaf9d0f70e7", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tRB.GamepadPrompt:setText( Engine&#91;@\"hash_4F9F1239CFD921FE\"&#93;( @\"hash_5BFED5292621DA9A\" ) )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "self:addElement", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 148, "line_end": 148, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "9a94149c94a7617871dc7c9440932d90d2ee24b398d0e36372c594267f257b8d", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tself:addElement( RB )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "self:mergeStateConditions", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 151, "line_end": 151, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "f80e120986602aa448c1707f3e91220ab2b7f14cf0f0242f97e8bd05ffce2459", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tself:mergeStateConditions( {", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "self:appendEventHandler", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 165, "line_end": 165, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "baa2a784dc94e83674a95f5f96f0ffca0007c4817873eca48d33cd8a0b78b4bf", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tself:appendEventHandler( \"input_source_changed\", function ( f17_arg0, f17_arg1 )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "f1_arg0:updateElementState", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 167, "line_end": 167, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "3dea055b2fe7501733aa5007853f761b889f12d37ec915124c543fbe0b72e502", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\t\tf1_arg0:updateElementState( self, f17_arg1 )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:165-168", "scope_role": "registered_callback", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "f1_local6", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 172, "line_end": 172, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "4de05cc1ea9119c42da375c3abcafcfec985aa2ce0eb40a643160e0ace08ceb5", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\tf1_local6( f1_local7, f1_local8.LastInput, function ( f18_arg0 )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "f1_arg0:updateElementState", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 173, "line_end": 173, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "5e650146f503c88e98185e993fb212fe193eb1daf81d6d0ae92b22ae0938a741", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\t\tf1_arg0:updateElementState( self, {", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:172-180", "scope_role": "passed_callable_or_aliased_registration", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "f18_arg0:get", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 177, "line_end": 177, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "ad96a49ba13ea095b122fe147ae02f67b0d404bcfa7e49e472d616dc78547087", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\t\t\tmodelValue = f18_arg0:get(),", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:172-180", "scope_role": "passed_callable_or_aliased_registration", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}, {"unit_id": "hmh07-lua-follow4:244", "source_symbol": "CoD.DirectorFeaturedAccentCarousel.new", "symbol": "PostLoadFunc", "caller_citation": {"area": "references", "path": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua", "line_start": 190, "line_end": 190, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "54ad2dba345df4d50b1222f41411a38c3e21d760c20e01814f00205e3442b515", "line_span_sha256": "4dbef5997b3a65062e8c8bbfb97d55f505c5f9f18c20af45a45813d428535171", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "statement": "\t\tPostLoadFunc( self, f1_arg1, f1_arg0 )", "scope_id": "lua/ui/uieditor/widgets/director/directorfeaturedaccentcarousel.lua:11-203", "scope_role": "selected_callable", "classification": "NEED_CONTEXT", "missing": "Need exact receiver/lexical alias/dynamic datasource key/export/native registration or source declaration. Generic method or other-file local name is not provider proof.", "target_semantics_authored": false}&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/33`.

  Archived evidence ID: `archived-record-00215` at JSON pointer ``; file SHA-256 `119110dfadd20c99097211812c37ab2bf4ff7d38b5eb18f432910418e87bd253`.

- `hmh07-lua:154` (original lines 4875-4885, 4875-4885, 4880-4880, 4893-4914, 4875-4885): Returns false if native readyup is truthy; otherwise returns InReadyStage(controller). Uses the current menu lobbytype and host/client query module. Source does not enforce party/DLC constraints; callers add them.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/34`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/153`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `8ac3dfae8af44170c6c633e122de9911cdaec13e44aae78ac13c488d5032f36e`.

- `hmh07-lua-follow1:083` (original lines 2990-2999, 2990-2999): Preserve recovered DoubleXP functions with empty negative branches and fallthrough nil: main XP/loot return only through positive mode/native-event branch, and fallback native assignments at body end have no returned value. Main weapon XP explicitly returns false for WZ; positive event return short-circuits fake-gun dvar. Loot explicitly excludes zombies by element/session mode. TierBoost requires public online, excludes ZM/invalid/training, then fake/native/Korea or numeric scr_credit_scale>=2. Playlist helpers apply public/custom/pregame/training gates, rule0 exclusions and exact delegates; MainMode compares playlist.mainMode, weapon delegate omits playlist arg in source. No progression grants or repaired truth formula is claimed; enum/data/native services remain conditional.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/35`.

  Archived evidence ID: `archived-record-00036` at JSON pointer `/units/82`; file SHA-256 `279ba12c6a1d4cfd1fb6c7e030a47694d4ee3982256bb21a0b3aa6909aef143b`; selected record SHA-256 `5e8fa87dcdacd0308d8cea1453aa2247a4b4244b909d18ccaeed7aad91711974`.

- `hmh07-lua:136` (original lines 3444-3473, 3444-3473, 131-131, 3444-3473, 131-131): Returns false when arg1 differs from the source enum lobby_mainmode_wz or the result of ui_wzfeaturedonlycountries:get() is falsey. When the hashed dvar exists() and get() each compare equal to true, it requests the literal Using geoip log and opaque Engine&#91;@"hash_36D9D7474CDD485B"&#93;(); a non-nil result is matched with unanchored "(%a+)-(%a+)" and the second alphabetic capture is passed to string.lower. A nil result requests the warning and leaves the comparison value empty. The alternative requests opaque Engine&#91;@"hash_56BA9980BA648FB3"&#93;(arg0) and reads result.Country without a local result guard. Provider identity, account ownership and language/country provenance are unproved. If execution continues, it logs the value and compares it exactly against each nonempty comma-separated token from string.gmatch; a match returns true and normal loop exhaustion returns false. Invalid values, an unmatched pattern or opaque/native failures may prevent later operations; no recovery or common normalization is shown.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/36`.

  Archived evidence ID: `archived-record-00711` at JSON pointer ``; file SHA-256 `a5200a0c104e949870231d9d69a02ac83db543f45d30db16d402955cd2b3c695`.

- `hmh07-lua-follow4:134` (original lines 3233-3233, 3235-3235, 3233-3233, 3235-3235, 3233-3233, 3235-3235): MOTD_ShouldShowMOTD returns false when Dvar&#91;@"motd_enabled"&#93;:get() is falsey, or true when the shown override-dvar request is truthy. Otherwise Engine&#91;@"hash_1D30724405ED0D69"&#93;(MOTD_GetMOTDChannel()) supplies the numeric-for upper-bound expression U. For each actual iteration i starting at1 with step1, set index=i-1 and request Engine&#91;@"hash_15451F941503DA5A"&#93;(controller, MOTD_GetMOTDChannel(), index). The returned r must satisfy the exact short-circuit predicate r~=nil, r.messageID>0, MOTD_IsLocationEnabled(r.locationID), not ShouldSkipMessage(r,index,controller), and (IsERegEnabled(controller) or r.action==nil or r.action~="registration"); return true at the first such predicate, else false only if the loop/evaluation finishes. Each channel request is evaluated at its shown site. Opaque bindings/results/types, count/retrieval meaning and actual service content remain unknown; the nil-only first guard does not prove a valid result object or safe field access. HasMessageAtLocation requests Engine&#91;@"hash_1D30724405ED0D69"&#93;(location) and uses its returned U as the numeric-for upper-bound expression, with i starting at1 and step1. Each actual iteration requests the distinct literal Engine&#91;@"getmarketingmessage"&#93;(controller,location,i-1). It returns true at the first truthy returned r with r.messageID>0, otherwise false only after the shown loop finishes. It does not apply the other body's full eligibility predicate. Count meaning, numeric/result validity, provider effects and actual service/message contents remain unknown; errors may prevent later requests or return.

  unknowns: &#91;{"kind": "original_build", "gap": "Recovered-source revision is pinned; original PS4 build/byte/VM/native binding remains unverified."}, {"kind": "effective_data_settings_assets", "gap": "Engine/model/Dvar/asset/data requests do not supply effective runtime values, contents or ownership."}, {"kind": "server_service_persistence", "gap": "Unavailable authoritative server/service/provider code and successful persistence remain unavailable; not reconstructed or counted as completed."}, {"kind": "runtime_callback_lifetime", "gap": "Original loading, table overwrites, callback delivery/order, timings, state selection and UI cleanup are not runtime-proven."}&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/37`.

  Archived evidence ID: `archived-record-00331` at JSON pointer ``; file SHA-256 `fdd4a50c24816a13ddb7b094a666f14fe219da874072beb2978ab3306155c328`.

- `hmh07-lua:153` (original lines 4846-4854, 4846-4854, 4846-4854): Loops all local controller indices and toggles each current ready flag for the menu lobbytype. Query module is host/client according to native isHost, and each result is negated before setreadyup. Despite the name it toggles rather than unconditionally setting true; no atomicity/rollback or transport completion proof.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/38`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/152`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `1f3d563c092608783b067b1dea82cc46e325512ef73282f71f962b389fd961ed`.

- `hmh07-lua:140` (original lines 4252-4257, 4252-4257, 4253-4255, 4254-4254, 4241-4250, 4256-4256, 4252-4257): Registers trial_countdown_tick to invoke TickTrialCountdown and adds a repeating UITimer with interval1 and flagfalse. No explicit local cancellation is installed; timer units, scheduling/lifetime and trial backend are native/UI dependencies.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/39`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/139`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `ea83371dc1031bf14985b29e79034ca31c31630a4036b5ec98ffbc24feae676e`.

- `hmh07-lua-follow4:121` (original lines 3216-3227, 3216-3227): Builds a featured-item header, interact prompt, party-leader prompt and double-XP icons. A nonnil name is localized-if-hash then uppercased. ShowForAllClients controls party-leader visibility and small controls parent state. Session/lobby/model callbacks validate them; LastInput on PC hides the interact prompt for KBM and shows it for gamepad. Creates self via LUI.UIElement.new, GamemodeBackground via LUI.UIImage.new, NotFocused via LUI.UIImage.new, Header via LUI.UIText.new, DirectorFeatureInteractPrompt via CoD.DirectorFeatureInteractPrompt.new, PartyLeaderOnlyPrompt via CoD.DirectorPartyLeaderOnlyPrompt.new, DoubleXPCardIconsRightAligned via CoD.DoubleXPCardIconsRightAligned.new, FrontendFrameSelected via LUI.UIImage.new. Stores state predicates Invisible, Small; their body effects require state-system evaluation.

  unknowns: &#91;{"kind": "original_build", "gap": "Recovered-source revision is pinned; original PS4 build/byte/VM/native binding remains unverified."}, {"kind": "effective_data_settings_assets", "gap": "Engine/model/Dvar/asset/data requests do not supply effective runtime values, contents or ownership."}, {"kind": "server_service_persistence", "gap": "Unavailable authoritative server/service/provider code and successful persistence remain unavailable; not reconstructed or counted as completed."}, {"kind": "runtime_callback_lifetime", "gap": "Original loading, table overwrites, callback delivery/order, timings, state selection and UI cleanup are not runtime-proven."}&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/40`.

  Archived evidence ID: `archived-record-00004` at JSON pointer `/units/120`; file SHA-256 `52df95eaa9f17f90427f6313acbc648c9bdffa0602f6444566bbe8fa1a54ba59`; selected record SHA-256 `46eae1de3798b9133f9a88f86a48236d291705f404d74337d1447eeac53fc12a`.

- `hmh07-lua-follow2:099` (original lines 4027-4027, 4027-4027): Constructs CoD.LobbyDebugOverlay.new from its exact supplied layout/controller/menu arguments; creates/attaches LobbyProcessQueueDebug. Registers close ownership; calls PostLoadFunc only if truthy; returns self only at the displayed return. Callback/state/clip bodies are deferred, and the exact source effects below define their receiver, data and branch contracts.

  unknowns: &#91;"Exact original PS4/source version matching, recovered Lua/VM fidelity and global/native/LUI provider identity remain unverified.", "Model/storage/DDL/assets/localization/dvar/enum values, callback delivery/cancellation/error behavior, native networking and unavailable service/server code are separate inputs.", "Other-file locals are not providers by spelling. Exact qualified global declarations are source candidates until loader/table identity and caller conditions bind them.", "No implicit nil/type checks, exception recovery, timer/model disposal, idempotence or guarantee that later effects run after an error is added."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/41`.

  Archived evidence ID: `archived-record-00028` at JSON pointer `/units/98`; file SHA-256 `2f4ecc3aabb5072135e148ef5782181882bd3b940908913a20bf258d3754185e`; selected record SHA-256 `57c396e41a4b8e992dbaac6a5e4bc2682b0418badf29f21d98187402872eb964`.

- `hmh07-lua:186` (original lines 3059-3059, 3059-3068): Hud_WZ directly constructs this result widget. SetupGameEndScoreWidget and DisableAutoButtonCallback run first; demo.processedKeyframeJump and lobbyRoot.publicLobby.stage are initialized to0 (real model writes, not backend stage proof). Builds result/outcome/eliminator/status/timer/deathcam/VOIP/quit/placement/killer/weapon/AAR/director/crosshair children. The constructor requests a GameScore/titleString subscription. Only if its callback is delivered and model:get() is nonnil, it requests LocalizeToUpperString with that value and passes the unknown result to Outcome:setText, if earlier accesses/calls succeed; nil takes no explicit setText arm. Callback delivery, localization/case result and displayed effect remain unresolved; aliveTeammateCount drives DownNotOut art; GameScore model forwarded to eliminator/challenge/killer/weapon displays. Victory controls challenge coin visibility. meansOfDeath>0 hides killer/weapon displays and inversely reveals self-caused/means-of-death displays. Attacker identity model rebinding first removes and nils old per-field subscription, dereferences new attackerClientModel, then subscribes xuid/clientNum/rank/rankIcon; analogous clientModel rebinding populates MistakesWereMade identity. Calling card receives full client model; nonnil callbacks update emblem/name/cleaned clan/rank/icon. No nil update clears old displayed text explicitly. VOIP HudStart has a recovered early-return/branch shape (exact trace) and ShowForCodCaster AlwaysFalse; do not replace it with an assumed visibility formula. Outcome state family: ShowOutcomeTransition with no killcam -> Victory/PC; defeat/team_elimination with no killcam -> Defeat/GameOver variants; elimination -> Elimination. Platoon variants additionally platoonCount!=0; PC variants additionally IsPC. Non-PC named states do not themselves contain not-IsPC, so do not assume exclusivity; LUI arbitration stays external. State/current/visibility/profile/lobby/teammate/AAR/input subscriptions reevaluate state/buttons. Square prioritizes console spectate (hide AAR/send skip_deathcam/clear transition/location/hide occluder), then console online AAR close under ui_showWZAAR/noncustom/not-spectate. Triangle redeploy requires private host, all members can redeploy, no matchmaking, redeploy_enabled and noncustom. Cross console deathcam requires eligibility, non-PC, not alternate killcam button, not UI-active/demo/default and viewed report; sends play_deathcam, sets hasPlayedDeathCam, plays alias/music. Circle console hold-finished quits; PC branches quit on non-held conditions; contextual2 handles PC exit. Each action returns true when taken, label callbacks often return false despite valid action, exact source retained. setState CallOriginalFirst hook branches demo/console/PC-occluded focus/intro/cursor/chat behavior; keyframeJump clears transition only during demo. Close is registered via CallOriginalSecond to an unselected __onClose; optional postload then focus/safe-area setup and return. Assets, backend result/rank/AAR provenance, hook order/cleanup outside scope, native menu response and actual execution remain open.

  unknowns: &#91;"Original Lua-to-PS4 CUSA11100 build binding and bytecode/VM/decompiler fidelity unverified.", "Effective HMH settings, enum values, model/data production, LUI state arbitration, event delivery/ordering/cancellation, assets, storage/DDL, networking/service behavior remain explicit gaps where called.", "External helper bodies not selected here are dependencies only; no nil/error recovery assumed beyond visible source. Named LUI override APIs are preserved; no original/new callback ordering is guaranteed without their source contract.", "No independent correctness review, retail execution or function completion credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/42`.

  Archived evidence ID: `archived-record-00142` at JSON pointer ``; file SHA-256 `b0d33370bc53b6d610906b9981c296de28bdc07228c9f239705a7c6393a02db3`.

- `hmh07-lua:145` (original lines 4529-4543, 4529-4543, 4529-4543): Gets element model, optionally descends the named path when nonempty, reads XUID and compares against the primary controller's XUID. Missing either value or unequal values return false, equal nonnil values true. Argument2 is unused; no account mutation occurs.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/43`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/144`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `b42e090dd23b990276a4c77258ffdea3751c3fec7ac9fed8ef0b6f3c2df54896`.

- `hmh07-lua-follow8:012` (original lines 3883-3883, 3908-3908, 3910-3910, 3920-3920, 3927-3927, 3883-3883, 3908-3908, 3910-3910, 3920-3920, 3927-3927, 3884-3884, 3891-3891, 3912-3912, 3884-3884, 3891-3891, 3912-3912, 3677-3681, 3883-3883, 3908-3908, 3910-3910, 3920-3920, 3927-3927, 3884-3884, 3891-3891, 3912-3912): Exact selected canonical immediate source contracts saved below; all owned inline bodies are separate and all old units remain reused unchanged.

  unknowns: &#91;"Pinned recovered source only. No originating bytecode, source-to-PS4 match, loader/overwrite/metatable/native/VM/settings/assets/services/server or runtime-delivery proof. Author checks are not independent correctness review.", "No min/max gaps, unlisted other-file bodies, new data/writers or held OIC constructor were authored."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/44`.

  Archived evidence ID: `archived-record-00045` at JSON pointer `/units/11`; file SHA-256 `0c981d5eb446fe3dd44845673b101548cf36172da6abd92475497ba0faf30ce0`; selected record SHA-256 `33efdacdbd074c7e905ce4807c3f0a6f86b222e49d15484a868c5242c47d13a6`.

- `hmh07-lua:126` (original lines 2428-2443, 2428-2443, 3382-3382, 2438-2438, 2428-2443, 3382-3382): Creates a filter table with mainMode/id/name/icon, available=true and empty cards. Arena argument chooses CreateArenaCards; otherwise invokes selected CreateFilterCards with forwarded limits. Returns the filter after helper effects. Data population and mode eligibility are conditional on supplied tables and helpers.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/45`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/125`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `893a81e8a512bbd5affd01ba27ee5fec3d27ff6d9dbc42ba552fcc024d27dec9`.

- `hmh07-lua-follow2:121` (original lines 4838-4838, 2550-2550, 2550-2550, 2480-2678, 2551-2551, 2551-2551, 2480-2678, 4838-4838): AllMembersHaveDLCMap derives native map mask only when supplied map is truthy; truthy mask forwards client list/mask/native main mode, otherwise returns true. Numeric0 remains truthy in ordinary Lua. ConvertMapNameToXHash preserves an xhash input, converts every other type and returns result. No platform/DLC asset ownership is inferred from this source request.

  unknowns: &#91;"Exact original PS4/source version matching, recovered Lua/VM fidelity and global/native/LUI provider identity remain unverified.", "Model/storage/DDL/assets/localization/dvar/enum values, callback delivery/cancellation/error behavior, native networking and unavailable service/server code are separate inputs.", "Other-file locals are not providers by spelling. Exact qualified global declarations are source candidates until loader/table identity and caller conditions bind them.", "No implicit nil/type checks, exception recovery, timer/model disposal, idempotence or guarantee that later effects run after an error is added."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/46`.

  Archived evidence ID: `archived-record-00233` at JSON pointer ``; file SHA-256 `1ab76e676efb00e723e7ed5a52b125b844fee6c395f7768b1ebbeef823712887`.

- `hmh07-lua:124` (original lines 1059-1065, 1059-1065, 1059-1065): Returns the exact alternate custom-games localization hash when IsZombies() is truthy; otherwise returns the supplied reference unchanged. The deciding IsZombies helper reads LobbyData.GetCurrentMenuTarget().mainmode and compares it with Enum lobby_mainmode_zm. This source does not bind that current menu target to an in-game Warzone state or prove the actual HMH branch. Original menu/enum values, native localization and invocation remain unresolved.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/47`.

  Archived evidence ID: `archived-record-00658` at JSON pointer ``; file SHA-256 `2d7fe42288b8300bb9e1737c2a12da225a48edf2e6d7457b788da0361a3ec63b`.

- `hmh07-lua:133` (original lines 3182-3184, 3182-3184, 3183-3183, 3182-3184): Creates/reads global lobby-list playerCount, defaults its falsey value to0 and returns whether it is below GetMinPlayersToStart. Model root/method validity and minimum threshold are external; no search restart occurs here.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/48`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/132`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `4cdb6a80f5e2a7ead480c33590440c53117eb9b101c67fd35c041fa42c05cbda`.

- `hmh07-lua-follow2:113` (original lines 2550-2550, 2550-2550, 2480-2678): EnabledAndProfile comparison short-circuits IsShoutcaster before exact equality of profile boolean with supplied value. Aerial camera returns visibility flag when truthy, otherwise native aerial-cam result. IsCodCasterOrAssigned returns IsCodCaster when truthy else assigned-state helper. No model producer, spectator assignment or actual camera transition is reconstructed.

  unknowns: &#91;"Exact original PS4/source version matching, recovered Lua/VM fidelity and global/native/LUI provider identity remain unverified.", "Model/storage/DDL/assets/localization/dvar/enum values, callback delivery/cancellation/error behavior, native networking and unavailable service/server code are separate inputs.", "Other-file locals are not providers by spelling. Exact qualified global declarations are source candidates until loader/table identity and caller conditions bind them.", "No implicit nil/type checks, exception recovery, timer/model disposal, idempotence or guarantee that later effects run after an error is added."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/49`.

  Archived evidence ID: `archived-record-00052` at JSON pointer ``; file SHA-256 `3408409cff40bee6f3712fa7a758e88917c8bbf1e8bbc73683c49e932cc2d04c`.

- `hmh07-lua-follow1:214` (original lines 5171-5180, 2957-2960): Constructs common director market/laboratory/contracts/pregame/hint/app-loadout views. Black-market/contracts visibility follows exact dvar/UI gates; pregame list filters showPregameButton==true and uses DirectorPregameButtons. Focus changes refresh hint state, focused hintText updates content, and app readiness/lobby changes validate state. It installs close, calls optional PostLoadFunc, sets _preGameType public and returns self. Purchase, contracts and companion services remain unavailable/provider gaps.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/50`.

  Archived evidence ID: `archived-record-00038` at JSON pointer ``; file SHA-256 `da0818b063c0fccb4ce8b7f89a4d9b74dc23b9fb2872626b7c92e7234f2662a2`; selected record SHA-256 `f29bd1eff48daedad3e5f064cd5c2c8932b68f949ca40cbbb85ed9a8833dd9ad`.

- `hmh07-lua-follow4:189` (original lines 2175-2175, 2175-2175): GetQuickplayPlaylists3088-3101 leaves its first formal f155_arg0 unused and passes its second formal f155_arg1 as the FIRST argument to GetUnfilteredPlaylistEntriesForTab. The SECOND helper argument is the fixed FEATURED key at3090, then the fixed PUBLIC key at3095. For each returned list in that order, ipairs traversal appends each entry.id whose canQuickplay value is truthy, then returns the accumulated list. The helper uses its second formal for tab comparisons3059/3063, while its first formal is forwarded to IsSessionModeAvailable3054. The caller adds no deduplication, playlist-selection or game-launch request. External argument types, effective key/provider values, original build/VM and runtime behavior remain unproved.

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/51`.

  Archived evidence ID: `archived-record-00125` at JSON pointer ``; file SHA-256 `608762c7caf815af26056bb7518f4c04d9e11814c41f969aefce88d242341b53`.

- `hmh07-lua-follow1:227` (original lines 4126-4126, 4126-4126, 2438-2438, 2438-2438, 4666-4672, 4666-4672): The six arena helpers keep exact early exits and event/enum tests. CurrentArenaEventTypeEquals rejects nonpublic-arena or nil event; IsEventCompleteTimer dereferences the event without the nil guard present in IsNextEventCompleteTimer. UpdateArenaOnLobbyNav exits unless arena mode, then writes rank/event/team/storage models and populates stats. CreateArenaCards filters future-ending events, sorts them and appends only the recovered active-action branch, then may mark cards&#91;1&#93;.featured without an empty guard. Preserve dayCount/party-count globals, scope defects and original enum/settings uncertainty.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/52`.

  Archived evidence ID: `archived-record-00036` at JSON pointer `/units/226`; file SHA-256 `279ba12c6a1d4cfd1fb6c7e030a47694d4ee3982256bb21a0b3aa6909aef143b`; selected record SHA-256 `e3ca5d77eac0dac31de8ebd1bcd8b16ddc602cf598c828c8607637b87bb52427`.

- `hmh07-lua:148` (original lines 4584-4592, 4584-4592, 4584-4592): Gets elapsed/estimated models; returns estimated<=elapsed when both exist, otherwise false. Existing models with nil/noncomparable values can fail the comparison; this is local label visibility only.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/53`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/147`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `883b59c8eb7205757e6b41ee7548fb74dc32f0bf14e4426b223a6c7877f58b83`.

- `hmh07-lua-follow8:017` (original lines 4038-4038, 4038-4038): Exact selected canonical immediate source contracts saved below; all owned inline bodies are separate and all old units remain reused unchanged.

  unknowns: &#91;"Pinned recovered source only. No originating bytecode, source-to-PS4 match, loader/overwrite/metatable/native/VM/settings/assets/services/server or runtime-delivery proof. Author checks are not independent correctness review.", "No min/max gaps, unlisted other-file bodies, new data/writers or held OIC constructor were authored."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/54`.

  Archived evidence ID: `archived-record-00509` at JSON pointer ``; file SHA-256 `f77a94ffdb81d1ed17b4f2ecbf9a16be0603cb0f5cb87fe1b6048aba6542726b`.

- `hmh07-lua-follow1:231` (original lines 2157-2168, 2445-2447, 2449-2464, 2466-2478, 2962-2975, 3032-3035, 3037-3046, 3048-3057, 3059-3068, 3093-3103, 3105-3108, 3145-3148, 3561-3578, 3580-3620, 3622-3627, 3683-3686, 3742-4056, 4058-4065, 4168-4170, 4241-4250, 4337-4347, 4349-4354, 4646-4656, 4658-4664, 4666-4672, 4760-4768, 4835-4844, 4893-4914, 4972-4974, 5160-5169, 2157-2168, 2614-2614, 2614-2614, 2157-2168, 2157-2157, 2445-2447, 2629-2629, 2629-2629, 2445-2447, 2445-2445, 2449-2464, 2527-2527, 2527-2527, 2449-2464, 2449-2449, 2466-2478, 2642-2642, 2642-2642, 2466-2478, 2466-2466, 2962-2975, 2962-2975, 2962-2962, 3032-3035, 3032-3035, 3032-3032, 3037-3046, 3037-3046, 3037-3037, 3048-3057, 3048-3057, 3048-3048, 3059-3068, 3059-3068, 3059-3059, 3093-3103, 3093-3103, 3093-3093, 3105-3108, 3105-3108, 3105-3105, 3145-3148, 3145-3148, 3145-3145, 3561-3578, 4139-4139, 4139-4139, 3561-3578, 3561-3561, 3580-3620, 3580-3620, 3580-3580, 3583-3590, 3583-3583, 3593-3606, 3593-3593, 3608-3612, 3608-3608, 3614-3618, 3614-3614, 3622-3627, 3622-3627, 3622-3622, 3683-3686, 3683-3686, 3683-3683, 3742-4056, 3742-4056, 3742-3742, 3744-3754, 3744-3744, 3746-3750, 3746-3746, 3802-3860, 3802-3802, 3862-3936, 3862-3862, 3938-3969, 3938-3938, 3971-3975, 3971-3971, 3977-3979, 3977-3977, 3991-3999, 3991-3991, 4000-4002, 4000-4000, 4003-4005, 4003-4003, 4007-4013, 4007-4007, 4014-4023, 4014-4014, 4024-4037, 4024-4024, 4058-4065, 4058-4065, 4058-4058, 4168-4170, 4168-4170, 4168-4168, 4241-4250, 4254-4254, 4254-4254, 4241-4250, 4241-4241, 4337-4347, 4337-4347, 4337-4337, 4349-4354, 4349-4354, 4349-4349, 4646-4656, 4646-4656, 4646-4646, 4658-4664, 4658-4664, 4658-4658, 4666-4672, 2499-2499, 2499-2499, 4666-4672, 4666-4666, 4760-4768, 4760-4768, 4760-4760, 4835-4844, 4818-4818, 4818-4818, 4835-4844, 4835-4835, 4893-4914, 4880-4880, 4890-4890, 4880-4880, 4890-4890, 4893-4914, 4893-4893, 4972-4974, 4972-4974, 4972-4972, 5160-5169, 5160-5169, 5160-5160, 5164-5168, 5164-5164, 2157-2168, 2445-2447, 2449-2464, 2466-2478, 2962-2975, 3032-3035, 3037-3046, 3048-3057, 3059-3068, 3093-3103, 3105-3108, 3145-3148, 3561-3578, 3580-3620, 3622-3627, 3683-3686, 3742-4056, 4058-4065, 4168-4170, 4241-4250, 4337-4347, 4349-4354, 4646-4656, 4658-4664, 4666-4672, 4760-4768, 4835-4844, 4893-4914, 4972-4974, 5160-5169, 2157-2168, 2445-2447, 2449-2464, 2466-2478, 2962-2975, 3032-3035, 3037-3046, 3048-3057, 3059-3068, 3093-3103, 3145-3148, 3561-3578, 3583-3590, 3593-3606, 3608-3612, 3614-3618, 3622-3627, 3683-3686, 3742-4056, 3744-3754, 3746-3750, 3802-3860, 3862-3936, 3938-3969, 3971-3975, 3991-3999, 4007-4013, 4014-4023, 4024-4037, 4058-4065, 4241-4250, 4337-4347, 4646-4656, 4658-4664, 4666-4672, 4760-4768, 4835-4844, 4893-4914, 4972-4974, 5164-5168, 1557-1563, 3561-3578, 3444-3473, 2451-2451, 2468-2468, 3063-3063, 3021-3030, 3063-3063, 3536-3548, 3575-3575, 3786-3786, 3791-3791, 3588-3588, 3592-3592, 3597-3597, 3601-3601, 3743-3743, 3748-3748, 3752-3752, 1557-1563, 3775-3775, 3503-3534, 3780-3780, 1612-1732, 3782-3782, 3805-3805, 3814-3814, 3825-3825, 3826-3826, 3832-3832, 3838-3838, 3840-3840, 3710-3727, 3828-3828, 3828-3828, 3834-3834, 3729-3740, 3830-3830, 3852-3852, 3853-3853, 3854-3854, 3855-3855, 3642-3650, 3879-3879, 3889-3889, 1315-1322, 3880-3880, 2952-2955, 3890-3890, 3890-3890, 3922-3922, 3932-3932, 4976-4980, 3973-3973, 4964-4970, 3978-3978, 3328-3350, 3992-3992, 4004-4004, 4011-4011, 4027-4027, 4038-4038, 4040-4040, 4054-4054, 4169-4169, 4237-4239, 4245-4245, 4327-4330, 4338-4338, 4350-4350, 4332-4335, 4352-4352, 3001-3010, 4647-4647, 3012-3019, 4649-4649, 2990-2999, 4649-4649, 4649-4649, 4838-4838, 4973-4973, 5148-5158, 5165-5165, 5166-5166, 2452-2452, 2454-2454, 2469-2469, 2471-2471, 2963-2963, 3033-3033, 3038-3038, 3049-3049, 3060-3060, 3094-3094, 3146-3146, 3575-3575, 3587-3587, 3747-3747, 3755-3755, 3757-3757, 3773-3773, 3939-3939, 3972-3972, 4044-4044, 3804-3804, 3818-3818, 3845-3845, 3845-3845, 3905-3905, 4895-4895, 4896-4896, 3812-3812, 3815-3815, 3874-3874, 3816-3816, 3876-3876, 3829-3829, 3835-3835, 3883-3883, 3908-3908, 3910-3910, 3920-3920, 3927-3927, 3884-3884, 3891-3891, 3912-3912, 3905-3905, 3905-3905, 3905-3905, 3906-3906, 3906-3906, 3907-3907, 3923-3923, 3945-3945, 3972-3972, 4001-4001, 4046-4046, 4060-4060, 4249-4249, 4649-4649, 4662-4662, 4667-4667, 4762-4762, 4762-4762, 2158-2158, 2158-2158, 2160-2160, 2160-2160, 2162-2162, 2162-2162, 2164-2164, 2164-2164, 2964-2964, 2964-2964, 3106-3106, 3562-3562, 3565-3565, 3684-3684, 3768-3768, 3813-3813, 3863-3863, 3867-3867, 3871-3871, 3896-3896, 3987-3987, 4007-4007, 4017-4017, 4024-4024, 4242-4242, 4894-4894, 4900-4900, 3095-3095, 3925-3925, 3567-3567, 3785-3785, 3942-3942, 3955-3955, 3745-3745, 3763-3763, 4042-4042, 3764-3764, 3765-3765, 3766-3766, 3796-3796, 3797-3797, 3798-3798, 3803-3803, 4010-4010, 4025-4025, 4894-4894, 3813-3813, 4017-4017, 3813-3813, 4007-4007, 4017-4017, 4024-4024, 4894-4894, 3834-3834, 3836-3836, 3850-3850, 3851-3851, 3880-3880, 3913-3913, 3914-3914, 3915-3915, 3916-3916, 3917-3917, 3918-3918, 3922-3922, 3993-3993, 3995-3995, 3997-3997, 4008-4008, 4043-4043, 4044-4044, 4045-4045, 4047-4047, 4048-4048, 4049-4049, 4053-4053, 4245-4245, 4763-4763, 5161-5161, 5166-5166, 2157-2168, 2445-2447, 2449-2464, 2466-2478, 2962-2975, 3032-3035, 3037-3046, 3048-3057, 3059-3068, 3093-3103, 3105-3108, 3145-3148, 3561-3578, 3580-3620, 3622-3627, 3683-3686, 3742-4056, 4058-4065, 4168-4170, 4241-4250, 4337-4347, 4349-4354, 4646-4656, 4658-4664, 4666-4672, 4760-4768, 4835-4844, 4893-4914, 4972-4974, 5160-5169): The30 selected DirectorUtility bodies cover quickplay/featured/show-state tests, focus-save/restore callbacks, playlist preference, menu lifecycle, selection cleanup and demo/trial/app helpers at their exact ranges. PostLoad registers deferred lobby/menu/model handlers; it can request profile commits, mode/map/settings changes, popups, image streaming, debug overlay and PC shortcuts only in the recorded branches. OnDirectorClose closes/clears the party subscription element and callback slots. Preserve ShowDirectorSelect's missing final return, SaveCurrentPlaylist's recovered local-scope defects, playlistID spelling, LobbyDebugyOverlay typo and comparison grouping. AllMembersHaveAMapInPlaylist succeeds on any qualifying rotation map, not every map. No original service/runtime behavior is credited.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/55`.

  Archived evidence ID: `archived-record-00122` at JSON pointer ``; file SHA-256 `d8f2d61181b7f59073ed6ae6273414056db7eaf6b0f4c86b10d40de7aee8c05e`; selected record SHA-256 `e5a090b5ba50cb09f60a61ca0776ba8cf3d6ad9065ce59e54d08c33eec1707d5`.

- `hmh07-lua-follow2:111` (original lines 2550-2550, 2550-2550, 2480-2678, 2551-2551, 2551-2551, 2480-2678): Reuse both historical exact semantic contracts: IsBitwiseAndNonZero tests bitwise intersection~=0 with original VM width/precedence limits. ClearBit subtracts1<<index only when IsBitSet; empty else falls through nil. Do not add an unchanged-value fallback. This file question has zero new draft credit because both bodies are reused.

  unknowns: &#91;"Exact original PS4/source version matching, recovered Lua/VM fidelity and global/native/LUI provider identity remain unverified.", "Model/storage/DDL/assets/localization/dvar/enum values, callback delivery/cancellation/error behavior, native networking and unavailable service/server code are separate inputs.", "Other-file locals are not providers by spelling. Exact qualified global declarations are source candidates until loader/table identity and caller conditions bind them.", "No implicit nil/type checks, exception recovery, timer/model disposal, idempotence or guarantee that later effects run after an error is added."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/56`.

  Archived evidence ID: `archived-record-00028` at JSON pointer `/units/110`; file SHA-256 `2f4ecc3aabb5072135e148ef5782181882bd3b940908913a20bf258d3754185e`; selected record SHA-256 `4567dbac7e486de026370682511823da51e716f72ad4ef365b647f4796b1fe40`.

- `hmh07-lua:150` (original lines 4801-4808, 4801-4808, 4801-4808): Only in Live reads playlist info and opens a warning popup using its maxPartySize. PC adds an OK label, other platforms pass nil. It assumes playlist info exists; no party mutation or explicit return.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/57`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/149`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `1278a9a4380a376b1decda47fbc0c42bcbcc0eab9ff0400017a38a0eadd16b28`.

- `CoD.DirectorUtility.CardNavigateToLobby` (original lines 4087-4166): No standalone body contract is available in this selected summary. Available classification: shared_Blackout_or_BO4.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/58`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/77`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `c8e2469aeb83422916b0e3f39be28d8d4168cd2df05c3dac82ef1c8688d1a2e1`.

- `hmh07-lua-follow7:002` (original lines 5496-5496, 5495-5497, 5496-5496, 2471-2471, 2466-2478, 2471-2471, 2471-2471, 2469-2469, 2466-2478, 2469-2469, 2469-2469, 2454-2454, 2449-2464, 2454-2454, 2454-2454, 2452-2452, 2449-2464, 2452-2452, 2452-2452, 2621-2621, 2480-2678): Only a truthy DDL-like first argument triggers two ClearDDLKeysAndArrays requests, in literal source sequence. The second request follows the first return and has no rollback. Return immediately for a falsey row list or destination. Otherwise traverse ipairs rows, write destination&#91;index-1&#93; using a native hash conversion of row&#91;key&#93; or EmptyItemIndex. A truthy destination and truthy item hash can produce a conversion, optional fallback conversion, set request and explicit result. The recovered trailing assignment is outside the local declaration scope; it does not set the destination or return EmptyItemIndex. Populate primary/secondary attachment and item fields, then grenade; additional ZM and MP branches use literal mode guards. Preserve duplicate secondary write, optional fourth-argument arithmetic and possible nil comparisons/returns. Request the hashed storage buffer. Nil buffer returns false; otherwise a nested StatValue:get greater than zero returns true and all other comparable results return false. Return the direct result of Dvar hash_20997C814ED4B7ED:get without existence test, coercion or default. Use the specialized DLC query only when the dvar exists, its value is truthy and main mode is MP or WZ; otherwise request getdlcbits with no forwarded arguments. Make a fresh result list; for nonnil/nonempty input, append converted tokens matched by &#91;^%s;&#93;+ in iteration order and return the list. For nonnil/nonempty blacklist text, return true at the first nonempty token whose native converted hash equals arg0; otherwise return false. Assign a fresh outer table whose keys field is a fresh ordered string array: killstreak1, killstreak2, killstreak3, killstreak4. It does not set actual loadout slots or grant anything. Top-level source assignment of numeric literal0 to the local module table field EmptyItemIndex. No original DDL invalid-item semantics or native conversion meaning is inferred from the name.

  unknowns: &#91;"Exact selected recovered Lua source only, conditional module/caller bindings. Original loader/global overwrite/VM/native/DDL/settings/assets/service/server/PS4 behavior remain unverified. No independent review, acceptance, function completion or runtime credit.", "Local at649 is scoped inside648..662; trailing663 reads/writes a global spelling. Preserve as recovered; do not hoist or insert a missing set/return. Original bytecode/VM fidelity remains missing.", "Potential nil>1 when ZM and fourth arg falsey; do not invent a default variant.", "updateItemIndexFromLoadoutHash can fall through without a returned empty marker;687 still requests a secondary set of its returned value."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/59`.

  Archived evidence ID: `archived-record-00106` at JSON pointer `/units/1`; file SHA-256 `18e061e5ee7b1c2bc739ab68607b07765f3b9de61ca899283d64f04ffa0fc469`; selected record SHA-256 `d983452a945b56a8ddaaed414ca9f87e8b280662103e224975214f9b9fd2e98a`.

- `hmh07-lua:121` (original lines 94-140, 94-140, 3415-3415, 94-140, 3415-3415): Builds card-list rows only from supplied cards with no mode or a nonzero display-name result. Featured cards get span2 and special insertion priority; selectIndex chooses the current playlist only before _hasSetDefault. Regional featured-only/current-playlist/low-pop conditions govern ordinary insertion. Finally sets _hasSetDefault=true and clears FocusFeaturedFiltered. Recovered goto basicblock_21 has no normal Lua target syntax here; do not silently resolve intended featured fallthrough or repair decompiler output.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used.", "Selected recovered source has an explicit scope/control-flow/field assumption described in answer; original executable semantics are not guessed or repaired."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/60`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/120`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `219cabd85450b46a232175a977de236cf44746959b5db95026e21d9c567b6154`.

- `hmh07-lua:139` (original lines 4192-4210, 4192-4210, 4199-4199, 4202-4202, 4205-4205, 4207-4207, 4192-4210): Reads lobbyNav/menu mainmode, then chooses online arena-custom, online custom (after opaque native call), LAN arena or LAN menu. No mode means no navigation; missing menu is unguarded before the mode test. Actual transport/authorization and target table values remain external.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/61`.

  Archived evidence ID: `archived-record-00561` at JSON pointer ``; file SHA-256 `d7b895b172105e124accede8db9f845e6d646b6e5a0ed9b267e3b0d8e5a009e7`.

- `CoD.DirectorUtility.SetupDirectorFiltersCardsForMode` (original lines 3401-3423): No standalone body contract is available in this selected summary. Available classification: shared_Blackout_or_BO4.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/62`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/74`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `a9f8ac8d5c0b948bb5726bb0be1a0c7d059c0735d62426c36cc101388be13f0e`.

- `hmh07-lua:130` (original lines 3001-3010, 3001-3010, 3001-3010): Returns true only when menu lobbymode is public and isadvertised is not0. Missing/nil isadvertised is not equal to0 in recovered source, so it is not an explicit true-only advertisement check.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/63`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/129`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `646f6f58390c90bfab3dcfb3ad95a7cd5ced25b93db78dec4c3c9fc276caf900`.

- `hmh07-lua:149` (original lines 4784-4799, 4784-4799, 4784-4799): In Live reads selected playlist and current mainmode; returns true only for matching playlist mainmode and party count above its maximum. Every other completed path returns false. It creates playlist/count models but does not reduce party size or reject a connection itself.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/64`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/148`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `9d14b1e6277d9cce0e55617eed5e419b275714de8313d93f0061e72de983b7c7`.

- `CoD.DirectorUtility.PartyExceedsPlaylistMax` (original lines 4567-4572): No standalone body contract is available in this selected summary. Available classification: shared_Blackout_or_BO4.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/65`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/76`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `88524b20940de8b22ad3b6077c0cfcdebb3112a540f6b9c6765210d665f65263`.

- `hmh07-lua:131` (original lines 3012-3019, 3012-3019, 3013-3013, 3012-3019): Rejects when element available is neither nil nor true via helper; otherwise returns whether current menu lobbymode is custom. This is a UI visibility predicate, not host permission or native lobby creation.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/66`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/130`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `fad942d5ff4394e4280b4fedcc24751e8a526c923168dcbee58a7e1df6cb1ec5`.

- `hmh07-lua-follow4:122` (original lines 3305-3318, 3287-3303): Builds a party-count footer. Defines and immediately invokes both private-count and matchmaking-count text functions, then subscribes those same functions to private/game client updates. Matchmaking state tests publicLobby.stage against INVALID and is separately revalidated on stage changes. No party membership changes are implied. Creates self via LUI.UIHorizontalList.new, Label via LUI.UIText.new, Spacer2 via LUI.UIImage.new, Spacer via LUI.UIImage.new, PartyCount via LUI.UIText.new, MatchmakingCount via LUI.UIText.new. Stores state predicates Matchmaking; their body effects require state-system evaluation.

  unknowns: &#91;{"kind": "original_build", "gap": "Recovered-source revision is pinned; original PS4 build/byte/VM/native binding remains unverified."}, {"kind": "effective_data_settings_assets", "gap": "Engine/model/Dvar/asset/data requests do not supply effective runtime values, contents or ownership."}, {"kind": "server_service_persistence", "gap": "Unavailable authoritative server/service/provider code and successful persistence remain unavailable; not reconstructed or counted as completed."}, {"kind": "runtime_callback_lifetime", "gap": "Original loading, table overwrites, callback delivery/order, timings, state selection and UI cleanup are not runtime-proven."}&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/67`.

  Archived evidence ID: `archived-record-00004` at JSON pointer `/units/121`; file SHA-256 `52df95eaa9f17f90427f6313acbc648c9bdffa0602f6444566bbe8fa1a54ba59`; selected record SHA-256 `82b15c03fa31f039d5734ead3fbd7f5e95ae2b0b39700556179430889cac2d2f`.

- `CoD.DirectorUtility.SetPlaylist` (original lines 1041-1045): No standalone body contract is available in this selected summary. Available classification: shared_Blackout_or_BO4.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/68`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/78`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `bbbe038899c201011e069e620314a0043454d0012bc0b5286ae84715c9f9ec57`.

- `hmh07-lua-follow3:259` (original lines 2990-2990, 2990-2999): Creates CoD.RestrictedItemWarningBar using LUI.UIElement.new( f1_arg2, f1_arg3, f1_arg4, f1_arg5, f1_arg6, f1_arg7, f1_arg8, f1_arg9 ). Initializes and attaches children in source order: RestrictedBar, RestrictedWarning. Registers ordered presentation states Visible with the exact predicate bodies below. Defines 3 separate closure scopes; their model/event/table bindings and their own ordered writes/returns are retained, not flattened into construction. Visible requires not director pregame, not public WZ lobby, and self isRestricted; model/lobby changes revalidate. Returns self after the shown optional hooks and setup. Native UI/model/asset effects and callback delivery are external contracts.

  unknowns: &#91;"Original PS4/source match, original Lua bytecode and VM/decompiler fidelity remain unverified.", "Effective enum/dvar/settings, assets/localization/model/DDL/storage/playlist data remain exact external inputs; requested persistence/network/service effects are not successful execution proof.", "A field/method/import/spelling or other-file local alone does not bind a provider. Unknown identities remain unresolved rather than declared unavailable.", "Native model/event/timer/wrapper invocation, delivery, error/cleanup/lifetime and unavailable original server behavior are outside this source packet.", "No independent correctness review, acceptance, original-build or function-completion credit is recorded."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/69`.

  Archived evidence ID: `archived-record-00003` at JSON pointer `/units/258`; file SHA-256 `a63852530df9189721a410c240a42967af6648aa0fca4e70325b17a1e677ebb7`; selected record SHA-256 `6387621d4ab6f00774a367ae08570b7eb5cf502f784a2add1edf4862cf440f89`.

- `hmh07-lua-follow6:178` (original lines 4760-4768, 4760-4768): Takes a controller. Returns false for the PC/platform-native predicate, then false for non-PC Russian. In the final else block declares local f64_local0. Outside a game, an offline-demo branch queries hash_5CB675CA7856DA25 and returns its falsy value early; otherwise evaluates IsERegEnabled and, only if truthy, issignedintodemonware. In-game sets the block-local variable false. After that entire else block ends, line 1052 returns the separate non-local f64_local0, not the ended block-local variable. Preserve that literal scoping defect; the intended normal result is not reconstructed or silently repaired.

  unknowns: &#91;"Effective HMH settings/data/assets, true load/overwrite/class lookup order, original recovered-text fidelity, native callback delivery and service/server implementations remain open.", "Independent correctness review and final game tests remain deferred.", "The final f64_local0 read is outside the else block containing its local declaration. Whole-file and exact-fragment ASTs classify line1052 as a non-local identifier. Intended normal return needs original fidelity/VM evidence; no repair."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/70`.

  Archived evidence ID: `archived-record-00056` at JSON pointer `/units/177`; file SHA-256 `9b5470295d8bc5b945061358d29d8430f5da2392ccde6abf20deb11b8b9c027f`; selected record SHA-256 `9af15e83e3a71b2c05d56a29b8216842ddd590c8f5974dd1a094a7a4fa4e9691`.

- `CoD.DirectorUtility.CreateFilter` (original lines 2428-2443): No standalone body contract is available in this selected summary. Available classification: shared_Blackout_or_BO4.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/71`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/71`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `fcfdae87ab7825e3ee50ee9b55c51fd1957af94d8668b1a66931fe9750c6181a`.

- `hmh07-lua-follow1:091` (original lines 3320-3326): Creates lobby countdown/occlusion models, warning/radial timer/formatted time/decorations and team talker grid. Nonnil timeRemaining drives radial shader and TimeRemainingForMatchStart text. Visible requires IsMultiplayer, countdown>0 and<=20, and lobby menu occluded; VOIPVisible requires occluded alone. LobbyNav/time/occlusion notifications request reevaluation. Registers close, optional postload, returns self. Match-start scheduling, native countdown units and effective HMH mode predicate remain conditional.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/72`.

  Archived evidence ID: `archived-record-00036` at JSON pointer `/units/90`; file SHA-256 `279ba12c6a1d4cfd1fb6c7e030a47694d4ee3982256bb21a0b3aa6909aef143b`; selected record SHA-256 `07ac6ebd0932fc194e8d53818fcf83bd54f640ba4ec006cc93f3abbbf841de47`.

- `hmh07-lua:157` (original lines 4964-4970, 4964-4970, 4966-4966, 4968-4968, 4964-4970): When ZombieUtility exists invokes HideZMLoadoutPreview; otherwise merely fetches DirectorZMLoadoutPreview model into a local. No actual hiding write appears in the fallback, so none is invented. HMH use of the helper remains conditional.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/73`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/156`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `342c7f54c8d7536dcfedb1f7bb884da17c893502ce9eb7ef430b634eeaa416a3`.

- `hmh07-lua:239` (original lines not specified): The supplied factory self-definition is registration, not an observed invocation. Conditional factory contract: create DirectorFindGameWZ menu, set user-data properties, SetupDirectorFiltersCards, owner/sound, build selected info and 3x4 OptionsList using DirectorPlaylistOption. Confirm consumes over-max-party input without action; otherwise unlocked item runs ProcessListAction then GoBack and returns true; locked falls through. Label over-max/locked returns false, unlocked selects true. Selected info links active option model; tab grid dataSource changes replace OptionsList datasource. Footer/header/backing/tabbar menu_loaded handlers call local/super handler, safe-area logic (footer only non-PC) then dispatch unhandled events to children. Tabs Hidden=not MultiplePlaylistTabsAvailable, reevaluated on grid/input changes; tabs use DirectorFilters with8 columns. list_active_changed gives focus to menu default. Back button calls GoBack and returns true. ClearMenuSavedState is hooked through the named close override via CallOriginalFirst; self.__onClose is hooked before original via CallOriginalSecond, with exact implementation retained in qualified companion. PC setup/restore is conditional. menu_loaded is processed before final optional postload; SetModelFromPropertyModel and ignoreSavedActive=true occur last, then self returned. No live matchmaking request is proved; native factory dispatch/models/state and exact HMH tab/filter membership stay open.

  unknowns: &#91;"Original Lua-to-PS4 CUSA11100 build binding and bytecode/VM/decompiler fidelity unverified.", "Effective HMH settings, enum values, model/data production, LUI state arbitration, event delivery/ordering/cancellation, assets, storage/DDL, networking/service behavior remain explicit gaps where called.", "External helper bodies not selected here are dependencies only; no nil/error recovery assumed beyond visible source. Named LUI override APIs are preserved; no original/new callback ordering is guaranteed without their source contract.", "No independent correctness review, retail execution or function completion credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/74`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/238`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `11b40ca38c1b41286c7e78f9d8de4acd28109ea34dc6dc0c75f3f4b5d02de76a`.

- `hmh07-lua:152` (original lines 4831-4833, 4831-4833, 4831-4833): Opens a warning popup with exact localization keys and a PC-only OK label. It performs no DLC installation/unlock and returns no explicit result.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/75`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/151`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `344f7ecd89f230a66c966ef3f346da57200674effaa922080cdf772ede37943b`.

- `hmh07-lua-follow1:105` (original lines 2550-2550, 2550-2550, 2550-2550, 2480-2678): Selected model wrappers create/init controller models; InitIfNotSet checks model existence, not its stored false/nil value. GetMapValue hashes name and returns existing nonnil field else supplied default; AlreadyRegistered is identity. LocalizeIfNotCodcaster localizes only outside assigned/codcaster. MessageDialog subscription replaces the previous one, conditionally closes an existing dialog, opens an in-game HUD/controller-qualified priority overlay and locks input, or frontend overlay when unoccluded; close callback clears _messageDialogBox. HoldFinished returns true for absent/nil model, else tests the exact bit. MenuPreservesButton writes a map. PlayClipAndThenClose registers clip_over after playClip, with no cancellation fallback. CustomElementFunction calls only a truthy named field with four exact args. PlayMusic forwards to Engine. SelfShowsBuildInfo increments the global model and restores its captured prior value on close; nil/arithmetic/concurrent-close hazards are retained.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/76`.

  Archived evidence ID: `archived-record-00036` at JSON pointer `/units/104`; file SHA-256 `279ba12c6a1d4cfd1fb6c7e030a47694d4ee3982256bb21a0b3aa6909aef143b`; selected record SHA-256 `1f1f746fc68b2fb20780032847c94fe11eed227d3e24ae013f53547a88ddc3ac`.

- `hmh07-lua:156` (original lines 4924-4937, 4924-4937, 4928-4928, 4924-4937): Returns false on LAN. Otherwise returns true only when LobbyRoot.room is lobby_pose, arena_pose or private_lobby_pose. Model validity and actual3D pose assets remain external.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/77`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/155`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `dea4e54b1bbd095262f4624a0748738038d8e855791873def63bec38b94ed925`.

- `hmh07-lua:129` (original lines 2990-2999, 2990-2999, 2990-2999): Returns true only for online MP, ZM or WZ pregame menu names. It is an exact menu-name disjunction and does not include arbitrary game-state transitions.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/78`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/128`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `85c5be331de8251d6aeca9156a0282e3b00c15854fbf69822b52d45dd3c2a05f`.

- `hmh07-lua-follow1:081` (original lines 4256-4256, 4256-4256, 4256-4256, 4252-4257): UITimer.new calls create(interval,oneShot), creates event table for string name or mutates supplied event.timer for table input, sets event target, calls reset and returns timer. newElementTimer creates timer, packs varargs with n, installs timerEventFunction that shallow-copies args, appends the delivered event and calls callback(unpack(copy)); then reset and return. Actual ticks, stop/close behavior and vararg-hole/unpack semantics remain external to these bodies; no guaranteed scheduling or cancellation is inferred.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/79`.

  Archived evidence ID: `archived-record-00628` at JSON pointer ``; file SHA-256 `00b08c03f95ab28027d555b815f9e20c7a7307530be65fd8557c5c14ea43d033`.

- `hmh07-lua-follow3:151` (original lines 5071-5071, 5077-5077, 5071-5071, 5077-5077, 5071-5071, 5077-5077): For CoD.SocialUtility.IsPartyMissingRequiredDLCForSelectedPlaylist, evaluate the displayed formal inputs and captured values. Its exact paths are 2156: if f75_local0 then; 2159: if f75_local0 then; 2161: return f75_local1 and f75_local1.lockState == Enum&#91;@"playlistlockstate"&#93;&#91;@"pls_required_dlc_disabled"&#93;; 2163: return false. Its writes/requests begin 2155: f75_local0 = f75_local0.playlistId; 2157: f75_local0 = f75_local0:get(). The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior.

  unknowns: &#91;"Original source-to-PS4/VM/native/loader identity and bytecode fidelity are unverified.", "Effective settings, assets/tables/model schemas, server/service implementation and callback delivery/lifetime are unverified.", "Exact source request semantics do not prove rendering, networking, persistence, progression or game behavior.", "Public reuse is the frozen manager audit only; no worker web/repository discovery was performed."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/80`.

  Archived evidence ID: `archived-record-00003` at JSON pointer `/units/150`; file SHA-256 `a63852530df9189721a410c240a42967af6648aa0fca4e70325b17a1e677ebb7`; selected record SHA-256 `0ba867ee4c187deacb02c3bd55614ffe52a244fdfe6047e8f45566a3f4fde9e0`.

- `hmh07-lua:146` (original lines 4567-4572, 4567-4572, 4567-4572): Reads global playerCount with0 fallback and element maxPartySize with0 fallback; returns maxPartySize<playerCount. Model objects themselves are not guarded. It does not query or alter session membership.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/81`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/145`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `2cb12dc3e266dd253b61ecbd8b52d11174922905a02df8d700039802e0a913b5`.

- `hmh07-lua-follow1:113` (original lines 4811-4811, 4105-4105, 4135-4135, 4154-4154, 4163-4163, 4199-4199, 4202-4202, 4205-4205, 4207-4207, 4811-4811, 4811-4811, 4810-4822, 4105-4105, 4135-4135, 4154-4154, 4163-4163, 4105-4105, 4087-4166, 4135-4135, 4087-4166, 4154-4154, 4087-4166, 4163-4163, 4087-4166, 4199-4199, 4202-4202, 4205-4205, 4207-4207, 4199-4199, 4192-4210, 4202-4202, 4192-4210, 4205-4205, 4192-4210, 4207-4207, 4192-4210, 2192-2219, 4887-4891, 4887-4891, 4846-4854, 4846-4854, 3012-3019, 3012-3019): GetClientList annotates controlling-session clients using private-party membership (special ZM-private uses same session), nested xuid/simpleLobbyID scans, sorts by LobbyMemberSort, then marks adjacent-party flags and returns mutated sessionClients. NavigateToLobby returns for same target or trial/age/limited/access warnings; otherwise records navigation action and saved history before local/max-client warnings, sets optional training black screen and emits OnGoForward. LobbyGoBack clears saved state then prioritizes selection-screen refresh, manual timer stop, ZM ready-down/offline overlay, WZ public party-leave event, MP host party back, training outro callback and generic leave popup/with-party policy. StartSearch emits async start only when both local blockers false and playlist preparation succeeds. Vote select plays sound before native vote; location forwards private-lobby native update. AllMembersCanRedeploy returns false only on a nonnil location outside three allowed enums, true otherwise including empty/missing per-client locations. Unknown enums, data/native outcomes and original HMH binding stay explicit.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/82`.

  Archived evidence ID: `archived-record-00036` at JSON pointer `/units/112`; file SHA-256 `279ba12c6a1d4cfd1fb6c7e030a47694d4ee3982256bb21a0b3aa6909aef143b`; selected record SHA-256 `ad0cb7b81b6c76383292ed70b546c7d4e0608ced2c7fa410bd7a64c76cbec240`.

- `hmh07-lua-follow1:150` (original lines 4469-4490, 4976-4980, 5067-5073, 4784-4799, 2221-2231, 4801-4808, 5075-5081, 2699-2707, 1059-1065, 4192-4210, 4504-4506, 946-969, 1005-1022, 991-1003, 971-989, 900-915, 849-864, 2287-2294, 2990-2999): Builds the pregame director after public-lobby/position-draft/quickplay initialization. Find-match actions branch on Zombies, client limits and locking; custom-game actions differ for PC/Zombies/system overlays; map/game and tutorial actions keep separate host/mode gates. Playlist/network/session models update labels, images, state and button prompts. State changes select host/nonhost default focus; lobby/client changes refresh position draft. Existing close, optional PostLoadFunc and final PC redirect navigation precede return self. Other-mode actions remain conditional source branches, not HMH runtime requirements.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/83`.

  Archived evidence ID: `archived-record-00128` at JSON pointer ``; file SHA-256 `5dfd1c6697bec5c0500e13741c0b43e4ec821668f4b266de1bd3616181f81860`.

- `hmh07-lua-follow3:133` (original lines 3654-3654, 3655-3655, 3656-3656, 3657-3657, 3662-3662, 3663-3663, 3664-3664, 3665-3665, 3654-3654, 3655-3655, 3656-3656, 3657-3657, 3662-3662, 3663-3663, 3664-3664, 3665-3665, 3654-3654, 3655-3655, 3656-3656, 3657-3657, 3662-3662, 3663-3663, 3664-3664, 3665-3665): For CoD.BaseUtility.InitControllerModelEnumIfNotSet, evaluate the displayed formal inputs and captured values. Its exact paths are 50: if not f7_local0&#91;f7_arg1&#93; then. Its writes/requests begin 51: local f7_local1 = f7_local0:create( f7_arg1 ); 52: f7_local1:set( f7_arg2 ). The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior. For CoD.BaseUtility.SetElementModelToOtherElementModel, evaluate the displayed formal inputs and captured values. Its writes/requests begin 155: f30_arg1:setModel( f30_arg2:getModel(), f30_arg0 ). The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior. Looks up the requested mode's abbreviation and calls Engine.switchmode only in the displayed abbreviation branch. The trailing empty-string assignment is not converted into a fallback switch request. No success return or original mode-transition behavior is supplied. For CoD.BaseUtility.SwitchMode, evaluate the displayed formal inputs and captured values. Its exact paths are 282: if f46_local0 then; 284: if not f46_local1 then. Its writes/requests begin 283: f46_local1 = f46_local0.Abbreviation; 290: f46_local1 = "". The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior. For CoD.BaseUtility.RestoreState, evaluate the displayed formal inputs and captured values. The exact ordered provider request below is the entire visible wrapper behavior; no opaque provider effects are invented. The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior. For CoD.BaseUtility.DisableNavigation, evaluate the displayed formal inputs and captured values. Its writes/requests begin 592: f82_arg0.m_disableNavigation = true. The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior. For CoD.BaseUtility.EnableNavigation, evaluate the displayed formal inputs and captured values. Its writes/requests begin 596: f83_arg0.m_disableNavigation = false. The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior. For CoD.BaseUtility.SaveState, evaluate the displayed formal inputs and captured values. The exact ordered provider request below is the entire visible wrapper behavior; no opaque provider effects are invented. The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior. For CoD.BaseUtility.AddToMenuList, evaluate the displayed formal inputs and captured values. The exact ordered provider request below is the entire visible wrapper behavior; no opaque provider effects are invented. The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior. For CoD.BaseUtility.RemoveFromMenuList, evaluate the displayed formal inputs and captured values. The exact ordered provider request below is the entire visible wrapper behavior; no opaque provider effects are invented. The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior. For CoD.BaseUtility.GetTimerStruct, evaluate the displayed formal inputs and captured values. Its exact paths are 774: if not f113_local0&#91;f113_arg1&#93; then; 777: return f113_local0&#91;f113_arg1&#93;. Its writes/requests begin 775: f113_local0&#91;f113_arg1&#93; = {}. The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior. If the caller's named per-controller timer struct and interpolateTimer exist, requests that timer's close. It then replaces the named struct with a fresh empty table regardless of whether a timer existed. Close delivery and concurrent callback cancellation are external; replacement does not prove they occurred. For CoD.BaseUtility.ResetInterpolationTimer, evaluate the displayed formal inputs and captured values. Its exact paths are 781: if CoD.perController&#91;f114_arg0&#93;&#91;f114_arg1&#93; and CoD.perController&#91;f114_arg0&#93;&#91;f114_arg1&#93;.interpolateTimer then. Its writes/requests begin 782: CoD.perController&#91;f114_arg0&#93;&#91;f114_arg1&#93;.interpolateTimer:close(); 784: CoD.perController&#91;f114_arg0&#93;&#91;f114_arg1&#93; = {}. The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior. Diffs the old and requested image-key sets: requests streaming for new non-userdata keys, then releases removed non-userdata keys. It returns the caller's requested table itself. The two tables are not deep-copied. Membership tests use the OTHER table value truthiness, not mere key presence. For a shared non-userdata key a, old&#91;a&#93;=false,new&#91;a&#93;=true requests streaming in the first loop; old&#91;a&#93;=false,new&#91;a&#93;=false requests then releases in the two loops under ordinary Lua truthiness. Provider effects, errors and runtime delivery remain unverified. For CoD.BaseUtility.ForceStreamHelper, evaluate the displayed formal inputs and captured values. Its exact paths are 866: for f124_local3, f124_local4 in pairs( f124_arg1 ) do; 867: if type( f124_local3 ) ~= "userdata" and not f124_arg0&#91;f124_local3&#93; then; 871: for f124_local3, f124_local4 in pairs( f124_arg0 ) do; 872: if type( f124_local3 ) ~= "userdata" and not f124_arg1&#91;f124_local3&#93; then; 876: return f124_arg1. The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior. For CoD.BaseUtility.AddForcedImageToTable, evaluate the displayed formal inputs and captured values. Its exact paths are 880: if f125_arg0 ~= @"hash_0" and f125_arg0 ~= nil then. Its writes/requests begin 881: f125_arg1&#91;f125_arg0&#93; = true. The statement contracts below preserve exact arguments, reads/writes, short-circuit tests, loop and return behavior.

  unknowns: &#91;"Original source-to-PS4/VM/native/loader identity and bytecode fidelity are unverified.", "Effective settings, assets/tables/model schemas, server/service implementation and callback delivery/lifetime are unverified.", "Exact source request semantics do not prove rendering, networking, persistence, progression or game behavior.", "Public reuse is the frozen manager audit only; no worker web/repository discovery was performed."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/84`.

  Archived evidence ID: `archived-record-00360` at JSON pointer ``; file SHA-256 `38515590c26e8c9d73a00bd3f7b590fc301976f8fbccf3615fe1c9bcbd0b3198`; selected record SHA-256 `7d957d25fd3bcf91d3ca02764e46ddcf00d454673121a4786546c0f150e3dad1`.

- `hmh07-lua-follow1:104` (original lines 3653-3659, 3661-3667): CanShowAAR requires both stats records and one allowed menu state, resolves current gametype/fallback hash, checks a gametype stats entry, then mode-specific validity: zombies excludes tutorial; WZ compares TIME_PLAYED_TOTAL old<new; other modes require AAR.valid==1. ForceAAR is only the elseif fallback, requiring current stats and allowed menu state. OpenAARIfNeeded creates viewedAAR, returns when already true, otherwise postpones/forces images and schedules next-frame work; streamed images open immediately, otherwise50ms timer accumulates timeElapsed until >6000 or streamed, resumes streams, closes spinner, opens report, clears saved state and closes timer. viewedAAR is set true after scheduling. Ineligible public/arena invokes match survey. OpenAAR prioritizes WZ, zombies, arena, then MP overlay. Missing models, callback cancellation and backend validity are not supplied.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/85`.

  Archived evidence ID: `archived-record-00036` at JSON pointer `/units/103`; file SHA-256 `279ba12c6a1d4cfd1fb6c7e030a47694d4ee3982256bb21a0b3aa6909aef143b`; selected record SHA-256 `ae137128b156f2f0665d617515467cae912d7fb992d5064b37d53ba2a6ef2979`.

- `hmh07-lua:132` (original lines 3021-3030, 3021-3030, 3021-3030): Returns true when current menu is public and isadvertised==0. Despite the name, it does not test a private lobbymode enum.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/86`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/131`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `b42eee41ca4da721c907130ce0cdb1694f483462f8458ab2fca86460856e412b`.

- `hmh07-lua:142` (original lines 4492-4494, 4492-4494, 4492-4494): Returns the native localization call for hash_477D6F0B08C5E000 with the supplied estimate. No time calculation or service query occurs in this wrapper.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/87`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/141`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `2d257269e5ab1e210e78f4a4066a60467c8f17736b6466715615002b7b9a699f`.

- `hmh07-lua-follow2:240` (original lines 4038-4038, 4038-4038): Converts game-setting asset rows into name/setting/image/slider/options data, filtering the explicit PC-only-disabled row and falling back per label/value/hint. A toggle flag swaps in enabled/disabled arrays. The validation setter stores a function in a table; registration is not execution.

  unknowns: &#91;"Original PS4/source exact-version and original Lua/VM binding remain unverified.", "Effective enum/mode/platform/settings and asset/model/storage data are unavailable.", "Native/LUI event/subscription/timer dispatch, cleanup guarantees and errors not shown in selected source remain open.", "Unavailable service/server code is not reconstructed or counted."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/88`.

  Archived evidence ID: `archived-record-00712` at JSON pointer ``; file SHA-256 `0a1e87809ed2e90923c8b625702ca7fdf99183a65e51a6c36f01abaea76451c8`; selected record SHA-256 `8974e45aad9dced0b7bcdd199c11a3db23e58e1b0ce77513c9741a55630a5809`.

- `hmh07-lua:127` (original lines 2480-2678, 2480-2678, 2440-2440, 2550-2550, 2499-2499, 4666-4672, 2527-2527, 2449-2464, 2642-2642, 2466-2478, 2614-2614, 2157-2168, 2629-2629, 2445-2447, 2551-2551, 2624-2624, 2508-2508, 2505-2505, 2506-2506, 2507-2507, 2480-2678, 2440-2440): Iterates supplied playlist entries, chooses a navigation action and derives XP/weapon/tier/NP flags. Exclusion combines user tiers, native lock state, requested mode/arena, hidden flag, featured schedule and regional/PC blacklists. It deduplicates rotation maps/gametypes for display, then writes sequential card records with action/mode/playlist/limits/reward flags when not excluded. Recovered chained arena comparison, scope artifacts and basicblock gotos prevent an original executable reconstruction claim; the exact recovered branch/effect transcript is preserved rather than repaired. Assigning action is not calling it, and ZM/CP paths are not promoted to HMH.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used.", "Selected recovered source has an explicit scope/control-flow/field assumption described in answer; original executable semantics are not guessed or repaired."&#93;

  status: partial

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/89`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/126`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `523d816b3adf5cb7fbbafeacc1ca7b75dfa038b09761bd6af5b320bbf18d9b1d`.

- `hmh07-lua-follow1:017` (original lines 2624-2624, 2624-2624, 2624-2624, 2480-2678): StartKoreaIndulgenceChecks returns immediately outside IsInKorea; otherwise it subscribes only if global Korea.ShowIndulgenceMessage exists. A true update shows localized rounded(hours=dvar/3600) game event and then sets the trigger false. ShowKorea15Plus returns the short-circuit Korea test and native eligibility value. Playlist blacklist testing runs only under that predicate, first checks uniqueName against a semicolon list, then ipairs(rotationList) for any blacklisted map, returning true on first match and false after all. Country/platform/native/dvar and caller gates remain conditional, never inferred from the utility name.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/90`.

  Archived evidence ID: `archived-record-00036` at JSON pointer `/units/16`; file SHA-256 `279ba12c6a1d4cfd1fb6c7e030a47694d4ee3982256bb21a0b3aa6909aef143b`; selected record SHA-256 `672827bb83f4651b8777ff852cda0dc47ff8f69295e23eb2508109391682a847`.

- `hmh07-lua-follow1:101` (original lines 4740-4748): Initializes showPreAlphaText from NeedsWatermark and showBuildInfo0, constructs static/build/host/context text plus telemetry/achievement children. Nonnil links update their exact fields; state predicates read watermark1/2 and buildInfo>0, notifications reevaluate. menuOpened callback sizes non-PC safe area only with defined controller parameter; removeOverrides callback removes that exact registration, and close hook is registered through CallOriginalSecond. Achievement total-score subscription body is empty in this recovered range. Optional postload precedes identical PC/non-PC GlobalModel binding; only PC in-game resizes telemetry to HUD. Returns self. No actual build identity/telemetry/native behavior is inferred.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/91`.

  Archived evidence ID: `archived-record-00036` at JSON pointer `/units/100`; file SHA-256 `279ba12c6a1d4cfd1fb6c7e030a47694d4ee3982256bb21a0b3aa6909aef143b`; selected record SHA-256 `1acbb75d29d7def1f4fccb36727a45b3f2f74c5b7a4de9cff2bbc37c64439b43`.

- `hmh07-lua-follow2:215` (original lines 3932-3932, 3932-3932): Reads the current map story, forwards it to the native selected-story call, then creates/sets the controller selectedZMStory model. The shared preview caller remains qualified and this performs no Zombies gameplay reconstruction.

  unknowns: &#91;"Original PS4/source exact-version and original Lua/VM binding remain unverified.", "Effective enum/mode/platform/settings and asset/model/storage data are unavailable.", "Native/LUI event/subscription/timer dispatch, cleanup guarantees and errors not shown in selected source remain open.", "Unavailable service/server code is not reconstructed or counted."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/92`.

  Archived evidence ID: `archived-record-00028` at JSON pointer `/units/214`; file SHA-256 `2f4ecc3aabb5072135e148ef5782181882bd3b940908913a20bf258d3754185e`; selected record SHA-256 `e394c89fdcba4aca0f5db3c0d16cac218e46b0e351bdea75a7e2bb25e328013a`.

- `hmh07-lua:120` (original lines 56-65, 56-65, 56-65): If Filters is truthy, returns #Filters>1; otherwise returns the original falsey Filters value. Lua0 is truthy, so the intermediate length check does not suppress empty lists; an empty table produces false. No registration or mutation.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/93`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/119`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `940be0d4af525c50fe6aa0acb5406743efb806d0d6ff455afb231228a3f31ceb`.

- `CoD.DirectorUtility.SaveCurrentPlaylistForMainMode` (original lines 3561-3578): No standalone body contract is available in this selected summary. Available classification: shared_Blackout_or_BO4.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/94`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/80`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `5a2b2fb78ee350edc1446422c03c9b3dbccf8edec9c4a1c88e181506e303b652`.

- `hmh07-lua-follow6:002` (original lines 4956-4956, 4218-4218): 1 exact selected callable source contracts; 1 separate state groups. Qualified source table/export/call connections only. Old body/reader/writer records retained unchanged; no original/runtime/acceptance credit.

  unknowns: &#91;{"kind": "original_build", "status": "unverified", "reason": "No original PS4 bytecode-to-source match or target VM/loader proof."}, {"kind": "data_assets_settings", "status": "unverified", "reason": "Literal identifiers/expressions known; actual native-return data/assets/effective settings unavailable."}, {"kind": "service_server_runtime", "status": "unverified", "reason": "No service/server source, account/network semantics or game runtime execution."}, {"kind": "loader_lifetime", "status": "unverified", "reason": "require/import order and proxy assignment source only; circular loader/global overwrite/environment lifetime unknown."}&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/95`.

  Archived evidence ID: `archived-record-00056` at JSON pointer `/units/1`; file SHA-256 `9b5470295d8bc5b945061358d29d8430f5da2392ccde6abf20deb11b8b9c027f`; selected record SHA-256 `8dc05ae69111c0470a39431905f0c47764dd11a1d86d3e41b54eefec295586b3`.

- `hmh07-lua-follow3:298` (original lines 3644-3644, 3644-3644, 3644-3644): Returns for mode_invalid. Collects images for standard engine game types and maps matching supplied session mode; adds map image only when its type matches hash_0 type. Replaces cached ForceStreamedImages with ForceStreamHelper(old,new set). Returns GetLocalizedMapValue(mapName,mapName,empty string) directly.

  unknowns: &#91;"Original PS4/source match, original Lua bytecode and VM/decompiler fidelity remain unverified.", "Effective enum/dvar/settings, assets/localization/model/DDL/storage/playlist data remain exact external inputs; requested persistence/network/service effects are not successful execution proof.", "A field/method/import/spelling or other-file local alone does not bind a provider. Unknown identities remain unresolved rather than declared unavailable.", "Native model/event/timer/wrapper invocation, delivery, error/cleanup/lifetime and unavailable original server behavior are outside this source packet.", "No independent correctness review, acceptance, original-build or function-completion credit is recorded."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/96`.

  Archived evidence ID: `archived-record-00003` at JSON pointer `/units/297`; file SHA-256 `a63852530df9189721a410c240a42967af6648aa0fca4e70325b17a1e677ebb7`; selected record SHA-256 `c46106a0104a9e94757d2170635b6e190242ef17ee72eb3795ccf81250b0f67f`.

- `hmh07-lua:119` (original lines 8-55, 8-55, 8-55): Registers DirectorFilters list provider. Its callback builds tab models/properties from Filters, marking selectIndex for an equal card.playlist only outside Featured. The compared local is getplaylistid() when FocusFeaturedFiltered is falsey and the literal false sentinel otherwise; a false-valued card.playlist can therefore match on the filtered path. No validated playlist type excludes that case here. It may append ArenaNews only in arena, then returns the list. Registration does not invoke its action values; runtime provider delivery and exact playlist set remain external.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/97`.

  Archived evidence ID: `archived-record-00285` at JSON pointer ``; file SHA-256 `9277b835037b66b516aa2b4ec1ddb34d6d9822c4f35c3ba3276ae889c123ef62`.

- `CoD.DirectorUtility.LoadPreferredPlaylist` (original lines 3550-3559): No standalone body contract is available in this selected summary. Available classification: shared_Blackout_or_BO4.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/98`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/79`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `e5510f4f2c9703d2547ea67f144255d1eba45e2728d6894d8b139b613d0da5af`.

- `CoD.DirectorUtility.GetDirectorFiltersCardsForMode` (original lines 3352-3399): No standalone body contract is available in this selected summary. Available classification: shared_Blackout_or_BO4.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/99`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/73`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `15974751fffc5b41fd8247a2834f3365feaf368525bfb025b20e0eef7689466b`.

- `hmh07-lua-follow8:002` (original lines 5496-5496, 5495-5497, 5496-5496, 2471-2471, 2466-2478, 2471-2471, 2471-2471, 2469-2469, 2466-2478, 2469-2469, 2469-2469, 2454-2454, 2449-2464, 2454-2454, 2454-2454, 2452-2452, 2449-2464, 2452-2452, 2452-2452, 2621-2621, 2480-2678): Reject an item index <= EmptyItemIndex or a falsey attachment list; otherwise build and return a fresh ordered list of converted attachment indices >= EmptyItemIndex. Create mode-to-slot-order table. Symbolic ZM->LoadoutSlotOrderZM, MP->LoadoutSlotOrderMP, CP->LoadoutSlotOrderCP, WZ->LoadoutSlotOrderMP. Create LoadoutPaintjobSlots.structs.primary.keys and .secondary.keys as separate nested tables, each with the one literal string paintjobSlot. Assign symbolic hash literal default_specialist_equipment to DefaultSpecialistEquipment.

  unknowns: &#91;"Exact selected recovered Lua source only, conditional module/caller bindings. Original loader/global overwrite/VM/native/DDL/settings/assets/service/server/PS4 behavior remain unverified. No independent review, acceptance, function completion or runtime credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/100`.

  Archived evidence ID: `archived-record-00045` at JSON pointer `/units/1`; file SHA-256 `0c981d5eb446fe3dd44845673b101548cf36172da6abd92475497ba0faf30ce0`; selected record SHA-256 `0e0b8ac6edf15d211b52dba253d709535489834d466af86a7c2510c9a3d58db6`.

- `hmh07-lua:151` (original lines 4810-4822, 4810-4822, 4818-4818, 4835-4844, 4811-4811, 4810-4822): Obtains client list, then in Live with valid matching-mainmode playlist returns AllMembersHaveAMapInPlaylist(clients,playlist). Otherwise false. Despite its name it delegates map ownership semantics; no claim of every DLC being owned is supported by this wrapper alone.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/101`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/150`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `157b189af22e7bedc5d16075298bd7ea351647b0079151b3321c1ca657de4c65`.

- `hmh07-lua:231` (original lines 4646-4646, 4646-4656, 4349-4349, 4349-4354, 3683-3683, 3683-3686, 3105-3105, 3105-3108, 4337-4337, 4337-4347, 5160-5160, 5160-5169, 4972-4972, 4972-4974, 4760-4760, 4760-4768, 4658-4658, 4658-4664, 4168-4168, 4168-4170, 4058-4058, 4058-4065, 3742-3742, 3742-4056, 3622-3622, 3622-3627, 3580-3580, 3580-3620, 3037-3037, 3037-3046, 3048-3048, 3048-3057, 2962-2962, 2962-2975, 3145-3145, 3145-3148, 3032-3032, 3032-3035, 3093-3093, 3093-3103): Supplied caller anchor is the Director factory definition itself, so external invocation/HMH menu navigation is unproven. Conditional constructor creates menu, setups default-focus callbacks/any-controller/offline-screen/build-info/companion-app/contracts model, then builds theater/custom/training/arena/public/private/pregame/select and shared/PC-looking children. Direct construction is not authority to reconstruct every other-mode child. Child menu_loaded wrappers use local/super menuLoaded, conditional non-PC safe-area sizing, then dispatch only if unhandled. State predicates: HideForGameStart from LobbyRoot hideMenusForGameStart1; ShowSelectKorea15Plus requires PC+Zombies+opaque Korea eligibility; other states delegate exact DirectorUtility ShowDirectorSelect/Pregame/Private/Custom/Arena/ArenaMatchmaking/Theater/Public/Training. lobbyNav/showSelect/hide flags reevaluate state; network/client/input/xuid/time/spinner/stage/session changes refresh button state. unused_gamepad_button invokes LobbyAddLocalClient(event.controller or owner) then dispatches children. Non-PC Start opens StartMenu_Main; non-PC social requires online/nonLAN/nonguest/allowed/not-demo-disabled/not-training, while PC select Triangle activates featured. Square branches offline-demo LAN hold behavior or nonPC select featured activation. Escape/mouse-keyboard and Circle/gamepad have separate ordered chains: hide preview, clear selected client, cancel/leave applicable custom/arena/theater/public states subject to spinner/timer/host/eligibility, or PC select quit. Duplicate preview branches are preserved and may be shadowed by earlier identical predicates; no guessed simplification. Back opens AAR only when CanShowAAR and refreshes prompt. RTrigger gestures requires dvar lobby_gestures_enabled plus opaque hash_61E20A632CB63092; then alias/preserve-button/open selector. setState CallOriginalFirst hook conditionally opens AAR/refreshes contract/client updates or initializes training; external predicates keep non-HMH internals conditional. Close CallOriginalFirst hook clears saved state and OnDirectorClose; class __onClose registered via CallOriginalSecond outside selected body remains dependency. lobby room/isMatchmaking callbacks refresh room; hideMenusForGameStart1 plays hide clip+loses focus/hides cursor,0 plays default/unhides cursor. menu_loaded then optional restore/postload; PC branch additionally key-color/friends/Korea/navigation/ZM-availability hooks, console branch DirectorUtility.PostLoad only. Exact default-focus registrations occur at end, then self returned. No live lobby/account action was executed; backend/model/enum/native dispatch, actual visibility and clip/close bodies remain open.

  unknowns: &#91;"Original Lua-to-PS4 CUSA11100 build binding and bytecode/VM/decompiler fidelity unverified.", "Effective HMH settings, enum values, model/data production, LUI state arbitration, event delivery/ordering/cancellation, assets, storage/DDL, networking/service behavior remain explicit gaps where called.", "External helper bodies not selected here are dependencies only; no nil/error recovery assumed beyond visible source. Named LUI override APIs are preserved; no original/new callback ordering is guaranteed without their source contract.", "No independent correctness review, retail execution or function completion credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/102`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/230`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `1f6648fc2dcfb6edc6f0e1cd2c5c68e770130fb98c071889a8d28be510874dcf`.

- `hmh07-lua:122` (original lines 849-864, 849-864, 849-864): Outside Live returns hash_0. In Live reads playlist info and returns a truthy name; recovered missing-info/name path only assigns hash_0 without returning it, so falls through nil. Preserve that source distinction rather than inventing a default return.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/103`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/121`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `6579c9e911d1542fd47b00140878c7d564a7d1118cc80c34d85e459843a80c53`.

- `hmh07-lua-follow1:050` (original lines 4966-4966, 3674-3674, 2508-2508, 4966-4966, 4966-4966, 4964-4970, 3674-3674, 3674-3674, 3673-3675, 2508-2508, 2508-2508, 2480-2678): Reuse stopped common/character/preview/XP caller facts: several ZM-named children are constructed unconditionally in shared recovered source, so names alone do not exclude these calls. Difficulty image only selects the four-entry difficulty array for LAN zclassic outside offline custom; otherwise transparent. Localized map name has LAN tutorial/trial special cases then generic map fallback. Hide preview resets three widget paths to CoD.NOTHING, shown/info false and item fields empty/hash0. IsOfflineCustom compares initialized model to CUSTOM_GAME. Preview index getter conditionally resolves item name/desc/image, localizes xhash name and forwards info. Three show helpers select current map story, set respective widget path and shown true. Lobby-client subscription is added only if no saved subscription, rebuilding the ZM character list on membersChanged. IsDoubleNP excludes in-game tutorial, then checks native zombies event, else dvar>1. Its supplied XP-widget visibility also requires IsZombies/live, so that edge is only conditionally excluded given an original mode proof, not globally excluded here. No unrelated Zombies gameplay or backend grants are reconstructed.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/104`.

  Archived evidence ID: `archived-record-00036` at JSON pointer `/units/49`; file SHA-256 `279ba12c6a1d4cfd1fb6c7e030a47694d4ee3982256bb21a0b3aa6909aef143b`; selected record SHA-256 `8e4d2baa240bbee865f12c5207ff6f9531a3b7fb6120519865bfdeec75a5d862`.

- `hmh07-lua-follow4:030` (original lines 4252-4257): Builds the trial countdown. A nonnil WarzoneTrialInfo.countdown_timer is formatted for text. Hidden is not IsGameTrial. After optional PostLoadFunc it requests EnableTrialTick before returning. Creates self via LUI.UIElement.new, SceneBlur via LUI.UIImage.new, NoiseTiledBacking via LUI.UIImage.new, Tint via LUI.UIImage.new, StoreCommonTextBacking via CoD.StoreCommonTextBacking.new, TrialWidget via CoD.TrialWidget.new, TrialText via LUI.UIText.new, TrialCountdownText via LUI.UIText.new, FrontendFrame02 via LUI.UIImage.new, CommonCornerPips via CoD.CommonCornerPips01.new. Stores state predicates Hidden; their body effects require state-system evaluation.

  unknowns: &#91;{"kind": "original_build", "gap": "Recovered-source revision is pinned; original PS4 build/byte/VM/native binding remains unverified."}, {"kind": "effective_data_settings_assets", "gap": "Engine/model/Dvar/asset/data requests do not supply effective runtime values, contents or ownership."}, {"kind": "server_service_persistence", "gap": "Unavailable authoritative server/service/provider code and successful persistence remain unavailable; not reconstructed or counted as completed."}, {"kind": "runtime_callback_lifetime", "gap": "Original loading, table overwrites, callback delivery/order, timings, state selection and UI cleanup are not runtime-proven."}&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/105`.

  Archived evidence ID: `archived-record-00004` at JSON pointer `/units/29`; file SHA-256 `52df95eaa9f17f90427f6313acbc648c9bdffa0602f6444566bbe8fa1a54ba59`; selected record SHA-256 `1a5a06a65b289ded4619d3795a358c65251cfda73190a292c9f2ba48ae6f696d`.

- `hmh07-lua:147` (original lines 4574-4582, 4574-4582, 4574-4582): Returns empty string when global playerCount<=supplied maximum, otherwise localizes the max-party warning with that maximum. Missing/nonnumeric values are not guarded.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/106`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/146`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `a5264c9aa9d2c82251b63ae7953762228385f6e988e9520aa9df80ca6d36cb41`.

- `hmh07-lua:058` (original lines 3380-3380, 3380-3380): Looks up LobbyMainModeData&#91;input&#93;; returns its truthy eMode. Missing entry or falsey eMode falls through after assigning nil and has no explicit return. The mapping table and enum values are external, so no numeric Warzone value is invented.

  unknowns: &#91;"Exact source-to-original-PS4/build match and decompiler fidelity unverified.", "Native LUI/Engine/VM/model ownership, callback delivery/order, cancellation, assets/localization/settings/DDL/storage/network/services and unavailable server code remain unverified where used."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/107`.

  Archived evidence ID: `archived-record-00040` at JSON pointer `/units/57`; file SHA-256 `9d3ed6530ff821234291a78ec78dcd26aabc639214372a07cedc6561cc12382d`; selected record SHA-256 `3f8b72f0b901d5c520395172a467fdc967687a88ca57f69c62260224062fec9f`.

- `hmh07-lua-follow7:001` (original lines 5496-5496, 5495-5497, 5496-5496, 2471-2471, 2466-2478, 2471-2471, 2471-2471, 2469-2469, 2466-2478, 2469-2469, 2469-2469, 2454-2454, 2449-2464, 2454-2454, 2454-2454, 2452-2452, 2449-2464, 2452-2452, 2452-2452, 2621-2621, 2480-2678): Look up the item-name hash in the first loot table; query the second only when the first result is falsey or the hash_0 sentinel. Return the second/first truthy result or hash_0. Assign a fresh outer table with hash-key ar_galil_t8 mapping to a fresh two-element sequence of symbolic mode_zombies then mode_warzone enum reads. This is a source default list, not proof of an actual unlock or original enum/item hash value.

  unknowns: &#91;"Exact selected recovered Lua source only, conditional module/caller bindings. Original loader/global overwrite/VM/native/DDL/settings/assets/service/server/PS4 behavior remain unverified. No independent review, acceptance, function completion or runtime credit."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/108`.

  Archived evidence ID: `archived-record-00106` at JSON pointer `/units/0`; file SHA-256 `18e061e5ee7b1c2bc739ab68607b07765f3b9de61ca899283d64f04ffa0fc469`; selected record SHA-256 `240cd20f30f7a067ffb93b31bd68cb0c77174f19422db3e4ccf183017f353064`.

- `CoD.DirectorUtility.CreateFilterCards` (original lines 2480-2678): No standalone body contract is available in this selected summary. Available classification: shared_Blackout_or_BO4.

  limit: Recovered-source statement only. Native behavior, original bytecode fidelity, server behavior and PlayStation compatibility are unverified.

  Complete explanatory fields: [exact projection](../../provenance/documentation/9ddbbd0d7f9a22ae-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/9ddbbd0d7f9a22ae.json) at JSON pointer `/claims/109`.

  Archived evidence ID: `archived-record-00001` at JSON pointer `/records/72`; file SHA-256 `807e03123fd761e66758e907a17d020b4437649f710f6cd5998282d56421d366`; selected record SHA-256 `ca16d0b8b155ca39947797a77a510de9eb8dc0f739a60794e9d213eb3b272231`.
