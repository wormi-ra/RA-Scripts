from pycheevos.models.generic import GameObject
from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.core.condition import Condition, ConditionList
from pycheevos.core.value import MemoryValue
from pycheevos.models.leaderboard import Leaderboard

from memory import Memory

class World:
    DREAM_FOREST = 0x1
    BAND_LAND = 0x2
    BLUE_MOUNTAINS = 0x3
    PICTURE_CITY = 0x4
    CAVES_OF_SKOPS = 0x5
    CANDY_CHATEAU = 0x6


class Bosses:
    BZZIT = bit7(Memory.EVENTS_BOSSES_BEATEN.address)
    MOSKITO = bit6(Memory.EVENTS_BOSSES_BEATEN.address)
    MR_SAX = bit5(Memory.EVENTS_BOSSES_BEATEN.address)
    MR_STONE = bit4(Memory.EVENTS_BOSSES_BEATEN.address)
    PIRATE_MAMA = bit3(Memory.EVENTS_BOSSES_BEATEN.address)
    SPACE_MAMA = bit2(Memory.EVENTS_BOSSES_BEATEN.address)
    MR_SKOPS = bit1(Memory.EVENTS_BOSSES_BEATEN.address)
    MR_DARK = bit0(Memory.EVENTS_BOSSES_BEATEN.address)


class LevelInfo(GameObject):
    MEMSIZE = 20

    def __init__(self, id: int) -> None:
        super().__init__(Memory.LEVEL_INFO_PINK_PLANT_WOODS + self.MEMSIZE * id)
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

    def on_cages_unlocked(self):
        return (
            Rayman.is_ingame() &
            (delta(self.cages) == 5) &
            (self.cages == 6)
        )


class Level:
    NAMES = {
        0: "Pink Plant Woods",
        1: "Anguish Lagoon",
        2: "The Swamps of Forgetfulness",
        3: "Moskito's Nest",
        4: "Bongo Hills",
        5: "Allegro Presto",
        6: "Gong Heights",
        7: "Mr. Sax's Hullaballoo",
        8: "Twilight Gulch",
        9: "The Hard Rocks",
        10: "Mr. Stone's Peaks",
        11: "Eraser Plains",
        12: "Pencil Pentathlon",
        13: "Space Mama's Crater",
        14: "Crystal Palace",
        15: "Eat at Joe's",
        16: "Mr. Skops' Stalactites",
        17: "Mr. Dark's Dare",
    }
    MAPS = {
        # Base                      Event           Bonus
        # Dream Forest
        0: ([1, 2, 4],              [3],            [21, 20]),
        1: ([5, 7],                 [6, 8],         []),
        2: ([9, 10, 11],            [],             [18]),
        3: ([12, 13, 15],           [14, 16, 17],   [19]),
        # Band Land
        4: ([1, 2, 3, 4, 5, 6],     [],             [17]),
        5: ([7, 8, 9],              [10, 11],       [18]),
        6: ([12, 13],               [],             []),
        7: ([14],                   [15, 16],       []),
        # Blue Mountains
        8: ([1],                    [2],            []),
        9: ([3, 4, 5],              [],             [12]),
        10: ([6, 7, 8, 9],          [10, 11],       [13]),
        # Picture City
        11: ([1, 2, 3],             [4],            [12]),
        12: ([5, 6, 7],             [],             []),
        13: ([8, 9, 10],            [11],           [13]),
        # Caves of Skops
        14: ([1, 2],                [],             [12]),
        15: ([3, 4, 5, 6, 7, 8],    [],             []),
        16: ([9],                   [10, 11],       []),
        # Candy Chateau
        17: ([],                    [1, 2, 3, 4],   []),
    }

    @staticmethod
    def get_world(id: int):
        if id in range(0, 4):
            return World.DREAM_FOREST
        if id in range(4, 8):
            return World.BAND_LAND
        if id in range(8, 11):
            return World.BLUE_MOUNTAINS
        if id in range(11, 14):
            return World.PICTURE_CITY
        if id in range(14, 17):
            return World.CAVES_OF_SKOPS
        return World.CANDY_CHATEAU

    def __init__(self, id: int) -> None:
        self.id = id
        self.info = LevelInfo(id)
        self.name = Level.NAMES[id]
        self.world = Level.get_world(id)
        self.base_maps, self.event_maps, self.bonus_maps = Level.MAPS[id]

    def on_cages_unlocked(self):
        return (
            Rayman.is_ingame() &
            (delta(self.info.cages) == 5) &
            (self.info.cages == 6)
        )

    def starting_map(self) -> int:
        return (self.base_maps + self.event_maps)[0]

    @staticmethod
    def on_clear(map_id: int = 0, world_id = 0):
        conds = ConditionList()
        if world_id != 0:
            conds.append(and_next(Rayman.current_world() == map_id))
        if map_id != 0:
            conds.append(and_next(Rayman.current_map() == map_id))
        conds.append(delta_check(Memory.INGAME_LEVEL_STATE, 0x0, 0x2))
        return conds

    def on_enter(self):
        return (
            (Rayman.current_world() == self.world) &
            (Rayman.current_map() == self.starting_map()) &
            delta_check(Memory.STATE_INGAME, 0, 1)
        )

    def is_selected(self):
        return Memory.LEVEL_SELECT_CURRENT_LEVEL_ID == self.id

    @staticmethod
    def on_map_ready():
        return delta_check(Memory.STATE_MAP_READY, 1, 0)

    def generate_leaderboard(self, lb: Leaderboard, *, replayable_only = False, exclude_maps: list[int] = [], extra_condition = None):
        maps: list[int] = self.base_maps
        if not replayable_only:
            maps += self.event_maps
        for id in exclude_maps:
            maps.remove(id)
        goal_map = max(maps)
        start = (
            (Memory.STATE_DEMO_PLAY == 0) &
            self.on_enter()
        )
        if extra_condition is not None:
            start = start & extra_condition
        lb.set_start(start)
        lb.set_cancel(
            Rayman.has_cheated() |
            (Memory.STATE_INGAME != 1)
        )
        lb.set_submit(
            self.on_clear(goal_map)
        )
        lb.set_value(
            Rayman.is_in_level(self.world, maps) &
            measured(Memory.INGAME_FRAME_COUNTER != delta(Memory.INGAME_FRAME_COUNTER))
        )


