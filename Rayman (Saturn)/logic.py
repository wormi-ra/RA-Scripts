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


class EntityData(GameObject):
    SIZE = 112

    @staticmethod
    def get_array_address(world_id: int):
        if (world_id == 1):
            return Memory.ENTITY_DATA_DREAM_FOREST
        return Memory.ENTITY_DATA

    def add_offset(self, cond: Condition):
        return ConditionList([
            add_address(Condition(value(self.base_address), "+", value(self.SIZE * self.id))),
            cond
        ])

    def __init__(self, id: int, world_id: int = 1) -> None:
        super().__init__(self.get_array_address(world_id))
        self.id = id
        self.animation_state = byte(0x57)
        self.animation_substate = byte(0x59)
        self.health = byte(0x61)
        self.active_state = byte(0x64)

    def on_livingstone_grimace(self):
        return ConditionList([
            # animation state changes from 0-2 to 1-b
            (and_next(self.add_offset(delta(self.animation_state) == 0x0))),
            (and_next(self.add_offset(self.animation_state == 0x1))),
            (and_next(self.add_offset(delta(self.animation_substate) == 0x2))),
            (self.add_offset(self.animation_substate == 0xb)),
        ])

    def on_tentacle_defeat(self):
        return ConditionList([
            # animation state changes from 0-15 to 0-3
            (and_next(self.add_offset(delta(self.animation_state) == 0x0))),
            (and_next(self.add_offset(self.animation_state == 0x0))),
            (and_next(self.add_offset(delta(self.animation_substate) == 0x15))),
            (self.add_offset(self.animation_substate == 0x3)),
        ])


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
        self.cages = self.offset(0x0)
        self.state = self.offset(0x1)
        self.starting_map_id = self.offset(0x2)
        self.world_id = self.offset(0x3)
        self.name = LevelInfo.NAMES[id]


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
