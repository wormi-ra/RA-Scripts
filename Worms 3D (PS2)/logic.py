from functools import reduce
from os import name
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
        self.framerate = {
            "US": 60,
            "EU": 50,
        }[region]


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


class Controller:
    class Button(Enum):
        L2 = 0
        R2 = 1
        L1 = 2
        R1 = 3
        TRIANGLE = 4
        O = 5
        X = 6
        SQUARE = 7
        SELECT = 8
        L3 = 9
        R3 = 10
        START = 11
        UP = 12
        RIGHT = 13
        DOWN = 14
        LEFT = 15

    @staticmethod
    def button_pressed(ctx: Context, button: Button):
        addr = [
            {
                "US": Memory.US_CONTROLLER_BUTTON_PRESSED_PRIMARY,
                "EU": Memory.EU_CONTROLLER_BUTTON_PRESSED_PRIMARY,
            },
            {
                "US": Memory.US_CONTROLLER_BUTTON_PRESSED_SECONDARY,
                "EU": Memory.EU_CONTROLLER_BUTTON_PRESSED_SECONDARY,
            },
        ][button.value // 8][ctx.region].address
        return [
            bit0, bit1, bit2, bit3, bit4, bit5, bit6, bit7
        ][button.value % 8](addr)


class GameMode:
    TUTORIAL = 3
    CAMPAIGN = 0
    CHALLENGE = 4


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

    def on_unlock(self, ctx: Context):
        return group(
            delta(self.locked(ctx)) == 1,
            self.locked(ctx) == 0
        )

    @staticmethod
    def on_unlock_type(ctx: Context, type: int):
        from data import UNLOCKS
        unlocks = list(filter(lambda e: e.type == type, UNLOCKS))
        return group(
            [
                sub_source(delta(unlock.locked(ctx)))
                for unlock in unlocks
            ],
            value(len(unlocks)) < value(len(unlocks)),
            [
                sub_source(unlock.locked(ctx))
                for unlock in unlocks
            ],
            value(len(unlocks)) == value(len(unlocks))
        )


class Mission:
    index: int
    mtype: int
    name: str
    filename: str
    gold: int
    land_maxheight: int | None
    teams: list

    def __init__(self, index: int, mtype: int, name: str, filename: str, gold: int | None, land_maxheight: int | None, teams: list) -> None:
        self.index = index
        self.mtype = mtype
        self.name = name
        self.filename = filename
        self.gold = gold or 0
        self.land_maxheight = land_maxheight
        self.teams = teams

    @staticmethod
    def current_script(ctx: Context):
        return {
            "EU": Memory.EU_INGAME_CURRENT_LUA_SCRIPT_NAME,
            "US": Memory.US_INGAME_CURRENT_LUA_SCRIPT_NAME,
        }[ctx.region]

    def is_loaded(self, ctx: Context):
        return string_equals(Mission.current_script(ctx), f"{self.filename}\0")

    @property
    def rp_hash(self):
        if self.land_maxheight == None:
            return 0
        bytes = (int.from_bytes(self.filename.encode()[:4]))
        return (self.land_maxheight + bytes) & 0xffffffff

    def on_complete(self, ctx: Context):
        gametime = XData.get_value(ctx, "MCa.LastGameTime")
        return (delta(gametime) == 0) & (gametime != 0)

    def generate_leaderboard(self, ctx: Context, lb: Leaderboard):
        for g in [lb.start]:
            if len(g) == 0:
                g.append(group(always_true()))
        lb.add_start(group(
            Worms3D.check_serial(ctx),
            self.is_loaded(ctx),
            self.on_complete(ctx),
        ))
        lb.set_cancel(always_false())
        lb.set_submit(always_true())
        lb.add_value(group(
            measured_if(Worms3D.check_serial(ctx)),
            measured(XData.get_value(ctx, "ElapsedRoundTime") / 10),
        ))


class Lua:
    @staticmethod
    def string_hash(s: str)-> int:
        l = len(s)
        h = l
        step = (l>>5)+1
        i = l
        while i >= step:
            h = h ^ ((h<<5)+(h>>2)+ord(s[i-1]))
            i -= step
        return h & 0xffffffff

    @staticmethod
    def get_index(s: str, lsize: int):
        return Lua.string_hash(s) % (1<<lsize)


class Worms3D:
    @staticmethod
    def init():
        XData.init()

    @staticmethod
    def check_serial(ctx: Context):
        return {
            "EU": string_equals(Memory.EU_SERIAL.address, "SLES"),
            "US": string_equals(Memory.US_SERIAL.address, "SLUS"),
        }[ctx.region]

    @staticmethod
    def current_gamemode(ctx: Context):
        return XData.get_value(ctx, "MCa.CurrentMissionType")

    @staticmethod
    def current_mission(ctx: Context):
        return XData.get_value(ctx, "MCa.CurrentMission")

    @staticmethod
    def game_booted(ctx: Context):
        return {
            "EU": Memory.EU_STATE_CHECK_IS_GAME_INIT,
            "US": Memory.US_STATE_CHECK_IS_GAME_INIT,
        }[ctx.region] == value(0x1)

    @staticmethod
    def is_in_menu(ctx: Context):
        return {
            "EU": Memory.EU_STATE_CHECK_IN_MENU == value(0x1),
            "US": Memory.US_STATE_CHECK_IN_MENU == value(0x1),
        }[ctx.region]

    @staticmethod
    def is_ingame(ctx: Context):
        addr = {
            "EU": Memory.EU_INGAME_CURRENT_LUA_SCRIPT_NAME,
            "US": Memory.US_INGAME_CURRENT_LUA_SCRIPT_NAME,
        }[ctx.region]
        return dword_be(addr) != dword_be(addr+1)
        # return {
        #     "EU": Memory.EU_STATE_CHECK_IN_GAME == value(0x1),
        #     "US": Memory.STATE_CHECK_IN_GAME == value(0x1),
        # }[ctx.region]

    @staticmethod
    def is_in_attract(ctx: Context):
        return bit2({
            "EU": Memory.EU_FLOWCONTROLSERVICE_GAME_STATE_2.address,
            "US": Memory.US_FLOWCONTROLSERVICE_GAME_STATE_2.address,
        }[ctx.region]) == value(0x1)

    @staticmethod
    def is_paused(ctx: Context):
        return bit0({
            "EU": Memory.EU_FLOWCONTROLSERVICE_GAME_STATE_2.address,
            "US": Memory.US_FLOWCONTROLSERVICE_GAME_STATE_2.address,
        }[ctx.region]) == value(0x1)

    @staticmethod
    def is_watching_cutscene(ctx: Context):
        return bit6({
            "EU": Memory.EU_FLOWCONTROLSERVICE_GAME_STATE.address,
            "US": Memory.US_FLOWCONTROLSERVICE_GAME_STATE.address,
        }[ctx.region]) == value(0x1)
        # return {
        #     "EU": Memory.EU_STATE_CHECK_MOVIE_PLAYING == value(0x1),
        #     "US": Memory.US_STATE_CHECK_MOVIE_PLAYING == value(0x1),
        # }[ctx.region]

    @staticmethod
    def is_loading(ctx: Context):
        return group(
            add_source({
                "EU": Memory.EU_FLOWCONTROLSERVICE_GAME_STATE,
                "US": Memory.US_FLOWCONTROLSERVICE_GAME_STATE,
            }[ctx.region] & value(0x1c)),
            value(0x0) > value(0x0)
        )
        # return {
        #     "EU": Memory.EU_STATE_CHECK_IS_LOADING == value(0x1),
        #     "US": Memory.US_STATE_CHECK_IS_LOADING == value(0x1),
        # }[ctx.region]
