# hashed/4017493401b24b33.lua

Project-added notes. See the [code](../../src/lua/hashed/4017493401b24b33.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `d183cb0a914c0003f7fd787855246f2dffd50fcbf1a14120ca784c48214f8300`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/ebd8e6a0de323f4b.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua-follow6:122` (original lines 59-63, 59-59, 50-50, 4-4, 9-9, 59-63, 59-59, 60-60, 61-61, 62-62, 63-63, 60-60, 61-61, 62-62, 59-63, 60-60, 61-61, 62-62, 59-63): Takes the CoD.DirectorFeatureInteractPrompt instance as f4_arg0. Calls close() with each child as implicit self, in this exact order: Description, buttonPromptImagePC, buttonPromptImage. There are no guards, branches, loops, explicit return values, field resets, timer cancellation or protected error handling in this body. Missing/already-closed children are not checked; an earlier receiver/provider error may prevent later closes. The same constructor sets this exact class and registers self.__onClose with CallOriginalSecond. That helper controls wrapping/order/invocation; registration alone does not prove game-time delivery.

  unknowns: &#91;"Effective HMH settings/data/assets, true load/overwrite/class lookup order, original recovered-text fidelity, native callback delivery and service/server implementations remain open.", "Independent correctness review and final game tests remain deferred."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/ebd8e6a0de323f4b-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/ebd8e6a0de323f4b.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00056` at JSON pointer `/units/121`; file SHA-256 `9b5470295d8bc5b945061358d29d8430f5da2392ccde6abf20deb11b8b9c027f`; selected record SHA-256 `51abea19ed7e8eeff9f3a8b3bbde6f9fcc6113ab9d7c9bfabeb6471c899af8ef`.

- `hmh07-lua-follow5:037` (original lines 7-57, 7-7, 25-30, 39-44, 7-57, 7-7, 8-8, 13-13, 28-28, 36-36, 37-37, 49-49, 50-50, 50-50, 59-63, 24-24, 42-42, 53-53, 7-57): local self = LUI.UIElement.new( f1_arg2, f1_arg3, f1_arg4, f1_arg5, f1_arg6, f1_arg7, f1_arg8, f1_arg9 ). Construct, configure and attach child fields in source order: Description, buttonPromptImagePC. descriptionText and alt2_button_image drive description and PC prompt. The separate buttonPromptImagePC child is allocated by LUI.UIImage.new at36; self.buttonPromptImage is assigned LUI.UIElement.createFake() at49. Provider effects remain external. Preserve optional load-hook position, callback registrations and final return exactly as written.

  unknowns: {"provider_or_lexical": &#91;{"source_caller": {"area": "references", "path": "lua/hashed/4017493401b24b33.lua", "line_start": 24, "line_end": 24, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "d183cb0a914c0003f7fd787855246f2dffd50fcbf1a14120ca784c48214f8300", "line_span_sha256": "a56e272efeed492e357c4ef6af2afd5dcb2a5d1a32425a1c334b8869ae466bc4", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "source_symbol": "CoD.DirectorFeatureInteractPrompt.new", "symbol_as_written": "RegisterImage", "statement": "Description:setBackingImage( RegisterImage( @\"hash_7C229CEBABEEAB0E\" ) )", "category": "unresolved_literal_global_or_constructor_provider", "limit": "No binding is inferred from an import, get(), method name or another-file local. Owned closure definitions are in body. Exact source candidate not found in supplied index does not prove source absence."}, {"source_caller": {"area": "references", "path": "lua/hashed/4017493401b24b33.lua", "line_start": 42, "line_end": 42, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "d183cb0a914c0003f7fd787855246f2dffd50fcbf1a14120ca784c48214f8300", "line_span_sha256": "d1e5ecb4806aa7a87ed853426c0be83669cf4c8eaf9e2def13d5e6aa0af4e177", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "source_symbol": "CoD.DirectorFeatureInteractPrompt.new", "symbol_as_written": "RegisterImage", "statement": "buttonPromptImagePC:setImage( RegisterImage( f3_local0 ) )", "category": "unresolved_literal_global_or_constructor_provider", "limit": "No binding is inferred from an import, get(), method name or another-file local. Owned closure definitions are in body. Exact source candidate not found in supplied index does not prove source absence."}, {"source_caller": {"area": "references", "path": "lua/hashed/4017493401b24b33.lua", "line_start": 53, "line_end": 53, "source_revision": "1a46c72b710c1820b63f72d22654f570286eee0b", "file_sha256": "d183cb0a914c0003f7fd787855246f2dffd50fcbf1a14120ca784c48214f8300", "line_span_sha256": "4dbef5997b3a65062e8c8bbfb97d55f505c5f9f18c20af45a45813d428535171", "line_span_hash_convention": "inclusive lines WITH ORIGINAL TERMINATORS"}, "source_symbol": "CoD.DirectorFeatureInteractPrompt.new", "symbol_as_written": "PostLoadFunc", "statement": "PostLoadFunc( self, f1_arg1, f1_arg0 )", "category": "unresolved_lexical_or_global_provider", "limit": "Supplied same-spelled locator candidates did not establish a usable lexical object/scope. Other-file local roots and member assignments were rejected. No target-body semantics or native-provider guess."}&#93;, "source_fidelity": &#91;&#93;, "original_build": "Recovered source is not matched to original PS4 bytecode/build; @0 is not a native address.", "VM_native": "Lua dialect, metatables, native/UI API execution, model dispatch/cancellation and input timing remain unverified.", "data_settings_assets": "Literal references do not supply effective model values, settings, data tables, localization or asset availability.", "server_service": "Online, stats, progression, marketing, lobby and backend behavior are unavailable service boundaries when requested by these exact bodies.", "runtime": "No game, console, account, router, save, native tool or independent review was run."}

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/ebd8e6a0de323f4b-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/ebd8e6a0de323f4b.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00343` at JSON pointer ``; file SHA-256 `aa2af33f30908da33e55f6dbe08195c902486f044ac1d1fe76e743a229ab09f0`; selected record SHA-256 `a1ac981445388826f4cd4234c52118ed28ac61de6ee6fbe8879a8c426873fbe4`.

- `hmh07-lua-follow4:121` (original lines 7-57): Builds a featured-item header, interact prompt, party-leader prompt and double-XP icons. A nonnil name is localized-if-hash then uppercased. ShowForAllClients controls party-leader visibility and small controls parent state. Session/lobby/model callbacks validate them; LastInput on PC hides the interact prompt for KBM and shows it for gamepad. Creates self via LUI.UIElement.new, GamemodeBackground via LUI.UIImage.new, NotFocused via LUI.UIImage.new, Header via LUI.UIText.new, DirectorFeatureInteractPrompt via CoD.DirectorFeatureInteractPrompt.new, PartyLeaderOnlyPrompt via CoD.DirectorPartyLeaderOnlyPrompt.new, DoubleXPCardIconsRightAligned via CoD.DoubleXPCardIconsRightAligned.new, FrontendFrameSelected via LUI.UIImage.new. Stores state predicates Invisible, Small; their body effects require state-system evaluation.

  unknowns: &#91;{"kind": "original_build", "gap": "Recovered-source revision is pinned; original PS4 build/byte/VM/native binding remains unverified."}, {"kind": "effective_data_settings_assets", "gap": "Engine/model/Dvar/asset/data requests do not supply effective runtime values, contents or ownership."}, {"kind": "server_service_persistence", "gap": "Unavailable authoritative server/service/provider code and successful persistence remain unavailable; not reconstructed or counted as completed."}, {"kind": "runtime_callback_lifetime", "gap": "Original loading, table overwrites, callback delivery/order, timings, state selection and UI cleanup are not runtime-proven."}&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/ebd8e6a0de323f4b-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/ebd8e6a0de323f4b.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00004` at JSON pointer `/units/120`; file SHA-256 `52df95eaa9f17f90427f6313acbc648c9bdffa0602f6444566bbe8fa1a54ba59`; selected record SHA-256 `46eae1de3798b9133f9a88f86a48236d291705f404d74337d1447eeac53fc12a`.
