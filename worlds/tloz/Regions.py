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

class RegionNames:
    MAIN_MENU = "Menu"
    OVERWORLD_MAINLAND = "Overworld Mainland"
    BOMBABLES = "Bombable Secrets"
    RAFT_ISLANDS = "Raft Islands"
    RECORDER_SECRETS = "Recorder Secrets"
    BURNABLES = "Candle Secrets"
    BRACELET_SECRETS = "Bracelet of Power Secrets"

    SHIELD_SHOPS = "Shield Shops"
    ARROW_SHOPS = "Arrow Shops"
    CANDLE_SHOPS = "Candle Shops"
    MEDICINE_SHOPS = "Medicine Shops"
    BLUE_RING_SHOP = "Blue Ring Shop"
    TAKE_ANYS = "Take Anys"
    
    LEVEL_1 = "Level 1"
    LEVEL_2 = "Level 2"
    LEVEL_3 = "Level 3"
    LEVEL_4 = "Level 4"
    LEVEL_5 = "Level 5"
    LEVEL_6 = "Level 6"
    LEVEL_7 = "Level 7"
    LEVEL_8 = "Level 8"
    LEVEL_9 = "Level 9"
    
    LEVELS = {i: f"Level {i+1}" for i in range(9)}
    
    # Lake
    WHITE_SWORD_CAVE = "White Sword Cave"
    BLUE_RING_SHOP = "Blue Ring Shop"
    LAKE_DOOR_REPAIRS = "Lake Door Repairs"
    LAKE_SECRET_SMALL = "Lake It's a Secret to Everybody Small"
    LAKE_SHIELD_SHOP_A = "Lake Shield Shop A"
    LAKE_SHIELD_SHOP_B = "Lake Shield Shop B"
    LAKE_ARROW_SHOP = "Lake Arrow Shop"
    LAKE_TAKE_ANY = "Lake Take Any"

    # Lost Hills
    LH_HINT_CAVE = "Lost Hills Hint Cave"
    LH_TAKE_ANY_ROAD = "Lost Hills Take Any Road You Want"
    LH_CANDLE_SHOP = "Lost Hills Candle Shop"
    LH_MEDICINE_SHOP = "Lost Hills Medicine Shop"
    
    # Coast
    LETTER_CAVE = "Letter Cave"
    COAST_DOOR_REPAIRS_A = "Coast Door Repairs A"
    COAST_DOOR_REPAIRS_B = "Coast Door Repairs B"
    COAST_SECRET_MEDIUM = "Coast It's a Secret to Everybody Medium"
    COAST_SECRET_LARGE = "Coast It's a Secret to Everybody Large"
    COAST_MONEY_GAME_A = "Coast Money Making Game A"
    COAST_MONEY_GAME_B = "Coast Money Making Game B"
    COAST_ARROW_SHOP = "Coast Arrow Shop"
    COAST_TAKE_ANY_A = "Coast Take Any A"
    COAST_TAKE_ANY_B = "Coast Take Any B"
    
    # River
    RIVER_HINT_CAVE = "River Hint Cave"
    RIVER_PAY_HINT_CAVE = "River Pay For Hint"
    RIVER_MEDICINE_SHOP = "River Medicine Shop"
    
    # Graveyard
    MAGICAL_SWORD_CAVE = "Magical Sword Grave"
    GRAVEYARD_TAKE_ANY_ROAD = "Graveyard Take Any Road You Want"
    GRAVEYARD_ARROW_SHOP = "Graveyard Arrow Shop"
    GRAVEYARD_MEDICINE_SHOP = "Graveyard Medicine Shop"
    
    # Desert
    DESERT_SECRET_MEDIUM = "Desert It's a Secret to Everybody Medium"
    DESERT_TAKE_ANY_ROAD = "Desert Take Any Road You Want"
    DESERT_ARROW_SHOP = "Desert Arrow Shop"
    DESERT_MEDICINE_SHOP = "Desert Medicine Shop"
    DESERT_TAKE_ANY = "Desert Take Any"

    # Forest
    FOREST_SECRET_SMALL_A = "Forest It's a Secret to Everybody Small A"
    FOREST_SECRET_SMALL_B = "Forest It's a Secret to Everybody Small B"
    FOREST_SECRET_MEDIUM = "Forest It's a Secret to Everybody Medium"
    FOREST_SECRET_LARGE = "Forest It's a Secret to Everybody Large"
    FOREST_SHIELD_SHOP = "Forest Shield Shop"
    FOREST_CANDLE_SHOP = "Forest Candle Shop"
    
    # Death Mountain
    DM_DOOR_REPAIRS_A = "Death Mountain Door Repairs A"
    DM_DOOR_REPAIRS_B = "Death Mountain Door Repairs B"
    DM_DOOR_REPAIRS_C = "Death Mountain Door Repairs C"
    DM_DOOR_REPAIRS_D = "Death Mountain Door Repairs D"
    DM_MONEY_GAME_A = "Death Mountain Money Making Game A"
    DM_MONEY_GAME_B = "Death Mountain Money Making Game B"
    DM_SECRET_MEDIUM = "Death Mountain It's a Secret to Everybody Medium"
    DM_SHIELD_SHOP = "Death Mountain Shield Shop"
    DM_MEDICINE_SHOP = "Death Mountain Medicine Shop"

    # Dead Woods
    DW_PAY_HINT_CAVE = "Dead Woods Pay For Hint"
    DW_DOOR_REPAIRS = "Dead Woods Door Repairs"
    DW_SECRET_SMALL = "Dead Woods It's a Secret to Everybody Small"
    DW_SECRET_MEDIUM = "Dead Woods It's a Secret to Everybody Medium"
    DW_SECRET_LARGE = "Dead Woods It's a Secret to Everybody Large"

    # Start
    START_SWORD_CAVE = "Starting Sword Cave"
    START_DOOR_REPAIRS = "Start Door Repairs"
    START_MONEY_GAME = "Start Money Making Game"
    START_SECRET_MEDIUM = "Start It's a Secret to Everybody Medium"
    START_TAKE_ANY_ROAD = "Start Take Any Road You Want"
    START_CANDLE_SHOP = "Start Candle Shop"
    START_MEDICINE_SHOP = "Start Medicine Shop"

