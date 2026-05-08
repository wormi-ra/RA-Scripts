from enum import Enum
from functools import reduce
from typing import Literal
from pycheevos.models.generic import GameObject
from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.core.condition import Condition, ConditionList
from pycheevos.core.value import MemoryExpression, MemoryValue
from pycheevos.models.leaderboard import Leaderboard
from memory import Memory
import polars as pl
import csv

Region = Literal["EU"] | Literal["US"]

class Context:
    region: Region

    def __init__(self, region: Region) -> None:
        self.region = region


class XData:
    DATA: dict

    @staticmethod
    def init():
        with open('data/xdata.csv', newline='') as csvfile:
            XData.DATA = {
                row["key"]: {
                    "sles": int(row["sles"], 16),
                    "slus": int(row["slus"], 16),
                }
                for row in csv.DictReader(csvfile)
            }

    @staticmethod
    def get_value(ctx: Context, key: str):
        return dword({
            "EU": XData.DATA[key]["sles"],
            "US": XData.DATA[key]["slus"],
        }[ctx.region]) >> dword(0x4) >> dword(0x1c)


class GameMode:
    TUTORIAL = 0x5475746f
    CAMPAIGN = 0x43616d70
    CHALLENGE = 0x4368616c
    QUICK = 0x51756963
    MULTIPLAYER = 0x4d756c74

class Unlock:
    class Type:
        VOICE = 0x0
        SCHEME = 0x1
        WEAPON = 0x2
        CHALLENGE = 0x3
        WORMAPEDIA = 0x4
        LANDSCAPE = 0x5

    key: str
    type: int

    def __init__(self, key: str, type: int):
        self.key = key
        self.type = type

    def locked(self, ctx: Context):
        return XData.get_value(ctx, self.key) >> dword(0x1c)


class Level:
    NAMES: dict[str, str]

    filename: str
    name: str

    @staticmethod
    def init():
        with open('data/levels.csv', newline='') as csvfile:
            Level.NAMES = {
                row["Filename"]: row["Name"] for row in csv.DictReader(csvfile)
            }

    @staticmethod
    def current_name(ctx: Context):
        return {
            "EU": Memory.EU_INGAME_CURRENT_SCENARIO_NAME,
            "US": Memory.US_INGAME_CURRENT_SCENARIO_NAME,
        }[ctx.region]

    def is_loaded(self, ctx: Context):
        return Level.current_name(ctx) == ascii_be(self.filename)


