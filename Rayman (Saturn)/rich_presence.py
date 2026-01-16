from pycheevos.core.condition import ConditionList
from pycheevos.core.helpers import add_address, add_source, byte, measured
from pycheevos.core.value import Flag
from pycheevos.models.rich_presence import *

from logic import LevelInfo
from memory import Memory

BONUS_LEVEL = "a Bonus Level"

FOREST_LOOKUP = {
    (1,2,3,4,20,21): 0,
    (5,6,7,8): 1,
    (9,10,11,18): 2,
    (12,13,14,15,16,17,19): 3
}

BAND_LOOKUP = {
    (1,2,3,4,5,6,17): 4,
    (7,8,9,10,11,18): 5,
    (12,13): 6,
    (14,15,16): 7
}

MOUNTAIN_LOOKUP = {
    (1,2): 8,
    (3,4,5,12): 9,
    (6,7,8,9,10,11,13): 10,
}

PICTURE_LOOKUP = {
    (1,2,3,4,12): 11,
    (5,6,7): 12,
    (8,9,10,11,13): 13,
}

CAVES_LOOKUP = {
    (1,2): 14,
    (5,6,7): 15,
    (8,9,10,11,13): 16,
}

WORLD_DICT = {
    1: "Forest",
    2: "Band",
    3: "Mountains",
    4: "Picture",
    5: "Caves",
    6: "Candy",
}

def render(conditions: ConditionList):
    return "_".join([cond.render() for cond in conditions])

class RaymanRichPresence(RichPresence):
    def __init__(self):
        super().__init__()
        self.game_id = 20900

    def generate(self):
        # TODO game over screen, options screen, intro cutscene, ending cutscene, credits
        self.add_lookup("Level", {**LevelInfo.NAMES})
        self.add_lookup("Paused", {
            1: "▌▌ "
        })
        self.add_display(
            (Memory.STATE_DEMO_PLAY == 1),
            "Rayman is watching a demo play"
        )
        self.add_display(
            (ConditionList(
                ((Memory.STATE_CURRENT_SAVE_FILE == 0) |
                (Memory.STATE_INGAME != 1)) &
                (Memory.STATE_IN_LEVEL_SELECT != 1)
            )),
            "Rayman is in the title screen"
        )
        self.add_display(
            Memory.STATE_IN_LEVEL_SELECT == 1,
            f"Rayman is selecting a level | {self.total_cages()} {self.lives()} {self.continues()}"
        )
        self.add_display(
            (
                (Memory.STATE_INGAME == 1) &
                (Memory.BONUS_LEVEL_TIME_LEFT != 0xfffe)
            ),
            f"{self.paused()}Rayman is playing a Magician level in @Level({Memory.LEVEL_SELECT_CURRENT_LEVEL_ID}) | {self.bonus_timer()} {self.bonus_tings()}"
        )
        self.add_display(
            Memory.STATE_INGAME == 1,
            f"{self.paused()}Rayman is in @Level({Memory.LEVEL_SELECT_CURRENT_LEVEL_ID}) | {self.ingame_status()}"
        )
        self.add_display(None, "Playing Rayman")

    def build_lookup(self, lookup: dict[tuple[int,...], int])-> dict[int, str]:
        output = {}
        for keys, value in lookup.items():
            for key in keys:
                output[key] = LevelInfo.NAMES[value]
        return output

    def paused(self):
        return f"@Paused({Memory.INGAME_PAUSED})"

    def bonus_tings(self):
        total_tings = (Condition(Memory.BONUS_LEVEL_TINGS_LEFT,  "+", Memory.BONUS_LEVEL_TINGS))
        return f"🔵x@Unsigned({Memory.BONUS_LEVEL_TINGS})/@Unsigned({total_tings})"

    def bonus_timer(self):
        return f"🕑@Unsigned({(Memory.BONUS_LEVEL_TIME_LEFT / 60)})"

    def total_cages(self):
        cages = ConditionList([
            add_source(Condition(LevelInfo(id).cages))
            for id in range(len(LevelInfo.NAMES))
        ]).with_flag(Flag.MEASURED)
        return f"😊x@Unsigned({render(cages)})/102"

    def tings(self):
        return f"🔵x@Unsigned({Memory.NUMBER_OF_TINGS})"

    def level_cages(self):
        cages = ConditionList([
            add_address(Memory.LEVEL_SELECT_CURRENT_LEVEL_ID * LevelInfo.SIZE),
            measured(byte(Memory.LEVEL_INFO_PINK_PLANT_WOODS + 0x8))
        ])
        return f"😊x@Unsigned({render(cages)})/6"

    def lives(self):
        return f"❤️x@Unsigned({Memory.NUMBER_OF_LIVES})"

    def continues(self):
        return f"⏰x@Unsigned({Memory.RAYMAN_CONTINUES})"

    def ingame_status(self):
        return f"{self.level_cages()} {self.lives()} {self.tings()} {self.continues()}"

if __name__=="__main__":
    rp = RaymanRichPresence()
    rp.generate()
    rp.save(rp.game_id, path="output/")

