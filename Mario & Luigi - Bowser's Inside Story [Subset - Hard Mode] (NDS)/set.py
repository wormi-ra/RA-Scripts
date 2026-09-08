from argparse import Action

from pycheevos.core.condition import ConditionList
from pycheevos.models.set import AchievementSet, Leaderboard
from pycheevos.models.achievement import Achievement
from pycheevos.core.helpers import *
from pycheevos.core.constants import *

from logic import MnLBIS, Equipment, Actor
from memory import Memory
from framework import achievement, achievement_set, leaderboard

import assets

@achievement_set(
    assets=assets,
    author="Wormi",
    subset_id=42788,
)
class MnLBISSubset(AchievementSet):
    def __init__(self):
        super().__init__(
            game_id=5323,
            title="Mario & Luigi: Bowser's Inside Story"
        )

    @achievement(634108)
    def tutorial(self, ach: Achievement):
        ach.add_core(group(
            MnLBIS.is_in_battle(
                battle_id=0x1000,
                top_screen_id=0x218,
            ),
            trigger(MnLBIS.on_enemy_dead()),
            MnLBIS.is_challenge_medal_equipped(),
        ))

    @achievement()
    def mr_broque(self, ach: Achievement):
        ach.add_core(group(
            MnLBIS.is_in_battle(
                battle_id=0x1016,
                top_screen_id=0x3d,
            ),
            MnLBIS.level_cap(4),
            trigger(MnLBIS.on_enemy_dead()),
            MnLBIS.is_challenge_medal_equipped(),
            MnLBIS.check_cheated_equipments(),
            MnLBIS.forbidden_equipment([
                Equipment.DOCTOR_SOCKS,
                Equipment.GUMPTION_SOCKS,
                Equipment.BRO_SOCKS,
                Equipment.NO_TOUCH_SOCKS,
                Equipment.HEAVY_GLOVES,
                Equipment.SPECIAL_GLOVES,
                Equipment.SIPHON_GLOVES,
                Equipment.DELICIOUS_GLOVES,
                Equipment.HEAVY_BOOTS,
                Equipment.SPECIAL_BOOTS,
                Equipment.SHELL_BOOTS,
                Equipment.SHROOB_BOOTS,
                Equipment.SIPHON_BOOTS,
                Equipment.DAREDEVIL_BOOTS,
                Equipment.TIP_TOP_BOOTS,
                Equipment.LUCK_CHARM,
                Equipment.HAPPY_CHARM,
                Equipment.TIGHT_BELT,
                Equipment.BUDGET_CHARM,
                Equipment.ADVICE_PATCH,
                Equipment.HEROIC_PATCH,
                Equipment.LUXURY_PATCH,
                Equipment.BIG_SHELL,
                Equipment.SMALL_SHELL,
                Equipment.GIANT_SHELL,
                Equipment.KO_SHELL,
                Equipment.VENGEANCE_CAPE,
            ], Actor.MARIO_LUIGI),
            MnLBIS.forbidden_equipment([
                Equipment.IRON_FIST_BAND,
                Equipment.STAMINA_BAND,
                Equipment.LUCKY_BAND,
                Equipment.FURY_BAND,
                Equipment.VAMPIRE_BAND,
                Equipment.INTRUDER_FANGS,
                Equipment.BURNING_FANGS,
                Equipment.FURY_FANGS,
                Equipment.RESTORE_RING,
                Equipment.PEACE_RING,
                Equipment.EXCELLENT_RING,
                Equipment.DRUMSTICK_RING,
                Equipment.GLUTTON_RING,
                Equipment.ECONOMY_RING,
                Equipment.CHEAP_RING,
                Equipment.HEROIC_RING,
            ], Actor.BOWSER),
            reset_next_if(
                MnLBIS.on_retry() |
                (Memory.SCREEN_ID_ != 0x6be) # not in battle
            ),
            pause_if(MnLBIS.badge_used()).with_hits(1)
        ))

    @achievement()
    def sea_pipe_statue(self, ach: Achievement):
        ach.add_core(group(
            MnLBIS.is_in_battle(
                battle_id=0x1018,
                top_screen_id=0x28b,
            ),
            MnLBIS.level_cap(5),
            trigger(MnLBIS.on_enemy_dead()),
            MnLBIS.is_challenge_medal_equipped(),
            MnLBIS.check_cheated_equipments(),
            MnLBIS.forbidden_equipment([
                Equipment.DOCTOR_SOCKS,
                Equipment.GUMPTION_SOCKS,
                Equipment.BRO_SOCKS,
                Equipment.NO_TOUCH_SOCKS,
                Equipment.HEAVY_GLOVES,
                Equipment.SPECIAL_GLOVES,
                Equipment.SIPHON_GLOVES,
                Equipment.DELICIOUS_GLOVES,
                Equipment.HEAVY_BOOTS,
                Equipment.SPECIAL_BOOTS,
                Equipment.SHELL_BOOTS,
                Equipment.SHROOB_BOOTS,
                Equipment.SIPHON_BOOTS,
                Equipment.DAREDEVIL_BOOTS,
                Equipment.TIP_TOP_BOOTS,
                Equipment.LUCK_CHARM,
                Equipment.HAPPY_CHARM,
                Equipment.TIGHT_BELT,
                Equipment.BUDGET_CHARM,
                Equipment.ADVICE_PATCH,
                Equipment.HEROIC_PATCH,
                Equipment.LUXURY_PATCH,
                Equipment.BIG_SHELL,
                Equipment.SMALL_SHELL,
                Equipment.GIANT_SHELL,
                Equipment.KO_SHELL,
                Equipment.VENGEANCE_CAPE,
            ], Actor.MARIO_LUIGI),
            MnLBIS.forbidden_equipment([
                Equipment.IRON_FIST_BAND,
                Equipment.STAMINA_BAND,
                Equipment.LUCKY_BAND,
                Equipment.FURY_BAND,
                Equipment.VAMPIRE_BAND,
                Equipment.INTRUDER_FANGS,
                Equipment.BURNING_FANGS,
                Equipment.FURY_FANGS,
                Equipment.RESTORE_RING,
                Equipment.PEACE_RING,
                Equipment.EXCELLENT_RING,
                Equipment.DRUMSTICK_RING,
                Equipment.GLUTTON_RING,
                Equipment.ECONOMY_RING,
                Equipment.CHEAP_RING,
                Equipment.HEROIC_RING,
            ], Actor.BOWSER),
            reset_next_if(
                MnLBIS.on_retry() |
                (Memory.SCREEN_ID_ != 0x6be) # not in battle
            ),
            pause_if(MnLBIS.badge_used()).with_hits(1)
        ))

    @achievement()
    def scutlet(self, ach: Achievement):
        ach.add_core(group(
            MnLBIS.is_in_battle(
                battle_id=0x1021,
                bottom_screen_id=0x39
            ),
            MnLBIS.level_cap(6, Actor.MARIO_LUIGI),
            trigger(MnLBIS.on_enemy_dead()),
            MnLBIS.is_challenge_medal_equipped(),
            MnLBIS.check_cheated_equipments(),
            MnLBIS.forbidden_equipment([
                Equipment.DOCTOR_SOCKS,
                Equipment.GUMPTION_SOCKS,
                Equipment.BRO_SOCKS,
                Equipment.NO_TOUCH_SOCKS,
                Equipment.HEAVY_GLOVES,
                Equipment.SPECIAL_GLOVES,
                Equipment.SIPHON_GLOVES,
                Equipment.DELICIOUS_GLOVES,
                Equipment.HEAVY_BOOTS,
                Equipment.SPECIAL_BOOTS,
                Equipment.SHELL_BOOTS,
                Equipment.SHROOB_BOOTS,
                Equipment.SIPHON_BOOTS,
                Equipment.DAREDEVIL_BOOTS,
                Equipment.TIP_TOP_BOOTS,
                Equipment.LUCK_CHARM,
                Equipment.HAPPY_CHARM,
                Equipment.TIGHT_BELT,
                Equipment.BUDGET_CHARM,
                Equipment.ADVICE_PATCH,
                Equipment.HEROIC_PATCH,
                Equipment.LUXURY_PATCH,
                Equipment.BIG_SHELL,
                Equipment.SMALL_SHELL,
                Equipment.GIANT_SHELL,
                Equipment.KO_SHELL,
                Equipment.VENGEANCE_CAPE,
            ], Actor.MARIO_LUIGI),
            reset_next_if(
                MnLBIS.on_retry() |
                (Memory.SCREEN_ID_ != 0x6be) # not in battle
            ),
            pause_if(MnLBIS.badge_used()).with_hits(1)
        ))

    @achievement()
    def broggy(self, ach: Achievement):
        ach.add_core(group(
            MnLBIS.is_in_battle(
                battle_id=0x1017,
                top_screen_id=0x35,
            ),
            MnLBIS.level_cap(7, Actor.BOWSER),
            trigger(MnLBIS.on_enemy_dead()),
            MnLBIS.is_challenge_medal_equipped(),
            MnLBIS.check_cheated_equipments(),
            MnLBIS.forbidden_equipment([
                Equipment.IRON_FIST_BAND,
                Equipment.STAMINA_BAND,
                Equipment.LUCKY_BAND,
                Equipment.FURY_BAND,
                Equipment.VAMPIRE_BAND,
                Equipment.INTRUDER_FANGS,
                Equipment.BURNING_FANGS,
                Equipment.FURY_FANGS,
                Equipment.RESTORE_RING,
                Equipment.PEACE_RING,
                Equipment.EXCELLENT_RING,
                Equipment.DRUMSTICK_RING,
                Equipment.GLUTTON_RING,
                Equipment.ECONOMY_RING,
                Equipment.CHEAP_RING,
                Equipment.HEROIC_RING,
            ], Actor.BOWSER)
        ))

    @achievement()
    def wiggler(self, ach: Achievement):
        ach.add_core(group(
            MnLBIS.is_in_battle(
                battle_id=0x102b,
                top_screen_id=0x33,
            ),
            MnLBIS.level_cap(9),
            trigger(MnLBIS.on_enemy_dead()),
            MnLBIS.is_challenge_medal_equipped(),
            MnLBIS.check_cheated_equipments(),
            MnLBIS.forbidden_equipment([
                Equipment.DOCTOR_SOCKS,
                Equipment.GUMPTION_SOCKS,
                Equipment.BRO_SOCKS,
                Equipment.NO_TOUCH_SOCKS,
                Equipment.HEAVY_GLOVES,
                Equipment.SPECIAL_GLOVES,
                Equipment.SIPHON_GLOVES,
                Equipment.DELICIOUS_GLOVES,
                Equipment.HEAVY_BOOTS,
                Equipment.SPECIAL_BOOTS,
                Equipment.SHELL_BOOTS,
                Equipment.SHROOB_BOOTS,
                Equipment.SIPHON_BOOTS,
                Equipment.DAREDEVIL_BOOTS,
                Equipment.TIP_TOP_BOOTS,
                Equipment.LUCK_CHARM,
                Equipment.HAPPY_CHARM,
                Equipment.TIGHT_BELT,
                Equipment.BUDGET_CHARM,
                Equipment.ADVICE_PATCH,
                Equipment.HEROIC_PATCH,
                Equipment.LUXURY_PATCH,
                Equipment.BIG_SHELL,
                Equipment.SMALL_SHELL,
                Equipment.GIANT_SHELL,
                Equipment.KO_SHELL,
                Equipment.VENGEANCE_CAPE,
            ], Actor.MARIO_LUIGI),
            MnLBIS.forbidden_equipment([
                Equipment.IRON_FIST_BAND,
                Equipment.STAMINA_BAND,
                Equipment.LUCKY_BAND,
                Equipment.FURY_BAND,
                Equipment.VAMPIRE_BAND,
                Equipment.INTRUDER_FANGS,
                Equipment.BURNING_FANGS,
                Equipment.FURY_FANGS,
                Equipment.RESTORE_RING,
                Equipment.PEACE_RING,
                Equipment.EXCELLENT_RING,
                Equipment.DRUMSTICK_RING,
                Equipment.GLUTTON_RING,
                Equipment.ECONOMY_RING,
                Equipment.CHEAP_RING,
                Equipment.HEROIC_RING,
            ], Actor.BOWSER),
            reset_next_if(
                MnLBIS.on_retry() |
                (Memory.SCREEN_ID_ != 0x6be) # not in battle
            ),
            pause_if(MnLBIS.badge_used()).with_hits(1)
        ))

    @achievement()
    def durmite(self, ach: Achievement):
        ach.add_core(group(
            MnLBIS.is_in_battle(
                battle_id=0x1030,
                bottom_screen_id=0x3a,
            ),
            MnLBIS.level_cap(8, Actor.MARIO_LUIGI),
            trigger(MnLBIS.on_enemy_dead()),
            MnLBIS.is_challenge_medal_equipped(),
            MnLBIS.check_cheated_equipments(),
            MnLBIS.forbidden_equipment([
                Equipment.DOCTOR_SOCKS,
                Equipment.GUMPTION_SOCKS,
                Equipment.BRO_SOCKS,
                Equipment.NO_TOUCH_SOCKS,
                Equipment.HEAVY_GLOVES,
                Equipment.SPECIAL_GLOVES,
                Equipment.SIPHON_GLOVES,
                Equipment.DELICIOUS_GLOVES,
                Equipment.HEAVY_BOOTS,
                Equipment.SPECIAL_BOOTS,
                Equipment.SHELL_BOOTS,
                Equipment.SHROOB_BOOTS,
                Equipment.SIPHON_BOOTS,
                Equipment.DAREDEVIL_BOOTS,
                Equipment.TIP_TOP_BOOTS,
                Equipment.LUCK_CHARM,
                Equipment.HAPPY_CHARM,
                Equipment.TIGHT_BELT,
                Equipment.BUDGET_CHARM,
                Equipment.ADVICE_PATCH,
                Equipment.HEROIC_PATCH,
                Equipment.LUXURY_PATCH,
                Equipment.BIG_SHELL,
                Equipment.SMALL_SHELL,
                Equipment.GIANT_SHELL,
                Equipment.KO_SHELL,
                Equipment.VENGEANCE_CAPE,
            ], Actor.MARIO_LUIGI),
            reset_next_if(
                MnLBIS.on_retry() |
                (Memory.SCREEN_ID_ != 0x6be) # not in battle
            ),
            pause_if(MnLBIS.badge_used()).with_hits(1)
        ))

    @achievement()
    def midbus(self, ach: Achievement):
        ach.add_core(group(
            MnLBIS.is_in_battle(
                battle_id=0x106a,
                top_screen_id=0x2d,
            ),
            MnLBIS.level_cap(15, Actor.BOWSER),
            trigger(MnLBIS.on_enemy_dead()),
            MnLBIS.is_challenge_medal_equipped(),
            MnLBIS.check_cheated_equipments(),
            MnLBIS.forbidden_equipment([
                Equipment.STAMINA_BAND,
                Equipment.FURY_BAND,
                Equipment.VAMPIRE_BAND,
                Equipment.INTRUDER_FANGS,
                Equipment.FURY_FANGS,
                Equipment.RESTORE_RING,
                Equipment.PEACE_RING,
                Equipment.EXCELLENT_RING,
                Equipment.DRUMSTICK_RING,
                Equipment.GLUTTON_RING,
                Equipment.ECONOMY_RING,
                Equipment.CHEAP_RING,
                Equipment.HEROIC_RING,
            ], Actor.BOWSER)
        ))

    @achievement()
    def alpha_keratin(self, ach: Achievement):
        ach.add_core(group(
            MnLBIS.is_in_battle(
                battle_id=0x1040,
                bottom_screen_id=0x4f,
            ),
            MnLBIS.level_cap(12, Actor.MARIO_LUIGI),
            trigger(Memory.BOSS_STATE__7 == 1),
            trigger(MnLBIS.on_enemy_dead()),
            MnLBIS.is_challenge_medal_equipped(),
            MnLBIS.check_cheated_equipments(),
            MnLBIS.forbidden_equipment([
                Equipment.DOCTOR_SOCKS,
                Equipment.GUMPTION_SOCKS,
                Equipment.BRO_SOCKS,
                Equipment.NO_TOUCH_SOCKS,
                Equipment.HEAVY_GLOVES,
                Equipment.SPECIAL_GLOVES,
                Equipment.SIPHON_GLOVES,
                Equipment.DELICIOUS_GLOVES,
                Equipment.HEAVY_BOOTS,
                Equipment.SPECIAL_BOOTS,
                Equipment.SHELL_BOOTS,
                Equipment.SHROOB_BOOTS,
                Equipment.SIPHON_BOOTS,
                Equipment.TIP_TOP_BOOTS,
                Equipment.LUCK_CHARM,
                Equipment.HAPPY_CHARM,
                Equipment.TIGHT_BELT,
                Equipment.BUDGET_CHARM,
                Equipment.ADVICE_PATCH,
                Equipment.HEROIC_PATCH,
                Equipment.LUXURY_PATCH,
                Equipment.BIG_SHELL,
                Equipment.SMALL_SHELL,
                Equipment.GIANT_SHELL,
                Equipment.KO_SHELL,
                Equipment.VENGEANCE_CAPE,
            ], Actor.MARIO_LUIGI),
            reset_next_if(
                MnLBIS.on_retry() |
                (Memory.SCREEN_ID_ != 0x6be) # not in battle
            ),
            pause_if(MnLBIS.badge_used()).with_hits(1)
        ))

    @achievement()
    def bowser(self, ach: Achievement):
        ach.add_core(group(
            MnLBIS.is_in_battle(
                battle_id=0x1050,
                top_screen_id=0x100,
            ),
            MnLBIS.level_cap(16, Actor.MARIO_LUIGI),
            trigger(MnLBIS.on_enemy_dead()),
            MnLBIS.is_challenge_medal_equipped(),
            MnLBIS.check_cheated_equipments(),
            MnLBIS.forbidden_equipment([
                Equipment.DOCTOR_SOCKS,
                Equipment.GUMPTION_SOCKS,
                Equipment.NO_TOUCH_SOCKS,
                Equipment.HEAVY_GLOVES,
                Equipment.SPECIAL_GLOVES,
                Equipment.SIPHON_GLOVES,
                Equipment.DELICIOUS_GLOVES,
                Equipment.HEAVY_BOOTS,
                Equipment.SPECIAL_BOOTS,
                Equipment.SHELL_BOOTS,
                Equipment.SHROOB_BOOTS,
                Equipment.SIPHON_BOOTS,
                Equipment.TIP_TOP_BOOTS,
                Equipment.LUCK_CHARM,
                Equipment.TIGHT_BELT,
                Equipment.ADVICE_PATCH,
                Equipment.HEROIC_PATCH,
                Equipment.LUXURY_PATCH,
                Equipment.BIG_SHELL,
                Equipment.GIANT_SHELL,
                Equipment.VENGEANCE_CAPE,
            ], Actor.MARIO_LUIGI),
            reset_next_if(
                MnLBIS.on_retry() |
                (Memory.SCREEN_ID_ != 0x6be) # not in battle
            ),
            pause_if(MnLBIS.badge_used()).with_hits(1)
        ))

    @achievement()
    def wisdurm(self, ach: Achievement):
        ach.add_core(group(
            MnLBIS.is_in_battle(
                battle_id=0x1060,
                bottom_screen_id=0x110,
            ),
            MnLBIS.level_cap(20, Actor.MARIO_LUIGI),
            trigger(MnLBIS.on_enemy_dead()),
            MnLBIS.is_challenge_medal_equipped(),
            MnLBIS.check_cheated_equipments(),
            MnLBIS.forbidden_equipment([
                Equipment.DOCTOR_SOCKS,
                Equipment.SPECIAL_GLOVES,
                Equipment.SIPHON_GLOVES,
                Equipment.SHROOB_BOOTS,
                Equipment.LUCK_CHARM,
                Equipment.TIGHT_BELT,
            ], Actor.MARIO_LUIGI),
            reset_next_if(
                MnLBIS.on_retry() |
                (Memory.SCREEN_ID_ != 0x6be) # not in battle
            ),
            pause_if(MnLBIS.badge_used()).with_hits(1)
        ))

    @achievement()
    def memories(self, ach: Achievement):
        ach.add_core(group(
            MnLBIS.is_in_battle(
                battle_id=0x106b,
                bottom_screen_id=0x14b,
            ),
            MnLBIS.level_cap(21, Actor.MARIO_LUIGI),
            trigger(MnLBIS.on_enemy_dead([1, 2])),
            MnLBIS.is_challenge_medal_equipped(),
            MnLBIS.check_cheated_equipments(),
            MnLBIS.forbidden_equipment([
                Equipment.DOCTOR_SOCKS,
                Equipment.SPECIAL_GLOVES,
                Equipment.SIPHON_GLOVES,
                Equipment.SHROOB_BOOTS,
                Equipment.LUCK_CHARM,
                Equipment.TIGHT_BELT,
            ], Actor.MARIO_LUIGI),
            reset_next_if(
                MnLBIS.on_retry() |
                (Memory.SCREEN_ID_ != 0x6be) # not in battle
            ),
            pause_if(MnLBIS.badge_used()).with_hits(1)
        ))

    @achievement()
    def shroobs(self, ach: Achievement):
        ach.add_core(group(
            MnLBIS.is_in_battle(
                battle_id=0x1069,
                top_screen_id=0x28f,
            ),
            MnLBIS.level_cap(25, Actor.MARIO_LUIGI),
            trigger(MnLBIS.on_enemy_dead([1, 2, 3])),
            MnLBIS.is_challenge_medal_equipped(),
            MnLBIS.check_cheated_equipments(),
            MnLBIS.forbidden_equipment([
                Equipment.SHROOB_BOOTS,
                Equipment.SIPHON_GLOVES,
            ], Actor.MARIO_LUIGI),
            reset_next_if(
                MnLBIS.on_retry() |
                (Memory.SCREEN_ID_ != 0x6be) # not in battle
            ),
            pause_if(MnLBIS.badge_used()).with_hits(1)
        ))

    @achievement()
    def junker(self, ach: Achievement):
        ach.add_core(group(
            MnLBIS.is_in_battle(
                battle_id=0x1073,
                top_screen_id=0x1a7,
            ),
            MnLBIS.level_cap(26, Actor.MARIO_LUIGI),
            trigger(MnLBIS.on_enemy_dead()),
            MnLBIS.is_challenge_medal_equipped(),
            MnLBIS.check_cheated_equipments(),
            MnLBIS.forbidden_equipment([
                Equipment.DOCTOR_SOCKS,
                Equipment.SPECIAL_GLOVES,
                Equipment.LUCK_CHARM,
            ], Actor.MARIO_LUIGI),
            reset_next_if(
                MnLBIS.on_retry() |
                (Memory.SCREEN_ID_ != 0x6be) # not in battle
            ),
            pause_if(MnLBIS.badge_used()).with_hits(1)
        ))

    @achievement()
    def blizzard_midbus(self, ach: Achievement):
        ach.add_core(group(
            MnLBIS.is_in_battle(
                battle_id=0x107b,
                top_screen_id=0x20e,
            ),
            MnLBIS.level_cap(28),
            trigger(MnLBIS.on_enemy_dead()),
            MnLBIS.is_challenge_medal_equipped(),
            MnLBIS.check_cheated_equipments(),
            MnLBIS.forbidden_equipment([
                Equipment.DOCTOR_SOCKS,
                Equipment.LUCK_CHARM,
            ], Actor.MARIO_LUIGI),
            MnLBIS.forbidden_equipment([
                Equipment.INTRUDER_FANGS,
            ], Actor.BOWSER),
            reset_next_if(
                MnLBIS.on_retry() |
                (Memory.SCREEN_ID_ != 0x6be) # not in battle
            ),
            pause_if(MnLBIS.badge_used()).with_hits(1)
        ))

    @achievement()
    def dark_star(self, ach: Achievement):
        ach.add_core(group(
            MnLBIS.is_in_battle(
                battle_id=0x1089,
                bottom_screen_id=0x1f9,
            ),
            MnLBIS.level_cap(30, Actor.MARIO_LUIGI),
            trigger(MnLBIS.on_enemy_dead()),
            MnLBIS.is_challenge_medal_equipped(),
            MnLBIS.check_cheated_equipments(),
            MnLBIS.forbidden_equipment([
                Equipment.DOCTOR_SOCKS,
                Equipment.LUCK_CHARM,
            ], Actor.MARIO_LUIGI),
            reset_next_if(
                MnLBIS.on_retry() |
                (Memory.SCREEN_ID_ != 0x6be) # not in battle
            ),
            pause_if(MnLBIS.badge_used()).with_hits(1)
        ))

    @achievement()
    def dark_fawful(self, ach: Achievement):
        ach.add_core(group(
            MnLBIS.is_in_battle(
                battle_id=0x1080,
                top_screen_id=0x241,
            ),
            MnLBIS.level_cap(33),
            trigger(MnLBIS.on_enemy_dead()),
            MnLBIS.is_challenge_medal_equipped(),
            MnLBIS.check_cheated_equipments(),
            MnLBIS.forbidden_equipment([
                Equipment.LUCK_CHARM,
            ], Actor.MARIO_LUIGI),
            MnLBIS.forbidden_equipment([
                Equipment.INTRUDER_FANGS,
            ], Actor.BOWSER),
            reset_next_if(
                MnLBIS.on_retry() |
                (Memory.SCREEN_ID_ != 0x6be) # not in battle
            ),
            pause_if(MnLBIS.badge_used()).with_hits(1)
        ))

    @achievement()
    def final_boss(self, ach: Achievement):
        ach.add_core(group(
            MnLBIS.is_in_battle(
                battle_id=0x1079,
                top_screen_id=0x22c,
            ),
            MnLBIS.level_cap(35),
            trigger(MnLBIS.on_enemy_dead([1, 2, 3])),
            MnLBIS.is_challenge_medal_equipped(),
            MnLBIS.check_cheated_equipments(),
            reset_next_if(
                MnLBIS.on_retry() |
                (Memory.SCREEN_ID_ != 0x6be) # not in battle
            ),
            pause_if(MnLBIS.badge_used()).with_hits(1)
        ))

    @achievement()
    def class_1(self, ach: Achievement):
        ach.add_core(group(
            (
                MnLBIS.on_gauntlet_enter(1)
            ).with_hits(1),
            MnLBIS.level_cap(18, Actor.MARIO_LUIGI),
            trigger(MnLBIS.on_gauntlet_completed(1)),
            MnLBIS.is_challenge_medal_equipped(),
            MnLBIS.check_cheated_equipments(),
            MnLBIS.forbidden_equipment([
                Equipment.GUMPTION_SOCKS,
                Equipment.TIGHT_BELT,
            ], Actor.MARIO_LUIGI),
            reset_if(
                (Memory.SCREEN_ID_ != 0x20b2) &
                (Memory.SCREEN_ID_ != 0x06be)
            ),
            reset_if((Memory.MARIOS_HP + Memory.LUIGIS_HP) == 0),
            reset_if(byte(Memory.GAUNTLET__8) == 0x64)
        ))

    @achievement()
    def class_2(self, ach: Achievement):
        ach.add_core(group(
            (
                MnLBIS.on_gauntlet_enter(2)
            ).with_hits(1),
            MnLBIS.level_cap(21, Actor.MARIO_LUIGI),
            trigger(MnLBIS.on_gauntlet_completed(2)),
            MnLBIS.is_challenge_medal_equipped(),
            MnLBIS.check_cheated_equipments(),
            MnLBIS.forbidden_equipment([
                Equipment.GUMPTION_SOCKS,
                Equipment.TIGHT_BELT,
            ], Actor.MARIO_LUIGI),
            reset_if(
                (Memory.SCREEN_ID_ != 0x20b2) &
                (Memory.SCREEN_ID_ != 0x06be)
            ),
            reset_if((Memory.MARIOS_HP + Memory.LUIGIS_HP) == 0),
            reset_if(byte(Memory.GAUNTLET__8) == 0x64)
        ))

    @achievement()
    def class_3(self, ach: Achievement):
        ach.add_core(group(
            (
                MnLBIS.on_gauntlet_enter(3)
            ).with_hits(1),
            MnLBIS.level_cap(26, Actor.MARIO_LUIGI),
            trigger(MnLBIS.on_gauntlet_completed(3)),
            MnLBIS.is_challenge_medal_equipped(),
            MnLBIS.check_cheated_equipments(),
            reset_if(
                (Memory.SCREEN_ID_ != 0x20b2) &
                (Memory.SCREEN_ID_ != 0x06be)
            ),
            reset_if((Memory.MARIOS_HP + Memory.LUIGIS_HP) == 0),
            reset_if(byte(Memory.GAUNTLET__8) == 0x64)
        ))

    @achievement()
    def class_4(self, ach: Achievement):
        ach.add_core(group(
            (
                MnLBIS.on_gauntlet_enter(4)
            ).with_hits(1),
            MnLBIS.level_cap(29, Actor.MARIO_LUIGI),
            trigger(MnLBIS.on_gauntlet_completed(4)),
            MnLBIS.is_challenge_medal_equipped(),
            MnLBIS.check_cheated_equipments(),
            reset_if(
                (Memory.SCREEN_ID_ != 0x20b2) &
                (Memory.SCREEN_ID_ != 0x06be)
            ),
            reset_if((Memory.MARIOS_HP + Memory.LUIGIS_HP) == 0),
            reset_if(byte(Memory.GAUNTLET__8) == 0x64)
        ))

    @achievement()
    def class_5(self, ach: Achievement):
        ach.add_core(group(
            (
                MnLBIS.on_gauntlet_enter(5)
            ).with_hits(1),
            MnLBIS.level_cap(34, Actor.MARIO_LUIGI),
            trigger(MnLBIS.on_gauntlet_completed(5)),
            MnLBIS.is_challenge_medal_equipped(),
            MnLBIS.check_cheated_equipments(),
            reset_if(
                (Memory.SCREEN_ID_ != 0x20b2) &
                (Memory.SCREEN_ID_ != 0x06be)
            ),
            reset_if((Memory.MARIOS_HP + Memory.LUIGIS_HP) == 0),
            reset_if(byte(Memory.GAUNTLET__8) == 0x64)
        ))

    @achievement()
    def class_6(self, ach: Achievement):
        ach.add_core(group(
            (
                MnLBIS.on_gauntlet_enter(6)
            ).with_hits(1),
            MnLBIS.level_cap(40, Actor.MARIO_LUIGI),
            trigger(MnLBIS.on_gauntlet_completed(6)),
            MnLBIS.is_challenge_medal_equipped(),
            MnLBIS.check_cheated_equipments(),
            reset_if(
                (Memory.SCREEN_ID_ != 0x20b2) &
                (Memory.SCREEN_ID_ != 0x06be)
            ),
            reset_if((Memory.MARIOS_HP + Memory.LUIGIS_HP) == 0),
            reset_if(byte(Memory.GAUNTLET__8) == 0x64)
        ))

    @achievement()
    def class_7(self, ach: Achievement):
        ach.add_core(group(
            (
                MnLBIS.on_gauntlet_enter(7)
            ).with_hits(1),
            MnLBIS.level_cap(50, Actor.MARIO_LUIGI),
            trigger(MnLBIS.on_gauntlet_completed(7)),
            MnLBIS.is_challenge_medal_equipped(),
            MnLBIS.check_cheated_equipments(),
            reset_if(
                (Memory.SCREEN_ID_ != 0x20b2) &
                (Memory.SCREEN_ID_ != 0x06be)
            ),
            reset_if((Memory.MARIOS_HP + Memory.LUIGIS_HP) == 0),
            reset_if(byte(Memory.GAUNTLET__8) == 0x64)
        ))

if __name__=="__main__":
    MnLBIS.init()
    MnLBISSubset().save("output/")
