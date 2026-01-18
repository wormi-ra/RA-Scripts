from pycheevos.models.generic import GameObject
from pycheevos.models.set import AchievementSet
from pycheevos.models.achievement import Achievement
from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.core.condition import Condition, ConditionList
from pycheevos.core.value import MemoryExpression, MemoryValue
from typing import Any, Callable

from memory import Memory

class Rayman:
    @staticmethod
    def is_ingame():
        return (Memory.STATE_INGAME == 1) & (Memory.STATE_CURRENT_SAVE_FILE != 0)

    @staticmethod
    def has_cheated():
        return (
            (Memory.INGAME_PAUSED == 1) &
            (Memory.RAYMAN_HITPOINTS > delta(Memory.RAYMAN_HITPOINTS))
        )

    @staticmethod
    def is_in_level(world_id: int, map_id: int | list[int]):
        if isinstance(map_id, list):
            return (
                (Rayman.current_world() == world_id) &
                ConditionList([
                    or_next(Rayman.current_map() == id)
                    for id in map_id
                ]).with_flag(Flag.NONE)
            )
        return (Rayman.current_world() == world_id) & (Rayman.current_map() == map_id)

    @staticmethod
    def current_world():
        return Memory.INGAME_CURRENT_WORLD

    @staticmethod
    def current_map():
        return Memory.INGAME_MAP_ID

    @staticmethod
    def tings():
        return Memory.NUMBER_OF_TINGS

    @staticmethod
    def lives():
        return Memory.NUMBER_OF_LIVES

    @staticmethod
    def continues():
        return Memory.RAYMAN_CONTINUES


class World:
    JUNGLE = 0x1
    MUSIC = 0x2
    MOUNTAIN = 0x3
    IMAGE = 0x4
    CAVE = 0x5
    CAKE = 0x6


class EntityData(GameObject):
    SIZE = 112

    @staticmethod
    def get_array_address(world_id: int):
        if (world_id == World.JUNGLE):
            return Memory.ENTITY_DATA_DREAM_FOREST
        return Memory.ENTITY_DATA

    def add_offset(self, cond: Condition):
        return ConditionList([
            add_address(Condition(value(self.base_address), "+", value(self.SIZE * self.id))),
            cond
        ])

    def __init__(self, id: int, world_id: int = World.JUNGLE) -> None:
        super().__init__(self.get_array_address(world_id))
        self.id = id
        self.pos_x = word(0x2c)
        self.pos_y = word(0x2e)
        self.camera_delta_x = word(0x32)
        self.camera_delta_y = word(0x34)
        self.initial_pos_x = word(0x38)
        self.initial_pos_y = word(0x3a)
        self.velocity_x = word(0x3c)
        self.velocity_y = word(0x3e)
        self.animation_state = byte(0x67)
        self.animation_substate = byte(0x69)
        self.health = byte(0x71)
        self.active_state = byte(0x74)

    def on_animation_change(self, prev: tuple[int, int], actual: tuple[int, int]):
        return (
            self.add_offset(delta(self.animation_state) == prev[0]) &
            self.add_offset(self.animation_state == actual[0]) &
            self.add_offset(delta(self.animation_substate) == prev[1]) &
            self.add_offset(self.animation_substate == actual[1])
        )


class MagicianLevel:
    LEVELS = {
        # (world, map)
        0: (1, 21),
        1: (1, 20),
        2: (1, 18),
        3: (1, 19),
        4: (2, 17),
        5: (2, 18),
        6: (3, 12),
        7: (3, 13),
        8: (4, 12),
        9: (4, 13),
        10: (5, 12)
    }

    def __init__(self, id) -> None:
        self.id = id

    def on_win(self):
        return (
            Rayman.is_ingame() &
            Rayman.is_in_level(*self.get_level()) &
            delta_check(Memory.BONUS_LEVEL_WIN_CUTSCENE_TIMER, 0xfffe, 0x0000)
        )

    def get_level(self):
        return self.LEVELS[self.id]


class LevelInfo(GameObject):
    SIZE = 20
    NAMES = {
        0: "Pink Plant Woods",
        1: "Anguish Lagoon",
        2: "The Swamps of Forgetfulness",
        3: "Moskito's Nest",
        4: "Bongo Hills",
        5: "Allegro Presto",
        6: "Gong Heights",
        7: "Mr Sax's Hullaballo",
        8: "Twilight Gulch",
        9: "The Hard Rocks",
        10: "Mr Stone's Peaks",
        11: "Eraser Plains",
        12: "Pencil Pentathlon",
        13: "Space Mama's Crater",
        14: "Crystal Palace",
        15: "Eat at Joe's",
        16: "Mr Skops' Stalactites",
        17: "Mr Dark's Dare",
    }

    def __init__(self, id: int) -> None:
        super().__init__(Memory.LEVEL_INFO_PINK_PLANT_WOODS + self.SIZE * id)
        self.pos_x = self.offset(0x00, word)
        self.pos_y = self.offset(0x02, word)
        self.index_up = self.offset(0x04, byte)
        self.index_left = self.offset(0x05, byte)
        self.index_down = self.offset(0x06, byte)
        self.index_right = self.offset(0x07, byte)
        self.cages = self.offset(0x08, byte)
        self.state = self.offset(0x09, byte)
        self.starting_map_id = self.offset(0x0a, byte)
        self.world_id = self.offset(0x0b, byte)
        self.name_ptr = self.offset(0x10,  dword)
        self.text_color = self.offset(0x15, byte)
        self.name = LevelInfo.NAMES[id]

    def on_cages_unlocked(self):
        return (
            Rayman.is_ingame() &
            (delta(self.cages) == 5) &
            (self.cages == 6)
        )


def delta_sources(sources: list[MemoryValue], delta_val: int, actual_val: int):
    return ConditionList([
        *(
            add_source(Condition(delta(source)))
            for source in sources[:-1]
        ),
        delta(sources[-1]) == delta_val,
        *(
            add_source(Condition(source))
            for source in sources[:-1]
        ),
        sources[-1] == actual_val
    ])

def delta_check(value: MemoryValue, prev: int, actual: int):
    return (delta(value) == prev) & (value == actual)
