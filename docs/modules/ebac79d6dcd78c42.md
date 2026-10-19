# scripts/weapons/grapple.csc

Project-added notes. See the [code](../../src/scripts/weapons/grapple.csc).

The complete file retains lexical context. These summary excerpts do not approve the whole file or prove HMH invocation.

Original revision: `f4b9a51f8b7fcfcb6d158303d3fd5fff2fcfb6ac`. Original SHA-256: `02ba7b1943ca86bba19a9a8756e4f52f4a21a8729a84f0520213772cd3501b23`.

Exact source spans, dependencies and bounded review evidence: [module record](../../provenance/modules/ebac79d6dcd78c42.json).

New notes and dependency decisions await independent review. Original build, native/VM, effective settings, service and gameplay limits remain open.

Selected source notes (excerpts; full records remain authoritative):

- `scripts/weapons/grapple.csc::function_2297363d` (original lines 131-171): Grapple earthquake/vignette loop (localclientnum; self = player). Restart idiom: self notify( "567d59ecc92fd8f5" ); self endon( "567d59ecc92fd8f5" ). player = self; doearthquake = 1; var_30f9f328 = 0 (shader constant accumulator). while isdefined( player ): first call function_fd33f2ef(localclientnum) is compared with3, without caching a state local. Branch1 (first result==3, meaning unproved): if doearthquake -> player.grappleeq = earthquake( localclientnum, level.var_1b2035de.var_1598129, 10000, player.origin, 0, 0 ) â€” screen-shake started once, magnitude from the 'grapple_custom_settings' bundle, duration arg 10000, at player origin; doearthquake = 0. Then player mapshaderconstant( localclientnum, 0, "scriptVector1", var_30f9f328, 0, 0, 0 ); var_30f9f328 += 0.05 (ramps a shader effect up 0.05 per frame, no clamp in-span). Branch2 (a second separate call to function_fd33f2ef(localclientnum)==0; meaning unproved): same mapshaderconstant write but var_30f9f328 -= 0.05 (ramps down; no floor clamp in-span). Else branch ( any other state ): player mapshaderconstant( localclientnum, 0, "scriptVector1", 0, 0, 0, 0 ) (snap constant to 0); only if isdefined(player.grappleeq), call function_196e7c4b(localclientnum,player.grappleeq), clear that handle and set doearthquake=1. An undefined handle skips all three actions; native earthquake/stop effects remain unresolved. waitframe( 1 ).

  unknowns: &#91;"function_fd33f2ef (state reader) and function_196e7c4b (earthquake stop) definitions not in catalog; state meanings 3/0/other inferred from branch structure only", "earthquake parameter convention (magnitude, duration 10000, position, two zeros) native", "mapshaderconstant 'scriptVector1' target shader is game data; negative constant handling (ramp-down below 0) unverified"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/ebac79d6dcd78c42-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/ebac79d6dcd78c42.json) at JSON pointer `/claims/0`.

  Archived evidence ID: `archived-record-00817` at JSON pointer ``; file SHA-256 `cee26ab7a0f3934fe0ffa5665e7f0fce06d71b1cf1b3e8de0c7b1bb04137790c`; selected record SHA-256 `5ea02f854a465c9dede86c4d31b082b0a07e1ff98914ba1b1a183f45f4135c7b`.

