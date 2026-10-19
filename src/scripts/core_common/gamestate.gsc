// HMH RESEARCH: this header is project-added; original code follows END.
// Recovered source: scripts/core_common/gamestate.gsc
// HMH role, inputs, effects, callbacks and limits: docs/modules/cb7f1e3a5c1694a0.md
// Whole module retained for source context; only recorded spans carry reused review.
// New assembly/comments await independent review. Retail/gameplay equivalence is unproved.
// END HMH PROJECT HEADER
#namespace gamestate;

// Namespace gamestate/gamestate
// Params 1
// Checksum 0xf3c8d505, Offset: 0x80
// Size: 0x2c
function set_state( state )
{
    game.state = state;
    function_cab6408d( state );
}

// Namespace gamestate/gamestate
// Params 1
// Checksum 0xed58268a, Offset: 0xb8
// Size: 0x1c, Type: bool
function is_state( state )
{
    return game.state == state;
}

// Namespace gamestate/gamestate
// Params 0
// Checksum 0x104cf608, Offset: 0xe0
// Size: 0x32, Type: bool
function is_game_over()
{
    return game.state == "postgame" || game.state == "shutdown";
}

// Namespace gamestate/gamestate
// Params 0
// Checksum 0x23f8666, Offset: 0x120
// Size: 0x18, Type: bool
function is_shutting_down()
{
    return game.state == "shutdown";
}
