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
class Draglade2Set(AchievementSet):
    def __init__(self):
        super().__init__(
            game_id=26886,
            title="Custom Beat Battle: Draglade 2"
        )

    ####################
    # Progression      #
    ####################

    @achievement(631472)
    def prog_hibito(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            Memory.STORY_PROGRESS == 0x7,
            (delta(Memory.VERSUS_WINNER) == 0),
            trigger(Memory.VERSUS_WINNER == 1)
        ))

    @achievement(631473)
    def prog_round1(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            delta(Memory.STORY_PROGRESS) == 0xd,
            Memory.STORY_PROGRESS == 0xe,
        ))

    @achievement(631474)
    def prog_round2(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            delta(Memory.STORY_PROGRESS) == 0x1e,
            Memory.STORY_PROGRESS == 0x1f,
        ))

    @achievement(631475)
    def prog_round3(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            delta(Memory.STORY_PROGRESS) == 0x2c,
            Memory.STORY_PROGRESS == 0x2d,
        ))

    @achievement(631476)
    def prog_round4(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            delta(Memory.STORY_PROGRESS) == 0x3d,
            Memory.STORY_PROGRESS == 0x3e,
        ))

    @achievement(631477)
    def prog_okuman(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            delta(Memory.STORY_PROGRESS) == 0x52,
            Memory.STORY_PROGRESS == 0x53,
        ))

    @achievement(631478)
    def prog_round5(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            delta(Memory.STORY_PROGRESS) == 0x5e,
            Memory.STORY_PROGRESS == 0x5f,
        ))
    
    @achievement(631479)
    def prog_round6(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            delta(Memory.STORY_PROGRESS) == 0x6c,
            Memory.STORY_PROGRESS == 0x6d,
        ))

    @achievement(631480)
    def prog_round7(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            delta(Memory.STORY_PROGRESS) == 0x76,
            Memory.STORY_PROGRESS == 0x77,
        ))

    @achievement(631481)
    def prog_round8(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            delta(Memory.STORY_PROGRESS) == 0x81,
            Memory.STORY_PROGRESS == 0x82,
        ))

    @achievement(631482)
    def prog_round9(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            delta(Memory.STORY_PROGRESS) == 0x92,
            Memory.STORY_PROGRESS == 0x93,
        ))

    @achievement(631483)
    def prog_round10(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            delta(Memory.STORY_PROGRESS) == 0xa1,
            Memory.STORY_PROGRESS == 0xa2,
        ))

    @achievement(631484)
    def prog_king(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            delta(Memory.STORY_PROGRESS) == 0xb5,
            Memory.STORY_PROGRESS == 0xb6,
        ))

    ####################
    # Quests           #
    ####################

    @achievement(631485)
    def quests_side(self, ach: Achievement):
        quests = [
            Quests.MIRAGE_EGG,
            Quests.RETURN_IT,
            Quests.DS_DROPPED,
            Quests.DORADORA,
            Quests.MY_TREASURE,
        ]
        ach.add_core(group(
            measured_if(Draglade2.is_booted()),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            Quests.on_quests_complete(quests)
        ))

    @achievement(631486)
    def quests_story(self, ach: Achievement):
        quests = [
            Quests.GOSHI_DESERT,
            Quests.SARU_RUINS,
            Quests.ZOFF_PASS,
            Quests.GHOST_TOWN_UG,
            Quests.KENMERI,
            Quests.POSHKA_RUINS,
            Quests.WIN_DESERT,
            Quests.IWAKU_PASS,
            Quests.HIDDEN_PATH,
            Quests.UNDERGROUND_LAB,
            Quests.UNDERGROUND_LAB_DEEP,
            Quests.MATTER_INVERT,
            Quests.OTHER_SPACE,
        ]
        ach.add_core(group(
            measured_if(Draglade2.is_booted()),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            Quests.on_quests_complete(quests)
        ))

    @achievement(631487)
    def quests_secret(self, ach: Achievement):
        quests = [
            Quests.CHANGE_BEAT,
            Quests.CHAR_GRAPPER,
            Quests.MYST_GRAPPER,
        ]
        ach.add_core(group(
            measured_if(Draglade2.is_booted()),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            Quests.on_quests_complete(quests)
        ))

    @achievement(631488)
    def quests_goril(self, ach: Achievement):
        quests = [
            Quests.GORILS_ROAR,
            Quests.GORILS_ROAR_PLUS,
            Quests.GORILS_RAGE,
            Quests.FINAL_GORIL,
        ]
        ach.add_core(group(
            measured_if(Draglade2.is_booted()),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            Quests.on_quests_complete(quests)
        ))

    @achievement(631489)
    def quests_arman(self, ach: Achievement):
        quests = [
            Quests.ARMAN_RANGER,
            Quests.ARMAN_SOLDIER,
            Quests.GOLDEN_ARMAN,
            Quests.ULT_ARMAN,
        ]
        ach.add_core(group(
            measured_if(Draglade2.is_booted()),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            Quests.on_quests_complete(quests)
        ))

    @achievement(631490)
    def quests_sudden_death(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            delta(Quests.SUDDEN_DEATH) == 0,
            Quests.SUDDEN_DEATH == 1,
        ))

    ####################
    # Titles           #
    ####################

    @achievement(631491)
    def superhero(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            Draglade2.on_title_unlock(Memory.TITLES_SUPERHERO),
        ))

    @achievement(631492)
    def super_rich(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Draglade2.on_title_unlock(Memory.TITLES_SUPER_RICH),
        ))

    @achievement(631493)
    def super_celebrity(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Draglade2.on_title_unlock(Memory.TITLES_SUPER_CELEBRITY),
        ))

    @achievement(631494)
    def scorer(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Draglade2.on_title_unlock(Memory.TITLES_SCORER),
        ))

    @achievement(631495)
    def composer(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Draglade2.on_title_unlock(Memory.TITLES_COMPOSER),
        ))

    @achievement(631496)
    def attacker(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Draglade2.on_title_unlock(Memory.TITLES_ATTACKER),
        ))

    @achievement(631497)
    def rushman(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Draglade2.on_title_unlock(Memory.TITLES_RUSHMAN),
        ))

    @achievement(631498)
    def tough_guy(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Draglade2.on_title_unlock(Memory.TITLES_TOUGH_GUY),
        ))

    @achievement(631499)
    def berserker(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Draglade2.on_title_unlock(Memory.TITLES_BERSERKER),
        ))

    @achievement(631513)
    def variant_hunter(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Draglade2.on_title_unlock(Memory.TITLES_VARIANT_HUNTER),
        ))

    @achievement(631500)
    def matter_br(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Draglade2.on_title_unlock(Memory.TITLES_MATTER_BR),
        ))

    @achievement(631514)
    def g_liver(self, ach: Achievement):
        ach.add_core(group(
            measured_if(Draglade2.is_booted()),
            measured(bitcount(Memory.STATS_G_LIVER_FLAGS.address) == 6),
            Draglade2.on_title_unlock(Memory.TITLES_G_LIVER),
        ))

    @achievement(631515)
    def ironman(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Draglade2.on_title_unlock(Memory.TITLES_IRON_MAN),
        ))

    @achievement(631501)
    def gladiator(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Draglade2.on_title_unlock(Memory.TITLES_GLADIATOR),
        ))

    @achievement(631516)
    def sp_ranker(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Draglade2.on_title_unlock(Memory.TITLES_SP_RANKER),
        ))

    @achievement(631502)
    def bd_mania(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Draglade2.on_title_unlock(Memory.TITLES_BEAT_DRIVE_MANIA),
        ))

    @achievement(631517)
    def bd_winner(self, ach: Achievement):
        ach.add_core(group(
            measured_if(Draglade2.is_booted()),
            add_source(bitcount(Memory.STATS_BD_WINNER_FLAGS.address)),
            measured(bitcount(Memory.STATS_BD_WINNER_FLAGS_1.address) == 10),
            Draglade2.on_title_unlock(Memory.TITLES_BEAT_DRIVE_WINNER),
        ))

    @achievement(631503)
    def sbc_winner(self, ach: Achievement):
        ach.add_core(group(
            measured_if(Draglade2.is_booted()),
            add_source(bitcount(Memory.STATS_SBC_WINNER_FLAGS.address)),
            measured(bitcount(Memory.STATS_SBC_WINNER_FLAGS_1.address) == 10),
            Draglade2.on_title_unlock(Memory.TITLES_SUPER_BEAT_COMBO_WINNER),
        ))

    @achievement(631518)
    def all_chests(self, ach: Achievement):
        chests = group(*[
            add_source(bitcount(chest.address))
            for chest in CHESTS
        ])
        ach.add_core(group(
            measured_if(Draglade2.is_booted()),
            add_source(chests),
            measured(value(0) == value(56)),
            Draglade2.on_title_unlock(Memory.TITLES_TREASURE_HUNTER),
        ))

    @achievement(631519)
    def all_bullets(self, ach: Achievement):
        bullets = group(*[
            add_source(bullet)
            for bullet in STORY_BULLETS
        ])
        ach.add_core(group(
            measured_if(Draglade2.is_booted()),
            add_source(bullets),
            measured(value(0) == value(97)),
            Draglade2.on_title_unlock(Memory.TITLES_BULLETEER),
        ))

    @achievement(631504)
    def bc_mania(self, ach: Achievement):
        titles = [
            Memory.TITLES_BEAT_COMBO_MANIA,
            Memory.TITLES_FULL_BEAT_COMBO,
            Memory.TITLES_SUPER_BEAT_COMBO_MANIA,
        ]
        ach.add_core(group(
            measured_if(Draglade2.is_booted()),
            Draglade2.on_titles_unlock(titles),
        ))

    @achievement(631520)
    def g_live_master(self, ach: Achievement):
        titles = [
            Memory.TITLES_G_LIVE_GRAPPER,
            Memory.TITLES_G_LIVE_KING,
            Memory.TITLES_G_LIVE_MASTER,
        ]
        ach.add_core(group(
            measured_if(Draglade2.is_booted()),
            Draglade2.on_titles_unlock(titles),
        ))

    @achievement(631505)
    def charismatic_grapper(self, ach: Achievement):
        titles = [
            Memory.TITLES_IDOL_GRAPPER,
            Memory.TITLES_STAR_GRAPPER,
            Memory.TITLES_CHARISMATIC_GRAPPER,
        ]
        ach.add_core(group(
            measured_if(Draglade2.is_booted()),
            Draglade2.on_titles_unlock(titles),
        ))

    @achievement(631521)
    def primary_elementalist(self, ach: Achievement):
        titles = [
            Memory.TITLES_AQUA_G,
            Memory.TITLES_FIRE_G,
            Memory.TITLES_ELEC_G,
            Memory.TITLES_ROCK_G,
        ]
        ach.add_core(group(
            measured_if(Draglade2.is_booted()),
            Draglade2.on_titles_unlock(titles),
        ))

    @achievement(631522)
    def secondary_elementalist(self, ach: Achievement):
        titles = [
            Memory.TITLES_WIND_G,
            Memory.TITLES_ICE_G,
            Memory.TITLES_PETAL_G,
            Memory.TITLES_POISON_G,
        ]
        ach.add_core(group(
            measured_if(Draglade2.is_booted()),
            Draglade2.on_titles_unlock(titles),
        ))

    @achievement(631506)
    def tertiary_elementalist(self, ach: Achievement):
        titles = [
            Memory.TITLES_LIGHT_G,
            Memory.TITLES_DARK_G,
            Memory.TITLES_MUSIC_G,
            Memory.TITLES_VOID_G,
        ]
        ach.add_core(group(
            measured_if(Draglade2.is_booted()),
            Draglade2.on_titles_unlock(titles),
        ))

    ####################
    # Challenges       #
    ####################

    @achievement(631523)
    def corocoro_challenge(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            delta(Memory.SAVE_DATA_SCRIPT_ID) == 0x22f,
            Memory.SAVE_DATA_SCRIPT_ID == 0x230,
        ))

    @achievement(631524)
    def speedrun_my_treasure(self, ach: Achievement):
        timer = 90 * FRAMERATE # 1 minute 30
        start = 0x177
        step = 0x178
        end = 0xc5
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            (
                (delta(Memory.SAVE_DATA_SCRIPT_ID) == start) &
                (Memory.SAVE_DATA_SCRIPT_ID == step)
            ).with_hits(1),
            trigger(
                (delta(Memory.SAVE_DATA_SCRIPT_ID) == step) &
                (Memory.SAVE_DATA_SCRIPT_ID == end)
            ),
            reset_if(
                (Memory.SAVE_DATA_SCRIPT_ID != end) &
                (Memory.SAVE_DATA_SCRIPT_ID != step)
            ),
            reset_if(Memory.BATTLE_FRAME_TIMER > delta(Memory.BATTLE_FRAME_TIMER)).with_hits(timer)
        ))

    @achievement(631507)
    def speedrun_underground_lab_core(self, ach: Achievement):
        timer = 120 * FRAMERATE # 2 minutes
        start = 0x13a
        step = 0x13b
        end = 0xb8
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            (
                (delta(Memory.SAVE_DATA_SCRIPT_ID) == start) &
                (Memory.SAVE_DATA_SCRIPT_ID == step)
            ).with_hits(1),
            trigger(
                (delta(Memory.SAVE_DATA_SCRIPT_ID) == step) &
                (Memory.SAVE_DATA_SCRIPT_ID == end)
            ),
            reset_if(
                (Memory.SAVE_DATA_SCRIPT_ID != end) &
                (Memory.SAVE_DATA_SCRIPT_ID != step)
            ),
            reset_if(
                (bit2(Memory.PLAYER_DAMAGE_EFFECT_1.address) == 1)
            ),
            reset_if(Memory.BATTLE_FRAME_TIMER > delta(Memory.BATTLE_FRAME_TIMER)).with_hits(timer),
        ))

    @achievement(631525)
    def challenge_goril(self, ach: Achievement):
        start = 0x186
        end = 0x1bc
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            Bullet.is_deck_empty(),
            delta(Memory.SAVE_DATA_SCRIPT_ID) == start,
            trigger(Memory.SAVE_DATA_SCRIPT_ID == end),
        ))

    @achievement(631508)
    def challenge_arman(self, ach: Achievement):
        start = 0x1a0
        step = 0x1a1
        step2 = 0x1b2
        end = 0x1bc
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            Bullet.is_deck_empty(),
            (Memory.SAVE_DATA_SCRIPT_ID == step) |
            (delta(Memory.SAVE_DATA_SCRIPT_ID) == step2),
            trigger(Memory.SAVE_DATA_SCRIPT_ID == end),
        ))

    ####################
    # Versus           #
    ####################

    @achievement(631526)
    def versus_hibito(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.VS_CPU,
            Draglade2.in_versus(),
            Memory.BATTLE_G_HALL == GHall.WATER,
            Memory.BATTLE_TRAPS == 1,
            Memory.BATTLE_PLAYER_CHARACTER == Character.HIBITO,
            Memory.BATTLE_ENEMY_CHARACTER == Character.KYLE,
            Bullet.deck_is_type(Bullet.Type.FIRE, is_versus=True),
            delta(Memory.VERSUS_WINNER) == 0,
            trigger(Memory.VERSUS_WINNER == 1),
        ))

    @achievement(631527)
    def versus_kyle(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.VS_CPU,
            Draglade2.in_versus(),
            Memory.BATTLE_G_HALL == GHall.CANYON,
            Memory.BATTLE_TRAPS == 1,
            Memory.BATTLE_PLAYER_CHARACTER == Character.KYLE,
            Memory.BATTLE_ENEMY_CHARACTER == Character.DAICHI,
            Bullet.deck_is_type(Bullet.Type.WATER, is_versus=True),
            delta(Memory.VERSUS_WINNER) == 0,
            trigger(Memory.VERSUS_WINNER == 1),
        ))

    @achievement(631509)
    def versus_daichi(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.VS_CPU,
            Draglade2.in_versus(),
            Memory.BATTLE_G_HALL == GHall.ELEKICK,
            Memory.BATTLE_TRAPS == 1,
            Memory.BATTLE_PLAYER_CHARACTER == Character.DAICHI,
            Memory.BATTLE_ENEMY_CHARACTER == Character.GUY,
            Bullet.deck_is_type(Bullet.Type.EARTH, is_versus=True),
            delta(Memory.VERSUS_WINNER) == 0,
            trigger(Memory.VERSUS_WINNER == 1),
        ))

    @achievement(631528)
    def versus_guy(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.VS_CPU,
            Draglade2.in_versus(),
            Memory.BATTLE_G_HALL == GHall.KINGS,
            Memory.BATTLE_PLAYER_CHARACTER == Character.GUY,
            Memory.BATTLE_ENEMY_CHARACTER == Character.JET,
            Bullet.deck_is_type(Bullet.Type.LIGHTNING, is_versus=True),
            delta(Memory.VERSUS_WINNER) == 0,
            trigger(Memory.VERSUS_WINNER == 1),
        ))

    @achievement(631510)
    def versus_jet(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.VS_CPU,
            Draglade2.in_versus(),
            Memory.BATTLE_G_HALL == GHall.HARMONIC,
            Memory.BATTLE_PLAYER_CHARACTER == Character.JET,
            Memory.BATTLE_ENEMY_CHARACTER == Character.NEON,
            Bullet.deck_is_type(Bullet.Type.VOID, is_versus=True),
            delta(Memory.VERSUS_WINNER) == 0,
            trigger(Memory.VERSUS_WINNER == 1),
        ))

    @achievement(631529)
    def versus_neon(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.VS_CPU,
            Draglade2.in_versus(),
            Memory.BATTLE_G_HALL == GHall.CANYON,
            Memory.BATTLE_TRAPS == 1,
            Memory.BATTLE_PLAYER_CHARACTER == Character.NEON,
            Memory.BATTLE_ENEMY_CHARACTER == Character.KAMZOU,
            Bullet.deck_is_type(Bullet.Type.MUSIC, is_versus=True),
            delta(Memory.VERSUS_WINNER) == 0,
            trigger(Memory.VERSUS_WINNER == 1),
        ))

    @achievement(631511)
    def versus_cross(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.VS_CPU,
            Draglade2.in_versus(),
            Memory.BATTLE_G_HALL == GHall.TRAINING_VS,
            Memory.BATTLE_PLAYER_CHARACTER == Character.CROSS,
            Memory.BATTLE_ENEMY_CHARACTER == Character.RAIO,
            Bullet.deck_is_type(Bullet.Type.LIGHT, is_versus=True),
            delta(Memory.VERSUS_WINNER) == 0,
            trigger(Memory.VERSUS_WINNER == 1),
        ))

    @achievement(631530)
    def versus_zeke(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.VS_CPU,
            Draglade2.in_versus(),
            Memory.BATTLE_G_HALL == GHall.G_LIVE_VS,
            Memory.BATTLE_PLAYER_CHARACTER == Character.ZEKE,
            Memory.BATTLE_ENEMY_CHARACTER == Character.CROSS,
            Bullet.deck_is_type(Bullet.Type.DARK, is_versus=True),
            delta(Memory.VERSUS_WINNER) == 0,
            trigger(Memory.VERSUS_WINNER == 1),
        ))

    @achievement(631531)
    def versus_kamzou(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.VS_CPU,
            Draglade2.in_versus(),
            Memory.BATTLE_G_HALL == GHall.VOLCANO,
            Memory.BATTLE_TRAPS == 1,
            Memory.BATTLE_PLAYER_CHARACTER == Character.KAMZOU,
            Memory.BATTLE_ENEMY_CHARACTER == Character.HIBITO,
            Bullet.deck_is_type(Bullet.Type.POISON, is_versus=True),
            delta(Memory.VERSUS_WINNER) == 0,
            trigger(Memory.VERSUS_WINNER == 1),
        ))

    @achievement(631512)
    def versus_raio(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.VS_CPU,
            Draglade2.in_versus(),
            Memory.BATTLE_G_HALL == GHall.OKUMAN,
            Memory.BATTLE_PLAYER_CHARACTER == Character.RAIO,
            Memory.BATTLE_ENEMY_CHARACTER == Character.ZEKE,
            Bullet.deck_is_type(Bullet.Type.EMPTY, is_versus=True),
            delta(Memory.VERSUS_WINNER) == 0,
            trigger(Memory.VERSUS_WINNER == 1),
        ))

    ####################
    # Leaderboards     #
    ####################

    @leaderboard(169497)
    def leaderboard_mirage_egg(self, lb: Leaderboard):
        Quest.generate_instant_leaderboard(lb, start=0x159, end=0xc3)

    @leaderboard(169487)
    def leaderboard_return_it(self, lb: Leaderboard):
        Quest.generate_versus_leaderboard(lb, script=0x160)

    @leaderboard(169498)
    def leaderboard_ds_dropped(self, lb: Leaderboard):
        Quest.generate_instant_leaderboard(lb, start=0x162, end=0xc4)

    @leaderboard(169499)
    def leaderboard_doradora(self, lb: Leaderboard):
        Quest.generate_versus_leaderboard(lb, script=0x176)

    @leaderboard(169488)
    def leaderboard_my_treasure(self, lb: Leaderboard):
        Quest(
            start=0x177,
            steps=[0x178],
            end=0xc5,
        ).generate_visible_leaderboard(lb)

    @leaderboard(169500)
    def leaderboard_goshi_desert(self, lb: Leaderboard):
        Quest(
            start=0xc8,
            steps=[0xc9, 0xcd],
            end=0x17,
        ).generate_visible_leaderboard(lb)

    @leaderboard(169501)
    def leaderboard_saru_ruins(self, lb: Leaderboard):
        Quest.generate_instant_leaderboard(lb, start=0xd0, end=0x27)
        # Quest(
        #     start=0xcf,
        #     steps=[0xd0],
        #     end=0x27,
        # ).generate_visible_leaderboard(lb)

    @leaderboard(169489)
    def leaderboard_zoff_pass(self, lb: Leaderboard):
        Quest(
            start=0xe0,
            steps=[0xe1, 0x5d, 0xe6],
            end=0x5e,
        ).generate_visible_leaderboard(lb)

    @leaderboard(169502)
    def leaderboard_ghost_underground(self, lb: Leaderboard):
        Quest(
            start=0xe8,
            steps=[0xea, 0xee],
            end=0x67,
        ).generate_visible_leaderboard(lb)

    @leaderboard(169490)
    def leaderboard_kenmeri(self, lb: Leaderboard):
        Quest.generate_instant_leaderboard(lb, start=0xf9, end=0x8b)
        # Quest(
        #     start=0xf8,
        #     steps=[0xf9],
        #     end=0x8b,
        # ).generate_visible_leaderboard(lb)

    @leaderboard(169508)
    def leaderboard_poshka_ruins(self, lb: Leaderboard):
        Quest(
            start=0x110,
            steps=[0x111, 0x122],
            end=0x9e,
        ).generate_visible_leaderboard(lb)

    @leaderboard(169503)
    def leaderboard_win_desert(self, lb: Leaderboard):
        Quest.generate_versus_leaderboard(lb, script=0xf5)

    @leaderboard(169491)
    def leaderboard_iwaku_pass(self, lb: Leaderboard):
        Quest.generate_versus_leaderboard(lb, script=0x10e)

    @leaderboard(169509)
    def leaderboard_hidden_path(self, lb: Leaderboard):
        Quest(
            start=0x124,
            steps=[0x125, 0xb3, 0x12c],
            end=0xb4,
        ).generate_visible_leaderboard(lb)

    @leaderboard(169510)
    def leaderboard_underground_lab(self, lb: Leaderboard):
        Quest(
            start=0x12d,
            steps=[0x12e, 0xb6, 0x134],
            end=0xb7,
        ).generate_visible_leaderboard(lb)

    @leaderboard(169492)
    def leaderboard_underground_lab_core(self, lb: Leaderboard):
        Quest(
            start=0x13a,
            steps=[0x13b],
            end=0xb8,
        ).generate_visible_leaderboard(lb)

    @leaderboard(169782)
    def leaderboard_matter_invert(self, lb: Leaderboard):
        Quest.generate_versus_leaderboard(lb, script=0x156)

    @leaderboard(169504)
    def leaderboard_other_space(self, lb: Leaderboard):
        Quest.generate_versus_leaderboard(lb, script=0x157)

    @leaderboard(169511)
    def leaderboard_change_beat(self, lb: Leaderboard):
        Quest.generate_versus_leaderboard(lb, script=0x180)

    @leaderboard(169493)
    def leaderboard_char_grapper(self, lb: Leaderboard):
        Quest.generate_versus_leaderboard(lb, script=0x181)

    @leaderboard(169512)
    def leaderboard_myst_grapper(self, lb: Leaderboard):
        Quest.generate_versus_leaderboard(lb, script=0x182)

    @leaderboard(169505)
    def leaderboard_gorils_roar(self, lb: Leaderboard):
        Quest.generate_versus_leaderboard(lb, script=0x183)

    @leaderboard(169494)
    def leaderboard_gorils_roar_plus(self, lb: Leaderboard):
        Quest.generate_versus_leaderboard(lb, script=0x184)

    @leaderboard(169513)
    def leaderboard_gorils_rage(self, lb: Leaderboard):
        Quest.generate_versus_leaderboard(lb, script=0x185)

    @leaderboard(169495)
    def leaderboard_final_goril(self, lb: Leaderboard):
        Quest.generate_versus_leaderboard(lb, script=0x186)

    @leaderboard(169506)
    def leaderboard_arman_ranger(self, lb: Leaderboard):
        Quest(
            start=0x187,
            steps=[0x188, 0x18c],
            end=0x1bc,
        ).generate_visible_leaderboard(lb)

    @leaderboard(169514)
    def leaderboard_arman_soldier(self, lb: Leaderboard):
        Quest(
            start=0x18d,
            steps=[0x18e, 0x198],
            end=0x1bc,
        ).generate_visible_leaderboard(lb)

    @leaderboard(169496)
    def leaderboard_golden_arman(self, lb: Leaderboard):
        Quest(
            start=0x199,
            steps=[0x19a, 0x19f],
            end=0x1bc,
        ).generate_visible_leaderboard(lb)

    @leaderboard(169515)
    def leaderboard_ultimate_arman(self, lb: Leaderboard):
        Quest(
            start=0x1a0,
            steps=[0x1a1, 0x1b2],
            end=0x1bc,
        ).generate_visible_leaderboard(lb)

    @leaderboard(169507)
    def leaderboard_sudden_death(self, lb: Leaderboard):
        Quest(
            start=-1,
            steps=[0x1b3, 0x1b4, 0x1b5, 0x1b6, 0x1b7, 0x1b8, 0x1b9, 0x1ba],
            end=0x1bc,
        ).generate_visible_leaderboard(lb)

    @leaderboard(169783)
    def leaderboard_challenge_arena(self, lb: Leaderboard):
        Quest(
            start=0x21e,
            steps=[0x225, 0x226, 0x227, 0x228, 0x229, 0x22a, 0x22b, 0x22c, 0x22d, 0x22e, 0x22f],
            end=0x230,
        ).generate_visible_leaderboard(lb)

if __name__=="__main__":
    Draglade2Set().save("output/")
