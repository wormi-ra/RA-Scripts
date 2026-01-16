from pycheevos.core.helpers import *

class Memory:
    ENTITY_DATA_ARRAY_COUNT = byte(0x04b005)
    """
    [8-bit] Entity Data | Array Count
    """

    ENTITY_DATA = (0x04b010)
    """
    [28672 bytes] [Array] Entity Data
    | [112 bytes] Entity Data Structure
    | +0x00 = [32-bit] Graphics related data
    | +0x04 = [32-bit] Graphics related data
    | +0x1c = [16-bit] Position X
    | +0x1e = [16-bit] Position Y
    | +0x22 = [16-bit] Camera relative pos X
    | +0x24 = [16-bit] Camera relative pos Y
    | +0x57 = [8-bit] Entity state
    | +0x59 = [8-bit] Entity substate
    | +0x61 = [8-bit] Health
    | +0x6c = [8-bit] [Bitfield] Pickup state
    | -- bit4 = Not Collected
    """

    ENTITY_DATA_DREAM_FOREST_ARRAY_COUNT = byte(0x054005)
    """
    [8-bit] Entity Data | Dream Forest | Array Count
    """

    ENTITY_DATA_DREAM_FOREST = (0x054010)
    """
    [28672 bytes] [Array] Entity Data | Dream Forest
    Memory range specific to world 1 (Dream Forest)
    | [112 bytes] Entity Data Structure
    | +0x00 = [32-bit] Graphics related data
    | +0x04 = [32-bit] Graphics related data
    | +0x1c = [16-bit] Position X
    | +0x1e = [16-bit] Position Y
    | +0x22 = [16-bit] Camera relative pos X
    | +0x24 = [16-bit] Camera relative pos Y
    | +0x57 = [8-bit] Entity state
    | +0x59 = [8-bit] Entity substate
    | +0x61 = [8-bit] Health
    | +0x6c = [8-bit] [Bitfield] Pickup state
    | -- bit4 = Not Collected
    """

    LEVEL_INFO_PINK_PLANT_WOODS = (0x18f908)
    """
    [20 bytes] [Array] Level Info | Pink Plant Woods
    |0x00 = [8-Bit] Cages unlocked count
    |0x01 = [8-Bit] [Bitfield] Level state
    -- bit7 = Unlocked
    -- bit6 = Visible
    |0x02 = [8-Bit] Starting map ID
    |0x03 = [8-Bit] World ID
    """

    LEVEL_INFO_ANGUISH_LAGOON = (0x18f91c)
    """
    [20 bytes] Level Info | Anguish Lagoon
    """

    LEVEL_INFO_THE_SWAMPS_OF_FORGETFULNESS = (0x18f930)
    """
    [20 bytes] Level Info | The Swamps of Forgetfulness
    """

    LEVEL_INFO_MOSKITOS_NEST = (0x18f944)
    """
    [20 bytes] Level Info | Moskito's Nest
    """

    LEVEL_INFO_BONGO_HILLS = (0x18f958)
    """
    [20 bytes] Level Info | Bongo Hills
    """

    LEVEL_INFO_ALLEGRO_PRESTO = (0x18f96c)
    """
    [20 bytes] Level Info | Allegro Presto
    """

    LEVEL_INFO_GONG_HEIGHTS = (0x18f980)
    """
    [20 bytes] Level Info | Gong Heights
    """

    LEVEL_INFO_MR_SAXS_HULLABALLO = (0x18f994)
    """
    [20 bytes] Level Info | Mr Sax's Hullaballo
    """

    LEVEL_INFO_TWILIGHT_GULCH = (0x18f9a8)
    """
    [20 bytes] Level Info | Twilight Gulch
    """

    LEVEL_INFO_THE_HARD_ROCKS = (0x18f9bc)
    """
    [20 bytes] Level Info | The Hard Rocks
    """

    LEVEL_INFO_MR_STONES_PEAKS = (0x18f9d0)
    """
    [20 bytes] Level Info | Mr Stone's Peaks
    """

    LEVEL_INFO_ERASER_PLAINS = (0x18f9e4)
    """
    [20 bytes] Level Info | Eraser Plains
    """

    LEVEL_INFO_PENCIL_PENTATHLON = (0x18f9f8)
    """
    [20 bytes] Level Info | Pencil Pentathlon
    """

    LEVEL_INFO_SPACE_MAMAS_CRATER = (0x18fa0c)
    """
    [20 bytes] Level Info | Space Mama's Crater
    """

    LEVEL_INFO_CRYSTAL_PALACE = (0x18fa20)
    """
    [20 bytes] Level Info | Crystal Palace
    """

    LEVEL_INFO_EAT_AT_JOES = (0x18fa34)
    """
    [20 bytes] Level Info | Eat at Joe's
    """

    LEVEL_INFO_MR_SKOPS_STALACTITES = (0x18fa48)
    """
    [20 bytes] Level Info | Mr Skops' Stalactites
    """

    LEVEL_INFO_MR_DARKS_DARE = (0x18fa5c)
    """
    [20 bytes] Level Info | Mr Dark's Dare
    """

    INGAME_PAUSED = byte(0x1a4ba7)
    """
    [8-bit] [Boolean] Ingame | Paused
    0x0 = False
    0x1 = True
    """

    BONUS_LEVEL_TIMER = word(0x1a4ca2)
    """
    [16-bit] Bonus Level | Timer
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

    RAYMAN_HITPOINTS = byte(0x1a6d91)
    """
    [8-bit] Rayman | Hitpoints
    0x0 = 1 hp
    0x1 = 2 hp
    0x2 = 3 hp
    0x3 = 4 hp
    0x4 = 5 hp
    """

    STATE_GAME_OVER = byte(0x1a6eb1)
    """
    [8-bit] [Boolean] State | Game Over
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

