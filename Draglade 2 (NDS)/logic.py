from pycheevos.models.generic import GameObject
from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.core.condition import Condition, ConditionList
from pycheevos.core.value import MemoryValue
from pycheevos.models.leaderboard import Leaderboard

from memory import Memory

def ptr(val):
    return tbyte(val)

class GameMode:
    UNINITIALIZED = 0x0 
    BOOTING_UP = 0x1
    TITLE_SCREEN = 0x2
    MAIN_MENU = 0x3
    STORY = 0x5
    VS_CPU = 0x6
    TRAINING = 0x7
    TUTORIAL = 0x8
    WIFI_CONFIG = 0xb


class Quests:
    # Side quests
    MIRAGE_EGG =            bit7(Memory.QUESTS_COMPLETION.address)
    RETURN_IT =             bit0(Memory.QUESTS_COMPLETION_1.address)
    DS_DROPPED =            bit1(Memory.QUESTS_COMPLETION_1.address)
    DORADORA =              bit2(Memory.QUESTS_COMPLETION_1.address)
    MY_TREASURE =           bit3(Memory.QUESTS_COMPLETION_1.address)
    # Story
    GOSHI_DESERT =          bit4(Memory.QUESTS_COMPLETION_1.address)
    SARU_RUINS =            bit5(Memory.QUESTS_COMPLETION_1.address)
    ZOFF_PASS =             bit6(Memory.QUESTS_COMPLETION_1.address)
    GHOST_TOWN_UG =         bit7(Memory.QUESTS_COMPLETION_1.address)
    KENMERI =               bit0(Memory.QUESTS_COMPLETION_2.address)
    POSHKA_RUINS =          bit1(Memory.QUESTS_COMPLETION_2.address)
    WIN_DESERT =            bit2(Memory.QUESTS_COMPLETION_2.address)
    IWAKU_PASS =            bit3(Memory.QUESTS_COMPLETION_2.address)
    HIDDEN_PATH =           bit4(Memory.QUESTS_COMPLETION_2.address)
    UNDERGROUND_LAB =       bit5(Memory.QUESTS_COMPLETION_2.address)
    UNDERGROUND_LAB_DEEP =  bit6(Memory.QUESTS_COMPLETION_2.address)
    MATTER_INVERT =         bit7(Memory.QUESTS_COMPLETION_2.address)
    OTHER_SPACE =           bit0(Memory.QUESTS_COMPLETION_3.address)
    # Secret
    CHANGE_BEAT =           bit1(Memory.QUESTS_COMPLETION_3.address)
    CHAR_GRAPPER =          bit2(Memory.QUESTS_COMPLETION_3.address)
    MYST_GRAPPER =          bit3(Memory.QUESTS_COMPLETION_3.address)
    # Goril
    GORILS_ROAR =           bit4(Memory.QUESTS_COMPLETION_3.address)
    GORILS_ROAR_PLUS =      bit5(Memory.QUESTS_COMPLETION_3.address)
    GORILS_RAGE =           bit6(Memory.QUESTS_COMPLETION_3.address)
    FINAL_GORIL =           bit7(Memory.QUESTS_COMPLETION_3.address)
    # Arman
    ARMAN_RANGER =          bit0(Memory.QUESTS_G_LIVE_COMPLETION.address)
    ARMAN_SOLDIER =         bit1(Memory.QUESTS_G_LIVE_COMPLETION.address)
    GOLDEN_ARMAN =          bit2(Memory.QUESTS_G_LIVE_COMPLETION.address)
    ULT_ARMAN =             bit3(Memory.QUESTS_G_LIVE_COMPLETION.address)
    # Sudden Death
    SUDDEN_DEATH =          bit4(Memory.QUESTS_G_LIVE_COMPLETION.address)

    @staticmethod
    def on_quests_complete(quests: list[MemoryValue]):
        return group(
            *map(add_source, map(delta, quests)),
            value(0) == value(len(quests) - 1),
            *map(add_source, quests),
            measured(value(0) == value(len(quests)))
        )


class Quest:
    start: int
    steps: list[int]
    end: int

    def __init__(self, start, steps, end) -> None:
        self.start = start
        self.steps = steps
        self.end = end
        pass

    @staticmethod
    def generate_instant_leaderboard(lb: Leaderboard, start: int, end: int):
            lb.set_start(group(
                Draglade2.is_booted(),
                Memory.STATE_GAME_MODE == GameMode.STORY,
                delta(Memory.SAVE_DATA_SCRIPT_ID) == start,
                Memory.SAVE_DATA_SCRIPT_ID == end,
            ))
            lb.set_cancel(always_false())
            lb.set_submit(always_true())
            lb.set_value(measured(Memory.BATTLE_FRAME_TIMER))

    @staticmethod
    def generate_versus_leaderboard(lb: Leaderboard, script: int):
            lb.set_start(group(
                Draglade2.is_booted(),
                Memory.STATE_GAME_MODE == GameMode.STORY,
                Memory.SAVE_DATA_SCRIPT_ID == script,
                delta(Memory.RESULT_STATE) != 0x3,
                Memory.RESULT_STATE == 0x3,
            ))
            lb.set_cancel(always_false())
            lb.set_submit(always_true())
            lb.set_value(measured(Memory.BATTLE_FRAME_TIMER))

    def generate_visible_leaderboard(self, lb: Leaderboard):
        lb.set_start(group(
            Draglade2.is_booted(),
            Memory.STATE_GAME_MODE == GameMode.STORY,
            (
                (delta(Memory.SAVE_DATA_SCRIPT_ID) == self.start)
                if (self.start != -1)
                else (delta(Memory.SAVE_DATA_SCRIPT_ID) != self.steps[0])
            ),
            (Memory.SAVE_DATA_SCRIPT_ID == self.steps[0]),
        ))
        lb.set_cancel(group(
            (Memory.SAVE_DATA_SCRIPT_ID != self.end),
            *map(lambda step: Memory.SAVE_DATA_SCRIPT_ID != step, self.steps),
        ))
        lb.set_submit(group(
            (delta(Memory.SAVE_DATA_SCRIPT_ID) == self.steps[-1]),
            (Memory.SAVE_DATA_SCRIPT_ID == self.end),
        ))
        lb.set_value(group(
            measured(Memory.BATTLE_FRAME_TIMER > delta(Memory.BATTLE_FRAME_TIMER))
        ))


