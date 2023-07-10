import typing

from .Locations import level_locations
from .Names import RegionNames
from BaseClasses import Entrance, Region, Location, MultiWorld, CollectionState
from enum import Enum
from collections import namedtuple, defaultdict

class CaveRequirement(Enum):
    NONE = 0,
    BOMBS = 1,
    RAFT = 2,
    RECORDER = 3,
    CANDLE = 4,
    BRACELET = 5

CaveMetadata = namedtuple(
    "CaveMetadata",
    ["screen_code", "entrance_type", "location_name"],
    defaults=[CaveRequirement.NONE]
)

class Cave(Region):
    def __init__(
            self,
            name: str,
            player: int,
            world: MultiWorld,
            cave_code: int,
            metadata: CaveMetadata):
        super().__init__(name, player, world)
        self.metadata = metadata
        self.cave_code = cave_code

# this file is based on DKC3's implementation


all_cave_names = [
    # Levels
    RegionNames.LEVEL_1,
    RegionNames.LEVEL_2,
    RegionNames.LEVEL_3,
    RegionNames.LEVEL_4,
    RegionNames.LEVEL_5,
    RegionNames.LEVEL_6,
    RegionNames.LEVEL_7,
    RegionNames.LEVEL_8,
    RegionNames.LEVEL_9,

    # Lake
    RegionNames.WHITE_SWORD_CAVE,
    RegionNames.BLUE_RING_SHOP,
    RegionNames.LAKE_DOOR_REPAIRS,
    RegionNames.LAKE_SECRET_SMALL,
    RegionNames.LAKE_SHIELD_SHOP_A,
    RegionNames.LAKE_SHIELD_SHOP_B,
    RegionNames.LAKE_ARROW_SHOP,
    RegionNames.LAKE_TAKE_ANY,

    # Lost Hills
    RegionNames.LH_HINT_CAVE,
    RegionNames.LH_TAKE_ANY_ROAD,
    RegionNames.LH_CANDLE_SHOP,
    RegionNames.LH_MEDICINE_SHOP,

    # Coast
    RegionNames.LETTER_CAVE,
    RegionNames.COAST_DOOR_REPAIRS_A,
    RegionNames.COAST_DOOR_REPAIRS_B,
    RegionNames.COAST_SECRET_MEDIUM,
    RegionNames.COAST_SECRET_LARGE,
    RegionNames.COAST_MONEY_GAME_A,
    RegionNames.COAST_MONEY_GAME_B,
    RegionNames.COAST_ARROW_SHOP,
    RegionNames.COAST_TAKE_ANY_A,
    RegionNames.COAST_TAKE_ANY_B,

    # River
    RegionNames.RIVER_HINT_CAVE,
    RegionNames.RIVER_PAY_HINT_CAVE,
    RegionNames.RIVER_MEDICINE_SHOP,

    # Graveyard
    RegionNames.MAGICAL_SWORD_CAVE,
    RegionNames.GRAVEYARD_TAKE_ANY_ROAD,
    RegionNames.GRAVEYARD_ARROW_SHOP,
    RegionNames.GRAVEYARD_MEDICINE_SHOP,

    # Desert
    RegionNames.DESERT_SECRET_MEDIUM,
    RegionNames.DESERT_TAKE_ANY_ROAD,
    RegionNames.DESERT_ARROW_SHOP,
    RegionNames.DESERT_MEDICINE_SHOP,
    RegionNames.DESERT_TAKE_ANY,

    # Forest
    RegionNames.FOREST_SECRET_SMALL_A,
    RegionNames.FOREST_SECRET_SMALL_B,
    RegionNames.FOREST_SECRET_MEDIUM,
    RegionNames.FOREST_SECRET_LARGE,
    RegionNames.FOREST_SHIELD_SHOP,
    RegionNames.FOREST_CANDLE_SHOP,

    # Death Mountain
    RegionNames.DM_DOOR_REPAIRS_A,
    RegionNames.DM_DOOR_REPAIRS_B,
    RegionNames.DM_DOOR_REPAIRS_C,
    RegionNames.DM_DOOR_REPAIRS_D,
    RegionNames.DM_MONEY_GAME_A,
    RegionNames.DM_MONEY_GAME_B,
    RegionNames.DM_SECRET_MEDIUM,
    RegionNames.DM_SHIELD_SHOP,
    RegionNames.DM_MEDICINE_SHOP,

    # Dead Woods
    RegionNames.DW_PAY_HINT_CAVE,
    RegionNames.DW_DOOR_REPAIRS,
    RegionNames.DW_SECRET_SMALL,
    RegionNames.DW_SECRET_MEDIUM,
    RegionNames.DW_SECRET_LARGE,

    # Start
    RegionNames.START_SWORD_CAVE,
    RegionNames.START_DOOR_REPAIRS,
    RegionNames.START_MONEY_GAME,
    RegionNames.START_SECRET_MEDIUM,
    RegionNames.START_TAKE_ANY_ROAD,
    RegionNames.START_CANDLE_SHOP,
    RegionNames.START_MEDICINE_SHOP,
]