class Levels:
    PINK_PLANT_WOODS = Level(0)
    ANGUISH_LAGOON = Level(1)
    THE_SWAMPS_OF_FORGETFULNESS = Level(2)
    MOSKITOS_NEST = Level(3)
    BONGO_HILLS = Level(4)
    ALLEGRO_PRESTO = Level(5)
    GONG_HEIGHTS = Level(6)
    MR_SAXS_HULLABALLOO = Level(7)
    TWILIGHT_GULCH = Level(8)
    THE_HARD_ROCKS = Level(9)
    MR_STONES_PEAKS = Level(10)
    ERASER_PLAINS = Level(11)
    PENCIL_PENTATHLON = Level(12)
    SPACE_MAMAS_CRATER = Level(13)
    CRYSTAL_PALACE = Level(14)
    EAT_AT_JOES = Level(15)
    MR_SKOPS_STALACTITES = Level(16)
    MR_DARKS_DARE = Level(17)


class MagicianLevel:
    LEVELS = {
        # (world, map)
        0: (World.DREAM_FOREST, 21),
        1: (World.DREAM_FOREST, 20),
        2: (World.DREAM_FOREST, 18),
        3: (World.DREAM_FOREST, 19),
        4: (World.BAND_LAND, 17),
        5: (World.BAND_LAND, 18),
        6: (World.BLUE_MOUNTAINS, 12),
        7: (World.BLUE_MOUNTAINS, 13),
        8: (World.PICTURE_CITY, 12),
        9: (World.PICTURE_CITY, 13),
        10: (World.CAVES_OF_SKOPS, 12)
    }

    def __init__(self, id) -> None:
        self.id = id

    def on_win(self):
        return (
            Rayman.is_ingame() &
            Rayman.is_in_level(*self.get_level()) &
            delta_check(Memory.BONUS_LEVEL_WIN_CUTSCENE_TIMER, 0xfffe, 0x0000)
        )

    def generate_leaderboard(self, lb: Leaderboard):
        lb.set_start(self.on_win())
        lb.set_cancel(value(0x0) == value(0x1)) # never cancel
        lb.set_submit(value(0x1) == value(0x1)) # instant submit
        lb.set_value([
            sub_source(value(119)), # timer overhead
            measured(Memory.INGAME_MAP_TIMER_LOW)
        ])

    def get_level(self):
        return self.LEVELS[self.id]


