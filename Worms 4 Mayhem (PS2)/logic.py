from typing import Literal
from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.core.condition import Condition
from pycheevos.core.value import MemoryExpression
from pycheevos.models.leaderboard import Leaderboard
from pycheevos.models.set import Achievement
from memory import Memory
import csv

class XData:
    DATA: dict

    @staticmethod
    def init():
        with open('data/xdata.csv', newline='') as csvfile:
            XData.DATA = {
                row["key"]: int(row["address"], 16)
                for row in csv.DictReader(csvfile)
            }

    @staticmethod
    def get_value(key: str, type_override = dword) -> MemoryExpression:
        return dword(XData.DATA[key]) >> dword(0x4) >> type_override(0x1c)

    @staticmethod
    def on_value_changed(key: str, type_override = dword) -> MemoryExpression:
        return dword(XData.DATA[key]) >> dword(0x4) >> delta(type_override(0x1c)) != type_override(0x1c)

    @staticmethod
    def on_value_decreased(key: str, type_override = dword)  -> MemoryExpression:
        return dword(XData.DATA[key]) >> dword(0x4) >> delta(type_override(0x1c)) > type_override(0x1c)

    @staticmethod
    def on_value_increased(key: str, type_override = dword)  -> MemoryExpression:
        return dword(XData.DATA[key]) >> dword(0x4) >> delta(type_override(0x1c)) < type_override(0x1c)


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
    def button_pressed(button: Button):
        addr = [
            Memory.CONTROLLER_BUTTON_PRESSED_PRIMARY,
            Memory.CONTROLLER_BUTTON_PRESSED_SECONDARY,
        ][button.value // 8].address
        return [
            bit0, bit1, bit2, bit3, bit4, bit5, bit6, bit7
        ][button.value % 8](addr)

    @staticmethod
    def plugged():
        return Memory.CONTROLLER_STATE == value(0x6)


class Unlock:
    class Type:
        STORY = -7
        TUTORIAL = -6
        TIME_BONUS = -5
        TROPHY = -4
        EASTER_EGG = -3
        CHALLENGE = -2
        DEATHMATCH = -1
        NONE = 0x0
        SOUND = 0x1
        MAP = 0x2
        HAT = 0x3
        FACE = 0x4
        HAND = 0x5
        MUSTACHE = 0x6
        WEAPON = 0x7
        SCHEME = 0x8
        SET = 0x9

    UNLOCKS: list['Unlock'] = []

    key: str
    type: int

    def __init__(self, key: str, type: int = 0):
        self.key = key
        self.type = type

    @staticmethod
    def init():
        with open("data/unlocks.csv") as file:
            for row in csv.DictReader(file):
                key = str(row["Key"])
                utype = str(row["Type"])
                # addr = int(row["Address"], 16)
                preunlock = int(row["PreUnlocked"]) == 1
                if preunlock:
                    continue
                Unlock.UNLOCKS.append(Unlock(
                    key=key,
                    type=Unlock.Type.__dict__[utype],
                ))

    def locked(self):
        return XData.get_value(self.key) >> dword(0x20)

    def on_unlock(self):
        return group(
            delta(self.locked()) < 2,
            self.locked() == 2
        )

    @staticmethod
    def on_unlock_type(type: int):
        unlocks = list(filter(lambda e: e.type == type, Unlock.UNLOCKS))
        return group(
            [
                add_source(delta(unlock.locked()) / 2)
                for unlock in unlocks
            ],
            value(len(unlocks)) < value(len(unlocks)),
            [
                add_source(unlock.locked() / 2)
                for unlock in unlocks
            ],
            value(len(unlocks)) == value(len(unlocks))
        )


class Weapons:
    NONE = 0x0
    BAZOOKA = 0x1
    GRENADE = 0x2
    CLUSTER_BOMB = 0x3
    AIR_STRIKE = 0x4
    DYNAMITE = 0x5
    HOLY_HAND_GRENADE = 0x6
    BANANA_BOMB = 0x7
    LAND_MINE = 0x8
    SHOTGUN = 0x9
    BASEBALL_BAT = 0xa
    PROD = 0xb
    FIRE_PUNCH = 0xc
    HOMING_MISSILE = 0xd
    FLOOD = 0xe
    SHEEP = 0xf
    GAS_CANISTER = 0x10
    OLD_WOMAN = 0x11
    CONCRETE_DONKEY = 0x12
    SUPER_SHEEP = 0x13
    STARBURST = 0x14
    CUSTOM_WEAPON = 0x15
    ALIEN_ABDUCTION = 0x16
    FATKINS_STRIKE = 0x17
    INFLATABLE_SCOUSER = 0x18
    TAIL_NAIL = 0x19
    POISON_ARROW = 0x1a
    SENTRY_GUN = 0x1b
    SNIPER = 0x1c
    BOVINE_BLITZ = 0x1d
    GIRDER = 0x22
    NINJA_ROPE = 0x23
    PARACHUTE = 0x24
    JETPACK = 0x25
    SKIP_GO = 0x26
    SURRENDER = 0x27
    WORM_SELECT = 0x28
    BUBBLE_TROUBLE = 0x29
    ICARUS_POTION = 0x2a


class Inventory:
    class InventoryType(Enum):
        WORM = 0
        TEAM = 1
        ALLIANCE = 2

    @staticmethod
    def get_inventory(index: int, itype: InventoryType = InventoryType.TEAM):
        address = [
            Memory.WORM_INVENTORY_INSTANCES_ARRAY,
            Memory.TEAM_INSTANCES_INVENTORY_ARRAY,
            Memory.ALLIANCE_INSTANCES_INVENTORY_ARRAY,
        ][itype.value].address + (4 * index)
        return dword(address) >> dword(0x4) >> dword(0x1c)

    @staticmethod
    def get_ammo_address(weapon: int):
        return byte({
            # TODO
        }[weapon])

    @staticmethod
    def get_ammo(weapon: int, index: int, itype: InventoryType = InventoryType.TEAM):
        return Inventory.get_inventory(index, itype) >> Inventory.get_ammo_address(weapon)


class Mission:
    class Type:
        TUTORIAL = 0
        STORY = 1
        CHALLENGE = 2

    index: int
    mtype: int
    name: str
    script: str
    time_bonus: int
    teams: list

    def __init__(self, index: int, mtype: int, name: str, script: str, time_bonus: int, teams: list) -> None:
        self.index = index
        self.mtype = mtype
        self.name = name
        self.script = script
        self.time_bonus = time_bonus
        self.teams = teams

    def is_deathmatch(self):
        return self.script.startswith("Deathmatch")

    @staticmethod
    def current_script():
        return XData.get_value("GameLogic.CurrentScript")

    def is_selected(self):
        return group(
            remember(Mission.current_script()),
            string_equals(0x0, f"{self.script}\0", transform=lambda addr: recall() >> addr)
        )

    def is_loaded(self):
        return (
            self.is_selected() &
            (Lua.base_pointer() != 0x0)
        )

    def on_start(self):
        return (
            self.is_loaded() &
            (delta(XData.get_value("ElapsedRoundTime")) == 0) &
            (XData.get_value("ElapsedRoundTime") != 0)
        )

    def on_loaded(self):
        return (
            self.is_selected() &
            (delta(Lua.base_pointer()) == 0x0) &
            (Lua.base_pointer() != 0x0)
        )
    
    @staticmethod
    def on_leave():
        return (
            (delta(Lua.base_pointer()) != 0x0) &
            (Lua.base_pointer() == 0x0)
        )

    def time_bonus_on_pace(self):
        return (
            (XData.get_value("ElapsedRoundTime") < self.time_bonus)
        )

    def on_complete(self):
        # TODO
        pass

    def on_time_bonus_unlock(self):
        # TODO
        pass

    def generate_leaderboard(self, lb: Leaderboard):
        pass
        # lb.add_start(group(
        #     Worms3D.check_serial(),
        #     self.is_selected(),
        #     self.on_complete(),
        #     reset_next_if(Mission.on_hash_changed()),
        #     pause_if(~Controller.plugged().with_hits(1)),
        # ))
        # lb.set_cancel(always_false())
        # lb.set_submit(always_true())
        # lb.add_value(group(
        #     measured_if(Worms3D.check_serial()),
        #     measured(XData.get_value("ElapsedRoundTime") / 10),
        # ))

    def get_challenge_data(self):
        if self.mtype != Mission.Type.CHALLENGE:
            raise ValueError(f"Mission is not a challenge: {self.name}")
        return (
            XData.get_value("DATA.TeamBarracks")
            >> MemoryExpression(dword(0x14))._build_conditions("+", value(self.index * 4))
            >> dword(0x40)
        )

    def get_challenge_time(self):
        return (self.get_challenge_data() >> dword(0x14))

    @staticmethod
    def check_high_score_array_size():
        return (
            XData.get_value("DATA.TeamBarracks")
            >> dword(0x14) >> dword(0x18)
        ) == 20

    @staticmethod
    def generate_challenge_trophies(ach: Achievement, challenges: list["Mission"]):
        pass
        # is_deathmatch = challenges[0].is_deathmatch()
        # game_awarded = XData.get_value("MCa.GameAwarded")
        # ach.add_alt(group(
        #     pause_if(~Worms3D.check_serial()),
        #     # make sure the high score array is initialized before accumulating hits
        #     pause_if(~Worms3D.game_booted()),
        #     pause_if(~Mission.check_high_score_array_size()),
        #     *(
        #         add_hits(chall.has_challenge_time()).with_hits(1)
        #         for chall in challenges
        #     ),
        #     measured(always_false()).with_hits(len(challenges)),
        #     group(*(
        #         or_next(chall.was_loaded())
        #         for chall in challenges
        #     )).with_flag(Flag.NONE),
        #     group(
        #         remember(XData.get_value("MCa.LastGameTime")),
        #         (
        #             XData.get_value("MCa.BestGold") > recall() if is_deathmatch
        #             else XData.get_value("MCa.BestGold") < recall()
        #         )
        #     ),
        #     delta(game_awarded) == 0,
        #     game_awarded == 1,
        #     reset_if(XData.on_value_changed("PS2.CurrSlot")),
        # ))


class Worm:
    id: int
    team: int

    # TODO
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
    def get_worm_array():
        return Memory.WORM_DATA_INSTANCES_ARRAY

    def get_instance(self):
        if self.id == -1:
            raise ValueError("Cannot get instance of worm ID -1")
        return Worm.Instance(
            dword(Worm.get_worm_array().address + self.id * 4)
            >> dword(0x4) >> dword(0x1c)
        )

    @staticmethod
    def get_active_worm():
        return Worm.Instance(
            (XData.get_value("ActiveWormIndex") * value(4))
            >> Worm.get_worm_array() >> dword(0x4) >> dword(0x1c)
        )

    @staticmethod
    def on_attack():
        return (XData.on_value_changed("Weapon.GraphicalLaunchLocation"))


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
    def get_team_array():
        return Memory.TEAM_DATA_INSTANCES_ARRAY

    def get_instance(self):
        if self.id == -1:
            raise ValueError("Cannot get instance of team ID -1")
        return Team.Instance(
            dword(Team.get_team_array().address + self.id * 4)
            >> dword(0x4) >> dword(0x1c)
        )

    @staticmethod
    def get_active_team():
        return Team.Instance(
            (XData.get_value("CurrentTeamIndex") * value(4))
            >> Team.get_team_array() >> dword(0x4) >> dword(0x1c)
        )

    @staticmethod
    def get_starting_worm_count(team_id: int):
        return (
            XData.get_value("GM.GameInitData") 
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
    def get_team_array():
        return  Memory.TEAM_PERSIST_INSTANCES_ARRAY

    def get_instance(self):
        if self.id == -1:
            raise ValueError("Cannot get instance of team ID -1")
        return TeamPersist.Instance(
            dword(TeamPersist.get_team_array().address + self.id * 4)
            >> dword(0x4) >> dword(0x1c)
        )

    @staticmethod
    def get_active_team():
        return Team.Instance(
            (XData.get_value("CurrentTeamIndex") * value(4))
            >> Team.get_team_array() >> dword(0x4) >> dword(0x1c)
        )


class StringMap:
    strings: list[str]

    def __init__(self, strings: list[str]) -> None:
        self.strings = strings

    def equals(self, addr: MemoryExpression | MemoryValue, cmp: int | str, offset: int = 0, endianness: Literal['little', 'big'] = "big", encoding: str = "ascii"):
        if isinstance(cmp, int):
            string = self.strings[cmp]
        else:
            string = cmp
        assert string in self.strings
        b = string.encode(encoding)
        length = len(b)
        conds: list[tuple] = []
        candidates = [s.encode(encoding) for s in self.strings]
        i = 0
        while len(candidates) > 1 and i < length:
            chunk = b[i: i + 4]
            size = {
                "little": {
                    1: byte,
                    2: word,
                    3: tbyte,
                    4: dword,
                },
                "big": {
                    1: byte,
                    2: word_be,
                    3: tbyte_be,
                    4: dword_be,
                }
            }[endianness][len(chunk)]
            candidates = [s for s in candidates if s[i: i + 4] == chunk]
            lvalue = size(offset + i)
            rvalue = value(int.from_bytes(chunk, byteorder=endianness))
            conds.append((lvalue, rvalue))
            i += 4
        if len(conds) == 1:
            base = mem
        else:
            base = recall()
        logic = group(*[and_next(base >> lvalue == rvalue) for lvalue, rvalue in conds]).with_flag(Flag.NONE)
        if len(conds) != 1:
            logic.insert(0, remember(addr))
        return logic


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
    def base_pointer():
        return Memory.BASE_LUA_POINTER

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
    def get_node(key: str, lsize: int, depth: int):
        offset = Lua.get_index(key, lsize) * Lua.NODESIZE
        address = Lua.base_pointer() >> dword(0x38) >> dword(0x10) >> dword(0x44)
        address = address >> MemoryExpression(Condition(0x10, "+", value(offset)), start_flag=Flag.ADD_ADDRESS)
        while depth > 0:
            address >>= dword(0x10)
            depth -= 1
        return Lua.Node(key, address)


class Worms4Mayhem:
    @staticmethod
    def init():
        XData.init()
        Unlock.init()

    # @staticmethod
    # def current_gamemode():
    #     return XData.get_value("MCa.CurrentMissionType")

    # @staticmethod
    # def current_mission():
    #     return XData.get_value("MCa.CurrentMission")

    @staticmethod
    def current_team():
        return XData.get_value("CurrentTeamIndex")

    @staticmethod
    def game_booted():
        return Memory.STATE_GAME_INITIALIZED == value(0x1)

    @staticmethod
    def current_menu():
        return XData.get_value("FE.CurrentMenu")

    @staticmethod
    def is_in_menu():
        return Worms4Mayhem.current_menu() >> byte(0x0) != value(0x0)

    @staticmethod
    def is_ingame():
        return Lua.base_pointer() != dword(0x0)

    @staticmethod
    def is_in_attract():
        return Memory.ATTRACT_MODE != dword(0x0)

    @staticmethod
    def is_paused():
        # TODO
        pass

    @staticmethod
    def is_watching_cutscene():
        # TODO
        pass

    @staticmethod
    def is_loading():
        # TODO
        pass

    @staticmethod
    def number_of_teams():
        return (
            XData.get_value("GM.GameInitData") 
            >> dword(0x5c)
        )

    @staticmethod
    def frame_counter():
        counter = Memory.GLOBAL_FRAME_COUNTER
        return group(
            remember(counter % value(5)),
            add_hits(recall() == 0),
            (delta(counter) != counter),
        )


if __name__=="__main__":
    from pycheevos.utils.markdown import format_logic_group
    XData.init()
    levels = [
        "Tutorial1",
        "Tutorial2",
        "Tutorial3",
        "DinerMight",
        "SneakyBridgeThieves",
        "BuildingSiteSaboteurs",
        "TheCrateEscape",
        "DestructAndServe",
        "StormTheCastle",
        "TheWindyWizard",
        "RobInTheHood",
        "JoustAboutIt",
        "NiceToSiegeYou",
        "MineAllMine",
        "GhostHillGraveyard",
        "TinCanWally",
        "DoomCanyon",
    ]
    levels = [f"{lvl}\0" for lvl in levels]
    strmap = StringMap(levels)
    mem = XData.get_value("GameLogic.CurrentScript")
    # print(format_logic_group("Test", strmap.equals(mem, "Tutorial2").render()))
    print(strmap.equals(mem, "Tutorial1\0").render())
