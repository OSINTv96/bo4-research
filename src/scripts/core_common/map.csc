// HMH RESEARCH: this header is project-added; original code follows END.
// Recovered source: scripts/core_common/map.csc
// HMH role, inputs, effects, callbacks and limits: docs/modules/393cf2e443a78220.md
// Whole module retained for source context; only recorded spans carry reused review.
// New assembly/comments await independent review. Retail/gameplay equivalence is unproved.
// END HMH PROJECT HEADER
#namespace map;

// Namespace map/map
// Params 0
// Checksum 0x752e8654, Offset: 0x68
// Size: 0x14
function init()
{
    get_script_bundle();
}

// Namespace map/map
// Params 0
// Checksum 0xc7700528, Offset: 0x88
// Size: 0x6e
function get_script_bundle()
{
    if ( !isdefined( level.var_427d6976 ) )
    {
        level.var_427d6976 = getmapscriptbundle();
    }

    if ( !isdefined( level.var_427d6976 ) )
    {
        level.var_179eaba8 = 1;
        level.var_427d6976 = {};
    }
    else
    {
        level.var_179eaba8 = 0;
    }

    return level.var_427d6976;
}

// Namespace map/map
// Params 0
// Checksum 0x921a99bf, Offset: 0x100
// Size: 0x2a
function is_default()
{
    if ( !isdefined( level.var_179eaba8 ) )
    {
        level.var_179eaba8 = 1;
    }

    return level.var_179eaba8;
}
