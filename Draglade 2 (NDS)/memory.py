from pycheevos.core.helpers import *
from dataclasses import dataclass

@dataclass(frozen=True)
class Memory:
    SET_CREATED_WITH_THE_HELP_OF_PYCHEEVOS_SCRIPTS = (0x000000)
    """
    [Notes] Set created with the help of PyCheevos scripts
    See github below for source code and further information
    https://github.com/wormi-ra/RA-Scripts/tree/main/Draglade%202%20(NDS)

    Overlay Table:
    // See $0xeb89c
    ov00 = 0x021252c0 (19,328 bytes)
    ov01 = 0x021252c0 (179,840 bytes)
    ov02 = 0x021252c0 (135,104 bytes)
    ov03 = 0x021252c0 (166,432 bytes)
    ov04 = 0x021252c0 (172,800 bytes)
    ov05 = 0x021252c0 (1,536 bytes)
    ov06 = 0x021252c0 (16,832 bytes)
    ov07 = 0x021252c0 (6,176 bytes)
    // See $0xeb8d0
    ov08 = 0x02151240 (480 bytes)
    ov09 = 0x02151240 (9,920 bytes)
    ov10 = 0x02151240 (1,664 bytes)
    ov11 = 0x02151240 (90,144 bytes)
    ov12 = 0x02151240 (315,232 bytes)
    ov13 = 0x02151240 (9,408 bytes)
    // See $0xeb904
    ov14 = 0x021a2120 (10,208 bytes)
    ov15 = 0x021a2120 (17,120 bytes)
    ov16 = 0x021a2120 (16,992 bytes)
    ov17 = 0x021a2120 (14,784 bytes)
    """

    STATE_SCRIPT_ACTIVE = dword(0x0eac3c)
    """
    [32-bit] State | Script Active
    0x0 = Inactive
    0x3 = Active
    """

    AREA_POINTER = tbyte(0x0eac50)
    """
    [24-bit] Area Pointer
    +0x0 = [32-bit] Magic "#DMP" (0x504d4423)
    +0x4 = [16-bit] Map Width
    +0x6 = [16-bit] Map Height
    +0x8 = [16-bit] [Boolean] Unknown
    """

    OVERLAY_TABLE_ID = dword(0x0eb89c)
    """
    [32-bit] Overlay Table [0] | ID
    Loads at $0x1252c0

    0x0 = Title Screen
    0x1 = Main Menu
    0x2 = ?
    0x3 = VS CPU / Training
    0x4 = Story
    0x5 = ?
    0x6 = Result Screen
    0x7 = VS Intro
    """

    OVERLAY_TABLE_ID_1 = dword(0x0eb8d0)
    """
    [32-bit] Overlay Table [1] | ID
    Loads at $0x151240

    0x8 = ?
    0x9 = ?
    0xa = Default
    0xb = Pause Menu
    0xc = Wi-Fi Config Menu
    """

    OVERLAY_TABLE_ID_2 = dword(0x0eb904)
    """
    [32-bit] Overlay Table [2] | ID
    Loads at $0x1a2120

    0xe = Area Select
    0xf = Title Screen
    0x10 = Wireless
    0x11 = Wi-Fi Connection
    """

    STATE_GAME_PAUSE = byte(0x0eb930)
    """
    [8-bit] [Bitfield] State | Game Pause
    Bit0 = Can Pause
    Bit1 = Paused
    Bit2 = ?
    Bit3 = Quit to main menu
    """

    STATE_NETWORK_MODE = byte(0x0eb932)
    """
    [8-bit] State | Network Mode
    0x0 = Offline
    0x1 = Wireless
    0x2 = Wi-Fi
    """

    STATE_TUTORIAL = byte(0x0eb933)
    """
    [8-bit] [Boolean] State | Tutorial
    """

    STATE_GAME_MODE = byte(0x0eb934)
    """
    [8-bit] State | Game Mode
    0x0 = Uninitialized
    0x1 = Booting up
    0x2 = Title Screen
    0x3 = Main Menu
    0x5 = Story
    0x6 = VS CPU
    0x7 = Training
    0x8 = Grap Tutorial
    0xb = Wi-Fi Config Menu
    """

    STATE_LAST_GAME_MODE = byte(0x0eb936)
    """
    [8-bit] State | Last Game Mode
    Prior value of 0xeb934
    """

    RESULT_ENTRY_BONUS = word(0x0ebe02)
    """
    [16-bit] Result | Entry Bonus
    """

    RESULT_WIN_BONUS = word(0x0ebe04)
    """
    [16-bit] Result | Win Bonus
    """

    RESULT_BEAT_APPEAL = word(0x0ebe06)
    """
    [16-bit] Result | Beat Appeal
    """

    RESULT_BEAT_APPEAL_SP = word(0x0ebe08)
    """
    [16-bit] Result | Beat Appeal SP
    """

    RESULT_MP_BONUS = word(0x0ebe0a)
    """
    [16-bit] Result | MP Bonus
    """

    RESULT_BULLET_BONUS = word(0x0ebe0c)
    """
    [16-bit] Result | Bullet Bonus
    """

    RESULT_ATTACK_BONUS = word(0x0ebe0e)
    """
    [16-bit] Result | Attack Bonus
    """

    RESULT_ACT_BONUS = word(0x0ebe10)
    """
    [16-bit] Result | Act Bonus
    """

    RESULT_STATE = byte(0x0ebe14)
    """
    [8-bit] Result | State
    0x0 = Disabled
    0x1 = VS Intro
    0x2 = In Battle
    0x3 = In Result Screen
    """

    AREA_SELECTION_CURRENT_AREA = byte(0x0ebee0)
    """
    [8-bit] Area Selection | Current Area
    Not initialized on first load
    0x0 = King's Area
    0x1 = Volcano Area
    0x2 = Water Area
    0x3 = Canyon Area
    0x4 = Elekick Area
    0x5 = Harmonic Area
    0x6 = Main Land
    0x7 = Okuman Land
    0x8 = Area Selection
    """

    AREA_SELECTION_NEXT_AREA = byte(0x0ebee1)
    """
    [8-bit] Area Selection | Next Area
    0x0 = King's Area
    0x1 = Volcano Area
    0x2 = Water Area
    0x3 = Canyon Area
    0x4 = Elekick Area
    0x5 = Harmonic Area
    0xff = None
    """

    STATE_GAME_BOOTED = byte(0x0ebee4)
    """
    [8-bit] [Boolean] State | Game Booted
    """

    SAVE_DATA_USERNAME = (0x0ebeec)
    """
    [12 bytes] [String] Save Data | Username
    16-bit JIS encoding
    Max 6 characters
    """

    SAVE_DATA_MENU_COLOR = byte(0x0ebefa)
    """
    [8-bit] Save Data | Menu Color
    0x0 = A (Yellow)
    0x1 = B (Blue)
    0x2 = C (Green)
    0x3 = D (Red)
    0x4 = E (Purple)
    0x5 = F (Light Blue)
    0x6 = G (Pink)
    0x7 = H (Black)
    """

    SAVE_DATA_CREDITS = dword(0x0ebefc)
    """
    [32-bit] Save Data | Credits
    Story currency
    """

    SAVE_DATA_CHARACTER_UNLOCKS = byte(0x0ebf38)
    """
    [8-bit] [Bitfield] Save Data | Character Unlocks [0]
    Bit0 = Hibito
    Bit1 = Guy
    Bit2 = Daichi
    Bit3 = Kyle
    Bit4 = Zeke
    Bit5 = Cross
    Bit6 = Raio
    Bit7 = Jet
    """

    SAVE_DATA_CHARACTER_UNLOCKS_1 = byte(0x0ebf39)
    """
    [8-bit] [Bitfield] Save Data | Character Unlocks [1]
    Bit0 = Neon
    Bit1 = Kamzou
    """

    SAVE_DATA_G_HALL_UNLOCKS = byte(0x0ebf3a)
    """
    [8-bit] [Bitfield] Save Data | G-Hall Unlocks [0]
    Bit0 = King's
    Bit1 = Volcano
    Bit2 = Water
    Bit3 = Canyon
    Bit4 = Elekick
    Bit5 = Harmonic
    Bit6 = Okuman
    Bit7 = Training
    """

    SAVE_DATA_G_HALL_UNLOCKS_1 = byte(0x0ebf3b)
    """
    [8-bit] [Bitfield] Save Data | G-Hall Unlocks [1]
    Bit0 = G-Live (CoroCoro Cup)
    Bit1 = Unused
    Bit2 = G-Live (VS)
    """

    SAVE_DATA_BULLETS = byte(0x0ebf3c)
    """
    [8-bit] [Bitfield] Save Data | Bullets [0]
    // Fire Bullets
    bit0 = 001 p Fire
    bit1 = 002 m Fire
    bit2 = 003 f Fire
    bit3 = 004 p Burn
    bit4 = 005 f Burn
    bit5 = 006 Phoenix
    bit6 = 007 Attack Up
    bit7 = 008 Fire Vest
    """

    SAVE_DATA_BULLETS_1 = byte(0x0ebf3d)
    """
    [8-bit] [Bitfield] Save Data | Bullets [1]
    bit0 = 009 p Blast
    // Aqua Bullets
    bit1 = 010 p Water
    bit2 = 011 m Water
    bit3 = 012 f Water
    bit4 = 013 p Heal
    bit5 = 014 m Heal
    bit6 = 015 Cleanse
    bit7 = 016 Demcarp
    """

    SAVE_DATA_BULLETS_2 = byte(0x0ebf3e)
    """
    [8-bit] [Bitfield] Save Data | Bullets [2]
    bit0 = 017 Aqua Vest
    bit1 = 018 Tuna-Tuna
    // Lightning Bullets
    bit2 = 019 p Bolt
    bit3 = 020 m Bolt
    bit4 = 021 f Bolt
    bit5 = 022 p Spark
    bit6 = 023 f Spark
    bit7 = 024 Stun gun
    """

    SAVE_DATA_BULLETS_3 = byte(0x0ebf3f)
    """
    [8-bit] [Bitfield] Save Data | Bullets [3]
    bit0 = 025 Bolt Star
    bit1 = 026 Bolt Vest
    bit2 = 027 Giga Beam
    // Earth Bullets
    bit3 = 028 p Rock
    bit4 = 029 m Rock
    bit5 = 030 f Rock
    bit6 = 031 p Earth
    bit7 = 032 f Earth
    """

    SAVE_DATA_BULLETS_4 = byte(0x0ebf40)
    """
    [8-bit] [Bitfield] Save Data | Bullets [4]
    bit0 = 033 f Wall
    bit1 = 034 Armor Up
    bit2 = 035 Rock Vest
    bit3 = 036 Gaia Rock
    // Wind Bullets
    bit4 = 037 p Wind
    bit5 = 038 m Wind
    bit6 = 039 f Wind
    bit7 = 040 p Storm
    """

    SAVE_DATA_BULLETS_5 = byte(0x0ebf41)
    """
    [8-bit] [Bitfield] Save Data | Bullets [5]
    bit0 = 041 f Storm
    bit1 = 042 Air Slicer
    bit2 = 043 Vanish
    bit3 = 044 Wind Vest
    bit4 = 045 f Cyclone
    // Ice Bullets
    bit5 = 046 p Ice
    bit6 = 047 m Ice
    bit7 = 048 f Ice
    """

    SAVE_DATA_BULLETS_6 = byte(0x0ebf42)
    """
    [8-bit] [Bitfield] Save Data | Bullets [6]
    bit0 = 049 Ice Star
    bit1 = 050 Ice Link
    bit2 = 051 Ice Rain
    bit3 = 052 Ice Vest
    bit4 = 053 Ice Spikes
    // Flower Bullets
    bit5 = 054 p Cactus
    bit6 = 055 m Cactus
    bit7 = 056 f Cactus
    """

    SAVE_DATA_BULLETS_7 = byte(0x0ebf43)
    """
    [8-bit] [Bitfield] Save Data | Bullets [7]
    bit0 = 057 Bamboo
    bit1 = 058 Bam-Bamboo
    bit2 = 059 Rose Road
    bit3 = 060 Petal Vest
    bit4 = 061 Rose Rush
    // Poison Bullets
    bit5 = 062 p Daze
    bit6 = 063 m Daze
    bit7 = 064 f Daze
    """

    SAVE_DATA_BULLETS_8 = byte(0x0ebf44)
    """
    [8-bit] [Bitfield] Save Data | Bullets [8]
    bit0 = 065 Toxin Mush
    bit1 = 066 Gas Jump
    bit2 = 067 Toxin Vest
    bit3 = 068 PoisPunsh
    // Light Bullets
    bit4 = 069 p Light
    bit5 = 070 m Light
    bit6 = 071 f Light
    bit7 = 072 Sol Shiner
    """

    SAVE_DATA_BULLETS_9 = byte(0x0ebf45)
    """
    [8-bit] [Bitfield] Save Data | Bullets [9]
    bit0 = 073 Fiberray
    bit1 = 074 Twin Razor
    bit2 = 075 Light Vest
    bit3 = 076 Light Wing
    // Dark Bullets
    bit4 = 077 Beckon
    bit5 = 078 Lure
    bit6 = 079 Demon Hand
    bit7 = 080 p Night
    """

    SAVE_DATA_BULLETS_10 = byte(0x0ebf46)
    """
    [8-bit] [Bitfield] Save Data | Bullets [10]
    bit0 = 081 f Night
    bit1 = 082 Dark Star
    bit2 = 083 Dark Vest
    bit3 = 084 Dark Flash
    // Sound Bullets
    bit4 = 085 p Sonar
    bit5 = 086 m Sonar
    bit6 = 087 f Sonar
    bit7 = 088 Pulse
    """

    SAVE_DATA_BULLETS_11 = byte(0x0ebf47)
    """
    [8-bit] [Bitfield] Save Data | Bullets [11]
    bit0 = 089 Overdrive
    // Void Bullets
    bit1 = 090 Sam-5
    bit2 = 091 Sam-10
    bit3 = 092 Tub Drop
    bit4 = 093 Tub Storm
    bit5 = 094 Boomerang
    bit6 = 095 Present
    bit7 = 096 Whoops!
    """

    SAVE_DATA_BULLETS_12 = byte(0x0ebf48)
    """
    [8-bit] [Bitfield] Save Data | Bullets [12]
    bit0 = 097 Poop
    // Special Bullets
    bit1 = 098 Huge Bomb
    bit2 = 099 Carp King
    bit3 = 100 Iron Soul
    bit4 = 101 Wind Blade
    bit5 = 102 Ki Blast
    bit6 = 103 Angel Wing
    bit7 = 104 Demon Face
    """

    SAVE_DATA_BULLETS_13 = byte(0x0ebf49)
    """
    [8-bit] [Bitfield] Save Data | Bullets [13]
    bit0 = 105 Meteor Dive
    """

    DECK_1_MAIN_BULLET_1 = byte(0x0ed46c)
    """
    [8-bit] Deck 1 [0] | Main Bullet 1
    0xff = Empty
    0x00-0x68 = Bullet ID

    IDs starts at 0
    ID = No. -1
    see $0xebf3c for bullet IDs
    Each Deck data is 8 bytes long
    """

    DECK_1_MAIN_BULLET_2 = byte(0x0ed46d)
    """
    [8-bit] Deck 1 [0] | Main Bullet 2
    """

    DECK_1_MAIN_BULLET_3 = byte(0x0ed46e)
    """
    [8-bit] Deck 1 [0] | Main Bullet 3
    """

    DECK_1_STOCK_BULLET_1 = byte(0x0ed46f)
    """
    [8-bit] Deck 1 [0] | Stock Bullet 1
    """

    DECK_1_STOCK_BULLET_2 = byte(0x0ed470)
    """
    [8-bit] Deck 1 [0] | Stock Bullet 2
    """

    DECK_1_STOCK_BULLET_3 = byte(0x0ed471)
    """
    [8-bit] Deck 1 [0] | Stock Bullet 3
    """

    DECK_1_SELECTED_BEAT_SCORE_INDEX = byte(0x0ed472)
    """
    [8-bit] Deck 1 [0] | Selected Beat Score Index
    """

    DECK_2_MAIN_BULLET_1 = byte(0x0ed474)
    """
    [8-bit] Deck 2 [1] | Main Bullet 1
    """

    DECK_2_MAIN_BULLET_2 = byte(0x0ed475)
    """
    [8-bit] Deck 2 [1] | Main Bullet 2
    """

    DECK_2_MAIN_BULLET_3 = byte(0x0ed476)
    """
    [8-bit] Deck 2 [1] | Main Bullet 3
    """

    DECK_2_STOCK_BULLET_1 = byte(0x0ed477)
    """
    [8-bit] Deck 2 [1] | Stock Bullet 1
    """

    DECK_2_STOCK_BULLET_2 = byte(0x0ed478)
    """
    [8-bit] Deck 2 [1] | Stock Bullet 2
    """

    DECK_2_STOCK_BULLET_3 = byte(0x0ed479)
    """
    [8-bit] Deck 2 [1] | Stock Bullet 3
    """

    DECK_2_SELECTED_BEAT_SCORE_INDEX = byte(0x0ed47a)
    """
    [8-bit] Deck 2 [1] | Selected Beat Score Index
    """

    DECK_3_MAIN_BULLET_1 = byte(0x0ed47c)
    """
    [8-bit] Deck 3 [2] | Main Bullet 1
    """

    DECK_3_MAIN_BULLET_2 = byte(0x0ed47d)
    """
    [8-bit] Deck 3 [2] | Main Bullet 2
    """

    DECK_3_MAIN_BULLET_3 = byte(0x0ed47e)
    """
    [8-bit] Deck 3 [2] | Main Bullet 3
    """

    DECK_3_STOCK_BULLET_1 = byte(0x0ed47f)
    """
    [8-bit] Deck 3 [2] | Stock Bullet 1
    """

    DECK_3_STOCK_BULLET_2 = byte(0x0ed480)
    """
    [8-bit] Deck 3 [2] | Stock Bullet 2
    """

    DECK_3_STOCK_BULLET_3 = byte(0x0ed481)
    """
    [8-bit] Deck 3 [2] | Stock Bullet 3
    """

    DECK_3_SELECTED_BEAT_SCORE_INDEX = byte(0x0ed482)
    """
    [8-bit] Deck 3 [2] | Selected Beat Score Index
    """

    DECK_4_MAIN_BULLET_1 = byte(0x0ed484)
    """
    [8-bit] Deck 4 [3] | Main Bullet 1
    """

    DECK_4_MAIN_BULLET_2 = byte(0x0ed485)
    """
    [8-bit] Deck 4 [3] | Main Bullet 2
    """

    DECK_4_MAIN_BULLET_3 = byte(0x0ed486)
    """
    [8-bit] Deck 4 [3] | Main Bullet 3
    """

    DECK_4_STOCK_BULLET_1 = byte(0x0ed487)
    """
    [8-bit] Deck 4 [3] | Stock Bullet 1
    """

    DECK_4_STOCK_BULLET_2 = byte(0x0ed488)
    """
    [8-bit] Deck 4 [3] | Stock Bullet 2
    """

    DECK_4_STOCK_BULLET_3 = byte(0x0ed489)
    """
    [8-bit] Deck 4 [3] | Stock Bullet 3
    """

    DECK_4_SELECTED_BEAT_SCORE_INDEX = byte(0x0ed48a)
    """
    [8-bit] Deck 4 [3] | Selected Beat Score Index
    """

    DECK_5_MAIN_BULLET_1 = byte(0x0ed48c)
    """
    [8-bit] Deck 5 [4] | Main Bullet 1
    """

    DECK_5_MAIN_BULLET_2 = byte(0x0ed48d)
    """
    [8-bit] Deck 5 [4] | Main Bullet 2
    """

    DECK_5_MAIN_BULLET_3 = byte(0x0ed48e)
    """
    [8-bit] Deck 5 [4] | Main Bullet 3
    """

    DECK_5_STOCK_BULLET_1 = byte(0x0ed48f)
    """
    [8-bit] Deck 5 [4] | Stock Bullet 1
    """

    DECK_5_STOCK_BULLET_2 = byte(0x0ed490)
    """
    [8-bit] Deck 5 [4] | Stock Bullet 2
    """

    DECK_5_STOCK_BULLET_3 = byte(0x0ed491)
    """
    [8-bit] Deck 5 [4] | Stock Bullet 3
    """

    DECK_5_SELECTED_BEAT_SCORE_INDEX = byte(0x0ed492)
    """
    [8-bit] Deck 5 [4] | Selected Beat Score Index
    """

    RAIO_NAME = (0x0ed49c)
    """
    [12 bytes] [String] Raio | Name
    16-bit JIS encoding
    Max 6 characters
    """

    RAIO_COLOR = byte(0x0ed4aa)
    """
    [8-bit] Raio | Color
    """

    ACTIVE_DECK_INDEX = byte(0x0ed4ab)
    """
    [8-bit] Active Deck Index
    0x0 = Deck 1
    0x1 = Deck 2
    0x2 = Deck 3
    0x3 = Deck 4
    0x4 = Deck 5
    """

    RAIO_GP_EX = dword(0x0ed4bc)
    """
    [32-bit] Raio | GP-EX
    (Experience)
    """

    QUESTS_COMPLETION = byte(0x0ed4c5)
    """
    [8-bit] [Bitfield] Quests | Completion [0]
    Bit0 = CoroCoro Cup Registered
    Bit7 = Mirage Egg
    """

    QUESTS_COMPLETION_1 = byte(0x0ed4c6)
    """
    [8-bit] [Bitfield] Quests | Completion [1]
    bit0 = Return It
    bit1 = DS Dropped
    bit2 = DoraDora
    bit3 = My treasure
    bit4 = Goshi Desert
    bit5 = Saru Ruins
    bit6 = Zoff Pass
    bit7 = Ghost Town Underground
    """

    QUESTS_COMPLETION_2 = byte(0x0ed4c7)
    """
    [8-bit] [Bitfield] Quests | Completion [2]
    bit0 = Kenmeri
    bit1 = Poshka Ruins
    bit2 = Win Desert
    bit3 = Iwaku Pass
    bit4 = Hidden Path
    bit5 = Underground Lab
    bit6 = Underground Lab Deep
    bit7 = Matter Invert
    """

    QUESTS_COMPLETION_3 = byte(0x0ed4c8)
    """
    [8-bit] [Bitfield] Quests | Completion [3]
    bit0 = Other Space
    bit1 = Change Beat!
    bit2 = Char Grapper
    bit3 = Myst Grapper
    bit4 = Goril's Roar
    bit5 = Goril's Roar+
    bit6 = Goril's Rage
    bit7 = Final Goril
    """

    QUESTS_G_LIVE_COMPLETION = byte(0x0ed4c9)
    """
    [8-bit] [Bitfield] Quests / G-Live | Completion [4]
    bit0 = Arman Ranger
    bit1 = Arman Soldier
    bit2 = Golden Arman
    bit3 = Ult. Arman
    bit4 = Sudden Death
    bit5 = G-Live Grapper 1 Fought
    bit6 = G-Live Grapper 2 Fought
    bit7 = G-Live Grapper 3 Fought
    """

    CHEST_FLAGS = byte(0x0ed4cb)
    """
    [8-bit] [Bitfield] Chest Flags [0]
    // Format: Level | Map ID | Reward
    Bit0 = Goshi Desert | 0xc9 | 100 MP
    Bit1 = Saru Ruins | 0xd1 | 100 MP
    Bit2 = Saru Ruins | 0xd6 | Lure
    Bit3 = Mirage Egg | 0x15a | p Light
    Bit4 = Mirage Egg | 0x15d | 200 MP
    Bit5 = Mirage Egg | 0x15e | m Daze
    Bit6 = Mirage Egg | 0x15f | Phoenix
    Bit7 = Zoff Pass | 0xe3 | Rock Vest
    """

    CHEST_FLAGS_1 = byte(0x0ed4cc)
    """
    [8-bit] [Bitfield] Chest Flags [1]
    Bit0 = Zoff Pass | 0xe4 | m Heal
    Bit1 = Ghost Underground | 0xe9 | Ice Vest
    Bit2 = Ghost Underground | 0xf2 | p Heal
    Bit3 = Ghost Underground | 0xf3 | 300 MP
    Bit4 = DS Dropped | 0x164 | Light Vest
    Bit5 = DS Dropped | 0x16f | f Ice
    Bit6 = DS Dropped | 0x170 | p Burn
    Bit7 = DS Dropped | 0x171 | 300 MP
    """

    CHEST_FLAGS_2 = byte(0x0ed4cd)
    """
    [8-bit] [Bitfield] Chest Flags [2]
    Bit0 = DS Dropped | 0x175 | Dark Star
    Bit1 = Kenmeri | 0xfa | p Ice
    Bit2 = Kenmeri | 0x102 | Armor up
    Bit3 = Kenmeri | 0x107 | Bit Slicer
    Bit4 = Kenmeri | 0x10b | Pulse
    Bit5 = Kenmeri | 0x10d | p Fire
    Bit6 = Poshka Ruins | 0x112 | Ice Rain
    Bit7 = Poshka Ruins | 0x116 | Wind Vest
    """

    CHEST_FLAGS_3 = byte(0x0ed4ce)
    """
    [8-bit] [Bitfield] Chest Flags [3]
    Bit0 = Poshka Ruins | 0x116 | m Sonar
    Bit1 = Poshka Ruins | 0x11c | m Sonar
    Bit2 = Poshka Ruins | 0x11d | Dark Vest
    Bit3 = Poshka Ruins | 0x121 | 300 MP
    Bit4 = Poshka Ruins | 0x121 | m Bolt
    Bit5 = My Treasure | 0x178 | 200 MP
    Bit6 = My Treasure | 0x178 | Twin Razor
    Bit7 = My Treasure | 0x17a | m Rock
    """

    CHEST_FLAGS_4 = byte(0x0ed4cf)
    """
    [8-bit] [Bitfield] Chest Flags [4]
    Bit0 = My Treasure | 0x17f | m Daze
    Bit1 = My Treasure | 0x17f | Vanish
    Bit2 = Hidden Path | 0x127 | 200 MP
    Bit3 = Underground Lab | 0x130 | Bolt Vest
    Bit4 = Underground Lab | 0x136 | f Water
    Bit5 = Underground Lab | 0x137 | Sam-10
    Bit6 = Underground Lab | 0x137 | 300 MP
    Bit7 = Underground Lab Core | 0x13e | f Daze
    """

    CHEST_FLAGS_5 = byte(0x0ed4d0)
    """
    [8-bit] [Bitfield] Chest Flags [5]
    Bit0 = Underground Lab Core | 0x142 | 100 MP
    Bit1 = Underground Lab Core | 0x145 | m Fire
    Bit2 = Underground Lab Core | 0x14b | 300 MP
    Bit3 = Underground Lab Core | 0x150 | f Rock
    Bit4 = Underground Lab Core | 0x152 | f Night
    Bit5 = Underground Lab Core | 0x155 | p Ice
    Bit6 = Arman Ranger | 0x188 | f Spark
    Bit7 = Arman Soldier | 0x18e | m Water
    """

    CHEST_FLAGS_6 = byte(0x0ed4d1)
    """
    [8-bit] [Bitfield] Chest Flags [6]
    Bit0 = Arman Soldier | 0x197 | f Sonar
    Bit1 = Golden Arman | 0x19c | f Water
    Bit2 = Golden Arman | 0x19e | m Daze
    Bit3 = Golden Arman | 0x19e | 200 MP
    Bit4 = Ultimate Arman | 0x1a2 | f Light
    Bit5 = Ultimate Arman | 0x1ad | f Fire
    Bit6 = Ultimate Arman | 0x1b1 | 300 MP
    Bit7 = Ultimate Arman | 0x1b1 | p Earth
    """

    STORY_PROGRESS = byte(0x0ed504)
    """
    [8-bit] Story Progress
    Increments after each story related cutscene

    0x0 = Story Start
    0x7 = Hibito Fight
    0xd = Round 1
    0x13 = Goshi Desert
    0x1e = Round 2
    0x23 = Saru Ruins
    0x2c = Round 3
    0x3d = Round 4
    0x49 = Okuman GP Match 1
    0x4b = Okuman GP Match 2
    0x4d = Okuman GP Match 3
    0x4f = Okuman GP Match 4
    0x52 = Okuman GP Match 5
    0x59 = Zoff Pass
    0x5e = Round 5
    0x63 = Ghost Underground
    0x6c = Round 6
    0x72 = Win Desert
    0x76 = Round 7
    0x81 = Round 8
    0x87 = Kenmeri
    0x8e = Iwaku Pass
    0x92 = Round 9 (quarterfinals)
    0x9a = Poshka Ruins
    0xa1 = Round 10 (semifinals)
    0xaf = Underground Lab
    0xb0 = Underground Lab (Zeke Fight)
    0xb3 = Underground Lab (Variant Fight)
    0xb4 = Deep Underground Lab
    0xb5 = King Fight
    0xba = Evil One Fight
    0xbb = Credits
    0xbc = Post-credits Cutscene
    0xbd = Story End
    """

    LAST_QUEST_STARTED = byte(0x0ed505)
    """
    [8-bit] Last Quest Started
    0x5 = Mirage Egg
    0x6 = Return It
    0x7 = DS Dropped
    0x8 = DoraDora
    0x9 = My Treasure
    0xa = Goshi Desert
    0xb = Saru Ruins
    0xc = Zoff Pass
    0xd = Ghost Town Underground
    0xe = Kenmeri
    0xf = Poshka Ruins
    0x10 = Win Desert
    0x11 = Iwaku Pass
    0x12 = Hidden Path
    0x13 = Underground Lab
    0x14 = Deep Underground Lab
    0x15 = Matter Invert
    0x16 = Other Space
    0x17 = Change Beat!
    0x18 = Char Grapper
    0x19 = Myst Grapper
    0x1a = Goril's Roar
    0x1b = Goril's Roar+
    0x1c = Goril's Rage
    0x1d = Final Goril
    0x1e = Arman Ranger
    0x1f = Arman Soldier
    0x20 = Golden Arman
    0x21 = Ultimate Arman
    0x22 = Sudden Death
    """

    SAVE_DATA_SCRIPT_ID = word(0x0ed528)
    """
    [16-bit] Save Data | Script ID
    See $0x23bb70
    """

    RAIO_LEVEL = byte(0x0ed52d)
    """
    [8-bit] Raio | Level
    """

    RAIO_GRADE = byte(0x0ed52f)
    """
    [8-bit] Raio | Grade
    0x0 = M-9
    0x1 = M-8
    0x2 = M-7
    0x3 = M-6
    0x4 = M-5
    0x5 = M-4
    0x6 = M-3
    0x7 = M-2
    0x8 = M-1
    """

    STATS_QUESTS = dword(0x0ed5e0)
    """
    [32-bit] Stats | Quests
    """

    STATS_CHESTS = dword(0x0ed5e4)
    """
    [32-bit] Stats | Chests
    """

    STATS_G_LIVE = dword(0x0ed5e8)
    """
    [32-bit] Stats | G-Live
    """

    STATS_G_LIVER_FLAGS = byte(0x0ed5ec)
    """
    [8-bit] Stats | G-Liver Flags
    Hidden Stat

    Bit0 = King's Area
    Bit1 = Volcano Area
    Bit2 = Water Area
    Bit3 = Canyon Area
    Bit4 = Elekick Area
    Bit5 = Harmonic Area
    """

    STATS_VARIANTS_KILLED = byte(0x0ed5ed)
    """
    [8-bit] Stats | Variants Killed
    Hidden Stat
    """

    STATS_BASIC_ATTACKS = dword(0x0ed5f0)
    """
    [32-bit] Stats | Basic Attacks
    """

    STATS_COMBOS = dword(0x0ed5f4)
    """
    [32-bit] Stats | Combos
    """

    STATS_MAX_COMBO = dword(0x0ed5f8)
    """
    [32-bit] Stats | Max Combo
    """

    STATS_HIT_COUNT = dword(0x0ed5fc)
    """
    [32-bit] Stats | Hit count
    """

    STATS_DAMAGE_DEALT = dword(0x0ed600)
    """
    [32-bit] Stats | Damage Dealt
    """

    STATS_GRAB_ATTACKS = dword(0x0ed604)
    """
    [32-bit] Stats | Grab Attacks
    """

    STATS_BOUNCE = dword(0x0ed608)
    """
    [32-bit] Stats | Bounce
    """

    STATS_ENEMIES_DEFEATED = dword(0x0ed60c)
    """
    [32-bit] Stats | Enemies Defeated
    """

    STATS_PERFECT_WINS = dword(0x0ed610)
    """
    [32-bit] Stats | Perfect Wins
    """

    STATS_CLOSE_WINS = dword(0x0ed614)
    """
    [32-bit] Stats | Close Wins
    """

    STATS_MATCHES_OVER_1000_CREDITS = byte(0x0ed618)
    """
    [8-bit] Stats | Matches Over 1000 Credits
    Hidden Stat
    """

    STATS_MATCHES_WON = byte(0x0ed619)
    """
    [8-bit] Stats | Matches Won (Charismatic Grapper)
    Hidden Stat
    """

    STATS_CLOSE_WINS_1 = byte(0x0ed61a)
    """
    [8-bit] Stats | Close Wins (Gladiator)
    Hidden Stat
    """

    STATS_BEAT_COMBO_COUNT = dword(0x0ed61c)
    """
    [32-bit] Stats | Beat Combo Count
    """

    STATS_BEAT_COMBO_PERFECTS = dword(0x0ed620)
    """
    [32-bit] Stats | Beat Combo Perfects
    """

    STATS_SUPER_BEAT_COMBO_COUNT = dword(0x0ed624)
    """
    [32-bit] Stats | Super Beat Combo Count
    """

    STATS_SUPER_BEAT_COMBO_WINS = dword(0x0ed628)
    """
    [32-bit] Stats | Super Beat Combo Wins
    """

    STATS_SBC_WINNER_FLAGS = byte(0x0ed62c)
    """
    [8-bit] [Bitfield] Stats | SBC Winner Flags [0]
    Hidden Stat

    Bit0 = Hibito
    Bit1 = Guy
    Bit2 = Daichi
    Bit3 = Kyle
    Bit4 = Zeke
    Bit5 = Cross
    Bit6 = Raio
    Bit7 = Jet
    """

    STATS_SBC_WINNER_FLAGS_1 = byte(0x0ed62d)
    """
    [8-bit] [Bitfield] Stats | SBC Winner Flags [1]
    Hidden Stat

    Bit0 = Neon
    Bit1 = Kamzou
    """

    STATS_BEAT_DRIVE_COUNT = dword(0x0ed630)
    """
    [32-bit] Stats | Beat Drive Count
    """

    STATS_BEAT_DRIVE_WINS = dword(0x0ed634)
    """
    [32-bit] Stats | Beat Drive Wins
    """

    STATS_BD_WINNER_FLAGS = byte(0x0ed638)
    """
    [8-bit] [Bitfield] Stats | BD Winner Flags [0]
    Hidden Stat

    Bit0 = Hibito
    Bit1 = Guy
    Bit2 = Daichi
    Bit3 = Kyle
    Bit4 = Zeke
    Bit5 = Cross
    Bit6 = Raio
    Bit7 = Jet
    """

    STATS_BD_WINNER_FLAGS_1 = byte(0x0ed639)
    """
    [8-bit] [Bitfield] Stats | BD Winner Flags [1]
    Hidden Stat

    Bit0 = Neon
    Bit1 = Kamzou
    """

    STATS_FIRE_BULLETS = dword(0x0ed63c)
    """
    [32-bit] Stats | Fire Bullets
    """

    STATS_WATER_BULLETS = dword(0x0ed640)
    """
    [32-bit] Stats | Water Bullets
    """

    STATS_LIGHTNING_BULLETS = dword(0x0ed644)
    """
    [32-bit] Stats | Lightning Bullets
    """

    STATS_EARTH_BULLETS = dword(0x0ed648)
    """
    [32-bit] Stats | Earth Bullets
    """

    STATS_WIND_BULLETS = dword(0x0ed64c)
    """
    [32-bit] Stats | Wind Bullets
    """

    STATS_ICE_BULLETS = dword(0x0ed650)
    """
    [32-bit] Stats | Ice Bullets
    """

    STATS_FLOWER_BULLETS = dword(0x0ed654)
    """
    [32-bit] Stats | Flower Bullets
    """

    STATS_POISON_BULLETS = dword(0x0ed658)
    """
    [32-bit] Stats | Poison Bullets
    """

    STATS_LIGHT_BULLETS = dword(0x0ed65c)
    """
    [32-bit] Stats | Light Bullets
    """

    STATS_DARK_BULLETS = dword(0x0ed660)
    """
    [32-bit] Stats | Dark Bullets
    """

    STATS_SOUND_BULLETS = dword(0x0ed664)
    """
    [32-bit] Stats | Sound Bullets
    """

    STATS_VOID_BULLETS = dword(0x0ed668)
    """
    [32-bit] Stats | Void Bullets
    """

    STATS_BULLET_WINS = dword(0x0ed66c)
    """
    [32-bit] Stats | Bullet Wins
    """

    STATS_WIRELESS_MATCHES = word(0x0ed674)
    """
    [16-bit] Stats | Wireless Matches
    """

    STATS_WIRELESS_WINS = word(0x0ed676)
    """
    [16-bit] Stats | Wireless Wins
    """

    STATS_WIRELESS_WIN_STREAK = word(0x0ed678)
    """
    [16-bit] Stats | Wireless Win Streak
    """

    STATS_WI_FI_MATCHES = word(0x0ed67c)
    """
    [16-bit] Stats | Wi-Fi Matches
    """

    STATS_WI_FI_WINS = word(0x0ed67e)
    """
    [16-bit] Stats | Wi-Fi Wins
    """

    STATS_WI_FI_WIN_STREAK = word(0x0ed680)
    """
    [16-bit] Stats | Wi-Fi Win Streak
    """

    STATS_WI_FI_BULLET_DOWNLOADS = word(0x0ed684)
    """
    [16-bit] Stats | Wi-Fi Bullet Downloads
    """

    STATS_WI_FI_BEAT_SCORE_DOWNLOADS = word(0x0ed686)
    """
    [16-bit] Stats | Wi-Fi Beat Score Downloads
    """

    STATS_COROCORO_CUP_PARTICIPATIONS = word(0x0ed68e)
    """
    [16-bit] Stats | CoroCoro Cup Participations
    """

    STATS_COROCORO_CUP_PARTICIPATION_STREAK = word(0x0ed690)
    """
    [16-bit] Stats | CoroCoro Cup Participation Streak
    """

    STATS_COROCORO_CUP_MATCHES_PLAYED = word(0x0ed692)
    """
    [16-bit] Stats | CoroCoro Cup Matches Played
    """

    STATS_COROCORO_CUP_WINS = word(0x0ed694)
    """
    [16-bit] Stats | CoroCoro Cup Wins
    """

    STATS_COROCORO_CUP_WIN_STREAK = word(0x0ed696)
    """
    [16-bit] Stats | CoroCoro Cup Win Streak
    """

    TITLES_SUPERHERO = byte(0x0ed698)
    """
    [8-bit] Titles [0] | Superhero
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_SUPER_RICH = byte(0x0ed699)
    """
    [8-bit] Titles [1] | Super Rich
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_SUPER_CELEBRITY = byte(0x0ed69a)
    """
    [8-bit] Titles [2] | Super Celebrity
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_QUEST_MASTER = byte(0x0ed69b)
    """
    [8-bit] Titles [3] | Quest Master
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_TREASURE_HUNTER = byte(0x0ed69c)
    """
    [8-bit] Titles [4] | Treasure Hunter
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_VARIANT_HUNTER = byte(0x0ed69d)
    """
    [8-bit] Titles [5] | Variant Hunter
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_SCORER = byte(0x0ed69e)
    """
    [8-bit] Titles [6] | Scorer
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_G_LIVER = byte(0x0ed69f)
    """
    [8-bit] Titles [7] | G-Liver
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_G_LIVE_MASTER = byte(0x0ed6a0)
    """
    [8-bit] Titles [8] | G-Live Master
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_G_LIVE_KING = byte(0x0ed6a1)
    """
    [8-bit] Titles [9] | G-Live King
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_G_LIVE_GRAPPER = byte(0x0ed6a2)
    """
    [8-bit] Titles [10] | G-Live Grapper
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_ATTACKER = byte(0x0ed6a3)
    """
    [8-bit] Titles [11] | Attacker
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_RUSHMAN = byte(0x0ed6a4)
    """
    [8-bit] Titles [12] | Rushman
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_TOUGH_GUY = byte(0x0ed6a5)
    """
    [8-bit] Titles [13] | Tough guy
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_BERSERKER = byte(0x0ed6a6)
    """
    [8-bit] Titles [14] | Berserker
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_IRON_MAN = byte(0x0ed6a7)
    """
    [8-bit] Titles [15] | Iron Man
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_GLADIATOR = byte(0x0ed6a8)
    """
    [8-bit] Titles [16] | Gladiator
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_MATTER_BR = byte(0x0ed6a9)
    """
    [8-bit] Titles [17] | Matter Br.
    0x0 = Locked
    0x2 = Unlocked
    """

    TITLES_SP_RANKER = byte(0x0ed6aa)
    """
    [8-bit] Titles [18] | Sp. Ranker
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_CHARISMATIC_GRAPPER = byte(0x0ed6ab)
    """
    [8-bit] Titles [19] | Charismatic Grapper
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_STAR_GRAPPER = byte(0x0ed6ac)
    """
    [8-bit] Titles [20] | Star Grapper
    0x0 = Locked
    0x2 = Unlocked
    """

    TITLES_IDOL_GRAPPER = byte(0x0ed6ad)
    """
    [8-bit] Titles [21] | Idol Grapper
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_COMPOSER = byte(0x0ed6ae)
    """
    [8-bit] Titles [22] | Composer
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_BEAT_COMBO_MANIA = byte(0x0ed6af)
    """
    [8-bit] Titles [23] | Beat Combo Mania
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_FULL_BEAT_COMBO = byte(0x0ed6b0)
    """
    [8-bit] Titles [24] | Full Beat Combo
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_SUPER_BEAT_COMBO_MANIA = byte(0x0ed6b1)
    """
    [8-bit] Titles [25] | Super Beat Combo Mania
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_SUPER_BEAT_COMBO_WINNER = byte(0x0ed6b2)
    """
    [8-bit] Titles [26] | Super Beat Combo Winner
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_BEAT_DRIVE_MANIA = byte(0x0ed6b3)
    """
    [8-bit] Titles [27] | Beat Drive Mania
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_BEAT_DRIVE_WINNER = byte(0x0ed6b4)
    """
    [8-bit] Titles [28] | Beat Drive Winner
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_BULLETEER = byte(0x0ed6b5)
    """
    [8-bit] Titles [29] | Bulleteer
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_BULLET_MANIAC = byte(0x0ed6b6)
    """
    [8-bit] Titles [30] | Bullet Maniac
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_FIRE_G = byte(0x0ed6b7)
    """
    [8-bit] Titles [31] | Fire G
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_AQUA_G = byte(0x0ed6b8)
    """
    [8-bit] Titles [32] | Aqua G
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_ELEC_G = byte(0x0ed6b9)
    """
    [8-bit] Titles [33] | Elec G
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_ROCK_G = byte(0x0ed6ba)
    """
    [8-bit] Titles [34] | Rock G
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_WIND_G = byte(0x0ed6bb)
    """
    [8-bit] Titles [35] | Wind G
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_ICE_G = byte(0x0ed6bc)
    """
    [8-bit] Titles [36] | Ice G
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_PETAL_G = byte(0x0ed6bd)
    """
    [8-bit] Titles [37] | Petal G
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_POISON_G = byte(0x0ed6be)
    """
    [8-bit] Titles [38] | Poison G
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_LIGHT_G = byte(0x0ed6bf)
    """
    [8-bit] Titles [39] | Light G
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_DARK_G = byte(0x0ed6c0)
    """
    [8-bit] Titles [40] | Dark G
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_MUSIC_G = byte(0x0ed6c1)
    """
    [8-bit] Titles [41] | Music G
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_VOID_G = byte(0x0ed6c2)
    """
    [8-bit] Titles [42] | Void G
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_DOWNLOADER = byte(0x0ed6c3)
    """
    [8-bit] Titles [43] | Downloader
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_WIRELESS_MAJOR = byte(0x0ed6c4)
    """
    [8-bit] Titles [44] | Wireless Major
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_WIRELESS_G = byte(0x0ed6c5)
    """
    [8-bit] Titles [45] | Wireless G
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_WIRELESS_HERO = byte(0x0ed6c6)
    """
    [8-bit] Titles [46] | Wireless Hero
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_WIRELESS_GOLD = byte(0x0ed6c7)
    """
    [8-bit] Titles [47] | Wireless Gold
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_WI_FI_MAJOR = byte(0x0ed6c8)
    """
    [8-bit] Titles [48] | Wi-Fi Major
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_WI_FI_G = byte(0x0ed6c9)
    """
    [8-bit] Titles [49] | Wi-Fi G
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_WI_FI_F = byte(0x0ed6ca)
    """
    [8-bit] Titles [50] | Wi-Fi F
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_WI_FI_KING = byte(0x0ed6cb)
    """
    [8-bit] Titles [51] | Wi-Fi King
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_WI_FI_HERO = byte(0x0ed6cc)
    """
    [8-bit] Titles [52] | Wi-Fi Hero
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_WI_FI_GUTS = byte(0x0ed6cd)
    """
    [8-bit] Titles [53] | Wi-Fi Guts
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_WI_FI_DIAMOND = byte(0x0ed6ce)
    """
    [8-bit] Titles [54] | Wi-Fi Diamond
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_WI_FI_PEARL = byte(0x0ed6cf)
    """
    [8-bit] Titles [55] | Wi-Fi Pearl
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_WI_FI_PLATINUM = byte(0x0ed6d0)
    """
    [8-bit] Titles [56] | Wi-Fi Platinum
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_WI_FI_GOLD = byte(0x0ed6d1)
    """
    [8-bit] Titles [57] | Wi-Fi Gold
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_WI_FI_SILVER = byte(0x0ed6d2)
    """
    [8-bit] Titles [58] | Wi-Fi Silver
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_WI_FI_BRONZE = byte(0x0ed6d3)
    """
    [8-bit] Titles [59] | Wi-Fi Bronze
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_G_POINT_MASTER = byte(0x0ed6d4)
    """
    [8-bit] Titles [60] | G-Point Master
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_G_POINT_KING = byte(0x0ed6d5)
    """
    [8-bit] Titles [61] | G-Point King
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_G_POINT_GET = byte(0x0ed6d6)
    """
    [8-bit] Titles [62] | G-Point Get
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_COROCORO_CUP_1 = byte(0x0ed6d7)
    """
    [8-bit] Titles [63] | CoroCoro Cup 1
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_COROCORO_CUP_2 = byte(0x0ed6d8)
    """
    [8-bit] Titles [64] | CoroCoro Cup 2
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_COROCORO_CUP_3 = byte(0x0ed6d9)
    """
    [8-bit] Titles [65] | CoroCoro Cup 3
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_COROCORO_CUP_4 = byte(0x0ed6da)
    """
    [8-bit] Titles [66] | CoroCoro Cup 4
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_COROCORO_CUP_5 = byte(0x0ed6db)
    """
    [8-bit] Titles [67] | CoroCoro Cup 5
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_COROCORO_CUP_6 = byte(0x0ed6dc)
    """
    [8-bit] Titles [68] | CoroCoro Cup 6
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_COROCORO_CUP_7 = byte(0x0ed6dd)
    """
    [8-bit] Titles [69] | CoroCoro Cup 7
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_COROCORO_CUP_8 = byte(0x0ed6de)
    """
    [8-bit] Titles [70] | CoroCoro Cup 8
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    TITLES_COROCORO_CUP_9 = byte(0x0ed6df)
    """
    [8-bit] Titles [71] | CoroCoro Cup 9
    0x0 = Locked
    0x1 = Unlock Popup
    0x2 = Unlocked
    """

    UNIDENTIFIED_LINKED_LIST = tbyte(0x0edf8c)
    """
    [24-bit Pointer] Unidentified Linked List
    +0x0 = [24-bit Pointer] Next
    +0x4 = [24-bit Pointer] Prev
    +0x8 = [24-bit Pointer] Data
    ..Points to static bytecode addresses

    Null in match battle
    """

    PLAYER_CHARACTER = word(0x0f3594)
    """
    [16-bit] Player | Character
    0x0 = Hibito
    0x1 = Guy
    0x2 = Daichi
    0x3 = Kyle
    0x4 = Zeke
    0x5 = Cross
    0x6 = Raio
    0x7 = Jet
    0x8 = Neon
    0x9 = Kamzou
    """

    PLAYER_ACTIVE = byte(0x0f35a4)
    """
    [8-bit] [Boolean] Player | Active
    """

    PLAYER_POSITION_X = dword(0x0f36d8)
    """
    [32-bit] [Float] Player | Position X
    """

    PLAYER_POSITION_Y = dword(0x0f36dc)
    """
    [32-bit] [Float] Player | Position Y
    """

    PLAYER_ORIENTATION = byte(0x0f3710)
    """
    [8-bit] Player | Orientation
    0x0 = Right
    0x1 = Left
    """

    PLAYER_IN_AIR = byte(0x0f3711)
    """
    [8-bit] [Boolean] Player | In Air
    0x0 = Touching Ground
    0x1 = In Air
    """

    PLAYER_MAX_HEALTH = word(0x0f3720)
    """
    [16-bit] Player | Max Health
    """

    PLAYER_HEALTH = word(0x0f3728)
    """
    [16-bit] Player | Health
    """

    PLAYER_CURRENT_BP = byte(0x0f3734)
    """
    [8-bit] Player | Current BP
    0x9 = Max
    """

    PLAYER_DAMAGE_EFFECT = byte(0x0f374e)
    """
    [8-bit] [Bitfield] Player | Damage Effect [0]
    Bit4 = Electrocuted
    """

    PLAYER_DAMAGE_EFFECT_1 = byte(0x0f374f)
    """
    [8-bit] [Bitfield] Player | Damage Effect [1]
    Bit2 = Touching Floor Hazard
    Bit3 = Aerial Recovery
    """

    PLAYER_PENDING_TICK_DAMAGE = word(0x0f375e)
    """
    [16-bit] Player | Pending Tick Damage
    """

    ENEMY_HEALTH = word(0x0f8bb4)
    """
    [16-bit] Enemy (Match) | Health
    """

    INPUTS_PRIMARY = byte(0x0fffb0)
    """
    [8-bit] [Bitfield] Inputs | Primary
    bit0 = A
    bit1 = B
    bit2 = Select
    bit3 = Start
    bit4 = Right
    bit5 = Left
    bit6 = Up
    bit7 = Down
    """

    INPUTS_SECONDARY = byte(0x0fffb1)
    """
    [8-bit] [Bitfield] Inputs | Secondary
    bit0 = R
    bit1 = L
    bit2 = X
    bit3 = Y
    """

    VERSUS_ENDING_TIMER = word(0x100104)
    """
    [16-bit] Versus | Ending Timer
    0x0 = In Versus
    0x1-0xf8 = Ending Timer
    """

    VERSUS_WINNER = word(0x100106)
    """
    [16-bit] Versus | Winner
    0x0 = None
    0x1 = Player
    0x2 = Enemy
    """

    VERSUS_RESULT_SCREEN = word(0x100108)
    """
    [16-bit] [Boolean] Versus | Result Screen
    0x1 = In Result Screen
    """

    VERSUS_READY_TIMER = word(0x100118)
    """
    [16-bit] Versus | Ready Timer
    0x1-0x8b = Ready Timer
    0x0 = Battle Started
    """

    VERSUS_READY_STATE = word(0x10011a)
    """
    [16-bit] Versus | Ready State
    0x3 = Readying
    0x4 = Battle Started
    """

    BATTLE_G_HALL = word(0x10025c)
    """
    [16-bit] Battle | G-Hall
    0x6 = King
    0x7 = Volcano
    0x8 = Water
    0x9 = Canyon
    0x10 = G-Live (VS)
    0xa = Elekick
    0xb = Harmonic
    0xd = Training (VS)
    0xc = Okuman
    0xe = G-Live (CoroCoro Cup)
    0xf = Tutorial
    0x14 = G-Live (Story)
    0x3f = Zoff Pass (Daichi)
    0x49 = Underground Lab (Zeke)
    0x4a = Underground (Return It)
    """

    BATTLE_TRAPS = word(0x10025e)
    """
    [16-bit] [Boolean] Battle | Traps
    """

    BATTLE_MODE = word(0x100260)
    """
    [16-bit] Battle | Mode
    0x0 = VS CPU
    0x3 = Training
    0x4 = Tutorial
    0x5 = Story
    """

    BATTLE_PLAYER_CHARACTER = word(0x100262)
    """
    [16-bit] Battle | Player Character
    0x0 = Hibito
    0x1 = Guy
    0x2 = Daichi
    0x3 = Kyle
    0x4 = Zeke
    0x5 = Cross
    0x6 = Raio
    0x7 = Jet
    0x8 = Neon
    0x9 = Kamzou
    """

    BATTLE_ENEMY_CHARACTER = word(0x100264)
    """
    [16-bit] Battle | Enemy Character
    0x0 = Hibito
    0x1 = Guy
    0x2 = Daichi
    0x3 = Kyle
    0x4 = Zeke
    0x5 = Cross
    0x6 = Raio
    0x7 = Jet
    0x8 = Neon
    0x9 = Kamzou
    0xa = Ichiman
    0xb = Ask (Trainer)
    0xd = Saike
    0xf = Nemuemi
    0x11 = Blue Nor
    0x12 = Doum
    0x13 = Gamuran
    0x14 = Sho
    0x15 = Linda
    0x16 = Mamesh
    0x17 = McDou
    0x18 = Pokina
    """

    BATTLE_PLAYER_COLOR = word(0x100266)
    """
    [16-bit] Battle | Player Color
    """

    BATTLE_ENEMY_COLOR = word(0x100268)
    """
    [16-bit] Battle | Enemy Color
    """

    BATTLE_FRAME_TIMER = dword(0x1004ac)
    """
    [32-bit] Battle | Frame Timer
    Frames elapsed during current quest map or battle
    Affects the time left at the top of the screen
    Time is not in seconds
    1 unit = 110 frames
    """

    BATTLE_TIME_LIMIT = word(0x1004b0)
    """
    [16-bit] [Boolean] Battle | Time Limit
    0x0 = Time Limited
    0x1 = Infinite Time
    """

    BATTLE_TIMER = word(0x1004b2)
    """
    [16-bit] Battle | Timer
    "Seconds" left in quest or battle displayed on top of the screen
    Not actual seconds
    1 unit = 110 frames
    """

    INGAME_DATA_POINTER = tbyte(0x106f1c)
    """
    [24-bit Pointer] Ingame Data Pointer
    Always point to 0x23b7e0
    0x0 when no script is loaded
    """

    ENEMY_HEALTH_1 = word(0x111edc)
    """
    [16-bit] Enemy (Quest) | Health
    Seems to always be the first active/loaded enemy
    """

    EVENT_FLAG_BUFFER = (0x23bb28)
    """
    [40 bytes] Event Flag Buffer
    Initialized when $0x106f1c != 0x0
    Copy buffer of  $0xed4c4 - $0xed4e8
    Overwrites save data on level transition
    """

    CURRENT_SCRIPT_ID = word(0x23bb70)
    """
    [16-bit] Current Script ID
    Use when $0xeac50 != 0x0

    0x0 = Tutorial
    // Story
    0x01-0x0d = King's Area
    0x0e-0x15 = Elekick Area
    0x16-0x17 = Goshi Desert
    0x18-0x1a = King's Area
    0x1b-0x1e = Water Area
    0x1f-0x25 = Volcano Area
    0x26-0x28 = Saru Ruins
    0x29-0x2c = Canyon Area
    0x2d-0x35 = Harmonic Area
    0x36-0x3e = Elekick Area
    0x3f-0x45 = Water Area
    0x46 = Matter Energy Lab
    0x47-0x48 = King's Area
    0x49-0x5b = Okuman Land
    0x5c-0x5f = Zoff Pass
    0x60-0x65 = Canyon Area
    0x66-0x68 = Ghost Underground
    0x69-0x6a = King's Area
    0x6b = Matter Energy Lab
    0x6c-0x6d = King's Area
    0x6e-0x74 = Harmonic Area
    0x75-0x77 = Win Desert
    0x78-0x7e = Water Area
    0x7f-0x82 = Volcano Area
    0x83-0x89 = Elekick Area
    0x8a-0x8c = Kenmeri Forest
    0x8d-0x90 = Harmonic Area
    0x91-0x93 = Iwaku Pass
    0x94-0x9c = Canyon Area
    0x9d-0x9f = Poshka Ruins
    0xa0-0xa2 = King's Area
    0xa3-0xa9 = Volcano Area
    0xaa-0xaf = King's Area
    0xb0-0xb1 = Matter Energy Lab
    0xb2-0xb4 = Underground Lab
    0xb5-0xb7 = Deep Underground Lab
    0xb8-0xb9 = Underground Lab Core
    0xba-0xbc = Matter Energy Lab
    0xbd-0xc0 = King's Area (Final Fight)
    0xc1-0xc2 = Credits

    // Quest Cutscenes
    0xc3 = Dora Desert (Mirage Egg)
    0xc4 = Korman Forest (Dropped DS)
    0xc5 = Urakko Pass (My Treasure)

    // Quests
    0xc6 = King's Area (Hibito Fight)
    0xc7 = Elekick Area (Round 1)
    0xc8-0xcd = Goshi Desert
    0xce = Volcano Area (Round 2)
    0xcf-0xd7 = Saru Ruins
    0xd8 = Harmonic Area (Round 3)
    0xd9 = Elekick Area (Guy)
    0xda = Water Area (Round 4)
    0xdb-0xdf = Okuman Land
    0xe0-0xe6 = Zoff Pass
    0xe7 = Canyon Area (Round 5)
    0xe8-0xf3 = Ghost Underground
    0xf4 = Harmonic Area (Round 6)
    0xf5 = Win Desert
    0xf6 = Water Area (Round 7)
    0xf7 = Volcano Area (Round 8)
    0xf8-0x10d = Kenmeri Forest
    0x10e = Iwaku Pass
    0x10f = Canyon Area (Round 9)
    0x110-0x122 = Poshka Ruins
    0x123 = Volcano Area (Round 10)
    0x124-0x12b = Underground Lab
    0x12c = Underground Lab (Zeke)
    0x134 = Deep Underground Lab (Variant)
    0x12d-0x139 = Deep Underground Lab
    0x13a-0x155 = Underground Lab Core
    0x156 = Underground Lab Core (King)
    0x157 = King's Area (Evil One)
    0x158-0x15f = Dora Desert (Mirage Egg)
    0x160 = Underground Hideout (Return It)
    0x161-0x175 = Korman Forest (DS Dropped)
    0x176 = Delhezi Ruins (DoraDora)
    0x177-0x17f = Urakko Pass (My Treasure)
    0x180 = G-Live (Change Beat!)
    0x181 = Underground Lab Core (Charismatic Grapper)
    0x182 = Underground Lab Core (Mysterious Grapper)
    0x183 = Underground Hideout (Goril's Roar)
    0x184 = Delhezi Ruins (Goril's Roar+)
    0x185 = Win Desert (Goril's Rage)
    0x186 = Polka Forest (Final Goril)
    0x187-0x18c = Goshi Desert (Arman Ranger)
    0x18d-0x198 = Underground Hideout (Arman Soldier)
    0x199-0x19f = Zoff Pass (Golden Arman)
    0x1a0-0x1b2 = Poshka Ruins (Ultimate Arman)
    0x1b3-0x1bb = King's Area (Sudden Death)
    0x1bc = G-Center (Quest Reward)
    0x1bd = G-Center (Quest Failed)

    // Overworld
    0x1be-0x1c9 = King's Area
    0x1ca-0x1d8 = Volcano Area
    0x1d9-0x1e7 = Water Area
    0x1e8-0x1f5 = Canyon Area
    0x1f6-0x204 = Elekick Area
    0x205-0x213 = Harmonic Area
    0x214-0x21b = Matter Energy Lab
    0x21c-0x21d = Okuman Land
    0x21e-0x21f = Challenge Area
    0x220 = Underground Lab
    0x221 = Deep Underground Lab
    0x222 = G-Live (Battle)
    0x223 = G-Live (Win)
    0x224 = G-Live (Lose)
    0x225-0x230 = Challenge Area

    // Misc
    0x231-0x24f = GNN
    0x250 = Area Selection
    0x251 = Title Screen
    """

    GLOBAL_FRAME_COUNTER = dword(0x3ffc3c)
    """
    [32-bit] Global Frame Counter
    """

