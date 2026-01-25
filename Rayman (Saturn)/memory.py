from pycheevos.core.helpers import *
from dataclasses import dataclass

@dataclass(frozen=True)
class Memory:
    SET_CREATED_WITH_THE_HELP_OF_PYCHEEVOS_SCRIPTS = (0x000000)
    """
    [Notes] Set created with the help of PyCheevos scripts
    See github below for source code and further information
    https://github.com/wormi-ra/RA-Scripts/tree/main/Rayman%20(Saturn)

    Helpful resources:

    - RayMap
    https://raym.app/maps_r1/index.html?mode=RaymanSaturnUS&folder=r1/saturn_us
    raym.app is a map viewer for every rayman games and versions, it is a great tool to identify level IDs, entity IDs and state IDs in a level

    - Ray1 BinarySerializer
    https://github.com/BinarySerializer/BinarySerializer.Ray1/tree/main/src/BinarySerializer.Ray1/DataTypes
    Definition of most data types used in Rayman 1, this repository mostly contains types for the PS1 and PC versions, so not guaranteed to be exact, but most types can be applied to the Saturn version

    Memory layout:
    Most static game variables and useful adresses are found in the high work RAM region (0x100000-0x1fffff)
    The low work RAM region contains entity data at adresses 0x54000 for the first world (Dream forest) and 0x4b000 for the other worlds
    """

    ENTITY_DATA = (0x04b000)
    """
    [28672 bytes] [Array] Entity Data
    Memory range specific to world 2-6 (All except Dream Forest)
    | [112 bytes] Entity Data Structure
    | 0x10 = [32-bit Pointer] Sprite data
    | 0x14 = [32-bit Pointer] Animation data
    | 0x18 = [32-bit Pointer] Image buffer data
    | 0x1c = [32-bit Pointer] Script related data
    | 0x20 = [32-bit Pointer] Script related data
    | 0x24 = [32-bit Pointer] Script related data
    | 0x28 = [32-bit Pointer] Script related data
    | 0x2c = [16-bit] Position X
    | 0x2e = [16-bit] Position Y
    | 0x30 = [16-bit] Entity ID
    | 0x32 = [16-bit] Camera relative pos X
    | 0x34 = [16-bit] Camera relative pos Y
    | 0x38 = [16-bit] Initial position X
    | 0x3a = [16-bit] Initial position Y
    | 0x3c = [16-bit] Velocity X
    | 0x3e = [16-bit] Velocity Y
    | 0x48 = [16-bit] Follow Y
    | 0x4a = [16-bit] Follow X
    | 0x64 = [8-bit] Animation frame
    | 0x65 = [8-bit] Animation index
    | 0x67 = [8-bit] Animation state
    | - Always use in combination with substate
    | - Check possible values in raym.app
    | 0x69 = [8-bit] Animation substate
    | 0x71 = [8-bit] Health
    | 0x7c = [8-bit] [Bitfield] Flags
    | - bit5 = Alive
    | - bit4 = Active
    | - bit2 = Active (alt)?
    | - bit1 = Flip X
    """

    ENTITY_DATA_DREAM_FOREST = (0x054000)
    """
    [28672 bytes] [Array] Entity Data | Dream Forest
    Memory range specific to world 1 (Dream Forest)
    | [112 bytes] Entity Data Structure
    | 0x10 = [32-bit Pointer] Sprite data
    | 0x14 = [32-bit Pointer] Animation data
    | 0x18 = [32-bit Pointer] Image buffer data
    | 0x1c = [32-bit Pointer] Script related data
    | 0x20 = [32-bit Pointer] Script related data
    | 0x24 = [32-bit Pointer] Script related data
    | 0x28 = [32-bit Pointer] Script related data
    | 0x2c = [16-bit] Position X
    | 0x2e = [16-bit] Position Y
    | 0x30 = [16-bit] Entity ID
    | 0x32 = [16-bit] Camera relative pos X
    | 0x34 = [16-bit] Camera relative pos Y
    | 0x38 = [16-bit] Initial position X
    | 0x3a = [16-bit] Initial position Y
    | 0x3c = [16-bit] Velocity X
    | 0x3e = [16-bit] Velocity Y
    | 0x48 = [16-bit] Follow Y
    | 0x4a = [16-bit] Follow X
    | 0x64 = [8-bit] Animation frame
    | 0x65 = [8-bit] Animation index
    | 0x67 = [8-bit] Animation state
    | - Always use in combination with substate
    | - Check possible values in raym.app
    | 0x69 = [8-bit] Animation substate
    | 0x71 = [8-bit] Health
    | 0x7c = [8-bit] [Bitfield] Flags
    | - bit5 = Alive
    | - bit4 = Active
    | - bit2 = Active (alt)?
    | - bit1 = Flip X
    """

    CUTSCENE_TIMER = word(0x0a28b2)
    """
    [16-bit] Cutscene Timer
    """

    STATE_WATCHING_CUTSCENE = byte(0x0a28e2)
    """
    [8-bit] [Boolean] State | Watching Cutscene
    """

    LEVEL_INFO_PINK_PLANT_WOODS = (0x18f900)
    """
    [480 bytes] [Array] Level Info | Pink Plant Woods
    | [20 bytes] Level Info Structure
    | 0x00 = [16-bit] Map position X
    | 0x02 = [16-bit] Map position Y
    | 0x04 = [8-bit] Map index up
    | 0x05 = [8-bit] Map index left
    | 0x06 = [8-bit] Map index down
    | 0x07 = [8-bit] Map index right
    | 0x08 = [8-bit] Cages unlocked count
    | 0x09 = [8-bit] [Bitfield] Level state
    | - bit7 = Unlocked
    | - bit6 = Visible
    | - bit5 = Waiting unlock animation
    | 0x0a = [8-bit] Starting map ID
    | 0x0b = [8-bit] World ID
    | 0x1d = [8-bit] Level text color
    | 0x10 = [32-bit Pointer] Level name
    """

    LEVEL_INFO_ANGUISH_LAGOON = (0x18f914)
    """
    [20 bytes] Level Info | Anguish Lagoon
    """

    LEVEL_INFO_THE_SWAMPS_OF_FORGETFULNESS = (0x18f928)
    """
    [20 bytes] Level Info | The Swamps of Forgetfulness
    """

    LEVEL_INFO_MOSKITOS_NEST = (0x18f93c)
    """
    [20 bytes] Level Info | Moskito's Nest
    """

    LEVEL_INFO_BONGO_HILLS = (0x18f950)
    """
    [20 bytes] Level Info | Bongo Hills
    """

    LEVEL_INFO_ALLEGRO_PRESTO = (0x18f964)
    """
    [20 bytes] Level Info | Allegro Presto
    """

    LEVEL_INFO_GONG_HEIGHTS = (0x18f978)
    """
    [20 bytes] Level Info | Gong Heights
    """

    LEVEL_INFO_MR_SAXS_HULLABALLO = (0x18f98c)
    """
    [20 bytes] Level Info | Mr Sax's Hullaballo
    """

    LEVEL_INFO_TWILIGHT_GULCH = (0x18f9a0)
    """
    [20 bytes] Level Info | Twilight Gulch
    """

    LEVEL_INFO_THE_HARD_ROCKS = (0x18f9b4)
    """
    [20 bytes] Level Info | The Hard Rocks
    """

    LEVEL_INFO_MR_STONES_PEAKS = (0x18f9c8)
    """
    [20 bytes] Level Info | Mr Stone's Peaks
    """

    LEVEL_INFO_ERASER_PLAINS = (0x18f9dc)
    """
    [20 bytes] Level Info | Eraser Plains
    """

    LEVEL_INFO_PENCIL_PENTATHLON = (0x18f9f0)
    """
    [20 bytes] Level Info | Pencil Pentathlon
    """

    LEVEL_INFO_SPACE_MAMAS_CRATER = (0x18fa04)
    """
    [20 bytes] Level Info | Space Mama's Crater
    """

    LEVEL_INFO_CRYSTAL_PALACE = (0x18fa18)
    """
    [20 bytes] Level Info | Crystal Palace
    """

    LEVEL_INFO_EAT_AT_JOES = (0x18fa2c)
    """
    [20 bytes] Level Info | Eat at Joe's
    """

    LEVEL_INFO_MR_SKOPS_STALACTITES = (0x18fa40)
    """
    [20 bytes] Level Info | Mr Skops' Stalactites
    """

    LEVEL_INFO_MR_DARKS_DARE = (0x18fa54)
    """
    [20 bytes] Level Info | Mr Dark's Dare
    """

    LEVEL_INFO_SAVE_1 = (0x18fa68)
    """
    [20 bytes] Level Info | Save 1
    """

    LEVEL_INFO_SAVE_2 = (0x18fa7c)
    """
    [20 bytes] Level Info | Save 2
    """

    LEVEL_INFO_SAVE_3 = (0x18fa90)
    """
    [20 bytes] Level Info | Save 3
    """

    LEVEL_INFO_SAVE_4 = (0x18faa4)
    """
    [20 bytes] Level Info | Save 4
    """

    LEVEL_INFO_SAVE_5 = (0x18fab8)
    """
    [20 bytes] Level Info | Save 5
    """

    LEVEL_INFO_SAVE_6 = (0x18facc)
    """
    [20 bytes] Level Info | Save 6
    """

    ENTITY_DATA_POINTER_WORLD_1 = dword(0x191914)
    """
    [32-bit ME Pointer & 0x1fffff] Entity Data Pointer | World 1
    Always point to 0x54000
    """

    ENTITY_DATA_POINTER_WORLD_2 = dword(0x191918)
    """
    [32-bit ME Pointer & 0x1fffff] Entity Data Pointer | World 2
    Always point to 0x4b000
    """

    ENTITY_DATA_POINTER_WORLD_3 = dword(0x19191c)
    """
    [32-bit ME Pointer & 0x1fffff] Entity Data Pointer | World 3
    Always point to 0x4b000
    """

    ENTITY_DATA_POINTER_WORLD_4 = dword(0x191920)
    """
    [32-bit ME Pointer & 0x1fffff] Entity Data Pointer | World 4
    Always point to 0x4b000
    """

    ENTITY_DATA_POINTER_WORLD_5 = dword(0x191924)
    """
    [32-bit ME Pointer & 0x1fffff] Entity Data Pointer | World 5
    Always point to 0x4b000
    """

    ENTITY_DATA_POINTER_WORLD_6 = dword(0x191928)
    """
    [32-bit ME Pointer & 0x1fffff] Entity Data Pointer | World 6
    Always point to 0x4b000
    """

    INGAME_LEVEL_STATE = byte(0x1a4ba3)
    """
    [8-bit] Ingame | Level State
    0x0 = Playing
    0x1 = Cage breaking animation
    0x2 = Exit sign touched
    """

    INGAME_PAUSED = byte(0x1a4ba7)
    """
    [8-bit] [Boolean] Ingame | Paused
    0x0 = False
    0x1 = True
    """

    BONUS_LEVEL_TIME_LEFT = word(0x1a4ca2)
    """
    [16-bit] Bonus Level | Time Left
    0xfffe = disabled
    Any other value = Frames left before end of the timer
    """

    LEVEL_SELECT_CURRENT_LEVEL_ID = byte(0x1a509e)
    """
    [8-bit] Level Select | Current Level ID
    0x00 = Pink Plant Woods
    0x01 = Anguish Lagoon
    0x02 = The Swamps of Forgetfulness
    0x03 = Moskito's Nest
    0x04 = Bongo Hills
    0x05 = Allegro Presto
    0x06 = Gong Heights
    0x07 = Mr Sax's Hullaballo
    0x08 = Twilight Gulch
    0x09 = The Hard Rocks
    0x0a = Mr Stone's Peaks
    0x0b = Eraser Plains
    0x0c = Pencil Pentathlon
    0x0d = Space Mama's Crater
    0x0e = Crystal Palace
    0x0f = Eat at Joe's
    0x10 = Mr Skops' Stalactites
    0x11 = Mr Dark's Dare
    0x12 = Save 1
    0x13 = Save 2
    0x14 = Save 3
    0x15 = Save 4
    0x16 = Save 5
    0x17 = Save 6
    """

    STATE_IN_LEVEL_SELECT = byte(0x1a50c7)
    """
    [8-bit] [Boolean] State | In Level Select
    """

    INGAME_FRAME_COUNTER = word(0x1a5b12)
    """
    [16-bit] Ingame | Frame counter
    Pauses when rayman is not in control, in menu, during pause, breaking cages, loading...
    """

    BONUS_LEVEL_TINGS = byte(0x1a5c2f)
    """
    [8-bit] Bonus Level | Tings
    """

    STATE_MAP_READY = byte(0x1a6c73)
    """
    [8-bit] [Boolean] State | Map Ready
    0x0 = True
    0x1 = False

    Can be used for resetting achievements, changes from 0x1 to 0x0 on map changes and respawn
    """

    LEVEL_SELECT_DESTINATION_LEVEL_ID = word(0x1a6cc4)
    """
    [16-bit] Level Select | Destination Level ID
    """

    INGAME_CURRENT_WORLD = byte(0x1a6d18)
    """
    [8-bit] Ingame | Current world
    0x1 = The Dream Forest
    0x2 = Band Land
    0x3 = Blue Mountains
    0x4 = Picture City
    0x5 = The Cave of Skops
    0x6 = Candy Chateau
    """

    NUMBER_OF_LIVES = word(0x1a6d20)
    """
    Number of Lives (16-bit)
    """

    NUMBER_OF_TINGS = byte(0x1a6d27)
    """
    Number of Tings (8-bit)
    """

    RAYMAN_POSITION_X = word(0x1a6d4c)
    """
    [16-bit] Rayman | Position X
    """

    RAYMAN_POSITION_Y = word(0x1a6d4e)
    """
    [16-bit] Rayman | Position Y
    """

    RAYMAN_VELOCITY_X = word(0x1a6d5c)
    """
    [16-bit] Rayman | Velocity X
    """

    RAYMAN_VELOCITY_Y = word(0x1a6d5e)
    """
    [16-bit] Rayman | Velocity Y
    """

    RAYMAN_ANIMATION_STATE = byte(0x1a6d87)
    """
    [8-bit] Rayman | Animation State
    Always use in combination with substate
    Check possible values in raym.app
    """

    RAYMAN_ANIMATION_SUBSTATE = byte(0x1a6d89)
    """
    [8-bit] Rayman | Animation Substate
    """

    RAYMAN_HITPOINTS = byte(0x1a6d91)
    """
    [8-bit] Rayman | Hitpoints
    0x0 = 1 hp
    0x1 = 2 hp
    0x2 = 3 hp
    0x3 = 4 hp
    0x4 = 5 hp
    """

    RAYMAN_FLAGS = byte(0x1a6d9c)
    """
    [8-bit] Rayman | Flags
    - bit5 = Alive
    - bit4 = Active
    - bit1 = Flip X
    """

    STATE_GAME_OVER = byte(0x1a6eb1)
    """
    [8-bit] [Boolean] State | Game Over
    True when on the game over screen, as well as the ending cutscene and credits
    """

    RAYMAN_RESPAWN_POSITION_X = word(0x1a6f0a)
    """
    [16-bit] Rayman | Respawn Position X
    """

    RAYMAN_RESPAWN_POSITION_Y = word(0x1a6f0c)
    """
    [16-bit] Rayman | Respawn Position Y
    """

    GENERAL_FRAME_COUNTER = word(0x1a7046)
    """
    [16-bit] General | Frame counter
    Pauses during loading times
    """

    RAYMAN_CONTINUES = byte(0x1a8593)
    """
    [8-bit] Rayman | Continues
    """

    LIFE_COUNTER_SCREEN_ANIMATION = word(0x1a97c2)
    """
    [16-bit] Life Counter Screen Animation
    0xffff = Inactive
    """

    LOADING_WORLD = byte(0x1a9f40)
    """
    [8-bit] Loading | World
    0x1 = The Dream Forest
    0x2 = Band Land
    0x3 = Blue Mountains
    0x4 = Picture City
    0x5 = The Cave of Skops
    0x6 = Candy Chateau
    """

    STATE_DEMO_PLAY = byte(0x1a9ff4)
    """
    [8-bit] [Boolean] State | Demo play
    0x0 = False
    0x1 = True
    """

    BONUS_LEVEL_TINGS_LEFT = byte(0x1ab013)
    """
    [8-bit] Bonus Level | Tings left
    """

    BONUS_LEVEL_WIN_CUTSCENE_TIMER = word(0x1ab090)
    """
    [16-bit] Bonus Level | Win cutscene timer
    0x0000 = Inactive
    0x0001 - 0x111 = Active cutscene timer
    0xffe0 - 0xfffe = Pre-cutscene timer
    """

    STATE_CURRENT_SAVE_FILE = byte(0x1ab0a2)
    """
    [8-bit] State | Current Save File
    0x0 = Main menu
    0x1 = Save 1
    0x2 = Save 2
    0x3 = Save 3
    """

    INGAME_MAP_TIMER_HIGH = word(0x1ab630)
    """
    [16-bit] Ingame | Map Timer High
    Frames spent playing on the current map
    Resets on death and map changes

    Add the high value with the low value together to obtain the total time as a 32-bit using the following formula:
    High * 0x10000 + Low
    """

    INGAME_MAP_TIMER_LOW = word(0x1ab632)
    """
    [16-bit] Ingame | Map Timer Low
    Frames spent playing on the current map
    Resets on death and map changes

    Add the high value with the low value together to obtain the total time as a 32-bit using the following formula:
    High * 0x10000 + Low
    """

    LOADING_MAP_ID = byte(0x1ab662)
    """
    [8-bit] Loading | Map ID (alt)
    Changes when loading map
    can be unreliable?
    """

    LOADING_NEXT_MAP_ID = byte(0x1ab978)
    """
    [8-bit] Loading | Next Map ID
    Changes when a map change is requested
    when hitting a sign for example
    """

    INGAME_MAP_ID = byte(0x1ac286)
    """
    [8-bit] Ingame | Map ID
    Changes when the level is actually loaded
    """

    COLLECTIBLE_PINK_PLANT_WOODS_1 = byte(0x1ac2c1)
    """
    [8-bit] [Bitfield] Collectible | Pink Plant Woods 1
    bit7 = Life
    """

    COLLECTIBLE_PINK_PLANT_WOODS_2 = byte(0x1ac2e0)
    """
    [8-bit] [Bitfield] Collectible | Pink Plant Woods 2
    bit7 = Life
    bit6 = Life
    """

    COLLECTIBLE_PINK_PLANT_WOODS_4_1 = byte(0x1ac321)
    """
    [8-bit] [Bitfield] Collectible | Pink Plant Woods 4-1
    bit7 = Life
    bit6 = Life
    bit4 = Life
    """

    COLLECTIBLE_PINK_PLANT_WOODS_4_2 = byte(0x1ac323)
    """
    [8-bit] [Bitfield] Collectible | Pink Plant Woods 4-2
    bit5 = Life
    bit2 = Life
    """

    EVENTS_BOSSES_BEATEN = byte(0x1acf2b)
    """
    [8-bit] [Bitfield] Events | Bosses beaten
    bit7 = Bzzit
    bit6 = Moskito
    bit5 = Mr Sax
    bit4 = Mr Stone
    bit3 = Pirate Mama
    bit2 = Space Mama
    bit1 = Mr Skops
    bit0 = Mr Dark
    """

    RAYMAN_MODIFIERS = byte(0x1acfc4)
    """
    [8-bit] [Bitfield] Rayman | Modifiers
    bit0 = Death?
    bit1 = Reverse controls 1
    bit2 = Reverse controls 2
    bit3 = Begin infinite run
    bit4 = Infinite run
    bit5 = Firefly light
    bit6 = Mini Rayman
    bit7 = Unlocked run ability
    """

    RAYMAN_ABILITIES = byte(0x1acfc5)
    """
    [8-bit] [Bitfield] Rayman | Abilities
    bit7 = Punch
    bit6 = Hang
    bit5 = Helicopter
    bit4 = Super helicopter
    bit3 = ?
    bit2 = ?
    bit1 = Seed
    bit0 = Grappling
    """

    RAYMAN_HELICOPTER_TIMER = word(0x1acfcc)
    """
    [16-bit] Rayman | Helicopter timer
    0xffff = not in helicopter state
    """

    STATE_INGAME = byte(0x1bfb6c)
    """
    [8-bit] [Boolean] State | Ingame
    0x0 = False
    0x1 = True
    """