class Versus:
    @staticmethod
    def on_win():
        return (
            (delta(Memory.VERSUS_WINNER) == 0) &
            (Memory.VERSUS_WINNER == 1)
        )


class GHall:
    KINGS = 0x6
    VOLCANO = 0x7
    WATER = 0x8
    CANYON = 0x9
    G_LIVE_VS = 0x10
    ELEKICK = 0xa
    HARMONIC = 0xb
    TRAINING_VS = 0xd
    OKUMAN = 0xc
    G_LIVE_COROCORO = 0xe
    TUTORIAL = 0xf
    G_LIVE_STORY = 0x14
    ZOFF_PASS = 0x3f
    UNDERGROUND_LAB = 0x49
    UNDERGROUND_HIDEOUT = 0x4a


class Bullet:
    class Type:
        EMPTY = -1
        FIRE = 0
        WATER = 1
        LIGHTNING = 2
        EARTH = 3
        WIND =  4
        ICE = 5
        FLOWER = 6
        POISON = 7
        LIGHT = 8
        DARK = 9
        MUSIC = 10
        VOID = 11
        SPECIAL = 12

    @staticmethod
    def get_active_deck(is_versus = False):
        size = 8
        if is_versus:
            return Memory.VERSUS_ACTIVE_DECK_INDEX * size
        return Memory.ACTIVE_DECK_INDEX * size
        

    @staticmethod
    def get_slot(slot: int, is_versus = False):
        return Bullet.get_active_deck(is_versus) >> byte(Memory.DECK_1_MAIN_BULLET_1.address + slot)

    @staticmethod
    def is_deck_empty(is_versus = False):
        return (
            ((Bullet.get_active_deck(is_versus) >> tbyte(Memory.DECK_1_MAIN_BULLET_1.address + 0x0)) == value(0xffffff)) &
            ((Bullet.get_active_deck(is_versus) >> tbyte(Memory.DECK_1_MAIN_BULLET_1.address + 0x3)) == value(0xffffff))
        )

    @staticmethod
    def deck_is_type(btype: int, is_versus = False):
        if btype == Bullet.Type.EMPTY:
            return Bullet.is_deck_empty(is_versus)
        btypes = {
            Bullet.Type.FIRE: range(0, 9),
            Bullet.Type.WATER: range(9, 18),
            Bullet.Type.LIGHTNING: range(18, 27),
            Bullet.Type.EARTH: range(27, 36),
            Bullet.Type.WIND: range(36, 45),
            Bullet.Type.ICE: range(45, 53),
            Bullet.Type.FLOWER: range(53, 61),
            Bullet.Type.POISON: range(61, 68),
            Bullet.Type.LIGHT: range(68, 76),
            Bullet.Type.DARK: range(76, 84),
            Bullet.Type.MUSIC: range(84, 89),
            Bullet.Type.VOID: range(89, 97),
            Bullet.Type.SPECIAL: range(97, 105),
        }
        r = btypes[btype]
        if r.start == 0:
            return group(*[
                (Bullet.get_slot(i, is_versus) == 0xff) |
                (Bullet.get_slot(i, is_versus) < r.stop)
                for i in range(6)
            ])
        return group(*[
            (Bullet.get_slot(i, is_versus) == 0xff) |
            (Bullet.get_slot(i, is_versus) < r.stop) &
            (Bullet.get_slot(i, is_versus) >= r.start)
            for i in range(6)
        ])


class Character:
    HIBITO = 0x0
    GUY = 0x1
    DAICHI = 0x2
    KYLE = 0x3
    ZEKE = 0x4
    CROSS = 0x5
    RAIO = 0x6
    JET = 0x7
    NEON = 0x8
    KAMZOU = 0x9


class Draglade2:
    @staticmethod
    def is_booted():
        return Memory.STATE_GAME_BOOTED == 1
    
    @staticmethod
    def script_active():
        return Memory.AREA_POINTER != 0

    @staticmethod
    def in_versus():
        return Memory.RESULT_STATE != 0

    @staticmethod
    def on_title_unlock(title: MemoryValue):
        return group(
            (delta(title) == 1) &
            (title == 2),
        )

    @staticmethod
    def on_titles_unlock(titles: list[MemoryValue]):
        return group(
            *map(lambda title: or_next(delta(title) == 1), titles[:-1]),
            delta(titles[-1]) == 1,
            *map(lambda title: add_source(delta(title) / 2), titles),
            value(0) < value(len(titles)),
            *map(lambda title: add_source(title / 2), titles),
            measured(value(0) == value(len(titles))),
        )
