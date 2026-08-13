from pycheevos.models.generic import GameObject
from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.core.condition import Condition, ConditionList
from pycheevos.core.value import MemoryValue
from pycheevos.models.leaderboard import Leaderboard

from memory import Memory

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
            group(*map(lambda title: add_source(delta(title) / 2), titles)),
            value(0) < value(len(titles)),
            group(*map(lambda title: add_source(title / 2), titles)),
            measured(value(0) == value(len(titles))),
        )
