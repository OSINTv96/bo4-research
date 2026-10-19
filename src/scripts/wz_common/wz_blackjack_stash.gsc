// HMH RESEARCH: this header is project-added; original code follows END.
// Recovered source: scripts/wz_common/wz_blackjack_stash.gsc
// HMH role, inputs, effects, callbacks and limits: docs/modules/a649eacf4ec3c56c.md
// Whole module retained for source context; only recorded spans carry reused review.
// New assembly/comments await independent review. Retail/gameplay equivalence is unproved.
// END HMH PROJECT HEADER
#using scripts\core_common\system_shared;
#using scripts\mp_common\item_world;

#namespace wz_stash_blackjack;

// Namespace wz_stash_blackjack/wz_blackjack_stash
// Params 0, eflags: 0x2
// Checksum 0xeda00467, Offset: 0x78
// Size: 0x3c
function autoexec __init__system__()
{
    system::register( #"wz_stash_blackjack", &__init__, undefined, undefined );
}

// Namespace wz_stash_blackjack/wz_blackjack_stash
// Params 0
// Checksum 0xa2c3c610, Offset: 0xc0
// Size: 0xcc
function __init__()
{
    level.blackjackstash = isdefined( getgametypesetting( #"wzlootlockers" ) ) ? getgametypesetting( #"wzlootlockers" ) : 0;
    customgame = gamemodeismode( 1 ) || gamemodeismode( 7 );

    if ( customgame || !level.blackjackstash )
    {
        level thread function_e973becc();
    }
}

// Namespace wz_stash_blackjack/wz_blackjack_stash
// Params 0, eflags: 0x4
// Checksum 0x5cd2ebde, Offset: 0x198
// Size: 0xb0
function private function_e973becc()
{
    item_world::function_4de3ca98();
    var_14957968 = getdynentarray( #"wz_stash_blackjack" );

    foreach ( var_2e01d28f in var_14957968 )
    {
        item_world::function_160294c7( var_2e01d28f );
    }
}
