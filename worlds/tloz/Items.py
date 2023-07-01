from BaseClasses import ItemClassification
import typing
from typing import Dict
from .Names import ItemNames

progression = ItemClassification.progression
filler = ItemClassification.filler
useful = ItemClassification.useful
trap = ItemClassification.trap


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    classification: ItemClassification


item_table: Dict[str, ItemData] = {
    ItemNames.BOOMERANG: ItemData(100, useful),
    ItemNames.BOW: ItemData(101, progression),
    ItemNames.MAGICAL_BOOMERANG: ItemData(102, useful),
    ItemNames.RAFT: ItemData(103, progression),
    ItemNames.STEPLADDER: ItemData(104, progression),
    ItemNames.RECORDER: ItemData(105, progression),
    ItemNames.MAGICAL_ROD: ItemData(106, progression),
    ItemNames.RED_CANDLE: ItemData(107, progression),
    ItemNames.BOOK_OF_MAGIC: ItemData(108, progression),
    ItemNames.MAGICAL_KEY: ItemData(109, useful),
    ItemNames.RED_RING: ItemData(110, useful),
    ItemNames.SILVER_ARROW: ItemData(111, progression),
    ItemNames.SWORD: ItemData(112, progression),
    ItemNames.WHITE_SWORD: ItemData(113, progression),
    ItemNames.MAGICAL_SWORD: ItemData(114, progression),
    ItemNames.HEART_CONTAINER: ItemData(115, progression),
    ItemNames.LETTER: ItemData(116, progression),
    ItemNames.MAGICAL_SHIELD: ItemData(117, useful),
    ItemNames.CANDLE: ItemData(118, progression),
    ItemNames.ARROW: ItemData(119, progression),
    ItemNames.FOOD: ItemData(120, progression),
    ItemNames.WATER_OF_LIFE_BLUE: ItemData(121, useful),
    ItemNames.WATER_OF_LIFE_RED: ItemData(122, useful),
    ItemNames.BLUE_RING: ItemData(123, useful),
    ItemNames.TRIFORCE_FRAGMENT: ItemData(124, progression),
    ItemNames.POWER_BRACELET: ItemData(125, useful),
    ItemNames.SMALL_KEY: ItemData(126, filler),
    ItemNames.BOMB: ItemData(127, filler),
    ItemNames.RECOVERY_HEART: ItemData(128, filler),
    ItemNames.FIVE_RUPEES: ItemData(129, filler),
    ItemNames.RUPEE: ItemData(130, filler),
    ItemNames.CLOCK: ItemData(131, filler),
    ItemNames.FAIRY: ItemData(132, filler)

}

item_game_ids = {
    ItemNames.BOMB: 0x00,
    ItemNames.SWORD: 0x01,
    ItemNames.WHITE_SWORD: 0x02,
    ItemNames.MAGICAL_SWORD: 0x03,
    ItemNames.FOOD: 0x04,
    ItemNames.RECORDER: 0x05,
    ItemNames.CANDLE: 0x06,
    ItemNames.RED_CANDLE: 0x07,
    ItemNames.ARROW: 0x08,
    ItemNames.SILVER_ARROW: 0x09,
    ItemNames.BOW: 0x0A,
    ItemNames.MAGICAL_KEY: 0x0B,
    ItemNames.RAFT: 0x0C,
    ItemNames.STEPLADDER: 0x0D,
    ItemNames.FIVE_RUPEES: 0x0F,
    ItemNames.MAGICAL_ROD: 0x10,
    ItemNames.BOOK_OF_MAGIC: 0x11,
    ItemNames.BLUE_RING: 0x12,
    ItemNames.RED_RING: 0x13,
    ItemNames.POWER_BRACELET: 0x14,
    ItemNames.LETTER: 0x15,
    ItemNames.SMALL_KEY: 0x19,
    ItemNames.HEART_CONTAINER: 0x1A,
    ItemNames.TRIFORCE_FRAGMENT: 0x1B,
    ItemNames.MAGICAL_SHIELD: 0x1C,
    ItemNames.BOOMERANG: 0x1D,
    ItemNames.MAGICAL_BOOMERANG: 0x1E,
    ItemNames.WATER_OF_LIFE_BLUE: 0x1F,
    ItemNames.WATER_OF_LIFE_RED: 0x20,
    ItemNames.RECOVERY_HEART: 0x22,
    ItemNames.RUPEE: 0x18,
    ItemNames.CLOCK: 0x21,
    ItemNames.FAIRY: 0x23
}

