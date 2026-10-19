// HMH RESEARCH: this header is project-added; original code follows END.
// Recovered source: scripts/mp_common/gametypes/globallogic_score.csc
// HMH role, inputs, effects, callbacks and limits: docs/modules/8d2000b68aff4152.md
// Whole module retained for source context; only recorded spans carry reused review.
// New assembly/comments await independent review. Retail/gameplay equivalence is unproved.
// END HMH PROJECT HEADER
#using scripts\core_common\clientfield_shared;

#namespace globallogic_score;

// Namespace globallogic_score/globallogic_score
// Params 0, eflags: 0x2
// Checksum 0x93af3d88, Offset: 0x108
// Size: 0xe4
function autoexec __init__()
{
    clientfield::register( "clientuimodel", "hudItems.scoreProtected", 1, 1, "int", undefined, 0, 0 );
    clientfield::register( "clientuimodel", "hudItems.minorActions.action0", 1, 1, "counter", undefined, 0, 0 );
    clientfield::register( "clientuimodel", "hudItems.minorActions.action1", 1, 1, "counter", undefined, 0, 0 );
    clientfield::register( "clientuimodel", "hudItems.hotStreak.level", 1, 3, "int", undefined, 0, 0 );
}
