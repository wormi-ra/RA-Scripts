from pycheevos.core.helpers import add_address, add_source, byte, delta, dword, dword_be, measured, measured_if, measured_percent, recall, remember, sub_source, value, group, string_equals, word_be
from pycheevos.models.rich_presence import *

from logic import *
from memory import Memory

class Worms4RichPresence(RichPresence):
    def __init__(self):
        super().__init__()
        self.game_id = 20526

    def unlocks(self):
        unlocks = group(
            *[
                add_source(unlock.locked() / 2)
                for unlock in Unlock.UNLOCKS
            ],
            remember(value(0)),
            remember(recall() * 100),
            remember(recall() / len(Unlock.UNLOCKS)),
            measured_if(recall() <= 100),
            measured(recall()),
        )
        return f"🔓@Number({unlocks})%"

    def trophies(self):
        unlocks = list(filter(lambda e: e.type == Unlock.Type.TROPHY, Unlock.UNLOCKS))
        trophies = group(
            *[
                add_source(unlock.locked() / 2)
                for unlock in unlocks
            ],
            measured(value(0)),
        )
        return f"🏆@Number({trophies})"

    def language(self):
        return f"@Language({Memory.LANGUAGE})"

    # def level_hash(self):
    #     return measured(Mission.current_hash())

    def paused(self):
        return f"@Paused({measured(Worms4Mayhem.is_paused())})"

    def coins(self):
        return f"🟡@Number({measured(XData.get_value("WXFE.Shop.Balance"))}) Coins"

    def status(self):
        status = 0
        return f"@Status({status})"

    def round_time(self):
        seconds = XData.get_value("ElapsedRoundTime") / 1000
        return f"⏱️@Seconds({measured(seconds)})"

    def landscape(self):
        landscape = 0
        return f"🗺️@Landscape({landscape})"

    def generate(self):
        # self.add_lookup(
        #     "Level", 
        #     values={
        #         mission.filehash: mission.name
        #         for mission in (Missions.TUTORIAL + Missions.CAMPAIGN + Missions.CHALLENGE)
        #     },
        #     default=""
        # )
        # self.add_lookup(
        #     "Landscape",
        #     values={
        #         landscape.maxheight: landscape.name
        #         for landscape in Landscape.LANDSCAPES
        #     },
        #     default="Custom Map"
        # )
        # self.add_lookup(
        #     "Language",
        #     values={
        #         0x0: "🇬🇧",
        #         0x3: "🇫🇷",
        #         0x4: "🇩🇪",
        #         0x5: "🇮🇹",
        #         0x9: "🇪🇸",
        #     }
        # )
        self.add_lookup(
            "Paused",
            values={
                0x1: "▌▌ ",
            },
            default=""
        )
        self.add_lookup(
            "Status",
            values={
            },
            default="Playing Worms 4: Mayhem"
        )
        self.add_display(
            (
                Worms4Mayhem.game_booted()
            ),
            f"{self.status()} • {self.coins()} • {self.unlocks()} • {self.trophies()}"
        )
        self.add_display(None, "Playing Worms 4: Mayhem")


if __name__=="__main__":
    Worms4Mayhem.init()
    rp = Worms4RichPresence()
    rp.generate()
    rp.save(rp.game_id, path="output/")
