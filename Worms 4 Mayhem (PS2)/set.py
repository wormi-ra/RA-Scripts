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

FRAMERATE = 50

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
    # Story Challenges #
    ####################

    @achievement(648990)
    def diner_might(self, ach: Achievement):
        mission = Mission.STORY[0] # Diner Might
        enemies = [4, 5, 6, 7]
        ach.add_core(group(
            mission.is_loaded(),
            XData.get_value("ElapsedRoundTime") > value(0),
            *[
                Worm(enemy).get_instance().is_alive()
                for enemy in enemies
            ],
            trigger(mission.on_complete()),
        ))

    @achievement(648987)
    def sneaky_bridge_thieves(self, ach: Achievement):
        mission = Mission.STORY[1] # Sneaky Bridge Thieves
        ach.add_core(group(
            mission.on_start().with_hits(1),
            trigger(mission.on_complete()),
            reset_if(~Worms4Mayhem.is_ingame()),
            reset_if(
                (delta(Worms4Mayhem.current_team()) == 0) &
                (Worms4Mayhem.current_team() == 1)
            ).with_hits(2)
        ))

    @achievement(648988)
    def building_site_saboteurs(self, ach: Achievement):
        mission = Mission.STORY[2] # Building Site Saboteurs
        ach.add_core(group(
            mission.on_start().with_hits(1),
            trigger(mission.on_complete()),
            reset_if(~Worms4Mayhem.is_ingame()),
            reset_if(
                (Worms4Mayhem.current_team() == 0) &
                (Worm(0).get_instance().equipped_weapon != Weapons.DYNAMITE) &
                Worm.on_attack()
            ),
            reset_if(Inventory.on_ammo_decrease(Weapons.AIR_STRIKE, 0, Inventory.InventoryType.ALLIANCE))
        ))

    @achievement(648991)
    def the_crate_escape(self, ach: Achievement):
        mission = Mission.STORY[3] # The Crate Escape
        enemies = [2, 3, 4, 5]
        # Main logic
        ach.add_core(group(
            reset_if(~Worms4Mayhem.is_ingame()),
            reset_if(
                (Worms4Mayhem.current_team() == 0) &
                (Worm.get_active_worm().using_parachute() == 1)
            ),
        ))
        # Kill counter
        ach.add_alt(group(
            measured_if(mission.on_start().with_hits(1)),
            *(
                add_hits(
                    Worm(enemy).get_instance().on_death()
                ).with_hits(1)
                for enemy in enemies
            ),
            measured(always_false()).with_hits(len(enemies)),
            mission.on_complete()
        ))
        # Challenge indicator (never trigger)
        ach.add_alt(group(
            mission.on_start().with_hits(1),
            trigger(always_false()),
        ))

    @achievement(648989)
    def destruct_and_serve(self, ach: Achievement):
        mission = Mission.STORY[4] # Destruct And Serve
        enemies = [4, 5, 6, 7, 8, 9]
        ach.add_core(group(
            mission.on_start().with_hits(1),
            mission.time_bonus_on_pace(),
            trigger(mission.on_complete()),
            reset_if(~Worms4Mayhem.is_ingame()),
            reset_if(group(
                *[
                    add_source(Worm(enemy).get_instance().health)
                    for enemy in enemies
                ],
                (value(0) != value(0)) &
                XData.on_value_changed("Trigger.Index") &
                (XData.get_value("Trigger.Index") < value(8))
            ))
        ))

    @achievement(649252)
    def storm_the_castle(self, ach: Achievement):
        mission = Mission.STORY[5] # Storm The Castle
        enemies = [5, 6, 7, 8, 10, 11, 12, 14]
        time_machine = Lua.Node("TimeMachinePartsHaveBeenCollected", MemoryExpression(recall()))
        ach.add_core(group(
            mission.on_start().with_hits(1),
            XData.get_value("Girder.TotalNumberPlaced") <= value(1),
            trigger(mission.on_complete()),
            remember(Lua.get_node(time_machine.key, 8, 0).address),
            reset_if(
                (time_machine.get_hash() == value(time_machine.hashstr)) &
                (time_machine.get_value(type=dword) == value(0x0)) &
                (XData.get_value("DeadWorm.Id") >= 5)
            ),
            reset_if(~Worms4Mayhem.is_ingame()),
        ))

    @achievement(649534)
    def the_windy_wizard(self, ach: Achievement):
        mission = Mission.STORY[6] # The Windy Wizard
        player = Worm(1).get_instance()
        wizard = Worm(9).get_instance()
        ach.add_core(group(
            mission.on_start().with_hits(1),
            trigger(mission.on_complete()),
            reset_next_if(wizard.is_alive()).with_hits(1),
            reset_if(
                (Worms4Mayhem.current_team() == 0) &
                (player.equipped_weapon == Weapons.BAZOOKA) &
                Worm.on_attack()
            ),
            reset_if(~Worms4Mayhem.is_ingame()),
        ))

    @achievement(649535)
    def rob_in_the_hood(self, ach: Achievement):
        mission = Mission.STORY[7] # Rob In The Hood
        ach.add_core(group(
            mission.on_start().with_hits(1),
            mission.time_bonus_on_pace(),
            trigger(mission.on_complete()),
            reset_if(
                XData.on_value_decreased("Jetpack.Fuel")
            ),
            reset_if(~Worms4Mayhem.is_ingame()),
        ))

    @achievement(649536)
    def joust_about_it(self, ach: Achievement):
        mission = Mission.STORY[8] # Joust About It
        player_team = [1, 2, 3]
        recall_worm = Worm.Instance(MemoryExpression(recall()))
        ach.add_core(group(
            mission.on_start().with_hits(1),
            trigger(mission.on_complete()),
            *[
                group(
                    remember(Worm(id).get_instance()),
                    reset_if(recall_worm.health == 0x0),
                    reset_if(recall_worm.on_healed()),
                )
                for id in player_team
            ],
            reset_if(~Worms4Mayhem.is_ingame()),
        ))

    @achievement(649537)
    def nice_to_siege_you(self, ach: Achievement):
        mission = Mission.STORY[9] # Nice To Siege You
        player_team = [0, 1, 2]
        enemy_team = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        kills = 15
        # prof = 3
        # easter egg worm = 14
        ach.add_core(group(
            *[
                reset_if(Worm(id).get_instance().health == 0x0)
                for id in player_team
            ],
            reset_if(~Worms4Mayhem.is_ingame()),
        ))
        # Kill counter
        ach.add_alt(group(
            measured_if(mission.on_start().with_hits(1)),
            pause_if(XData.get_value("ElapsedRoundTime") == 0x0),
            *(
                add_hits(
                    Worm(enemy).get_instance().on_death()
                )
                for enemy in enemy_team
            ),
            measured(always_false()).with_hits(kills),
            mission.on_complete()
        ))
        # Challenge indicator (never trigger)
        ach.add_alt(group(
            mission.on_start().with_hits(1),
            trigger(always_false()),
        ))

    @achievement()
    def mine_all_mine(self, ach: Achievement):
        mission = Mission.STORY[10] # Mine All Mine
        ach.add_core(group(
            mission.on_start().with_hits(1),
            trigger(mission.on_complete()),
            reset_if(
                (Worms4Mayhem.current_team() == 0) &
                (Worm.get_active_worm().equipped_weapon == Weapons.BASEBALL_BAT) &
                Worm.on_attack()
            ).with_hits(2),
            reset_if(~Worms4Mayhem.is_ingame()),
        ))

    @achievement()
    def ghost_hill_graveyard(self, ach: Achievement):
        mission = Mission.STORY[11] # Ghost Hill Graveyard
        enemies = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ach.add_core(group(
            mission.on_start().with_hits(1),
            pause_if(XData.get_value("ElapsedRoundTime") == 0x0),
            trigger(mission.on_complete()),
            reset_next_if(XData.get_value("Crate.Index") == 0x4).with_hits(1),
            and_next(Worms4Mayhem.current_team() == 0x0),
            *(
                group(
                    add_source(delta(Worm(enemy).get_instance().health)),
                    sub_source(Worm(enemy).get_instance().health),
                )
                for enemy in enemies
            ),
            reset_if(value(0x80000000) > value(0x80000000)),
            reset_if(~Worms4Mayhem.is_ingame()),
        ))

    @achievement()
    def tin_can_wally(self, ach: Achievement):
        mission = Mission.STORY[12] # Tin Can Wally
        ach.add_core(group(
            mission.on_start().with_hits(1),
            trigger(mission.on_complete()),
            reset_if(
                (Worms4Mayhem.current_team() == 0x0) &
                (XData.on_value_increased("TurnTimeRemaining"))
            ).with_hits(9),
            reset_if(~Worms4Mayhem.is_ingame()),
        ))

    @achievement()
    def doom_canyon(self, ach: Achievement):
        mission = Mission.STORY[13] # Doom Canyon
        ach.add_core(group(
            mission.on_start().with_hits(1),
            trigger(mission.on_complete()),
            reset_if(~Worms4Mayhem.is_ingame()),
        ))

    @achievement()
    def high_noon_hijinx(self, ach: Achievement):
        mission = Mission.STORY[14] # High Noon Hijinx
        ach.add_core(group(
            mission.on_start().with_hits(1),
            trigger(mission.on_complete()),
            reset_if(~Worms4Mayhem.is_ingame()),
        ))

    @achievement()
    def turkish_delights(self, ach: Achievement):
        mission = Mission.STORY[15] # Turkish Delights
        ach.add_core(group(
            mission.on_start().with_hits(1),
            trigger(mission.on_complete()),
            reset_if(~Worms4Mayhem.is_ingame()),
        ))

    @achievement()
    def no_room_for_error(self, ach: Achievement):
        mission = Mission.STORY[16] # No Room For Error
        ach.add_core(group(
            mission.on_start().with_hits(1),
            trigger(mission.on_complete()),
            reset_if(~Worms4Mayhem.is_ingame()),
        ))

    @achievement()
    def carpet_capers(self, ach: Achievement):
        mission = Mission.STORY[17] # Carpet Capers
        ach.add_core(group(
            mission.on_start().with_hits(1),
            trigger(mission.on_complete()),
            reset_if(~Worms4Mayhem.is_ingame()),
        ))

    @achievement()
    def traitorous_waters(self, ach: Achievement):
        mission = Mission.STORY[18] # Traitorous Waters
        ach.add_core(group(
            mission.on_start().with_hits(1),
            trigger(mission.on_complete()),
            reset_if(~Worms4Mayhem.is_ingame()),
        ))

    @achievement()
    def gibbon_take(self, ach: Achievement):
        mission = Mission.STORY[19] # Gibbon Take
        ach.add_core(group(
            mission.on_start().with_hits(1),
            trigger(mission.on_complete()),
            reset_if(~Worms4Mayhem.is_ingame()),
        ))

    @achievement()
    def fast_food_dino(self, ach: Achievement):
        mission = Mission.STORY[20] # Fast Food Dino
        ach.add_core(group(
            mission.on_start().with_hits(1),
            trigger(mission.on_complete()),
            reset_if(~Worms4Mayhem.is_ingame()),
        ))

    @achievement()
    def escape_from_tree_rex(self, ach: Achievement):
        mission = Mission.STORY[21] # Escape From Tree-Rex
        ach.add_core(group(
            mission.on_start().with_hits(1),
            trigger(mission.on_complete()),
            reset_if(~Worms4Mayhem.is_ingame()),
        ))

    @achievement()
    def chute_to_victory(self, ach: Achievement):
        mission = Mission.STORY[22] # Chute To Victory
        ach.add_core(group(
            mission.on_start().with_hits(1),
            trigger(mission.on_complete()),
            reset_if(~Worms4Mayhem.is_ingame()),
        ))

    @achievement()
    def the_land_that_worms_forgot(self, ach: Achievement):
        mission = Mission.STORY[23] # The Land That Worms Forgot
        ach.add_core(group(
            mission.on_start().with_hits(1),
            trigger(mission.on_complete()),
            reset_if(~Worms4Mayhem.is_ingame()),
        ))

    @achievement()
    def valley_of_the_dinoworms(self, ach: Achievement):
        mission = Mission.STORY[24] # Valley Of The Dinoworms
        ach.add_core(group(
            mission.on_start().with_hits(1),
            trigger(mission.on_complete()),
            reset_if(~Worms4Mayhem.is_ingame()),
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

    @leaderboard(174727)
    def lb_time_tracker(self, lb: Leaderboard):
        lb.set_start(group(
            Worms4Mayhem.is_in_menu(),
            reset_next_if(
                (Controller.button_pressed(Controller.Button.L1) == 0) |
                (Controller.button_pressed(Controller.Button.R1) == 0)
            ),
            (
                (Controller.button_pressed(Controller.Button.L1) == 1) &
                (Controller.button_pressed(Controller.Button.R1) == 1)
            ).with_hits(FRAMERATE * 2),
        ))
        lb.set_cancel(group(
            Worms4Mayhem.is_in_menu(),
            reset_next_if(
                (Controller.button_pressed(Controller.Button.L1) == 0) |
                (Controller.button_pressed(Controller.Button.R1) == 0)
            ),
            (
                (Controller.button_pressed(Controller.Button.L1) == 1) &
                (Controller.button_pressed(Controller.Button.R1) == 1)
            ).with_hits(FRAMERATE * 4),
        ))
        lb.set_submit(always_false())
        for mission in (Mission.STORY + Mission.CHALLENGE):
            lb.add_value(group(
                measured_if(mission.is_loaded()),
                sub_source(XData.get_value("ElapsedRoundTime")),
                remember(value(mission.time_bonus * 1000)),
                measured_if(recall() < 0x80000000),
                measured(recall() / value(10)),
            ))

    @leaderboard(176438)
    def lb_worminkle_university(self, lb: Leaderboard):
        Mission.TUTORIAL[0].generate_leaderboard(lb)

    @leaderboard(176439)
    def lb_unsporting_behaviour(self, lb: Leaderboard):
        Mission.TUTORIAL[1].generate_leaderboard(lb)

    @leaderboard(176440)
    def lb_mikes_secret_laboratory(self, lb: Leaderboard):
        Mission.TUTORIAL[2].generate_leaderboard(lb)

    @leaderboard(176441)
    def lb_diner_might(self, lb: Leaderboard):
        Mission.STORY[0].generate_leaderboard(lb)

    @leaderboard(176442)
    def lb_sneaky_bridge_thieves(self, lb: Leaderboard):
        Mission.STORY[1].generate_leaderboard(lb)

    @leaderboard(176443)
    def lb_building_site_saboteurs(self, lb: Leaderboard):
        Mission.STORY[2].generate_leaderboard(lb)

    @leaderboard(176444)
    def lb_the_crate_escape(self, lb: Leaderboard):
        Mission.STORY[3].generate_leaderboard(lb)

    @leaderboard(176445)
    def lb_destruct_and_serve(self, lb: Leaderboard):
        Mission.STORY[4].generate_leaderboard(lb)

    @leaderboard(176446)
    def lb_storm_the_castle(self, lb: Leaderboard):
        Mission.STORY[5].generate_leaderboard(lb)

    @leaderboard(176447)
    def lb_the_windy_wizard(self, lb: Leaderboard):
        Mission.STORY[6].generate_leaderboard(lb)

    @leaderboard(176448)
    def lb_rob_in_the_hood(self, lb: Leaderboard):
        Mission.STORY[7].generate_leaderboard(lb)

    @leaderboard(176449)
    def lb_joust_about_it(self, lb: Leaderboard):
        Mission.STORY[8].generate_leaderboard(lb)

    @leaderboard(176450)
    def lb_nice_to_siege_you(self, lb: Leaderboard):
        Mission.STORY[9].generate_leaderboard(lb)

    @leaderboard(176569)
    def lb_nice_to_siege_you_kills(self, lb: Leaderboard):
        mission = Mission.STORY[9] # Nice To Siege You
        enemy_team = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        lb.set_start(mission.on_start())
        lb.set_cancel(~Worms4Mayhem.is_ingame())
        lb.set_submit(mission.on_complete())
        lb.set_value(group(
            pause_if(XData.get_value("ElapsedRoundTime") == 0x0),
            *(
                add_hits(
                    Worm(enemy).get_instance().on_death()
                )
                for enemy in enemy_team
            ),
            measured(always_false())
        ))

    @leaderboard(176451)
    def lb_mine_all_mine(self, lb: Leaderboard):
        Mission.STORY[10].generate_leaderboard(lb)

    @leaderboard(176452)
    def lb_ghost_hill_graveyard(self, lb: Leaderboard):
        Mission.STORY[11].generate_leaderboard(lb)

    @leaderboard(176453)
    def lb_tin_can_wally(self, lb: Leaderboard):
        Mission.STORY[12].generate_leaderboard(lb)

    @leaderboard(176454)
    def lb_doom_canyon(self, lb: Leaderboard):
        Mission.STORY[13].generate_leaderboard(lb)

    @leaderboard(176455)
    def lb_high_noon_hijinx(self, lb: Leaderboard):
        Mission.STORY[14].generate_leaderboard(lb)

    @leaderboard(176456)
    def lb_turkish_delights(self, lb: Leaderboard):
        Mission.STORY[15].generate_leaderboard(lb)

    @leaderboard(176457)
    def lb_no_room_for_error(self, lb: Leaderboard):
        Mission.STORY[16].generate_leaderboard(lb)

    @leaderboard(176458)
    def lb_carpet_capers(self, lb: Leaderboard):
        Mission.STORY[17].generate_leaderboard(lb)

    @leaderboard(176459)
    def lb_traitorous_waters(self, lb: Leaderboard):
        Mission.STORY[18].generate_leaderboard(lb)

    @leaderboard(176460)
    def lb_gibbon_take(self, lb: Leaderboard):
        Mission.STORY[19].generate_leaderboard(lb)

    @leaderboard(176461)
    def lb_fast_food_dino(self, lb: Leaderboard):
        Mission.STORY[20].generate_leaderboard(lb)

    @leaderboard(176462)
    def lb_escape_from_tree_rex(self, lb: Leaderboard):
        Mission.STORY[21].generate_leaderboard(lb)

    @leaderboard(176463)
    def lb_chute_to_victory(self, lb: Leaderboard):
        Mission.STORY[22].generate_leaderboard(lb)

    @leaderboard(176464)
    def lb_the_land_that_worms_forgot(self, lb: Leaderboard):
        Mission.STORY[23].generate_leaderboard(lb)

    @leaderboard(176465)
    def lb_valley_of_the_dinoworms(self, lb: Leaderboard):
        Mission.STORY[24].generate_leaderboard(lb)

    @leaderboard(176466)
    def lb_sniper_rifle_challenge(self, lb: Leaderboard):
        Mission.CHALLENGE[0].generate_leaderboard(lb)

    @leaderboard(176467)
    def lb_jet_pack_challenge(self, lb: Leaderboard):
        Mission.CHALLENGE[1].generate_leaderboard(lb)

    @leaderboard(176468)
    def lb_super_sheep_challenge(self, lb: Leaderboard):
        Mission.CHALLENGE[2].generate_leaderboard(lb)

    @leaderboard(176469)
    def lb_icarus_potion_challenge(self, lb: Leaderboard):
        Mission.CHALLENGE[3].generate_leaderboard(lb)

    @leaderboard(176470)
    def lb_shotgun_challenge(self, lb: Leaderboard):
        Mission.CHALLENGE[4].generate_leaderboard(lb)

    @leaderboard(176478)
    def lb_accuracy_challenge(self, lb: Leaderboard):
        Mission.CHALLENGE[5].generate_leaderboard(lb)

    @leaderboard(176471)
    def lb_navigation_challenge(self, lb: Leaderboard):
        Mission.CHALLENGE[6].generate_leaderboard(lb)

    @leaderboard(176479)
    def lb_crate_collect_challenge(self, lb: Leaderboard):
        Mission.CHALLENGE[7].generate_leaderboard(lb)

    @leaderboard(176476)
    def lb_deathmatch_1(self, lb: Leaderboard):
        Mission.CHALLENGE[8].generate_leaderboard(lb)

    @leaderboard(176472)
    def lb_deathmatch_2(self, lb: Leaderboard):
        Mission.CHALLENGE[9].generate_leaderboard(lb)

    @leaderboard(176480)
    def lb_deathmatch_3(self, lb: Leaderboard):
        Mission.CHALLENGE[10].generate_leaderboard(lb)

    @leaderboard(176473)
    def lb_deathmatch_4(self, lb: Leaderboard):
        Mission.CHALLENGE[11].generate_leaderboard(lb)

    @leaderboard(176481)
    def lb_deathmatch_5(self, lb: Leaderboard):
        Mission.CHALLENGE[12].generate_leaderboard(lb)

    @leaderboard(176474)
    def lb_deathmatch_6(self, lb: Leaderboard):
        Mission.CHALLENGE[13].generate_leaderboard(lb)

    @leaderboard(176482)
    def lb_deathmatch_7(self, lb: Leaderboard):
        Mission.CHALLENGE[14].generate_leaderboard(lb)

    @leaderboard(176477)
    def lb_deathmatch_8(self, lb: Leaderboard):
        Mission.CHALLENGE[15].generate_leaderboard(lb)

    @leaderboard(176475)
    def lb_deathmatch_9(self, lb: Leaderboard):
        Mission.CHALLENGE[16].generate_leaderboard(lb)

    @leaderboard(176483)
    def lb_deathmatch_10(self, lb: Leaderboard):
        Mission.CHALLENGE[17].generate_leaderboard(lb)

if __name__=="__main__":
    Worms4Mayhem.init()
    Worms4MayhemSet().save("output/")
