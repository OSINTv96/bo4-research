// HMH RESEARCH: this header is project-added; original code follows END.
// Recovered source: scripts/wz_common/wz_ignore_systems.csc
// HMH role, inputs, effects, callbacks and limits: docs/modules/5d90fd2943e72aa3.md
// Whole module retained for source context; only recorded spans carry reused review.
// New assembly/comments await independent review. Retail/gameplay equivalence is unproved.
// END HMH PROJECT HEADER
#using scripts\core_common\system_shared;

#namespace wz_ignore_systems;

// Namespace wz_ignore_systems/wz_ignore_systems
// Params 0, eflags: 0x2
// Checksum 0x60472f20, Offset: 0x70
// Size: 0x104
function autoexec ignore_systems()
{
    system::ignore( #"recon_car" );
    system::ignore( #"planemortar" );
    system::ignore( #"supplydrop" );
    system::ignore( #"ultimate_turret" );
    system::ignore( #"armor_station" );
    system::ignore( #"counteruav" );
    system::ignore( #"uav" );
    system::ignore( #"supplypod" );
}