def create_regions(world: MultiWorld, player: int):
    main_menu = Region(RegionNames.MAIN_MENU, player, world)
    overworld_mainland = Region(RegionNames.OVERWORLD_MAINLAND, player, world)
    bombable_secrets = Region(RegionNames.BOMBABLES, player, world)
    raft_islands = Region(RegionNames.RAFT_ISLANDS, player, world)
    recorder_secrets = Region(RegionNames.RECORDER_SECRETS, player, world)
    candle_secrets = Region(RegionNames.BURNABLES, player, world)
    bracelet_secrets = Region(RegionNames.BRACELET_SECRETS, player, world)
    shield_shops = Region(RegionNames.SHIELD_SHOPS, player, world)
    arrow_shops = Region(RegionNames.ARROW_SHOPS, player, world)
    candle_shops = Region(RegionNames.CANDLE_SHOPS, player, world)
    medicine_shops = Region(RegionNames.MEDICINE_SHOPS, player, world)
    blue_ring_shop = Region(RegionNames.BLUE_RING_SHOP, player, world)
    take_anys = Region(RegionNames.TAKE_ANYS, player, world)
    
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
        blue_ring_shop,
        medicine_shops,
        take_anys,
    ]
    
    world.regions += top_level_regions
    
    main_menu.add_exits({overworld_mainland.name: "New File"})
    
    # Connect top-level regions
    _connect_restricted(
        overworld_mainland,
        raft_islands,
        lambda state: state.has("Raft", player),
        "Use Raft",
        "Raft Back"
    )
    
    _connect_restricted(
        overworld_mainland,
        recorder_secrets,
        lambda state: state.has("Recorder", player),
        "Reveal Recorder Secret",
        "Exit Recorder Secret"
    )

    _connect_restricted(
        overworld_mainland,
        candle_secrets,
        lambda state: state.has_any({"Candle", "Red Candle"}, player),
        "Burn Candle Secret",
        "Exit Candle Secret"
    )
    
    _connect_restricted(
        overworld_mainland,
        bracelet_secrets,
        lambda state: state.has("Power Bracelet", player),
        "Push Secret With Power Bracelet",
        "Exit Power Bracelet Secret"
    )
    
    _connect_restricted(
        overworld_mainland,
        bombable_secrets,
        lambda state: state.has_group("swords", player),
        "Blow Up Secret",
        "Exit Bombable Secret"
    )
    
    def new_cave(name, original_screen, cave_code, requirement=CaveRequirement.NONE):
        return Cave(name, player, world, original_screen, cave_code, requirement)

    levels = {
        1: new_cave(RegionNames.LEVEL_1, 0x37, 1),
        2: new_cave(RegionNames.LEVEL_2, 0x3c, 2),
        3: new_cave(RegionNames.LEVEL_3, 0x74, 3),
        4: new_cave(RegionNames.LEVEL_4, 0x45, 4),
        5: new_cave(RegionNames.LEVEL_5, 0x0b, 5),
        6: new_cave(RegionNames.LEVEL_6, 0x22, 6),
        7: new_cave(RegionNames.LEVEL_7, 0x42, 7),
        8: new_cave(RegionNames.LEVEL_8, 0x6d, 8),
        9: new_cave(RegionNames.LEVEL_9, 0x05, 9)
    }

    # Create subregions for every entrance
    mainland_readily_accessible_entrances = [
        # Lake
        levels[1],
        new_cave(RegionNames.WHITE_SWORD_CAVE, 0x0a, 18),
        
        # Lost Hills
        levels[5],
        new_cave(RegionNames.LH_HINT_CAVE, 0x1c, 21),
        
        # Coast
        new_cave(RegionNames.LETTER_CAVE, 0x0e, 24),
        new_cave(RegionNames.COAST_SECRET_LARGE, 0x0f, 34),
        new_cave(RegionNames.COAST_MONEY_GAME_A, 0x1f, 22),
        # Stepladder heart container is a location
        
        # River
        new_cave(RegionNames.RIVER_HINT_CAVE, 0x75, 25),
        new_cave(RegionNames.RIVER_PAY_HINT_CAVE, 0x1a, 27),
        
        # Graveyard
        levels[6],
        new_cave(RegionNames.MAGICAL_SWORD_CAVE, 0x21, 19),
        # Armos item is a location, no need for a region for it
        
        # Forest
        levels[2],
        new_cave(RegionNames.FOREST_SECRET_SMALL_B, 0x4e, 35),
        new_cave(RegionNames.FOREST_SECRET_MEDIUM, 0x3d, 33),
        
        # Dead woods
        levels[3],
        new_cave(RegionNames.DW_PAY_HINT_CAVE, 0x70, 28),
        
        # Start
        new_cave(RegionNames.START_SWORD_CAVE, 0x77, 16)
    ]
    
    bombables = [
        # Coast
        new_cave(RegionNames.COAST_DOOR_REPAIRS_A, 0x7d, 23),
        new_cave(RegionNames.COAST_DOOR_REPAIRS_A, 0x1e, 23),
        new_cave(RegionNames.COAST_SECRET_MEDIUM, 0x2d, 33),
        new_cave(RegionNames.COAST_MONEY_GAME_B, 0x7c, 22),

        # Death Mountain
        new_cave(RegionNames.DM_DOOR_REPAIRS_A, 0x01, 23),
        new_cave(RegionNames.DM_DOOR_REPAIRS_B, 0x03, 23),
        new_cave(RegionNames.DM_DOOR_REPAIRS_C, 0x07, 23),
        new_cave(RegionNames.DM_DOOR_REPAIRS_D, 0x14, 23),
        new_cave(RegionNames.DM_MONEY_GAME_A, 0x10, 22),
        new_cave(RegionNames.DM_MONEY_GAME_B, 0x16, 22),
        new_cave(RegionNames.DM_SECRET_MEDIUM, 0x13, 33),
        levels[9],      
        
        # Dead Woods
        new_cave(RegionNames.DW_SECRET_MEDIUM, 0x70, 33),

        # Start
        new_cave(RegionNames.START_MONEY_GAME, 0x76, 22),
        new_cave(RegionNames.START_SECRET_MEDIUM, 0x67, 33),
    ]
    
    for region in bombables.values():
        region.requirement = CaveRequirement.BOMBS

    raft_islands = [
        levels[4],
    ]
    
    for region in raft_islands.values():
        region.requirement = CaveRequirement.RAFT

    burnables = [
        # Desert
        new_cave(RegionNames.DESERT_SECRET_MEDIUM, 0x28, 33),
        
        # Forest
        levels[8],
        new_cave(RegionNames.FOREST_SECRET_SMALL_A, 0x5b, 35),
        new_cave(RegionNames.FOREST_SECRET_LARGE, 0x6b, 34),

        # Lake
        new_cave(RegionNames.LAKE_DOOR_REPAIRS, 0x6a, 23),
        new_cave(RegionNames.LAKE_SECRET_SMALL, 0x56, 35),

        # Dead Woods
        new_cave(RegionNames.DW_DOOR_REPAIRS, 0x63, 23),
        new_cave(RegionNames.DW_SECRET_SMALL, 0x51, 35),
        new_cave(RegionNames.DW_SECRET_LARGE, 0x62, 34),
        
        # Start
        new_cave(RegionNames.START_DOOR_REPAIRS, 0x68, 23)
    ]
    
    for region in burnables.values():
        region.requirement = CaveRequirement.CANDLE

    recorder_secrets = [
        levels[7]
    ]
    
    for region in recorder_secrets.values():
        region.requirement = CaveRequirement.RECORDER

    power_bracelet_secrets = [
        new_cave(RegionNames.START_TAKE_ANY_ROAD, 0x79, 20),
        new_cave(RegionNames.DESERT_TAKE_ANY_ROAD, 0x49, 20),
        new_cave(RegionNames.LH_TAKE_ANY_ROAD, 0x1d, 20),
        new_cave(RegionNames.GRAVEYARD_TAKE_ANY_ROAD, 0x23, 20),
    ]
    
    for region in power_bracelet_secrets.values():
        region.requirement = CaveRequirement.BRACELET
    
    shield_shops_ = [
        new_cave(RegionNames.LAKE_SHIELD_SHOP_A, 0x26, 31, CaveRequirement.BOMBS),
        new_cave(RegionNames.LAKE_SHIELD_SHOP_B, 0x46, 31, CaveRequirement.CANDLE),
        new_cave(RegionNames.DM_SHIELD_SHOP, 0x12, 31, CaveRequirement.BOMBS),
        new_cave(RegionNames.FOREST_SHIELD_SHOP, 0x4d, 31, CaveRequirement.CANDLE),
    ]
    
    for shop in shield_shops_.values():
        _connect_unrestricted(shield_shops, shop, f"{shield_shops.name} -> {shop.name}")
    
    arrow_shops_ = [
        new_cave(RegionNames.COAST_ARROW_SHOP, 0x6f, 29, CaveRequirement.NONE),
        new_cave(RegionNames.GRAVEYARD_ARROW_SHOP, 0x25, 29, CaveRequirement.NONE),
        new_cave(RegionNames.DESERT_ARROW_SHOP, 0x4a, 29, CaveRequirement.NONE),
        new_cave(RegionNames.LAKE_ARROW_SHOP, 0x44, 29, CaveRequirement.NONE),
    ]
    
    for shop in arrow_shops_.values():
        _connect_unrestricted(arrow_shops, shop, f"{arrow_shops.name} -> {shop.name}")
    
    candle_shops_ = [
        new_cave(RegionNames.LH_CANDLE_SHOP, 0x0c, 30, CaveRequirement.NONE),
        new_cave(RegionNames.START_CANDLE_SHOP, 0x66, 30, CaveRequirement.NONE),
        new_cave(RegionNames.FOREST_CANDLE_SHOP, 0x5e, 30, CaveRequirement.NONE),
    ]
    
    for shop in candle_shops_.values():
        _connect_unrestricted(candle_shops, shop, f"{candle_shops.name} -> {shop.name}")
    
    medicine_shops_ = [
        new_cave(RegionNames.LH_MEDICINE_SHOP, 0x0d, 26, CaveRequirement.BOMBS),
        new_cave(RegionNames.DM_MEDICINE_SHOP, 0x04, 26, CaveRequirement.NONE),
        new_cave(RegionNames.START_MEDICINE_SHOP, 0x78, 26, CaveRequirement.CANDLE),
        new_cave(RegionNames.RIVER_MEDICINE_SHOP, 0x27, 26, CaveRequirement.BOMBS),
        new_cave(RegionNames.GRAVEYARD_MEDICINE_SHOP, 0x33, 26, CaveRequirement.BOMBS),
        new_cave(RegionNames.DESERT_MEDICINE_SHOP, 0x46, 26, CaveRequirement.CANDLE),
    ]

    for shop in medicine_shops_.values():
        _connect_unrestricted(medicine_shops, shop, f"{medicine_shops.name} -> {shop.name}")

    brs = new_cave(RegionNames.BLUE_RING_SHOP, 0x34, 32)
    blue_ring_shop_ = {
        "Lake blue ring shop": brs
    }

    _connect_unrestricted(blue_ring_shop, brs, f"{blue_ring_shop.name} -> {brs.name}")

    take_anys_ = [
        new_cave(RegionNames.LAKE_TAKE_ANY, 0x47, 17, CaveRequirement.CANDLE),
        new_cave(RegionNames.COAST_TAKE_ANY_A, 0x7b, 17, CaveRequirement.BOMBS),
        new_cave(RegionNames.COAST_TAKE_ANY_A, 0x2f, 17, CaveRequirement.RAFT),
        new_cave(RegionNames.DESERT_TAKE_ANY, 0x2c, 17, CaveRequirement.BOMBS),
    ]
    
    for t_a in take_anys_:
        _connect_unrestricted(take_anys, t_a, f"{take_anys.name} -> {t_a.name}")

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
        
    
    overworld_mainland.locations.append("Armos Knights")
    
    all_caves = {
        *mainland_readily_accessible_entrances,
        *bombables,
        *raft_islands,
        *burnables,
        *recorder_secrets,
        *power_bracelet_secrets,
        *levels
        *shield_shops_,
        *arrow_shops_,
        *candle_shops_,
        *medicine_shops_,
        *blue_ring_shop_,
        *take_anys,
    }
    
    world.regions += all_caves
    
    # original: typing.List[Cave] = list(all_caves.values())
    # shuffled: typing.List[Cave] = list(original)
    # world.random.shuffle(shuffled)
    # cave_mapping = {}
    
    # for old_location, new_location in zip(original, shuffled):
    #     cave_mapping[old_location.screen] = (new_location.cave_code, old_location.requirement)
    
    
    
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