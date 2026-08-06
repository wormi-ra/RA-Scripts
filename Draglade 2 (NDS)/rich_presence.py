from pycheevos.core.condition import ConditionList
from pycheevos.core.helpers import add_address, add_source, bit1, byte, delta, group, measured, recall, remember, value
from pycheevos.core.value import Flag
from pycheevos.models.rich_presence import *

# from logic import Level, LevelInfo
from memory import Memory, bitcount
from data import BULLETS, CHESTS, QUESTS, TITLES

class DG2RichPresence(RichPresence):
    def __init__(self):
        super().__init__()
        self.game_id = 26886

    def generate(self):
        # self.add_lookup("Level", {**Level.NAMES})
        self.add_lookup("Paused", {
            1: "▌▌ "
        })
        self.add_lookup("State", {
            2: "In the title screen",
            3: "In the main menu",
            5: "Playing the story",
            6: "VS CPU",
            7: "Training",
            8: "Learning to grap",
            0xb: "Trying to setup Wi-Fi for some reason",
        }, default="Playing Draglade 2")
        self.add_display(
            (
                (Memory.STATE_GAME_BOOTED == 1)
            ),
            f"{self.paused()}{self.game_state()} • {self.player_level()} • {self.credits()} • {self.story_progress()} • {self.total_quests()} • {self.total_bullets()} • {self.total_titles()}"
        )
        self.add_display(None, "Playing Custom Beat Battle: Draglade 2")

    def paused(self):
        return f"@Paused({bit1(Memory.STATE_GAME_PAUSE.address)})"

    def game_state(self):
        return f"@State({Memory.STATE_GAME_MODE})"

    def credits(self):
        return f"@Number({Memory.SAVE_DATA_CREDITS})￠"

    def player_level(self):
        return f"Lv.@Number({Memory.RAIO_LEVEL})"

    def story_progress(self):
        return f"📖Story @Number({group(
            remember(Memory.STORY_PROGRESS * 100),
            measured(recall() / 0xbd)
        )})%"

    def total_titles(self):
        titles = group(*[
            add_source(title / 2)
            for title in TITLES
        ])
        return f"🏅Titles @Number({measured(titles)})"

    def total_chests(self):
        chests = group(*[
            add_source(bitcount(chest.address))
            for chest in CHESTS
        ])
        return f"🧰Chests @Number({measured(chests)})/64"

    def total_quests(self):
        quests = group(*[
            add_source(quests)
            for quests in QUESTS
        ])
        return f"📜Quests @Number({measured(quests)})/30"

    def total_bullets(self):
        bullets = group(*[
            add_source(bitcount(bullet.address))
            for bullet in BULLETS
        ])
        return f"💥Bullets @Number({measured(bullets)})/105"

if __name__=="__main__":
    rp = DG2RichPresence()
    rp.generate()
    rp.save(rp.game_id, path="output/")