class Rayman:
    @staticmethod
    def is_ingame():
        return (Memory.STATE_INGAME == 1) & (Memory.STATE_DEMO_PLAY == 0)

    @staticmethod
    def has_cheated():
        return (
            (Memory.INGAME_PAUSED == 1) &
            (Memory.RAYMAN_HITPOINTS > delta(Memory.RAYMAN_HITPOINTS)) |
            # (Memory.INGAME_PAUSED == 1) &
            # (Rayman.lives() > delta(Rayman.lives())) |
            (Rayman.continues() > delta(Rayman.continues()))
        )

    @staticmethod
    def died():
        return (Rayman.lives() < delta(Rayman.lives()))

    @staticmethod
    def took_damage():
        return (Memory.RAYMAN_HITPOINTS < delta(Memory.RAYMAN_HITPOINTS))

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
    def on_animation_change(prev: tuple[int, int] | None, actual: tuple[int, int]):
        if prev is None:
            return (
                (delta(mem=Memory.RAYMAN_ANIMATION_STATE) != Memory.RAYMAN_ANIMATION_STATE) &
                (Memory.RAYMAN_ANIMATION_STATE == actual[0]) &
                (delta(Memory.RAYMAN_ANIMATION_SUBSTATE) != Memory.RAYMAN_ANIMATION_SUBSTATE) &
                (Memory.RAYMAN_ANIMATION_SUBSTATE == actual[1])
            )
        return (
            (delta(mem=Memory.RAYMAN_ANIMATION_STATE) == prev[0]) &
            (Memory.RAYMAN_ANIMATION_STATE == actual[0]) &
            (delta(Memory.RAYMAN_ANIMATION_SUBSTATE) == prev[1]) &
            (Memory.RAYMAN_ANIMATION_SUBSTATE == actual[1])
        )

    @staticmethod
    def on_ting_collected(max_hits: int = 3):
        if (max_hits <= 1):
            return delta(Rayman.tings()) != Rayman.tings()
        hits = []
        for hit in range(2, max_hits+1):
            hits += [add_hits(RecallValue() == value(hit)) for _ in range(hit-1)]
            hits += [add_hits(RecallValue() == value(-100 + hit)) for _ in range(hit-1)]
        return ConditionList([
            # remember(Rayman.tings() - delta(Rayman.tings())),
            remember(Condition(Rayman.tings(), "-", delta(Rayman.tings()))),
            hits,
            (delta(Rayman.tings()) != Rayman.tings()),
        ])

    @staticmethod
    def position():
        return (Memory.RAYMAN_POSITION_X, Memory.RAYMAN_POSITION_Y)

    @staticmethod
    def respawn_position():
        return (Memory.RAYMAN_RESPAWN_POSITION_X, Memory.RAYMAN_RESPAWN_POSITION_Y)

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
    MEMSIZE = 112

    @staticmethod
    def get_array_address(world_id: int):
        if (world_id == World.DREAM_FOREST):
            return Memory.ENTITY_DATA_DREAM_FOREST
        return Memory.ENTITY_DATA

    # def add_offset(self, cond: Condition):
    #     return ConditionList([
    #         add_address(Condition(value(self.base_address), "+", value(self.MEMSIZE * self.id))),
    #         cond
    #     ])

    def __init__(self, id: int, world_id: int = 0) -> None:
        super().__init__(self.get_array_address(world_id) + self.MEMSIZE * id)
        self.id = id
        self.pos_x = self.offset(0x2c, word)
        self.pos_y = self.offset(0x2e, word)
        self.camera_delta_x = self.offset(0x32, word)
        self.camera_delta_y = self.offset(0x34, word)
        self.initial_pos_x = self.offset(0x38, word)
        self.initial_pos_y = self.offset(0x3a, word)
        self.velocity_x = self.offset(0x3c, word)
        self.velocity_y = self.offset(0x3e, word)
        self.animation_frame = self.offset(0x64, byte)
        self.animation_index = self.offset(0x65, byte)
        self.animation_state = self.offset(0x67, byte)
        self.animation_substate = self.offset(0x69, byte)
        self.health = self.offset(0x71, byte)
        self.alive = self.offset(0x7c, bit5)
        self.active = self.offset(0x7c, bit4)
        self.flipx = self.offset(0x7c, bit1)

    def on_animation_change(self, prev: tuple[int, int], actual: tuple[int, int]):
        return (
            (delta(self.animation_state) == prev[0]) &
            (self.animation_state == actual[0]) &
            (delta(self.animation_substate) == prev[1]) &
            (self.animation_substate == actual[1])
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

def value_changed(value: MemoryValue):
    return delta(value) != value
