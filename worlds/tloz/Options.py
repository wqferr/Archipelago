import typing
from Options import Option as BaseOption, Toggle, DefaultOnToggle, Choice


class ExpandedPool(DefaultOnToggle):
    """Puts room clear drops and take any caves into the pool of items and locations."""
    display_name = "Expanded Item Pool"


class TriforceLocations(Choice):
    """Where Triforce fragments can be located. Note that Triforce pieces
    obtained in a dungeon will heal and warp you out, while overworld Triforce pieces obtained will appear to have
    no immediate effect. This is normal."""
    display_name = "Triforce Locations"
    option_vanilla = 0
    option_dungeons = 1
    option_anywhere = 2


class StartingPosition(Choice):
    """How easy is the start of the game.
    Safe means a weapon is guaranteed in Starting Sword Cave.
    Unsafe means that a weapon is guaranteed between Starting Sword Cave, Letter Cave, and Armos Knight.
    Dangerous adds these level locations to the unsafe pool (if they exist):
#       Level 1 Compass, Level 2 Bomb Drop (Keese), Level 3 Key Drop (Zols Entrance), Level 3 Compass
    Very Dangerous is the same as dangerous except it doesn't guarantee a weapon. It will only mean progression
    will be there in single player seeds. In multi worlds, however, this means all bets are off and after checking
    the dangerous spots, you could be stuck until someone sends you a weapon"""
    display_name = "Starting Position"
    option_safe = 0
    option_unsafe = 1
    option_dangerous = 2
    option_very_dangerous = 3

class RandomStartingWeapon(Toggle):
    """If the starting weapon should be chosen at random.
    "false" means starting weapon will always be the Sword.
    "true" means starting weapon will be any of the Swords, Red Candle, or Magical Rod
    """
    display_name = "Random Starting Weapon"

class ShuffleCaves(DefaultOnToggle):
    """Whether to shuffle cave entrances.
    "false" means all caves are in their vanilla locations.
    "true" means all caves, including the starting sword cave, are randomized.
    
    When "on" is selected with "safe" starting position, all caves but the Starting Sword Cave
    are randomized.
    """
    display_name = "Shuffle Caves"


tloz_options: typing.Dict[str, typing.Type[BaseOption]] = {
    "ExpandedPool": ExpandedPool,
    "TriforceLocations": TriforceLocations,
    "StartingPosition": StartingPosition,
    "ShuffleCaves": ShuffleCaves,
    "RandomStartingWeapon": RandomStartingWeapon,
}
