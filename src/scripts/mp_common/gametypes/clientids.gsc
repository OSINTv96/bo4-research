// HMH RESEARCH: this header is project-added; original code follows END.
// Recovered source: scripts/mp_common/gametypes/clientids.gsc
// HMH role, inputs, effects, callbacks and limits: docs/modules/e030e13dc9d3bfc2.md
// Whole module retained for source context; only recorded spans carry reused review.
// New assembly/comments await independent review. Retail/gameplay equivalence is unproved.
// END HMH PROJECT HEADER
#using scripts\core_common\callbacks_shared;
#using scripts\core_common\system_shared;

#namespace clientids;

// Namespace clientids/clientids
// Params 0, eflags: 0x2
// Checksum 0x9eb1d71, Offset: 0x78
// Size: 0x3c
function autoexec __init__system__()
{
    system::register( #"clientids", &__init__, undefined, undefined );
}

// Namespace clientids/clientids
// Params 0
// Checksum 0xd1fe180a, Offset: 0xc0
// Size: 0x44
function __init__()
{
    callback::on_start_gametype( &init );
    callback::on_connect( &on_player_connect );
}

// Namespace clientids/clientids
// Params 0
// Checksum 0x53cc0c3e, Offset: 0x110
// Size: 0x12
function init()
{
    level.clientid = 0;
}

// Namespace clientids/clientids
// Params 0
// Checksum 0x2f05036b, Offset: 0x130
// Size: 0x9c
function on_player_connect()
{
    self.clientid = matchrecordnewplayer( self );

    if ( !isdefined( self.clientid ) || self.clientid == -1 )
    {
        self.clientid = level.clientid;
        level.clientid++;
    }

    println( "<dev string:x38>" + self.name + "<dev string:x43>" + self.clientid );
}
