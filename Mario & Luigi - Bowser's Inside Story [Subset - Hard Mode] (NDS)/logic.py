import csv
from pycheevos.core.helpers import *
from memory import Memory

class Slots:
    MARIO_LUIGI = [
        Memory.EQUIPMENT_,      # Mario 1
        Memory.EQUIPMENT__1,    # Mario 2
        Memory.EQUIPMENT__2,    # Mario 3
        Memory.EQUIPMENT__3,    # Luigi 1
        Memory.EQUIPMENT__4,    # Luigi 2
        Memory.EQUIPMENT__5,    # Luigi 3
    ]
    BOWSER = [
        Memory.EQUIPMENT__6,    # Bowser 1
        Memory.EQUIPMENT__7,    # Bowser 2
        Memory.EQUIPMENT__8,    # Bowser 3
    ]


class Actor:
    ALL = -1
    MARIO_LUIGI = 0
    BOWSER = 1


class Equipment:
    NONE = 0x00
    THIN_WEAR = 0x01
    PICNIC_WEAR = 0x02
    LEISURE_WEAR = 0x03
    FIGHTER_WEAR = 0x04
    HEART_WEAR = 0x05
    BRAWNY_WEAR = 0x06
    GROWN_UP_WEAR = 0x07
    KOOPA_WEAR = 0x08
    HERO_WEAR = 0x09
    BALM_WEAR = 0x0A
    MUSCLE_WEAR = 0x0B
    MASTER_WEAR = 0x0C
    KING_WEAR = 0x0D
    STAR_WEAR = 0x0E
    D_STAR_WEAR = 0x0F
    A_OK_WEAR = 0x10
    RENTAL_WEAR = 0x11
    HP_SOCKS = 0x12
    DELUXE_HP_SOCKS = 0x13
    SP_SOCKS = 0x14
    DX_SP_SOCKS = 0x15
    HUSTLE_SOCKS = 0x16
    COIN_SOCKS = 0x17
    STARCHED_SOCKS = 0x18
    GUMPTION_SOCKS = 0x19
    BRO_SOCKS = 0x1A
    GALL_SOCKS = 0x1B
    RUGGED_SOCKS = 0x1C
    EXP_SOCKS = 0x1D
    NO_TOUCH_SOCKS = 0x1E
    NURSE_SOCKS = 0x1F
    DOCTOR_SOCKS = 0x20
    SPECIAL_SOCKS = 0x21
    SURPRISING_SOCKS = 0x22
    GUARDIAN_SOCKS = 0x23
    POW_GLOVES = 0x24
    DX_POW_GLOVES = 0x25
    MUSROOM_GLOVES = 0x26
    SPECIAL_GLOVES = 0x27
    HEAVY_GLOVES = 0x28
    DELICIOUS_GLOVES = 0x29
    FLOWER_GLOVES = 0x2A
    BYE_BYE_GLOVES = 0x2B
    SOFTENER_GLOVES = 0x2C
    ITEM_GLOVES = 0x2D
    SIPHON_GLOVES = 0x2E
    DENT_GLOVES = 0x2F
    POW_BOOTS = 0x30
    DX_POW_BOOTS = 0x31
    TIP_TOP_BOOTS = 0x32
    SPECIAL_BOOTS = 0x33
    HEAVY_BOOTS = 0x34
    DAREDEVIL_BOOTS = 0x35
    SHELL_BOOTS = 0x36
    DIZZY_BOOTS = 0x37
    SHROOB_BOOTS = 0x38
    COIN_BOOTS = 0x39
    SIPHON_BOOTS = 0x3A
    BIG_STOMP_BOOTS = 0x3B
    HAPPY_CHARM = 0x3C
    LUCK_CHARM = 0x3D
    THRIFT_CHARM = 0x3E
    BUDGET_CHARM = 0x3F
    TIGHT_BELT = 0x40
    ADVICE_PATCH = 0x41
    LUXURY_PATCH = 0x42
    HEROIC_PATCH = 0x43
    SMALL_SHELL = 0x44
    BIG_SHELL = 0x45
    GIANT_SHELL = 0x46
    KO_SHELL = 0x47
    GOLD_RING = 0x48
    GOLD_CROWN = 0x49
    LAZY_SCARF = 0x4A
    MUSHROOM_STONE = 0x4B
    POW_MUSH_JAM = 0x4C
    DEF_MUSH_JAM = 0x4D
    TREASURE_SPECS = 0x4E
    VENGEANCE_CAPE = 0x4F
    CHALLENGE_MEDAL = 0x50
    SHABBY_SHELL = 0x51
    SPECIAL_SHELL = 0x52
    SAFETY_SHELL = 0x53
    JUDGE_SHELL = 0x54
    ROCK_SHELL = 0x55
    ARMORED_SHELL = 0x56
    RAMPAGE_SHELL = 0x57
    DREAM_SHELL = 0x58
    WICKED_SHELL = 0x59
    IRONCLAD_SHELL = 0x5A
    BLOCK_RING = 0x5B
    KING_SHELL = 0x5C
    POWER_BAND = 0x5D
    POWER_BAND_PLUS = 0x5E
    MINION_BAND = 0x5F
    MINION_BAND_SP = 0x60
    IRON_FIST_BAND = 0x61
    VAMPIRE_BAND = 0x62
    STAMINA_BAND = 0x63
    HUNTER_BAND = 0x64
    LUCKY_BAND = 0x65
    BLOCK_BAND = 0x66
    FURY_BAND = 0x67
    POWER_FANGS = 0x68
    POWER_FANGS_X = 0x69
    SPECIAL_FANGS = 0x6A
    SPECIAL_FANGS_X = 0x6B
    RED_HOT_FANGS = 0x6C
    BURNING_FANGS = 0x6D
    FURY_FANGS = 0x6E
    BONE_FANGS = 0x6F
    INTRUDER_FANGS = 0x70
    BLOCK_FANGS = 0x71
    FLASHY_FANGS = 0x72
    CHEAP_RING = 0x73
    ECONOMY_RING = 0x74
    HEROIC_RING = 0x75
    GLUTTON_RING = 0x76
    EXCELLENT_RING = 0x77
    DRUMSTICK_RING = 0x78
    PEACE_RING = 0x79
    FILL_UP_RING = 0x7A
    RESTORE_RING = 0x7B
    FAST_CASH_RING = 0x7C
    TREASURE_RING = 0x7D
    SAFETY_RING = 0x7E
    HARD_RING = 0x7F
    RENTAL_SHELL = 0x80


