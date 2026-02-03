from pycheevos.core.condition import ConditionList
from pycheevos.models.set import AchievementSet, Leaderboard
from pycheevos.models.achievement import Achievement
from pycheevos.core.helpers import *
from pycheevos.core.constants import *

from logic import Bosses, EntityData, Level, LevelInfo, Levels, MagicianLevel, Rayman, World, delta_check, delta_sources
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
            title="Rayman"
        )

    @achievement(578904)
    def warning(self, ach: Achievement):
        ach.add_core(
            (Memory.STATE_TITLE_SCREEN == 1) &
            (delta(Memory.STATE_CURRENT_SAVE_FILE) == 0) &
            (Memory.STATE_CURRENT_SAVE_FILE != 0)
        )

    ##########################
    # Progression: Abilities #
    ##########################

    @achievement(574636)
    def betilla_punch(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            Rayman.is_in_level(World.DREAM_FOREST, 3) &
            delta_check(Rayman.can_punch(), 0, 1)
        )

    @achievement(574637)
    def betilla_hang(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            Rayman.is_in_level(World.DREAM_FOREST, 8) &
            delta_check(Rayman.can_hang(), 0, 1)
        )
    
    @achievement(574638)
    def betilla_rings(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            Rayman.is_in_level(World.DREAM_FOREST, 17) &
            delta_check(Rayman.can_grapple(), 0, 1)
        )

    @achievement(574639)
    def betilla_helicopter(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            Rayman.is_in_level(World.BAND_LAND, 11) &
            delta_check(Rayman.can_helicopter(), 0, 1)
        )

    @achievement(574640)
    def betilla_run(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            Rayman.is_in_level(World.BLUE_MOUNTAINS, 11) &
            delta_check(Rayman.can_run(), 0, 1)
        )

    #######################
    # Progression: Bosses #
    #######################

    @achievement(574641)
    def boss_bzzit(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            Rayman.is_in_level(World.DREAM_FOREST, 6) &
            Bosses.on_defeated(Bosses.BZZIT)
        )

    @achievement(574642)
    def boss_moskito(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            Rayman.is_in_level(World.DREAM_FOREST, 16) &
            Bosses.on_defeated(Bosses.MOSKITO)
        )

    @achievement(574643)
    def boss_mr_sax(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            Rayman.is_in_level(World.BAND_LAND, 16) &
            Bosses.on_defeated(Bosses.MR_SAX)
        )

    @achievement(574644)
    def boss_mr_stone(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            Rayman.is_in_level(World.BLUE_MOUNTAINS, 10) &
            Bosses.on_defeated(Bosses.MR_STONE)
        )

    @achievement(574645)
    def boss_pirate_mama(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            Rayman.is_in_level(World.PICTURE_CITY, 4) &
            Bosses.on_defeated(Bosses.PIRATE_MAMA)
        )

    @achievement(574646)
    def boss_space_mama(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            Rayman.is_in_level(World.PICTURE_CITY, 11) &
            Bosses.on_defeated(Bosses.SPACE_MAMA)
        )

    @achievement(574647)
    def boss_mr_skops(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            Rayman.is_in_level(World.CAVES_OF_SKOPS, 11) &
            Bosses.on_defeated(Bosses.MR_SKOPS)
        )

    @achievement(574648)
    def boss_mr_dark(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            Rayman.is_in_level(World.CANDY_CHATEAU, 4) &
            Bosses.on_defeated(Bosses.MR_DARK)
        )

    ######################
    # Progression: Cages #
    ######################

    @achievement(573015)
    def cages_pink_plant_woods(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() & 
            Levels.PINK_PLANT_WOODS.is_selected() &
            Levels.PINK_PLANT_WOODS.on_cages_unlocked()
        )

    @achievement(573016)
    def cages_anguish_lagoon(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() & 
            Levels.ANGUISH_LAGOON.is_selected() &
            Levels.ANGUISH_LAGOON.on_cages_unlocked()
        )

    @achievement(573017)
    def cages_swamps_of_forgetfulness(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() & 
            Levels.THE_SWAMPS_OF_FORGETFULNESS.is_selected() &
            Levels.THE_SWAMPS_OF_FORGETFULNESS.on_cages_unlocked()
        )

    @achievement(573018)
    def cages_moskitos_nest(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() & 
            Levels.MOSKITOS_NEST.is_selected() &
            Levels.MOSKITOS_NEST.on_cages_unlocked()
        )

    @achievement(573019)
    def cages_bongo_hills(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() & 
            Levels.BONGO_HILLS.is_selected() &
            Levels.BONGO_HILLS.on_cages_unlocked()
        )

    @achievement(573020)
    def cages_allegro_presto(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() & 
            Levels.ALLEGRO_PRESTO.is_selected() &
            Levels.ALLEGRO_PRESTO.on_cages_unlocked()
        )

    @achievement(573021)
    def cages_gong_heights(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() & 
            Levels.GONG_HEIGHTS.is_selected() &
            Levels.GONG_HEIGHTS.on_cages_unlocked()
        )

    @achievement(573022)
    def cages_mr_sax_hullaballo(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() & 
            Levels.MR_SAXS_HULLABALLO.is_selected() &
            Levels.MR_SAXS_HULLABALLO.on_cages_unlocked()
        )

    @achievement(573023)
    def cages_twilight_gulch(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() & 
            Levels.TWILIGHT_GULCH.is_selected() &
            Levels.TWILIGHT_GULCH.on_cages_unlocked()
        )

    @achievement(573024)
    def cages_hard_rocks(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() & 
            Levels.THE_HARD_ROCKS.is_selected() &
            Levels.THE_HARD_ROCKS.on_cages_unlocked()
        )

    @achievement(573025)
    def cages_mr_stone_peaks(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() & 
            Levels.MR_STONES_PEAKS.is_selected() &
            Levels.MR_STONES_PEAKS.on_cages_unlocked()
        )

    @achievement(573026)
    def cages_eraser_plains(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() & 
            Levels.ERASER_PLAINS.is_selected() &
            Levels.ERASER_PLAINS.on_cages_unlocked()
        )

    @achievement(573027)
    def cages_pencil_pentathlon(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() & 
            Levels.PENCIL_PENTATHLON.is_selected() &
            Levels.PENCIL_PENTATHLON.on_cages_unlocked()
        )

    @achievement(573028)
    def cages_space_mama_crater(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() & 
            Levels.SPACE_MAMAS_CRATER.is_selected() &
            Levels.SPACE_MAMAS_CRATER.on_cages_unlocked()
        )

    @achievement(573029)
    def cages_crystal_palace(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() & 
            Levels.CRYSTAL_PALACE.is_selected() &
            Levels.CRYSTAL_PALACE.on_cages_unlocked()
        )

    @achievement(573030)
    def cages_eat_at_joes(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() & 
            Levels.EAT_AT_JOES.is_selected() &
            Levels.EAT_AT_JOES.on_cages_unlocked()
        )

    @achievement(573031)
    def cages_mr_skops_stalactites(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() & 
            Levels.MR_SKOPS_STALACTITES.is_selected() &
            Levels.MR_SKOPS_STALACTITES.on_cages_unlocked()
        )

    @achievement(574661)
    def all_cages(self, ach: Achievement):
        # sources = [
        #     LevelInfo(id).cages
        #     for id in range(17)
        # ]
        ach.add_core(
            Rayman.is_ingame() &
            delta_check(Memory.TOTAL_CAGES_UNLOCKED, 101, 102)
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
        ach.add_core([
            Rayman.is_ingame(),
            measured_if(Memory.STATE_IN_LEVEL_SELECT == 0),
            measured_if(Levels.PINK_PLANT_WOODS.is_selected()),
            measured(delta_sources(sources, 7, 8))
        ])

    @achievement(577245)
    def challenge_anguish_lagoon(self, ach: Achievement):
        powerups = ConditionList([
            *(
                sub_source(EntityData(id, world_id=World.DREAM_FOREST).alive)
                for id in [46, 47, 48, 63, 92, 182]
            ),
            value(6) == value(6)
        ])
        ach.add_core([
            reset_if(Rayman.on_spawn()),
            Rayman.is_ingame() &
            Rayman.is_in_level(World.DREAM_FOREST, 7),
            trigger(Level.on_clear()),
        ])
        ach.add_alt([
            pause_if(Memory.RAYMAN_HITPOINTS < delta(Memory.RAYMAN_HITPOINTS)).with_hits(1),
            # stop measuring when the next map is loading due to an issue with entities unloading and messing with the counter
            pause_if(
                (delta(Memory.INGAME_LEVEL_STATE) == 0x2) &
                (Memory.INGAME_LEVEL_STATE == 0x2)
            ).with_hits(1),
            measured_if(
                Rayman.is_ingame() &
                Rayman.is_in_level(World.DREAM_FOREST, 7)
            ),
            measured(powerups),
        ])
        ach.add_alt([
            pause_if(Memory.RAYMAN_HITPOINTS < delta(Memory.RAYMAN_HITPOINTS)).with_hits(1),
            trigger(value(0) == value(1)) # group never trigger
        ])

    @achievement(577246)
    def challenge_swamps_of_forgetfulness(self, ach: Achievement):
        ach.add_core([
            Rayman.is_ingame(),
            Rayman.is_in_level(World.DREAM_FOREST, 9),
            reset_next_if(Rayman.on_spawn()),
            pause_if(Rayman.on_animation_change(None, (0x3, 0x10)).with_hits(7)),
            trigger(Level.on_clear())
        ])

    @achievement(577247)
    def challenge_moskito_nest(self, ach: Achievement):
        plum = EntityData(13, world_id=World.DREAM_FOREST)
        ach.add_core([
            reset_if(Rayman.on_spawn()),
            Rayman.is_ingame(),
            Rayman.is_in_level(World.DREAM_FOREST, 13),
            # has not used checkpoint
            Rayman.respawn_position()[0] == 0x008c,
            (
                (plum.active == 1) &
                plum.on_animation_change((0x00, 0x0c), (0x02, 0x02))
            ).with_hits(1)
        ])
        ach.add_alt([
            pause_if(Rayman.died()).with_hits(1),
            trigger(
                (Rayman.alive() == 1) &
                # start of the map
                (Rayman.position()[0] <= 0x0120)
            )
        ])

    @achievement(577248)
    def challenge_bongo_hills(self, ach: Achievement):
        magician = EntityData(151, world_id=World.BAND_LAND)
        ach.add_core([
            Rayman.is_ingame(),
            Levels.BONGO_HILLS.is_selected(),
            reset_if(Levels.BONGO_HILLS.on_enter()),
            trigger(Levels.BONGO_HILLS.on_clear(map_id=6)),
        ])
        ach.add_alt([
            measured_if(Memory.STATE_IN_LEVEL_SELECT == 0),
            measured_if(Levels.BONGO_HILLS.is_selected()),
            pause_if(Rayman.died()).with_hits(1),
            pause_if(Rayman.has_cheated_hp()).with_hits(1),
            pause_if( # rayman is giving tings to the magician
                (Rayman.current_map() == 4) &
                (magician.animation_state == 0x8) &
                (magician.animation_substate == 0x3)
            ),
            pause_if(delta(Memory.BONUS_LEVEL_TINGS) > 0),
            pause_if(Rayman.current_map() == 17), # bonus level
            measured(Rayman.on_ting_collected()).with_hits(200),
        ])
        ach.add_alt([
            pause_if(Rayman.died()).with_hits(1),
            pause_if(Rayman.has_cheated_hp()).with_hits(1),
            trigger(value(0) == value(1)), # never trigger
        ])

    @achievement(577249)
    def challenge_allegro_presto(self, ach: Achievement):
        ach.add_core([
            Rayman.is_ingame(),
            (Bosses.MR_SAX == 0) &
            (Rayman.can_run() == 0) &
            Levels.ALLEGRO_PRESTO.on_enter().with_hits(1),
            trigger(Level.on_clear(map_id=10)),
            reset_if(
                Rayman.is_in_level(World.BAND_LAND, [7, 8, 9, 10]) &
                (Memory.INGAME_FRAME_COUNTER != delta(Memory.INGAME_FRAME_COUNTER))
            ).with_hits((4*60+30) * FRAMERATE),
            reset_if(Level.on_leave()),
            reset_if(Rayman.has_cheated_hp())
        ])

    @achievement(577250)
    def challenge_gong_heights(self, ach: Achievement):
        ach.add_core([
            Rayman.is_ingame(),
            Rayman.is_in_level(World.BAND_LAND, 13),
            reset_if(Rayman.on_spawn()),
            trigger(Level.on_clear()),
        ])
        ach.add_alt(
            pause_if(Rayman.took_damage()).with_hits(1)
        )

    @achievement(578882)
    def challenge_mr_sax_hullaballo(self, ach: Achievement):
        ach.add_core([
            Rayman.is_ingame(),
            Levels.MR_SAXS_HULLABALLO.on_enter().with_hits(1),
            Rayman.current_map() == 14,
            trigger(Level.on_clear()),
            reset_if(
                (Memory.INGAME_FRAME_COUNTER != delta(Memory.INGAME_FRAME_COUNTER))
            ).with_hits((2*60+40) * FRAMERATE),
            reset_if(Level.on_leave()),
            reset_if(Rayman.has_cheated_hp())
        ])

    @achievement(578883)
    def challenge_twilight_gulch(self, ach: Achievement):
        ach.add_core([
            Rayman.is_ingame(),
            (
                (Levels.TWILIGHT_GULCH.info.cages == 0) &
                Levels.TWILIGHT_GULCH.on_enter()
            ).with_hits(1),
            Rayman.current_map() == 1,
            trigger(Levels.TWILIGHT_GULCH.on_cages_unlocked()),
            reset_if(Level.on_leave()),
        ])

    @achievement(578884)
    def challenge_hard_rocks(self, ach: Achievement):
        sources = [
            bit5(Memory.COLLECTIBLE_THE_HARD_ROCKS_1_1.address),
            bit1(Memory.COLLECTIBLE_THE_HARD_ROCKS_1_2.address),
            bit1(Memory.COLLECTIBLE_THE_HARD_ROCKS_2.address),
            bit1(Memory.COLLECTIBLE_THE_HARD_ROCKS_3_1.address),
            bit0(Memory.COLLECTIBLE_THE_HARD_ROCKS_3_2.address),
            bit7(Memory.COLLECTIBLE_THE_HARD_ROCKS_3_3.address),
        ]
        ach.add_core([
            measured_if(Memory.STATE_IN_LEVEL_SELECT == 0),
            measured_if(Levels.THE_HARD_ROCKS.is_selected()),
            measured(delta_sources(sources, 5, 6))
        ])

    @achievement(578885)
    def challenge_mr_stones_peaks(self, ach: Achievement):
        ach.add_core([
            (
                Rayman.is_ingame() &
                Rayman.is_in_level(World.BLUE_MOUNTAINS, 6) &
                (delta(Rayman.can_super_helicopter()) == 0) &
                (Rayman.can_super_helicopter() == 1)
            ).with_hits(1),
            trigger(Level.on_clear()),
            reset_if(
                (Memory.INGAME_FRAME_COUNTER != delta(Memory.INGAME_FRAME_COUNTER))
            ).with_hits((1*60+45) * FRAMERATE),
            reset_if(Rayman.on_spawn()),
            reset_if(Level.on_leave()),
            reset_if(Rayman.took_damage()),
            reset_if(Rayman.has_cheated_hp())
        ])

    @achievement(578886)
    def challenge_eraser_plains(self, ach: Achievement):
        magician = EntityData(94, world_id=World.PICTURE_CITY)
        ach.add_core([
            Rayman.is_ingame(),
            Levels.ERASER_PLAINS.is_selected(),
            (Rayman.current_map() != 4), # pirate mama fight
            reset_if(Levels.ERASER_PLAINS.on_enter()),
            trigger(Levels.ERASER_PLAINS.on_clear(map_id=3)),
        ])
        ach.add_alt([
            measured_if(Memory.STATE_IN_LEVEL_SELECT == 0),
            measured_if(Levels.ERASER_PLAINS.is_selected()),
            pause_if(Rayman.died()).with_hits(1),
            pause_if(Rayman.has_cheated_hp()).with_hits(1),
            pause_if( # rayman is giving tings to the magician
                (Rayman.current_map() == 3) &
                (magician.animation_state == 0x8) &
                (magician.animation_substate == 0x3)
            ),
            pause_if(delta(Memory.BONUS_LEVEL_TINGS) > 0),
            pause_if(Rayman.current_map() == 12), # bonus level
            measured(Rayman.on_ting_collected()).with_hits(75),
        ])
        ach.add_alt([
            pause_if(Rayman.died()).with_hits(1),
            pause_if(Rayman.has_cheated_hp()).with_hits(1),
            trigger(value(0) == value(1)), # never trigger
        ])

    @achievement(578887)
    def challenge_pencil_pentathlon(self, ach: Achievement):
        ach.add_core([
            Rayman.is_ingame(),
            Rayman.is_in_level(World.PICTURE_CITY, 5),
            (Rayman.respawn_position()[0] == 0x0066),
            reset_if(Rayman.on_spawn()),
            trigger(Level.on_clear()),
        ])
        ach.add_alt([
            pause_if(Rayman.on_animation_change(None, (0x7, 0x1))).with_hits(4),
            pause_if(Rayman.has_cheated_hp()).with_hits(1),
        ])

    @achievement(578888)
    def challenge_space_mamas_crater(self, ach: Achievement):
        ach.add_core([
            Rayman.is_ingame(),
            Levels.SPACE_MAMAS_CRATER.on_enter().with_hits(1),
            trigger(Level.on_clear(map_id=10)),
            reset_if(
                Rayman.is_in_level(World.PICTURE_CITY, [8, 9, 10]) &
                (Memory.INGAME_FRAME_COUNTER != delta(Memory.INGAME_FRAME_COUNTER))
            ).with_hits((5*60) * FRAMERATE),
            reset_if(Level.on_leave()),
            reset_if(Rayman.has_cheated_hp())
        ])

    @achievement(578889)
    def challenge_crystal_palace(self, ach: Achievement):
        # map_id, respawn_y
        checkpoints = [
            (1, 0x00dd),
            (1, 0x0022),
            (2, 0x01dc),
            (2, 0x01d2),
        ]
        checkpoints_conds = [
            [
                reset_next_if(
                    (Rayman.current_map() == map_id) &
                    (Rayman.respawn_position()[1] == respawn_y) &
                    Rayman.on_spawn()
                ),
                pause_if(
                    (Rayman.current_map() == map_id) &
                    (Rayman.respawn_position()[1] == respawn_y) &
                    (Memory.RAYMAN_HELICOPTER_TIMER != 0xffff)
                ).with_hits(1),
            ] for map_id, respawn_y in checkpoints
        ]
        ach.add_core([
            Rayman.is_ingame(),
            Levels.CRYSTAL_PALACE.is_selected(),
            *checkpoints_conds,
            trigger(Level.on_clear(map_id=2)),
            reset_if(Level.on_leave()),
        ])
        ach.add_alt(
            pause_if(Rayman.has_cheated_hp()).with_hits(1),
        )

    @achievement(578890)
    def challenge_eat_at_joes(self, ach: Achievement):
        ach.add_core([
            Rayman.is_ingame(),
            Rayman.is_in_level(World.CAVES_OF_SKOPS, 4),
            trigger(Level.on_clear()),
            reset_if(Rayman.on_spawn()),
        ]).add_alt([
            pause_if(Rayman.has_cheated_hp()).with_hits(1),
            pause_if(Memory.RAYMAN_IS_PUNCHING == 1).with_hits(1)
        ])

    @achievement(578891)
    def challenge_mr_skops_stalactites(self, ach: Achievement):
        ach.add_core([
            Rayman.is_ingame(),
            (
                (Levels.MR_SKOPS_STALACTITES.info.cages == 0) &
                Levels.MR_SKOPS_STALACTITES.on_enter()
            ).with_hits(1),
            Rayman.is_in_level(World.CAVES_OF_SKOPS, 9),
            trigger(Levels.MR_SKOPS_STALACTITES.on_cages_unlocked()),
            reset_if(Level.on_leave()),
        ])

    @achievement(578892)
    def challenge_mr_darks_dare(self, ach: Achievement):
        dark_rayman = EntityData(148, World.CANDY_CHATEAU)
        ach.add_core([
            Rayman.is_ingame(),
            Rayman.is_in_level(World.CANDY_CHATEAU, 2),
            # check the previous frame because dark rayman despawns as soon as the player touch the end sign
            delta(dark_rayman.alive) == 1,
            # victory dance animation
            # for some reason the level state flag doesn't change in this level
            trigger(Level.on_clear(use_animation=True)),
            reset_if(Rayman.on_spawn()),
        ]).add_alt([
            pause_if(Rayman.has_cheated_hp()).with_hits(1),
            pause_if(
                (Memory.RAYMAN_ANIMATION_STATE == 0x1) &
                (Memory.RAYMAN_ANIMATION_SUBSTATE == 0x3)
            ).with_hits(1 * FRAMERATE)
        ])

    ######################
    # Challenges: Bosses #
    ######################

    @achievement(577251)
    def challenge_boss_moskito(self, ach: Achievement):
        ach.add_core([
            Rayman.is_ingame(),
            Rayman.is_in_level(World.DREAM_FOREST, 16),
            reset_if(Rayman.on_spawn()),
            trigger(Bosses.on_defeated(Bosses.MOSKITO)),
        ])
        ach.add_alt([
            pause_if(Rayman.took_damage()).with_hits(1),
        ])

    @achievement(577252)
    def challenge_boss_mr_sax(self, ach: Achievement):
        sax = EntityData(0, world_id=World.BAND_LAND)
        ach.add_core([
            Rayman.is_ingame(),
            Rayman.is_in_level(World.BAND_LAND, [15, 16]),
            # chase section checkpoint
            reset_next_if(
                (Rayman.current_map() == 15) &
                Rayman.on_spawn()
            ),
            pause_if(
                (Rayman.current_map() == 15) &
                Rayman.took_damage()
            ).with_hits(1),
            # implied fight checkpoint
            reset_next_if(Rayman.on_spawn()),
            pause_if(Rayman.took_damage()).with_hits(1),
            # boss should have 6 hp or less at the start of the second part
            reset_next_if(Rayman.on_spawn()),
            pause_if(
                (Rayman.current_map() == 16) &
                (sax.health > 6)
            ).with_hits(1),
            trigger(Bosses.on_defeated(Bosses.MR_SAX)),
        ])

    @achievement(577253)
    def challenge_boss_mr_stone(self, ach: Achievement):
        ach.add_core([
            Rayman.is_ingame(),
            Rayman.is_in_level(World.BLUE_MOUNTAINS, 10),
            reset_if(Rayman.on_spawn()),
            trigger(Bosses.on_defeated(Bosses.MR_STONE)),
        ])
        ach.add_alt(
            pause_if(Rayman.took_damage()).with_hits(1)
        )

    @achievement(577254)
    def challenge_boss_space_mama(self, ach: Achievement):
        ach.add_core([
            Rayman.is_ingame(),
            Rayman.is_in_level(World.PICTURE_CITY, 11),
            reset_if(Rayman.on_spawn()),
            trigger(Bosses.on_defeated(Bosses.SPACE_MAMA)),
        ])
        ach.add_alt(
            pause_if(Rayman.took_damage()).with_hits(1)
        )

    @achievement(577255)
    def challenge_boss_mr_skops(self, ach: Achievement):
        ach.add_core([
            Rayman.is_ingame(),
            Rayman.is_in_level(World.CAVES_OF_SKOPS, [10, 11]),
            # chase section checkpoint
            reset_next_if(
                (Rayman.current_map() == 10) &
                Rayman.on_spawn()
            ),
            pause_if(
                (Rayman.current_map() == 10) &
                Rayman.took_damage()
            ).with_hits(1),
            # implied fight checkpoint
            reset_next_if(Rayman.on_spawn()),
            pause_if(Rayman.took_damage()).with_hits(1),
            trigger(Bosses.on_defeated(Bosses.MR_SKOPS)),
        ])

    @achievement(577256)
    def challenge_boss_mr_dark(self, ach: Achievement):
        ach.add_core([
            Rayman.is_ingame(),
            Rayman.is_in_level(World.CANDY_CHATEAU, 4),
            # checkpoint for phase 1
            reset_next_if(
                (Rayman.can_punch() == 0) &
                Rayman.on_spawn()
            ),
            pause_if(
                (Rayman.can_punch() == 0) &
                Rayman.took_damage()
            ).with_hits(1),
            # rest of the fight
            reset_next_if(Rayman.on_spawn()),
            pause_if(Rayman.took_damage()).with_hits(1),
            trigger(Bosses.on_defeated(Bosses.MR_DARK)),
        ])


    #################
    # Miscellaneous #
    #################

    @achievement(573033)
    def livingstone_grimace(self, ach: Achievement):
        ach.add_core([
            Rayman.is_ingame(),
            Rayman.current_world() == World.DREAM_FOREST
        ])
        with open('data/livingstones.csv', newline='') as csvfile:
            for row in csv.DictReader(csvfile):
                entity = EntityData(int(row['Entity ID']), world_id=World.DREAM_FOREST)
                map_id = int(row['Map ID'])
                ach.add_alt([
                    Rayman.current_map() == map_id,
                    entity.active == 1,
                    entity.on_animation_change((0x0, 0x2), (0x1, 0xb))
                ])

    @achievement(573499)
    def tentacle_flower(self, ach: Achievement):
        entity = EntityData(122, world_id=World.DREAM_FOREST)
        ach.add_core(
            Rayman.is_ingame() &
            (Rayman.is_in_level(World.DREAM_FOREST, 12)) &
            (entity.active == 1) &
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

    @achievement(578893)
    def mad_drummer(self, ach: Achievement):
        ach.add_core([
            Rayman.is_ingame(),
            Rayman.is_in_level(World.BAND_LAND, 6),
        ])
        for id in [114, 115]:
            entity = EntityData(id, world_id=World.BAND_LAND)
            ach.add_alt([
                entity.active == 1,
                entity.health < delta(entity.health)
            ])

    @achievement(578894)
    def hard_rocks_exit(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            (Rayman.is_in_level(World.BLUE_MOUNTAINS, 3)) &
            (Rayman.position()[0] < 0x0700) &
            Level.on_clear()
        )

    @achievement(578895)
    def space_mama_low_exit(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            (Rayman.is_in_level(World.PICTURE_CITY, 8)) &
            (Rayman.position()[1] > 0x0300) &
            Level.on_clear()
        )

    @achievement(578896)
    def space_mama_high_exit(self, ach: Achievement):
        ach.add_core(
            Rayman.is_ingame() &
            (Rayman.is_in_level(World.PICTURE_CITY, 8)) &
            (Rayman.position()[1] < 0x0300) &
            Level.on_clear()
        )

    @achievement(578897)
    def space_pirate(self, ach: Achievement):
        ach.add_core([
            Rayman.is_ingame(),
            Rayman.current_world() == World.PICTURE_CITY,
            Rayman.is_tiny() == 1,
        ])
        with open('data/space_pirates.csv', newline='') as csvfile:
            for row in csv.DictReader(csvfile):
                entity = EntityData(int(row['Entity ID']), world_id=World.PICTURE_CITY)
                map_id = int(row['Map ID'])
                ach.add_alt([
                    Rayman.current_map() == map_id,
                    entity.active == 1,
                    (delta(entity.health) > 0) &
                    (entity.health == 0)
                ])

    @achievement(578898)
    def challenge_sax_speedrun(self, ach: Achievement):
        ach.add_core([
            (
                (Memory.STATE_DEMO_PLAY == 0) &
                (Memory.STATE_CURRENT_SAVE_FILE != 0) &
                Rayman.is_fresh_save() &
                Levels.PINK_PLANT_WOODS.on_enter()
            ).with_hits(1),
            trigger(
            Level.is_map_ready() &
                Rayman.is_in_level(World.BAND_LAND, 16) &
                Bosses.on_defeated(Bosses.MR_SAX)
            ),
            reset_if(Memory.STATE_CURRENT_SAVE_FILE != delta(mem=Memory.STATE_CURRENT_SAVE_FILE)),
            reset_if(
                Memory.GENERAL_FRAME_COUNTER != delta(Memory.GENERAL_FRAME_COUNTER)
            ).with_hits(30 * 60 * FRAMERATE),
            *(
                reset_if(cheat)
                for cheat in Rayman.has_cheated()
            )
        ])

    #############################
    # Leaderboards: Time Attack #
    #############################

    @leaderboard(154961)
    def leaderboard_sax_speedrun(self, lb: Leaderboard):
        lb.set_start(
            (Memory.STATE_CURRENT_SAVE_FILE == 3) &
            Rayman.is_fresh_save() &
            Levels.PINK_PLANT_WOODS.on_enter(),
        )
        lb.set_cancel(
            value(1) == value(1), # core
            Memory.STATE_DEMO_PLAY != 0, # alt 1
            Memory.STATE_CURRENT_SAVE_FILE != delta(mem=Memory.STATE_CURRENT_SAVE_FILE), # alt 2
            *Rayman.has_cheated(), # alt 3-5
        )
        lb.set_submit(
            Level.is_map_ready() &
            Rayman.is_in_level(World.BAND_LAND, 16) &
            Bosses.on_defeated(Bosses.MR_SAX)
        )
        lb.set_value(
            measured(Memory.GENERAL_FRAME_COUNTER != delta(Memory.GENERAL_FRAME_COUNTER))
        )

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
        lb.set_start(
            Rayman.is_ingame() &
            Rayman.is_in_level(World.DREAM_FOREST, 9) &
            (delta(Rayman.has_seed()) == 0) &
            (Rayman.has_seed() == 1)
        )

    @leaderboard(152778)
    def leaderboard_moskitos_nest(self, lb: Leaderboard):
        Levels.MOSKITOS_NEST.generate_leaderboard(lb,
            replayable_only=False,
            exclude_maps=[17], # exclude betilla
            # extra_condition=(Bosses.MOSKITO == 0),
        )
        lb.set_submit(
            Level.is_map_ready() &
            Rayman.is_in_level(World.DREAM_FOREST, 16) &
            Bosses.on_defeated(Bosses.MOSKITO)
        )

    @leaderboard(152779)
    def leaderboard_bongo_hills(self, lb: Leaderboard):
        Levels.BONGO_HILLS.generate_leaderboard(lb, replayable_only=True)

    @leaderboard(152780)
    def leaderboard_allegro_presto(self, lb: Leaderboard):
        Levels.ALLEGRO_PRESTO.generate_leaderboard(lb,
            replayable_only=False,
            exclude_maps=[11], # exclude betilla
            # extra_condition=(Bosses.MR_SAX == 0),
        )

    @leaderboard(152781)
    def leaderboard_gong_heights(self, lb: Leaderboard):
        Levels.GONG_HEIGHTS.generate_leaderboard(lb, replayable_only=True)

    @leaderboard(152782)
    def leaderboard_mr_saxs_hullaballo(self, lb: Leaderboard):
        Levels.MR_SAXS_HULLABALLO.generate_leaderboard(lb,
            replayable_only=False,
        )
        lb.set_submit(
            Level.is_map_ready() &
            Rayman.is_in_level(World.BAND_LAND, 16) &
            Bosses.on_defeated(Bosses.MR_SAX)
        )

    @leaderboard(152783)
    def leaderboard_twilight_gulch(self, lb: Leaderboard):
        Levels.TWILIGHT_GULCH.generate_leaderboard(lb,
            replayable_only=False,
            # extra_condition=(Bosses.MR_STONE == 0),
        )

    @leaderboard(152784)
    def leaderboard_the_hard_rocks(self, lb: Leaderboard):
        Levels.THE_HARD_ROCKS.generate_leaderboard(lb, replayable_only=True)

    @leaderboard(152785)
    def leaderboard_mr_stones_peak(self, lb: Leaderboard):
        Levels.MR_STONES_PEAKS.generate_leaderboard(lb,
            replayable_only=False,
            exclude_maps=[11], # exclude betilla
        )
        lb.set_start(
            Rayman.is_ingame() &
            Rayman.is_in_level(World.BLUE_MOUNTAINS, 6) &
            (delta(Rayman.can_super_helicopter()) == 0) &
            (Rayman.can_super_helicopter() == 1)
        )
        lb.set_submit(
            Level.is_map_ready() &
            Rayman.is_in_level(World.BLUE_MOUNTAINS, 10) &
            Bosses.on_defeated(Bosses.MR_STONE)
        )

    @leaderboard(152786)
    def leaderboard_eraser_plains(self, lb: Leaderboard):
        Levels.ERASER_PLAINS.generate_leaderboard(lb,
            replayable_only=False,
        )
        lb.set_submit(
            Level.is_map_ready() &
            Rayman.is_in_level(World.PICTURE_CITY, 4) &
            Bosses.on_defeated(Bosses.PIRATE_MAMA)
        )

    @leaderboard(152787)
    def leaderboard_pencil_pentathlon(self, lb: Leaderboard):
        Levels.PENCIL_PENTATHLON.generate_leaderboard(lb, replayable_only=True)

    @leaderboard(152788)
    def leaderboard_space_mamas_crater(self, lb: Leaderboard):
        Levels.SPACE_MAMAS_CRATER.generate_leaderboard(lb,
            replayable_only=False,
        )
        lb.set_submit(
            Level.is_map_ready() &
            Rayman.is_in_level(World.PICTURE_CITY, 11) &
            Bosses.on_defeated(Bosses.SPACE_MAMA)
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
        )
        lb.set_submit(
            Level.is_map_ready() &
            Rayman.is_in_level(World.CAVES_OF_SKOPS, 11) &
            Bosses.on_defeated(Bosses.MR_SKOPS)
        )

    @leaderboard(152792)
    def leaderboard_mr_darks_dare(self, lb: Leaderboard):
        Levels.MR_DARKS_DARE.generate_leaderboard(lb,
            replayable_only=False,
        )
        lb.set_submit(
            Level.is_map_ready() &
            Rayman.is_in_level(World.CANDY_CHATEAU, 4) &
            Bosses.on_defeated(Bosses.MR_DARK)
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
