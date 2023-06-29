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
    
    # Connect top-level regions
    _connect_restricted(
        overworld_mainland,
        raft_islands,
        lambda state: state.has("Raft"),
        "Use Raft",
        "Raft Back"
    )
    
    _connect_restricted(
        overworld_mainland,
        recorder_secrets,
        lambda state: state.has("Recorder"),
        "Reveal Recorder Secret",
        "Exit Recorder Secret"
    )

    _connect_restricted(
        overworld_mainland,
        candle_secrets,
        lambda state: state.has_any("Candle", "Red Candle"),
        "Burn Candle Secret",
        "Exit Candle Secret"
    )
    
    _connect_restricted(
        overworld_mainland,
        bracelet_secrets,
        lambda state: state.has("Power Bracelet"),
        "Push Secret With Power Bracelet",
        "Exit Power Bracelet Secret"
    )
    
    new_region = lambda name: Region(name, player, world)
    
    # TODO add regions that are not readily accessible via mainland
    # TODO add offsets in ROM here, probably by inheriting from Region

    # Create subregions for every entrance
    mainland_readily_accessible_entrances = {
        # Death Mountain
        "DM door repairs A": new_region("Death Mountain Door Repairs A"),
        "DM door repairs B": new_region("Death Mountain Door Repairs B"),
        "DM door repairs C": new_region("Death Mountain Door Repairs C"),
        "DM money making game A": new_region("Death Mountain Money Making Game A"),
        "DM money making game B": new_region("Death Mountain Money Making Game B"),
        "DM secret to everybody 30": new_region("Death Mountain It's a Secret to Everybody (30)"),
        "DM heart shop": new_region("Death Mountain Recovery Heart Shop"),
        "DM medicine shop": new_region("Death Mountain Medicine Shop"),

        # Lake
        "White sword cave": new_region("White Sword Cave"),
        "Lake heart shop A": new_region("Lake Recovery Heart Shop A"),
        "Lake heart shop B": new_region("Lake Recovery Heart Shop B"),
        "Lake blue ring shop": new_region("Lake Blue Ring Shop"),
        "Lake arrow shop": new_region("Lake Arrow Shop"),
        "Level 1": new_region("Level 1"),
        "Level 4": new_region("Level 4"),
        # Level 7 is under Recorder Secrets
        "Lake take any medicine/heart container": new_region("Lake Take Any Medicine or Heart Container"),
        "Lake secret to everybody 10": new_region("Lake It's a Secret to Everybody (10)"),
        "Lake door repairs": new_region("Lake Door Repairs"),
        
        # Lost Hills
        "Level 5": new_region("Level 5"),
        "LH candle shop": new_region("Lost Hills Candle Shop"),
        "LH hint cave": new_region("Lost Hills Hint Cave"),
        "LH medicine shop": new_region("Lost Hills Medicine Shop"),
        "LH take any road": new_region("Lost Hills Take Any Road You Want"),
        
        # Coast
        "Coast letter cave": new_region("Coast Letter Cave"),
        "Coast secret to everybody 30": new_region("Coast It's a Secret to Everybody (30)"),
        "Coast secret to everybody 100": new_region("Coast It's a Secret to Everybody (100)"),
        "Coast door repairs A": new_region("Coast Door Repairs A"),
        "Coast door repairs B": new_region("Coast Door Repairs B"),
        "Coast money making game A": new_region("Coast Money Making Game A"),
        "Coast money making game B": new_region("Coast Money Making Game B"),
        "Coast take any medicine/heart container": new_region("Coast Take Any Medicine or Heart Container"),
        # Other take any medicine/heart container needs raft
        # Stepladder heart container is a location
        "Coast arrow shop": new_region("Coast Arrow Shop"),
        
        # River
        "River hint cave": new_region("River Hint Cave"),
        "River medicine shop": new_region("River Medicine Shop"),
        "River pay for hint": new_region("River Pay For Hint"),
        
        # Graveyard
        "Magical sword grave": new_region("Magical Sword Grave"),
        "Level 6": new_region("Level 6"),
        "Graveyard take any road": new_region("Graveyard Take Any Road You Want"),
        # Armos item is a location, no need for a region for it
        "Graveyard arrow shop": new_region("Graveyard Arrow Shop"),
        "Graveyard medicine shop": new_region("Graveyard Medicine Shop"),
        
        # Desert
        "Desert secret to everybody 30": new_region("Desert It's a Secret to Everybody (30)"),
        "Desert take any medicine/heart container": new_region("Coast Take Any Medicine or Heart Container"),
        "Desert take any road": new_region("Desert Take Any Road You Want"),
        "Desert arrow shop": new_region("Desert Arrow Shop"),
        "Desert medicine shop": new_region("Desert Medicine Shop"),
        
        # Forest
        "Level 2": new_region("Level 2"),
        # Level 8 requires candle
        "Forest secret to everybody 10 A": new_region("Forest It's a Secret to Everybody (10) A"),
        "Forest secret to everybody 10 B": new_region("Forest It's a Secret to Everybody (10) B"),
        "Forest secret to everybody 30": new_region("Forest It's a Secret to Everybody (30)"),
        "Forest secret to everybody 100": new_region("Forest It's a Secret to Everybody (100)"),
        "Forest heart shop": new_region("Forest Heart Shop"),
        "Forest candle shop": new_region("Forest Candle Shop"),
        
        # Dead woods
        "Level 3": new_region("Level 3"),
        "DW pay for hint": new_region("Dead Woods Pay For Hint"),
        "DW secret to everybody 10": new_region("Dead Woods It's a Secret to Everybody (10)"),
        "DW secret to everybody 30": new_region("Dead Woods It's a Secret to Everybody (30)"),
        "DW secret to everybody 100": new_region("Dead Woods It's a Secret to Everybody (100)"),
        "DW door repairs": new_region("Dead Woods Door Repairs"),
        "DW medicine shop": new_region("Dead Woods Medicine Shop"),
        
        # Start
        "Start door repairs": new_region("Start Door Repairs"),
        "Start secret to everybody 30": new_region("Start It's a Secret to Everybody (30)"),
        "Start candle shop": new_region("Start Candle Shop"),
        "Start money making game": new_region("Start Money Making Game"),
        "Starting sword cave": new_region("Starting Sword Cave"),
        "Start medicine shop": new_region("Start Medicine Shop"),
        "Start take any road": new_region("Start Take Any Road You Want")
    }

    
def _connect_restricted(
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
        
def _connect_unrestricted(
        src_region: Region,
        dst_region: Region,
        action_description: str,
        way_back_action_description: typing.Optional[str] = None):
    src_region.add_exits({dst_region.name: action_description})
    if way_back_action_description is not None:
        dst_region.add_exits({src_region.name: way_back_action_description})

def _connect_subregion(parent_region: Region, child_region: Region):
    _connect_unrestricted(
        parent_region,
        child_region,
        f"{parent_region.name} -> {child_region.name}"
        f"{child_region.name} -> {parent_region.name}"
    )