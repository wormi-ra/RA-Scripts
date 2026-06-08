from pycheevos.core.helpers import add_address, add_source, byte, delta, dword, dword_be, measured, measured_if, measured_percent, recall, remember, sub_source, value, group, string_equals, word_be
from pycheevos.models.rich_presence import *

from data import UNLOCKS, Missions
from logic import Context, GameMode, Landscape, Lua, Mission, Worms3D, XData
from memory import Memory

class WormsRichPresence(RichPresence):
    def __init__(self):
        super().__init__()
        self.game_id = 21184

    def region(self, ctx: Context):
        region = {
            "EU": "🇪🇺",
            "US": "🇺🇸",
        }[ctx.region]
        lang = measured(XData.get_value(ctx, "SAVE.Language"))
        return f"{region}@Language({lang})"

    def unlocks(self, ctx: Context):
        unlocks = group(
            *[
                sub_source(unlock.locked(ctx))
                for unlock in UNLOCKS
            ],
            remember(value(len(UNLOCKS))),
            remember(recall() * 100),
            remember(recall() / len(UNLOCKS)),
            measured_if(recall() <= 100),
            measured(recall()),
        )
        return f"🔓@Number({unlocks})%"

    def level_hash(self, ctx: Context):
        return measured(Mission.current_hash(ctx))

    def paused(self, ctx: Context):
        return f"@Paused({measured(Worms3D.is_paused(ctx).lvalue)})"

    def status(self, ctx: Context):
        status = measured({
            "EU": Memory.EU_FLOWCONTROLSERVICE_GAME_STATE,
            "US": Memory.US_FLOWCONTROLSERVICE_GAME_STATE,
        }[ctx.region] & value(0x5c))
        return f"@Status({status})"

    def round_time(self, ctx: Context):
        seconds = XData.get_value(ctx, "ElapsedRoundTime") / 1000
        return f"⏱️@Seconds({measured(seconds)})"

    def landscape(self, ctx: Context):
        landscape = group(
            measured_if(XData.get_value(ctx, "Land.File") >> byte(0x0) != 0),
            measured(XData.get_value(ctx, "Land.InitialMaxHeight")),
        )
        return f"🗺️@Landscape({landscape})"

    def generate(self):
        self.add_lookup(
            "Level", 
            values={
                mission.filehash: mission.name
                for mission in (Missions.TUTORIAL + Missions.CAMPAIGN + Missions.CHALLENGE)
            },
            default=""
        )
        self.add_lookup(
            "Landscape",
            values={
                landscape.maxheight: landscape.name
                for landscape in Landscape.LANDSCAPES
            },
            default="Custom Map"
        )
        self.add_lookup(
            "GameMode",
            values={
                GameMode.TUTORIAL: "🎯Tutorial",
                GameMode.CAMPAIGN: "🗺️Campaign",
                GameMode.CHALLENGE: "🏆Challenge",
            },
        )
        self.add_lookup(
            "Language",
            values={
                0x0: " (🇬🇧)",
                # 0x1: " (🇺🇸)",
                0x3: " (🇫🇷)",
                0x4: " (🇩🇪)",
                0x5: " (🇮🇹)",
                0x9: " (🇪🇸)",
            }
        )
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
                (64, 68, 72, 76, 80, 84, 88, 92): "🎬Watching a movie",
                (4, 8, 12, 16, 20, 24, 28): "⏳Loading...",
                (0,): "🌐Main Menu",
            },
            default="🥥Shaking their coconuts"
        )
        for ctx in [Context("US"), Context("EU")]:
            self.add_display(
                (
                    Worms3D.check_serial(ctx) &
                    Worms3D.is_ingame(ctx) &
                    (Mission.current_hash(ctx) == Lua.string_hash("stdvs"))
                ),
                f"{self.paused(ctx)}👥Multiplayer • {self.landscape(ctx)} • {self.round_time(ctx)} • {self.unlocks(ctx)} • {self.region(ctx)}"
            )
            self.add_display(
                (
                    Worms3D.check_serial(ctx) &
                    Worms3D.is_ingame(ctx) &
                    ~Worms3D.is_in_attract(ctx) &
                    (Mission.current_hash(ctx) != Lua.string_hash("stdvs"))
                ),
                f"{self.paused(ctx)}@GameMode({measured(Worms3D.current_gamemode(ctx))}) • 🗺️@Level({self.level_hash(ctx)}) • {self.round_time(ctx)} • {self.unlocks(ctx)} • {self.region(ctx)}"
            )
            self.add_display(
                (
                    Worms3D.check_serial(ctx) &
                    Worms3D.game_booted(ctx)
                ),
                f"{self.status(ctx)} • {self.unlocks(ctx)} • {self.region(ctx)}"
            )
        self.add_display(None, "Playing Worms 3D")


if __name__=="__main__":
    Worms3D.init()
    rp = WormsRichPresence()
    rp.generate()
    rp.save(rp.game_id, path="output/")
