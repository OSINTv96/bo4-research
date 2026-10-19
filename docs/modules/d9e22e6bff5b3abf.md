# scripts/wz_common/wz_perk_paranoia.csc

Project-added notes. See the [code](../../src/scripts/wz_common/wz_perk_paranoia.csc).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `f4b9a51f8b7fcfcb6d158303d3fd5fff2fcfb6ac`. Original SHA-256: `8fbba053d2c723d952a3401848502785db5ef001fa62ec2463f4164e2acd0112`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/d9e22e6bff5b3abf.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `scripts/wz_common/wz_perk_paranoia.csc::function_c9d3a835` (original lines 77-80): Paranoia victim reference point (private): single statement: return self.origin + ( 0, 0, 36 ) â€” mid-height point on the hidden player. No guards.

  unknowns: &#91;"None beyond function scope"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/d9e22e6bff5b3abf-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/d9e22e6bff5b3abf.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00029` at JSON pointer `/units/495`; file SHA-256 `3234f0ff6dd1316d5a04f6793a677d66131f03145482b1edd146000e932ad991`; selected record SHA-256 `f3a85367401994e4f1fbdafab5de1960fddbb9f54ff579571e0fe49a61dc3803`.

- `scripts/wz_common/wz_perk_paranoia.csc::function_3e9077b` (original lines 86-227): PARANOIA HEARTBEAT loop (private, threaded on the local player on every paranoia perk state change from unit 494). Ends: level endon( #"game_ended" ); self endon( #"disconnect", #"shutdown", #"death" ) (three endons in one call); restart-identity singleton: self notify( "1cd9d4f64a9f9459" ) then self endon( "1cd9d4f64a9f9459" ) â€” PLAIN STRING tokens (no # prefix) exactly as printed at lines 90-91. Perk gate: if !self hasperk( localclientnum, #"specialty_paranoia" ) -> return. var_81f254ba = cos( 10 ) (literal cos(10), computed once; angle units and math/VM contract unresolved). OUTER while(true): var_7cefa3dc = undefined; players = getplayers( localclientnum ). foreach player: guards in order â€” skip !isdefined(player); skip player == self; skip !isalive(player); skip when NOT player util::isenemyteam( self.team ) (util_shared; prior notes call it enemy-team test); skip when isdefined( player function_bee2bbc7() ) && player function_bee2bbc7() (opaque per-player predicate, shared with tracker files; prior notes infer dead/other-state); skip when NOT ads: if !( isdefined( player isplayerads() ) && player isplayerads() ) -> continue. Geometry test per candidate: player_eye_pos = player function_dbd63244() (unit 495 by-stance eye); var_2cb75b52 = self function_c9d3a835() (unit 496 mid-height point); to_self = var_2cb75b52 - player_eye_pos; skip when lengthsquared( to_self ) > 21600 * 21600 (LITERAL 21600-unit distance gate exactly as printed â€” prior drafts mis-derived it as 360 units); player_angles = player getplayerangles(); player_forward = anglestoforward( player_angles ); var_e1a2a16a = vectornormalize( to_self ); skip when vectordot( player_forward, var_e1a2a16a ) < var_81f254ba (literal dot/cos threshold; a ten-degree interpretation remains unproved). LOS scan: test_points rebuilt per candidate (decompiler hygiene: test_points = &#91;&#93; then redundant isdefined/isarray guards, then three appends at self.origin + z 11, 40, 60 â€” the three self-stance heights); foreach test_point: trace_dist = length( to_self ) + 100; trace_end = test_point + vectorscale( player_forward, trace_dist * -1 ) (trace BACKWARD along the enemy view axis); trace = bullettrace( test_point, trace_end, 1, self ); los = 1 AND break when trace&#91; #"fraction" &#93; < 1 && trace&#91; #"entity" &#93; === player (the ads-enemy is the first blocker â€” as written). A waitframe( 1 ) sits INSIDE the foreach (line 210) after the LOS test â€” only candidates reaching the unsuccessful LOS fallthrough wait there; early continue filters and successful LOS break skip this wait. After the pass: if isdefined( var_7cefa3dc ) && isdefined( player ): var_2b836fea = player playsound( localclientnum, var_7cefa3dc ) â€” the paranoia sting hash #"hash_56f62705c6a2bcb6" (var_7cefa3dc) played on/from the ads-enemy; while soundplaying( var_2b836fea ): waitframe( 1 ); wait randomfloat( 1 ) (cooldown up to 1s). Final waitframe( 1 ) per outer iteration. Loop ends only via the endons.

  unknowns: &#91;"function_bee2bbc7 opaque (outside packet; shared with tracker predicates)", "util::isenemyteam semantics (util_shared) outside packet", "The exact trigger for the hash-named callback state watcher (unit 494) and the meaning of the plain-string restart token 1cd9d4f64a9f9459 consumers are outside this file (wiring in unit 493 + callbacks_shared)", "Bullettrace direction-backward geometry is recorded exactly as printed; its gameplay interpretation (hidden-player LOS from stance points behind the enemy view) is an inference"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/d9e22e6bff5b3abf-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/d9e22e6bff5b3abf.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00782` at JSON pointer ``; file SHA-256 `7cc337ecbafef8c8d5cbb39cbf2d902e0643617a2a4a8f5dfd88a6186f90935b`; selected record SHA-256 `c0bf9406ff55f3360bbccdc9ae4813e9162d94b09b78a01e8427dbdbe7e53563`.

- `scripts/wz_common/wz_perk_paranoia.csc::function_dbd63244` (original lines 49-71): Enemy eye-position provider (private, runs on the scan-candidate enemy). assert( isplayer( self ) ) (printed outside a dev block; original build inclusion/handling unproved). If self function_da43934d() -> return self geteye() (engine eye when the predicate passes). Else by stance via self getstance(): case #"prone" -> return self.origin + ( 0, 0, 11 ); case #"crouch" -> + ( 0, 0, 40 ); case #"stand" -> + ( 0, 0, 60 ); default -> + ( 0, 0, 60 ). No other state.

  unknowns: &#91;"getstance hash return values and geteye builtin are engine-side", "The same predicate da43934d governs engine-eye vs stance-approximation fallback"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/d9e22e6bff5b3abf-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/d9e22e6bff5b3abf.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00783` at JSON pointer ``; file SHA-256 `203272bec204e0decbef1ad4a283eb26bfb2d5948af7f7845f2761cd888d2894`; selected record SHA-256 `45a513f2f09263842f6f26ed7e91d81947b3f58319096285b19a7407fd82beac`.

- `scripts/wz_common/wz_perk_paranoia.csc::__init__system__` (original lines 11-14): Client-side autoexec registration. function autoexec __init__system__(): system::register( #"wz_perk_paranoia", &__init__, undefined, undefined ) (file 228 lines).

  unknowns: &#91;"system::register semantics outside packet"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/d9e22e6bff5b3abf-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/d9e22e6bff5b3abf.json) at JSON pointer `/claims/3`.

  Archived evidence ID: `archived-record-00029` at JSON pointer `/units/491`; file SHA-256 `3234f0ff6dd1316d5a04f6793a677d66131f03145482b1edd146000e932ad991`; selected record SHA-256 `7ccf5c0c6b8472499b3d5c639784e1c4ea95691af83baf6cab3c6aace023c99f`.

- `scripts/wz_common/wz_perk_paranoia.csc::function_930e5d42` (original lines 29-43): Paranoia perk state-change watcher (function(localclientnum); the hash-named callback registered in unit 493). Gate: if self function_da43934d() (SAME opaque predicate family as vision-pulse usage): var_369be743 = self hasperk( localclientnum, #"specialty_paranoia" ) (2-arg client hasperk); var_7c49d38b = self.var_369be743 !== var_369be743 â€” the entity field self.var_369be743 compared with the distinct local var_369be743 just assigned at33; the recovered identities are unambiguous; if var_7c49d38b -> self thread function_3e9077b( localclientnum ) (paranoia loop, unit 497); then self.var_369be743 = var_369be743 (store current state). Thread fires on every perk state change (gain or loss); the loop itself re-checks hasperk and exits immediately on loss.

  unknowns: &#91;"The source distinguishes stored entity field self.var_369be743 from local current result var_369be743; original VM/value comparison, source compatibility and actual event delivery remain unresolved.", "function_da43934d opaque (outside packet)"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/d9e22e6bff5b3abf-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/d9e22e6bff5b3abf.json) at JSON pointer `/claims/4`.

  Archived evidence ID: `archived-record-00784` at JSON pointer ``; file SHA-256 `a2997892563f2e1bf052fdc7b98d8d8bfb7827710de3485f9a9d8449ddf91833`; selected record SHA-256 `ce790e5653d0053f5138300ee0423db0c5b6a2ca2ec9b4f4bf18ab182bdc61bc`.

- `scripts/wz_common/wz_perk_paranoia.csc::__init__` (original lines 20-23): Paranoia init: single statement callback::function_930e5d42( &function_930e5d42 ) â€” registers THIS-FILE function_930e5d42 under a hash-named callback (self-referential alias as printed; consumer wiring outside packet). No mode gate at file level (per-player perk gate applied later).

  unknowns: &#91;"callbacks_shared registration model: the hash key and dispatch consumer are module-internal, outside packet"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/d9e22e6bff5b3abf-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/d9e22e6bff5b3abf.json) at JSON pointer `/claims/5`.

  Archived evidence ID: `archived-record-00029` at JSON pointer `/units/492`; file SHA-256 `3234f0ff6dd1316d5a04f6793a677d66131f03145482b1edd146000e932ad991`; selected record SHA-256 `b7cffe7d9df68c05b731c7706fc9640bff16d9a5e3efd25a27dceb60af501510`.
