# hashed/7370c75599db15e7.lua

Project-added notes. See the [code](../../src/lua/hashed/7370c75599db15e7.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `6ebe55ca549e44fcba7b2938d35b10d1ab0f7b1506ddd8ea0d435cdb68aa1191`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/ebdc9dbb201f7ed1.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua-follow1:046` (original lines 9-39): Initializes six controller progress/status models only when absent, then creates dynent/heal/revive/being-revived/bleedout progress and text/prompt children. Healing requires powerRatio>0, ability in-use and player not dead; Reviving uses reviveProgress>0, BeingRevived equality1, CowardsWayOut exact setting plus last-stand/not-ended/not-finished guards, Deposit both dynent progress and depositing>0. Ratio updates write the exact shader data; reviveProgress callback delegates smooth interpolation only for nonnil values. All status changes request state reevaluation. Close registration/postload precede SetupReviveProgressBar and SetupBleedoutProgressBar, then self return. This consumes combat state and does not implement revive/deposit timing or native cancellation.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/ebdc9dbb201f7ed1-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/ebdc9dbb201f7ed1.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00036` at JSON pointer `/units/45`; file SHA-256 `279ba12c6a1d4cfd1fb6c7e030a47694d4ee3982256bb21a0b3aa6909aef143b`; selected record SHA-256 `fdaa334df17588399c67f6d8177ad2c96cabf3507c4db13e68a15815bd54d78f`.

- `hmh07-lua-follow2:199` (original lines 9-39, 9-39, 9-39, 23-28, 25-25, 34-34, 38-38, 10-10, 16-16, 26-26, 32-32, 11-11, 19-19, 20-20, 21-21, 22-22, 23-23, 35-35, 9-39): The constructor requests the item-name widget and registers ItemName:subscribeToGlobalModel(controller,"PlayerAbilities","playerGadget1.name",callback) at23–28. Only if that callback is delivered and model:get() returns a nonnil value (including false), it requests LocalizeIntoStringIfNotEmpty(@"warzone/using",value) as the nested argument to ItemName:setText. The selected helper187–198, in the recovered ordinary Lua path, returns literal "" for exact empty input: empty strings are truthy, so its shown else reaches194. Nonempty input reaches an opaque Engine&#91;@"hash_4F9F1239CFD921FE"&#93; argument request/assignment at197, then the helper ends without an explicit return of that result. Preserve this fallthrough, rather than inferring returned formatting/localization or displayed text. Original VM/decompiler fidelity, provider/result/rendering semantics and actual delivery remain unknown; preceding evaluation/call failures may prevent later requests. The shown direct statements read the gadget-name model and contain no direct gadget-use request. Opaque child/model/provider calls and optional direct PostLoadFunc34–36 prevent a claim that the whole invocation cannot start gadget use.

  unknowns: &#91;"Original PS4/source exact-version and original Lua/VM binding remain unverified.", "Effective enum/mode/platform/settings and asset/model/storage data are unavailable.", "Native/LUI event/subscription/timer dispatch, cleanup guarantees and errors not shown in selected source remain open.", "Unavailable service/server code is not reconstructed or counted."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/ebdc9dbb201f7ed1-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/ebdc9dbb201f7ed1.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00545` at JSON pointer ``; file SHA-256 `d4f4ffa011b145f9465c82a1b9403cb583cd40c7743bf08acce9355b1635f0cc`.
