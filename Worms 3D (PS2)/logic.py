from functools import reduce
from os import name
from typing import Literal
from pycheevos.models.generic import GameObject
from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.core.condition import Condition, ConditionList
from pycheevos.core.value import MemoryExpression, MemoryValue
from pycheevos.models.leaderboard import Leaderboard
from pycheevos.models.set import Achievement
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
    def get_value(ctx: Context, key: str, type_override = dword) -> MemoryExpression:
        return dword({
            "EU": XData.DATA[key]["sles"],
            "US": XData.DATA[key]["slus"],
        }[ctx.region]) >> dword(0x4) >> type_override(0x1c)

    @staticmethod
    def on_value_changed(ctx: Context, key: str, type_override = dword) -> MemoryExpression:
        return dword({
            "EU": XData.DATA[key]["sles"],
            "US": XData.DATA[key]["slus"],
        }[ctx.region]) >> dword(0x4) >> delta(type_override(0x1c)) != type_override(0x1c)

    @staticmethod
    def on_value_decreased(ctx: Context, key: str, type_override = dword)  -> MemoryExpression:
        return dword({
            "EU": XData.DATA[key]["sles"],
            "US": XData.DATA[key]["slus"],
        }[ctx.region]) >> dword(0x4) >> delta(type_override(0x1c)) > type_override(0x1c)

    @staticmethod
    def on_value_increased(ctx: Context, key: str, type_override = dword)  -> MemoryExpression:
        return dword({
            "EU": XData.DATA[key]["sles"],
            "US": XData.DATA[key]["slus"],
        }[ctx.region]) >> dword(0x4) >> delta(type_override(0x1c)) < type_override(0x1c)


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

    def __init__(self, key: str, type: int = 0):
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


class Weapons:
    BAZOOKA = 0x0
    GRENADE = 0x1
    CLUSTER_BOMB = 0x2
    AIRSTRIKE = 0x3
    DYNAMITE = 0x4
    HOLY_HAND_GRENADE = 0x5
    BANANA_BOMB = 0x6
    LAND_MINE = 0x7
    SHOTGUN = 0x8
    UZI = 0x9
    BASEBALL_BAT = 0xa
    PROD = 0xb
    VIKING_AXE = 0xc
    FIRE_PUNCH = 0xd
    HOMING_MISSILE = 0xe
    MORTAR = 0xf
    HOMING_PIDGEON = 0x10
    EARTHQUAKE = 0x11
    SHEEP = 0x12
    PETROL_BOMB = 0x14
    GAS_CANISTER = 0x15
    MAD_COW = 0x17
    OLD_WOMAN = 0x18
    CONCRETE_DONKEY = 0x19
    NUCLEAR_BOMB = 0x1a
    SUPER_SHEEP = 0x1d
    BLOWPIPE = 0x1e
    LOTTERY_STRIKE = 0x1f
    DOCTORS_STRIKE = 0x20
    MEGA_MINE = 0x21
    STICKY_BOMB = 0x22
    BINOCULARS = 0x23
    GIRDER = 0x27
    BRIDGE_KIT = 0x28
    NINJA_ROPE = 0x29
    PARACHUTE = 0x2a
    SCALES_OF_JUSTICE = 0x2b
    LOW_GRAVITY = 0x2c
    QUICK_WALK = 0x2d
    TELEPORT = 0x2f
    JETPACK = 0x30
    SKIP_GO = 0x31
    SURRENDER = 0x32
    WORM_SELECT = 0x33
    FREEZE = 0x34
    REDBULL = 0x35


