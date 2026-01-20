from pycheevos.models.set import AchievementSet, Leaderboard
from pycheevos.models.achievement import Achievement
from pycheevos.core.helpers import *
from pycheevos.core.constants import *

from logic import EntityData, LevelInfo, MagicianLevel, Rayman, World, delta_check, delta_sources
from memory import Memory
from framework import achievement, achievement_set

import assets
import csv

@achievement_set(
    assets=assets,
    author="Wormi"
)
class RaymanSet(AchievementSet):
    def __init__(self):
        super().__init__(
            game_id=20900,
            title="Rayman (Saturn)"
        )
        self.leaderboard_pink_plant_woods(assets.leaderboards[152558])
        self.add_leaderboard(assets.leaderboards[152558])

    ##########################
    # Progression: Abilities #
    ##########################

    @achievement(574636)
    def betilla_punch(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            Rayman.is_in_level(1, 3) &
            delta_check(bit7(Memory.RAYMAN_ABILITIES.address), 0, 1)
        )

    @achievement(574637)
    def betilla_hang(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            Rayman.is_in_level(1, 8) &
            delta_check(bit6(Memory.RAYMAN_ABILITIES.address), 0, 1)
        )
    
    @achievement(574638)
    def betilla_rings(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            Rayman.is_in_level(1, 17) &
            delta_check(bit0(Memory.RAYMAN_ABILITIES.address), 0, 1)
        )

    @achievement(574639)
    def betilla_helicopter(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            Rayman.is_in_level(2, 11) &
            delta_check(bit5(Memory.RAYMAN_ABILITIES.address), 0, 1)
        )

    @achievement(574640)
    def betilla_run(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            Rayman.is_in_level(3, 11) &
            delta_check(bit7(Memory.RAYMAN_MODIFIERS.address), 0, 1)
        )

    #######################
    # Progression: Bosses #
    #######################

    @achievement(574641)
    def boss_bzzit(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            delta_check(bit7(Memory.EVENTS_BOSSES_BEATEN.address), 0, 1)
        )

    @achievement(574642)
    def boss_moskito(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            delta_check(bit6(Memory.EVENTS_BOSSES_BEATEN.address), 0, 1)
        )

    @achievement(574643)
    def boss_mr_sax(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            delta_check(bit5(Memory.EVENTS_BOSSES_BEATEN.address), 0, 1)
        )

    @achievement(574644)
    def boss_mr_stone(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            delta_check(bit4(Memory.EVENTS_BOSSES_BEATEN.address), 0, 1)
        )

    @achievement(574645)
    def boss_pirate_mama(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            delta_check(bit3(Memory.EVENTS_BOSSES_BEATEN.address), 0, 1)
        )

    @achievement(574646)
    def boss_space_mama(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            delta_check(bit2(Memory.EVENTS_BOSSES_BEATEN.address), 0, 1)
        )

    @achievement(574647)
    def boss_mr_skops(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            delta_check(bit1(Memory.EVENTS_BOSSES_BEATEN.address), 0, 1)
        )

    @achievement(574648)
    def boss_mr_dark(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            delta_check(bit0(Memory.EVENTS_BOSSES_BEATEN.address), 0, 1)
        )

    ######################
    # Progression: Cages #
    ######################

    @achievement(573015)
    def cages_pink_plant_woods(self, ach: Achievement):
        ach.add_core(LevelInfo(0).on_cages_unlocked())

    @achievement(573016)
    def cages_anguish_lagoon(self, ach: Achievement):
        ach.add_core(LevelInfo(1).on_cages_unlocked())

    @achievement(573017)
    def cages_swamps_of_forgetfulness(self, ach: Achievement):
        ach.add_core(LevelInfo(2).on_cages_unlocked())

    @achievement(573018)
    def cages_moskitos_nest(self, ach: Achievement):
        ach.add_core(LevelInfo(3).on_cages_unlocked())

    @achievement(573019)
    def cages_bongo_hills(self, ach: Achievement):
        ach.add_core(LevelInfo(4).on_cages_unlocked())

    @achievement(573020)
    def cages_allegro_presto(self, ach: Achievement):
        ach.add_core(LevelInfo(5).on_cages_unlocked())

    @achievement(573021)
    def cages_gong_heights(self, ach: Achievement):
        ach.add_core(LevelInfo(6).on_cages_unlocked())

    @achievement(573022)
    def cages_mr_sax_hullaballo(self, ach: Achievement):
        ach.add_core(LevelInfo(7).on_cages_unlocked())

    @achievement(573023)
    def cages_twilight_gulch(self, ach: Achievement):
        ach.add_core(LevelInfo(8).on_cages_unlocked())

    @achievement(573024)
    def cages_hard_rocks(self, ach: Achievement):
        ach.add_core(LevelInfo(9).on_cages_unlocked())

    @achievement(573025)
    def cages_mr_stone_peaks(self, ach: Achievement):
        ach.add_core(LevelInfo(10).on_cages_unlocked())

    @achievement(573026)
    def cages_eraser_plains(self, ach: Achievement):
        ach.add_core(LevelInfo(11).on_cages_unlocked())

    @achievement(573027)
    def cages_pencil_pentathlon(self, ach: Achievement):
        ach.add_core(LevelInfo(12).on_cages_unlocked())

    @achievement(573028)
    def cages_space_mama_crater(self, ach: Achievement):
        ach.add_core(LevelInfo(13).on_cages_unlocked())

    @achievement(573029)
    def cages_crystal_palace(self, ach: Achievement):
        ach.add_core(LevelInfo(14).on_cages_unlocked())

    @achievement(573030)
    def cages_eat_at_joes(self, ach: Achievement):
        ach.add_core(LevelInfo(15).on_cages_unlocked())

    @achievement(573031)
    def cages_mr_skops_stalactites(self, ach: Achievement):
        ach.add_core(LevelInfo(16).on_cages_unlocked())

    @achievement(574661)
    def all_cages(self, ach: Achievement):
        sources = [
            LevelInfo(id).cages
            for id in range(17)
        ]
        ach.add_core(
            Rayman.is_ingame() &
            delta_sources(sources, 101, 102)
        )

    ##########################
    # Bonus: Magician levels #
    ##########################

    @achievement(574649)
    def magician_pink_plant_woods_1(self, ach: Achievement):
        ach.add_core(MagicianLevel(0).on_win())

    @achievement(574650)
    def magician_pink_plant_woods_2(self, ach: Achievement):
        ach.add_core(MagicianLevel(1).on_win())

    @achievement(574651)
    def magician_swamps_of_forgetfulness(self, ach: Achievement):
        ach.add_core(MagicianLevel(2).on_win())

    @achievement(574652)
    def magician_moskitos_next(self, ach: Achievement):
        ach.add_core(MagicianLevel(3).on_win())

    @achievement(574653)
    def magician_bongo_hills(self, ach: Achievement):
        ach.add_core(MagicianLevel(4).on_win())

    @achievement(574654)
    def magician_allegro_presto(self, ach: Achievement):
        ach.add_core(MagicianLevel(5).on_win())

    @achievement(574655)
    def magician_hard_rocks(self, ach: Achievement):
        ach.add_core(MagicianLevel(6).on_win())

    @achievement(574656)
    def magician_mr_stone_peaks(self, ach: Achievement):
        ach.add_core(MagicianLevel(7).on_win())

    @achievement(574657)
    def magician_eraser_plains(self, ach: Achievement):
        ach.add_core(MagicianLevel(8).on_win())

    @achievement(574658)
    def magician_space_mama_crater(self, ach: Achievement):
        ach.add_core(MagicianLevel(9).on_win())

    @achievement(574659)
    def magician_crystal_palace(self, ach: Achievement):
        ach.add_core(MagicianLevel(10).on_win())

    ################################
    # Challenges: Individual Level #
    ################################

    @achievement(573034)
    def challenge_pink_plant_woods(self, ach: Achievement):
        sources = [
            bit7(Memory.COLLECTIBLE_PINK_PLANT_WOODS_1.address),
            bit7(Memory.COLLECTIBLE_PINK_PLANT_WOODS_2.address),
            bit6(Memory.COLLECTIBLE_PINK_PLANT_WOODS_2.address),
            bit7(Memory.COLLECTIBLE_PINK_PLANT_WOODS_4_1.address),
            bit6(Memory.COLLECTIBLE_PINK_PLANT_WOODS_4_1.address),
            bit4(Memory.COLLECTIBLE_PINK_PLANT_WOODS_4_1.address),
            bit5(Memory.COLLECTIBLE_PINK_PLANT_WOODS_4_2.address),
            bit2(Memory.COLLECTIBLE_PINK_PLANT_WOODS_4_2.address),
        ]
        ach.add_core(
            reset_if(
                (delta(Memory.STATE_INGAME) == 0) &
                (Memory.STATE_INGAME == 1) &
                (Rayman.is_in_level(1, [1, 2, 4]))
            )
        ).add_alt([
            pause_if(~(Rayman.is_ingame())).with_hits(1),
            measured(delta_sources(sources, 7, 8))
        ])

    #################
    # Miscellaneous #
    #################

    @achievement(573033)
    def livingstone_grimace(self, ach: Achievement):
        ach.add_core([
            reset_if(
                (delta(Memory.STATE_INGAME) == 0) &
                (Memory.STATE_INGAME == 1)
            ),
            reset_if(delta(Rayman.current_map()) != Rayman.current_map()),
            Rayman.is_ingame(),
            Rayman.current_world() == World.JUNGLE
        ])
        with open('data/livingstones.csv', newline='') as csvfile:
            for row in csv.DictReader(csvfile):
                entity = EntityData(int(row['Entity ID']), world_id=World.JUNGLE)
                map_id = int(row['Map ID'])
                ach.add_alt([
                    pause_if(Rayman.current_map() != map_id).with_hits(1),
                    entity.on_animation_change((0x0, 0x2), (0x1, 0xb))
                ])

    @achievement(573499)
    def tentacle_flower(self, ach: Achievement):
        entity = EntityData(122, world_id=World.JUNGLE)
        ach.add_core(
            Rayman.is_ingame() &
            (Rayman.is_in_level(World.JUNGLE, 12)) &
            entity.on_animation_change((0x0, 0x15), (0x0, 0x3))
        )

    @achievement(573032)
    def extra_life(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            (Rayman.tings() < delta(Rayman.tings())) &
            (delta(Memory.LIFE_COUNTER_SCREEN_ANIMATION) == 0xffff) &
            (Memory.LIFE_COUNTER_SCREEN_ANIMATION != 0xffff)
        )

    def leaderboard_pink_plant_woods(self, lb: Leaderboard):
        lb.set_start(
            (Memory.STATE_DEMO_PLAY == 0) &
            (Rayman.is_in_level(World.JUNGLE, 1)) &
            delta_check(Memory.STATE_INGAME, 0, 1) 
        )
        lb.set_cancel(
            (Memory.STATE_INGAME != 1) |
            Rayman.has_cheated()
        )
        lb.set_value(
            Rayman.is_in_level(World.JUNGLE, [1, 2, 4]) &
            measured(Memory.INGAME_MAP_TIMER_LOW != delta(Memory.INGAME_MAP_TIMER_LOW))
        )
        lb.set_submit(
            (Rayman.current_map() == 0x4) &
            delta_check(Memory.STATE_LEVEL_CLEAR, 0x0, 0x2)
        )

if __name__=="__main__":
    RaymanSet().save("output/")