all_shield_shop_names = [
    RegionNames.LAKE_SHIELD_SHOP_A,
    RegionNames.LAKE_SHIELD_SHOP_B,
    RegionNames.FOREST_SHIELD_SHOP,
    RegionNames.DM_SHIELD_SHOP,
]

all_arrow_shop_names = [
    RegionNames.LAKE_ARROW_SHOP,
    RegionNames.COAST_ARROW_SHOP,
    RegionNames.GRAVEYARD_ARROW_SHOP,
    RegionNames.DESERT_ARROW_SHOP,
]

all_candle_shop_names = [
    RegionNames.LH_CANDLE_SHOP,
    RegionNames.FOREST_CANDLE_SHOP,
    RegionNames.START_CANDLE_SHOP,
]

all_medicine_shop_names = [
    RegionNames.LH_MEDICINE_SHOP,
    RegionNames.RIVER_MEDICINE_SHOP,
    RegionNames.GRAVEYARD_MEDICINE_SHOP,
    RegionNames.DESERT_MEDICINE_SHOP,
    RegionNames.DM_MEDICINE_SHOP,
    RegionNames.START_MEDICINE_SHOP,
]

all_take_any_names = [
    RegionNames.LAKE_TAKE_ANY,
    RegionNames.COAST_TAKE_ANY_A,
    RegionNames.COAST_TAKE_ANY_B,
    RegionNames.DESERT_TAKE_ANY,
]