class Inventory:
    class InventoryType(Enum):
        WORM = 0
        TEAM = 1
        ALLIANCE = 2

    @staticmethod
    def get_inventory(ctx: Context, index: int, itype: InventoryType = InventoryType.TEAM):
        address = [
            {
                "US": Memory.US_INGAME_WORM_INVENTORY_INSTANCES_ARRAY,
                "EU": Memory.EU_INGAME_WORM_INVENTORY_INSTANCES_ARRAY,
            },
            {
                "US": Memory.US_TEAM_INSTANCES_INVENTORY_ARRAY,
                "EU": Memory.EU_TEAM_INSTANCES_INVENTORY_ARRAY,
            },
            {
                "US": Memory.US_ALLIANCE_INSTANCES_INVENTORY_ARRAY,
                "EU": Memory.EU_ALLIANCE_INSTANCES_INVENTORY_ARRAY,
            },
        ][itype.value][ctx.region].address + (4 * index)
        return dword(address) >> dword(0x4) >> dword(0x1c)

    @staticmethod
    def get_ammo_address(weapon: int):
        return byte({
            Weapons.OLD_WOMAN: 0x14,
            Weapons.MAD_COW: 0x15,
            Weapons.GAS_CANISTER: 0x17,
            Weapons.PETROL_BOMB: 0x18,
            Weapons.BRIDGE_KIT: 0x19,
            Weapons.SHEEP: 0x1a,
            Weapons.EARTHQUAKE: 0x1b,
            Weapons.HOMING_PIDGEON: 0x1c,
            Weapons.MORTAR: 0x1d,
            Weapons.HOMING_MISSILE: 0x1e,
            Weapons.FIRE_PUNCH: 0x1f,
            Weapons.BAZOOKA: 0x20,
            Weapons.PROD: 0x21,
            Weapons.BASEBALL_BAT: 0x22,
            Weapons.UZI: 0x23,
            Weapons.SHOTGUN: 0x24,
            Weapons.LAND_MINE: 0x25,
            Weapons.BLOWPIPE: 0x26,
            Weapons.HOLY_HAND_GRENADE: 0x27,
            Weapons.DYNAMITE: 0x28,
            Weapons.AIRSTRIKE: 0x29,
            Weapons.CLUSTER_BOMB: 0x2a,
            Weapons.GRENADE: 0x2b,
            Weapons.VIKING_AXE: 0x2c,
            Weapons.CONCRETE_DONKEY: 0x2d,
            Weapons.TELEPORT: 0x2e,
            Weapons.BINOCULARS: 0x2f,
            Weapons.STICKY_BOMB: 0x30,
            Weapons.MEGA_MINE: 0x31,
            Weapons.DOCTORS_STRIKE: 0x32,
            Weapons.LOTTERY_STRIKE:0x33,
            Weapons.BANANA_BOMB: 0x34,
            Weapons.FREEZE: 0x35,
            Weapons.WORM_SELECT: 0x36,
            Weapons.SURRENDER: 0x37,
            Weapons.SKIP_GO: 0x38,
            Weapons.JETPACK: 0x39,
            Weapons.REDBULL: 0x3a,
            Weapons.QUICK_WALK: 0x3c,
            Weapons.LOW_GRAVITY: 0x3d,
            Weapons.SCALES_OF_JUSTICE: 0x3e,
            Weapons.PARACHUTE: 0x3f,
            Weapons.NINJA_ROPE: 0x40,
            Weapons.GIRDER: 0x42,
            Weapons.SUPER_SHEEP: 0x43,
            Weapons.NUCLEAR_BOMB: 0x46,
        }[weapon])

    @staticmethod
    def get_ammo(ctx: Context, weapon: int, index: int, itype: InventoryType = InventoryType.TEAM):
        return Inventory.get_inventory(ctx, index, itype) >> Inventory.get_ammo_address(weapon)


