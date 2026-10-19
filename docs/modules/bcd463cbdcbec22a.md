# scripts/weapons/acid_bomb.csc

Project-added notes. See the [code](../../src/scripts/weapons/acid_bomb.csc).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `f4b9a51f8b7fcfcb6d158303d3fd5fff2fcfb6ac`. Original SHA-256: `bb1385661b382555b6b3664112d699f1d0c5598d1720adc8446f535f4244d1a0`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/bcd463cbdcbec22a.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `scripts/weapons/acid_bomb.csc::fx_think` (original lines 44-59): Blinking-light FX loop threaded on the grenade by spawned(). Ordered: (1) self notify(#"light_disable") to kill any prior loop; (2) self endon(#"death", #"light_disable") â€” loop ends on entity death or the light_disable notify; (3) util::waittill_dobj( localclientnum ) waits for dobj readiness; (4) var_18407835 = self.origin captured once; (5) infinite for-loop with interval starting 0.3: each pass calls self stop_light_fx(localclientnum), self start_light_fx(localclientnum), self fullscreen_fx(localclientnum), playsound(localclientnum, #"hash_2bb4a8b02a0d697", var_18407835) at the captured origin, then util::server_wait(localclientnum, interval, 0.01, "player_switch"). Loop-local interval update: interval = math::clamp(interval / 1.2, 0.08, 0.3) so the beacon accelerates from 0.3s down to 0.08s and stays there. Termination only via endon death/light_disable; no other exit.

  unknowns: &#91;"util::waittill_dobj and util::server_wait wait semantics (third arg 0.01 and tag \"player_switch\") are util/native, not resolvable from this span", "Sound #\"hash_2bb4a8b02a0d697\" identity not in catalog", "Whether origin staleness during grenade motion is intentional is unknown"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/bcd463cbdcbec22a-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/bcd463cbdcbec22a.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00102` at JSON pointer `/units/3`; file SHA-256 `bec4988a5459cac825b94dcc33e1b58fc8dc9b791fc0a299fcedfa5c5250bdd0`; selected record SHA-256 `42cdb24c633e3f5c308295345e3cf858fefb9447e1f29413667d51f8d9d693f1`.

- `scripts/weapons/acid_bomb.csc::__init__system__` (original lines 12-15): Client-side (CSC) autoexec system registration for the acid bomb grenade. Sole statement: system::register(#"acid_bomb", undefined, &__main__, undefined) â€” registers namespace system named 'acid_bomb' with undefined init callback and __main__ as the main callback, undefined extra argument. No state reads/writes beyond this registration; no branching.

  unknowns: &#91;"system::register fourth-argument semantics (undefined passed) not resolvable from this span", "runtime registration timing/effect is engine behavior, unverified"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/bcd463cbdcbec22a-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/bcd463cbdcbec22a.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00102` at JSON pointer `/units/0`; file SHA-256 `bec4988a5459cac825b94dcc33e1b58fc8dc9b791fc0a299fcedfa5c5250bdd0`; selected record SHA-256 `8114e1930112c10b5fb9867586f9c0204aee6a419e744e956b0db7ec4e5f2e97`.

- `scripts/weapons/acid_bomb.csc::spawned` (original lines 30-38): Entity-spawned client callback (takes localclientnum). Branch: if self isgrenadedud() -> return (no FX threading for dud grenades). Otherwise: self thread fx_think( localclientnum ) â€” spawns the FX loop coroutine on the grenade entity. No state writes.

  unknowns: &#91;"isgrenadedud is a native predicate; dud conditions not documented in this span", "who/what entity calls spawned (engine grenade spawn callback) is not shown in-file"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/bcd463cbdcbec22a-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/bcd463cbdcbec22a.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00102` at JSON pointer `/units/2`; file SHA-256 `bec4988a5459cac825b94dcc33e1b58fc8dc9b791fc0a299fcedfa5c5250bdd0`; selected record SHA-256 `7ecc583c23e7227c9b47be0ed428ba90af2a2a4a7e2506a77c8d0d7399ec53cc`.

- `scripts/weapons/acid_bomb.csc::fullscreen_fx` (original lines 87-109): Fullscreen/rumble gate called each blink iteration from fx_think. Ordered early-outs: (1) if function_1cbf351b( localclientnum ) -> return; (2) else if util::is_player_view_linked_to_entity( localclientnum ) -> return; (3) if self function_83973173() -> return. Then: parent = self getparententity(); if isdefined( parent ) && parent function_21c0fa55() -> parent playrumbleonentity( localclientnum, "buzz_high" ). Effect: controller rumble 'buzz_high' on the parent entity (e.g. the player holding/viewing the bomb) when all three gates pass. No state writes to level.

  unknowns: &#91;"Definitions of function_1cbf351b, function_83973173, function_21c0fa55 are not in the frozen catalog (unresolved externals); call sites elsewhere assign function_1cbf351b(localclientnum) to 'inkillcam', so plausibly a killcam/spectator-view gate, but semantics are not proven from definition", "util::is_player_view_linked_to_entity native semantics unverified", "Which concrete parent entities pass function_21c0fa55 is unknown"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/bcd463cbdcbec22a-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/bcd463cbdcbec22a.json) at JSON pointer `/claims/3`.

  Archived evidence ID: `archived-record-00102` at JSON pointer `/units/6`; file SHA-256 `bec4988a5459cac825b94dcc33e1b58fc8dc9b791fc0a299fcedfa5c5250bdd0`; selected record SHA-256 `18b722a6a48966ea2255a83b4b361b711db8ae10cd27c641c016e3291df5f743`.

- `scripts/weapons/acid_bomb.csc::stop_light_fx` (original lines 74-81): Stops the light FX handle cleanly. Branch: if isdefined( self.fx ) && self.fx != 0 -> stopfx( localclientnum, self.fx ); self.fx = undefined. No-op when no live handle. This is the per-iteration teardown paired with start_light_fx inside fx_think's loop (toggle-style blink).

  unknowns: &#91;"Whether self.fx can be a stale/invalid handle after entity FX teardown is engine-dependent and unverified"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/bcd463cbdcbec22a-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/bcd463cbdcbec22a.json) at JSON pointer `/claims/4`.

  Archived evidence ID: `archived-record-00102` at JSON pointer `/units/5`; file SHA-256 `bec4988a5459cac825b94dcc33e1b58fc8dc9b791fc0a299fcedfa5c5250bdd0`; selected record SHA-256 `3c1f5b95c61ee6a824637888ce51b939bcf0b6a68d851a04d50f49fa1d04e2d3`.

- `scripts/weapons/acid_bomb.csc::__main__` (original lines 21-24): System main callback for acid_bomb on client VM. Single write: level._effect&#91;#"grenade_light"&#93; = #"weapon/fx8_equip_light_os" â€” installs the grenade light FX alias used later by start_light_fx. __init__system__ passes &__main__ in system::register; actual invocation timing/count remain unresolved; no branches.

  unknowns: &#91;"Exact when __main__ is invoked by system::register (engine dispatch) is unverified"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/bcd463cbdcbec22a-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/bcd463cbdcbec22a.json) at JSON pointer `/claims/5`.

  Archived evidence ID: `archived-record-00749` at JSON pointer ``; file SHA-256 `bec6aea08a425e2a744b11ea7795bec2dc992edfe94b8be67c5ac7e77941a7ff`; selected record SHA-256 `7ef7c72d45565881d3a63d6d18aaae12cb8b3ef1201be5f75109caada2ed4a76`.

- `scripts/weapons/acid_bomb.csc::start_light_fx` (original lines 65-68): Starts the grenade light FX: self.fx = util::playfxontag( localclientnum, level._effect&#91;#"grenade_light"&#93;, self, "tag_fx" ). Reads level._effect&#91;#"grenade_light"&#93; (set by __main__), stores the FX handle on the entity field self.fx. No branches.

  unknowns: &#91;"util::playfxontag return-handle semantics (0 vs undefined when FX fails) are native behavior", "tag_fx assumption on the grenade model is game-data, not verifiable here"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/bcd463cbdcbec22a-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/bcd463cbdcbec22a.json) at JSON pointer `/claims/6`.

  Archived evidence ID: `archived-record-00102` at JSON pointer `/units/4`; file SHA-256 `bec4988a5459cac825b94dcc33e1b58fc8dc9b791fc0a299fcedfa5c5250bdd0`; selected record SHA-256 `1bfa6c99adaa0d2b6eccc876498b77892a963f8ef8fee829cdc90b749f4fc70c`.

Dependency decisions: [exact edge records](../../provenance/dependency-decisions.json). Included callees remain at the bounded static scopes recorded there.

- [AV0239](../../provenance/dependency-decisions/AV0239.json): `src/scripts/weapons/acid_bomb.csc` to `scripts/core_common/math_shared.csc`; include_conditional_source.

  Exact executable reference in a selected bounded caller function, a local call/pointer chain from it, or a Lua module-load entry. Callee source is needed if that candidate path is admitted. Pointer storage is not callback delivery; lexical control-flow feasibility and HMH/runtime admission remain conditional. Whole file retained only as lexical context; other functions are not promoted to HMH requirements.

  Selected callee candidates: `clamp`. Source-only conditional selection; refer to the full edge record for caller lines and gates.
