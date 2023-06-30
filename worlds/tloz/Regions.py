import typing

from .Locations import level_locations
from BaseClasses import Entrance, Region, Location, MultiWorld, CollectionState
from enum import Enum

class CaveRequirement(Enum):
    NONE = 0,
    BOMBS = 1,
    RAFT = 2,
    RECORDER = 3,
    CANDLE = 4,
    BRACELET = 5

class Cave(Region):
    def __init__(
            self,
            name: str,
            player: int, 
            world: MultiWorld,
            screen: int, 
            cave_code: int,
            requirement: CaveRequirement = CaveRequirement.NONE):
        super().__init__(name, player, world)
        self.screen = screen
        self.cave_code = cave_code
        self.requirement = requirement

# this file is based on DKC3's implementation

def create_regions(world: MultiWorld, player: int):
    main_menu = Region("Menu", player, world)
    overworld_mainland = Region("Overworld Mainland", player, world)
    bombable_secrets = Region("Bombable Secrets", player, world)
    raft_islands = Region("Raft Islands", player, world)
    recorder_secrets = Region("Recorder Secrets", player, world)
    candle_secrets = Region("Candle Secrets", player, world)
    bracelet_secrets = Region("Bracelet of Power Secrets", player, world)
    shield_shops = Region("Heart Shops", player, world)
    arrow_shops = Region("Arrow Shops", player, world)
    candle_shops = Region("Candle Shops", player, world)
    medicine_shops = Region("Medicine Shops", player, world)
    take_anys = Region("Take Anys", player, world)
    
    top_level_regions = [
        main_menu,
        overworld_mainland,
        bombable_secrets,
        raft_islands,
        recorder_secrets,
        candle_secrets,
        bracelet_secrets,
        shield_shops,
        candle_shops,
        arrow_shops,
        medicine_shops,
        take_anys,
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
    
    _connect_restricted(
        overworld_mainland,
        bombable_secrets,
        lambda state: state.has_any("Sword", "White Sword", "Magical Sword"),
        "Blow Up Secret",
        "Exit Bombable Secret"
    )
    
    def new_region(name, original_screen, cave_code, requirement=CaveRequirement.NONE):
        return Cave(name, player, world, original_screen, cave_code, requirement)

    levels = {
        1: new_region("Level 1", 0x37, 1),
        2: new_region("Level 2", 0x3c, 2),
        3: new_region("Level 3", 0x74, 3),
        4: new_region("Level 4", 0x45, 4),
        5: new_region("Level 5", 0x0b, 5),
        6: new_region("Level 6", 0x22, 6),
        7: new_region("Level 7", 0x42, 7),
        8: new_region("Level 8", 0x6d, 8),
        9: new_region("Level 9", 0x05, 9)
    }

    # Create subregions for every entrance
    mainland_readily_accessible_entrances = {
        # Lake
        "Level 1": levels[1],
        "White sword cave": new_region("White Sword Cave", 0x0a, 18),
        "Lake blue ring shop": new_region("Lake Blue Ring Shop", 0x34, 32),
        
        # Lost Hills
        "Level 5": levels[5],
        "LH hint cave": new_region("Lost Hills Hint Cave", 0x1c, 21),
        
        # Coast
        "Coast letter cave": new_region("Coast Letter Cave", 0x0e, 24),
        "Coast secret to everybody large": new_region("Coast It's a Secret to Everybody Large", 0x0f, 34),
        "Coast money making game A": new_region("Coast Money Making Game A", 0x1f, 22),
        # Stepladder heart container is a location
        
        # River
        "River hint cave": new_region("River Hint Cave", 0x75, 25),
        "River pay for hint": new_region("River Pay For Hint", 0x1a, 27),
        
        # Graveyard
        "Level 6": levels[6],
        "Magical sword grave": new_region("Magical Sword Grave", 0x21, 19),
        # Armos item is a location, no need for a region for it
        
        # Forest
        "Level 2": levels[2],
        "Forest secret to everybody small B": new_region("Forest It's a Secret to Everybody Small B", 0x4e, 35),
        "Forest secret to everybody medium": new_region("Forest It's a Secret to Everybody Medium", 0x3d, 33),
        
        # Dead woods
        "Level 3": levels[3],
        "DW pay for hint": new_region("Dead Woods Pay For Hint", 0x70, 28),
        
        # Start
        "Starting sword cave": new_region("Starting Sword Cave", 0x77, 16)
    }
    
    bombables = {
        # Coast
        "Coast door repairs A": new_region("Coast Door Repairs A", 0x7d, 23),
        "Coast door repairs B": new_region("Coast Door Repairs B", 0x1e, 23),
        "Coast secret to everybody medium": new_region("Coast It's a Secret to Everybody Medium", 0x2d, 33),
        "Coast money making game B": new_region("Coast Money Making Game B", 0x7c, 22),

        # Death Mountain
        "DM door repairs A": new_region("Death Mountain Door Repairs A", 0x01, 23),
        "DM door repairs B": new_region("Death Mountain Door Repairs B", 0x03, 23),
        "DM door repairs C": new_region("Death Mountain Door Repairs C", 0x07, 23),
        "DM door repairs D": new_region("Death Mountain Door Repairs D", 0x14, 23),
        "DM money making game A": new_region("Death Mountain Money Making Game A", 0x10, 22),
        "DM money making game B": new_region("Death Mountain Money Making Game B", 0x16, 22),
        "DM secret to everybody medium": new_region("Death Mountain It's a Secret to Everybody Medium", 0x13, 33),
        "Level 9": levels[9],      
        
        # Dead Woods
        "DW secret to everybody medium": new_region("Dead Woods It's a Secret to Everybody Medium", 0x70, 33),
        
        # Lost Hills

        # Start
        "Start money making game": new_region("Start Money Making Game", 0x76, 22),
        "Start secret to everybody medium": new_region("Start It's a Secret to Everybody Medium", 0x67, 33),
    }
    
    for region in bombables.values():
        region.requirement = CaveRequirement.BOMBS

    raft_islands = {
        "Level 4": levels[4],
    }
    
    for region in raft_islands.values():
        region.requirement = CaveRequirement.RAFT

    burnables = {
        # Desert
        "Desert secret to everybody medium": new_region("Desert It's a Secret to Everybody Medium", 0x28, 33),
        
        # Forest
        "Level 8": levels[8],
        "Forest secret to everybody small A": new_region("Forest It's a Secret to Everybody Small A", 0x5b, 35),
        "Forest secret to everybody large": new_region("Forest It's a Secret to Everybody Large", 0x6b, 34),

        # Lake
        "Lake door repairs": new_region("Lake Door Repairs", 0x6a, 23),
        "Lake secret to everybody small": new_region("Lake It's a Secret to Everybody Small", 0x56, 35),

        # Dead Woods
        "DW door repairs": new_region("Dead Woods Door Repairs", 0x63, 23),
        "DW small secret": new_region("Dead Woods It's a Secret to Everybody Small", 0x51, 35),
        "DW secret to everybody large": new_region("Dead Woods It's a Secret to Everybody Large", 0x62, 34),
        
        # Start
        "Start door repairs": new_region("Start Door Repairs", 0x68, 23)
    }
    
    for region in burnables.values():
        region.requirement = CaveRequirement.CANDLE

    recorder_secrets = {
        "Level 7": levels[7]
    }
    
    for region in recorder_secrets.values():
        region.requirement = CaveRequirement.RECORDER

    power_bracelet_secrets = {
        "Start take any road": new_region("Start Take Any Road You Want", 0x79, 20),
        "Desert take any road": new_region("Desert Take Any Road You Want", 0x49, 20),
        "LH take any road": new_region("Lost Hills Take Any Road You Want", 0x1d, 20),
        "Graveyard take any road": new_region("Graveyard Take Any Road You Want", 0x23, 20),
    }
    
    for region in power_bracelet_secrets.values():
        region.requirement = CaveRequirement.BRACELET
    
    shield_shops_ = {
        "Lake heart shop A": new_region("Lake Recovery Heart Shop A", 0x26, 31, CaveRequirement.BOMBS),
        "DM heart shop": new_region("Death Mountain Recovery Heart Shop", 0x12, 31, CaveRequirement.BOMBS),
        "Forest heart shop": new_region("Forest Heart Shop", 0x4d, 31, CaveRequirement.CANDLE),
        "Lake heart shop B": new_region("Lake Recovery Heart Shop B", 0x46, 31, CaveRequirement.CANDLE),
    }
    
    for shop in shield_shops_.values():
        _connect_unrestricted(shield_shops, shop, f"Heart Shops -> {shop.name}")
    
    arrow_shops_ = {
        "Coast arrow shop": new_region("Coast Arrow Shop", 0x6f, 29, CaveRequirement.NONE),
        "Graveyard arrow shop": new_region("Graveyard Arrow Shop", 0x25, 29, CaveRequirement.NONE),
        "Desert arrow shop": new_region("Desert Arrow Shop", 0x4a, 29, CaveRequirement.NONE),
        "Lake arrow shop": new_region("Lake Arrow Shop", 0x44, 29, CaveRequirement.NONE),
    }
    
    for shop in arrow_shops_.values():
        _connect_unrestricted(arrow_shops, shop, f"Arrow Shops -> {shop.name}")
    
    candle_shops_ = {
        "LH candle shop": new_region("Lost Hills Candle Shop", 0x0c, 30, CaveRequirement.NONE),
        "Start candle shop": new_region("Start Candle Shop", 0x66, 30, CaveRequirement.NONE),
        "Forest candle shop": new_region("Forest Candle Shop", 0x5e, 30, CaveRequirement.NONE),
    }
    
    for shop in candle_shops_.values():
        _connect_unrestricted(candle_shops, shop, f"Candle Shops -> {shop.name}")
    
    medicine_shops_ = {
        "LH medicine shop": new_region("Lost Hills Medicine Shop", 0x0d, 26, CaveRequirement.BOMBS),
        "DM medicine shop": new_region("Death Mountain Medicine Shop", 0x04, 26, CaveRequirement.NONE),
        "Start medicine shop": new_region("Start Medicine Shop", 0x78, 26, CaveRequirement.CANDLE),
        "River medicine shop": new_region("River Medicine Shop", 0x27, 26, CaveRequirement.BOMBS),
        "Graveyard medicine shop": new_region("Graveyard Medicine Shop", 0x33, 26, CaveRequirement.BOMBS),
        "Desert medicine shop": new_region("Desert Medicine Shop", 0x46, 26, CaveRequirement.CANDLE),
    }

    for shop in medicine_shops_.values():
        _connect_unrestricted(medicine_shops, shop, f"Medicine Shops -> {shop.name}")


    take_anys_ = {
        "Lake take any medicine/heart container": new_region("Lake Take Any", 0x47, 17, CaveRequirement.CANDLE),
        "Coast take any medicine/heart container A": new_region("Coast Take Any A", 0x7b, 17, CaveRequirement.BOMBS),
        "Coast take any medicine/heart container B": new_region("Coast Take Any B", 0x2f, 17, CaveRequirement.RAFT),
        "Desert take any medicine/heart container": new_region("Desert Take Any", 0x2c, 17, CaveRequirement.BOMBS),
    }
    
    for t_a in take_anys_:
        _connect_unrestricted(take_anys, t_a, f"Take Anys -> {t_a.name}")

    for level_nr, level_region in levels.items():
        loc_names = level_locations[level_nr - 1]
        for loc_name in loc_names:
            level_region.locations.append(world.get_location(loc_name))
    
    for slot in ("Left", "Middle", "Right"):
        shield_shops.locations.append(f"Shield Shop Item {slot}")
        arrow_shops.locations.append(f"Arrow Shop Item {slot}")
        candle_shops.locations.append(f"Candle Shop Item {slot}")
        medicine_shops.locations.append(f"Medicine Shop Item {slot}")
        take_anys.locations.append(f"Take Any Item {slot}")
        # TODO blue ring shop?
        
    
    
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