class Mission:
    index: int
    mtype: int
    name: str
    filename: str
    filehash: int
    gold: int
    land_maxheight: int | None
    teams: list

    def __init__(self, index: int, mtype: int, name: str, filename: str, gold: int | None, land_maxheight: int | None, teams: list) -> None:
        self.index = index
        self.mtype = mtype
        self.name = name
        self.filename = filename
        self.filehash = Lua.string_hash(filename)
        self.gold = gold or 0
        self.land_maxheight = land_maxheight
        self.teams = teams

    @staticmethod
    def current_script(ctx: Context):
        return {
            "EU": Memory.EU_INGAME_CURRENT_LUA_SCRIPT_NAME,
            "US": Memory.US_INGAME_CURRENT_LUA_SCRIPT_NAME,
        }[ctx.region]

    @staticmethod
    def current_hash(ctx: Context):
        return {
            "EU": Memory.EU_INGAME_CURRENT_LUA_SCRIPT_HASH,
            "US": Memory.US_INGAME_CURRENT_LUA_SCRIPT_HASH,
        }[ctx.region]

    def is_loaded(self, ctx: Context):
        return Mission.current_hash(ctx) == self.filehash
        # return string_equals(Mission.current_script(ctx), f"{self.filename}\0")

    def on_start(self, ctx: Context):
        return (
            self.is_loaded(ctx) &
            (delta(XData.get_value(ctx, "ElapsedRoundTime")) == 0) &
            (XData.get_value(ctx, "ElapsedRoundTime") != 0)
        )

    def on_loaded(self, ctx: Context):
        return (
            (delta(Mission.current_hash(ctx)) != self.filehash) &
            (Mission.current_hash(ctx) == self.filehash)
        )

    def on_leave(self, ctx: Context):
        return (
            (delta(Mission.current_hash(ctx)) == self.filehash) &
            (Mission.current_hash(ctx) != self.filehash)
        )

    def gold_timer_on_pace(self, ctx: Context):
        return (
            # when time runs out
            (XData.get_value(ctx, "MCa.LastGameTime") == 3) |
            (XData.get_value(ctx, "ElapsedRoundTime") < self.gold)
        )

    @property
    def rp_hash(self):
        if self.land_maxheight == None:
            return 0
        bytes = (int.from_bytes(self.filename.encode()[:4]))
        return (self.land_maxheight + bytes) & 0xffffffff

    @staticmethod
    def on_complete(ctx: Context):
        gametime = XData.get_value(ctx, "MCa.LastGameTime")
        return (delta(gametime) == 0) & (gametime != 0)

    @staticmethod
    def on_gold_medal(ctx: Context, gamemode = GameMode.CAMPAIGN, is_deathmatch = False):
        if gamemode == GameMode.CHALLENGE:
            return group(
                remember(XData.get_value(ctx, "MCa.LastGameTime")),
                (delta(XData.get_value(ctx, "MCa.LastGameTime")) == 0) &
                (
                    XData.get_value(ctx, "MCa.BestGold") > recall() if is_deathmatch
                    else XData.get_value(ctx, "MCa.BestGold") < recall()
                )
            )
        gametime = XData.get_value(ctx, "MCa.LastGameTime")
        return (delta(gametime) == 0) & (gametime == 3)

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

    def get_challenge_data(self, ctx: Context):
        if self.mtype != GameMode.CHALLENGE:
            raise ValueError(f"Mission is not a challenge: {self.name}")
        return (
            XData.get_value(ctx, "DATA.TeamBarracks")
            >> MemoryExpression(dword(0x14))._build_conditions("+", value(self.index * 4))
            >> dword(0x40) 
        )

    def get_challenge_goldtime(self, ctx: Context):
        return (self.get_challenge_data(ctx) >> dword(0x24))

    def has_challenge_goldtime(self, ctx: Context):
        if self.name.startswith("Deathmatch"):
            return self.get_challenge_goldtime(ctx) < self.gold
        else:
            return self.get_challenge_goldtime(ctx) > self.gold

    @staticmethod
    def generate_challenge_trophies(ctx: Context, challenges: list["Mission"]):
        game_awarded = XData.get_value(ctx, "MCa.GameAwarded")
        return group(
            pause_if(~Worms3D.check_serial(ctx)),
            *(
                add_hits(chall.has_challenge_goldtime(ctx)).with_hits(1)
                for chall in challenges
            ),
            measured(always_false()).with_hits(len(challenges)),
            XData.get_value(ctx, "GameOver.AwardMovie") >> dword_be(0x0) == int.from_bytes("gold".encode()),
            delta(game_awarded) == 0,
            game_awarded == 1,
            reset_if(XData.on_value_changed(ctx, "PS2.CurrSlot")),
        )

    @staticmethod
    def on_hash_changed(ctx: Context):
        return (delta(Mission.current_hash(ctx)) != Mission.current_hash(ctx))


class Landscape:
    LANDSCAPES: list["Landscape"] = []

    filename: str
    name: str
    maxheight: int

    def __init__(self, filename: str, name: str, maxheight: int) -> None:
        self.filename = filename
        self.name = name
        self.maxheight = maxheight

    @staticmethod
    def init():
        Landscape.LANDSCAPES = []
        with open("data/landscapes.csv") as file:
            for row in csv.DictReader(file):
                h = int(row["Land.InitialMaxHeight"], 16)
                Landscape.LANDSCAPES.append(Landscape(row["Filename"], row["Name"], h))