class MnLBIS:
    STATS_CAP = {}

    @staticmethod
    def init():
        with open('data/stats.csv', newline='') as csvfile:
            for row in csv.DictReader(csvfile):
                for item in row.items():
                    k, v = item
                    if k not in MnLBIS.STATS_CAP:
                        MnLBIS.STATS_CAP[k] = [v]
                    MnLBIS.STATS_CAP[k].append(v)

    @staticmethod
    def on_retry():
        return Memory.INVENTORY_RETRY_CLOCKS < delta(Memory.INVENTORY_RETRY_CLOCKS)

    @staticmethod
    def badge_used():
        flag = bit0(0x002b33c1)
        return (
            (Memory.SCREEN_ID_ == 0x6be) & # in battle
            (flag == 1)
        )
        # mario = word(0x002b33c8)
        # luigi = word(0x002b33d8)\
        # return group(
        #     (delta(mario) + delta(luigi) == 0xf0) &
        #     (mario + luigi == 0x0),
        # )

    @staticmethod
    def is_in_battle(
        battle_id: int,
        top_screen_id: int = -1,
        bottom_screen_id: int = -1,
        gauntlet: bool = False,
    ):
        conditions = group(
            (
                (Memory.SCREEN_ID_ == 0x6be) |
                (Memory.SCREEN_ID_ == 0x20b2)
            ) if gauntlet else (
                Memory.SCREEN_ID_ == 0x6be
            ),
            (Memory.BATTLE_ID_ == battle_id),
        )
        if top_screen_id != -1:
            conditions.append((Memory.TOP_SCREEN_AREA_ == top_screen_id))
        if bottom_screen_id != -1:
            conditions.append((Memory.BOTTOM_SCREEN_AREA_ == bottom_screen_id))
        return conditions.with_flag(Flag.NONE)

    @staticmethod
    def on_gauntlet_enter(gauntlet: int):
        battle_ids = {
            1: 0x300b,
            2: 0x300c,
            3: 0x300d,
            4: 0x300e,
            5: 0x300f,
            6: 0x3010,
            7: 0x300b,
        }
        turns = {
            1: 5,
            2: 15,
            3: 18,
            4: 10,
            5: 15,
            6: 12,
            7: 35,
        }
        return (
            (delta(Memory.SCREEN_ID_) == 0x20b2) &
            (Memory.SCREEN_ID_ == 0x06be) &
            (byte(Memory.GAUNTLET__8) == turns[gauntlet]) &
            (Memory.BATTLE_ID_ == battle_ids[gauntlet])
        )


    @staticmethod
    def on_gauntlet_completed(gauntlet: int):
        flag = {
            1: bit1,
            2: bit2,
            3: bit3,
            4: bit4,
            5: bit5,
            6: bit6,
            7: bit7,
        }[gauntlet](Memory.GAUNTLET_)
        return group(
            delta(flag) == 0,
            (Memory.SCREEN_ID_ == 0x20b2) &
            (flag == 1)
        )


    @staticmethod
    def on_enemy_dead(ids: list[int] = [1]):
        enemies = {
            1: Memory.ENEMY_1_HP,
            2: Memory.ENEMY_2_HP,
            3: Memory.ENEMY_3_HP,
            4: Memory.ENEMY_4_HP,
            5: Memory.ENEMY_5_HP,
            6: Memory.ENEMY_6_HP,
        }
        return group(
            group(*[
                or_next(delta(enemies[i]) > 0)
                for i in ids
            ]).with_flag(Flag.NONE),
            group(*[
                and_next(enemies[i] == 0)
                for i in ids
            ]).with_flag(Flag.NONE),
        )

    @staticmethod
    def allowed_equipment(equipments: list[int], actor: int):
        equipments = [0] + equipments
        slots = [Slots.MARIO_LUIGI, Slots.BOWSER][actor]
        return group(
            group(*[
                or_next(slot == id)
                for id in equipments
            ]).with_flag(Flag.NONE)
            for slot in slots
        )

    @staticmethod
    def forbidden_equipment(equipments: list[int], actor: int):
        slots = [Slots.MARIO_LUIGI, Slots.BOWSER][actor]
        return group(*[
            (slot != id)
            for id in equipments
            for slot in slots
        ])

    @staticmethod
    def check_cheated_equipments():
        return group(
            *[
                slot <= Equipment.CHALLENGE_MEDAL
                for slot in Slots.MARIO_LUIGI
            ],
            *[
                (slot == 0x0) | (slot > Equipment.CHALLENGE_MEDAL)
                for slot in Slots.BOWSER
            ]
        )

    @staticmethod
    def is_challenge_medal_equipped():
        slots = [
            Memory.EQUIPMENT_,      # Mario 1
            Memory.EQUIPMENT__1,    # Mario 2
            Memory.EQUIPMENT__2,    # Mario 3
            Memory.EQUIPMENT__3,    # Luigi 1
            Memory.EQUIPMENT__4,    # Luigi 2
            Memory.EQUIPMENT__5,    # Luigi 3
        ]
        return group(*[
            or_next(slot == Equipment.CHALLENGE_MEDAL)
            for slot in slots
        ]).with_flag(Flag.NONE)

    @staticmethod
    def level_cap(lvl: int, actor: int = Actor.ALL):
        def ml_hp_cap(stat):
            return int(stat + lvl * 4 + stat * 0.3)

        def ml_pow_cap(stat):
            return int(stat + lvl/40*80 + lvl/40*54 + stat * 0.5)

        def ml_def_cap(stat):
            return int(stat + lvl/40*150 + stat*0.5)

        def bow_hp_cap(stat):
            return int(stat + lvl * 4 + stat * 0.2)

        def bow_pow_cap(stat):
            return int(stat + lvl/40*30 + lvl/40*54 + stat * 0.5)

        def bow_def_cap(stat):
            return int(stat + lvl/40*300 + stat*0.5)

        ml = [
            Memory.MARIO_LV_RANK_ <= lvl,
            Memory.LUIGI_LV_RANK_ <= lvl,
            Memory.STATISTICS_ < ml_hp_cap(int(MnLBIS.STATS_CAP["Mario HP"][lvl - 1])),
            Memory.STATISTICS__4 < ml_pow_cap(int(MnLBIS.STATS_CAP["Mario POW"][lvl - 1])),
            Memory.STATISTICS__5 < ml_def_cap(int(MnLBIS.STATS_CAP["Mario DEF"][lvl - 1])),
            Memory.STATISTICS__8 < ml_hp_cap(int(MnLBIS.STATS_CAP["Luigi HP"][lvl - 1])),
            Memory.STATISTICS__12 < ml_pow_cap(int(MnLBIS.STATS_CAP["Luigi POW"][lvl - 1])),
            Memory.STATISTICS__13 < ml_def_cap(int(MnLBIS.STATS_CAP["Luigi DEF"][lvl - 1])),
        ]
        bowser = [
            Memory.BOWSER_LV_RANK_ <= lvl,
            Memory.STATISTICS__16 < bow_hp_cap(int(MnLBIS.STATS_CAP["Bowser HP"][lvl - 1])),
            Memory.STATISTICS__20 < bow_pow_cap(int(MnLBIS.STATS_CAP["Bowser POW"][lvl - 1])),
            Memory.STATISTICS__21 < bow_def_cap(int(MnLBIS.STATS_CAP["Bowser DEF"][lvl - 1])),
        ]
        if actor == Actor.MARIO_LUIGI:
            conds = [*ml]
        elif actor == Actor.BOWSER:
            conds = [*bowser]
        else:
            conds = [*ml, *bowser]
        return group(*conds)
