from pycheevos.core.helpers import *
from dataclasses import dataclass

@dataclass(frozen=True)
class Memory:
    ASSEMBLY_GAME_SPEED = byte(0x3b2550)
    """
    [8-bit] Assembly | Game Speed
    addiu a1,zero,0x28

    0x28 = 1.0x Speed
    0x14 = 0.5x Speed (50 FPS Patch)
    """

    LANGUAGE = byte(0x5c77c4)
    """
    [8-bit] Language
    0x00 = English
    0x03 = French
    0x04 = German
    0x05 = Italian
    0x09 = Spanish
    """

    GLOBAL_FRAME_COUNTER = dword(0x6f7100)
    """
    [32-bit] Global Frame Counter
    """

    GLOBAL_PLAYING_FRAME_COUNTER = dword(0x6f7104)
    """
    [32-bit] Global Playing Frame Counter
    Pauses during loading times
    """

    XDATARESOURCEMANAGER = dword(0x6f7910)
    """
    [32-bit Pointer] XDataResourceManager
    +0x18 = [32-bit Pointer] Pointer to Hashmap | XDataResourceDescriptor
    . Array of 8000 32-bit pointers in a deterministic order based on their key name
    . Always point to $0xde74c0
    . Some pointers can be null because there is more reserved slots than actual keys
    . Dump of all keys with their associated base pointers:
    . https://github.com/wormi-ra/RA-Scripts/blob/main/Worms%204%20Mayhem%20(PS2)/data/xdata.csv
    .
    . Each entry follow the same structure:
    ++0x4 = [32-bit Pointer] XDataResourceDetails
    +++0x18 = [32-bit Pointer] Key
    ++++0x0 = [ASCII] Key String
    +++0x1c = [32-bit] Data
    ... Can be a pointer or a value depending on resource type
    """

    STATE_GAME_INITIALIZED = dword(0x6fadac)
    """
    [32-bit] [Boolean] State | Game Initialized
    """

    EMPTY_STRING = byte(0x6fb77e)
    """
    [8-bit] [ASCII] Empty String
    Empty strings always points here
    0x0 = Null character
    """

    WORM_DATA_INSTANCES_ARRAY = dword(0x989d28)
    """
    [32-bit Pointer] Worm Data Instances Array [0]
    +0x4
    ++0x1c = [32-bit Pointer] WormDataContainer
    +++0x48 = [32-bit Float] Horizontal Angle
    +++0x98 = [32-bit Float] X Position
    +++0x9c = [32-bit Float] Y Position
    +++0xa0 = [32-bit Float] Z Position
    +++0xb4 = [32-bit Float] Vertical Angle
    +++0xc0 = [32-bit] Internal Timer (milliseconds)
    +++0xd8 = [32-bit] Selected Weapon
    ... 0x0 = None
    ... 0x1 = Bazooka
    ... 0x2 = Grenade
    ... 0x3 = Cluster Bomb
    ... 0x4 = Air Strike
    ... 0x5 = Dynamite
    ... 0x6 = Holy Hand Grenade
    ... 0x7 = Banana Bomb
    ... 0x8 = Land Mine
    ... 0x9 = Shotgun
    ... 0xa = Baseball Bat
    ... 0xb = Prod
    ... 0xc = Fire Punch
    ... 0xd = Homing Missile
    ... 0xe = Flood
    ... 0xf = Sheep
    ... 0x10 = Gas Canister
    ... 0x11 = Old Woman
    ... 0x12 = Concrete Donkey
    ... 0x13 = Super Sheep
    ... 0x14 = Starburst
    ... 0x15 = Custom Weapon
    ... 0x16 = Alien Abduction
    ... 0x17 = Fatkins Strike
    ... 0x18 = Inflatable Scouser
    ... 0x19 = Tail Nail
    ... 0x1a = Poison Arrow
    ... 0x1b = Sentry Gun
    ... 0x1c = Sniper
    ... 0x1d = Bovine Blitz
    ... 0x22 = Girder
    ... 0x23 = Ninja Rope
    ... 0x24 = Parachute
    ... 0x25 = Jetpack
    ... 0x26 = Skip Go
    ... 0x27 = Surrender
    ... 0x28 = Worm Select
    ... 0x29 = Icarus Potion
    ... 0x2a = Bubble Trouble
    +++0x108 = [32-bit] State
    ... 0x0 = Idle/Walking
    ... 0x1 = Preparing to jump
    ... 0x2 = Jumping
    ... 0x3 = Falling
    ... 0x4 = Climbing Step
    ... 0x5 = Using Jetpack/Parachute/Ninja Rope/Teleporter
    ... 0x6 = Inactive (Waiting for turn)
    ... 0x8 = Drowning
    +++0x110 = [8-bit] [Bitfield] Utility State
    ... Bit0 = Using Jetpack
    ... Bit1 = Using Parachute
    ... Bit3 = Using Ninja Rope
    ... Bit6 = Using Teleporter
    +++0x11e = [16-bit] Health
    +++0x12b = [8-bit] Team ID
    +++0x12f = [8-bit] [Boolean] Is Alive
    """

    WORM_DATA_INSTANCES_ARRAY_1 = dword(0x989d2c)
    """
    [32-bit Pointer] Worm Data Instances Array [1]
    """

    WORM_DATA_INSTANCES_ARRAY_2 = dword(0x989d30)
    """
    [32-bit Pointer] Worm Data Instances Array [2]
    """

    WORM_DATA_INSTANCES_ARRAY_3 = dword(0x989d34)
    """
    [32-bit Pointer] Worm Data Instances Array [3]
    """

    WORM_DATA_INSTANCES_ARRAY_4 = dword(0x989d38)
    """
    [32-bit Pointer] Worm Data Instances Array [4]
    """

    WORM_DATA_INSTANCES_ARRAY_5 = dword(0x989d3c)
    """
    [32-bit Pointer] Worm Data Instances Array [5]
    """

    WORM_DATA_INSTANCES_ARRAY_6 = dword(0x989d40)
    """
    [32-bit Pointer] Worm Data Instances Array [6]
    """

    WORM_DATA_INSTANCES_ARRAY_7 = dword(0x989d44)
    """
    [32-bit Pointer] Worm Data Instances Array [7]
    """

    WORM_DATA_INSTANCES_ARRAY_8 = dword(0x989d48)
    """
    [32-bit Pointer] Worm Data Instances Array [8]
    """

    WORM_DATA_INSTANCES_ARRAY_9 = dword(0x989d4c)
    """
    [32-bit Pointer] Worm Data Instances Array [9]
    """

    WORM_DATA_INSTANCES_ARRAY_10 = dword(0x989d50)
    """
    [32-bit Pointer] Worm Data Instances Array [10]
    """

    WORM_DATA_INSTANCES_ARRAY_11 = dword(0x989d54)
    """
    [32-bit Pointer] Worm Data Instances Array [11]
    """

    WORM_DATA_INSTANCES_ARRAY_12 = dword(0x989d58)
    """
    [32-bit Pointer] Worm Data Instances Array [12]
    """

    WORM_DATA_INSTANCES_ARRAY_13 = dword(0x989d5c)
    """
    [32-bit Pointer] Worm Data Instances Array [13]
    """

    WORM_DATA_INSTANCES_ARRAY_14 = dword(0x989d60)
    """
    [32-bit Pointer] Worm Data Instances Array [14]
    """

    WORM_DATA_INSTANCES_ARRAY_15 = dword(0x989d64)
    """
    [32-bit Pointer] Worm Data Instances Array [15]
    """

    WORM_INVENTORY_INSTANCES_ARRAY = dword(0x989d68)
    """
    [32-bit Pointer] Worm Inventory Instances Array [0]
    Worm specific inventory, only used on CPU-controlled worms in some missions.
    Note that the final ammo count for a given worm can be different, all inventory types are summed up as such:
    Final Inventory = Alliance Inventory + Team Inventory + Worm Inventory
    +0x4
    ++0x1c = [32-bit Pointer] WeaponInventory
    +++0x14 = [40 bytes] Weapon Ammo Data
    """

    WORM_INVENTORY_INSTANCES_ARRAY_1 = dword(0x989d6c)
    """
    [32-bit Pointer] Worm Inventory Instances Array [1]
    """

    WORM_INVENTORY_INSTANCES_ARRAY_2 = dword(0x989d70)
    """
    [32-bit Pointer] Worm Inventory Instances Array [2]
    """

    WORM_INVENTORY_INSTANCES_ARRAY_3 = dword(0x989d74)
    """
    [32-bit Pointer] Worm Inventory Instances Array [3]
    """

    WORM_INVENTORY_INSTANCES_ARRAY_4 = dword(0x989d78)
    """
    [32-bit Pointer] Worm Inventory Instances Array [4]
    """

    WORM_INVENTORY_INSTANCES_ARRAY_5 = dword(0x989d7c)
    """
    [32-bit Pointer] Worm Inventory Instances Array [5]
    """

    WORM_INVENTORY_INSTANCES_ARRAY_6 = dword(0x989d80)
    """
    [32-bit Pointer] Worm Inventory Instances Array [6]
    """

    WORM_INVENTORY_INSTANCES_ARRAY_7 = dword(0x989d84)
    """
    [32-bit Pointer] Worm Inventory Instances Array [7]
    """

    WORM_INVENTORY_INSTANCES_ARRAY_8 = dword(0x989d88)
    """
    [32-bit Pointer] Worm Inventory Instances Array [8]
    """

    WORM_INVENTORY_INSTANCES_ARRAY_9 = dword(0x989d8c)
    """
    [32-bit Pointer] Worm Inventory Instances Array [9]
    """

    WORM_INVENTORY_INSTANCES_ARRAY_10 = dword(0x989d90)
    """
    [32-bit Pointer] Worm Inventory Instances Array [10]
    """

    WORM_INVENTORY_INSTANCES_ARRAY_11 = dword(0x989d94)
    """
    [32-bit Pointer] Worm Inventory Instances Array [11]
    """

    WORM_INVENTORY_INSTANCES_ARRAY_12 = dword(0x989d98)
    """
    [32-bit Pointer] Worm Inventory Instances Array [12]
    """

    WORM_INVENTORY_INSTANCES_ARRAY_13 = dword(0x989d9c)
    """
    [32-bit Pointer] Worm Inventory Instances Array [13]
    """

    WORM_INVENTORY_INSTANCES_ARRAY_14 = dword(0x989da0)
    """
    [32-bit Pointer] Worm Inventory Instances Array [14]
    """

    WORM_INVENTORY_INSTANCES_ARRAY_15 = dword(0x989da4)
    """
    [32-bit Pointer] Worm Inventory Instances Array [15]
    """

    HASHMAP_SIZE = dword(0xde74b0)
    """
    [32-bit] Hashmap Size
    0x1f40 = 8000
    Hashmap starts at $0xde74c0
    """

    HASHMAP_STORYDESTRUCTANDSERVE = dword(0xde74d4)
    """
    [32-bit Pointer] Hashmap | Story.DestructAndServe
    +0x4
    ++0x1c = [32-bit Pointer] Story Mission Definition | Destruct And Serve
    .. Refer to $0xde9818
    """

    HASHMAP_LOCKTASHAFROB = dword(0xde7548)
    """
    [32-bit Pointer] Hashmap | Lock.Tash.Afro.B
    +0x4
    ++0x1c = [32-bit Pointer] Lock Container
    .. Every "Lock." hashmap entry follow this structure
    +++0x18 = [32-bit] Price
    +++0x1c = [32-bit Pointer] FETXT ID String
    +++0x20 = [32-bit] Worm Mustaches | Afro.B
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    +++0x24 = [32-bit] Shop Category
    ... 0x0 = None
    ... 0x1 = Sound Banks
    ... 0x2 = Maps
    ... 0x3 = Hats
    ... 0x4 = Spectacles
    ... 0x5 = Hands
    ... 0x6 = Mustaches
    ... 0x7 = Weapons
    ... 0x8 = Game Styles
    ... 0x9 = Character
    """

    HASHMAP_LOCKTASHAFROG = dword(0xde755c)
    """
    [32-bit Pointer] Hashmap | Lock.Tash.Afro.G
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Mustaches | Afro.G
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTASHAFROR = dword(0xde7590)
    """
    [32-bit Pointer] Hashmap | Lock.Tash.Afro.R
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Mustaches | Afro.R
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATPUNKY = dword(0xde75a4)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Punk.Y
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Punk.Y
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKFACENHS = dword(0xde76d0)
    """
    [32-bit Pointer] Hashmap | Lock.Face.NHS
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Spectacles | NHS
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSCHEMEROOTNSHOOT = dword(0xde7790)
    """
    [32-bit Pointer] Hashmap | Lock.Scheme.RootNShoot
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Game Styles | RootNShoot
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATSPACESUIT = dword(0xde77d0)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Spacesuit
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Spacesuit
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTSTORYTURKISHDELIGHTS = dword(0xde780c)
    """
    [32-bit Pointer] Hashmap | Lock.T.Story.TurkishDelights
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Story.TurkishDelights
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKTCHALLENGECRATECOLLECT = dword(0xde7810)
    """
    [32-bit Pointer] Hashmap | Lock.T.Challenge.CrateCollect
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Challenge.CrateCollect
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKTSTORYSABOTEURS = dword(0xde7854)
    """
    [32-bit Pointer] Hashmap | Lock.T.Story.Saboteurs
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Story.Saboteurs
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKSTORYSABOTEURS = dword(0xde78d4)
    """
    [32-bit Pointer] Hashmap | Lock.Story.Saboteurs
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Story Chapter | Saboteurs
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_JETPACKFUEL = dword(0xde78f0)
    """
    [32-bit Pointer] Hashmap | Jetpack.Fuel
    +0x4
    ++0x1c = [32-bit] Jetpack Fuel
    """

    HASHMAP_LOCKSOUNDGAMESHOW = dword(0xde795c)
    """
    [32-bit Pointer] Hashmap | Lock.Sound.Gameshow
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Sound Banks | Gameshow
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTSTORYNOROOMFORERROR = dword(0xde7988)
    """
    [32-bit Pointer] Hashmap | Lock.T.Story.NoRoomForError
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Story.NoRoomForError
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKTASHCOWBOYBK = dword(0xde7a2c)
    """
    [32-bit Pointer] Hashmap | Lock.Tash.Cowboy.Bk
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Mustaches | Cowboy.Bk
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKWEAPONICARUSPOTION = dword(0xde7a38)
    """
    [32-bit Pointer] Hashmap | Lock.Weapon.IcarusPotion
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Weapons | IcarusPotion
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATARABIAND = dword(0xde7ad0)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Arabian.D
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Arabian.D
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATPARTY = dword(0xde7ae4)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Party
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Party
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATARABIANR = dword(0xde7b08)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Arabian.R
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Arabian.R
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKMAPSABOTEURS = dword(0xde7b0c)
    """
    [32-bit Pointer] Hashmap | Lock.Map.Saboteurs
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Maps | Saboteurs
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATARABIANW = dword(0xde7b1c)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Arabian.W
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Arabian.W
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_AWARDS = dword(0xde7b8c)
    """
    [32-bit Pointer] Hashmap | Awards
    +0x4
    ++0x1c
    +++0x14
    ++++0x40 = [32-bit] [Boolean] Trophy | Gold Damage
    ++++0x44 = [32-bit] [Boolean] Trophy | 4 Bagger
    ++++0x48 = [32-bit] [Boolean] Trophy | Big Blast
    ++++0x4c = [32-bit] [Boolean] Trophy | Magic Bullet
    ++++0x50 = [32-bit] [Boolean] Trophy | The Beast Within
    ++++0x54 = [32-bit] [Boolean] Trophy | Silver Damage
    ++++0x58 = [32-bit] [Boolean] Trophy | 3 Bagger
    ++++0x5c = [32-bit] [Boolean] Trophy | Hot Foot
    ++++0x60 = [32-bit] [Boolean] Trophy | Animal Lover
    ++++0x64 = [32-bit] [Boolean] Trophy | Weapon Specialist
    ++++0x68 = [32-bit] [Boolean] Trophy | Bronze Damage
    ++++0x6c = [32-bit] [Boolean] Trophy | Body Count
    ++++0x70 = [32-bit] [Boolean] Trophy | Barrel Buster
    ++++0x74 = [32-bit] [Boolean] Trophy | Rocketeer
    ++++0x78 = [32-bit] [Boolean] Trophy | Greedy Worm
    """

    HASHMAP_LOCKSTORYDESTRUCTANDSERVE = dword(0xde7b98)
    """
    [32-bit Pointer] Hashmap | Lock.Story.DestructAndServe
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Story Chapter | DestructAndServe
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_WXDLEVELCURRENT = dword(0xde7bd0)
    """
    [32-bit Pointer] Hashmap | WXD.Level.Current
    +0x4
    ++0x1c
    +++0x0 = [ASCII] Current Map
    """

    HASHMAP_LOCKTCHALLENGEJETPACK = dword(0xde7bec)
    """
    [32-bit Pointer] Hashmap | Lock.T.Challenge.JetPack
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Challenge.JetPack
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKMAPHOLDUNTIL = dword(0xde7bf0)
    """
    [32-bit Pointer] Hashmap | Lock.Map.HoldUntil
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Maps | HoldUntil
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTASHCOWBOYB = dword(0xde7c08)
    """
    [32-bit Pointer] Hashmap | Lock.Tash.Cowboy.B
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Mustaches | Cowboy.B
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTASHCOWBOYG = dword(0xde7c1c)
    """
    [32-bit Pointer] Hashmap | Lock.Tash.Cowboy.G
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Mustaches | Cowboy.G
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHANDSPIRATE = dword(0xde7c54)
    """
    [32-bit Pointer] Hashmap | Lock.Hands.Pirate
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hands | Pirate
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKFACERAYBAN2 = dword(0xde7ccc)
    """
    [32-bit Pointer] Hashmap | Lock.Face.Rayban2
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Spectacles | Rayban2
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATWIZARDGR = dword(0xde7d08)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Wizard.Gr
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Wizard.Gr
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSOUNDWIZARD = dword(0xde7d14)
    """
    [32-bit Pointer] Hashmap | Lock.Sound.Wizard
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Sound Banks | Wizard
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSCHEMEDARKSIDER = dword(0xde7d88)
    """
    [32-bit Pointer] Hashmap | Lock.Scheme.Darksider
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Game Styles | Darksider
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTSTORYWINDYWIZARD = dword(0xde7dd0)
    """
    [32-bit Pointer] Hashmap | Lock.T.Story.WindyWizard
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Story.WindyWizard
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKMAPGHOSTHILL = dword(0xde7df0)
    """
    [32-bit Pointer] Hashmap | Lock.Map.GhostHill
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Maps | GhostHill
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_FCSGAMEOVER = dword(0xde8008)
    """
    [32-bit Pointer] Hashmap | FCS.GameOver
    +0x4
    ++0x1c = [32-bit] [Boolean] Is Game Over
    """

    HASHMAP_LOCKSOUNDSCOTT = dword(0xde8050)
    """
    [32-bit Pointer] Hashmap | Lock.Sound.Scott
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Sound Banks | Scott
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKWEAPONINFLATABLESCOUSER = dword(0xde80cc)
    """
    [32-bit Pointer] Hashmap | Lock.Weapon.InflatableScouser
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Weapons | InflatableScouser
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_ROUNDTIMEREMAINING = dword(0xde81ac)
    """
    [32-bit Pointer] Hashmap | RoundTimeRemaining
    +0x4
    ++0x1c = [32-bit] Round Time Remaining in milliseconds
    """

    HASHMAP_LOCKDEATHMATCH10 = dword(0xde8200)
    """
    [32-bit Pointer] Hashmap | Lock.Deathmatch.10
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Challenge | Deathmatch 10
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKFACEMATRIX = dword(0xde82a4)
    """
    [32-bit Pointer] Hashmap | Lock.Face.Matrix
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Spectacles | Matrix
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATBASEBALLGY = dword(0xde8364)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Baseball.Gy
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Baseball.Gy
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSTORYDOOMCANYON = dword(0xde8378)
    """
    [32-bit Pointer] Hashmap | Lock.Story.DoomCanyon
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Story Chapter | DoomCanyon
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_STORYSABOTEURS = dword(0xde840c)
    """
    [32-bit Pointer] Hashmap | Story.Saboteurs
    +0x4
    ++0x1c = [32-bit Pointer] Story Mission Definition | Building Site Saboteurs
    .. Refer to $0xde9818
    """

    HASHMAP_LOCKHATAMERICANFOOTBALLS = dword(0xde844c)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.AmericanFootball.S
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | AmericanFootball.S
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATAMERICANFOOTBALLY = dword(0xde8464)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.AmericanFootball.Y
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | AmericanFootball.Y
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_DAMAGEDWORMID = dword(0xde84d4)
    """
    [32-bit Pointer] Hashmap | DamagedWorm.Id
    +0x4
    ++0x1c = [32-bit] ID of the last damaged worm
    """

    HASHMAP_LOCKFACE3D = dword(0xde8510)
    """
    [32-bit Pointer] Hashmap | Lock.Face.3D
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Spectacles | 3D
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTCHALLENGEICARUS = dword(0xde854c)
    """
    [32-bit Pointer] Hashmap | Lock.T.Challenge.Icarus
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Challenge.Icarus
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKHATBASEBALLPE = dword(0xde8558)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Baseball.Pe
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Baseball.Pe
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATWIZARD = dword(0xde85d0)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Wizard
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Wizard
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKFACEXRAY = dword(0xde85e4)
    """
    [32-bit Pointer] Hashmap | Lock.Face.XRay
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Spectacles | XRay
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSOUNDBLUESMAN = dword(0xde8638)
    """
    [32-bit Pointer] Hashmap | Lock.Sound.BluesMan
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Sound Banks | BluesMan
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKMAPTURKISHDELIGHTS = dword(0xde864c)
    """
    [32-bit Pointer] Hashmap | Lock.Map.TurkishDelights
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Maps | TurkishDelights
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_CSTORYDINERMIGHT = dword(0xde8710)
    """
    [32-bit Pointer] Hashmap | C.Story.DinerMight
    +0x4
    ++0x1c = [32-bit] Mission Completed Counter | Diner Might
    """

    HASHMAP_LOCKSOUNDWISEWORM = dword(0xde8834)
    """
    [32-bit Pointer] Hashmap | Lock.Sound.Wiseworm
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Sound Banks | Wiseworm
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSCHEMESTANDARD = dword(0xde88d0)
    """
    [32-bit Pointer] Hashmap | Lock.Scheme.Standard
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Game Styles | Standard
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSCHEMEKITCHENSINK = dword(0xde88ec)
    """
    [32-bit Pointer] Hashmap | Lock.Scheme.KitchenSink
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Game Styles | KitchenSink
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKMAPLANDWORMSFORGOT = dword(0xde8990)
    """
    [32-bit Pointer] Hashmap | Lock.Map.LandWormsForgot
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Maps | LandWormsForgot
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATAFRO = dword(0xde89bc)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Afro
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Afro
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTDEATHMATCH1 = dword(0xde8a44)
    """
    [32-bit Pointer] Hashmap | Lock.T.Deathmatch.1
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Deathmatch.1
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKSETPROFESSOR = dword(0xde8a48)
    """
    [32-bit Pointer] Hashmap | Lock.Set.Professor
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Character Sets | Professor
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTDEATHMATCH2 = dword(0xde8a4c)
    """
    [32-bit Pointer] Hashmap | Lock.T.Deathmatch.2
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Deathmatch.2
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKTDEATHMATCH3 = dword(0xde8a50)
    """
    [32-bit Pointer] Hashmap | Lock.T.Deathmatch.3
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Deathmatch.3
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKTDEATHMATCH4 = dword(0xde8a58)
    """
    [32-bit Pointer] Hashmap | Lock.T.Deathmatch.4
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Deathmatch.4
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKTDEATHMATCH5 = dword(0xde8a5c)
    """
    [32-bit Pointer] Hashmap | Lock.T.Deathmatch.5
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Deathmatch.5
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKTDEATHMATCH6 = dword(0xde8a60)
    """
    [32-bit Pointer] Hashmap | Lock.T.Deathmatch.6
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Deathmatch.6
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKTDEATHMATCH7 = dword(0xde8a64)
    """
    [32-bit Pointer] Hashmap | Lock.T.Deathmatch.7
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Deathmatch.7
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKTDEATHMATCH8 = dword(0xde8a68)
    """
    [32-bit Pointer] Hashmap | Lock.T.Deathmatch.8
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Deathmatch.8
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKTDEATHMATCH9 = dword(0xde8a6c)
    """
    [32-bit Pointer] Hashmap | Lock.T.Deathmatch.9
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Deathmatch.9
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKMAPGIBBONTAKE = dword(0xde8a94)
    """
    [32-bit Pointer] Hashmap | Lock.Map.GibbonTake
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Maps | GibbonTake
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKMAPNOROOMFORERROR = dword(0xde8b48)
    """
    [32-bit Pointer] Hashmap | Lock.Map.NoRoomForError
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Maps | NoRoomForError
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTSTORYTINCANWALLY = dword(0xde8c24)
    """
    [32-bit Pointer] Hashmap | Lock.T.Story.TinCanWally
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Story.TinCanWally
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKHANDSKNIGHTGN = dword(0xde8cfc)
    """
    [32-bit Pointer] Hashmap | Lock.Hands.Knight.Gn
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hands | Knight.Gn
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSCHEMEALLACTION = dword(0xde8db8)
    """
    [32-bit Pointer] Hashmap | Lock.Scheme.AllAction
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Game Styles | AllAction
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTSTORYBRIDGETHIEVES = dword(0xde8dcc)
    """
    [32-bit Pointer] Hashmap | Lock.T.Story.BridgeThieves
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Story.BridgeThieves
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKTSTORYTRAITOROUSWATERS = dword(0xde8e0c)
    """
    [32-bit Pointer] Hashmap | Lock.T.Story.TraitorousWaters
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Story.TraitorousWaters
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKHATPIRATE = dword(0xde8f54)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Pirate
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Pirate
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSOUNDWHOOPSIE = dword(0xde8f94)
    """
    [32-bit Pointer] Hashmap | Lock.Sound.Whoopsie
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Sound Banks | Whoopsie
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKMAPJOUSTABOUTIT = dword(0xde8fd4)
    """
    [32-bit Pointer] Hashmap | Lock.Map.JoustAboutIt
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Maps | JoustAboutIt
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTCHALLENGENAVIGATION = dword(0xde9038)
    """
    [32-bit Pointer] Hashmap | Lock.T.Challenge.Navigation
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Challenge.Navigation
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKSOUNDCLASSIC = dword(0xde904c)
    """
    [32-bit Pointer] Hashmap | Lock.Sound.Classic
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Sound Banks | Classic
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATCOWBOY = dword(0xde9064)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Cowboy
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Cowboy
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHANDSPIRATEGN = dword(0xde90f8)
    """
    [32-bit Pointer] Hashmap | Lock.Hands.Pirate.Gn
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hands | Pirate.Gn
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKCHALLENGEICARUS = dword(0xde910c)
    """
    [32-bit Pointer] Hashmap | Lock.Challenge.Icarus
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Challenge | Icarus
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKMAPCHUTETOVICTORY = dword(0xde9164)
    """
    [32-bit Pointer] Hashmap | Lock.Map.ChuteToVictory
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Maps | ChuteToVictory
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSTORYTINCANWALLY = dword(0xde9168)
    """
    [32-bit Pointer] Hashmap | Lock.Story.TinCanWally
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Story Chapter | TinCanWally
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKHATCROWN = dword(0xde9178)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Crown
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Crown
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSTORYTURKISHDELIGHTS = dword(0xde918c)
    """
    [32-bit Pointer] Hashmap | Lock.Story.TurkishDelights
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Story Chapter | TurkishDelights
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKFACENHSBL = dword(0xde91b0)
    """
    [32-bit Pointer] Hashmap | Lock.Face.NHS.Bl
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Spectacles | NHS.Bl
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKMAPTINCANWALLY = dword(0xde91e4)
    """
    [32-bit Pointer] Hashmap | Lock.Map.TinCanWally
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Maps | TinCanWally
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATBASEBALL = dword(0xde91f0)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Baseball
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Baseball
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHANDSPIRATEBK = dword(0xde922c)
    """
    [32-bit Pointer] Hashmap | Lock.Hands.Pirate.Bk
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hands | Pirate.Bk
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATBLUESBROTHER = dword(0xde9288)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.BluesBrother
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | BluesBrother
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHANDSWHITE = dword(0xde92d8)
    """
    [32-bit Pointer] Hashmap | Lock.Hands.White
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hands | White
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKMAPWINDYWIZARD = dword(0xde93d0)
    """
    [32-bit Pointer] Hashmap | Lock.Map.WindyWizard
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Maps | WindyWizard
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSCHEMEHOLYGRAIL = dword(0xde93f4)
    """
    [32-bit Pointer] Hashmap | Lock.Scheme.HolyGrail
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Game Styles | HolyGrail
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSTORYGIBBONTAKE = dword(0xde9454)
    """
    [32-bit Pointer] Hashmap | Lock.Story.GibbonTake
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Story Chapter | GibbonTake
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKSOUNDARABIANTHIEF = dword(0xde9518)
    """
    [32-bit Pointer] Hashmap | Lock.Sound.ArabianThief
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Sound Banks | ArabianThief
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTCHALLENGESNIPERRIFLE = dword(0xde9558)
    """
    [32-bit Pointer] Hashmap | Lock.T.Challenge.SniperRifle
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Challenge.SniperRifle
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_DAMAGETYPETAKEN = dword(0xde95bc)
    """
    [32-bit Pointer] Hashmap | DamageTypeTaken
    +0x4
    ++0x1c = [32-bit] Last type of damage taken
    .. 0x0 = Regular
    .. 0x1 = Fall Damage
    .. 0x2 = Cluster
    .. 0x3 = ?
    .. 0x4 = Custom Weapon
    .. 0x5 = ?
    .. 0x6 = Poison
    """

    HASHMAP_LOCKMAPROBINTHEHOOD = dword(0xde9658)
    """
    [32-bit Pointer] Hashmap | Lock.Map.RobInTheHood
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Maps | RobInTheHood
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSTORYCRATEESCAPE = dword(0xde96d4)
    """
    [32-bit Pointer] Hashmap | Lock.Story.CrateEscape
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Story Chapter | CrateEscape
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKHATPIGTAILS = dword(0xde978c)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Pigtails
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Pigtails
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_STORYDINERMIGHT = dword(0xde9818)
    """
    [32-bit Pointer] Hashmap | Story.DinerMight
    +0x4
    ++0x1c = [32-bit Pointer] Story Mission Definition | DinerMight
    +++0x14 = [32-bit] Time Bonus target in seconds
    +++0x1c = [32-bit] ?
    +++0x20 = [32-bit Pointer] Unlock ID
    +++0x24 = [32-bit] ?
    +++0x28 = [32-bit] ? (Seems to affect whether the mission is displayed or not in the chapter select)
    +++0x2c = [32-bit Pointer] Obj ID?
    +++0x30 = [32-bit Pointer] Map ID
    +++0x34 = [32-bit Pointer] Script ID
    +++0x38 = [32-bit Pointer] Mission Image Filename
    +++0x3c = [32-bit Pointer] Mission Description Text ID
    +++0x40 = [32-bit Pointer] Mission Name Text ID
    """

    HASHMAP_LOCKWEAPONHOLYHANDGRENADE = dword(0xde9858)
    """
    [32-bit Pointer] Hashmap | Lock.Weapon.HolyHandGrenade
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Weapons | HolyHandGrenade
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKAWARD0 = dword(0xde9880)
    """
    [32-bit Pointer] Hashmap | Lock.Award.0
    +0x4
    ++0x1c
    +++0x20 = [32-bit] Trophy | Gold Damage
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    ... Value changes when unlocking the trophy but is not the actual flag used to
    ... display the trophy in the trophy cabinet, see $0xde7b8c
    """

    HASHMAP_LOCKAWARD1 = dword(0xde9884)
    """
    [32-bit Pointer] Hashmap | Lock.Award.1
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Trophy | 4 Bagger
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKAWARD2 = dword(0xde9888)
    """
    [32-bit Pointer] Hashmap | Lock.Award.2
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Trophy | Big Blast
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKAWARD3 = dword(0xde988c)
    """
    [32-bit Pointer] Hashmap | Lock.Award.3
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Trophy | Magic Bullet
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKAWARD4 = dword(0xde9890)
    """
    [32-bit Pointer] Hashmap | Lock.Award.4
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Trophy | The Beast Within
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKAWARD5 = dword(0xde9894)
    """
    [32-bit Pointer] Hashmap | Lock.Award.5
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Trophy | Silver Damage
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKAWARD6 = dword(0xde9898)
    """
    [32-bit Pointer] Hashmap | Lock.Award.6
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Trophy | 3 Bagger
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKAWARD7 = dword(0xde989c)
    """
    [32-bit Pointer] Hashmap | Lock.Award.7
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Trophy | Hot Foot
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKAWARD8 = dword(0xde98a0)
    """
    [32-bit Pointer] Hashmap | Lock.Award.8
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Trophy | Animal Lover
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKAWARD9 = dword(0xde98a4)
    """
    [32-bit Pointer] Hashmap | Lock.Award.9
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Trophy | Weapon Specialist
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKCHALLENGESHOTGUN = dword(0xde98fc)
    """
    [32-bit Pointer] Hashmap | Lock.Challenge.Shotgun
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Challenge | Shotgun
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKHANDSBONES = dword(0xde994c)
    """
    [32-bit Pointer] Hashmap | Lock.Hands.Bones
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hands | Bones
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATHELMETKING = dword(0xde995c)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.HelmetKing
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | HelmetKing
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKFACEMONOCLE = dword(0xde9998)
    """
    [32-bit Pointer] Hashmap | Lock.Face.Monocle
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Spectacles | Monocle
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSTORYCHUTETOVICTORY = dword(0xde99a4)
    """
    [32-bit Pointer] Hashmap | Lock.Story.ChuteToVictory
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Story Chapter | ChuteToVictory
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKMAPNICETOSIEGE = dword(0xde99d4)
    """
    [32-bit Pointer] Hashmap | Lock.Map.NiceToSiege
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Maps | NiceToSiege
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_AUDIOVOLMUSIC = dword(0xde9a0c)
    """
    [32-bit Pointer] Hashmap | Audio.Vol.Music
    +0x4
    ++0x1c = [32-bit] [Float] Music Volume
    .. 0.0 = Muted
    .. 1.0 = Max
    """

    HASHMAP_TURNTIMEREMAINING = dword(0xde9a1c)
    """
    [32-bit Pointer] Hashmap | TurnTimeRemaining
    +0x4
    ++0x1c = [32-bit] Turn Time Remaining (milliseconds)
    """

    HASHMAP_LOCKMAPHIGHNOON = dword(0xde9a38)
    """
    [32-bit Pointer] Hashmap | Lock.Map.HighNoon
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Maps | HighNoon
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTSTORYJOUSTABOUTIT = dword(0xde9ad0)
    """
    [32-bit Pointer] Hashmap | Lock.T.Story.JoustAboutIt
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Story.JoustAboutIt
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKHANDSCOWBOY = dword(0xde9b64)
    """
    [32-bit Pointer] Hashmap | Lock.Hands.Cowboy
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hands | Cowboy
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSTORYGHOSTHILL = dword(0xde9bb0)
    """
    [32-bit Pointer] Hashmap | Lock.Story.GhostHill
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Story Chapter | GhostHill
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    POINTER_TO_SHOP_COINS = dword(0xde9c94)
    """
    [32-bit] Pointer to Shop Coins
    +0x04
    ++0x1c | Coins [32-bit]
    """

    HASHMAP_LOCKSTORYESCAPE = dword(0xde9cd4)
    """
    [32-bit Pointer] Hashmap | Lock.Story.Escape
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Story Chapter | Escape
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKMAPTRAITOROUSWATERS = dword(0xde9d90)
    """
    [32-bit Pointer] Hashmap | Lock.Map.TraitorousWaters
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Maps | TraitorousWaters
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTSTORYDOOMCANYON = dword(0xde9db8)
    """
    [32-bit Pointer] Hashmap | Lock.T.Story.DoomCanyon
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Story.DoomCanyon
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKTSTORYALL = dword(0xde9e70)
    """
    [32-bit Pointer] Hashmap | Lock.T.Story.All
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Story.All
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKSOUNDCOWBOY = dword(0xde9ea4)
    """
    [32-bit Pointer] Hashmap | Lock.Sound.Cowboy
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Sound Banks | Cowboy
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKMAPDINERMIGHT = dword(0xde9f10)
    """
    [32-bit Pointer] Hashmap | Lock.Map.DinerMight
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Maps | DinerMight
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATREDBERET = dword(0xde9f50)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.RedBeret
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | RedBeret
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTSTORYLANDWORMSFORGOT = dword(0xde9f58)
    """
    [32-bit Pointer] Hashmap | Lock.T.Story.LandWormsForgot
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Story.LandWormsForgot
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKSOUNDCAVEWORM = dword(0xde9ff4)
    """
    [32-bit Pointer] Hashmap | Lock.Sound.CaveWorm
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Sound Banks | CaveWorm
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKFACEPIRATE = dword(0xdea014)
    """
    [32-bit Pointer] Hashmap | Lock.Face.Pirate
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Spectacles | Pirate
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTSTORYGHOSTHILL = dword(0xdea030)
    """
    [32-bit Pointer] Hashmap | Lock.T.Story.GhostHill
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Story.GhostHill
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKHATPIGTAILSBND = dword(0xdea098)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Pigtails.Bnd
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Pigtails.Bnd
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKFACENHSR = dword(0xdea188)
    """
    [32-bit Pointer] Hashmap | Lock.Face.NHS.R
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Spectacles | NHS.R
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSTORYWINDYWIZARD = dword(0xdea190)
    """
    [32-bit Pointer] Hashmap | Lock.Story.WindyWizard
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Story Chapter | WindyWizard
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKFACENHSW = dword(0xdea19c)
    """
    [32-bit Pointer] Hashmap | Lock.Face.NHS.W
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Spectacles | NHS.W
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATROCKETMAN = dword(0xdea3f8)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.RocketMan
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | RocketMan
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKMAPDOOMCANYON = dword(0xdea438)
    """
    [32-bit Pointer] Hashmap | Lock.Map.DoomCanyon
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Maps | DoomCanyon
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSTORYVALLEYOFDINOWORMS = dword(0xdea44c)
    """
    [32-bit Pointer] Hashmap | Lock.Story.ValleyOfDinoWorms
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Story Chapter | ValleyOfDinoWorms
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKHATFASHION = dword(0xdea478)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Fashion
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Fashion
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKMAPCRATEESCAPE = dword(0xdea4a8)
    """
    [32-bit Pointer] Hashmap | Lock.Map.CrateEscape
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Maps | CrateEscape
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKMAPDESTRUCTANDSERVE = dword(0xdea4e8)
    """
    [32-bit Pointer] Hashmap | Lock.Map.DestructAndServe
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Maps | DestructAndServe
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_DEADWORMID = dword(0xdea554)
    """
    [32-bit Pointer] Hashmap | DeadWorm.Id
    +0x4
    ++0x1c = [32-bit] ID of the last dead worm
    """

    HASHMAP_LOCKTSTORYHIGHNOON = dword(0xdea5f8)
    """
    [32-bit Pointer] Hashmap | Lock.T.Story.HighNoon
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Story.HighNoon
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKHATWIZARDD = dword(0xdea650)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Wizard.D
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Wizard.D
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_GAMELOGICCURRENTSCRIPT = dword(0xdea658)
    """
    [32-bit Pointer] Hashmap | GameLogic.CurrentScript
    +0x4
    ++0x1c
    +++0x0 = [ASCII] Current Script Name
    ... // Multiplayer
    ... "stdvs,wormpot" = Standard/Homelands Multiplayer Game
    ... "Survivor" = Survivor Multiplayer Game
    ... "MultiplayerDestruction" = Destruction Multiplayer Game
    ... "StatueDefend" = Statue Defend Multiplayer Game
    ... // Tutorial
    ... "Tutorial1" = Worminkle University
    ... "Tutorial2" = Unsporting Behaviour
    ... "Tutorial3" = Mike's Secret Laboratory
    ... // Construction
    ... "DinerMight" = Diner Might
    ... "SneakyBridgeThieves" = Sneaky Bridge Thieves Inc.
    ... "BuildingSiteSaboteurs" = Building Site Saboteurs
    ... "TheCrateEscape" = The Crate Escape
    ... "DestructAndServe" = Destruct And Serve
    ... // Camelot
    ... "StormTheCastle" = Storm The Castle
    ... "TheWindyWizard" = The Windy Wizard
    ... "RobInTheHood" = Rob In The Hood
    ... "JoustAboutIt" = Joust About It
    ... "NiceToSiegeYou" = Nice To Siege You
    """

    HASHMAP_LOCKHATWIZARDR = dword(0xdea688)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Wizard.R
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Wizard.R
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKMAPMINEALLMINE = dword(0xdea694)
    """
    [32-bit Pointer] Hashmap | Lock.Map.MineAllMine
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Maps | MineAllMine
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATUSMARINE = dword(0xdea6d8)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.USMarine
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | USMarine
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATBUNNY = dword(0xdea764)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Bunny
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Bunny
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKDEATHMATCH1 = dword(0xdea7c4)
    """
    [32-bit Pointer] Hashmap | Lock.Deathmatch.1
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Challenge | Deathmatch 1
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKDEATHMATCH2 = dword(0xdea7c8)
    """
    [32-bit Pointer] Hashmap | Lock.Deathmatch.2
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Challenge | Deathmatch 2
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKDEATHMATCH3 = dword(0xdea7cc)
    """
    [32-bit Pointer] Hashmap | Lock.Deathmatch.3
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Challenge | Deathmatch 3
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKDEATHMATCH4 = dword(0xdea7d4)
    """
    [32-bit Pointer] Hashmap | Lock.Deathmatch.4
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Challenge | Deathmatch 4
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKDEATHMATCH5 = dword(0xdea7d8)
    """
    [32-bit Pointer] Hashmap | Lock.Deathmatch.5
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Challenge | Deathmatch 5
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKDEATHMATCH6 = dword(0xdea7dc)
    """
    [32-bit Pointer] Hashmap | Lock.Deathmatch.6
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Challenge | Deathmatch 6
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKDEATHMATCH7 = dword(0xdea7e0)
    """
    [32-bit Pointer] Hashmap | Lock.Deathmatch.7
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Challenge | Deathmatch 7
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKDEATHMATCH8 = dword(0xdea7e4)
    """
    [32-bit Pointer] Hashmap | Lock.Deathmatch.8
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Challenge | Deathmatch 8
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKDEATHMATCH9 = dword(0xdea7e8)
    """
    [32-bit Pointer] Hashmap | Lock.Deathmatch.9
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Challenge | Deathmatch 9
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKTCHALLENGESHOTGUN = dword(0xdea978)
    """
    [32-bit Pointer] Hashmap | Lock.T.Challenge.Shotgun
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Challenge.Shotgun
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKHATWW1 = dword(0xdeaac4)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.WW1
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | WW1
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATWW2 = dword(0xdeaac8)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.WW2
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | WW2
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATCOWBOYBK = dword(0xdeabec)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Cowboy.Bk
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Cowboy.Bk
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSOUNDKNIGHT = dword(0xdeac50)
    """
    [32-bit Pointer] Hashmap | Lock.Sound.Knight
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Sound Banks | Knight
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSCHEMEMEGAPOWER = dword(0xdeacc8)
    """
    [32-bit Pointer] Hashmap | Lock.Scheme.MegaPower
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Game Styles | MegaPower
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATPIGTAILSR = dword(0xdead48)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Pigtails.R
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Pigtails.R
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTSTORYDESTRUCTANDSERVE = dword(0xdead54)
    """
    [32-bit Pointer] Hashmap | Lock.T.Story.DestructAndServe
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Story.DestructAndServe
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKHANDSWHITEY = dword(0xdead64)
    """
    [32-bit Pointer] Hashmap | Lock.Hands.White.Y
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hands | White.Y
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHANDSWHITED = dword(0xdead90)
    """
    [32-bit Pointer] Hashmap | Lock.Hands.White.D
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hands | White.D
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSCHEMEPRO = dword(0xdeadbc)
    """
    [32-bit Pointer] Hashmap | Lock.Scheme.Pro
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Game Styles | Pro
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKMAPBRIDGETHIEVES = dword(0xdeae0c)
    """
    [32-bit Pointer] Hashmap | Lock.Map.BridgeThieves
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Maps | BridgeThieves
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATPOLICE = dword(0xdeaf14)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Police
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Police
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTASHSCOTT = dword(0xdeb090)
    """
    [32-bit Pointer] Hashmap | Lock.Tash.Scott
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Mustaches | Scott
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKWEAPONSNIPERRIFLE = dword(0xdeb0d4)
    """
    [32-bit Pointer] Hashmap | Lock.Weapon.SniperRifle
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Weapons | SniperRifle
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHANDSSPACESUITP = dword(0xdeb1c0)
    """
    [32-bit Pointer] Hashmap | Lock.Hands.Spacesuit.P
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hands | Spacesuit.P
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHANDSSPACESUITB = dword(0xdeb208)
    """
    [32-bit Pointer] Hashmap | Lock.Hands.Spacesuit.B
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hands | Spacesuit.B
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSTORYSTORMTHECASTLE = dword(0xdeb214)
    """
    [32-bit Pointer] Hashmap | Lock.Story.StormTheCastle
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Story Chapter | StormTheCastle
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKHANDSSPACESUITG = dword(0xdeb21c)
    """
    [32-bit Pointer] Hashmap | Lock.Hands.Spacesuit.G
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hands | Spacesuit.G
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKFACEELVISR = dword(0xdeb28c)
    """
    [32-bit Pointer] Hashmap | Lock.Face.Elvis.R
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Spectacles | Elvis.R
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKFACEELVISS = dword(0xdeb290)
    """
    [32-bit Pointer] Hashmap | Lock.Face.Elvis.S
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Spectacles | Elvis.S
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKFACEELVIS = dword(0xdeb2cc)
    """
    [32-bit Pointer] Hashmap | Lock.Face.Elvis
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Spectacles | Elvis
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTASHVIKING = dword(0xdeb2dc)
    """
    [32-bit Pointer] Hashmap | Lock.Tash.Viking
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Mustaches | Viking
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTSTORYCRATEESCAPE = dword(0xdeb4a4)
    """
    [32-bit Pointer] Hashmap | Lock.T.Story.CrateEscape
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Story.CrateEscape
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKSOUNDASTRONAUT = dword(0xdeb594)
    """
    [32-bit Pointer] Hashmap | Lock.Sound.Astronaut
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Sound Banks | Astronaut
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSETHORROR = dword(0xdeb65c)
    """
    [32-bit Pointer] Hashmap | Lock.Set.Horror
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Character Sets | Horror
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHANDSPUNKGN = dword(0xdeb6f8)
    """
    [32-bit Pointer] Hashmap | Lock.Hands.Punk.Gn
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hands | Punk.Gn
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHANDSRINGED = dword(0xdeb790)
    """
    [32-bit Pointer] Hashmap | Lock.Hands.Ringed
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hands | Ringed
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTASHAFRO = dword(0xdeb7bc)
    """
    [32-bit Pointer] Hashmap | Lock.Tash.Afro
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Mustaches | Afro
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKMAPESCAPE = dword(0xdeb858)
    """
    [32-bit Pointer] Hashmap | Lock.Map.Escape
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Maps | Escape
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATSPACESUITBL = dword(0xdeb9f0)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Spacesuit.Bl
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Spacesuit.Bl
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_STORYBRIDGETHIEVES = dword(0xdeba0c)
    """
    [32-bit Pointer] Hashmap | Story.BridgeThieves
    +0x4
    ++0x1c = [32-bit Pointer] Story Mission Definition | Sneaky Bridge Thieves Inc.
    .. Refer to $0xde9818
    """

    HASHMAP_LOCKFACEELVISBK = dword(0xdeba6c)
    """
    [32-bit Pointer] Hashmap | Lock.Face.Elvis.Bk
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Spectacles | Elvis.Bk
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKMAPTRAININGGROUNDS = dword(0xdeba8c)
    """
    [32-bit Pointer] Hashmap | Lock.Map.TrainingGrounds
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Maps | TrainingGrounds
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATAMERICANFOOTBALLBL = dword(0xdebaf4)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.AmericanFootball.Bl
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | AmericanFootball.Bl
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTASHSMALLBR = dword(0xdebb48)
    """
    [32-bit Pointer] Hashmap | Lock.Tash.Small.Br
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Mustaches | Small.Br
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATSPACESUITGY = dword(0xdebb68)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Spacesuit.Gy
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Spacesuit.Gy
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATBASEBALLC = dword(0xdebbd0)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Baseball.C
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Baseball.C
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATBASEBALLP = dword(0xdebc0c)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Baseball.P
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Baseball.P
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATBASEBALLR = dword(0xdebc14)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Baseball.R
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Baseball.R
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTASHCURLYB = dword(0xdebc48)
    """
    [32-bit Pointer] Hashmap | Lock.Tash.Curly.B
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Mustaches | Curly.B
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTASHCURLYG = dword(0xdebc5c)
    """
    [32-bit Pointer] Hashmap | Lock.Tash.Curly.G
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Mustaches | Curly.G
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSTORYBRIDGETHIEVES = dword(0xdebc8c)
    """
    [32-bit Pointer] Hashmap | Lock.Story.BridgeThieves
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Story Chapter | BridgeThieves
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKTASHCURLYR = dword(0xdebc90)
    """
    [32-bit Pointer] Hashmap | Lock.Tash.Curly.R
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Mustaches | Curly.R
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTASHSMALLR = dword(0xdebd48)
    """
    [32-bit Pointer] Hashmap | Lock.Tash.Small.R
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Mustaches | Small.R
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTASHSMALLW = dword(0xdebd5c)
    """
    [32-bit Pointer] Hashmap | Lock.Tash.Small.W
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Mustaches | Small.W
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTASHCOWBOY = dword(0xdebd64)
    """
    [32-bit Pointer] Hashmap | Lock.Tash.Cowboy
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Mustaches | Cowboy
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_AUDIOVOLSPEECH = dword(0xdebda0)
    """
    [32-bit Pointer] Hashmap | Audio.Vol.Speech
    +0x4
    ++0x1c = [32-bit] [Float] Speech Volume
    .. 0.0 = Muted
    .. 1.0 = Max
    """

    HASHMAP_LOCKFACESTARP = dword(0xdebdc0)
    """
    [32-bit Pointer] Hashmap | Lock.Face.Star.P
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Spectacles | Star.P
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKFACESTARZ = dword(0xdebde8)
    """
    [32-bit Pointer] Hashmap | Lock.Face.Star.Z
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Spectacles | Star.Z
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKCHALLENGESSHEEP = dword(0xdebe00)
    """
    [32-bit Pointer] Hashmap | Lock.Challenge.SSheep
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Challenge | SSheep
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKFACESTARL = dword(0xdebe30)
    """
    [32-bit Pointer] Hashmap | Lock.Face.Star.L
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Spectacles | Star.L
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSCHEMESTRATEGY = dword(0xdebe64)
    """
    [32-bit Pointer] Hashmap | Lock.Scheme.Strategy
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Game Styles | Strategy
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKCHALLENGEJETPACK = dword(0xdebf6c)
    """
    [32-bit Pointer] Hashmap | Lock.Challenge.JetPack
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Challenge | JetPack
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_ACTIVEWORMINDEX = dword(0xdebfe0)
    """
    [32-bit Pointer] Hashmap | ActiveWormIndex
    +0x4
    ++0x1c = [32-bit] Active Worm Index
    .. 0x0-0xf = Worm Index
    .. 0xffffffff = None
    """

    HASHMAP_STORYCRATEESCAPE = dword(0xdec01c)
    """
    [32-bit Pointer] Hashmap | Story.CrateEscape
    +0x4
    ++0x1c = [32-bit Pointer] Story Mission Definition | The Crate Escape
    .. Refer to $0xde9818
    """

    HASHMAP_FECURRENTMENU = dword(0xdec098)
    """
    [32-bit Pointer] Hashmap | FE.CurrentMenu
    +0x4
    ++0x1c = [32-bit Pointer] Current Menu
    +++0x0 = [ASCII] Menu ID String
    ... "" = Not in a menu
    ... "WXFE.MainMenu" = Main Menu
    ... "WXFE.Tutorial" = Tutorial Menu
    ... "WXFE.Story" = Story Menu
    ... "WXFE.CreateAGame" = Standard/Homelands Multiplayer Menu
    ... "WXFE.CreateAGameDest" = Destruction Multiplayer Menu
    ... "WXFE.CreateAGameSD" = Statue Defend/Survivor Multiplayer Menu
    ... "WXFE.Wormpot" = Wormpot Menu
    ... "WXFE.Customise" = Customise Menu
    ... "WXFE.TeamOptions" = Team Create/Edit Menu
    ... "WXFE.WeaponFactory1" = Weapon Factory Menu
    ... "WXFE.SchemeBuilderBase" = Game Style Create/Edit Menu
    ... "WXFE.Challenges" = Challenges Menu
    ... "WXFE.TrophyCabinet" = Trophy Cabinet Menu
    ... "WXFE.ItemShop" = Item Shop Menu
    ... "WXFE.Options" = Options Menu
    ... "WXFE.ControlOptions" = Control Options Menu
    ... "WXFE.SoundAndVideo" = Sound And Video Menu
    ... "WXFE.CenterScreen" = Center Screen Menu
    ... "WXFE.ChangingLanguage" = Changing Language Menu
    ... "WXFE.Credits" = Credits Menu
    ... "WXFE.PreStart" = Starting Game Menu (Transition before loading screen)
    ... "WXFE.WinTutorial" = Tutorial Complete Menu
    ... "WXFE.WinMission" = Mission Complete Menu
    ... "WXFE.WinChallenge" = Challenge Complete Menu
    ... "WXFE.WinRound" = Multiplayer Round Results Menu
    ... "WXFE.PreRound" = Multiplayer Next Round Ready Menu
    ... "WXFE.WinMatch" = Multiplayer Match Results Menu
    ... "WXFE.WinAward" = Trophy Awarded Menu
    ... "WXFE.EasterEggFound" = Easter Egg Found Menu
    """

    HASHMAP_LOCKMAPRESUBMISSION = dword(0xdec0f8)
    """
    [32-bit Pointer] Hashmap | Lock.Map.ReSubmission
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Maps | ReSubmission
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSOUNDBUILDER = dword(0xdec108)
    """
    [32-bit Pointer] Hashmap | Lock.Sound.Builder
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Sound Banks | Builder
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKMAPTOPSECRET = dword(0xdec114)
    """
    [32-bit Pointer] Hashmap | Lock.Map.TopSecret
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Maps | TopSecret
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKFACESTAR = dword(0xdec1c8)
    """
    [32-bit Pointer] Hashmap | Lock.Face.Star
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Spectacles | Star
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATVIKING = dword(0xdec3dc)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Viking
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Viking
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_WXDCURRENTTUTORIAL = dword(0xdec434)
    """
    [32-bit Pointer] Hashmap | WXD.CurrentTutorial
    +0x4
    ++0x1c = [32-bit] Current Tutorial or Challenge selected
    .. // Tutorials
    .. 0x0 = Worminkle University
    .. 0x1 = Unsporting Behaviour
    .. 0x2 = Mike's Secret Laboratory
    .. // Challenges
    .. 0x0 = Sniper Rifle Challenge
    .. 0x1 = Jet Pack Challenge
    .. 0x2 = Super Sheep Challenge
    .. 0x3 = Icarus Potion Challenge
    .. 0x4 = Shotgun Challenge
    .. 0x5 = Accuracy Challenge
    .. 0x6 = Navigation Challenge
    .. 0x7 = Crate Collect Challenge
    .. 0x8 = Deathmatch 1
    .. 0x9 = Deathmatch 2
    .. 0xa = Deathmatch 3
    .. 0xb = Deathmatch 4
    .. 0xc = Deathmatch 5
    .. 0xd = Deathmatch 6
    .. 0xe = Deathmatch 7
    .. 0xf = Deathmatch 8
    .. 0x10 = Deathmatch 9
    .. 0x11 = Deathmatch 10
    """

    HASHMAP_LOCKTSTORYESCAPE = dword(0xdec454)
    """
    [32-bit Pointer] Hashmap | Lock.T.Story.Escape
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Story.Escape
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKSCHEMEBNG = dword(0xdec59c)
    """
    [32-bit Pointer] Hashmap | Lock.Scheme.Bng
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Game Styles | Bng
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHANDSPIRATEW = dword(0xdec61c)
    """
    [32-bit Pointer] Hashmap | Lock.Hands.Pirate.W
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hands | Pirate.W
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTCHALLENGESSHEEP = dword(0xdec640)
    """
    [32-bit Pointer] Hashmap | Lock.T.Challenge.SSheep
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Challenge.SSheep
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKFACERAYBAN = dword(0xdec7f8)
    """
    [32-bit Pointer] Hashmap | Lock.Face.Rayban
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Spectacles | Rayban
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKFACEXRAYP = dword(0xdec8c0)
    """
    [32-bit Pointer] Hashmap | Lock.Face.XRay.P
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Spectacles | XRay.P
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKFACEXRAYS = dword(0xdec8cc)
    """
    [32-bit Pointer] Hashmap | Lock.Face.XRay.S
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Spectacles | XRay.S
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKFACEXRAYY = dword(0xdec8e4)
    """
    [32-bit Pointer] Hashmap | Lock.Face.XRay.Y
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Spectacles | XRay.Y
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKCHALLENGENAVIGATION = dword(0xdec938)
    """
    [32-bit Pointer] Hashmap | Lock.Challenge.Navigation
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Challenge | Navigation
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKTSTORYMINEALLMINE = dword(0xdec958)
    """
    [32-bit Pointer] Hashmap | Lock.T.Story.MineAllMine
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Story.MineAllMine
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKSOUNDMEME = dword(0xdec9d8)
    """
    [32-bit Pointer] Hashmap | Lock.Sound.Meme
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Sound Banks | Meme
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSCHEMEMYSTERY = dword(0xdeca64)
    """
    [32-bit Pointer] Hashmap | Lock.Scheme.Mystery
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Game Styles | Mystery
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATSPACESUITP = dword(0xdecb00)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Spacesuit.P
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Spacesuit.P
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHANDSSPACESUIT = dword(0xdecb90)
    """
    [32-bit Pointer] Hashmap | Lock.Hands.Spacesuit
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hands | Spacesuit
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHANDSWHITEBR = dword(0xdecc88)
    """
    [32-bit Pointer] Hashmap | Lock.Hands.White.Br
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hands | White.Br
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKMAPCARPETCAPERS = dword(0xdecd0c)
    """
    [32-bit Pointer] Hashmap | Lock.Map.CarpetCapers
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Maps | CarpetCapers
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATQUEENOFSHEBA = dword(0xded084)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.QueenOfSheba
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | QueenOfSheba
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHANDSCOWBOYBK = dword(0xded0ac)
    """
    [32-bit Pointer] Hashmap | Lock.Hands.Cowboy.Bk
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hands | Cowboy.Bk
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSOUNDGANGSTER = dword(0xded0c8)
    """
    [32-bit Pointer] Hashmap | Lock.Sound.Gangster
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Sound Banks | Gangster
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSOUNDDISCO = dword(0xded0fc)
    """
    [32-bit Pointer] Hashmap | Lock.Sound.Disco
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Sound Banks | Disco
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATBUILDER = dword(0xded188)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Builder
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Builder
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSTORYTRAITOROUSWATERS = dword(0xded1cc)
    """
    [32-bit Pointer] Hashmap | Lock.Story.TraitorousWaters
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Story Chapter | TraitorousWaters
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKHANDSFUMANCHU = dword(0xded218)
    """
    [32-bit Pointer] Hashmap | Lock.Hands.FuManChu
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hands | FuManChu
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSTORYMINEALLMINE = dword(0xded21c)
    """
    [32-bit Pointer] Hashmap | Lock.Story.MineAllMine
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Story Chapter | MineAllMine
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKTSTORYGIBBONTAKE = dword(0xded220)
    """
    [32-bit Pointer] Hashmap | Lock.T.Story.GibbonTake
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Story.GibbonTake
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKHATPUNKBL = dword(0xded270)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Punk.Bl
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Punk.Bl
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATPUNKGR = dword(0xded2cc)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Punk.Gr
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Punk.Gr
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LEVELDETAILSNAME = dword(0xded2e0)
    """
    [32-bit Pointer] Hashmap | LevelDetailsName
    +0x4
    ++0x1c
    +++0x0 = [ASCII] Selected Level Name
    ... // Tutorial
    ... "Tutorial.1" = Worminkle University
    ... "Tutorial.2" = Unsporting Behaviour
    ... "Tutorial.3" = Mike's Secret Laboratory
    ... // Construction
    ... "Story.DinerMight" = Diner Might
    ... "Story.BridgeThieves" = Sneaky Bridge Thieves Inc.
    ... "Story.Saboteurs" = Building Site Saboteurs
    ... "Story.CrateEscape" = The Crate Escape
    ... "Story.DestructAndServe" = Destruct And Serve
    ... // Camelot
    ... "Story.StormTheCastle" = Storm The Castle
    ... "Story.WindyWizard" = The Windy Wizard
    ... "Story.RobInTheHood" = Rob In The Hood
    ... "Story.JoustAboutIt" = Joust About It
    ... "Story.NiceToSiege" = Nice To Siege You
    """

    HASHMAP_LOCKCHALLENGECRATECOLLECT = dword(0xded450)
    """
    [32-bit Pointer] Hashmap | Lock.Challenge.CrateCollect
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Challenge | CrateCollect
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKSTORYDINERMIGHT = dword(0xded4d0)
    """
    [32-bit Pointer] Hashmap | Lock.Story.DinerMight
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Story Chapter | DinerMight
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKSCHEMESHOPPING = dword(0xded59c)
    """
    [32-bit Pointer] Hashmap | Lock.Scheme.Shopping
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Game Styles | Shopping
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKMAPSTORMTHECASTLE = dword(0xded5d4)
    """
    [32-bit Pointer] Hashmap | Lock.Map.StormTheCastle
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Maps | StormTheCastle
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATBISHOP = dword(0xded640)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Bishop
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Bishop
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATCOWBOY2 = dword(0xded688)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Cowboy2
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Cowboy2
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATSCOTTISH = dword(0xded760)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Scottish
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Scottish
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHANDSKNIGHT = dword(0xded790)
    """
    [32-bit Pointer] Hashmap | Lock.Hands.Knight
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hands | Knight
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATPREHISTORIC = dword(0xded80c)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Prehistoric
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Prehistoric
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATAMERICANFOOTBALL = dword(0xded870)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.AmericanFootball
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | AmericanFootball
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKCHALLENGESNIPERRIFLE = dword(0xded8d8)
    """
    [32-bit Pointer] Hashmap | Lock.Challenge.SniperRifle
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Challenge | SniperRifle
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKTASHVIKINGBK = dword(0xded92c)
    """
    [32-bit Pointer] Hashmap | Lock.Tash.Viking.Bk
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Mustaches | Viking.Bk
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSOUNDSCOUSER = dword(0xded9c8)
    """
    [32-bit Pointer] Hashmap | Lock.Sound.Scouser
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Sound Banks | Scouser
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_CURRENTTEAMINDEX = dword(0xdedaa0)
    """
    [32-bit Pointer] Hashmap | CurrentTeamIndex
    +0x4
    ++0x1c = [32-bit] Current Team Index
    """

    HASHMAP_WXDCOINSAWARDED = dword(0xdedb90)
    """
    [32-bit Pointer] Hashmap | WXD.CoinsAwarded
    +0x4
    ++0x1c = [32-bit] Coins awarded at the end of a match
    """

    HASHMAP_LOCKTASHVIKINGR = dword(0xdedbc8)
    """
    [32-bit Pointer] Hashmap | Lock.Tash.Viking.R
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Mustaches | Viking.R
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSOUNDBOBBY = dword(0xdedbe8)
    """
    [32-bit Pointer] Hashmap | Lock.Sound.Bobby
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Sound Banks | Bobby
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTASHVIKINGG = dword(0xdedc1c)
    """
    [32-bit Pointer] Hashmap | Lock.Tash.Viking.G
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Mustaches | Viking.G
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATCHINESE = dword(0xdedc54)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Chinese
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Chinese
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_AUDIOVOLSFX = dword(0xdedc60)
    """
    [32-bit Pointer] Hashmap | Audio.Vol.Sfx
    +0x4
    ++0x1c = [32-bit] [Float] Effects Volume
    .. 0.0 = Muted
    .. 1.0 = Max
    """

    HASHMAP_LOCKSTORYJOUSTABOUTIT = dword(0xdedd50)
    """
    [32-bit Pointer] Hashmap | Lock.Story.JoustAboutIt
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Story Chapter | JoustAboutIt
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKSTORYCARPETCAPERS = dword(0xdedd90)
    """
    [32-bit Pointer] Hashmap | Lock.Story.CarpetCapers
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Story Chapter | CarpetCapers
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKHATPUNK = dword(0xdeddac)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Punk
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Punk
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHANDSKNIGHTW = dword(0xdededc)
    """
    [32-bit Pointer] Hashmap | Lock.Hands.Knight.W
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hands | Knight.W
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATARABIAN = dword(0xdedef8)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Arabian
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Arabian
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHANDSKNIGHTG = dword(0xdedf1c)
    """
    [32-bit Pointer] Hashmap | Lock.Hands.Knight.G
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hands | Knight.G
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKCHALLENGEACCURACY = dword(0xdedf24)
    """
    [32-bit Pointer] Hashmap | Lock.Challenge.Accuracy
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Challenge | Accuracy
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKHATPIGTAILSBL = dword(0xdedf30)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Pigtails.Bl
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Pigtails.Bl
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKMAPFASTFOODDINO = dword(0xdedf3c)
    """
    [32-bit Pointer] Hashmap | Lock.Map.FastFoodDino
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Maps | FastFoodDino
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKEASTEREGG0 = dword(0xdedf40)
    """
    [32-bit Pointer] Hashmap | Lock.EasterEgg.0
    +0x4
    ++0x1c
    +++0x20 = [32-bit] Easter Egg | 88 MPH
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKEASTEREGG1 = dword(0xdedf44)
    """
    [32-bit Pointer] Hashmap | Lock.EasterEgg.1
    +0x4
    ++0x1c
    +++0x20 = [32-bit] Easter Egg | Hidden Room
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKEASTEREGG2 = dword(0xdedf48)
    """
    [32-bit Pointer] Hashmap | Lock.EasterEgg.2
    +0x4
    ++0x1c
    +++0x20 = [32-bit] Easter Egg | Shoot the Crapper
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKEASTEREGG3 = dword(0xdedf4c)
    """
    [32-bit Pointer] Hashmap | Lock.EasterEgg.3
    +0x4
    ++0x1c
    +++0x20 = [32-bit] Easter Egg | Hidden Crate
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKEASTEREGG4 = dword(0xdedf54)
    """
    [32-bit Pointer] Hashmap | Lock.EasterEgg.4
    +0x4
    ++0x1c
    +++0x20 = [32-bit] Easter Egg | Feed the T. Rex
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKWEAPONBUBBLETROUBLE = dword(0xdee158)
    """
    [32-bit Pointer] Hashmap | Lock.Weapon.BubbleTrouble
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Weapons | BubbleTrouble
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTASHSAFETYPIN = dword(0xdee2c4)
    """
    [32-bit Pointer] Hashmap | Lock.Tash.SafetyPin
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Mustaches | SafetyPin
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATCOWBOYR = dword(0xdee388)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Cowboy.R
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Cowboy.R
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTSTORYVALLEYOFDINOWORMS = dword(0xdee390)
    """
    [32-bit Pointer] Hashmap | Lock.T.Story.ValleyOfDinoWorms
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Story.ValleyOfDinoWorms
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKHATCOWBOYW = dword(0xdee3a0)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Cowboy.W
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Cowboy.W
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTSTORYROBINTHEHOOD = dword(0xdee450)
    """
    [32-bit Pointer] Hashmap | Lock.T.Story.RobInTheHood
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Story.RobInTheHood
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKTASHCURLY = dword(0xdee4a8)
    """
    [32-bit Pointer] Hashmap | Lock.Tash.Curly
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Mustaches | Curly
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTDEATHMATCH10 = dword(0xdee544)
    """
    [32-bit Pointer] Hashmap | Lock.T.Deathmatch.10
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Deathmatch.10
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKSTORYLANDWORMSFORGOT = dword(0xdee5d0)
    """
    [32-bit Pointer] Hashmap | Lock.Story.LandWormsForgot
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Story Chapter | LandWormsForgot
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKSTORYROBINTHEHOOD = dword(0xdee5d4)
    """
    [32-bit Pointer] Hashmap | Lock.Story.RobInTheHood
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Story Chapter | RobInTheHood
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_DATATEAMBARRACKS = dword(0xdee64c)
    """
    [32-bit Pointer] Hashmap | DATA.TeamBarracks
    +0x4
    ++0x1c = [32-bit Pointer] TeamDataColective
    +++0x14 = [32-bit Pointer] XomContainerArray | High Scores
    ++++0x18 = [32-bit] Array Size (Always 20)
    ++++0x40 = [32-bit Pointer] Best Score [0] | Sniper Rifle Challenge
    +++++0x14 = [32-bit] Best Time in Seconds
    +++++0x18 = [32-bit Pointer] Player Name
    ++++0x44 = [32-bit Pointer] Best Score [1] | Jet Pack Challenge
    ++++0x48 = [32-bit Pointer] Best Score [2] | Super Sheep Challenge
    ++++0x4c = [32-bit Pointer] Best Score [3] | Icarus Potion Challenge
    ++++0x50 = [32-bit Pointer] Best Score [4] | Shotgun Challenge
    ++++0x54 = [32-bit Pointer] Best Score [5] | Accuracy Challenge
    ++++0x58 = [32-bit Pointer] Best Score [6] | Navigation Challenge
    ++++0x5c = [32-bit Pointer] Best Score [7] | Crate Collect Challenge
    ++++0x60 = [32-bit Pointer] Best Score [8] | Deathmatch 1
    ++++0x64 = [32-bit Pointer] Best Score [9] | Deathmatch 2
    ++++0x68 = [32-bit Pointer] Best Score [10] | Deathmatch 3
    ++++0x6c = [32-bit Pointer] Best Score [11] | Deathmatch 4
    ++++0x70 = [32-bit Pointer] Best Score [12] | Deathmatch 5
    ++++0x74 = [32-bit Pointer] Best Score [13] | Deathmatch 6
    ++++0x78 = [32-bit Pointer] Best Score [14] | Deathmatch 7
    ++++0x7c = [32-bit Pointer] Best Score [15] | Deathmatch 8
    ++++0x80 = [32-bit Pointer] Best Score [16] | Deathmatch 9
    ++++0x84 = [32-bit Pointer] Best Score [17] | Deathmatch 10
    ++++0x88 = [32-bit Pointer] Best Score [18] | Unused 1?
    ++++0x8c = [32-bit Pointer] Best Score [19] | Unused 2?
    """

    HASHMAP_LOCKSTORYNOROOMFORERROR = dword(0xdee688)
    """
    [32-bit Pointer] Hashmap | Lock.Story.NoRoomForError
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Story Chapter | NoRoomForError
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKSETDINOWORM = dword(0xdee6f4)
    """
    [32-bit Pointer] Hashmap | Lock.Set.Dinoworm
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Character Sets | Dinoworm
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTASHCHINESE = dword(0xdee714)
    """
    [32-bit Pointer] Hashmap | Lock.Tash.Chinese
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Mustaches | Chinese
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATSKULL = dword(0xdee730)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Skull
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Skull
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTSTORYDINERMIGHT = dword(0xdee790)
    """
    [32-bit Pointer] Hashmap | Lock.T.Story.DinerMight
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Story.DinerMight
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKTCHALLENGEACCURACY = dword(0xdee7a8)
    """
    [32-bit Pointer] Hashmap | Lock.T.Challenge.Accuracy
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Challenge.Accuracy
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKFACEPIRATER = dword(0xdee848)
    """
    [32-bit Pointer] Hashmap | Lock.Face.Pirate.R
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Spectacles | Pirate.R
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKFACEPIRATEW = dword(0xdee85c)
    """
    [32-bit Pointer] Hashmap | Lock.Face.Pirate.W
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Spectacles | Pirate.W
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSOUNDSECRETAGENT = dword(0xdee8d0)
    """
    [32-bit Pointer] Hashmap | Lock.Sound.SecretAgent
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Sound Banks | SecretAgent
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKFACEPIRATEBE = dword(0xdee918)
    """
    [32-bit Pointer] Hashmap | Lock.Face.Pirate.Be
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Spectacles | Pirate.Be
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_ELAPSEDROUNDTIME = dword(0xdee920)
    """
    [32-bit Pointer] Hashmap | ElapsedRoundTime
    +0x4
    ++0x1c = [32-bit] Elapsed Round Time in milliseconds
    """

    HASHMAP_LOCKTASHSMALLBLN = dword(0xdee978)
    """
    [32-bit Pointer] Hashmap | Lock.Tash.Small.Bln
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Mustaches | Small.Bln
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSTORYFASTFOODDINO = dword(0xdee9bc)
    """
    [32-bit Pointer] Hashmap | Lock.Story.FastFoodDino
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Story Chapter | FastFoodDino
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKHANDSCOWBOYR = dword(0xdee9c8)
    """
    [32-bit Pointer] Hashmap | Lock.Hands.Cowboy.R
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hands | Cowboy.R
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHANDSCOWBOYW = dword(0xdee9dc)
    """
    [32-bit Pointer] Hashmap | Lock.Hands.Cowboy.W
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hands | Cowboy.W
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSETALIEN = dword(0xdee9f8)
    """
    [32-bit Pointer] Hashmap | Lock.Set.Alien
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Character Sets | Alien
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTSTORYFASTFOODDINO = dword(0xdeeb3c)
    """
    [32-bit Pointer] Hashmap | Lock.T.Story.FastFoodDino
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Story.FastFoodDino
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKTSTORYNICETOSIEGE = dword(0xdeebd4)
    """
    [32-bit Pointer] Hashmap | Lock.T.Story.NiceToSiege
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Story.NiceToSiege
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKSCHEMEBEGINNER = dword(0xdeec48)
    """
    [32-bit Pointer] Hashmap | Lock.Scheme.Beginner
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Game Styles | Beginner
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSTORYNICETOSIEGE = dword(0xdeec98)
    """
    [32-bit Pointer] Hashmap | Lock.Story.NiceToSiege
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Story Chapter | NiceToSiege
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKHATHOCKEY = dword(0xdeece4)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Hockey
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Hockey
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKFACENVISION = dword(0xdeed00)
    """
    [32-bit Pointer] Hashmap | Lock.Face.NVision
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Spectacles | NVision
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTSTORYSTORMTHECASTLE = dword(0xdeed14)
    """
    [32-bit Pointer] Hashmap | Lock.T.Story.StormTheCastle
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Story.StormTheCastle
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKSTORYHIGHNOON = dword(0xdeedf8)
    """
    [32-bit Pointer] Hashmap | Lock.Story.HighNoon
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Story Chapter | HighNoon
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKMAPUNIVERSITYCHALLENGED = dword(0xdeee90)
    """
    [32-bit Pointer] Hashmap | Lock.Map.UniversityChallenged
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Maps | UniversityChallenged
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATBASEBALLT17 = dword(0xdeeedc)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Baseball.T17
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Baseball.T17
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKSETCYBERWORM = dword(0xdeeef4)
    """
    [32-bit Pointer] Hashmap | Lock.Set.Cyberworm
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Character Sets | Cyberworm
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKAWARD10 = dword(0xdeef00)
    """
    [32-bit Pointer] Hashmap | Lock.Award.10
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Trophy | Bronze Damage
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKAWARD11 = dword(0xdeef04)
    """
    [32-bit Pointer] Hashmap | Lock.Award.11
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Trophy | Body Count
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKAWARD12 = dword(0xdeef08)
    """
    [32-bit Pointer] Hashmap | Lock.Award.12
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Trophy | Barrel Buster
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKAWARD13 = dword(0xdeef0c)
    """
    [32-bit Pointer] Hashmap | Lock.Award.13
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Trophy | Rocketeer
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKAWARD14 = dword(0xdeef10)
    """
    [32-bit Pointer] Hashmap | Lock.Award.14
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Trophy | Greedy Worm
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKTSTORYCHUTETOVICTORY = dword(0xdeefa4)
    """
    [32-bit Pointer] Hashmap | Lock.T.Story.ChuteToVictory
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Story.ChuteToVictory
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKHATHELMET = dword(0xdeefd0)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.Helmet
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | Helmet
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATFLATCAP = dword(0xdef080)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.FlatCap
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | FlatCap
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHATSOVIETARMY = dword(0xdef0a4)
    """
    [32-bit Pointer] Hashmap | Lock.Hat.SovietArmy
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hats | SovietArmy
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKTSTORYCARPETCAPERS = dword(0xdef10c)
    """
    [32-bit Pointer] Hashmap | Lock.T.Story.CarpetCapers
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Time Bonus | Story.CarpetCapers
    ... 0x0 = Locked
    ... 0x2 = Unlocked
    """

    HASHMAP_LOCKHANDSPUNK = dword(0xdef12c)
    """
    [32-bit Pointer] Hashmap | Lock.Hands.Punk
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hands | Punk
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHANDSPUNKG = dword(0xdef15c)
    """
    [32-bit Pointer] Hashmap | Lock.Hands.Punk.G
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hands | Punk.G
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKHANDSPUNKR = dword(0xdef188)
    """
    [32-bit Pointer] Hashmap | Lock.Hands.Punk.R
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Worm Hands | Punk.R
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    HASHMAP_LOCKMAPVALLEYOFDINOWORMS = dword(0xdef190)
    """
    [32-bit Pointer] Hashmap | Lock.Map.ValleyOfDinoWorms
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x20 = [32-bit Boolean] Maps | ValleyOfDinoWorms
    ... 0x0 = Locked
    ... 0x1 = Available
    ... 0x2 = Bought
    """

    CURRENT_STORY_CHAPTER_POINTER = dword(0xdf74b8)
    """
    [32-bit] Current Story Chapter Pointer
    +0xc4 | Current Chapter [32-bit]
    """

    BASE_LUA_POINTER = dword(0xdf7884)
    """
    [32-bit Pointer] Base Lua Pointer
    0x0 = Lua script unloaded
    Read https://github.com/wormi-ra/RA-Scripts/blob/main/docs/Lua.md for more details
    Lua version 5.0.1

    +0x38 = [32-bit Pointer] Lua State
    ++0x10 = [32-bit Pointer] Global State
    +++0x0 = [32-bit Pointer] String Hash Table
    +++0x8 = [32-bit] String Table Size
    ++0x44 = [32-bit Pointer] Global Table
    +++0x7 = [8-bit] LSize
    ... 0x0 = 1
    ... 0x1 = 2
    ... 0x2 = 4
    ... 0x3 = 8
    ... 0x4 = 16
    ... 0x5 = 32
    ... 0x6 = 64
    ... 0x7 = 128
    ... 0x8 = 256
    ... 0x9 = 512
    ... 0xa = 1024
    ... 0xb = 2048
    ... 0xc = 4096
    ... 0xd = 8192 (Theoretical max)
    +++0x10 = [32-bit Pointer] Global Node Vector
    ... Dynamic Array of 20 bytes Node Structure
    ... The offset of a given node is calculated using the following formula:
    ... (StringHash % (1 << LSize)) * 20
    ... StringHash being the precomputed Lua string hash of said variable and
    ... LSize being the Log2 size of the vector
    ...
    ... [20 bytes] Node Structure
    ... |+0x0 = [32-bit] Key Type
    ... |. Always 0x4 (String)
    ... |+0x4 = [32-bit Pointer] Key
    ... |++0x8 = [32-bit] String Hash
    ... |++0xc = [32-bit] String Length
    ... |++0x10 = [ASCII] Key String
    ... |+0x8 = [32-bit] Value Type
    ... |. 0x0 = Null (Always 0x0)
    ... |. 0x1 = Boolean (0x0 or 0x1)
    ... |. 0x2 = LightUserData (Pointer)
    ... |. 0x3 = Number (Float)
    ... |. 0x4 = String (Pointer)
    ... |. 0x5 = Table (Pointer)
    ... |. 0x6 = Function (Pointer)
    ... |. 0x7 = UserData (Pointer)
    ... |. 0x8 = Thread (Pointer)
    ... |+0xc = [32-bit] Value or Pointer
    ... |+0x10 = [32-bit Pointer] Next Node
    """

    ATTRACT_MODE = dword(0x11e9ac4)
    """
    [32-bit Pointer] Attract Mode
    Pointer to the "Press START button" text
    0x0 = Disabled

    +0xb = [8-bit] [Bitfield] Text State
    . Bit7 = Text Displayed
    """