class Worm:
    id: int
    team: int

    class Instance(MemoryExpression):
        def __init__(self, expression: MemoryExpression):
            super().__init__(expression.terms[0][0], Flag.NONE)
            self.terms = expression.terms[:]

        @property
        def team(self):
            return self >> byte(0xd5)

        @property
        def health(self):
            return self >> word(0xaa)

        @property
        def equipped_weapon(self):
            return self >> dword(0x84)

        @property
        def pending_damage(self):
            return self >> dword(0xa4)

        @property
        def animation_state(self):
            return self >> dword(0x80)

        @property
        def team_id(self):
            return self >> byte(0xd5)

        @property
        def is_active(self):
            return self >> dword(0xdc)

        def on_death(self):
            return (
                (delta(self.health) != 0) &
                (self.health == 0)
            )

        def on_jump(self):
            return (
                (self.animation_state == 0x3) | # Regular jump
                (self.animation_state == 0x4) | # Straight jump
                (self.animation_state == 0x6) | # Backflip
                (self.animation_state == 0x24) & # Frontflip
                (delta(self.animation_state) == 0x2) # About to jump
            )


    def __init__(self, id: int = -1, team: int = -1) -> None:
        self.id = id
        self.team = team

    @staticmethod
    def get_worm_array(ctx: Context):
        return {
            "EU": Memory.EU_INGAME_WORM_DATA_INSTANCES_ARRAY,
            "US": Memory.US_INGAME_WORM_DATA_INSTANCES_ARRAY,
        }[ctx.region]

    def get_instance(self, ctx: Context):
        if self.id == -1:
            raise ValueError("Cannot get instance of worm ID -1")
        return Worm.Instance(
            dword(Worm.get_worm_array(ctx).address + self.id * 4)
            >> dword(0x4) >> dword(0x1c)
        )

    @staticmethod
    def get_active_worm(ctx: Context):
        return Worm.Instance(
            (XData.get_value(ctx, "ActiveWormIndex") * value(4))
            >> Worm.get_worm_array(ctx) >> dword(0x4) >> dword(0x1c)
        )

    @staticmethod
    def on_attack(ctx: Context):
        return (XData.on_value_changed(ctx, "Weapon.GraphicalLaunchLocation"))


class Team:
    id: int

    class Instance(MemoryExpression):
        def __init__(self, expression: MemoryExpression):
            super().__init__(expression.terms[0][0], Flag.NONE)
            self.terms = expression.terms[:]

        @property
        def is_local(self):
            return self >> dword(0x20)

        @property
        def is_ai_controlled(self):
            return self >> dword(0x34)

        @property
        def skill(self):
            return self >> byte(0x24)

        @property
        def allied_group(self):
            return self >> byte(0x3c)


    def __init__(self, id: int = -1) -> None:
        self.id = id

    @staticmethod
    def get_team_array(ctx: Context):
        return {
            "EU": Memory.EU_INGAME_TEAM_DATA_INSTANCES_ARRAY,
            "US": Memory.US_INGAME_TEAM_DATA_INSTANCES_ARRAY,
        }[ctx.region]

    def get_instance(self, ctx: Context):
        if self.id == -1:
            raise ValueError("Cannot get instance of team ID -1")
        return Team.Instance(
            dword(Team.get_team_array(ctx).address + self.id * 4)
            >> dword(0x4) >> dword(0x1c)
        )

    @staticmethod
    def get_active_team(ctx: Context):
        return Team.Instance(
            (XData.get_value(ctx, "CurrentTeamIndex") * value(4))
            >> Team.get_team_array(ctx) >> dword(0x4) >> dword(0x1c)
        )

    @staticmethod
    def get_starting_worm_count(ctx: Context, team_id: int):
        return (
            XData.get_value(ctx, "GM.GameInitData") 
            >> dword([
                0x38, 0x88, 0xd0, 0x11c
            ][team_id])
        )


class TeamPersist:
    id: int

    class Instance(MemoryExpression):
        def __init__(self, expression: MemoryExpression):
            super().__init__(expression.terms[0][0], Flag.NONE)
            self.terms = expression.terms[:]

        @property
        def rounds_won(self):
            return self >> dword(0x14)


    def __init__(self, id: int = -1) -> None:
        self.id = id

    @staticmethod
    def get_team_array(ctx: Context):
        return {
            "EU": Memory.EU_TEAM_PERSIST_INSTANCES_ARRAY,
            "US": Memory.US_TEAM_PERSIST_INSTANCES_ARRAY,
        }[ctx.region]

    def get_instance(self, ctx: Context):
        if self.id == -1:
            raise ValueError("Cannot get instance of team ID -1")
        return TeamPersist.Instance(
            dword(TeamPersist.get_team_array(ctx).address + self.id * 4)
            >> dword(0x4) >> dword(0x1c)
        )

    @staticmethod
    def get_active_team(ctx: Context):
        return Team.Instance(
            (XData.get_value(ctx, "CurrentTeamIndex") * value(4))
            >> Team.get_team_array(ctx) >> dword(0x4) >> dword(0x1c)
        )