class Worms3D:
    UNLOCKS = [
        Unlock("L.L.Counting", Unlock.Type.LANDSCAPE),
        Unlock("L.L.Leek", Unlock.Type.LANDSCAPE),
        Unlock("L.P.Pinball", Unlock.Type.WORMAPEDIA),
        Unlock("L.L.Alien", Unlock.Type.LANDSCAPE),
        Unlock("L.Sch.All", Unlock.Type.SCHEME),
        Unlock("L.L.Cooped", Unlock.Type.LANDSCAPE),
        Unlock("L.L.Apple", Unlock.Type.LANDSCAPE),
        Unlock("L.L.Atlantis", Unlock.Type.LANDSCAPE),
        Unlock("L.W.Banana", Unlock.Type.WEAPON),
        Unlock("L.P.Pete", Unlock.Type.WORMAPEDIA),
        Unlock("L.W.BridgeK", Unlock.Type.WEAPON),
        Unlock("L.P.Bright", Unlock.Type.WORMAPEDIA),
        Unlock("L.P.Chatter", Unlock.Type.WORMAPEDIA),
        Unlock("L.P.Donkey", Unlock.Type.WORMAPEDIA),
        Unlock("L.L.Holiday", Unlock.Type.LANDSCAPE),
        Unlock("L.L.CrateBritain", Unlock.Type.LANDSCAPE),
        Unlock("L.L.Crop", Unlock.Type.LANDSCAPE),
        Unlock("L.L.DDay", Unlock.Type.LANDSCAPE),
        Unlock("L.P.Darkside", Unlock.Type.WORMAPEDIA),
        Unlock("L.C.DM1", Unlock.Type.CHALLENGE),
        Unlock("L.C.DM10", Unlock.Type.CHALLENGE),
        Unlock("L.C.DM2", Unlock.Type.CHALLENGE),
        Unlock("L.C.DM3", Unlock.Type.CHALLENGE),
        Unlock("L.C.DM4", Unlock.Type.CHALLENGE),
        Unlock("L.C.DM5", Unlock.Type.CHALLENGE),
        Unlock("L.C.DM6", Unlock.Type.CHALLENGE),
        Unlock("L.C.DM7", Unlock.Type.CHALLENGE),
        Unlock("L.C.DM8", Unlock.Type.CHALLENGE),
        Unlock("L.C.DM9", Unlock.Type.CHALLENGE),
        Unlock("L.L.Crust", Unlock.Type.LANDSCAPE),
        Unlock("L.W.EQuake", Unlock.Type.WEAPON),
        Unlock("L.P.Tapper", Unlock.Type.WORMAPEDIA),
        Unlock("L.P.Fools", Unlock.Type.WORMAPEDIA),
        Unlock("L.S.Lover", Unlock.Type.VOICE),
        Unlock("L.S.Gramps", Unlock.Type.VOICE),
        Unlock("L.L.Graveyard", Unlock.Type.LANDSCAPE),
        Unlock("L.L.Helter", Unlock.Type.LANDSCAPE),
        Unlock("L.L.High", Unlock.Type.LANDSCAPE),
        Unlock("L.S.Horror", Unlock.Type.VOICE),
        Unlock("L.L.Ice", Unlock.Type.LANDSCAPE),
        Unlock("L.C.JP1", Unlock.Type.CHALLENGE),
        Unlock("L.L.Cratefun", Unlock.Type.LANDSCAPE),
        Unlock("L.C.JP2", Unlock.Type.CHALLENGE),
        Unlock("L.C.JP3", Unlock.Type.CHALLENGE),
        Unlock("L.P.Lightside", Unlock.Type.WORMAPEDIA),
        Unlock("L.P.LandD", Unlock.Type.WORMAPEDIA),
        Unlock("L.W.MadCow", Unlock.Type.WEAPON),
        Unlock("L.S.Mad", Unlock.Type.VOICE),
        Unlock("L.L.Landing", Unlock.Type.LANDSCAPE),
        Unlock("L.L.Funfair", Unlock.Type.LANDSCAPE),
        Unlock("L.W.Nuke", Unlock.Type.WEAPON),
        Unlock("L.C.P1", Unlock.Type.CHALLENGE),
        Unlock("L.C.P2", Unlock.Type.CHALLENGE),
        Unlock("L.C.P3", Unlock.Type.CHALLENGE),
        Unlock("L.P.Pink", Unlock.Type.WORMAPEDIA),
        Unlock("L.L.Plaice", Unlock.Type.LANDSCAPE),
        Unlock("L.Sch.Pro", Unlock.Type.SCHEME),
        Unlock("L.L.Ragna", Unlock.Type.LANDSCAPE),
        Unlock("L.L.Chateau", Unlock.Type.LANDSCAPE),
        Unlock("L.L.Schools", Unlock.Type.LANDSCAPE),
        Unlock("L.L.Timbers", Unlock.Type.LANDSCAPE),
        Unlock("L.C.Shotgun2", Unlock.Type.CHALLENGE),
        Unlock("L.C.Shotgun3", Unlock.Type.CHALLENGE),
        Unlock("L.L.Showdown", Unlock.Type.LANDSCAPE),
        Unlock("L.Sch.WBnG", Unlock.Type.SCHEME),
        Unlock("L.Sch.Sniping", Unlock.Type.SCHEME),
        Unlock("L.P.Beatbox", Unlock.Type.WORMAPEDIA),
        Unlock("L.Sch.Sticky", Unlock.Type.SCHEME),
        Unlock("L.C.SS1", Unlock.Type.CHALLENGE),
        Unlock("L.C.SS2", Unlock.Type.CHALLENGE),
        Unlock("L.C.SS3", Unlock.Type.CHALLENGE),
        Unlock("L.W.SSheep", Unlock.Type.WEAPON),
        Unlock("L.S.Villain", Unlock.Type.VOICE),
        Unlock("L.L.Cherry", Unlock.Type.LANDSCAPE),
        Unlock("L.L.Tubes", Unlock.Type.LANDSCAPE),
        Unlock("L.P.Giraffe", Unlock.Type.WORMAPEDIA),
        Unlock("L.P.Horror", Unlock.Type.WORMAPEDIA),
        Unlock("L.P.Lost", Unlock.Type.WORMAPEDIA),
        Unlock("L.L.Kong", Unlock.Type.LANDSCAPE),
        Unlock("L.P.Sally", Unlock.Type.WORMAPEDIA),
        Unlock("L.P.Story", Unlock.Type.WORMAPEDIA),
        Unlock("L.L.Tree", Unlock.Type.LANDSCAPE),
        Unlock("L.L.Collide", Unlock.Type.LANDSCAPE),
        Unlock("L.P.Proto", Unlock.Type.WORMAPEDIA),
    ]

    @staticmethod
    def init():
        XData.init()
        Level.init()

    @staticmethod
    def check_serial(ctx: Context):
        return {
            "EU": Memory.EU_SERIAL == value(ascii_be("SLES")),
            "US": Memory.NTSC_SERIAL == value(ascii_be("SLUS")),
        }[ctx.region]

    @staticmethod
    def current_gamemode(ctx: Context):
        return XData.get_value(ctx, "MCa.CurrentMissionType")

    @staticmethod
    def current_mission(ctx: Context):
        return XData.get_value(ctx, "MCa.CurrentMission")

    @staticmethod
    def current_script(ctx: Context):
        return {
            "EU": Memory.EU_INGAME_CURRENT_LUA_SCRIPT_NAME,
            "US": Memory.US_INGAME_CURRENT_LUA_SCRIPT_NAME,
        }[ctx.region]

    @staticmethod
    def is_in_menu(ctx: Context):
        return {
            "EU": Memory.EU_STATE_CHECK_IN_MENU == value(0x1),
            "US": Memory.STATE_CHECK_IN_MENU == value(0x1),
        }[ctx.region]

    @staticmethod
    def is_ingame(ctx: Context):
        return {
            "EU": Memory.EU_STATE_CHECK_IN_GAME == value(0x1),
            "US": Memory.STATE_CHECK_IN_GAME == value(0x1),
        }[ctx.region]

    @staticmethod
    def is_watching_cutscene(ctx: Context):
        return {
            "EU": Memory.EU_STATE_CHECK_MOVIE_PLAYING == value(0x1),
            "US": Memory.US_STATE_CHECK_MOVIE_PLAYING == value(0x1),
        }[ctx.region]

    @staticmethod
    def is_loading(ctx: Context):
        return {
            "EU": Memory.EU_STATE_CHECK_IS_LOADING == value(0x1),
            "US": Memory.US_STATE_CHECK_IS_LOADING == value(0x1),
        }[ctx.region]

def ascii_be(value: str) -> int:
    return reduce(lambda x, y: x | y, [ord(value[len(value) - i - 1]) << (8 * i) for i in range(len(value))])
