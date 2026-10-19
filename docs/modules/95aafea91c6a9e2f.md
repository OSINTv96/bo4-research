# hashed/50d6ed3ff89b4c44.lua

Project-added notes. See the [code](../../src/lua/hashed/50d6ed3ff89b4c44.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `726f348e0395c05b4df30f694b0b186484ee686ec593be99b288dce38f5c9e1c`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/95aafea91c6a9e2f.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua-follow1:042` (original lines 10-127): Stopped Director constructs this shared custom lobby child. Initializes selected gametype/map/update/player-count and local ZM models, builds party/map/setup/start/header/preview/lab controls. Map selection requires host and no countdown; offline-ZM-private opens a different chooser, otherwise generic map/game chooser. Host Start launches only if every client owns DLC, else opens maps-not-enabled popup; both action branches return true while label callbacks return false. CustomGames action chooses ZM custom mutation or non-ZM custom-games overlay. State family preserves ZM live/LAN/host/offline predicates, WZ IsWarzone, and PC variant. Model/session/focus callbacks refresh state/labels/descriptions/draft models; the repeated ShowDirectorCustom elseif is retained literally. LobbyNav focus changes prioritize ZM custom host tutorial, then custom host StartButton, then ZM custom nonhost home. Close registration/postload precede platform-specific preGameType and default-focus update. Every nested function/return/guard remains below; no ZM-only gameplay or real launch is claimed.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/95aafea91c6a9e2f-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/95aafea91c6a9e2f.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00094` at JSON pointer ``; file SHA-256 `b7bc897872c9d1f0e13fa377f6ce9790d674551ff1a9a1e06a12be723cb2014c`; selected record SHA-256 `1869abf568bc2ec05339bbeeab4867bfc96dae74546e4ecc60186659eb44c367`.

Dependency decisions: [exact edge records](../../provenance/dependency-decisions.json). Included callees remain at the bounded static scopes recorded there.

- [AV0367](../../provenance/dependency-decisions/AV0367.json): `src/lua/hashed/50d6ed3ff89b4c44.lua` to `lua/ui/uieditor/menus/social/social_inviteplayerspopup.lua`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.
