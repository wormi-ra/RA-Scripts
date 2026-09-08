from pycheevos.core.helpers import *
from dataclasses import dataclass

@dataclass(frozen=True)
class Memory:
    ATTACK_PIECES_CURRENT_AREA = (0x056024)
    """
    Attack Pieces: Current Area
    """

    ABILITIES_ = (0x056038)
    """
    Abilities: [Per Bit]
    Bit 0 = Hammer (Luigi: Minimize Mario)
    Bit 1 = Hammer (Mario: Activate/Break Things)
    Bit 2 = Spin (Mario: Long Jump)
    Bit 3 = Drill (Luigi: Into Ground)
    Bit 4 = Flame (Bowser: Breath Fire)
    Bit 5 = Megapunch (Bowser: Punch While Moving)
    Bit 6 = Body Slam (Bowser: Slaming on ground)
    Bit 7 = Spike Ball (Bowser: Rolling on ground)
    """

    SPECIALS_ = (0x05603a)
    """
    Specials: [Per Bit]
    Bit 0 = Green Shell
    Bit 1 = Spin Pipe
    Bit 2 = Yoo Who Cannon
    Bit 3 = Falling Star
    Bit 6 = Jump Helmet
    Bit 7 = Super Bouncer
    """

    SPECIALS__1 = (0x05603b)
    """
    Specials: [Per Bit]
    Bit 3 = Magic Window
    Bit 2 = Snack Basket
    Bit 1 = Fire Flower
    Bit 0 = Mighty Meteor

    Bit 7 = Koopa Corps
    Bit 6 = Shy Guy Squad
    Bit 5 = Bob-omb Blitz
    Bit 4 = Goomba Storm
    """

    SPECIALS__2 = (0x05603c)
    """
    Specials: [Per Bit]
    Bit 2 = Broggy Bonker
    Bit 1 = Magikoopa Mob
    """

    AIRWAY_MINIGAME_BLOCKS_HIT = (0x0561cd)
    """
    Airway Minigame - Blocks hit [Per Bit]
    0 = something else
    1-7 = Block with that number hit
    """

    AIRWAY_MINIGAME_BLOCKS_HIT_1 = (0x0561ce)
    """
    Airway Minigame - Blocks hit [Per Bit]
    0 = Block 8 hit
    """

    SIDEQUEST_HIDE_AND_SEEK_ = (0x0561fb)
    """
    Sidequest: Hide-and-Seek: [Upper4]
    **Toad location
    Note: Use Upper4 as the lower 4 bits are used for something else and could be changed.
    0: Sidequest not started
    1: next to blorbed toad [based on 0x0561fc]
    3: inside Item shop
    5: next to coffee shop
    9: inside boutique
    """

    SIDEQUEST_HIDE_AND_SEEK__1 = (0x0561fc)
    """
    Sidequest: Hide-and-Seek: [Per-Bit]
    (Changes the way 0x0561fc behaves if that address is 1f)
    Bit 0: changes to 1 after boutique location
    Bit 1: changes to 1 once the last location is found
    """

    DIMBLE_WOOD_MEMORY = (0x05620f)
    """
    Dimble Wood Memory? [Per Bit]
    6=If Luigi walks around with a Sockop
    """

    DIMBLE_WOOD_MEMORY_1 = (0x056210)
    """
    Dimble Wood Memory? [Per Bit]
    3 = If Luigi walks around alone
    4 = First !-Block in Sockop Area hit (only small Mario can reach this and gets kidnapped immediately)
    5 = !-Block hit to open the door for Luigi to follow Mario
    """

    DIMBLE_WOOD_MEMORY_2 = (0x056213)
    """
    Dimble Wood Memory? [Per Bit]
    3=Flower shortcut opened in Sockop Area after hitting !-Block
    """

    BLITTIES_IN_INVENTORY_ = (0x05621d)
    """
    Blitties in inventory: [Per-Bit]
    Bit 2: Chuboomba
    Bit 3: Toothy
    Bit 4: Treevil
    Bit 5: Trashure
    Bit 6: Flifit
    Bit 7: Chain Chawful
    """

    BLITTIES_IN_INVENTORY__1 = (0x05621e)
    """
    Blitties in inventory: [Per-Bit]
    Bit 0: Choomba
    Bit 1: Beehoss
    Bit 2: Crawful
    Bit 3: Jailgoon
    Bit 4: Sniffle Thwomp
    Bit 5: Mechawful
    Bit 6: Naplock
    Bit 7: Dark Trashure
    """

    BLITTIES_IN_INVENTORY__2 = (0x05621f)
    """
    Blitties in inventory: [Per-Bit]
    Bit 0: Dark Mechawful
    """

    KUZZLE_JIGSAW_PUZZLES_ = (0x056223)
    """
    Kuzzle Jigsaw Puzzles: [Per Bit]
    Note: Bit 0, 5, 6, 7 seem to be used for unrelated things (maybe if the puzzle got obtained?).
    Bit 1: 2nd Puzzle (sofa-bed)
    Bit 2: 3rd puzzle (table)
    Bit 3: 4th Puzzle (carpet)
    Bit 4: 5th Puzzle (mystery-window)
    """

    CHAKROADS_ = (0x056225)
    """
    Chakroads:
    Bit 7 = Cavi Cape Exit
    Bit 6 = Cavi Cape Cave
    Note: Bits decrease once a chakroad is discovered.
    """

    CHAKROADS__1 = (0x056226)
    """
    Chakroads:
    Bit 0 = Plack Beach
    Bit 1 = Dimble Wood
    Bit 3 = Bowser's Castle
    Bit 4 = Underground Tunnel
    Bit 5 = Lake-Plain Border
    Bit 7 = Peach's Castle
    Note: Bits decrease once a chakroad is discovered.
    """

    CHAKROADS__2 = (0x056227)
    """
    Chakroads:
    Bit 0 = Top of Peach's Castle
    Note: Bits decrease once a chakroad is discovered
    """

    GAUNTLET_ = (0x056273)
    """
    Gauntlet: [Per Bit]
    Which bosses are beaten
    Bit 1: Class 1/Durmite X
    Bit 2: Class 2/Kretin X
    Bit 3: Class 3/Wisdurm X
    Bit 4: Class 4/Bowser Memory X
    Bit 5: Class 5/Junker X
    Bit 6: Class 6/Dark Star X
    Bit 7: Class 7/Bowser X
    """

    ATTACK_PIECES_PUMP_WORKS = (0x0562ca)
    """
    Attack Pieces: Pump Works (Fire Flower)
    """

    ATTACK_PIECES_FLAB_ZONE = (0x0562d0)
    """
    Attack Pieces: Flab Zone (Jump Helmet)
    """

    ATTACK_PIECES_ENERGY_HOLD = (0x0562d4)
    """
    Attack Pieces: Energy Hold (Super Bouncer)
    """

    ATTACK_PIECES_DIMBLE_WOODS = (0x0562dc)
    """
    Attack Pieces: Dimble Woods (Snack Basket)
    """

    ATTACK_PIECES_PEACHS_CASTLE = (0x0562df)
    """
    Attack Pieces: Peachs Castle (Falling Star)
    """

    ATTACK_PIECES_TRASH_PIT = (0x0562e5)
    """
    Attack Pieces: Trash Pit (Green Shell)
    """

    SIDEQUEST_MUSHROOM_BALLS_ = (0x0562e9)
    """
    Sidequest: Mushroom Balls:
    Total Mushroom Balls found
    """

    SIDEQUEST_MUSHROOM_BALLS__1 = (0x0562ea)
    """
    Sidequest: Mushroom Balls:
    Amount of Mushroom Balls opened
    """

    SIDEQUEST_MUSHROOM_BALLS__2 = (0x0562ec)
    """
    Sidequest: Mushroom Balls:
    Amount of Mushroom Balls in inventory
    """

    BEANS_ENERGY_HOLD = (0x0562f6)
    """
    Beans: Energy Hold
    """

    BEANS_AIRWAY = (0x0562f7)
    """
    Beans: Airway
    """

    BEANS_TOAD_TOWN = (0x0562f9)
    """
    Beans: Toad Town
    """

    BEANS_TOAD_TOWN_CAVES = (0x0562fa)
    """
    Beans: Toad Town Caves
    """

    BEANS_BLUBBLE_LAKE = (0x0562fb)
    """
    Beans: Blubble Lake
    """

    BEANS_PLACK_BEACH = (0x0562fc)
    """
    Beans: Plack Beach
    """

    BEANS_DIMBLE_WOOD = (0x0562fd)
    """
    Beans: Dimble Wood
    """

    BEANS_PEACHS_CASTLE = (0x0562fe)
    """
    Beans: Peachs Castle
    """

    BEANS_CAVI_CAPE = (0x0562ff)
    """
    Beans: Cavi Cape
    """

    BEANS_BUMPSY_PLAINS = (0x056300)
    """
    Beans: Bumpsy Plains
    """

    BEANS_BOWSER_PATH = (0x056301)
    """
    Beans: Bowser Path
    """

    BEANS_BOWSER_CASTLE = (0x056302)
    """
    Beans: Bowser Castle
    """

    GAUNTLET__1 = word(0x056350)
    """
    Gauntlet: [16-Bit]
    Class 1/Durmite X Turns (bytes seem to be swapped)
    """

    GAUNTLET__2 = word(0x056352)
    """
    Gauntlet: [16-Bit]
    Class 2/Kretin X Turns (bytes seem to be swapped)
    """

    GAUNTLET__3 = word(0x056354)
    """
    Gauntlet: [16-Bit]
    Class 3/Wisdurm X Turns (bytes seem to be swapped)
    """

    GAUNTLET__4 = word(0x056356)
    """
    Gauntlet: [16-Bit]
    Class 4/Bowser Memory X Turns (bytes seem to be swapped)
    """

    GAUNTLET__5 = word(0x056358)
    """
    Gauntlet: [16-Bit]
    Class 5/Junker X Turns (bytes seem to be swapped)
    """

    GAUNTLET__6 = word(0x05635a)
    """
    Gauntlet: [16-Bit]
    Class 6/Dark Star X Turns (bytes seem to be swapped)
    """

    GAUNTLET__7 = word(0x05635c)
    """
    Gauntlet: [16-Bit]
    Class 7/Bowser X Turns (bytes seem to be swapped)
    """

    GAUNTLET__8 = (0x05635e)
    """
    Gauntlet:
    Current turns left (note: switches value once boss is selected, not once battle starts)
    """

    STATISTICS_ = word(0x05637e)
    """
    Statistics: [16-Bit]
    Mario HP (Total)
    """

    STATISTICS__1 = word(0x056380)
    """
    Statistics: [16-Bit]
    Mario HP (Actual)
    """

    STATISTICS__2 = word(0x056382)
    """
    Statistics: [16-Bit]
    Mario SP (Total)
    """

    STATISTICS__3 = word(0x056384)
    """
    Statistics: [16-Bit]
    Mario SP (Actual)
    """

    STATISTICS__4 = word(0x056386)
    """
    Statistics: [16-Bit]
    Mario POW
    """

    STATISTICS__5 = word(0x056388)
    """
    Statistics: [16-Bit]
    Mario DEF
    """

    STATISTICS__6 = word(0x05638a)
    """
    Statistics: [16-Bit]
    Mario SPEED
    """

    STATISTICS__7 = word(0x05638c)
    """
    Statistics: [16-Bit]
    Mario STACHE
    """

    MARIO_LV_RANK_ = byte(0x056390)
    """
    Mario LV/RANK: [8-Bit]
    6 = Shell
    C = Flower
    12 = Shine
    19 = Star
    28 = Rainbow
    """

    MARIO_EXP = tbyte(0x056391)
    """
    Mario EXP [24-Bit]
    """

    EQUIPMENT_ = byte(0x056398)
    """
    Equipment: [8-Bit]
    Mario Slot 1
    """

    EQUIPMENT__1 = byte(0x056399)
    """
    Equipment: [8-Bit]
    Mario Slot 2
    """

    EQUIPMENT__2 = byte(0x05639a)
    """
    Equipment: [8-Bit]
    Mario Slot 3
    """

    STATISTICS__8 = word(0x0563ae)
    """
    Statistics: [16-Bit]
    Luigi HP (Total)
    """

    STATISTICS__9 = word(0x0563b0)
    """
    Statistics: [16-Bit]
    Luigi HP (Actual)
    """

    STATISTICS__10 = word(0x0563b2)
    """
    Statistics: [16-Bit]
    Luigi SP (Total)
    """

    STATISTICS__11 = word(0x0563b4)
    """
    Statistics: [16-Bit]
    Luigi SP (Actual)
    """

    STATISTICS__12 = word(0x0563b6)
    """
    Statistics: [16-Bit]
    Luigi POW
    """

    STATISTICS__13 = word(0x0563b8)
    """
    Statistics: [16-Bit]
    Luigi DEF
    """

    STATISTICS__14 = word(0x0563ba)
    """
    Statistics: [16-Bit]
    Luigi SPEED
    """

    STATISTICS__15 = word(0x0563bc)
    """
    Statistics: [16-Bit]
    Luigi STACHE
    """

    LUIGI_LV_RANK_ = byte(0x0563c0)
    """
    Luigi LV/RANK: [8-Bit]
    6 = Shell
    C = Flower
    12 = Shine
    19 = Star
    28 = Rainbow
    """

    EQUIPMENT__3 = byte(0x0563c8)
    """
    Equipment: [8-Bit]
    Luigi Slot 1
    """

    EQUIPMENT__4 = byte(0x0563c9)
    """
    Equipment: [8-Bit]
    Luigi Slot 2
    """

    EQUIPMENT__5 = byte(0x0563ca)
    """
    Equipment: [8-Bit]
    Luigi Slot 3
    """

    STATISTICS__16 = word(0x0563de)
    """
    Statistics: [16-Bit]
    Bowser HP (Total)
    """

    STATISTICS__17 = word(0x0563e0)
    """
    Statistics: [16-Bit]
    Bowser HP (Actual)
    """

    STATISTICS__18 = word(0x0563e2)
    """
    Statistics: [16-Bit]
    Bowser SP (Total)
    """

    STATISTICS__19 = word(0x0563e4)
    """
    Statistics: [16-Bit]
    Bowser SP (Actual)
    """

    STATISTICS__20 = word(0x0563e6)
    """
    Statistics: [16-Bit]
    Bowser POW
    """

    STATISTICS__21 = word(0x0563e8)
    """
    Statistics: [16-Bit]
    Bowser DEF
    """

    STATISTICS__22 = word(0x0563ea)
    """
    Statistics: [16-Bit]
    Bowser SPEED
    """

    STATISTICS__23 = word(0x0563ec)
    """
    Statistics: [16-Bit]
    Bowser HORN
    """

    BOWSER_LV_RANK_ = byte(0x0563f0)
    """
    Bowser LV/RANK: [8-Bit]
    A = Silver Boss
    14 = Gold Boss
    28 = Final Boss
    """

    BOWSER_EXP = tbyte(0x0563f1)
    """
    Bowser EXP [24-Bit]
    """

    EQUIPMENT__6 = byte(0x0563f8)
    """
    Equipment: [8-Bit]
    Bowser Slot 1
    """

    EQUIPMENT__7 = byte(0x0563f9)
    """
    Equipment: [8-Bit]
    Bowser Slot 2
    """

    EQUIPMENT__8 = byte(0x0563fa)
    """
    Equipment: [8-Bit]
    Bowser Slot 3
    """

    COINS = dword(0x056400)
    """
    Coins [32-Bit]
    Note: During the Midbus fight, coins gotten by Midbus are added to this as well
    """

    INVENTORY_MUSHROOM = byte(0x056406)
    """
    Inventory: Mushroom [8-Bit]
    """

    INVENTORY_SUPER_MUSHROOM = byte(0x056407)
    """
    Inventory: Super Mushroom [8-Bit]
    """

    INVENTORY_ULTRA_MUSHROOM = byte(0x056408)
    """
    Inventory: Ultra Mushroom [8-Bit]
    """

    INVENTORY_MAX_MUSHROOM = byte(0x056409)
    """
    Inventory: Max Mushroom [8-Bit]
    """

    INVENTORY_HOT_DRUMSTICKS = byte(0x05640a)
    """
    Inventory: Hot Drumsticks [8-Bit]
    """

    INVENTORY_FIERY_DRUMSTICKS = byte(0x05640b)
    """
    Inventory: Fiery Drumsticks [8-Bit]
    """

    INVENTORY_TNT_DRUMSTICKS = byte(0x05640c)
    """
    Inventory: TNT Drumsticks [8-Bit]
    """

    INVENTORY_NUTS = byte(0x05640d)
    """
    Inventory: Nuts [8-Bit]
    """

    INVENTORY_SUPER_NUTS = byte(0x05640e)
    """
    Inventory: Super Nuts [8-Bit]
    """

    INVENTORY_ULTRA_NUTS = byte(0x05640f)
    """
    Inventory: Ultra Nuts [8-Bit]
    """

    INVENTORY_MAX_NUTS = byte(0x056410)
    """
    Inventory: Max Nuts [8-Bit]
    """

    INVENTORY_SYRUP_JARS = byte(0x056411)
    """
    Inventory: Syrup Jars [8-Bit]
    """

    INVENTORY_SUPERSYRUP_JARS = byte(0x056412)
    """
    Inventory: Supersyrup Jars [8-Bit]
    """

    INVENTORY_ULTRASYRUP_JARS = byte(0x056413)
    """
    Inventory: Ultrasyrup Jars [8-Bit]
    """

    INVENTORY_MAX_SYRUP_JARS = byte(0x056414)
    """
    Inventory: Max Syrup Jars [8-Bit]
    """

    INVENTORY_STAR_CANDIES = byte(0x056415)
    """
    Inventory: Star Candies [8-Bit]
    """

    INVENTORY_1_UP_MUSHROOMS = byte(0x056416)
    """
    Inventory: 1-Up Mushrooms [8-Bit]
    """

    INVENTORY_1_UP_DELUXES = byte(0x056417)
    """
    Inventory: 1-Up Deluxes [8-Bit]
    """

    INVENTORY_REFRESHING_HERBS = byte(0x056418)
    """
    Inventory: Refreshing Herbs [8-Bit]
    """

    INVENTORY_DUMMY = byte(0x056419)
    """
    Inventory: DUMMY [8-Bit]
    Note: Unused
    """

    INVENTORY_HEART_BEANS = byte(0x05641a)
    """
    Inventory: Heart Beans [8-Bit]
    """

    INVENTORY_SPECIAL_BEANS = byte(0x05641b)
    """
    Inventory: Special Beans [8-Bit]
    """

    INVENTORY_POWER_BEANS = byte(0x05641c)
    """
    Inventory: Power Beans [8-Bit]
    """

    INVENTORY_RETRY_CLOCKS = byte(0x05641d)
    """
    Inventory: Retry Clocks [8-Bit]
    """

    INVENTORY_DUMMY_1 = byte(0x05641e)
    """
    Inventory: DUMMY [8-Bit]
    Note: Unused
    """

    INVENTORY_DUMMY_2 = byte(0x05641f)
    """
    Inventory: DUMMY [8-Bit]
    Note: Unused
    """

    INVENTORY_THIN_WEAN = byte(0x056427)
    """
    Inventory: Thin Wean [8-Bit]
    """

    INVENTORY_PICNIC_WEAR = byte(0x056428)
    """
    Inventory: Picnic Wear [8-Bit]
    """

    INVENTORY_LEISURE_WEAR = byte(0x056429)
    """
    Inventory: Leisure Wear [8-Bit]
    """

    INVENTORY_FIGHTER_WEAR = byte(0x05642a)
    """
    Inventory: Fighter Wear [8-Bit]
    """

    INVENTORY_HEART_WEAR = byte(0x05642b)
    """
    Inventory: Heart Wear [8-Bit]
    """

    INVENTORY_BRAWNY_WEAR = byte(0x05642c)
    """
    Inventory: Brawny Wear [8-Bit]
    """

    INVENTORY_GROWN_UP_WEAR = byte(0x05642d)
    """
    Inventory: Grown-up Wear [8-Bit]
    """

    INVENTORY_KOOPA_WEAR = byte(0x05642e)
    """
    Inventory: Koopa Wear [8-Bit]
    """

    INVENTORY_HERO_WEAR = byte(0x05642f)
    """
    Inventory: Hero Wear [8-Bit]
    """

    INVENTORY_BALM_WEAR = byte(0x056430)
    """
    Inventory: Balm Wear [8-Bit]
    """

    INVENTORY_MUSCLE_WEAR = byte(0x056431)
    """
    Inventory: Muscle Wear [8-Bit]
    """

    INVENTORY_MASTER_WEAR = byte(0x056432)
    """
    Inventory: Master Wear [8-Bit]
    """

    INVENTORY_KING_WEAR = byte(0x056433)
    """
    Inventory: King Wear [8-Bit]
    """

    INVENTORY_STAR_WEAR = byte(0x056434)
    """
    Inventory: Star Wear [8-Bit]
    """

    INVENTORY_D_STAR_WEAR = byte(0x056435)
    """
    Inventory: D-Star Wear [8-Bit]
    """

    INVENTORY_A_OK_WEAR = byte(0x056436)
    """
    Inventory: A-OK Wear [8-Bit]
    """

    INVENTORY_RENTAL_WEAR = byte(0x056437)
    """
    Inventory: Rental Wear [8-Bit]
    Note: Unused
    """

    INVENTORY_HP_SOCKS = byte(0x056438)
    """
    Inventory: HP Socks [8-Bit]
    """

    INVENTORY_DELUXE_HP_SOCKS = byte(0x056439)
    """
    Inventory: Deluxe HP Socks [8-Bit]
    """

    INVENTORY_SP_SOCKS = byte(0x05643a)
    """
    Inventory: SP Socks [8-Bit]
    """

    INVENTORY_DX_SP_SOCKS = byte(0x05643b)
    """
    Inventory: DX SP Socks [8-Bit]
    """

    INVENTORY_HUSTLE_SOCKS = byte(0x05643c)
    """
    Inventory: Hustle Socks [8-Bit]
    """

    INVENTORY_COIN_SOCKS = byte(0x05643d)
    """
    Inventory: Coin Socks [8-Bit]
    """

    INVENTORY_STARCHED_SOCKS = byte(0x05643e)
    """
    Inventory: Starched Socks [8-Bit]
    """

    INVENTORY_GRUMPTION_SOCKS = byte(0x05643f)
    """
    Inventory: Grumption Socks [8-Bit]
    """

    INVENTORY_BRO_SOCKS = byte(0x056440)
    """
    Inventory: Bro Socks [8-Bit]
    """

    INVENTORY_GALL_SOCKS = byte(0x056441)
    """
    Inventory: Gall Socks [8-Bit]
    """

    INVENTORY_RUGGED_SOCKS = byte(0x056442)
    """
    Inventory: Rugged Socks [8-Bit]
    """

    INVENTORY_EXP_SOCKS = byte(0x056443)
    """
    Inventory: EXP Socks [8-Bit]
    """

    INVENTORY_NO_TOUCH_SOCKS = byte(0x056444)
    """
    Inventory: No-touch Socks [8-Bit]
    """

    INVENTORY_NURSE_SOCKS = byte(0x056445)
    """
    Inventory: Nurse Socks [8-Bit]
    """

    INVENTORY_DOCTOR_SOCKS = byte(0x056446)
    """
    Inventory: Doctor Socks [8-Bit]
    """

    INVENTORY_SPECIAL_SOCKS = byte(0x056447)
    """
    Inventory: Special Socks [8-Bit]
    """

    INVENTORY_SURPRISING_SOCKS = byte(0x056448)
    """
    Inventory: Surprising Socks [8-Bit]
    """

    INVENTORY_GUARDIAN_SOCKS = byte(0x056449)
    """
    Inventory: Guardian Socks [8-Bit]
    """

    INVENTORY_POW_GLOVES = byte(0x05644a)
    """
    Inventory: POW Gloves [8-Bit]
    """

    INVENTORY_DX_POW_GLOVES = byte(0x05644b)
    """
    Inventory: DX POW Gloves [8-Bit]
    """

    INVENTORY_MUSHROOM_GLOVES = byte(0x05644c)
    """
    Inventory: Mushroom Gloves [8-Bit]
    """

    INVENTORY_SPECIAL_GLOVES = byte(0x05644d)
    """
    Inventory: Special Gloves [8-Bit]
    """

    INVENTORY_HEAVY_GLOVES = byte(0x05644e)
    """
    Inventory: Heavy Gloves [8-Bit]
    """

    INVENTORY_DELICIROUS_GLOVES = byte(0x05644f)
    """
    Inventory: Delicirous Gloves [8-Bit]
    """

    INVENTORY_FLOWER_GLOVES = byte(0x056450)
    """
    Inventory: Flower Gloves [8-Bit]
    """

    INVENTORY_BYE_BYE_GLOVES = byte(0x056451)
    """
    Inventory: Bye-Bye Gloves [8-Bit]
    """

    INVENTORY_SOFTENER_GLOVES = byte(0x056452)
    """
    Inventory: Softener Gloves [8-Bit]
    """

    INVENTORY_ITEM_GLOVES = byte(0x056453)
    """
    Inventory: Item Gloves [8-Bit]
    """

    INVENTORY_SIPHON_GLOVES = byte(0x056454)
    """
    Inventory: Siphon Gloves [8-Bit]
    """

    INVENTORY_DENT_GLOVES = byte(0x056455)
    """
    Inventory: Dent Gloves [8-Bit]
    """

    INVENTORY_POW_BOOTS = byte(0x056456)
    """
    Inventory: POW Boots [8-Bit]
    """

    INVENTORY_DX_POW_BOOTS = byte(0x056457)
    """
    Inventory: DX POW Boots [8-Bit]
    """

    INVENTORY_TIP_TOP_BOOTS = byte(0x056458)
    """
    Inventory: Tip-Top Boots [8-Bit]
    """

    INVENTORY_SPECIAL_BOOTS = byte(0x056459)
    """
    Inventory: Special Boots [8-Bit]
    """

    INVENTORY_HEAVY_BOOTS = byte(0x05645a)
    """
    Inventory: Heavy Boots [8-Bit]
    """

    INVENTORY_DAREDEVIL_BOOTS = byte(0x05645b)
    """
    Inventory: Daredevil Boots [8-Bit]
    """

    INVENTORY_SHELL_BOOTS = byte(0x05645c)
    """
    Inventory: Shell Boots [8-Bit]
    """

    INVENTORY_DIZZY_BOOTS = byte(0x05645d)
    """
    Inventory: Dizzy Boots [8-Bit]
    """

    INVENTORY_SHROOB_BOOTS = byte(0x05645e)
    """
    Inventory: Shroob Boots [8-Bit]
    """

    INVENTORY_COIN_BOOTS = byte(0x05645f)
    """
    Inventory: Coin Boots [8-Bit]
    """

    INVENTORY_SIPHON_BOOTS = byte(0x056460)
    """
    Inventory: Siphon Boots [8-Bit]
    """

    INVENTORY_BIG_STOMP_BOOTS = byte(0x056461)
    """
    Inventory: Big Stomp Boots [8-Bit]
    """

    INVENTORY_HAPPY_CHARMS = byte(0x056462)
    """
    Inventory: Happy Charms [8-Bit]
    """

    INVENTORY_LUCK_CHARMS = byte(0x056463)
    """
    Inventory: Luck Charms [8-Bit]
    """

    INVENTORY_THRIFT_CHARMS = byte(0x056464)
    """
    Inventory: Thrift Charms [8-Bit]
    """

    INVENTORY_BUDGET_CHARMS = byte(0x056465)
    """
    Inventory: Budget Charms [8-Bit]
    """

    INVENTORY_TIGHT_BELTS = byte(0x056466)
    """
    Inventory: Tight Belts [8-Bit]
    """

    INVENTORY_ADVICE_PATCHES = byte(0x056467)
    """
    Inventory: Advice Patches [8-Bit]
    """

    INVENTORY_LUXURY_PARCHES = byte(0x056468)
    """
    Inventory: Luxury Parches [8-Bit]
    """

    INVENTORY_HEROIC_PATCHES = byte(0x056469)
    """
    Inventory: Heroic Patches [8-Bit]
    """

    INVENTORY_SMALL_SHELLS = byte(0x05646a)
    """
    Inventory: Small Shells [8-Bit]
    """

    INVENTORY_BIG_SHELLS = byte(0x05646b)
    """
    Inventory: Big Shells [8-Bit]
    """

    INVENTORY_GIANT_SHELLS = byte(0x05646c)
    """
    Inventory: Giant Shells [8-Bit]
    """

    INVENTORY_KO_SHELLS = byte(0x05646d)
    """
    Inventory: KO Shells [8-Bit]
    """

    INVENTORY_GOLD_RINGS = byte(0x05646e)
    """
    Inventory: Gold Rings [8-Bit]
    """

    INVENTORY_GOLD_CROWNS = byte(0x05646f)
    """
    Inventory: Gold Crowns [8-Bit]
    """

    INVENTORY_LAZY_SCARVES = byte(0x056470)
    """
    Inventory: Lazy Scarves [8-Bit]
    """

    INVENTORY_MUSHROOM_STONES = byte(0x056471)
    """
    Inventory: Mushroom Stones [8-Bit]
    """

    INVENTORY_POW_MUSH_JAMS = byte(0x056472)
    """
    Inventory: POW Mush Jams [8-Bit]
    """

    INVENTORY_DEF_MUSH_JAMS = byte(0x056473)
    """
    Inventory: DEF Mush Jams [8-Bit]
    """

    INVENTORY_TRASURE_SPECS = byte(0x056474)
    """
    Inventory: Trasure Specs [8-Bit]
    """

    INVENTORY_VENGEANCE_CAPES = byte(0x056475)
    """
    Inventory: Vengeance Capes [8-Bit]
    """

    INVENTORY_CHALLENGE_MEDALS = byte(0x056476)
    """
    Inventory: Challenge Medals [8-Bit]
    """

    INVENTORY_SHABBY_SHELLS = byte(0x056477)
    """
    Inventory: Shabby Shells [8-Bit]
    """

    INVENTORY_SPECIAL_SHELLS = byte(0x056478)
    """
    Inventory: Special Shells [8-Bit]
    """

    INVENTORY_SAFETY_SHELLS = byte(0x056479)
    """
    Inventory: Safety Shells [8-Bit]
    """

    INVENTORY_JUDGE_SHELLS = byte(0x05647a)
    """
    Inventory: Judge Shells [8-Bit]
    """

    INVENTORY_ROCK_SHELLS = byte(0x05647b)
    """
    Inventory: Rock Shells [8-Bit]
    """

    INVENTORY_ARMORED_SHELLS = byte(0x05647c)
    """
    Inventory: Armored Shells [8-Bit]
    """

    INVENTORY_RAMPAGE_SHELLS = byte(0x05647d)
    """
    Inventory: Rampage Shells [8-Bit]
    """

    INVENTORY_DREAM_SHELLS = byte(0x05647e)
    """
    Inventory: Dream Shells [8-Bit]
    """

    INVENTORY_WICKED_SHELLS = byte(0x05647f)
    """
    Inventory: Wicked Shells [8-Bit]
    """

    INVENTORY_IRONCLAD_SHELLS = byte(0x056480)
    """
    Inventory: Ironclad Shells [8-Bit]
    """

    INVENTORY_BLOCK_RINGS = byte(0x056481)
    """
    Inventory: Block Rings [8-Bit]
    """

    INVENTORY_KING_SHELLS = byte(0x056482)
    """
    Inventory: King Shells [8-Bit]
    """

    INVENTORY_POWER_BANDS = byte(0x056483)
    """
    Inventory: Power Bands [8-Bit]
    """

    INVENTORY_POWER_BANDS_1 = byte(0x056484)
    """
    Inventory: Power Bands + [8-Bit]
    """

    INVENTORY_MINION_BANDS = byte(0x056485)
    """
    Inventory: Minion Bands [8-Bit]
    """

    INVENTORY_MINION_BANDS_SP = byte(0x056486)
    """
    Inventory: Minion Bands SP [8-Bit]
    """

    INVENTORY_IRON_FIST_BANDS = byte(0x056487)
    """
    Inventory: Iron Fist Bands [8-Bit]
    """

    INVENTORY_VAMPIRE_BANDS = byte(0x056488)
    """
    Inventory: Vampire Bands [8-Bit]
    """

    INVENTORY_STAMINA_BANDS = byte(0x056489)
    """
    Inventory: Stamina Bands [8-Bit]
    """

    INVENTORY_HUNTER_BANDS = byte(0x05648a)
    """
    Inventory: Hunter Bands [8-Bit]
    """

    INVENTORY_LUCKY_BANDS = byte(0x05648b)
    """
    Inventory: Lucky Bands [8-Bit]
    """

    INVENTORY_BLOCK_BANDS = byte(0x05648c)
    """
    Inventory: Block Bands [8-Bit]
    """

    INVENTORY_FURY_BANDS = byte(0x05648d)
    """
    Inventory: Fury Bands [8-Bit]
    """

    INVENTORY_POWER_FANGS = byte(0x05648e)
    """
    Inventory: Power Fangs [8-Bit]
    """

    INVENTORY_POWER_FANGS_X = byte(0x05648f)
    """
    Inventory: Power Fangs X [8-Bit]
    """

    INVENTORY_SPECIAL_FANGS = byte(0x056490)
    """
    Inventory: Special Fangs [8-Bit]
    """

    INVENTORY_SPECIAL_FANGS_X = byte(0x056491)
    """
    Inventory: Special Fangs X [8-Bit]
    """

    INVENTORY_RED_HOT_FANGS = byte(0x056492)
    """
    Inventory: Red-hot Fangs [8-Bit]
    """

    INVENTORY_BURNING_FANGS = byte(0x056493)
    """
    Inventory: Burning Fangs [8-Bit]
    """

    INVENTORY_FURY_FANGS = byte(0x056494)
    """
    Inventory: Fury Fangs [8-Bit]
    """

    INVENTORY_BONE_FANGS = byte(0x056495)
    """
    Inventory: Bone Fangs [8-Bit]
    """

    INVENTORY_INTRUDER_FANGS = byte(0x056496)
    """
    Inventory: Intruder Fangs [8-Bit]
    """

    INVENTORY_BLOCK_FANGS = byte(0x056497)
    """
    Inventory: Block Fangs [8-Bit]
    """

    INVENTORY_FLASHY_FANGS = byte(0x056498)
    """
    Inventory: Flashy Fangs [8-Bit]
    """

    INVENTORY_CHEAP_RINGS = byte(0x056499)
    """
    Inventory: Cheap Rings [8-Bit]
    """

    INVENTORY_ECONOMY_RINGS = byte(0x05649a)
    """
    Inventory: Economy Rings [8-Bit]
    """

    INVENTORY_HEROIC_RINGS = byte(0x05649b)
    """
    Inventory: Heroic Rings [8-Bit]
    """

    INVENTORY_GLUTTON_RINGS = byte(0x05649c)
    """
    Inventory: Glutton Rings [8-Bit]
    """

    INVENTORY_EXCELLENT_RINGS = byte(0x05649d)
    """
    Inventory: Excellent Rings [8-Bit]
    """

    INVENTORY_DRUMSTICK_RINGS = byte(0x05649e)
    """
    Inventory: Drumstick Rings [8-Bit]
    """

    INVENTORY_PEACE_RINGS = byte(0x05649f)
    """
    Inventory: Peace Rings [8-Bit]
    """

    INVENTORY_FILL_UP_RINGS = byte(0x0564a0)
    """
    Inventory: Fill-up Rings [8-Bit]
    """

    INVENTORY_RESTORE_RINGS = byte(0x0564a1)
    """
    Inventory: Restore Rings [8-Bit]
    """

    INVENTORY_FAST_CASH_RINGS = byte(0x0564a2)
    """
    Inventory: Fast Cash Rings [8-Bit]
    """

    INVENTORY_TREASURE_RINGS = byte(0x0564a3)
    """
    Inventory: Treasure Rings [8-Bit]
    """

    INVENTORY_SAFETY_RINGS = byte(0x0564a4)
    """
    Inventory: Safety Rings [8-Bit]
    """

    INVENTORY_HARD_RINGS = byte(0x0564a5)
    """
    Inventory: Hard Rings [8-Bit]
    """

    INVENTORY_RENTAL_SHELL = byte(0x0564a6)
    """
    Inventory: Rental Shell [8-Bit]
    Note: Unused
    """

    INVENTORY_BADGES = (0x0564a7)
    """
    Inventory: Badges
    Bit 0 = Mario Mushroom Badge
    Bit 1 = Mario Powerful Badge
    Bit 2 = Mario Bonus Badge
    Bit 3 = Mario Bro Badge
    Bit 4 = Luigi Good Badge
    Bit 5 = Luigi Great Badge
    Bit 6 = Luigi Excellent! Badge
    Bit 7 = Luigi Excellent!! Badge
    """

    PLAYTIME = dword(0x0564b4)
    """
    Playtime [32-Bit]
    """

    CHALLENGE_NODE_ = word(0x0564cc)
    """
    Challenge Node: [16-Bit]
    Green Shell High Score
    B: 100
    A: 150
    """

    CHALLENGE_NODE__1 = word(0x0564ce)
    """
    Challenge Node: [16-Bit]
    Yoo Who Cannon High Score
    B: 80
    A: 120
    """

    CHALLENGE_NODE__2 = word(0x0564d0)
    """
    Challenge Node: [16-Bit]
    Super Bouncer High Score
    B: 20
    A: 30
    """

    CHALLENGE_NODE__3 = word(0x0564d2)
    """
    Challenge Node: [16-Bit]
    Spin Pipe High Score
    B: 20
    A: 30
    """

    CHALLENGE_NODE__4 = word(0x0564d4)
    """
    Challenge Node: [16-Bit]
    Magic Window High Score
    B: 70
    A: 120
    """

    CHALLENGE_NODE__5 = word(0x0564d6)
    """
    Challenge Node: [16-Bit]
    Jump Helmet High Score
    B: 30 (25 in JP)
    A: 60 (50 in JP)
    """

    BROQUE_MADAME_ = word(0x0564d8)
    """
    Broque Madame: [16-Bit]
    Goomba Storm High Score
    B: 150
    A: 250
    """

    BROQUE_MADAME__1 = word(0x0564da)
    """
    Broque Madame: [16-Bit]
    Koopa Corps High Score
    B: 250
    A: 350
    """

    BROQUE_MADAME__2 = word(0x0564dc)
    """
    Broque Madame: [16-Bit]
    Bob-Omb Blitz High Score
    B: 120
    A: 150
    """

    BROQUE_MADAME__3 = word(0x0564de)
    """
    Broque Madame: [16-Bit]
    Magikoopa Mob High Score
    B: 200
    A: 300
    """

    BATTLE_ID_ = word(0x0564e0)
    """
    Battle ID: [16-Bit]
    All Battle IDs used are listed here: https://github.com/blueYOSHI9000/RetroAchievements-stuff/blob/main/NDS%20-%20Mario%20Luigi%20Bowsers%20Inside%20Story/Room%20IDs%20%26%20Battle%20IDs%20%26%20Stage%20IDs.txt
    """

    STAGE_ID_ = word(0x0564e2)
    """
    Stage ID: [16-Bit]
    All Stage IDs used are listed here: https://github.com/blueYOSHI9000/RetroAchievements-stuff/blob/main/NDS%20-%20Mario%20Luigi%20Bowsers%20Inside%20Story/Room%20IDs%20%26%20Battle%20IDs%20%26%20Stage%20IDs.txt
    """

    CHALLENGE_NODE_BROQUE_MADAME_ = byte(0x0564e6)
    """
    Challenge Node/Broque Madame: [8-Bit]
    Attack selected
    1c = Green Shell
    1d = Yoo Who Cannon
    1e = Super Bouncer
    1f = Spin Pipe
    20 = Magic Window
    22 = Jump Helmet

    24 = Goomba Storm
    25 = Koopa Corps
    26 = Bob-Omb Blitz
    27 = Magikoopa Mob

    Following are used in the pause menu when practising:
    00 = Green Shell (also used when on the menu)
    01 = Fire Flower
    02 = Jump Helmet
    03 = Yoo Who Cannon
    04 = Super Bouncer
    05 = Mighty Meteor
    06 = Spin Pipe
    07 = Snack Basket
    08 = Magic Window
    10 = Falling Star

    0a = Goomba Storm
    0b = Shy Guy Squad
    0c = Koopa Corps
    0d = Bob-Omb Blitz
    0e = Magikoopa Mob
    0f = Broggy Bonker
    """

    PRACTISE = (0x0564e7)
    """
    Practise [Bit 4]
    0 = Not practising
    1 = Practising Special Attacks in pause menu
    """

    BUTTONS_PRESSED_ = (0x05650c)
    """
    Buttons pressed: [Per Bit]
    0: A
    1: B

    D-Pad:
    4: Right
    5: Left
    6: Up
    7: Down
    """

    BUTTONS_PRESSED__1 = (0x05650d)
    """
    Buttons pressed: [Per Bit]
    Only tested in Lumbar Nook.
    0: R
    1: L
    2: X
    3: Y
    """

    BATTLE_RESULT_SCREEN = (0x056fa3)
    """
    Battle result screen? [Bit 0]
    0: In Battle/Overworld/basically anything else
    1: Battle Result screen
    """

    GAUNTLET__9 = byte(0x05af98)
    """
    Gauntlet: [8-Bit]
    Turns left
    """

    JIGSAW_PUZZLE_ = (0x077748)
    """
    Jigsaw Puzzle:
    1
    """

    JIGSAW_PUZZLE__1 = (0x077750)
    """
    Jigsaw Puzzle:
    2
    """

    JIGSAW_PUZZLE__2 = (0x077758)
    """
    Jigsaw Puzzle:
    3
    """

    JIGSAW_PUZZLE__3 = (0x077760)
    """
    Jigsaw Puzzle:
    4
    """

    JIGSAW_PUZZLE__4 = (0x077768)
    """
    Jigsaw Puzzle:
    5
    """

    JIGSAW_PUZZLE__5 = (0x077770)
    """
    Jigsaw Puzzle:
    6
    """

    JIGSAW_PUZZLE__6 = (0x077778)
    """
    Jigsaw Puzzle:
    7
    """

    JIGSAW_PUZZLE__7 = (0x077780)
    """
    Jigsaw Puzzle:
    8
    """

    JIGSAW_PUZZLE__8 = (0x077788)
    """
    Jigsaw Puzzle:
    9
    """

    JIGSAW_PUZZLE__9 = (0x077790)
    """
    Jigsaw Puzzle:
    10
    """

    JIGSAW_PUZZLE__10 = (0x077798)
    """
    Jigsaw Puzzle:
    11
    """

    JIGSAW_PUZZLE__11 = (0x0777a0)
    """
    Jigsaw Puzzle:
    12
    """

    JIGSAW_PUZZLE__12 = (0x0777a8)
    """
    Jigsaw Puzzle:
    13
    """

    JIGSAW_PUZZLE__13 = (0x0777b0)
    """
    Jigsaw Puzzle:
    14
    """

    JIGSAW_PUZZLE__14 = (0x0777b8)
    """
    Jigsaw Puzzle:
    15
    """

    JIGSAW_PUZZLE__15 = (0x0777c0)
    """
    Jigsaw Puzzle:
    16
    """

    JIGSAW_PUZZLE__16 = (0x0777c8)
    """
    Jigsaw Puzzle:
    17
    """

    JIGSAW_PUZZLE__17 = (0x0777d0)
    """
    Jigsaw Puzzle:
    18
    """

    JIGSAW_PUZZLE__18 = (0x0777d8)
    """
    Jigsaw Puzzle:
    19
    """

    JIGSAW_PUZZLE__19 = (0x0777e0)
    """
    Jigsaw Puzzle:
    20
    """

    JIGSAW_PUZZLE__20 = (0x0777e8)
    """
    Jigsaw Puzzle:
    21
    """

    JIGSAW_PUZZLE__21 = (0x0777f0)
    """
    Jigsaw Puzzle:
    22
    """

    JIGSAW_PUZZLE__22 = (0x0777f8)
    """
    Jigsaw Puzzle:
    23
    """

    JIGSAW_PUZZLE__23 = (0x077800)
    """
    Jigsaw Puzzle:
    24
    """

    JIGSAW_PUZZLE__24 = (0x077808)
    """
    Jigsaw Puzzle:
    25
    """

    JIGSAW_PUZZLE__25 = (0x077810)
    """
    Jigsaw Puzzle:
    26
    """

    JIGSAW_PUZZLE__26 = (0x077818)
    """
    Jigsaw Puzzle:
    27
    """

    JIGSAW_PUZZLE__27 = (0x077820)
    """
    Jigsaw Puzzle:
    28
    """

    JIGSAW_PUZZLE__28 = (0x077828)
    """
    Jigsaw Puzzle:
    29
    """

    JIGSAW_PUZZLE__29 = (0x077830)
    """
    Jigsaw Puzzle:
    30
    """

    MIC_LOUDNESS = word(0x084abd)
    """
    Mic Loudness [16-Bit]
    Only works on the Mic Test screen
    Seems broken? I dunno, cheevo got tickets when using this
    """

    SCREEN_ID_ = word(0x085a48)
    """
    Screen ID: [16-Bit]
    04e4: Overworld
    06be: Battle & Challenge Node menu

    ????: Staff credits (random trash is displayed during credits)
    0000: Puzzles
    4284: Booting up the game
    6750: Titlescreen
    4545: File Select
    0214: Mic Test
    3044: Pause menu
    1b41: Shop menu
    20b2: Gauntlet menu
    """

    SCREEN_ID__1 = byte(0x085a49)
    """
    Screen ID: [8-Bit]
    04: Overworld
    06: Battle (incl. Giant fights) & Challenge Node menu

    00: Staff credits & Puzzles
    42: Booting up the game
    67: Titlescreen
    45: File Select
    02: Mic Test
    30: Pause menu
    1b: Shop menu
    20: Gauntlet menu
    """

    BONUS_COIN_GET = (0x0b4005)
    """
    Bonus Coin Get
    """

    BONUS_CARD = (0x0b401a)
    """
    Bonus Card?
    """

    SHOP_COIN_SPENT_ = dword(0x0b401c)
    """
    Shop Coin Spent: [32-Bit]
    """

    SHOP_BONUS_CARD_ = byte(0x0b402c)
    """
    Shop Bonus Card: [8-Bit]
    00 = nothing gotten yet
    01 = Star (40%)
    02 = Flower (20%)
    03 = Mushroom (10%)
    FF = Fawful (0%)
    """

    CHALLENGE_NODE__6 = word(0x0d10c0)
    """
    Challenge Node: [16-Bit]
    Green Shell Score Counter (resets once minigame is over)
    """

    BROQUE_MADAME__4 = word(0x0d5128)
    """
    Broque Madame: [16-Bit]
    Bob-Omb Blitz Score (resets after challenge)
    """

    BROQUE_MADAME__5 = word(0x0d7e3c)
    """
    Broque Madame: [16-Bit]
    Koopa Corps Score (resets after challenge)
    """

    CHALLENGE_NODE__7 = word(0x0d870c)
    """
    Challenge Node: [16-Bit]
    Spin Pipe Score Counter (resets once minigame is over)
    """

    BROQUE_MADAME__6 = word(0x0d8b78)
    """
    Broque Madame: [16-Bit]
    Magikoopa Mob Score (resets after challenge)
    """

    BROQUE_MADAME__7 = word(0x0d8d28)
    """
    Broque Madame: [16-Bit]
    Goomba Storm Score (resets after challenge)
    """

    CHALLENGE_NODE__8 = word(0x0d9034)
    """
    Challenge Node: [16-Bit]
    Magic Window Score Counter (resets once minigame is over)
    """

    CHALLENGE_NODE__9 = word(0x0d9d10)
    """
    Challenge Node: [16-Bit]
    Super Bouncer Score Counter (resets once minigame is over)
    """

    CHALLENGE_NODE__10 = word(0x0da2f8)
    """
    Challenge Node: [16-Bit]
    Yoo Who Cannon Score Counter (resets once minigame is over)
    """

    GIANT_BOWSERS_BATTLE_BLOCK_ = byte(0x0db9b5)
    """
    Giant Bowsers Battle Block: [8-Bit]
    Value stays throughout the enemies attack.
    0f = can select, but nothing selected yet
    00 = punch (also at the start of the battle)
    01 = fire
    02 = mushroom
    """

    GIGA_BATTLE_TIMER = dword(0x0dba20)
    """
    Giga Battle Timer? [32-Bit]
    """

    BOSS_STATE_ = byte(0x0e0ba4)
    """
    Boss state: [8-Bit]
    **Fawful Express
    Distance left to final station, starts at 64 and ends at 00
    """

    CHALLENGE_NODE_BROQUE_MADAME__1 = byte(0x0eff5b)
    """
    Challenge Node/Broque Madame: [8-Bit]
    00 = challenge not started
    02 = challenge started
    """

    TOWER_OF_YIKK_X_POSITION_ = word(0x0f0845)
    """
    Tower of Yikk X Position: [16-Bit]
    Lowest number is on the left, highest on the right. Duplicate of 0x0f0855, 0x0f087d, 0x0f0889.
    fd90 = jumping on Bowser (overflows over 0000)
    001e = About the lowest you can get without falling into the water (roughly)
    079e = Starting Position
    0860 = Tower is in the water
    """

    CHALLENGE_NODE__11 = byte(0x0f1b6c)
    """
    Challenge Node: [8-Bit]
    Jump Helmet score display? (only counts up to 9, then wraps around to 0 - not ideal but it is consistent in all available languages - there does not seem to be an actual score value like the other attacks)
    """

    BATTLE_TIMER = dword(0x0f6468)
    """
    Battle Timer? [32-Bit]
    """

    BOSS_STATE__1 = byte(0x0f97ec)
    """
    Boss state: [8-Bit]
    **Fawful Express
    Distance left, will stop at 01, but will change to c8 past the final station
    """

    GAUNTLET__10 = byte(0x0f9800)
    """
    Gauntlet: [8-Bit]
    Boss selected (Note: stays the same after battle)
    Boss Rush uses whatever Boss is on-screen at the moment
    FF = transitioning to battle
    15 = Durmite X
    20 = Kretin X
    17 = Wisdurm X
    19 = Bowser Memory X
    22 = Junker X
    1B = Dark Star X
    81 = Bowser X
    """

    BOSS_STATE__2 = byte(0x10a49c)
    """
    Boss State: [8-Bit]
    **Bowser
    Note: Address changes during certain attacks & counters
    Note 2: If Luigi is dead and Mario hooks 08 is still used
    08 = Mario hooked first
    0a = Mario hooked second
    """

    BOSS_STATE__3 = byte(0x10a660)
    """
    Boss State: [8-Bit]
    **Bowser
    Note: Address changes during certain attacks & counters
    Note 2: If Mario is dead and Luigi hooks 08 is still used
    08 = Luigi hooked first
    0a = Luigi hooked second
    """

    GIGA_BOWSER_HP = word(0x10e12e)
    """
    Giga Bowser HP [16-Bit]
    Amount of HP isn't always the same (not sure if fixed per fight though).
    """

    GIGA_ENEMY_1_HP = (0x10e426)
    """
    Giga Enemy 1 HP
    """

    GIGA_ENEMY_2_HP = (0x10e54a)
    """
    Giga Enemy 2 HP
    """

    BOSS_STATE__4 = byte(0x11338c)
    """
    Boss state: [8-Bit]
    **Bowser
    Note: 56 is briefly used while Starlow appears, then 01 is used while the text-box is on-screen (if there is a text-box), then 60 is used briefly, then finally it switches to 00 which is when the player starts to be able to hook on Starlow.
    tl;dr: 56 > (01 >) > 60 > 00 -- Everything before 00 is cutscene
    Note 2: 00 is also used outside of the Starlow sequences during the fight

    00: Luigi not hooked
    01: Luigi hooked
    33: Bowser spits fire
    """

    BOSS_STATE__5 = byte(0x113740)
    """
    Boss state: [8-Bit]
    **Bowser
    Whos hooked on Starlow (Note: If a character got hooked, then got released and hooked again then the address will display it like they were the second character to get hooked)
    01: Mario first
    02: Luigi first
    05: Luigi first & Mario
    06: Mario first & Luigi
    """

    BOSS_STATE__6 = byte(0x126224)
    """
    Boss State: [8-Bit]
    **Midbus 2
    00 = Bowser's Ovation
    01 = Midbus' Ovation
    """

    WISDURM_METER_ = dword(0x126228)
    """
    Wisdurm Meter: [32-Bits]
    Min = 0
    Max = 14000
    """

    BOSS_STATE__7 = byte(0x126230)
    """
    Boss State: [8-Bit]
    **Keratin
    00 = No Duplication/Merged together
    01 = Has Duplicated
    """

    BOSS_STATE__8 = byte(0x126234)
    """
    Boss State: [8-Bit]
    **Bowser 2
    00 = Idle
    01 = Attacking
    02 = Flames
    """

    BOSS_STATE__9 = byte(0x12623c)
    """
    Boss State: [8-Bit]
    **Keratin
    0-5 = Assembled
    6 = Disassembled
    Note: Increase when a part of Alpha Keratin has been defeated.
    """

    VAR_1 = (0x12624c)
    """
    1
    """

    VAR_2 = (0x126250)
    """
    2
    """

    VAR_3 = (0x126254)
    """
    3
    """

    VAR_4 = (0x126258)
    """
    4
    """

    VAR_5 = (0x12625c)
    """
    5
    """

    VAR_6 = (0x126260)
    """
    6
    """

    BOSS_STATE__10 = byte(0x126264)
    """
    Boss State: [8-Bit]
    **Sea Pipe Statue
    (Note: this can only change the following way: 0 > 1 > 2 > 0 > repeat)
    0 = Idle (with head)
    1 = Headless (inside Bowser)
    2 = Stuck
    **Blizzard Midbus
    Snow/Snawful counter
    """

    BOSS_STATE__11 = byte(0x126274)
    """
    Boss State: [8-Bit]
    **Junker
    0 = Luigi not caught
    1-5 = which trash can Luigi is caught in
    """

    BOSS_STATE__12 = byte(0x1262e8)
    """
    Boss State: [8-Bit]
    **Scutlet
    Note: switches to 00 before attack, sometimes after an attack as well
    00 = No Damage
    01 = Counter Attack
    02 = Defleted Starlow
    """

    WIGGLER_HARMED_BY_RADDISH = (0x12632c)
    """
    Wiggler harmed by raddish?
    """

    MARIOS_HP = word(0x127906)
    """
    Mario's HP [16-Bit]
    """

    MARIOS_SP = word(0x12790a)
    """
    Mario's SP [16-Bit]
    """

    BATTLE_ = word(0x127928)
    """
    Battle: [16-Bit]
    Mario Attack Animation?
    Note: This is always 0000 unless Mario is attacking
    """

    MARIOS_BATTLE_BLOCK_ = byte(0x127af6)
    """
    Mario's Battle Block: [8-Bit]
    01 = Jump
    """

    LUIGIS_HP = word(0x127c1a)
    """
    Luigi's HP [16-Bits]
    """

    LUIGIS_SP = word(0x127c1e)
    """
    Luigi's SP [16-Bit]
    """

    BATTLE__1 = word(0x127c3c)
    """
    Battle: [16-Bit]
    Luigi Attack Animation?
    Note: This is always 0000 unless Luigi is attacking
    """

    ALLY_BLOCK = (0x127e0a)
    """
    Ally Block?!
    01 = Jump
    """

    BOWSERS_HP = word(0x127f2e)
    """
    Bowser's HP [16-Bit]
    """

    BOWSERS_BATTLE_BLOCK_ = byte(0x12811e)
    """
    Bowsers Battle Block: [8-Bit]
    Note: Always switches to 00 at the start of a battle
    9 = Inhale
    7 = Flame
    6 = Puch
    5 = Special
    4 = Item
    3 = Flee
    """

    TURN_NUMBER_ = (0x128202)
    """
    Turn Number:
    Increase each enemy turn.
    Decrease to 00 if retry clock used.
    """

    ENEMY_1_MAX_HP = word(0x128224)
    """
    Enemy 1 Max HP [16-Bit]
    """

    ENEMY_1_HP = word(0x128226)
    """
    Enemy 1 HP [16-Bit]
    """

    ENEMY_1 = (0x12822e)
    """
    Enemy 1 (defense?)
    """

    INSTANT_WIN = (0x12823c)
    """
    Instant Win (Enemy 1) = 01
    """

    BOSS_STATE__13 = (0x128262)
    """
    Boss State: [Bit 2]
    **Dark Star
    0=no shield
    1=shield up, immune to damage
    """

    ENEMY_2_MAX_HP = word(0x128348)
    """
    Enemy 2 Max HP? [16-Bit]
    """

    ENEMY_2_HP = word(0x12834a)
    """
    Enemy 2 HP [16-Bit]
    """

    ENEMY_2 = (0x128352)
    """
    Enemy 2 (defense?)
    """

    INSTANT_WIN_1 = (0x128360)
    """
    Instant Win (Enemy 2) = 01
    """

    BOSS_STATE__14 = byte(0x12836b)
    """
    Boss State: [8-Bit]
    **Dark Star
    Top Dark Satellmite state (Enemy 2)
    02 = alive/broken
    00 = gone (after attack)
    """

    ENEMY_3_MAX_HP = word(0x12846c)
    """
    Enemy 3 Max HP? [16-Bit]
    """

    ENEMY_3_HP = word(0x12846e)
    """
    Enemy 3 HP? [16-Bit]
    """

    ENEMY_3 = (0x128476)
    """
    Enemy 3 (defense?)
    """

    BOSS_STATE__15 = byte(0x12848f)
    """
    Boss State: [8-Bit]
    **Dark Star
    Bottom Dark Satellmite state (Enemy 3)
    02 = alive/broken
    00 = gone (after attack)
    """

    ENEMY_4_MAX_HP = word(0x128590)
    """
    Enemy 4 Max HP [16-Bit]
    """

    ENEMY_4_HP = word(0x128592)
    """
    Enemy 4 HP? [16-Bit]
    """

    ENEMY_4 = (0x12859a)
    """
    Enemy 4 (defense?)
    """

    ENEMY_5_MAX_HP = word(0x1286b4)
    """
    Enemy 5 Max HP [16-Bit]
    """

    ENEMY_5_HP = word(0x1286b6)
    """
    Enemy 5 HP? [16-Bit]
    """

    ENEMY_6_MAX_HP = word(0x1287d8)
    """
    Enemy 6 Max HP [16-Bit]
    """

    ENEMY_6_HP = word(0x1287da)
    """
    Enemy 6 HP? [16-Bit]
    """

    TOP_SCREEN_INHALED_ENEMY_1_ = word(0x128a20)
    """
    Top Screen/Inhaled Enemy #1: [16-Bit]
    Max HP
    """

    TOP_SCREEN_INHALED_ENEMY_1__1 = word(0x128a22)
    """
    Top Screen/Inhaled Enemy #1: [16-Bit]
    HP
    """

    TOP_SCREEN_INHALED_ENEMY_1__2 = word(0x128a28)
    """
    Top Screen/Inhaled Enemy #1: [16-Bit]
    POW?
    """

    TOP_SCREEN_INHALED_ENEMY_1__3 = word(0x128a2a)
    """
    Top Screen/Inhaled Enemy #1: [16-Bit]
    DEF
    """

    VAR_00_NO_TEXT_ON_SCREEN = (0x12ad02)
    """
    00: no text on-screen
    """

    CAMERA_Y_POSITION = word(0x153dd7)
    """
    Camera Y Position [16-Bit]
    Only tested in in Lumbar Nook. Maybe 8-Bit?
    During the tea session it will go down to 4100, if the password is entered it even goes down to 4000.
    """

    CHALLENGE_NODE__12 = byte(0x16a613)
    """
    Challenge Node: [8-Bit]
    00 = 99-Block not started
    02 = 99-Block started
    """

    CHALLENGE_NODE__13 = byte(0x1712ba)
    """
    Challenge Node: [8-Bit]
    99-Block score (likely text)
    """

    CHARACTERS_TURN = (0x2b2607)
    """
    Characters turn
    00 = Mario/Luigi/Bowser
    02 = Enemy
    Will switch to M/L/B briefly when a bro dies mid-attack.
    Will also switch to M/L/B during a Dark Star attack.
    """

    AIR_MACHINE_ = byte(0x330b90)
    """
    Air Machine: [8-Bit]
    24 = Clear
    """

    MINIGAME_TIMER_DISPLAY = byte(0x3347ec)
    """
    Minigame Timer Display (Milliseconds) [8-Bit]
    Multiply by 1.7 and you get Milliseconds, since this only goes up to 60.
    Original note said 16-Bit but the second 8-Bit don't seem to affect anything.
    """

    MINIGAME_TIMER = byte(0x3347ed)
    """
    Minigame Timer (Milliseconds) [8-Bit]
    This seems to be the real one?
    """

    MINIGAME_TIMER_1 = (0x3347ee)
    """
    Minigame Timer (Seconds)
    """

    MINIGAME_TIMER_2 = (0x3347ef)
    """
    Minigame Timer (Minutes)
    """

    X_AXIS_HORIZONTAL_POSITION = word(0x33638e)
    """
    X Axis/Horizontal position [16-Bit]
    Only Overworld, not inside Bowser!
    """

    Y_AXIS_VERTICAL_POSITION = word(0x3363aa)
    """
    Y Axis/Vertical Position [16-Bit]
    Only Overworld, not inside Bowser!
    """

    X_AXIS_HORIZONTAL_POSITION_1 = word(0x337325)
    """
    X Axis/Horizontal position [16-Bit]
    Inside Bowser
    """

    Y_AXIS_VERTICAL_POSITION_1 = word(0x3388d5)
    """
    Y Axis/Vertical Position [16-Bit]
    Inside Bowser. 0000 seems to always be the lowest point of the room.
    """

    Y_AXIS_VERTICAL_POSITION_2 = word(0x33896e)
    """
    Y Axis/Vertical Position [16-Bit]
    Mario on the overworld.
    """

    X_AXIS_HORIZONTAL_POSITION_2 = word(0x33897e)
    """
    X Axis/Horizontal Position [16-Bit]
    Mario on the overworld.
    """

    CHARACTER_USED = (0x339504)
    """
    Character used
    03: Bowser
    01: Mario & Luigi inside Bowser
    80: Mario & Luigi outside Bowser
    00: Mario & Luigi outisde Bowser (this one is used when the savefile is loaded)
    """

    BOTTOM_SCREEN_AREA_ = word(0x3395d4)
    """
    Bottom Screen Area: [16-Bit]
    All Room IDs I found are listed here: https://github.com/blueYOSHI9000/RetroAchievements-stuff/blob/main/NDS%20-%20Mario%20Luigi%20Bowsers%20Inside%20Story/Room%20IDs%20%26%20Battle%20IDs%20%26%20Stage%20IDs.txt
    """

    CHALLENGE_NODE__14 = byte(0x339f20)
    """
    Challenge Node: [8-Bit]
    99-Block score (resets to 0 once done)
    """

    AIRWAY_MINIGAME_AMOUNT_OF_BLOCKS_HIT = byte(0x339f44)
    """
    Airway Minigame - Amount of blocks hit [8-Bit]
    """

    CARROT_PIECE = word(0x339f98)
    """
    Carrot Piece [16-Bits]
    """

    CHARACTER_USED_1 = byte(0x33a098)
    """
    Character used [8-Bit]
    02: Bowser
    00: Mario & Luigi
    (the following seem to only be used during specific instances - I've noticed them after freeing Luigi in Trash Pit and before the Midbus tutorial fight)
    03: Bowser
    01: Mario & Luigi
    """

    TOP_SCREEN_AREA_ = word(0x33abe4)
    """
    Top Screen Area: [16-Bit]
    All Room IDs I found are listed here: https://github.com/blueYOSHI9000/RetroAchievements-stuff/blob/main/NDS%20-%20Mario%20Luigi%20Bowsers%20Inside%20Story/Room%20IDs%20%26%20Battle%20IDs%20%26%20Stage%20IDs.txt
    """

    CARROT_ROUND = (0x33b580)
    """
    Carrot Round
    """

    CARROT_PIECES = (0x33b58c)
    """
    Carrot pieces
    """

    AMOUNT_OF_LIGHTS_TURNED_ON_IN_MIC_TEST = byte(0x33ca02)
    """
    [8-Bit] Amount of lights turned on in Mic Test
    """

