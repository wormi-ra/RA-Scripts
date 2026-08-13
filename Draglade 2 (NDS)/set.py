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

    @achievement()
    def prog_round1(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            delta(Memory.STORY_PROGRESS) == 0xd,
            Memory.STORY_PROGRESS == 0xe,
        ))

    @achievement()
    def prog_round2(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            delta(Memory.STORY_PROGRESS) == 0x1e,
            Memory.STORY_PROGRESS == 0x1f,
        ))

    @achievement()
    def prog_round3(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            delta(Memory.STORY_PROGRESS) == 0x2c,
            Memory.STORY_PROGRESS == 0x2d,
        ))

    @achievement()
    def prog_round4(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            delta(Memory.STORY_PROGRESS) == 0x3d,
            Memory.STORY_PROGRESS == 0x3e,
        ))

    @achievement()
    def prog_okuman(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            delta(Memory.STORY_PROGRESS) == 0x52,
            Memory.STORY_PROGRESS == 0x53,
        ))

    @achievement()
    def prog_round5(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            delta(Memory.STORY_PROGRESS) == 0x5e,
            Memory.STORY_PROGRESS == 0x5f,
        ))
    
    @achievement()
    def prog_round6(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            delta(Memory.STORY_PROGRESS) == 0x6c,
            Memory.STORY_PROGRESS == 0x6d,
        ))

    @achievement()
    def prog_round7(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            delta(Memory.STORY_PROGRESS) == 0x76,
            Memory.STORY_PROGRESS == 0x77,
        ))

    @achievement()
    def prog_round8(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            delta(Memory.STORY_PROGRESS) == 0x81,
            Memory.STORY_PROGRESS == 0x82,
        ))

    @achievement()
    def prog_round9(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            delta(Memory.STORY_PROGRESS) == 0x92,
            Memory.STORY_PROGRESS == 0x93,
        ))

    @achievement()
    def prog_round10(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            delta(Memory.STORY_PROGRESS) == 0xa1,
            Memory.STORY_PROGRESS == 0xa2,
        ))

    @achievement()
    def prog_king(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            delta(Memory.STORY_PROGRESS) == 0xb5,
            Memory.STORY_PROGRESS == 0xb6,
        ))

    ####################
    # Titles           #
    ####################

    @achievement()
    def superhero(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            Draglade2.on_title_unlock(Memory.TITLES_SUPERHERO),
        ))

    @achievement()
    def super_rich(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Draglade2.on_title_unlock(Memory.TITLES_SUPER_RICH),
        ))

    @achievement()
    def super_celebrity(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Draglade2.on_title_unlock(Memory.TITLES_SUPER_CELEBRITY),
        ))

    @achievement()
    def scorer(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Draglade2.on_title_unlock(Memory.TITLES_SCORER),
        ))

    @achievement()
    def composer(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Draglade2.on_title_unlock(Memory.TITLES_COMPOSER),
        ))

    @achievement()
    def attacker(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Draglade2.on_title_unlock(Memory.TITLES_ATTACKER),
        ))

    @achievement()
    def rushman(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Draglade2.on_title_unlock(Memory.TITLES_RUSHMAN),
        ))

    @achievement()
    def tough_guy(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Draglade2.on_title_unlock(Memory.TITLES_TOUGH_GUY),
        ))

    @achievement()
    def berserker(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Draglade2.on_title_unlock(Memory.TITLES_BERSERKER),
        ))

    @achievement()
    def variant_hunter(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Draglade2.on_title_unlock(Memory.TITLES_VARIANT_HUNTER),
        ))

    @achievement()
    def matter_br(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Draglade2.on_title_unlock(Memory.TITLES_MATTER_BR),
        ))

    @achievement()
    def g_liver(self, ach: Achievement):
        ach.add_core(group(
            measured_if(Draglade2.is_booted()),
            measured(bitcount(Memory.STATS_G_LIVER_FLAGS.address) == 6),
            Draglade2.on_title_unlock(Memory.TITLES_G_LIVER),
        ))

    @achievement()
    def ironman(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Draglade2.on_title_unlock(Memory.TITLES_IRON_MAN),
        ))

    @achievement()
    def gladiator(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Draglade2.on_title_unlock(Memory.TITLES_GLADIATOR),
        ))

    @achievement()
    def high_ranker(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Draglade2.on_title_unlock(Memory.TITLES_SP_RANKER),
        ))

    @achievement()
    def bd_mania(self, ach: Achievement):
        ach.add_core(group(
            Draglade2.is_booted(),
            Draglade2.on_title_unlock(Memory.TITLES_BEAT_DRIVE_MANIA),
        ))

    @achievement()
    def bd_winner(self, ach: Achievement):
        ach.add_core(group(
            measured_if(Draglade2.is_booted()),
            add_source(bitcount(Memory.STATS_BD_WINNER_FLAGS.address)),
            measured(bitcount(Memory.STATS_BD_WINNER_FLAGS_1.address) == 10),
            Draglade2.on_title_unlock(Memory.TITLES_BEAT_DRIVE_WINNER),
        ))

    @achievement()
    def sbc_winner(self, ach: Achievement):
        ach.add_core(group(
            measured_if(Draglade2.is_booted()),
            add_source(bitcount(Memory.STATS_SBC_WINNER_FLAGS.address)),
            measured(bitcount(Memory.STATS_SBC_WINNER_FLAGS_1.address) == 10),
            Draglade2.on_title_unlock(Memory.TITLES_SUPER_BEAT_COMBO_WINNER),
        ))

    @achievement()
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

    @achievement()
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

    @achievement()
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

    @achievement()
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

    @achievement()
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

    @achievement()
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

    @achievement()
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

    @achievement()
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

if __name__=="__main__":
    Draglade2Set().save("output/")