def create_regions(world: MultiWorld, player: int):
    def new_top_level_region(name):
        return Region(name, player, world)
    main_menu = new_top_level_region(RegionNames.MAIN_MENU)
    overworld_mainland = new_top_level_region(RegionNames.OVERWORLD_MAINLAND)
    bombable_secrets = new_top_level_region(RegionNames.BOMBABLES)
    raft_islands = new_top_level_region(RegionNames.RAFT_ISLANDS)
    recorder_secrets = new_top_level_region(RegionNames.RECORDER_SECRETS)
    candle_secrets = new_top_level_region(RegionNames.BURNABLES)
    bracelet_secrets = new_top_level_region(RegionNames.BRACELET_SECRETS)
    stepladder_dock = new_top_level_region(RegionNames.STEPLADDER_DOCK)
    shield_shops = new_top_level_region(RegionNames.SHIELD_SHOPS)
    arrow_shops = new_top_level_region(RegionNames.ARROW_SHOPS)
    candle_shops = new_top_level_region(RegionNames.CANDLE_SHOPS)
    medicine_shops = new_top_level_region(RegionNames.MEDICINE_SHOPS)
    blue_ring_shop = new_top_level_region(RegionNames.BLUE_RING_SHOP)
    take_anys = new_top_level_region(RegionNames.TAKE_ANYS)

    top_level_regions = [
        main_menu,
        overworld_mainland,
        bombable_secrets,
        raft_islands,
        recorder_secrets,
        candle_secrets,
        bracelet_secrets,
        stepladder_dock,
        shield_shops,
        candle_shops,
        arrow_shops,
        blue_ring_shop,
        medicine_shops,
        take_anys,
    ]

    world.regions += top_level_regions

    main_menu.add_exits({overworld_mainland.name: "Begin Game"})

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
        cave = Cave(name, player, world, cave_code, CaveMetadata(original_screen, requirement))
        world.regions.append(cave)
        return cave

    levels = {
        1: new_cave(RegionNames.LEVELS[1], 0x37, 1),
        2: new_cave(RegionNames.LEVELS[2], 0x3c, 2),
        3: new_cave(RegionNames.LEVELS[3], 0x74, 3),
        4: new_cave(RegionNames.LEVELS[4], 0x45, 4),
        5: new_cave(RegionNames.LEVELS[5], 0x0b, 5),
        6: new_cave(RegionNames.LEVELS[6], 0x22, 6),
        7: new_cave(RegionNames.LEVELS[7], 0x42, 7),
        8: new_cave(RegionNames.LEVELS[8], 0x6d, 8),
        9: new_cave(RegionNames.LEVELS[9], 0x05, 9)
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
        new_cave(RegionNames.COAST_DOOR_REPAIRS_B, 0x1e, 23),
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

    for region in bombables:
        region.requirement = CaveRequirement.BOMBS

    raft_islands = [
        levels[4],
    ]

    for region in raft_islands:
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

    for region in burnables:
        region.requirement = CaveRequirement.CANDLE

    recorder_secrets = [
        levels[7]
    ]

    for region in recorder_secrets:
        region.requirement = CaveRequirement.RECORDER

    power_bracelet_secrets = [
        new_cave(RegionNames.START_TAKE_ANY_ROAD, 0x79, 20),
        new_cave(RegionNames.DESERT_TAKE_ANY_ROAD, 0x49, 20),
        new_cave(RegionNames.LH_TAKE_ANY_ROAD, 0x1d, 20),
        new_cave(RegionNames.GRAVEYARD_TAKE_ANY_ROAD, 0x23, 20),
    ]

    for region in power_bracelet_secrets:
        region.requirement = CaveRequirement.BRACELET

    shield_shops_ = [
        new_cave(RegionNames.LAKE_SHIELD_SHOP_A, 0x26, 31, CaveRequirement.BOMBS),
        new_cave(RegionNames.LAKE_SHIELD_SHOP_B, 0x46, 31, CaveRequirement.CANDLE),
        new_cave(RegionNames.DM_SHIELD_SHOP, 0x12, 31, CaveRequirement.BOMBS),
        new_cave(RegionNames.FOREST_SHIELD_SHOP, 0x4d, 31, CaveRequirement.CANDLE),
    ]

    for shop in shield_shops_:
        _connect_unrestricted(shield_shops, shop, f"{shield_shops.name} -> {shop.name}")

    arrow_shops_ = [
        new_cave(RegionNames.COAST_ARROW_SHOP, 0x6f, 29, CaveRequirement.NONE),
        new_cave(RegionNames.GRAVEYARD_ARROW_SHOP, 0x25, 29, CaveRequirement.NONE),
        new_cave(RegionNames.DESERT_ARROW_SHOP, 0x4a, 29, CaveRequirement.NONE),
        new_cave(RegionNames.LAKE_ARROW_SHOP, 0x44, 29, CaveRequirement.NONE),
    ]

    for shop in arrow_shops_:
        _connect_unrestricted(arrow_shops, shop, f"{arrow_shops.name} -> {shop.name}")

    candle_shops_ = [
        new_cave(RegionNames.LH_CANDLE_SHOP, 0x0c, 30, CaveRequirement.NONE),
        new_cave(RegionNames.START_CANDLE_SHOP, 0x66, 30, CaveRequirement.NONE),
        new_cave(RegionNames.FOREST_CANDLE_SHOP, 0x5e, 30, CaveRequirement.NONE),
    ]

    for shop in candle_shops_:
        _connect_unrestricted(candle_shops, shop, f"{candle_shops.name} -> {shop.name}")

    medicine_shops_ = [
        new_cave(RegionNames.LH_MEDICINE_SHOP, 0x0d, 26, CaveRequirement.BOMBS),
        new_cave(RegionNames.DM_MEDICINE_SHOP, 0x04, 26, CaveRequirement.NONE),
        new_cave(RegionNames.START_MEDICINE_SHOP, 0x78, 26, CaveRequirement.CANDLE),
        new_cave(RegionNames.RIVER_MEDICINE_SHOP, 0x27, 26, CaveRequirement.BOMBS),
        new_cave(RegionNames.GRAVEYARD_MEDICINE_SHOP, 0x33, 26, CaveRequirement.BOMBS),
        new_cave(RegionNames.DESERT_MEDICINE_SHOP, 0x46, 26, CaveRequirement.CANDLE),
    ]

    for shop in medicine_shops_:
        _connect_unrestricted(medicine_shops, shop, f"{medicine_shops.name} -> {shop.name}")

    brs = new_cave(RegionNames.BLUE_RING_SHOP, 0x34, 32)

    _connect_unrestricted(blue_ring_shop, brs, f"{blue_ring_shop.name} -> {brs.name}")

    take_anys_ = [
        new_cave(RegionNames.LAKE_TAKE_ANY, 0x47, 17, CaveRequirement.CANDLE),
        new_cave(RegionNames.COAST_TAKE_ANY_A, 0x7b, 17, CaveRequirement.BOMBS),
        new_cave(RegionNames.COAST_TAKE_ANY_B, 0x2f, 17, CaveRequirement.RAFT),
        new_cave(RegionNames.DESERT_TAKE_ANY, 0x2c, 17, CaveRequirement.BOMBS),
    ]

    for t_a in take_anys_:
        _connect_unrestricted(take_anys, t_a, f"{take_anys.name} -> {t_a.name}")

    # all_caves = [
    #     *mainland_readily_accessible_entrances,
    #     *bombables,
    #     *raft_islands,
    #     *burnables,
    #     *recorder_secrets,
    #     *power_bracelet_secrets,
    #     *levels
    #     *shield_shops_,
    #     *arrow_shops_,
    #     *candle_shops_,
    #     *medicine_shops_,
    #     *blue_ring_shop_,
    #     *take_anys,
    # ]

    # world.regions += all_caves


def connect_regions(world: MultiWorld, player: int):
    """Connects caves to their respective regions based on their metadata.
    
    If shuffling is desired, change the cave metadata before calling this.
    """
    overworld_mainland = world.get_region(RegionNames.OVERWORLD_MAINLAND, player)
    bombables = world.get_region(RegionNames.BOMBABLES, player)
    burnables = world.get_region(RegionNames.BURNABLES, player)
    raft_islands = world.get_region(RegionNames.RAFT_ISLANDS, player)
    recorder_secrets = world.get_region(RegionNames.RECORDER_SECRETS, player)
    bracelet_secrets = world.get_region(RegionNames.BRACELET_SECRETS, player)

    mapped_entrances = set()
    for cave_name in all_cave_names:
        # group all shops/take anys
        if cave_name in all_arrow_shop_names:
            group_name = RegionNames.ARROW_SHOPS
        elif cave_name in all_candle_shop_names:
            group_name = RegionNames.CANDLE_SHOPS
        elif cave_name in all_shield_shop_names:
            group_name = RegionNames.SHIELD_SHOPS
        elif cave_name in all_medicine_shop_names:
            group_name = RegionNames.MEDICINE_SHOPS
        elif cave_name in all_take_any_names:
            group_name = RegionNames.TAKE_ANYS
        else:
            group_name = cave_name

        cave_region: Cave = world.get_region(cave_name, player)
        metadata = cave_region.metadata
        if (group_name, metadata.entrance_type) in mapped_entrances:
            continue

        group_region = world.get_region(group_name, player)

        mapped_entrances.add((group_name, metadata.entrance_type))
        if metadata.entrance_type == CaveRequirement.NONE:
            _connect_unrestricted(
                overworld_mainland, group_region, f"Enter {group_name}", f"Exit {group_name}"
            )
        elif metadata.entrance_type == CaveRequirement.BOMBS:
            _connect_unrestricted(
                bombables, group_region, f"Blow Up Entrance to {group_name}", f"Exit {group_name}"
            )
        elif metadata.entrance_type == CaveRequirement.CANDLE:
            _connect_unrestricted(
                burnables, group_region, f"Burn Entrance to {group_name}", f"Exit {group_name}"
            )
        elif metadata.entrance_type == CaveRequirement.RAFT:
            _connect_unrestricted(raft_islands, group_region, f"Raft to {group_name}")
        elif metadata.entrance_type == CaveRequirement.RECORDER:
            _connect_unrestricted(
                recorder_secrets,
                group_region,
                f"Play a Tune to Enter {group_name}",
                f"Exit {group_name}"
            )
        elif metadata.entrance_type == CaveRequirement.BRACELET:
            _connect_unrestricted(
                bracelet_secrets,
                group_region,
                f"Push a Rock and Enter {group_name}",
                f"Exit {group_name}"
            )
    
    for i, level_name in RegionNames.LEVELS.items():
        level = world.get_region(level_name, player)
        _connect_restricted(
            overworld_mainland,
            level,
            lambda state: state.has("Recorder", player),
            f"Warp to Level {i}"
        )
    

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
        dst_region.add_exits({src_region.name: way_back_action_description})

def _connect_unrestricted(
        src_region: Region,
        dst_region: Region,
        action_description: str,
        way_back_action_description: typing.Optional[str] = None):
    src_region.add_exits({dst_region.name: action_description})
    if way_back_action_description is not None:
        dst_region.add_exits({src_region.name: way_back_action_description})