# hashed/33618c4b3a4dfe62.lua

Project-added notes. See the [code](../../src/lua/hashed/33618c4b3a4dfe62.lua).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `1a46c72b710c1820b63f72d22654f570286eee0b`. Original SHA-256: `2ceb393d5f1b1e72d5cd7da5235be8265141526b52fa8324d0e3f591717702a7`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/33ceade7223aee0c.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `hmh07-lua-follow1:085` (original lines 9-182): Constructs kills, compass, WZ HUD menus, talker/VOIP and game-status children. Talker Visible requires spectator flag; full VOIP HudStart requires wzHardcore and not spectator, enemies-only HudStart AlwaysTrue and not wzHardcore. Status Right is AlwaysFalse and Left AlwaysTrue; filters split gameInformation/hudGameStat with exact HUD-left datasource. Parent HideForCodCaster and HideForSpawnSelect retain profile/show-model guards. scriptNotify dispatches create_prematch_timer or exact holding-pen hash with5000 helper duration. Close/postload precede custom WZ menu focus and quick-inventory auto-close setup5000, returns self. Source predicates and model consumers do not reconstruct VOIP network or match timer producers.

  unknowns: &#91;"Per-body nil/error/return/lifetime limits are explicit in ordered operations; no universal cleanup, cancellation or exception recovery is inferred.", "Recovered-source fidelity defects remain visible; saved AST/receipt checks are not independent correctness review."&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/33ceade7223aee0c-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/33ceade7223aee0c.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00036` at JSON pointer `/units/84`; file SHA-256 `279ba12c6a1d4cfd1fb6c7e030a47694d4ee3982256bb21a0b3aa6909aef143b`; selected record SHA-256 `4adc500e127b7b3dc320ce51541f186e748edcb255dc6f71bcfae65cd6159944`.
