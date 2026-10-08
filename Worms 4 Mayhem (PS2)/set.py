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
        missions = Mission.STORY[0:5]
        ach.add_core(conditions=group(
            Worms4Mayhem.is_ingame(),
            *[
                add_source(delta(mission.completion_unlock()) / 2)
                for mission in missions
            ],
            value(0) == value(len(missions) - 1),
            *[
                add_source((mission.completion_unlock()) / 2)
                for mission in missions
            ],
            value(0) == value(len(missions)),
        ))

    @achievement(642021)
    def prog_camelot(self, ach: Achievement):
        missions = Mission.STORY[5:10]
        ach.add_core(conditions=group(
            Worms4Mayhem.is_ingame(),
            *[
                add_source(delta(mission.completion_unlock()) / 2)
                for mission in missions
            ],
            value(0) == value(len(missions) - 1),
            *[
                add_source((mission.completion_unlock()) / 2)
                for mission in missions
            ],
            value(0) == value(len(missions)),
        ))

    @achievement(642022)
    def prog_wild_west(self, ach: Achievement):
        missions = Mission.STORY[10:15]
        ach.add_core(conditions=group(
            Worms4Mayhem.is_ingame(),
            *[
                add_source(delta(mission.completion_unlock()) / 2)
                for mission in missions
            ],
            value(0) == value(len(missions) - 1),
            *[
                add_source((mission.completion_unlock()) / 2)
                for mission in missions
            ],
            value(0) == value(len(missions)),
        ))

    @achievement(642023)
    def prog_arabian(self, ach: Achievement):
        missions = Mission.STORY[15:20]
        ach.add_core(conditions=group(
            Worms4Mayhem.is_ingame(),
            *[
                add_source(delta(mission.completion_unlock()) / 2)
                for mission in missions
            ],
            value(0) == value(len(missions) - 1),
            *[
                add_source((mission.completion_unlock()) / 2)
                for mission in missions
            ],
            value(0) == value(len(missions)),
        ))

    @achievement(642024)
    def prog_prehistoric(self, ach: Achievement):
        missions = Mission.STORY[20:25]
        ach.add_core(conditions=group(
            Worms4Mayhem.is_ingame(),
            *[
                add_source(delta(mission.completion_unlock()) / 2)
                for mission in missions
            ],
            value(0) == value(len(missions) - 1),
            *[
                add_source((mission.completion_unlock()) / 2)
                for mission in missions
            ],
            value(0) == value(len(missions)),
        ))

    ####################
    # Time Bonus       #
    ####################

    @achievement(642889)
    def time_bonus_construction(self, ach: Achievement):
        missions = Mission.STORY[0:5]
        ach.add_core(conditions=group(
            Worms4Mayhem.is_ingame(),
            *[
                add_source(delta(mission.time_bonus_unlock()) / 2)
                for mission in missions
            ],
            value(0) == value(len(missions) - 1),
            *[
                add_source((mission.time_bonus_unlock()) / 2)
                for mission in missions
            ],
            value(0) == value(len(missions)),
        ))

    @achievement(642890)
    def time_bonus_camelot(self, ach: Achievement):
        missions = Mission.STORY[5:10]
        ach.add_core(conditions=group(
            Worms4Mayhem.is_ingame(),
            *[
                add_source(delta(mission.time_bonus_unlock()) / 2)
                for mission in missions
            ],
            value(0) == value(len(missions) - 1),
            *[
                add_source((mission.time_bonus_unlock()) / 2)
                for mission in missions
            ],
            value(0) == value(len(missions)),
        ))

    @achievement(642891)
    def time_bonus_wild_west(self, ach: Achievement):
        missions = Mission.STORY[10:15]
        ach.add_core(conditions=group(
            Worms4Mayhem.is_ingame(),
            *[
                add_source(delta(mission.time_bonus_unlock()) / 2)
                for mission in missions
            ],
            value(0) == value(len(missions) - 1),
            *[
                add_source((mission.time_bonus_unlock()) / 2)
                for mission in missions
            ],
            value(0) == value(len(missions)),
        ))

    @achievement(642892)
    def time_bonus_arabian(self, ach: Achievement):
        missions = Mission.STORY[15:20]
        ach.add_core(conditions=group(
            Worms4Mayhem.is_ingame(),
            *[
                add_source(delta(mission.time_bonus_unlock()) / 2)
                for mission in missions
            ],
            value(0) == value(len(missions) - 1),
            *[
                add_source((mission.time_bonus_unlock()) / 2)
                for mission in missions
            ],
            value(0) == value(len(missions)),
        ))

    @achievement(642893)
    def time_bonus_prehistoric(self, ach: Achievement):
        missions = Mission.STORY[20:25]
        ach.add_core(conditions=group(
            Worms4Mayhem.is_ingame(),
            *[
                add_source(delta(mission.time_bonus_unlock()) / 2)
                for mission in missions
            ],
            value(0) == value(len(missions) - 1),
            *[
                add_source((mission.time_bonus_unlock()) / 2)
                for mission in missions
            ],
            value(0) == value(len(missions)),
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
    # Trophies         #
    ####################

    @achievement(642135)
    def trophy_bronze_damage(self, ach: Achievement):
        unlock = Unlock.get_unlock("Lock.Award.10")
        ach.add_core(group(
            Worms4Mayhem.game_booted(),
            Worms4Mayhem.is_ingame(),
            unlock.on_unlock()
        ))

    @achievement(642136)
    def trophy_silver_damage(self, ach: Achievement):
        unlock = Unlock.get_unlock("Lock.Award.5")
        ach.add_core(group(
            Worms4Mayhem.game_booted(),
            Worms4Mayhem.is_ingame(),
            unlock.on_unlock()
        ))

    @achievement(642137)
    def trophy_gold_damage(self, ach: Achievement):
        unlock = Unlock.get_unlock("Lock.Award.0")
        ach.add_core(group(
            Worms4Mayhem.game_booted(),
            Worms4Mayhem.is_ingame(),
            unlock.on_unlock()
        ))

    @achievement(642138)
    def trophy_body_count(self, ach: Achievement):
        unlock = Unlock.get_unlock("Lock.Award.11")
        ach.add_core(group(
            Worms4Mayhem.game_booted(),
            Worms4Mayhem.is_ingame(),
            unlock.on_unlock()
        ))

    @achievement(642139)
    def trophy_3_bagger(self, ach: Achievement):
        unlock = Unlock.get_unlock("Lock.Award.6")
        ach.add_core(group(
            Worms4Mayhem.game_booted(),
            Worms4Mayhem.is_ingame(),
            unlock.on_unlock()
        ))


    @achievement(642140)
    def trophy_4_bagger(self, ach: Achievement):
        unlock = Unlock.get_unlock("Lock.Award.1")
        ach.add_core(group(
            Worms4Mayhem.game_booted(),
            Worms4Mayhem.is_ingame(),
            unlock.on_unlock()
        ))

    @achievement(642141)
    def trophy_barrel_buster(self, ach: Achievement):
        unlock = Unlock.get_unlock("Lock.Award.12")
        ach.add_core(group(
            Worms4Mayhem.game_booted(),
            Worms4Mayhem.is_ingame(),
            unlock.on_unlock()
        ))

    @achievement(642142)
    def trophy_hot_foot(self, ach: Achievement):
        unlock = Unlock.get_unlock("Lock.Award.7")
        ach.add_core(group(
            Worms4Mayhem.game_booted(),
            Worms4Mayhem.is_ingame(),
            unlock.on_unlock()
        ))

    @achievement(642143)
    def trophy_big_blast(self, ach: Achievement):
        unlock = Unlock.get_unlock("Lock.Award.2")
        ach.add_core(group(
            Worms4Mayhem.game_booted(),
            Worms4Mayhem.is_ingame(),
            unlock.on_unlock()
        ))

    @achievement(642144)
    def trophy_rocketeer(self, ach: Achievement):
        unlock = Unlock.get_unlock("Lock.Award.13")
        ach.add_core(group(
            Worms4Mayhem.game_booted(),
            Worms4Mayhem.is_ingame(),
            unlock.on_unlock()
        ))

    @achievement(642145)
    def trophy_animal_lover(self, ach: Achievement):
        unlock = Unlock.get_unlock("Lock.Award.8")
        ach.add_core(group(
            Worms4Mayhem.game_booted(),
            Worms4Mayhem.is_ingame(),
            unlock.on_unlock()
        ))

    @achievement(642146)
    def trophy_magic_bullet(self, ach: Achievement):
        unlock = Unlock.get_unlock("Lock.Award.3")
        ach.add_core(group(
            Worms4Mayhem.game_booted(),
            Worms4Mayhem.is_ingame(),
            unlock.on_unlock()
        ))

    @achievement(642147)
    def trophy_greedy_worm(self, ach: Achievement):
        unlock = Unlock.get_unlock("Lock.Award.14")
        ach.add_core(group(
            Worms4Mayhem.game_booted(),
            Worms4Mayhem.is_ingame(),
            unlock.on_unlock()
        ))

    @achievement(642148)
    def trophy_weapon_specialist(self, ach: Achievement):
        unlock = Unlock.get_unlock("Lock.Award.9")
        ach.add_core(group(
            Worms4Mayhem.game_booted(),
            Worms4Mayhem.is_ingame(),
            unlock.on_unlock()
        ))

    @achievement(642149)
    def trophy_the_beast_within(self, ach: Achievement):
        unlock = Unlock.get_unlock("Lock.Award.4")
        ach.add_core(group(
            Worms4Mayhem.game_booted(),
            Worms4Mayhem.is_ingame(),
            unlock.on_unlock()
        ))

    @achievement(642150)
    def trophy_all(self, ach: Achievement):
        ach.add_core(group(
            measured_if(Worms4Mayhem.game_booted()),
            Worms4Mayhem.is_ingame(),
            measured(Unlock.on_unlock_type(Unlock.Type.TROPHY))
        ))

    ####################
    # Easter Eggs      #
    ####################

    @achievement(642894)
    def easter_egg_1(self, ach: Achievement):
        mission = Mission.STORY[4] # Destruct And Serve
        unlock = Unlock.get_unlock("Lock.EasterEgg.0")
        ach.add_core(group(
            mission.is_loaded(),
            unlock.on_unlock()
        ))

    @achievement(642895)
    def easter_egg_2(self, ach: Achievement):
        mission = Mission.STORY[9] # Nice To Siege You
        unlock = Unlock.get_unlock("Lock.EasterEgg.1")
        ach.add_core(group(
            mission.is_loaded(),
            unlock.on_unlock()
        ))

    @achievement(642896)
    def easter_egg_3(self, ach: Achievement):
        mission = Mission.STORY[12] # Tin Can Wally
        unlock = Unlock.get_unlock("Lock.EasterEgg.2")
        ach.add_core(group(
            mission.is_loaded(),
            unlock.on_unlock()
        ))

    @achievement(642897)
    def easter_egg_4(self, ach: Achievement):
        mission = Mission.STORY[17] # Carpet Capers
        unlock = Unlock.get_unlock("Lock.EasterEgg.3")
        ach.add_core(group(
            mission.is_loaded(),
            unlock.on_unlock()
        ))

    @achievement(642898)
    def easter_egg_5(self, ach: Achievement):
        mission = Mission.STORY[21] # Escape From Tree-Rex
        unlock = Unlock.get_unlock("Lock.EasterEgg.4")
        ach.add_core(group(
            mission.is_loaded(),
            unlock.on_unlock()
        ))

    ####################
    # Challenges       #
    ####################

    @achievement(642899)
    def challenge_completion(self, ach: Achievement):
        missions = Mission.CHALLENGE[0:8]
        ach.add_core(conditions=group(
            measured_if(Worms4Mayhem.game_booted()),
            Worms4Mayhem.is_ingame(),
            *[
                add_source(delta(mission.completion_unlock()) / 2)
                for mission in missions
            ],
            value(0) == value(len(missions) - 1),
            *[
                add_source((mission.completion_unlock()) / 2)
                for mission in missions
            ],
            measured(value(0) == value(len(missions))),
        ))

    @achievement(642900)
    def challenge_time_bonus(self, ach: Achievement):
        missions = Mission.CHALLENGE[0:8]
        ach.add_core(conditions=group(
            measured_if(Worms4Mayhem.game_booted()),
            Worms4Mayhem.is_ingame(),
            *[
                add_source(delta(mission.time_bonus_unlock()) / 2)
                for mission in missions
            ],
            value(0) == value(len(missions) - 1),
            *[
                add_source((mission.time_bonus_unlock()) / 2)
                for mission in missions
            ],
            measured(value(0) == value(len(missions))),
        ))

    @achievement(642901)
    def deathmatch_completion(self, ach: Achievement):
        missions = Mission.CHALLENGE[8:18]
        ach.add_core(conditions=group(
            measured_if(Worms4Mayhem.game_booted()),
            Worms4Mayhem.is_ingame(),
            *[
                add_source(delta(mission.completion_unlock()) / 2)
                for mission in missions
            ],
            value(0) == value(len(missions) - 1),
            *[
                add_source((mission.completion_unlock()) / 2)
                for mission in missions
            ],
            measured(value(0) == value(len(missions))),
        ))

    @achievement(642902)
    def deathmatch_time_bonus(self, ach: Achievement):
        missions = Mission.CHALLENGE[8:18]
        ach.add_core(conditions=group(
            measured_if(Worms4Mayhem.game_booted()),
            Worms4Mayhem.is_ingame(),
            *[
                add_source(delta(mission.time_bonus_unlock()) / 2)
                for mission in missions
            ],
            value(0) == value(len(missions) - 1),
            *[
                add_source((mission.time_bonus_unlock()) / 2)
                for mission in missions
            ],
            measured(value(0) == value(len(missions))),
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
