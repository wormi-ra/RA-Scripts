from pycheevos.core.helpers import *
from dataclasses import dataclass

@dataclass(frozen=True)
class Memory:
    EU_STATE_CHECK_MOVIE_PLAYING = dword(0x005da320)
    US_STATE_CHECK_MOVIE_PLAYING = dword(0x005ff3f0)
    EU_INGAME_CURRENT_LUA_SCRIPT_NAME = 0x018005b0
    US_INGAME_CURRENT_LUA_SCRIPT_NAME = 0x0180c5f8
    EU_STATE_CHECK_IS_LOADING = dword(0x0053359c)
    US_STATE_CHECK_IS_LOADING = dword(0x005f269c)

    EU_SERIAL = dword_be(0x5de0cc)
    """
    [32-bit BE ASCII] (EU) Serial
    (cdrom0:\SLES_518.43;1)
    0x534c4553 = SLES
    """

    EU_STATE_CHECK_TITLE_SCREEN_ACTIVE = dword(0x5e2008)
    """
    [32-bit] (EU) State Check | Title Screen Active
    """

    EU_STATE_CHECK_IN_MENU = dword(0x5e200c)
    """
    [32-bit] (EU) State Check | In Menu
    """

    EU_STATE_CHECK_IN_GAME = dword(0x5e2018)
    """
    [32-bit] (EU) State Check | In Game
    """

    NTSC_SERIAL = dword_be(0x6b294c)
    """
    [NTSC] | [32 Bit BE] Serial
    (cdrom0:\SLUS_208.94;1)
    """

    EU_INGAME_WORM_PLAYER_DATA_ARRAY = dword(0x6ce018)
    """
    [32-bit Pointer] (EU) Ingame | Worm Player Data Array
    +0x04
    ++0x1C
    +++0x50 = [32-bit Float] X Position
    +++0x54 = [32-bit Float] Y Position
    +++0x58 = [32-bit Float] Z Position
    +++0x80 = [32-bit] Action ID
    --- 0x00 = Waiting (End of turn?)
    --- 0x01 = Walking
    --- 0x02 = About to jump
    --- 0x03 = Jump
    --- 0x06 = Backflip
    --- 0x07 = Bonk
    --- 0x08 = Explosion recoil
    --- 0x09 = Head in ground
    --- 0x0a = Idle (Own turn)
    --- 0x0d = Drowning
    --- 0x0e = Using Jetpack
    --- 0x0f = Using Ninja rope
    --- 0x11 = Touching ground?
    --- 0x13 = Using Parachute
    --- 0x15 = Waiting (Own team turn?)
    --- 0x16 = Waiting (Enemy team turn?)
    --- 0x1b = Stunned
    --- 0x22 = Waiting (During projectile launch)?
    --- 0x24 = Frontflip
    --- 0x25 = Using teleporter
    --- 0x26 = Falling
    +++0x84 = [32-bit] Equipped Weapon ID
    --- 0x00 = Bazooka
    --- 0x01 = Grenade
    --- 0x02 = Cluster Bomb
    --- 0x04 = Dynamite
    --- 0x07 = Land Mine
    --- 0x08 = Shotgun
    --- 0x09 = Uzi
    --- 0x0a = Baseball Bat
    --- 0x0b = Prod
    --- 0x0d = Fire Punch
    --- 0x0e = Homing Missile
    --- 0x0f = Mortar
    --- 0x12 = Sheep
    --- 0x14 = Petrol Bomb
    --- 0x15 = Gas Canister
    --- 0x22 = Sticky Bomb
    --- 0x23 = Binoculars
    --- 0x27 = Girder
    --- 0x29 = Ninja Rope
    --- 0x2a = Parachute
    --- 0x2f = Teleport
    --- 0x30 = Jet Pack
    --- 0x31 = Skip Go
    --- 0x32 = Surrender
    --- 0x33 = Worm Select
    +++ 0xA4 = [32-bit] Damage taken this round
    +++0xAA = [8-bit] Worm Health
    """

    US_INGAME_WORM_PLAYER_DATA_ARRAY = dword(0x79dc00)
    """
    [32-bit Pointer] (US) Ingame | Worm Player Data Array
    +0x04
    ++0x1C
    +++0x50 = [32-bit Float] X Position
    +++0x54 = [32-bit Float] Y Position
    +++0x58 = [32-bit Float] Z Position
    +++0x80 = [32-bit] Action ID
    --- 0x00 = Waiting (End of turn?)
    --- 0x01 = Walking
    --- 0x02 = About to jump
    --- 0x03 = Jump
    --- 0x06 = Backflip
    --- 0x07 = Bonk
    --- 0x08 = Explosion recoil
    --- 0x09 = Head in ground
    --- 0x0a = Idle (Own turn)
    --- 0x0d = Drowning
    --- 0x0e = Using Jetpack
    --- 0x0f = Using Ninja rope
    --- 0x11 = Touching ground?
    --- 0x13 = Using Parachute
    --- 0x15 = Waiting (Own team turn?)
    --- 0x16 = Waiting (Enemy team turn?)
    --- 0x1b = Stunned
    --- 0x22 = Waiting (During projectile launch)?
    --- 0x24 = Frontflip
    --- 0x25 = Using teleporter
    --- 0x26 = Falling
    +++0x84 = [32-bit] Equipped Weapon ID
    --- 0x00 = Bazooka
    --- 0x01 = Grenade
    --- 0x02 = Cluster Bomb
    --- 0x04 = Dynamite
    --- 0x07 = Land Mine
    --- 0x08 = Shotgun
    --- 0x09 = Uzi
    --- 0x0a = Baseball Bat
    --- 0x0b = Prod
    --- 0x0d = Fire Punch
    --- 0x0e = Homing Missile
    --- 0x0f = Mortar
    --- 0x12 = Sheep
    --- 0x14 = Petrol Bomb
    --- 0x15 = Gas Canister
    --- 0x22 = Sticky Bomb
    --- 0x23 = Binoculars
    --- 0x27 = Girder
    --- 0x29 = Ninja Rope
    --- 0x2a = Parachute
    --- 0x2f = Teleport
    --- 0x30 = Jet Pack
    --- 0x31 = Skip Go
    --- 0x32 = Surrender
    --- 0x33 = Worm Select
    +++ 0xA4 = [32-bit] Damage taken this round
    +++0xAA = [8-bit] Worm Health
    """

    US_TEAM_STATUS_P1_SURRENDED = dword(0x79dcc0)
    """
    [32-bit Pointer] (US) Team Status | P1 Surrended
    + 0x4
    ++ 0x1c
    +++ 0x2c [32-bit] Team Surrended
    --- 0x0 = False
    --- 0x1 = True
    """

    US_TEAM_STATUS_P2_SURRENDED = dword(0x79dcc4)
    """
    [32-bit Pointer] (US) Team Status | P2 Surrended
    + 0x4
    ++ 0x1c
    +++ 0x2c [32-bit] Team Surrended
    --- 0x0 = False
    --- 0x1 = True
    """

    US_TEAM_STATUS_P3_SURRENDED = dword(0x79dcc8)
    """
    [32-bit Pointer] (US) Team Status | P3 Surrended
    + 0x4
    ++ 0x1c
    +++ 0x2c [32-bit] Team Surrended
    --- 0x0 = False
    --- 0x1 = True
    """

    US_TEAM_STATUS_P4_SURRENDED = dword(0x79dccc)
    """
    [32-bit Pointer] (US) Team Status | P4 Surrended
    + 0x4
    ++ 0x1c
    +++ 0x2c [32-bit] Team Surrended
    --- 0x0 = False
    --- 0x1 = True
    """

    STATE_CHECK_TITLE_SCREEN_ACTIVE = dword(0x79eb40)
    """
    [32 Bit] State Check | Title Screen Active
    """

    STATE_CHECK_IN_MENU = dword(0x79eb44)
    """
    [32 Bit] State Check | In Menu
    """

    STATE_CHECK_IN_GAME = dword(0x79eb50)
    """
    [32 Bit] State Check | In Game
    """

    EU_TUTORIAL1_CRATES_COLLECTED = dword(0x152834c)
    """
    [32-bit] (EU) Tutorial1 | Crates Collected
    0xffffffff = Uninitialized
    """

    EU_TUTORIAL1_SECRET_TRIGGER = dword(0x152963c)
    """
    [32-bit] (EU) Tutorial1 | Secret Trigger
    0xffffffff = Untriggered
    0x00000000 = Triggered
    """

    US_GAME_RESULTS_FREE_BATTLE_WINNER_ID = dword(0x153d1dc)
    """
    [32-bit] (US) Game Results | Free Battle Winner ID
    0xffffffff = Uninitialized
    0x0 = Player 1
    0x1 = Player 2
    0x2 = Player 3
    0x3 = Player 4
    """

    US_INGAME_CURRENT_ACTIVE_WORM_ID = dword(0x153dd1c)
    """
    [32-bit] (US) Ingame | Current Active Worm ID
    """

    US_TUTORIAL1_SECRET_TRIGGER = dword(0x153ed1c)
    """
    [32-bit] (US) Tutorial1 | Secret Trigger
    0xffffffff = Untriggered
    0x00000000 = Triggered
    """

    US_GAME_STATUS_GAME_ENDED = dword(0x154201c)
    """
    [32-bit] (US) Game Status | Game ended
    0x0 = False
    0x1 = True
    """

    LANDSCAPE_SELECTION_SMALL_OBJECTS = dword(0x154355c)
    """
    [32 Bit Pointer] Landscape Selection | Small Objects
    +0x04
    ++0x1C = [32 Bit] Small Object Amount
    --- 00 = 0%
    --- 01 = 33%
    --- 02 = 67%
    --- 03 = 100%
    """

    EU_GAME_RESULT_RECEIVED_MEDAL = dword(0x155ee7c)
    """
    [32-bit] (EU) Game Result | Received medal
    0x0 = None
    0x1 = Bronze
    0x2 = Silver
    0x3 = Gold
    """

    US_GAME_STATUS_IS_IN_INGAME_CUTSCENE = dword(0x15703bc)
    """
    [32-bit] (US) Game Status | Is in ingame cutscene
    0x0 = False
    0x1 = True
    """

    US_GAME_RESULT_RECEIVED_MEDAL = dword(0x157a9fc)
    """
    [32-bit] (US) Game Result | Received medal
    0x0 = None
    0x1 = Bronze
    0x2 = Silver
    0x3 = Gold
    """

    EU_INGAME_CURRENT_SCENARIO_NAME = dword_be(0x18005b0)
    """
    [32-bit BE ASCII] (EU) Ingame | Current scenario name
    0xdddddddd = Uninitialized
    'tutorial#' = Tutorial, # is the tutorial number
    'dday' = D-Day
    'attract' = demo
    'stdvs' = custom game
    """

    US_INGAME_CURRENT_SCENARIO_NAME = dword_be(0x180c5f8)
    """
    [32-bit BE ASCII] (US) Ingame | Current scenario name
    0xdddddddd = Uninitialized
    'tutorial#' = Tutorial, # is the tutorial number
    'dday' = D-Day
    'attract' = demo
    'stdvs' = custom game
    """

    EU_INGAME_CURRENT_ACTIVE_WORM_ID = dword(0x1ce3ef0)
    """
    [32-bit Pointer] (EU) Ingame | Current Active Worm ID
    +0x4
    ++0x1c = [32-bit] Current Active Worm ID
    """

    EU_INGAME_CURRENT_TEAM_ID_TURN = dword(0x1ce4240)
    """
    [32-bit Pointer] (EU) Ingame | Current Team ID Turn
    +0x4
    ++0x1c = [32-bit] ID of the current team
    """

    EU_GAME_RESULT_RECEIVED_MEDAL_OR_SCORE = dword(0x1ce6de8)
    """
    [32-bit Pointer] (EU) Game Result | Received medal or score
    +0x4
    ++0x1c = [32-bit] Received medal or score
    -- In Campain:
    -- 0x0 = None
    -- 0x1 = Bronze
    -- 0x2 = Silver
    -- 0x3 = Gold
    -- In Challenge: Time measured in milliseconds
    """

    EU_MODE_CONTEXT = dword(0x1ce7868)
    """
    [32-bit Pointer] (EU) Mode Context
    +0x04
    ++0x1C = [32-bit] Mode
    --- 00 = Tutorial
    --- 14 = Challenge
    --- 28 = Free Battle
    --- 32 = Campaign
    """

    GAME_OPTION_SUDDEN_DEATH_WATER_SETTING = dword(0x1cfb7f8)
    """
    [32 Bit Pointer] Game Option | Sudden Death Water Setting
    +0x04
    ++0x1C = [32 Bit] Sudden Death Water Setting
    --- 00 = Inactive
    --- 01 = Slow Speed
    --- 02 = Medium Speed
    --- 03 = Fast Speed
    """

    US_UNLOCKS_GRAVE_DANGER_MAP = dword(0x1cfb808)
    """
    [32-bit Pointer] (US) Unlocks | Grave Danger Map
    +0x4
    ++0x1c
    +++0x1c = [32-bit] Grave Danger Map Flag
    --- 0x0 = Unlocked
    --- 0x1 = Locked
    """

    LANDSCAPE_SELECTION_INDESTRUCTABLE_TERRAIN = dword(0x1cfb8dc)
    """
    [32 Bit Pointer] Landscape Selection | Indestructable Terrain
    +0x04
    ++0x1C = [32 Bit] Indestructable Terrain
    --- 00 = Inactive
    --- 01 = Active
    """

    P1_INVENTORY = dword(0x1cfbab0)
    """
    [32 Bit Pointer] P1 Inventory
    +0x04
    ++0x1C
    +++0x17 = [8 Bit] Total Ammo | Gas Canister
    +++0x18 = [8 Bit] Total Ammo | Petrol Bomb
    +++0x1A = [8 Bit] Total Ammo | Sheep
    +++0x1D = [8 Bit] Total Ammo | Mortar
    +++0x1F = [8 Bit] Total Ammo | Fire Punch
    +++0x22 = [8 Bit] Total Ammo | Baseball Bat
    +++0x23 = [8 Bit] Total Ammo | Uzi
    +++0x24 = [8 Bit] Total Ammo | Shotgun
    +++0x25 = [8 Bit] Total Ammo | Land Mine
    +++0x28 = [8 Bit] Total Ammo | Dynamite
    +++0x2A = [8 Bit] Total Ammo | Cluster Bomb
    +++0x2E = [8 Bit] Total Ammo | Teleport
    +++0x30 = [8 Bit] Total Ammo | Sticky Bomb
    +++0x39 = [8 Bit] Total Ammo | Jetpack
    +++0x3F = [8 Bit] Total Ammo | Parachute
    +++0x40 = [8 Bit] Total Ammo | Ninja Rope
    +++0x42 = [8 Bit] Total Ammo | Girder
    """

    POINTER_TO_MUSIC = dword(0x1cfbd7c)
    """
    [32-bit] Pointer to Music
    +0x04 
    ++0x1c | Music Volume [Float]
    """

    GAME_OPTION_STOCKPILING = dword(0x1cfbf20)
    """
    [32 Bit Pointer] Game Option | Stockpiling
    +0x04
    ++0x1C = [32 Bit] Game Option Check
    --- 00 = Inactive
    --- 01 = Active
    --- 02 = Anti
    """

    GAME_OPTION_ROUND_TIME = dword(0x1cfbf44)
    """
    [32 Bit Pointer] Game Option | Round Time
    +0x04
    ++0x1C = [32 Bit] Round Timer
    (Values use the time values ingame).
    --- 00 = 0 Minutes
    --- 493e0 = 5 Minutes
    --- 927c0 = 10 Minutes
    --- dbba0 = 15 Minutes
    --- 124f80 = 20 Minutes
    --- 16e360 = 25 Minutes
    --- 1b7740 = 30 Minutes
    """

    GAME_OPTION_WEAPON_CRATE_CHANCE = dword(0x1cfbf84)
    """
    [32 Bit Pointer] Game Option | Weapon Crate Chance
    +0x04
    ++0x1C = [32 Bit] Weapon Crate Chance
    """

    US_INGAME_CURRENT_TEAM_ID_TURN = dword(0x1cfbf90)
    """
    [32-bit Pointer] (US) Ingame | Current Team ID Turn
    +0x4
    ++0x1c = [32-bit] ID of the current team
    """

    US_INGAME_CURRENT_ACTIVE_WORM_ID = dword(0x1cfc410)
    """
    [32-bit Pointer] (US) Ingame | Current Active Worm ID
    +0x4
    ++0x1c = [32-bit] Current Active Worm ID
    """

    P1_WORM_DATA = dword(0x1cfc430)
    """
    [32 Bit Pointer] P1 Worm Data [1]
    +0x04
    ++0x1C
    +++0x50 = [32 Bit Float] X Position
    +++0x54 = [32 Bit Float] Y Position
    +++0x58 = [32 Bit Float] Z Position
    +++0x84 = [32 Bit] Equipped Weapon ID
    --- 00 = Bazooka
    --- 01 = Grenade
    --- 02 = Cluster Bomb
    --- 04 = Dynamite
    --- 07 = Land Mine
    --- 08 = Shotgun
    --- 09 = Uzi
    --- 0a = Baseball Bat
    --- 0b = Prod
    --- 0d = Fire Punch
    --- 0e = Homing Missile
    --- 0f = Mortar
    --- 12 = Sheep
    --- 14 = Petrol Bomb
    --- 15 = Gas Canister
    --- 22 = Sticky Bomb
    --- 23 = Binoculars
    --- 27 = Girder
    --- 29 = Ninja Rope
    --- 2a = Parachute
    --- 2f = Teleport
    --- 30 = Jet Pack
    --- 31 = Skip Go
    --- 32 = Surrender
    --- 33 = Worm Select
    +++0xAA = [8 Bit] Worm Health
    """

    P1_WORM_DATA = dword(0x1cfc434)
    """
    [32 Bit Pointer] P1 Worm Data [2]
    """

    P1_WORM_DATA = dword(0x1cfc438)
    """
    [32 Bit Pointer] P1 Worm Data [3]
    """

    P1_WORM_DATA = dword(0x1cfc43c)
    """
    [32 Bit Pointer] P1 Worm Data [4]
    """

    P1_WORM_DATA = dword(0x1cfc440)
    """
    [32 Bit Pointer] P1 Worm Data [5]
    """

    P1_WORM_DATA = dword(0x1cfc444)
    """
    [32 Bit Pointer] P1 Worm Data [6]
    """

    ROUND_TIMER = dword(0x1cfc458)
    """
    [32 Bit Pointer] Round Timer
    +0x04
    ++0x1C = [32 Bit] Round Timer
    """

    GAME_OPTION_ROUND_TIME_DISPLAY = dword(0x1cfc708)
    """
    [32 Bit Pointer] Game Option | Round Time Display
    +0x04
    ++0x1C = [32 Bit] Game Option Check
    --- 00 = Inactive
    --- 01 = Active
    """

    COMPLETION_ATLANTIS_TRAINING_FACILITY = dword(0x1cfcb3c)
    """
    [32 Bit Pointer] Completion - Atlantis Training Facility
    +0x04
    ++0x58
    +++0x40 - Team 1
    +++0x44 - Team 2
    +++0x50 - Team 3
    +++0x58 - Team 4
    +++0x5C - Team 5
    +++0x60 - Team 6
    +++0x64 - Team 7
    +++0x68 - Team 8
    +++0x6C - Team 9
    +++0x70 - Team 10
    +++0x74 - Team 11
    +++0x78 - Team 12
    +++0x7C - Team 13
    +++0x80 - Team 14
    +++0x84 - Team 15
    +++0x88 - Team 16
    +++0x8C - Team 17
    ++++0x30 = [32 Bit] Levels Completion Progression | Tutorial
    --- 00 = None
    --- 01 = Completed Atlantis Training Facility
    --- 02 = Completed Down in the Dumps
    --- 03 = Completed Return to Chateau Assassin
    --- 04 = Completed The Mighty Kong
    --- 05 = Completed Test Tubes
    --- 06 = Completed The Driving Range
    ++++0x40 = [32 Bit] Profile Selected Check
    --- 00 = Inactive
    --- 01 = Active
    """

    GAME_OPTION_SUDDEN_DEATH = dword(0x1cfd150)
    """
    [32 Bit Pointer] Game Option | Sudden Death
    +0x04
    ++0x1C = [32 Bit] Game Option Check
    --- 00 = Round Time Expiry Triggers Sudden Death
    --- 01 = 1 Health Point Sudden Death
    --- 02 = Sudden Death Rises Water
    --- 03 = No Sudden Death
    """

    GAME_OPTION_HEALTH_CRATE_CHANCE = dword(0x1cfd2c4)
    """
    [32 Bit Pointer] Game Option | Health Crate Chance
    +0x04
    ++0x1C = [32 Bit] Health Crate Chance
    """

    MODE_CONTEXT = dword(0x1cfd678)
    """
    [32 Bit Pointer] Mode Context
    +0x04
    ++0x1C = [32 Bit] Mode
    --- 00 = Tutorial
    --- 14 = Challenge
    --- 28 = Free Battle
    --- 32 = Campaign
    """

    LANDSCAPE_SELECTION_OBJECT_QUANTITY = dword(0x1cfd93c)
    """
    [32 Bit Pointer] Landscape Selection | Object Quantity
    +0x04
    ++0x1C = [32 Bit] Object Quantity Amount
    --- 00 = 0%
    --- 01 = 33%
    --- 02 = 67%
    --- 03 = 100%
    """

    TURN_TIMER = dword(0x1cfdccc)
    """
    [32 Bit Pointer] Turn Timer
    +0x04
    ++0x1C = [32 Bit] Turn Timer
    """

    GAME_OPTION_NUMBER_OF_ROUND_WINS = dword(0x1cfdd3c)
    """
    [32 Bit Pointer] Game Option | Number of Round Wins
    +0x04
    ++0x1C = [32 Bit] Number of Rounds Required to Win Match
    """

    GAME_OPTION_WORM_HEALTH = dword(0x1cfdf90)
    """
    [32 Bit Pointer] Game Option | Worm Health
    +0x04
    ++0x1C = [32 Bit] Worm Health Amount
    """

    GAME_OPTION_WORM_SELECT = dword(0x1cfe0a0)
    """
    [32 Bit Pointer] Game Option | Worm Select
    +0x04
    ++0x1C = [32 Bit] Game Option Check
    --- 00 = Inactive
    --- 01 = Active
    """

    GAME_OPTION_MINE_FUSE_SETTING = dword(0x1cfe0c4)
    """
    [32 Bit Pointer] Game Option | Mine Fuse Setting
    +0x04
    ++0x1C = [32 Bit] Game Option Check
    --- 00 = Instant
    --- 01 = Random
    """

    GAME_OPTION_FALL_DAMAGE = dword(0x1cfe1a0)
    """
    [32 Bit Pointer] Game Option | Fall Damage
    +0x04
    ++0x1C = [32 Bit] Game Option Check
    --- 00 = Inactive
    --- 01 = Active
    """

    GAME_OPTION_HOT_SEAT = dword(0x1cfe8c0)
    """
    [32 Bit Pointer] Game Option | Hot Seat
    +0x04
    ++0x1C = [32 Bit] Hot Seat Timer
    (Values use the time values ingame).
    --- 00 = 0 Seconds
    --- 1388 = 5 Seconds
    --- 2710 = 10 Seconds
    --- 3a98 = 15 Seconds
    """

    GAME_OPTION_PLACEMENT = dword(0x1cfeaa8)
    """
    [32 Bit Pointer] Game Option | Placement
    +0x04
    ++0x1C = [32 Bit] Game Option Check
    --- 00 = Random
    --- 01 = Manual
    """

    LANDSCAPE_SELECTION_LAND_HEIGHT = dword(0x1cfee44)
    """
    [32 Bit Pointer] Landscape Selection | Land Height
    +0x04
    ++0x1C = [32 Bit] Land Height Amount
    --- 00 = 0%
    --- 01 = 25%
    --- 02 = 50%
    --- 03 = 75%
    --- 04 = 100%
    """

    SELECTED_LANGUAGE = dword(0x1cff5c8)
    """
    [32 Bit Pointer] Selected Language
    +0x04
    ++0x1C = [Lower4] Selected Language
    --- 00 = Unselected
    --- 01 = English
    --- 03 = French
    """

    GAME_OPTION_UTILITY_CRATE_CHANCE = dword(0x1cff744)
    """
    [32 Bit Pointer] Game Option | Utility Crate Chance
    +0x04
    ++0x1C = [32 Bit] Utility Crate Chance
    """

    GAME_OPTION_UTILITY_CRATE_CHANCE = dword(0x1cff74c)
    """
    [32 Bit Pointer] Game Option | Utility Crate Chance
    +0x04
    ++0x1C = [32 Bit] Landscape Seed
    """

    LANDSCAPE_SELECTION_LAND_BLOCK_SIZE = dword(0x1cffb44)
    """
    [32 Bit Pointer] Landscape Selection | Land Block Size
    +0x04
    ++0x1C = [32 Bit] Land Block Size Amount
    --- 00 = 0%
    --- 01 = 17%
    --- 02 = 33%
    --- 03 = 50%
    --- 04 = 67%
    --- 05 = 83%
    --- 06 = 100%
    """

    LANDSCAPE_SELECTION_LAND_DISTANCE = dword(0x1cffb48)
    """
    [32 Bit Pointer] Landscape Selection | Land Distance
    +0x04
    ++0x1C = [32 Bit] Land Distance Amount
    --- 00 = 0%
    --- 01 = 50%
    --- 02 = 100%
    """

    XOM_LEVEL_ASCII = dword(0x1cfff04)
    """
    [32 Bit Pointer] .XOM Level ASCII
    +0x04
    ++0x1C
    +++0x00 = [32 Bit BE] Level ID 1
    --- 54617267 = 'TargetHunt.xom' | Challenge - 
    --- 64646179 = 'dday.xom' | Campaign - D-Day
    --- 64726976 = 'driving.xom' | Tutorial - The Driving Range
    --- 706c6561 = 'pleasenomoreislands.xom' | Deathmatch - Please No More Islands
    +++0x05 = [32 Bit BE] Level ID 2
    --- 69616c31 = 'tutorial1' | Tutorial - Atlantis Training Facility
    --- 69616c32 = 'tutorial2' | Tutorial - Down in the Dumps
    --- 69616c33 = 'tutorial3' | Tutorial - Return to Chateau Assassin
    --- 69616c34 = 'tutorial4' | Tutorial - The Mighty Kong
    --- 69616c35 = 'tutorial5' | Tutorial - Test Tubes
    """

    POINTER_TO_SFX = dword(0x1cfffd0)
    """
    [32-bit] Pointer to SFX
    +0x04 
    ++0x1c | SFX Volume [Float]
    """

    LANDSCAPE_SELECTION_AMOUNT_OF_LAND = dword(0x1d00040)
    """
    [32 Bit Pointer] Landscape Selection | Amount of Land
    +0x04
    ++0x1C = [32 Bit] Land Amount
    --- 00 = 0%
    --- 01 = 14%
    --- 02 = 29%
    --- 03 = 43%
    --- 04 = 57%
    --- 05 = 71%
    --- 06 = 86%
    --- 07 = 100%
    """

    GAME_OPTION_OBJECTS = dword(0x1d00158)
    """
    [32 Bit Pointer] Game Option | Objects
    +0x04
    ++0x1C = [32 Bit] Game Option Check
    --- 00 = None Active
    --- 01 = Mine Only
    --- 02 = Oil Drum Only
    --- 03 = All Active
    """

    LANDSCAPE_SELECTION_TIME_OF_DAY_TOGGLE = dword(0x1d005c4)
    """
    [32 Bit Pointer] Landscape Selection | Time of Day Toggle
    +0x04
    ++0x1C = [32 Bit] Time of Day
    --- 00 = Day
    --- 01 = Rain
    --- 02 = Night
    """

    GAME_OPTION_HEALTH_IN_CRATES = dword(0x1d00604)
    """
    [32 Bit Pointer] Game Option | Health in Crates
    +0x04
    ++0x1C = [32 Bit] Health Amount
    """

    WORMPOT_REEL_1 = dword(0x1d00864)
    """
    [32 Bit Pointer] Wormpot | Reel 1
    +0x04
    ++0x1C = [32 Bit] Wormpot ID
    """

    WORMPOT_REEL_2 = dword(0x1d00868)
    """
    [32 Bit Pointer] Wormpot | Reel 2
    +0x04
    ++0x1C = [32 Bit] Wormpot ID
    """

    WORMPOT_REEL_3 = dword(0x1d0086c)
    """
    [32 Bit Pointer] Wormpot | Reel 3
    +0x04
    ++0x1C = [32 Bit] Wormpot ID
    """

    GAME_OPTION_RETREAT_TIME = dword(0x1d00ac0)
    """
    [32 Bit Pointer] Game Option | Retreat Time
    +0x04
    ++0x1C = [32 Bit] Retreat Timer
    (Values use the time values ingame).
    --- 00 = 0 Seconds
    --- bb8 = 3 Seconds
    --- 1388 = 5 Seconds
    --- 2710 = 10 Seconds
    """

    GAME_OPTION_TURN_TIME = dword(0x1d00e84)
    """
    [32 Bit Pointer] Game Option | Turn Time
    +0x04
    ++0x1C = [32 Bit] Turn Timer
    (Values use the time values ingame).
    --- 3a98 = 15 Seconds
    --- 4e20 = 20 Seconds
    --- 7530 = 30 Seconds
    --- afc8 = 45 Seconds
    --- ea60 = 60 Seconds
    --- 15f90 = 90 Seconds
    """

    LANDSCAPE_SELECTION_BRIDGES = dword(0x1d010fc)
    """
    [32 Bit Pointer] Landscape Selection | Bridges
    +0x04
    ++0x1C = [32 Bit] Bridge Amount
    --- 00 = 0%
    --- 01 = 33%
    --- 02 = 67%
    --- 03 = 100%
    """

    US_DEMO_MODE_POINTER = dword(0x1dbe678)
    """
    [32-bit Pointer] (US) Demo mode pointer
    Pointer related to Demo mode
    Non-null if Demo mode is active
    """

    EU_DEMO_MODE_POINTER = dword(0x1e00290)
    """
    [32-bit Pointer] (EU) Demo mode pointer
    Pointer related to Demo mode
    Non-null if Demo mode is active
    """

