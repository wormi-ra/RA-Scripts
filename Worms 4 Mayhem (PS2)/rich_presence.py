from pycheevos.core.helpers import add_address, add_source, byte, delta, dword, dword_be, measured, measured_if, measured_percent, recall, remember, sub_source, value, group, string_equals, word_be
from pycheevos.models.rich_presence import *

from logic import *
from memory import Memory

MENU_LOOKUP = {
    "WXFE.Boot": "⏳Starting the game",
    "WXFE.MainMenu": "🌐In the main menu",
    "WXFE.Tutorial": "🎯Selecting a tutorial",
    "WXFE.Story": "📖Selecting a story chapter",
    "WXFE.CreateAGame": "✏️Creating a Multiplayer game",
    "WXFE.CreateAGameDest": "✏️Creating a Destruction game",
    "WXFE.CreateAGameSD": "✏️Creating a Statue Defender game",
    "WXFE.Wormpot": "🎰Gambling on the Wormpot",
    "WXFE.Customise": "✏️Editing teams",
    "WXFE.TeamOptions": "✏️Customizing a team",
    "WXFE.WeaponFactory1": "✏️Designing a secret weapon",
    "WXFE.SchemeBuilderBase": "✏️Editing a game style",
    "WXFE.Challenges": "🏆Selecting a challenge",
    "WXFE.TrophyCabinet": "🏆Taking pride in their achievements",
    "WXFE.ItemShop": "💰Shopping for items",
    "WXFE.Options": "⚙️In the options menu",
    "WXFE.ControlOptions": "⚙️In the control options menu",
    "WXFE.SoundAndVideo": "⚙️In the sound and video menu",
    "WXFE.CenterScreen": "⚙️In the center screen menu",
    "WXFE.ChangingLanguage": "⚙️Selecting a language",
    "WXFE.Credits": "🌐Watching credits",
    "WXFE.PreStart": "⏳Starting a new game",
    "WXFE.WinTutorial": "🎯Completed a tutorial",
    "WXFE.WinMission": "📖Completed a mission",
    "WXFE.WinChallenge": "🏆Completed a challenge",
    "WXFE.WinRound": "🌐In the multiplayer results menu",
    "WXFE.PreRound": "🌐In the multiplayer results menu",
    "WXFE.WinMatch": "🌐In the multiplayer results menu",
    "WXFE.WinAward": "🏆Obtained a new trophy",
    "WXFE.EasterEggFound": "🥚Found an easter egg",
}

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
        return f"💰@Number({measured(XData.get_value("WXFE.Shop.Balance"))}) Coins"

    def status(self):
        groups = [
            group(
                measured_if(Worms4Mayhem.is_loading() == 1),
                measured(value(1)),
            ),
            group(
                measured_if(Worms4Mayhem.is_in_attract()),
                measured(value(2)),
            ),
            group(
                measured_if(Worms4Mayhem.watching_fmv()),
                measured(value(3)),
            ),
        ]
        status = "$".join([
            g.render() for g in groups
        ])
        return f"@Status({status})"

    def round_time(self):
        seconds = XData.get_value("ElapsedRoundTime") / 1000
        return f"⏱️@Seconds({measured(seconds)})"

    def landscape(self):
        landscape = 0
        return f"🗺️@Landscape({landscape})"

    def levels(self, strmap: StringMap):
        return f"@Level({strmap.generate(XData.get_value("GameLogic.CurrentScript"))})"

    def menu(self, strmap: StringMap):
        return f"@Menu({strmap.generate(XData.get_value("FE.CurrentMenu"))})"

    def generate(self):
        levelmap = StringMap([f"{mission.script}\0" for mission in Mission.ALL])
        menumap = StringMap([f"{menu}\0" for menu in MENU_LOOKUP.keys()])
        mission_icon = {
            Mission.Type.STORY: "📖",
            Mission.Type.TUTORIAL: "🎓",
            Mission.Type.CHALLENGE: "🏆",
            Mission.Type.MULTIPLAYER: "👥",
        }
        self.add_lookup(
            "Level", 
            values={
                i+1: f"{mission_icon[Mission.ALL[i].mtype]}{Mission.ALL[i].name}"
                for i in range(len(Mission.ALL))
            },
            default="Playing Worms 4: Mayhem"
        )
        self.add_lookup(
            "Menu", 
            values={
                i+1: f"{name}"
                for i, name in zip(range(len(MENU_LOOKUP)), MENU_LOOKUP.values())
            },
            default="Playing Worms 4: Mayhem"
        )
        self.add_lookup(
            "Status",
            values={
                1: "⏳Loading...",
                2: "🎬Watching a demo play",
                3: "🎬Watching a cutscene",
            },
            default="Playing Worms 4: Mayhem"
        )
        # self.add_lookup(
        #     "Landscape",
        #     values={
        #         landscape.maxheight: landscape.name
        #         for landscape in Landscape.LANDSCAPES
        #     },
        #     default="Custom Map"
        # )
        self.add_lookup(
            "Language",
            values={
                0x0: "🇬🇧",
                0x3: "🇫🇷",
                0x4: "🇩🇪",
                0x5: "🇮🇹",
                0x9: "🇪🇸",
            }
        )
        self.add_lookup(
            "Paused",
            values={
                0x1: "⏸️ ",
            },
            default=""
        )

        self.add_display(
            (
                Worms4Mayhem.game_booted() &
                Worms4Mayhem.is_ingame() &
                ~Worms4Mayhem.is_in_attract() &
                ~Worms4Mayhem.watching_fmv()
            ),
            f"{self.paused()}{self.levels(levelmap)} • {self.round_time()} • {self.coins()} • {self.unlocks()} • {self.trophies()} • {self.language()}"
        )
        self.add_display(
            (
                Worms4Mayhem.game_booted() &
                Worms4Mayhem.is_in_menu() &
                ~Worms4Mayhem.watching_fmv()
            ),
            f"{self.menu(menumap)} • {self.coins()} • {self.unlocks()} • {self.trophies()} • {self.language()}"
        )
        self.add_display(
            (
                Worms4Mayhem.game_booted()
            ),
            f"{self.status()} • {self.coins()} • {self.unlocks()} • {self.trophies()} • {self.language()}"
        )
        self.add_display(None, "Playing Worms 4: Mayhem")


if __name__=="__main__":
    Worms4Mayhem.init()
    rp = Worms4RichPresence()
    rp.generate()
    rp.save(rp.game_id, path="output/")
