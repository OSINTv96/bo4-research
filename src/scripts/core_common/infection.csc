// HMH RESEARCH: this header is project-added; original code follows END.
// Recovered source: scripts/core_common/infection.csc
// HMH role, inputs, effects, callbacks and limits: docs/modules/d37d3dc115117bb0.md
// Whole module retained for source context; only recorded spans carry reused review.
// New assembly/comments await independent review. Retail/gameplay equivalence is unproved.
// END HMH PROJECT HEADER
#using scripts\core_common\system_shared;

#namespace infection;

// Namespace infection/infection
// Params 0, eflags: 0x2
// Checksum 0x8583f4a6, Offset: 0x80
// Size: 0x3c
function autoexec __init__system__()
{
    system::register( #"infection", &__init__, undefined, undefined );
}

// Namespace infection/infection
// Params 0
// Checksum 0x80f724d1, Offset: 0xc8
// Size: 0x4
function __init__()
{

}

// Namespace infection/infection
// Params 0
// Checksum 0x168d969c, Offset: 0xd8
// Size: 0x48, Type: bool
function function_74650d7()
{
    if ( isdefined( getgametypesetting( "infectionMode" ) ) && getgametypesetting( "infectionMode" ) )
    {
        return true;
    }

    return false;
}
