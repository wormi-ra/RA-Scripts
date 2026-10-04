from pycheevos.core.condition import ConditionList
from pycheevos.models.set import AchievementSet, Leaderboard
from pycheevos.models.achievement import Achievement
from pycheevos.core.helpers import *
from pycheevos.core.constants import *

from logic import *
from memory import Memory
from framework import achievement, achievement_set, leaderboard

from data import *
import assets
import csv

FRAMERATE = 60

@achievement_set(
    assets=assets,
    author="Wormi"
)
class Worms4MayhemSet(AchievementSet):
    def __init__(self):
        super().__init__(
            game_id=20526,
            title="Worms 4: Mayhem"
        )

    @achievement(642019)
    def tutorial(self, ach: Achievement):
        mission = Mission.TUTORIAL[2] # Mike's Secret Laboratory
        ach.add_core(group(
            mission.is_loaded() &
            mission.on_complete()
        ))

    ####################
    # Progression      #
    ####################

    @achievement(642020)
    def prog_construction(self, ach: Achievement):
        mission = Mission.STORY[4] # Destruct And Serve
        ach.add_core(group(
            mission.is_loaded() &
            mission.on_complete()
        ))

    @achievement(642021)
    def prog_camelot(self, ach: Achievement):
        mission = Mission.STORY[9] # Nice To Siege You
        ach.add_core(group(
            mission.is_loaded() &
            mission.on_complete()
        ))

    @achievement(642022)
    def prog_wild_west(self, ach: Achievement):
        mission = Mission.STORY[14] # High Noon Hijinx
        ach.add_core(group(
            mission.is_loaded() &
            mission.on_complete()
        ))

    @achievement(642023)
    def prog_arabian(self, ach: Achievement):
        mission = Mission.STORY[19] # Gibbon Take
        ach.add_core(group(
            mission.is_loaded() &
            mission.on_complete()
        ))

    @achievement(642024)
    def prog_prehistoric(self, ach: Achievement):
        mission = Mission.STORY[24] # Valley Of The Dinoworms
        ach.add_core(group(
            mission.is_loaded() &
            mission.on_complete()
        ))

    ####################
    # Unlocks          #
    ####################

    @achievement(642025)
    def unlocks_sounds(self, ach: Achievement):
        ach.add_core(group(
            Worms4Mayhem.menu_selected("WXFE.ItemShop"),
            measured_if(Worms4Mayhem.game_booted()),
            measured(Unlock.on_unlock_type(Unlock.Type.SOUND))
        ))

    @achievement(642026)
    def unlocks_maps(self, ach: Achievement):
        ach.add_core(group(
            Worms4Mayhem.menu_selected("WXFE.ItemShop"),
            measured_if(Worms4Mayhem.game_booted()),
            measured(Unlock.on_unlock_type(Unlock.Type.MAP))
        ))

    @achievement(642027)
    def unlocks_hats(self, ach: Achievement):
        ach.add_core(group(
            Worms4Mayhem.menu_selected("WXFE.ItemShop"),
            measured_if(Worms4Mayhem.game_booted()),
            measured(Unlock.on_unlock_type(Unlock.Type.HAT))
        ))

    @achievement(642028)
    def unlocks_face(self, ach: Achievement):
        ach.add_core(group(
            Worms4Mayhem.menu_selected("WXFE.ItemShop"),
            measured_if(Worms4Mayhem.game_booted()),
            measured(Unlock.on_unlock_type(Unlock.Type.FACE))
        ))

    @achievement(642029)
    def unlocks_hands(self, ach: Achievement):
        ach.add_core(group(
            Worms4Mayhem.menu_selected("WXFE.ItemShop"),
            measured_if(Worms4Mayhem.game_booted()),
            measured(Unlock.on_unlock_type(Unlock.Type.HAND))
        ))

    @achievement(642030)
    def unlocks_mustaches(self, ach: Achievement):
        ach.add_core(group(
            Worms4Mayhem.menu_selected("WXFE.ItemShop"),
            measured_if(Worms4Mayhem.game_booted()),
            measured(Unlock.on_unlock_type(Unlock.Type.MUSTACHE))
        ))

    @achievement(642031)
    def unlocks_weapons(self, ach: Achievement):
        ach.add_core(group(
            Worms4Mayhem.menu_selected("WXFE.ItemShop"),
            measured_if(Worms4Mayhem.game_booted()),
            measured(Unlock.on_unlock_type(Unlock.Type.WEAPON))
        ))

    @achievement(642032)
    def unlocks_game_styles(self, ach: Achievement):
        ach.add_core(group(
            Worms4Mayhem.menu_selected("WXFE.ItemShop"),
            measured_if(Worms4Mayhem.game_booted()),
            measured(Unlock.on_unlock_type(Unlock.Type.SCHEME))
        ))

    @achievement(642033)
    def unlocks_sets(self, ach: Achievement):
        ach.add_core(group(
            Worms4Mayhem.menu_selected("WXFE.ItemShop"),
            measured_if(Worms4Mayhem.game_booted()),
            measured(Unlock.on_unlock_type(Unlock.Type.SET))
        ))

    ####################
    # Misc             #
    ####################

    @achievement(642034)
    def wormpot(self, ach: Achievement):
        ach.add_core(group(
            Worms4Mayhem.menu_selected("WXFE.Wormpot"),
            XData.on_value_increased("WXFE.Shop.Balance")
        ))

    ####################
    # Leaderboards     #
    ####################

    @leaderboard(174176)
    def lb_hashmap_check(self, lb: Leaderboard):
        lb.set_start(
            (delta(Memory.STATE_GAME_INITIALIZED) == 0) &
            (Memory.STATE_GAME_INITIALIZED == 1) &
            (Memory.XDATARESOURCEMANAGER >> dword(0x18) != value(0xde74c0))
        )
        lb.set_cancel(always_false())
        lb.set_submit(always_true())
        lb.set_value(
            measured(Memory.XDATARESOURCEMANAGER >> dword(0x18))
        )


if __name__=="__main__":
    Worms4Mayhem.init()
    Worms4MayhemSet().save("output/")
