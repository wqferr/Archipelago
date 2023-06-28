import typing

from .Locations import level_locations
from BaseClasses import Entrance, Region, Location, MultiWorld, CollectionState

# this file is based on DKC3's implementation

def create_regions(world: MultiWorld, player: int):
    main_menu = Region("Menu", player, world)
    overworld_mainland = Region("Overworld Mainland", player, world)
    raft_islands = Region("Raft Islands", player, world)
    recorder_secrets = Region("Recorder Secrets", player, world)
    candle_secrets = Region("Candle Secrets", player, world)
    bracelet_secrets = Region("Bracelet of Power Secrets", player, world)
    
    top_level_regions = [
        main_menu,
        overworld_mainland,
        raft_islands,
        recorder_secrets,
        candle_secrets,
        bracelet_secrets
    ]
    
    world.regions += top_level_regions
    
    main_menu.add_exits({overworld_mainland.name: "New File"})
    
    _connect_restricted_region(
        overworld_mainland,
        raft_islands,
        lambda state: state.has("Raft"),
        "Use Raft",
        "Raft Back"
    )
    
    _connect_restricted_region(
        overworld_mainland,
        recorder_secrets,
        lambda state: state.has("Recorder"),
        "Reveal Recorder Secret",
        "Exit Recorder Secret"
    )

    _connect_restricted_region(
        overworld_mainland,
        candle_secrets,
        lambda state: state.has_any("Candle", "Red Candle"),
        "Burn Candle Secret",
        "Exit Candle Secret"
    )
    
    _connect_restricted_region(
        overworld_mainland,
        bracelet_secrets,
        lambda state: state.has("Power Bracelet"),
        "Push Secret With Power Bracelet",
        "Exit Power Bracelet Secret"
    )
    
    
def _connect_restricted_region(
        src_region: Region,
        dst_region: Region,
        state_check: typing.Callable[[CollectionState], bool],
        action_description: str,
        way_back_action_description: typing.Optional[str] = None):
    src_region.add_exits(
        {dst_region.name: action_description},
        {dst_region.name: state_check}
    )
    if way_back_action_description is not None:
        dst_region.add_exits({src_region.name, way_back_action_description})