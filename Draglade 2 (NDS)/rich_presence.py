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
            5: "Story Mode",
            6: "VS Mode",
            7: "Training",
            8: "Learning to grap",
            0xb: "Trying to setup Wi-Fi for some reason",
        }, default="Playing Draglade 2")
        self.add_lookup("Area", {
            # Story
            range(0x01, 0x0d+1): "King's Area",
            range(0x0e, 0x15+1): "Elekick Area",
            range(0x16, 0x17+1): "Goshi Desert",
            range(0x18, 0x1a+1): "King's Area",
            range(0x1b, 0x1e+1): "Water Area",
            range(0x1f, 0x25+1): "Volcano Area",
            range(0x26, 0x28+1): "Saru Ruins",
            range(0x29, 0x2c+1): "Canyon Area",
            range(0x2d, 0x35+1): "Harmonic Area",
            range(0x36, 0x3e+1): "Elekick Area",
            range(0x3f, 0x45+1): "Water Area",
            0x46: "Matter Energy Lab",
            range(0x47, 0x48+1): "King's Area",
            range(0x49, 0x5b+1): "Okuman Land",
            range(0x5c, 0x5f+1): "Zoff Pass",
            range(0x60, 0x65+1): "Canyon Area",
            range(0x66, 0x68+1): "Ghost Underground",
            range(0x69, 0x6a+1): "King's Area",
            0x6b: "Matter Energy Lab",
            range(0x6c, 0x6d+1): "King's Area",
            range(0x6e, 0x74+1): "Harmonic Area",
            range(0x75, 0x77+1): "Win Desert",
            range(0x78, 0x7e+1): "Water Area",
            range(0x7f, 0x82+1): "Volcano Area",
            range(0x83, 0x89+1): "Elekick Area",
            range(0x8a, 0x8c+1): "Kenmeri Forest",
            range(0x8d, 0x90+1): "Harmonic Area",
            range(0x91, 0x93+1): "Iwaku Pass",
            range(0x94, 0x9c+1): "Canyon Area",
            range(0x9d, 0x9f+1): "Poshka Ruins",
            range(0xa0, 0xa2+1): "King's Area",
            range(0xa3, 0xa9+1): "Volcano Area",
            range(0xaa, 0xaf+1): "King's Area",
            range(0xb0, 0xb1+1): "Matter Energy Lab",
            range(0xb2, 0xb4+1): "Underground Lab",
            range(0xb5, 0xb7+1): "Deep Underground Lab",
            range(0xb8, 0xb9+1): "Underground Lab Core",
            range(0xba, 0xbc+1): "Matter Energy Lab",
            range(0xbd, 0xc0+1): "King's Area",
            range(0xc1, 0xc2+1): "Credits",
            # Quest Cutscenes
            0xc3: "Mirage Egg",
            0xc4: "Dropped DS",
            0xc5: "My Treasure",
            # Quests
            0xc6: "King's Area",
            0xc7: "Elekick Area",
            range(0xc8, 0xcd+1): "Goshi Desert",
            0xce: "Volcano Area",
            range(0xcf, 0xd7+1): "Saru Ruins",
            0xd8: "Harmonic Area",
            0xd9: "Elekick Area",
            0xda: "Water Area",
            range(0xdb, 0xdf+1): "Okuman Land",
            range(0xe0, 0xe6+1): "Zoff Pass",
            0xe7: "Canyon Area",
            range(0xe8, 0xf3+1): "Ghost Underground",
            0xf4: "Harmonic Area",
            0xf5: "Win Desert",
            0xf6: "Water Area",
            0xf7: "Volcano Area",
            range(0xf8, 0x10d+1): "Kenmeri Forest",
            0x10e: "Iwaku Pass",
            0x10f: "Canyon Area",
            range(0x110, 0x122+1): "Poshka Ruins",
            0x123: "Volcano Area",
            range(0x124, 0x12b+1): "Underground Lab",
            0x12c: "Underground Lab",
            range(0x12d, 0x139+1): "Deep Underground Lab",
            range(0x13a, 0x156+1): "Underground Lab Core",
            0x157: "King's Area (Evil One)",
            range(0x158, 0x15f+1): "Mirage Egg",
            0x160: "Return It",
            range(0x161, 0x175+1): "DS Dropped",
            0x176: "DoraDora",
            range(0x177, 0x17f+1): "My Treasure",
            0x180: "Change Beat!",
            0x181: "Charismatic Grapper",
            0x182: "Mysterious Grapper",
            0x183: "Goril's Roar",
            0x184: "Goril's Roar+",
            0x185: "Goril's Rage",
            0x186: "Final Goril",
            range(0x187, 0x18c+1): "Arman Ranger",
            range(0x18d, 0x198+1): "Arman Soldier",
            range(0x199, 0x19f+1): "Golden Arman",
            range(0x1a0, 0x1b2+1): "Ultimate Arman",
            range(0x1b3, 0x1ba+1): "Sudden Death",
            0x1bc: "G-Center",
            # Overworld
            range(0x1be, 0x1c9+1): "King's Area",
            range(0x1ca, 0x1d8+1): "Volcano Area",
            range(0x1d9, 0x1e7+1): "Water Area",
            range(0x1e8, 0x1f5+1): "Canyon Area",
            range(0x1f6, 0x204+1): "Elekick Area",
            range(0x205, 0x213+1): "Harmonic Area",
            range(0x214, 0x21b+1): "Matter Energy Lab",
            range(0x21c, 0x21d+1): "Okuman Land",
            range(0x21e, 0x21f+1): "Challenge Area",
            0x220: "Underground Lab",
            0x221: "Deep Underground Lab",
            range(0x222, 0x224+1): "G-Live",
            range(0x225, 0x230+1): "Challenge Area",
            # Misc
            range(0x231, 0x24f+1): "GNN",
            0x250: "Area Selection",
            0x251: "Title Screen",
        })
        self.add_lookup("Char", {
            0x0: "Hibito",
            0x1: "Guy",
            0x2: "Daichi",
            0x3: "Kyle",
            0x4: "Zeke",
            0x5: "Cross",
            0x6: "Raio",
            0x7: "Jet",
            0x8: "Neon",
            0x9: "Kamzou",
            0xa: "Ichiman",
            0xb: "Ask",
            range(0xd, 0x18+1): "Grapper",
        })
        self.add_lookup("GHall", {
            0x6: "King's Area",
            0x7: "Volcano Area",
            0x8: "Water Area",
            0x9: "Canyon Area",
            0x10: "G-Live",
            0xa: "Elekick Area",
            0xb: "Harmonic Area",
            0xd: "Training Arena",
            0xc: "Okuman Land",
            0xe: "CoroCoro Arena",
            0xf: "Training Arena",
            0x14: "G-Live",
            0x3f: "Zoff Pass",
            0x49: "Underground Lab",
            0x4a: "Underground Hideout",
        })
        self.add_display(
            (
                (Memory.AREA_POINTER != 0)
            ),
            f"{self.paused()}{self.game_state()} • {self.area_script()} • {self.player_level()} • {self.credits()} • {self.story_progress()} • {self.total_quests()} • {self.total_bullets()} • {self.total_titles()}"
        )
        self.add_display(
            (
                (Memory.STATE_GAME_MODE == 5)
            ),
            f"{self.paused()}{self.game_state()} • {self.area_save()} • {self.player_level()} • {self.credits()} • {self.story_progress()} • {self.total_quests()} • {self.total_bullets()} • {self.total_titles()}"
        )
        self.add_display(
            group(
                (Memory.STATE_GAME_MODE == 6) | (Memory.STATE_GAME_MODE == 7),
                (Memory.RESULT_STATE != 0),
            ),
            f"{self.paused()}{self.game_state()} • {self.player_char()} VS {self.enemy_char()} • {self.ghall()} • {self.player_level()} • {self.credits()} • {self.story_progress()} • {self.total_quests()} • {self.total_bullets()} • {self.total_titles()}"
        )
        self.add_display(
            (
                (Memory.STATE_GAME_BOOTED == 1)
            ),
            f"{self.paused()}{self.game_state()} • {self.player_level()} • {self.credits()} • {self.story_progress()} • {self.total_quests()} • {self.total_bullets()} • {self.total_titles()}"
        )
        self.add_display(None, "Playing Custom Beat Battle: Draglade 2")

    def player_char(self):
        return f"@Char({Memory.BATTLE_PLAYER_CHARACTER})"

    def enemy_char(self):
        return f"@Char({Memory.BATTLE_ENEMY_CHARACTER})"

    def ghall(self):
        return f"🗺️@GHall({Memory.BATTLE_G_HALL})"

    def area_script(self):
        return f"🗺️@Area({Memory.CURRENT_SCRIPT_ID})"

    def area_save(self):
        return f"🗺️@Area({Memory.SAVE_DATA_SCRIPT_ID})"

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

