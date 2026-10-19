# scripts/wz_common/wz_perk_bloody_tracker.csc

Project-added notes. See the [code](../../src/scripts/wz_common/wz_perk_bloody_tracker.csc).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `f4b9a51f8b7fcfcb6d158303d3fd5fff2fcfb6ac`. Original SHA-256: `b1a328b0a48ca5291861f69f252aa30c5e4f9db9b83bcdb3b2e485d24d186f90`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/8bddf70ab1be9be0.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `scripts/wz_common/wz_perk_bloody_tracker.csc::bloody_tracker` (original lines 42-83): Blood-tracker scan loop (threaded on level per connect, never returns). while(true): wait 0.2 (5 Hz). Perk gate: if !function_5778f82( localclientnum, #"specialty_tracker" ) -> continue (opaque unqualified helper; prior notes infer local-player-has-perk-style query); helper not in packet. origin = getlocalclientpos( localclientnum ); players = getplayers( localclientnum ); players = arraysortclosest( players, origin, undefined, 1, 6000 ) (unqualified five-argument call; exact source/native provider and binding remain unresolved). tracked = 0. foreach player: stop/skip branch when tracked >= 10 (quota of10 processed eligible players per pass; no simultaneous FX lifetime limit is established) || !isalive( player ) || player function_83973173() (opaque predicate, also used by wz_perk_engineer helpers; prior notes infer spectating/dead-ish) || isdefined( getplayervehicle( player ) ) (players in vehicles skipped) -> player.tracker_last_pos = undefined; continue. Otherwise tracked++; if !isdefined( player.tracker_last_pos ) -> player.tracker_last_pos = player.origin; positionandrotationstruct = player gettrackerfxposition( localclientnum ) (same-file unit 478); if isdefined( positionandrotationstruct ) -> player tracker_playfx( localclientnum, positionandrotationstruct ) (unit 479). players = undefined after the pass. Runs forever; no endons (loop has no death guard â€” thread is level-owned).

  unknowns: &#91;"function_5778f82 and function_83973173 sources are not in packet; inferred meanings are prior-note inferences only", "Thread lifetime: because the loop never checks game end, it depends on level/thread cleanup semantics outside this file"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/8bddf70ab1be9be0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/8bddf70ab1be9be0.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00646` at JSON pointer ``; file SHA-256 `cf9007dcd598fcaad3c60fc7ceb4569893b0e51e748b7d41f5d1e6ab09787ac2`.

- `scripts/wz_common/wz_perk_bloody_tracker.csc::gettrackerfxposition` (original lines 89-157): Footstep-fx position/rotation builder for the tracked player (method on the TRACKED player, uses self). positionandrotation = undefined; player = self; offset = ( 0, 0, 1 ); dist2 = 1024 (32-unit squared threshold). FX selection by foot flag: if isdefined( self.trailrightfoot ) && self.trailrightfoot -> fx = "player/fx8_plyr_footstep_tracker_blood_r" ; else fx = "player/fx8_plyr_footstep_tracker_blood_l" (exact asset strings as printed). pos = self.origin + offset. Movement gate: if distancesquared( self.tracker_last_pos, pos ) > dist2 (previous stored raw entity origin versus current origin+(0,0,1); emitted ground-FX position is separate. For flat horizontal32 displacement the tested square is1025, not1024): trace = physicstraceex( pos, pos + ( 0, 0, -10 ), ( 0, 0, 0 ), ( 0, 0, 0 ), self, 1 ) (builtin 6-arg ex-form ground probe). if trace&#91; #"fraction" &#93; < 1 (ground hit): up = trace&#91; #"normal" &#93;; up = ( 0, 0, 0 ) - up (inverted normal as written); degenerate guard lengthsquared(up) <= 0 -> return undefined; fwd = anglestoforward( self.angles ); vel = self getvelocity(); if lengthsquared( vel ) > 1 -> fwd = vel (RAW velocity direction, not normalized, as written); right = vectorcross( fwd, up ); degenerate guard lengthsquared(right) <= 0 -> return undefined; fwd = vectorcross( up, right ) (re-orthogonalized, not normalized); pos = trace&#91; #"position" &#93; + trace&#91; #"normal" &#93; (raised by the ground normal); positionandrotation = spawnstruct() with fields .fx / .pos / .fwd / .up; self.tracker_last_pos = self.origin; foot flip: trailrightfoot truthy -> 0 else 1. No ground hit -> positionandrotation stays undefined. Final return positionandrotation.

  unknowns: &#91;"physicstraceex builtin semantics (flags/skipself) engine-side", "Cross products are not normalized in-source; fx orientation magnitude behavior engine-side", "dist2 = 1024 is a local literal (32 units), not a bundle field"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/8bddf70ab1be9be0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/8bddf70ab1be9be0.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00647` at JSON pointer ``; file SHA-256 `ab63047628b9d4cd43ebeee6783a9d492863a3915ba38b1949db5d1bdf4e6937`; selected record SHA-256 `2e083791bfe3cfb05c4854d1ea52a38892300335cd8dafdd33b77e6d461a4af4`.

- `scripts/wz_common/wz_perk_bloody_tracker.csc::tracker_playfx` (original lines 163-166): Blood-tracker fx emitter (function(localclientnum, positionandrotationstruct)). Single statement: handle = playfx( localclientnum, positionandrotationstruct.fx, positionandrotationstruct.pos, positionandrotationstruct.fwd, positionandrotationstruct.up ) â€” client 5-arg playfx with the produced struct fields (fx string, pos, fwd, up); handle captured and unused.

  unknowns: &#91;"None within function scope beyond engine playfx conventions"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/8bddf70ab1be9be0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/8bddf70ab1be9be0.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00029` at JSON pointer `/units/478`; file SHA-256 `3234f0ff6dd1316d5a04f6793a677d66131f03145482b1edd146000e932ad991`; selected record SHA-256 `7b90ba09e9559e479b6a24efea79ad9bef102c8354c1a3b0467e9c77927259f2`.

- `scripts/wz_common/wz_perk_bloody_tracker.csc::__init__system__` (original lines 10-13): Client-side autoexec registration. function autoexec __init__system__(): system::register( #"wz_perk_bloody_tracker", &__init__, undefined, undefined ). No other statements (file 167 lines).

  unknowns: &#91;"system::register semantics outside packet"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/8bddf70ab1be9be0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/8bddf70ab1be9be0.json) at JSON pointer `/claims/3`.

  Archived evidence ID: `archived-record-00029` at JSON pointer `/units/473`; file SHA-256 `3234f0ff6dd1316d5a04f6793a677d66131f03145482b1edd146000e932ad991`; selected record SHA-256 `71ab62b1be52c77c8a7f26e9f1081e40eb5ab1fb0deaed45ea9b6200f2308e38`.

- `scripts/wz_common/wz_perk_bloody_tracker.csc::on_player_connect` (original lines 33-36): Connect handler (registered only when the init gate passes): level thread bloody_tracker( localclientnum ) â€” one statement, threads the tracker loop on level with level as the receiver and only localclientnum passed; this body retains no connecting entity argument or receiver.

  unknowns: &#91;"None within function scope"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/8bddf70ab1be9be0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/8bddf70ab1be9be0.json) at JSON pointer `/claims/4`.

  Archived evidence ID: `archived-record-00648` at JSON pointer ``; file SHA-256 `a77e2d957f7af102cbd8ba3c0e2ca5d7d6c4905d978e76213114ce63f0426cd3`; selected record SHA-256 `f4d20b2911e155618dd592f29ed64aa51e695c46a51574be9be0253f7c1acbc2`.

- `scripts/wz_common/wz_perk_bloody_tracker.csc::__init__` (original lines 19-27): Blood-tracker init with MODE GATE (line 21 token resolved exactly): if !( isdefined( getgametypesetting( #"hash_1d02e28ba907a343" ) ) && getgametypesetting( #"hash_1d02e28ba907a343" ) ) -> return â€” the connect hook is wired ONLY when that gametype setting is defined AND truthy; otherwise nothing registers. When the gate passes: callback::on_localclient_connect( &on_player_connect ).

  unknowns: &#91;"The meaning of gametype setting hash_1d02e28ba907a343 (per prior notes it toggles between the two tracker flavors in wz_perk_tracker.csc) is not derivable from source text", "getgametypesetting value producer is mode/playlist data outside packet"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/8bddf70ab1be9be0-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/8bddf70ab1be9be0.json) at JSON pointer `/claims/5`.

  Archived evidence ID: `archived-record-00029` at JSON pointer `/units/474`; file SHA-256 `3234f0ff6dd1316d5a04f6793a677d66131f03145482b1edd146000e932ad991`; selected record SHA-256 `2e35b4f1141668394f78d8a7170247fa3b4d0dc076825deb98f90b5012aa18cd`.
