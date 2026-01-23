from pycheevos.core.condition import ConditionList
from pycheevos.core.helpers import add_address, add_source, byte, measured
from pycheevos.core.value import Flag
from pycheevos.models.rich_presence import *

from logic import Level, LevelInfo
from memory import Memory

def render(conditions: ConditionList):
    return "_".join([cond.render() for cond in conditions])

class RaymanRichPresence(RichPresence):
    def __init__(self):
        super().__init__()
        self.game_id = 20900

    def generate(self):
        # TODO game over screen, options screen, intro cutscene, ending cutscene, credits
        self.add_lookup("Level", {**Level.NAMES})
        self.add_lookup("Paused", {
            1: "▌▌ "
        })
        self.add_display(
            (Memory.STATE_DEMO_PLAY == 1),
            "Rayman is watching a demo play"
        )
        self.add_display(
            (
                ((Memory.STATE_CURRENT_SAVE_FILE == 0) |
                (Memory.STATE_INGAME != 1)) &
                (Memory.STATE_IN_LEVEL_SELECT != 1)
            ),
            "Rayman is in the title screen"
        )
        self.add_display(
            Memory.STATE_IN_LEVEL_SELECT == 1,
            f"Rayman is selecting a level | {self.ingame_status()} | {self.save_status()}"
        )
        self.add_display(
            (
                (Memory.STATE_INGAME == 1) &
                (Memory.BONUS_LEVEL_TIME_LEFT != 0xfffe)
            ),
            f"{self.paused()}Rayman is playing a Magician level in @Level({Memory.LEVEL_SELECT_CURRENT_LEVEL_ID}) {self.level_cages()} | {self.bonus_timer()} {self.bonus_tings()} {self.lives()} | {self.save_status()}"
        )
        self.add_display(
            Memory.STATE_INGAME == 1,
            f"{self.paused()}Rayman is in @Level({Memory.LEVEL_SELECT_CURRENT_LEVEL_ID}) {self.level_cages()} | {self.ingame_status()} | {self.save_status()}"
        )
        self.add_display(None, "Playing Rayman")

    def build_lookup(self, lookup: dict[tuple[int,...], int])-> dict[int, str]:
        output = {}
        for keys, value in lookup.items():
            for key in keys:
                output[key] = Level.NAMES[value]
        return output

    def paused(self):
        return f"@Paused({Memory.INGAME_PAUSED})"

    def bonus_tings(self):
        total_tings = (Condition(Memory.BONUS_LEVEL_TINGS_LEFT,  "+", Memory.BONUS_LEVEL_TINGS))
        return f"🔵x@Number({Memory.BONUS_LEVEL_TINGS})/@Number({total_tings})"

    def bonus_timer(self):
        return f"🕑@Number({(Memory.BONUS_LEVEL_TIME_LEFT / 60)})"

    def total_cages(self):
        cages = ConditionList([
            add_source(Condition(LevelInfo(id).cages))
            for id in range(len(Level.NAMES))
        ]).with_flag(Flag.MEASURED)
        return f"😊@Number({render(cages)})/102"

    def tings(self):
        return f"🔵x@Number({Memory.NUMBER_OF_TINGS})"

    def level_cages(self):
        cages = ConditionList([
            add_address(Memory.LEVEL_SELECT_CURRENT_LEVEL_ID * LevelInfo.MEMSIZE),
            measured(byte(Memory.LEVEL_INFO_PINK_PLANT_WOODS + 0x8))
        ])
        return f"😊@Number({render(cages)})/6"

    def lives(self):
        return f"❤️x@Number({Memory.NUMBER_OF_LIVES})"

    def continues(self):
        return f"⏰@Number({Memory.RAYMAN_CONTINUES})"

    def ingame_status(self):
        return f"{self.lives()} {self.tings()}"

    def save_status(self):
        return f"{self.total_cages()} {self.continues()}"

if __name__=="__main__":
    rp = RaymanRichPresence()
    rp.generate()
    rp.save(rp.game_id, path="output/")

