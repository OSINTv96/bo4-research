# hashed/703bc1b69f98130d.lua

Project-added notes. See the [code](../../src/lua/hashed/703bc1b69f98130d.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `fb5dec597488c9acc386174af216512ffd312fbdc2f4da2d5fa024e14b8f54cc`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/ef79d45c6fc2b6fc.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua-follow1:098` (original lines 10-55): Builds StartMenu_Main, initializes data and absent WZ-start/draft models, panels/tab frame/safe area/PC quit/Korea descriptors. TabWidget model changes changeFrameWidget only when nonnil. State order is frontend, zombies, campaign, WZ in-game, generic in-game. Menu-loaded delegates local/super, plays entry, fetches fileshare slots and sets heading; close-all/migration go back. PC WZ occlusion closes splitter. Circle/back branches preserve frontend cleanup, console/PC and demo resume paths; Triangle/weapnext/weapprev and PC slot bindings use exact WZ/in-game/non-demo gates; F1 class action is AlwaysFalse; Start always refreshes/goes back; square stats filter, PC contextual quit and PC start-Warzone remain individually guarded. Label callbacks can return false for working actions. Close first-hook clears saved state; spectator changes refresh tabs. menu_loaded/state restoration precedes same-class close hook/postload, optional MP class-slideout and safe-area sizing, then returns self. No quit/weapon request was executed during this work.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/ef79d45c6fc2b6fc-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/ef79d45c6fc2b6fc.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00155` at JSON pointer ``; file SHA-256 `cd1fa3f4247464fcba144bac4797828cfe9de5c9b4183ac87fa5137b44f6100d`; selected record SHA-256 `043bd05a037263640608edf72edda482a0ed4c212dd6cf6c23b6d2311c4433c4`.

- `hmh07-lua-follow1:144` (original lines 10-55): Constructs the inventory menu's weapon, inventory/ammo/attachments, health, gear, storage, equipment, resources, status and armor-plate views plus PC-specific/fake elements as written. Focus/model hooks update inventoryDescription and tooltips. Button and contextual providers gate drop/split/current-weapon detach actions by input type, scoreboard visibility, NONE ID and stackCount, preserving true versus nil/false returns. Open/close overrides maintain inventory.isOpen, scriptNotify consumes its matching argument then goes back, and the saved override-removal closure is retained. Final dual-weapon preferences replace selected widgets with fakes. All nested actions are deferred bindings; no inventory command success is proved.

  unknowns: &#91;"No actual callback delivery, cancellation-after-close, successful native mutation or service response is proved.", "Recovered source defects, nil fallthroughs, repeated/replaced registrations and opaque aliases are preserved rather than repaired.", "Public-reuse investigation is inherited from frozen archived-record-00026; this author performed no outside research."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/ef79d45c6fc2b6fc-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/ef79d45c6fc2b6fc.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00144` at JSON pointer ``; file SHA-256 `68397937adfed21a627e254f159c4cdd36569689fb5eac49dd0715bc91490cfa`.

- `hmh07-lua-follow3:199` (original lines 22-22, 22-22, 22-22): Creates CoD.PC_Korea_Menus_15ContentDescriptors_Icons using LUI.UIElement.new( f1_arg2, f1_arg3, f1_arg4, f1_arg5, f1_arg6, f1_arg7, f1_arg8, f1_arg9 ). Initializes and attaches children in source order: KoreaDrugReferenceIcon, KoreaCurrencyIcon, KoreaViolenceIcon, KoreaRating15Logo, KoreaRating18Logo, KoreaStrongLanguageIcon. Returns self after the shown optional hooks and setup. Native UI/model/asset effects and callback delivery are external contracts.

  unknowns: &#91;"Original PS4/source match, original Lua bytecode and VM/decompiler fidelity remain unverified.", "Effective enum/dvar/settings, assets/localization/model/DDL/storage/playlist data remain exact external inputs; requested persistence/network/service effects are not successful execution proof.", "A field/method/import/spelling or other-file local alone does not bind a provider. Unknown identities remain unresolved rather than declared unavailable.", "Native model/event/timer/wrapper invocation, delivery, error/cleanup/lifetime and unavailable original server behavior are outside this source packet.", "No independent correctness review, acceptance, original-build or function-completion credit is recorded."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/ef79d45c6fc2b6fc-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/ef79d45c6fc2b6fc.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00003` at JSON pointer `/units/198`; file SHA-256 `a63852530df9189721a410c240a42967af6648aa0fca4e70325b17a1e677ebb7`; selected record SHA-256 `fcd2e36a9068c5b5ebb33ad9063e23787239637a9dca9ad1026db19690cb8134`.

- `hmh07-lua-follow3:024` (original lines 17-17, 17-17, 17-17): Constructs CoD.PC_Korea_ContentDescriptors_Icons from the displayed menu/controller/layout arguments. Creates KoreaViolenceIcon as LUI.UIImage.new, KoreaRating18Logo01 as LUI.UIImage.new. The ordered effect contract retains every property, model, visual, navigation, callback and return mutation in source order; returning self is not proof the original game loads this widget.

  unknowns: &#91;"Original source-to-PS4/VM/native/loader identity and bytecode fidelity are unverified.", "Effective settings, assets/tables/model schemas, server/service implementation and callback delivery/lifetime are unverified.", "Exact source request semantics do not prove rendering, networking, persistence, progression or game behavior.", "Public reuse is the frozen manager audit only; no worker web/repository discovery was performed."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/ef79d45c6fc2b6fc-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/ef79d45c6fc2b6fc.json) at JSON pointer `/claims/3`.

  Archived evidence ID: `archived-record-00003` at JSON pointer `/units/23`; file SHA-256 `a63852530df9189721a410c240a42967af6648aa0fca4e70325b17a1e677ebb7`; selected record SHA-256 `0ed75babd756aa7ad4aca945344deb9fa12ba8fda43779445f5e8299c7cd4592`.

- `hmh07-lua-follow2:059` (original lines 10-55, 10-55): Constructs CoD.PC_Quit_Korea_Container.new from its exact supplied layout/controller/menu arguments; creates/attaches PCKoreaContentDescriptorsContainer. Registers close ownership; calls PostLoadFunc only if truthy; returns self only at the displayed return. Callback/state/clip bodies are deferred, and the exact source effects below define their receiver, data and branch contracts.

  unknowns: &#91;"Exact original PS4/source version matching, recovered Lua/VM fidelity and global/native/LUI provider identity remain unverified.", "Model/storage/DDL/assets/localization/dvar/enum values, callback delivery/cancellation/error behavior, native networking and unavailable service/server code are separate inputs.", "Other-file locals are not providers by spelling. Exact qualified global declarations are source candidates until loader/table identity and caller conditions bind them.", "No implicit nil/type checks, exception recovery, timer/model disposal, idempotence or guarantee that later effects run after an error is added."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/ef79d45c6fc2b6fc-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/ef79d45c6fc2b6fc.json) at JSON pointer `/claims/4`.

  Archived evidence ID: `archived-record-00028` at JSON pointer `/units/58`; file SHA-256 `2f4ecc3aabb5072135e148ef5782181882bd3b940908913a20bf258d3754185e`; selected record SHA-256 `1b87ea7a3de4098bfee9c5aa50ef0473060bfb43b778308e07019d0b191d6342`.
