// HMH RESEARCH: this header is project-added; original code follows END.
// Recovered source: scripts/wz/wz_open_skyscrapers_fixup.gsc
// HMH role, inputs, effects, callbacks and limits: docs/modules/69b0893ce14405c6.md
// Whole module retained for source context; only recorded spans carry reused review.
// New assembly/comments await independent review. Retail/gameplay equivalence is unproved.
// END HMH PROJECT HEADER
#using scripts\mp_common\item_world_fixup;

#namespace wz_open_skyscrapers_fixup;

// Namespace wz_open_skyscrapers_fixup/wz_open_skyscrapers_fixup
// Params 0, eflags: 0x2
// Checksum 0x1a8e5f24, Offset: 0x70
// Size: 0x24
function autoexec __init__()
{
    function_4305a789();
    function_c94723bd();
}

// Namespace wz_open_skyscrapers_fixup/wz_open_skyscrapers_fixup
// Params 0, eflags: 0x4
// Checksum 0x80f724d1, Offset: 0xa0
// Size: 0x4
function private function_4305a789()
{

}

// Namespace wz_open_skyscrapers_fixup/wz_open_skyscrapers_fixup
// Params 0, eflags: 0x4
// Checksum 0x20f82f51, Offset: 0xb0
// Size: 0xdc
function private function_c94723bd()
{
    if ( isdefined( getgametypesetting( #"wzenableflareguns" ) ) && getgametypesetting( #"wzenableflareguns" ) && !( isdefined( getgametypesetting( #"wzheavymetalheroes" ) ) && getgametypesetting( #"wzheavymetalheroes" ) ) )
    {
        item_world_fixup::function_e70fa91c( #"supply_stash_parent_dlc1", #"supply_stash_parent_dlc1_flare_guns", 5 );
    }
}
