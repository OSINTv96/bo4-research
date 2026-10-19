# hashed/6f4f7efec9bbee3c.lua

Project-added notes. See the [code](../../src/lua/hashed/6f4f7efec9bbee3c.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `9d95cc12d197332c06dee293ab45e0dc1eef2e7f45ac3c23ef964c1f10dc9735`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/16d5f2bbcfaaaeb8.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua-follow4:098` (original lines 7-30, 7-30, 7-30, 7-30, 7-30, 7-30, 8-8, 13-13, 14-14, 19-19, 26-26, 7-30, 7-30): Constructs CoD.FinalKillcamPlayerInfo with the supplied menu/controller/layout values; its exact visual/data fields, condition closures, hook requests and return are retained below. Creates self via LUI.UIElement.new, blurbackplate via LUI.UIImage.new, blackplate via LUI.UIImage.new.

  unknowns: &#91;{"kind": "original_build", "gap": "Recovered-source revision is pinned; original PS4 build/byte/VM/native binding remains unverified."}, {"kind": "effective_data_settings_assets", "gap": "Engine/model/Dvar/asset/data requests do not supply effective runtime values, contents or ownership."}, {"kind": "server_service_persistence", "gap": "Unavailable authoritative server/service/provider code and successful persistence remain unavailable; not reconstructed or counted as completed."}, {"kind": "runtime_callback_lifetime", "gap": "Original loading, table overwrites, callback delivery/order, timings, state selection and UI cleanup are not runtime-proven."}&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/16d5f2bbcfaaaeb8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/16d5f2bbcfaaaeb8.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00004` at JSON pointer `/units/97`; file SHA-256 `52df95eaa9f17f90427f6313acbc648c9bdffa0602f6444566bbe8fa1a54ba59`; selected record SHA-256 `56cb02793bc47b2f10aea97b14877a021bbd49282fb3157dad6ecf528f70ab71`.

- `hmh07-lua-follow3:040` (original lines 7-30): Constructs CoD.FinalKillcamWidget from the displayed menu/controller/layout arguments. Creates PlayerInfo as CoD.FinalKillcamPlayerInfo.new, CODGradientBacking as CoD.CODCasterTeamBaseGradient.new, blurbackplate as LUI.UIImage.new, BlackForeground as LUI.UIImage.new, topbarblack as LUI.UIImage.new, killcamTitle as CoD.PLayOfTheMatchTitle.new, AttackerPlayerCard as CoD.PlayOfTheMatchCallingCard.new. At66 it requests registration of the looked-up self.__onClose value; this constructor owns no inline callback and does not establish captured constructor menu/controller/widget references. The separate __onClose246–251 receives f20_arg0 and, if invoked and preceding accesses/calls succeed, requests its PlayerInfo:close(), CODGradientBacking:close(), killcamTitle:close(), then AttackerPlayerCard:close() in that order. Actual registration delivery, original wrapper order, successful child cleanup, lifetime and provider/native/VM effects remain unknown. Optional PostLoadFunc and the tail return occur only if reached. The ordered effect contract retains every property, model, visual, navigation, callback and return mutation in source order; returning self is not proof the original game loads this widget.

  unknowns: &#91;"Original source-to-PS4/VM/native/loader identity and bytecode fidelity are unverified.", "Effective settings, assets/tables/model schemas, server/service implementation and callback delivery/lifetime are unverified.", "Exact source request semantics do not prove rendering, networking, persistence, progression or game behavior.", "Public reuse is the frozen manager audit only; no worker web/repository discovery was performed."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/16d5f2bbcfaaaeb8-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/16d5f2bbcfaaaeb8.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00207` at JSON pointer ``; file SHA-256 `fc23e12d163fdc259f74f5ee864035d19580875af5322af0d3cf7d9864545caf`.
