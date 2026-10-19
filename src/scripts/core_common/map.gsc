// HMH RESEARCH: this header is project-added; original code follows END.
// Recovered source: scripts/core_common/map.gsc
// HMH role, inputs, effects, callbacks and limits: docs/modules/046eb0a2a5899e5c.md
// Whole module retained for source context; only recorded spans carry reused review.
// New assembly/comments await independent review. Retail/gameplay equivalence is unproved.
// END HMH PROJECT HEADER
#namespace map;

// Namespace map/map
// Params 0
// Checksum 0x849ae33a, Offset: 0x68
// Size: 0x14
function init()
{
    get_script_bundle();
}

// Namespace map/map
// Params 0
// Checksum 0x91f6b334, Offset: 0x88
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
// Checksum 0x2d270f97, Offset: 0x100
// Size: 0x2a
function is_default()
{
    if ( !isdefined( level.var_179eaba8 ) )
    {
        level.var_179eaba8 = 1;
    }

    return level.var_179eaba8;
}