# Item prices are going to get a bit of a writeup here, because these are some seemingly arbitrary
# design decisions and future contributors may want to know how these were arrived at.

# First, I based everything off of the Blue Ring. Since the Red Ring is twice as good as the Blue Ring,
# logic dictates it should cost twice as much. Since you can't make something cost 500 rupees, the only
# solution was to halve the price of the Blue Ring. Correspondingly, everything else sold in shops was
# also cut in half.

# Then, I decided on a factor for swords. Since each sword does double the damage of its predecessor, each
# one should be at least double. Since the sword saves so much time when upgraded (as, unlike other items,
# you don't need to switch to it), I wanted a bit of a premium on upgrades. Thus, a 4x multiplier was chosen,
# allowing the basic Sword to stay cheap while making the Magical Sword be a hefty upgrade you'll
# feel the price of.

# Since arrows do the same amount of damage as the White Sword and silver arrows are the same with the Magical Sword.
# they were given corresponding costs.

# Utility items were based on the prices of the shield, keys, and food. Broadly useful utility items should cost more,
# while limited use utility items should cost less. After eyeballing those, a few editorial decisions were made as
# deliberate thumbs on the scale of game balance. Those exceptions will be noted below. In general, prices were chosen
# based on how a player would feel spending that amount of money as opposed to how useful an item actually is.

item_prices = {
    ItemNames.BOMB: 10,
    ItemNames.SWORD: 10,
    ItemNames.WHITE_SWORD: 40,
    ItemNames.MAGICAL_SWORD: 160,
    ItemNames.FOOD: 30,
    ItemNames.RECORDER: 45,
    ItemNames.CANDLE: 30,
    ItemNames.RED_CANDLE: 60,
    ItemNames.ARROW: 40,
    ItemNames.SILVER_ARROW: 160,
    ItemNames.BOW: 40,
    ItemNames.MAGICAL_KEY: 250,  # Replacing all small keys commands a high premium
    ItemNames.RAFT: 80,
    ItemNames.STEPLADDER: 80,
    ItemNames.FIVE_RUPEES: 255,  # This could cost anything above 5 Rupees and be fine, but 255 is the funniest
    ItemNames.MAGICAL_ROD: 100,  # White Sword with forever beams should cost at least more than the White Sword itself
    ItemNames.BOOK_OF_MAGIC: 60,
    ItemNames.BLUE_RING: 125,
    ItemNames.RED_RING: 250,
    ItemNames.POWER_BRACELET: 25,
    ItemNames.LETTER: 20,
    ItemNames.SMALL_KEY: 40,
    ItemNames.HEART_CONTAINER: 80,
    ItemNames.TRIFORCE_FRAGMENT: 200,  # Since I couldn't make Zelda 1 track shop purchases, this is how to discourage repeat
    # Triforce purchases. The punishment for endless Rupee grinding to avoid searching out
    # Triforce pieces is that you're doing endless Rupee grinding to avoid playing the game
    ItemNames.MAGICAL_SHIELD: 45,
    ItemNames.BOOMERANG: 5,
    ItemNames.MAGICAL_BOOMERANG: 20,
    ItemNames.WATER_OF_LIFE_BLUE: 20,
    ItemNames.WATER_OF_LIFE_RED: 34,
    ItemNames.RECOVERY_HEART: 5,
    ItemNames.RUPEE: 50,
    ItemNames.CLOCK: 0,
    ItemNames.FAIRY: 10
}
