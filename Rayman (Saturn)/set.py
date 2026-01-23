from pycheevos.models.set import AchievementSet, Leaderboard
from pycheevos.models.achievement import Achievement
from pycheevos.core.helpers import *
from pycheevos.core.constants import *

from logic import Bosses, EntityData, LevelInfo, Levels, MagicianLevel, Rayman, World, delta_check, delta_sources
from memory import Memory
from framework import achievement, achievement_set, leaderboard

import assets
import csv

FRAMERATE = 60

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
            delta_check(Bosses.BZZIT, 0, 1)
        )

    @achievement(574642)
    def boss_moskito(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            delta_check(Bosses.MOSKITO, 0, 1)
        )

    @achievement(574643)
    def boss_mr_sax(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            delta_check(Bosses.MR_SAX, 0, 1)
        )

    @achievement(574644)
    def boss_mr_stone(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            delta_check(Bosses.MR_STONE, 0, 1)
        )

    @achievement(574645)
    def boss_pirate_mama(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            delta_check(Bosses.PIRATE_MAMA, 0, 1)
        )

    @achievement(574646)
    def boss_space_mama(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            delta_check(Bosses.SPACE_MAMA, 0, 1)
        )

    @achievement(574647)
    def boss_mr_skops(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            delta_check(Bosses.MR_SKOPS, 0, 1)
        )

    @achievement(574648)
    def boss_mr_dark(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            delta_check(Bosses.MR_DARK, 0, 1)
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
    def cages_mr_sax_hullaballoo(self, ach: Achievement):
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

    @achievement(1000001)
    def challenge_allegro_presto(self, ach: Achievement):
        ach.add_core([
            (Memory.STATE_DEMO_PLAY == 0) &
            (Rayman.is_in_level(World.BAND_LAND, 7)) &
            (bit5(Memory.EVENTS_BOSSES_BEATEN.address) == 0) &
            (bit7(Memory.RAYMAN_MODIFIERS.address) == 0) &
            delta_check(Memory.STATE_INGAME, 0, 1).with_hits(1),
            trigger(Rayman.current_map() == 10),
            trigger(delta_check(Memory.INGAME_LEVEL_CLEAR, 0x0, 0x2)),
            Rayman.is_in_level(World.BAND_LAND, [7, 8, 9, 10]) &
            reset_if(Memory.INGAME_FRAME_COUNTER != delta(Memory.INGAME_FRAME_COUNTER)).with_hits((4*60+30*60) * FRAMERATE),
            reset_if(Memory.STATE_INGAME == 0),
            reset_if(Rayman.has_cheated())
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
            Rayman.current_world() == World.DREAM_FOREST
        ])
        with open('data/livingstones.csv', newline='') as csvfile:
            for row in csv.DictReader(csvfile):
                entity = EntityData(int(row['Entity ID']), world_id=World.DREAM_FOREST)
                map_id = int(row['Map ID'])
                ach.add_alt([
                    pause_if(Rayman.current_map() != map_id).with_hits(1),
                    entity.on_animation_change((0x0, 0x2), (0x1, 0xb))
                ])

    @achievement(573499)
    def tentacle_flower(self, ach: Achievement):
        entity = EntityData(122, world_id=World.DREAM_FOREST)
        ach.add_core(
            Rayman.is_ingame() &
            (Rayman.is_in_level(World.DREAM_FOREST, 12)) &
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

    #############################
    # Leaderboards: Time Attack #
    #############################

    @leaderboard(152558)
    def leaderboard_pink_plant_woods(self, lb: Leaderboard):
        Levels.PINK_PLANT_WOODS.generate_leaderboard(lb,
        replayable_only=True, # exclude betilla
    )

    @leaderboard(152776)
    def leaderboard_anguish_lagoon(self, lb: Leaderboard):
        Levels.ANGUISH_LAGOON.generate_leaderboard(lb,
            replayable_only=False,
            exclude_maps=[8], # exclude betilla
            extra_condition=(Bosses.BZZIT == 0),
        )

    @leaderboard(152777)
    def leaderboard_the_swamps_of_forgetfulness(self, lb: Leaderboard):
        Levels.THE_SWAMPS_OF_FORGETFULNESS.generate_leaderboard(lb, replayable_only=True)

    @leaderboard(152778)
    def leaderboard_moskitos_nest(self, lb: Leaderboard):
        Levels.MOSKITOS_NEST.generate_leaderboard(lb,
            replayable_only=False,
            exclude_maps=[17], # exclude betilla
            extra_condition=(Bosses.MOSKITO == 0),
        )

    @leaderboard(152779)
    def leaderboard_bongo_hills(self, lb: Leaderboard):
        Levels.BONGO_HILLS.generate_leaderboard(lb, replayable_only=True)

    @leaderboard(152780)
    def leaderboard_allegro_presto(self, lb: Leaderboard):
        Levels.ALLEGRO_PRESTO.generate_leaderboard(lb,
            replayable_only=False,
            exclude_maps=[11], # exclude betilla
            extra_condition=(Bosses.MR_SAX == 0),
        )

    @leaderboard(152781)
    def leaderboard_gong_heights(self, lb: Leaderboard):
        Levels.BONGO_HILLS.generate_leaderboard(lb, replayable_only=True)

    @leaderboard(152782)
    def leaderboard_mr_saxs_hullaballoo(self, lb: Leaderboard):
        Levels.MR_SAXS_HULLABALLOO.generate_leaderboard(lb,
            replayable_only=False,
            extra_condition=(Bosses.MR_SAX == 0),
        )

    @leaderboard(152783)
    def leaderboard_twilight_gulch(self, lb: Leaderboard):
        Levels.TWILIGHT_GULCH.generate_leaderboard(lb,
            replayable_only=False,
            extra_condition=(Bosses.MR_STONE == 0),
        )

    @leaderboard(152784)
    def leaderboard_the_hard_rocks(self, lb: Leaderboard):
        Levels.THE_HARD_ROCKS.generate_leaderboard(lb, replayable_only=True)

    @leaderboard(152785)
    def leaderboard_mr_stones_peak(self, lb: Leaderboard):
        Levels.MR_STONES_PEAKS.generate_leaderboard(lb,
            replayable_only=False,
            exclude_maps=[11], # exclude betilla
            extra_condition=(Bosses.MR_STONE == 0),
        )

    @leaderboard(152786)
    def leaderboard_eraser_plains(self, lb: Leaderboard):
        Levels.ERASER_PLAINS.generate_leaderboard(lb,
            replayable_only=False,
            extra_condition=(Bosses.PIRATE_MAMA == 0),
        )

    @leaderboard(152787)
    def leaderboard_pencil_pentathlon(self, lb: Leaderboard):
        Levels.PENCIL_PENTATHLON.generate_leaderboard(lb, replayable_only=True)

    @leaderboard(152788)
    def leaderboard_space_mamas_crater(self, lb: Leaderboard):
        Levels.SPACE_MAMAS_CRATER.generate_leaderboard(lb,
            replayable_only=False,
            extra_condition=(Bosses.SPACE_MAMA == 0),
        )

    @leaderboard(152789)
    def leaderboard_crystal_palace(self, lb: Leaderboard):
        Levels.CRYSTAL_PALACE.generate_leaderboard(lb, replayable_only=True)

    @leaderboard(152790)
    def leaderboard_eat_at_joes(self, lb: Leaderboard):
        Levels.EAT_AT_JOES.generate_leaderboard(lb, replayable_only=True)

    @leaderboard(152791)
    def leaderboard_mr_skops_stalactites(self, lb: Leaderboard):
        Levels.MR_SKOPS_STALACTITES.generate_leaderboard(lb,
            replayable_only=False,
            extra_condition=(Bosses.MR_SKOPS == 0),
        )

    @leaderboard(152792)
    def leaderboard_mr_darks_dare(self, lb: Leaderboard):
        Levels.MR_DARKS_DARE.generate_leaderboard(lb,
            replayable_only=False,
            extra_condition=(Bosses.MR_DARK == 0),
        )

    ##########################
    # Leaderboards: Magician #
    ##########################

    @leaderboard(152793)
    def leaderboard_magician_ppw1(self, lb: Leaderboard):
       MagicianLevel(0).generate_leaderboard(lb)

    @leaderboard(152794)
    def leaderboard_magician_ppw2(self, lb: Leaderboard):
       MagicianLevel(1).generate_leaderboard(lb)

    @leaderboard(152795)
    def leaderboard_magician_swamps(self, lb: Leaderboard):
       MagicianLevel(2).generate_leaderboard(lb)

    @leaderboard(152796)
    def leaderboard_magician_moskito(self, lb: Leaderboard):
       MagicianLevel(3).generate_leaderboard(lb)

    @leaderboard(152797)
    def leaderboard_magician_bongo(self, lb: Leaderboard):
       MagicianLevel(4).generate_leaderboard(lb)

    @leaderboard(152798)
    def leaderboard_magician_allegro(self, lb: Leaderboard):
       MagicianLevel(5).generate_leaderboard(lb)

    @leaderboard(152799)
    def leaderboard_magician_hard_rocks(self, lb: Leaderboard):
       MagicianLevel(6).generate_leaderboard(lb)

    @leaderboard(152800)
    def leaderboard_magician_stone_peaks(self, lb: Leaderboard):
       MagicianLevel(7).generate_leaderboard(lb)

    @leaderboard(152801)
    def leaderboard_magician_eraser(self, lb: Leaderboard):
       MagicianLevel(8).generate_leaderboard(lb)

    @leaderboard(152802)
    def leaderboard_magician_space_mama(self, lb: Leaderboard):
       MagicianLevel(9).generate_leaderboard(lb)

    @leaderboard(152803)
    def leaderboard_magician_crystal(self, lb: Leaderboard):
       MagicianLevel(10).generate_leaderboard(lb)

if __name__=="__main__":
    RaymanSet().save("output/")