- `scripts/weapons/grapple.csc::grapple_light_watch_end` (original lines 113-125): Per-handle FX cleanup watcher (localclientnum, handle, name; self = player). Ordered: player endon( "grapple_light_done_watch" + name ) â€” dies when the main loop itself kills this handle (then notifies done_watch); player notify( "grapple_light_watch_end" + name ) then endon( "grapple_light_watch_end" + name ) â€” restart idiom clearing any previous watcher of the same name; player waittill( #"death" ); if isdefined( handle ) -> killfx( localclientnum, handle ) â€” final cleanup of leftover viewmodel FX on death.

  unknowns: &#91;"Interaction detail: the notify('grapple_light_watch_end'+name) at start could also be consumed by other systems \u00e2\u20ac\u201d only the pairing observed", "waittill(#\"death\") result usage none (only death triggers cleanup)"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/ebac79d6dcd78c42-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/ebac79d6dcd78c42.json) at JSON pointer `/claims/1`.

  Archived evidence ID: `archived-record-00102` at JSON pointer `/units/81`; file SHA-256 `bec4988a5459cac825b94dcc33e1b58fc8dc9b791fc0a299fcedfa5c5250bdd0`; selected record SHA-256 `44776edd8adf3f3807fe55cd33c74a3607fc1c9f835e32f146d87aec2ba3fbff`.

- `scripts/weapons/grapple.csc::__init__` (original lines 20-25): Client system init for grapple visuals/audio. Ordered: (1) callback::on_localplayer_spawned( &player_on_spawned ) â€” wires per-local-player spawn handling; (2) level.var_c3e66138 = &function_bbd7fc60 â€” stores the dialog hook (plays 'grappleGunWeaponUseFail' dialog; consumer of the pointer is unknown from this file); (3) level.var_1b2035de = getscriptbundle( "grapple_custom_settings" ) â€” loads the grapple settings script bundle; field var_1598129 is consumed by function_2297363d as the earthquake magnitude argument.

  unknowns: &#91;"Consumer of level.var_c3e66138 is outside this file", "getscriptbundle content (var_1598129 value) is bundle data not readable here"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/ebac79d6dcd78c42-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/ebac79d6dcd78c42.json) at JSON pointer `/claims/2`.

  Archived evidence ID: `archived-record-00102` at JSON pointer `/units/78`; file SHA-256 `bec4988a5459cac825b94dcc33e1b58fc8dc9b791fc0a299fcedfa5c5250bdd0`; selected record SHA-256 `2df8eaa3a4c93e147828f4434e7195be5b6cd9451667a94d60b04b124e65c7f6`.

- `scripts/weapons/grapple.csc::function_664d0a50` (original lines 51-107): Grapple aim light maintenance loop (localclientnum; self = player). Restart idiom: self notify( "16bdee31b75b050b" ); self endon( "16bdee31b75b050b" ). player = self; var_e413b7c3 (valid FX handle) = undefined; invalidhandle = undefined. while isdefined( player ): var_6e521a44 = function_15f112c3( localclientnum ) â€” unresolved external queried every frame (grapple-target validity state). Cases: (a) isdefined( var_6e521a44 ) && var_6e521a44 && !isdefined( var_e413b7c3 ) â€” target just became valid: if isdefined( invalidhandle ) -> killfx( localclientnum, invalidhandle ), player notify( "grapple_light_done_watch" + "invalid" ), invalidhandle = undefined; then var_e413b7c3 = playviewmodelfx( localclientnum, #"hash_2a3978ae302f2faf", "tag_fx1", 0 ) â€” valid-branch FX request (actual color/asset meaning unresolved) on the viewmodel tag_fx1; thread grapple_light_watch_end( localclientnum, var_e413b7c3, "valid" ). (b) isdefined && !var_6e521a44 && !isdefined( invalidhandle ) â€” target became invalid: if isdefined( var_e413b7c3 ) -> killfx, player notify( "grapple_light_done_watch" + "valid" ), var_e413b7c3 = undefined; invalidhandle = playviewmodelfx( localclientnum, #"hash_39ed4a0ecba806a2", "tag_fx1", 0 ); thread grapple_light_watch_end( localclientnum, invalidhandle, "invalid" ). (c) var_6e521a44 undefined â€” state unavailable: kill both handles if defined and clear them (does not notify either done tag; existing death watchers can remain active and may later attempt handle cleanup; original scheduling/stale-handle semantics remain unresolved). waitframe( 1 ) each pass. Runs while player is defined.

  unknowns: &#91;"function_15f112c3 definition not in catalog (the queried grapple state semantics unknown; three-way return true/false/undefined observed)", "FX aliases hash_2a3978ae302f2faf/hash_39ed4a0ecba806a2 identity not in catalog", "The player death case while loop exits only when player becomes undefined (undefined-ness driven by engine entity lifetime; endon/death handled by grapple_light_watch_end for the live handle)"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/ebac79d6dcd78c42-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/ebac79d6dcd78c42.json) at JSON pointer `/claims/3`.

  Archived evidence ID: `archived-record-00818` at JSON pointer ``; file SHA-256 `d29eba69d830cbe8ff3550a77f6b621a1f14f6f252bf3b7b373068a528669c94`; selected record SHA-256 `e27377ad1ecd00c6b8910f4f9b82bdcc5417cfde6fce5f7097be6540337e2ca1`.

- `scripts/weapons/grapple.csc::player_on_spawned` (original lines 31-45): Local-player spawn wiring (localclientnum arg; self = player). Gate chain: if sessionmodeismultiplayergame() || sessionmodeiswarzonegame() â€” only MP or warzone sessions proceed; then if !player function_21c0fa55() -> return â€” unresolved external predicate (same helper name appears in scripts/weapons/acid_bomb.csc line 105 gating rumble on a parent); if it passes: player thread function_664d0a50( localclientnum ) (grapple light FX loop) and player thread function_2297363d( localclientnum ) (earthquake/shader loop). Non-MP/non-warzone sessions start neither loop. No state writes.

  unknowns: &#91;"function_21c0fa55 definition not in catalog; role (plausibly local-ownership/is-local-player check) inferred from usage sites only", "Session-mode predicate exact semantics (native) unverified"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/ebac79d6dcd78c42-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/ebac79d6dcd78c42.json) at JSON pointer `/claims/4`.

  Archived evidence ID: `archived-record-00102` at JSON pointer `/units/79`; file SHA-256 `bec4988a5459cac825b94dcc33e1b58fc8dc9b791fc0a299fcedfa5c5250bdd0`; selected record SHA-256 `eb8c841f6737d95c3deaf09a0ec890d762ea00daed883bee2704304234bf08dc`.

- `scripts/weapons/grapple.csc::function_bbd7fc60` (original lines 177-192): Grapple use-failure dialog hook (var_428d0be2 = player target of the hook; stored as level.var_c3e66138 in __init__). Gates: if !isdefined( var_428d0be2 ) || ( isdefined( level.allowspecialistdialog ) && !level.allowspecialistdialog ) -> return (mode gate â€” dialog suppressed when level.allowspecialistdialog is false). dialogalias = var_428d0be2 dialog_shared::get_player_dialog_alias( "grappleGunWeaponUseFail" ); if !isdefined( dialogalias ) -> return; var_428d0be2 playsound( 0, dialogalias ) â€” plays the alias with leading argument 0 (observed call form).

  unknowns: &#91;"playsound( 0, dialogalias ) two-arg call convention on entities is native; exact channel meaning unverified", "Which code calls level.var_c3e66138 and with which entity (the player?) is the integration boundary noted in unit 79"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/ebac79d6dcd78c42-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/ebac79d6dcd78c42.json) at JSON pointer `/claims/5`.

  Archived evidence ID: `archived-record-00102` at JSON pointer `/units/83`; file SHA-256 `bec4988a5459cac825b94dcc33e1b58fc8dc9b791fc0a299fcedfa5c5250bdd0`; selected record SHA-256 `bf498dfca91465a49b3a738776ed9ecb36ae94ae8e322101ea5f286701ddf779`.

- `scripts/weapons/grapple.csc::__init__system__` (original lines 11-14): Client-side autoexec registering the grapple system: system::register( #"grapple", &__init__, undefined, undefined ). No branches.

  unknowns: &#91;"Engine dispatch timing of the registered init unverified"&#93;

  status: complete_bounded_contract

  Complete explanatory fields: [exact projection](../../provenance/documentation/ebac79d6dcd78c42-001.json). Older compact summaries and original evidence remain unchanged.

  Exact excerpt: [saved claim](../../provenance/modules/ebac79d6dcd78c42.json) at JSON pointer `/claims/6`.

  Archived evidence ID: `archived-record-00819` at JSON pointer ``; file SHA-256 `4f8d2cad9b12d6a7c8fb209e885755159e8e4d447f44c01cd41a6a1dc0e695b0`; selected record SHA-256 `fcd402e203efc15f51939a6ef4059643f7a31459f9c22976281cd71dba36b2ba`.