class Lua:
    NODESIZE = 20

    class Node:
        key: str
        hashstr: int
        address: MemoryExpression

        def __init__(self, key: str, address: MemoryExpression) -> None:
            self.key = key
            self.hashstr = Lua.string_hash(key)
            self.address = address

        def get_hash(self):
            return self.address >> dword(0x4) >> dword(0x8)

        def get_value(self):
            return self.address >> float32(0xc)

    @staticmethod
    def string_hash(s: str)-> int:
        l = len(s)
        h = l
        step = (l >> 5) + 1
        i = l
        while i >= step:
            h = (h ^ ((h << 5) + (h >> 2) + ord(s[i-1]))) & 0xffffffff
            i -= step
        return h

    @staticmethod
    def get_index(key: str, lsize: int):
        return Lua.string_hash(key) % (1 << lsize)

    @staticmethod
    def get_node(ctx: Context, key: str, lsize: int, depth: int):
        offset = Lua.get_index(key, lsize) * Lua.NODESIZE
        address = {
            "EU": Memory.EU_LUA_GLOBAL_TABLE_NODE_VECTOR,
            "US": Memory.US_LUA_GLOBAL_TABLE_NODE_VECTOR,
        }[ctx.region]
        address = MemoryExpression(Condition(address, "+", value(offset)), start_flag=Flag.ADD_ADDRESS)
        while depth > 0:
            address >>= dword(0x10)
            depth -= 1
        return Lua.Node(key, address)


class Worms3D:
    @staticmethod
    def init():
        XData.init()
        Landscape.init()

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
    def current_team(ctx: Context):
        return XData.get_value(ctx, "CurrentTeamIndex")

    @staticmethod
    def game_booted(ctx: Context):
        return {
            "EU": Memory.EU_STATE_CHECK_IS_GAME_INIT,
            "US": Memory.US_STATE_CHECK_IS_GAME_INIT,
        }[ctx.region] == value(0x1)

    @staticmethod
    def menu_state(ctx: Context):
        return {
            "EU": Memory.EU_STATE_CHECK_IN_MENU,
            "US": Memory.US_STATE_CHECK_IN_MENU,
        }[ctx.region]

    @staticmethod
    def is_in_menu(ctx: Context):
        return Worms3D.menu_state(ctx) == value(0x1)

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

    @staticmethod
    def number_of_teams(ctx: Context):
        return (
            XData.get_value(ctx, "GM.GameInitData") 
            >> dword(0x5c)
        )

    @staticmethod
    def generate_multiplayer_challenge(ctx: Context, ach: Achievement, scheme_name: str, land_name: str, skill = 5, player_worms = 4, enemy_worms = 4):
        from data import Missions
        mission = Missions.STDVS
        scheme = XData.get_value(ctx, "GM.SchemeData") >> dword(0x14)
        land = XData.get_value(ctx, "Land.File")
        for team_id in range(2):
            team_persist = TeamPersist(team_id).get_instance(ctx)
            team = Team(team_id).get_instance(ctx)
            enemy_team = Team(team_id ^ 1).get_instance(ctx)
            ach.add_alt(group(
                Worms3D.check_serial(ctx),
                mission.is_loaded(ctx),
                Worms3D.number_of_teams(ctx) == 2,
                Team.get_starting_worm_count(ctx, team_id) == player_worms,
                Team.get_starting_worm_count(ctx, team_id ^ 1) == enemy_worms,
                team.is_ai_controlled == 0,
                enemy_team.skill == skill,
                remember(scheme),
                string_equals(0x0, f"{scheme_name}\0", transform=lambda val: recall() >> val),
                remember(land),
                string_equals(0x0, f"{land_name}\0", transform=lambda val: recall() >> val),
                # No Wormpot
                XData.get_value(ctx, "FE.Wormpot.Reel1") == 0x11,
                XData.get_value(ctx, "FE.Wormpot.Reel2") == 0x11,
                XData.get_value(ctx, "FE.Wormpot.Reel3") == 0x11,
                # On round won
                trigger(team_persist >> delta(dword(0x14)) < dword(0x14)),
            ))
