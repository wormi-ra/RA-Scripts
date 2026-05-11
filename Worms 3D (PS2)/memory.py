from pycheevos.core.helpers import *
from dataclasses import dataclass

@dataclass(frozen=True)
class Memory:
    EU_STATE_CHECK_IS_LOADING = dword(0x53359c)
    """
    [32-bit Boolean] (EU) State Check | Is Loading
    """

    EU_STATE_CHECK_IS_GAME_INIT = dword(0x53b350)
    """
    [32-bit Boolean] (EU) State Check | Is Game Init
    (isInit)
    """

    EU_HEAP_POINTER = dword(0x53cec4)
    """
    [32-bit Pointer] (EU) Heap Pointer
    (heap_ptr.30)
    """

    EU_STATE_CHECK_MOVIE_PLAYING = dword(0x5da320)
    """
    [32-bit Boolean] (EU) State Check | Movie Playing
    (g_FMVEnable)
    """

    EU_XDATARESOURCEMANAGER = dword(0x5da42c)
    """
    [32-bit Pointer] (EU) XDataResourceManager
    +0x18 = [32-bit Pointer] Pointer to Hashmap | XDataResourceDescriptor
    - Array of 4300 32-bit pointers in a deterministic order based on their key name
    - Always point to 0x1ce3700
    - Some pointers can be null because there is more reserved slots than actual keys
    - Hash implementation is different between EU and US, keys are not stored in the same order between versions
    - Dump of all keys with their associated base pointers:
    - https://github.com/wormi-ra/RA-Scripts/blob/main/Worms%203D%20(PS2)/data/xdata.csv
    - Each entry follow the same structure:
    ++0x4 = [32-bit Pointer] XDataResourceDetails
    +++0x14 = [32-bit Pointer] (EU) Key Name
    +++0x18 = [32-bit Pointer] (US) Key Name
    +++0x1c = [32-bit] Data, can be a pointer or a value depending on resource type
    """

    EU_MISSIONSERVICE = dword(0x5db744)
    """
    [32-bit Pointer] (EU) MissionService
    +0x1c = [32-bit Pointer] Campaign IDs Array
    +0x2c = [32-bit Pointer] Challenge IDs Array
    +0x3c = [32-bit Pointer] Tutorial IDs Array
    +0x4c = [32-bit Pointer] Unlocked Maps Array
    Can't really determine the size of each array
    """

    EU_SERIAL = dword_be(0x5de0cc)
    """
    [32-bit BE ASCII] (EU) Serial
    (cdrom0:\\SLES_518.43;1)
    0x534c4553 = SLES
    """

    EU_STATE_CHECK_TITLE_SCREEN_ACTIVE = dword(0x5e2008)
    """
    [32-bit Boolean] (EU) State Check | Title Screen Active
    """

    EU_STATE_CHECK_IN_MENU = dword(0x5e200c)
    """
    [32-bit Boolean]  (EU) State Check | In Menu
    """

    EU_STATE_CHECK_IN_GAME = dword(0x5e2018)
    """
    [32-bit Boolean] (EU) State Check | In Game
    """

    US_STATE_CHECK_IS_LOADING = dword(0x5f269c)
    """
    [32-bit Boolean] (US) State Check | Is Loading
    """

    US_STATE_CHECK_IS_GAME_INIT = dword(0x5fb880)
    """
    [32-bit Boolean] (US) State Check | Is Game Init
    """

    US_STATE_CHECK_MOVIE_PLAYING = dword(0x5ff3f0)
    """
    [32-bit Boolean] (US) State Check | Movie Playing
    (g_FMVEnable)
    """

    NTSC_SERIAL = dword_be(0x6b294c)
    """
    [NTSC] | [32 Bit BE] Serial
    (cdrom0:\\SLUS_208.94;1)
    """

    EU_XMEMORYMANAGER_ARENALIST = (0x6b84d8)
    """
    [80 bytes] (EU) XMemoryManager | ArenaList
    Base array of 20 pointers for each of the 20 memory arenas.
    Arenas are always allocated at the same address every time and it can be very valuable to learn their regions for memory digging and understanding in which memory region is the address of a value you are looking for.

    List of arena regions in order:
    0x6d7080-0x7fc000 = XString
    0x7fe080-0x80e080 = XDxFieldManager.Data      
    0x80e100-0x81e100 = XDxFieldManager.Descriptor
    0x81e180-0x14fdfe0 = MField
    0x14fe000-0x17f2d60 = XContainer
    0x17f2d80-0x1832d80 = XLua
    0x1832e00-0x1ab2860 = AnimArena
    0x0 = ps2gl.DMA (Unused)
    0x0 = ps2gl.DList (Unused)
    0x1aba900-0x1b4d0c0 = PS2.DisplayList
    0x1b4d100-0x1b4f100 = CameraArena
    0x1b4f180-0x1b53180 = OtherStuffArena
    0x1b53200-0x1b55200 = ScriptArena
    0x1b55280-0x1b57280 = MessageRelayArena
    0x1b57300-0x1b5a300 = ParticleEmmiter
    0x1b5a380-0x1bda380 = ParticleObjects
    0x1bda400-0x1be0400 = InputArena
    0x1be0480-0x1c60480 = LandArena
    0x1c60500-0x1c62500 = ObjectRegArena
    0x1c62580-0x1ca4430 = AiArena
    """

    EU_INGAME_WORM_DATA_INSTANCES_ARRAY = dword(0x6ce018)
    """
    [32-bit Pointer] (EU) Ingame | Worm Data Instances Array [0]
    (DRM::g_pWormInstances)
    +0x4
    ++0x1c = [32-bit Pointer] WormDataContainer
    +++0x50 = [32-bit Float] X Position
    +++0x54 = [32-bit Float] Y Position
    +++0x58 = [32-bit Float] Z Position
    +++0x6c = [32-bit Pointer] SFX Bank Name
    +++0x68 = [32-bit] Weapon Herd
    +++0x70 = [32-bit] Weapon Fuse
    +++0x74 = [32-bit Float] Weapon Angle
    +++0x78 = [32-bit] Pending Poison Damage
    +++0x7C = [32-bit Float] Slope Angle
    +++0x80 = [32-bit] Animation State
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
    +++0x88 = [32-bit] Poison Rate
    +++0x8c = [32-bit Pointer] Name
    +++0x90 = [32-bit Float] Gun Wobble Yaw
    +++0x94 = [32-bit Float] Gun Wobble Pitch
    +++0x9c = [32-bit] Current Health
    +++0xa0 = [32-bit] Initial Health
    +++0xa4 = [32-bit] Pending Damage
    +++0xa8 = [16-bit] CPU Action Radius
    +++0xaa = [16-bit] Worm Health
    +++0xb4 = [32-bit Boolean] Is Quick Walking
    +++0xb8 = [32-bit Boolean] Is Hat Wearer
    +++0xbc = [32-bit Boolean] Is Allowed To Take Turn
    +++0xc0 = [32-bit Boolean] Is Parachute Spawn
    +++0xc4 = [32-bit Boolean] Artillary Mode
    +++0xc8 = [32-bit Boolean] Is After Touching?
    +++0xcc = [32-bit Boolean] Is Vital
    +++0xd0 = [32-bit Boolean] Place Worm At Position?
    +++0xd4 = [8-bit] CPU Fixed Weapon
    +++0xd5 = [8-bit] Team Index
    +++0xd8 = [32-bit Boolean] Weapon is Bounce Max
    +++0xdc = [32-bit Boolean] Is Active
    +++0xf8 = [32-bit Boolean] Has Drunk Redbull
    +++0x100 = [32-bit Boolean] Is Emotional
    +++0x104 = [32-bit Boolean] Is Teleport In
    """

    EU_INGAME_WORM_DATA_INSTANCES_ARRAY_1 = dword(0x6ce01c)
    """
    [32-bit Pointer] (EU) Ingame | Worm Data Instances Array [1]
    """

    EU_INGAME_WORM_DATA_INSTANCES_ARRAY_2 = dword(0x6ce020)
    """
    [32-bit Pointer] (EU) Ingame | Worm Data Instances Array [2]
    """

    EU_INGAME_WORM_DATA_INSTANCES_ARRAY_3 = dword(0x6ce024)
    """
    [32-bit Pointer] (EU) Ingame | Worm Data Instances Array [3]
    """

    EU_INGAME_WORM_DATA_INSTANCES_ARRAY_4 = dword(0x6ce028)
    """
    [32-bit Pointer] (EU) Ingame | Worm Data Instances Array [4]
    """

    EU_INGAME_WORM_DATA_INSTANCES_ARRAY_5 = dword(0x6ce02c)
    """
    [32-bit Pointer] (EU) Ingame | Worm Data Instances Array [5]
    """

    EU_INGAME_WORM_DATA_INSTANCES_ARRAY_6 = dword(0x6ce030)
    """
    [32-bit Pointer] (EU) Ingame | Worm Data Instances Array [6]
    """

    EU_INGAME_WORM_DATA_INSTANCES_ARRAY_7 = dword(0x6ce034)
    """
    [32-bit Pointer] (EU) Ingame | Worm Data Instances Array [7]
    """

    EU_INGAME_WORM_DATA_INSTANCES_ARRAY_8 = dword(0x6ce038)
    """
    [32-bit Pointer] (EU) Ingame | Worm Data Instances Array [8]
    """

    EU_INGAME_WORM_DATA_INSTANCES_ARRAY_9 = dword(0x6ce03c)
    """
    [32-bit Pointer] (EU) Ingame | Worm Data Instances Array [9]
    """

    EU_INGAME_WORM_DATA_INSTANCES_ARRAY_10 = dword(0x6ce040)
    """
    [32-bit Pointer] (EU) Ingame | Worm Data Instances Array [10]
    """

    EU_INGAME_WORM_DATA_INSTANCES_ARRAY_11 = dword(0x6ce044)
    """
    [32-bit Pointer] (EU) Ingame | Worm Data Instances Array [11]
    """

    EU_INGAME_WORM_DATA_INSTANCES_ARRAY_12 = dword(0x6ce048)
    """
    [32-bit Pointer] (EU) Ingame | Worm Data Instances Array [12]
    """

    EU_INGAME_WORM_DATA_INSTANCES_ARRAY_13 = dword(0x6ce04c)
    """
    [32-bit Pointer] (EU) Ingame | Worm Data Instances Array [13]
    """

    EU_INGAME_WORM_DATA_INSTANCES_ARRAY_14 = dword(0x6ce050)
    """
    [32-bit Pointer] (EU) Ingame | Worm Data Instances Array [14]
    """

    EU_INGAME_WORM_DATA_INSTANCES_ARRAY_15 = dword(0x6ce054)
    """
    [32-bit Pointer] (EU) Ingame | Worm Data Instances Array [15]
    """

    EU_INGAME_WORM_INVENTORY_INSTANCES_ARRAY = dword(0x6ce058)
    """
    [32-bit Pointer] (EU) Ingame | Worm Inventory Instances Array [0]
    (DRM::g_pWormInventoryInstances)
    +0x4
    ++0x1c = [32-bit Pointer] WeaponInventory
    +++0x14 = [50 bytes] Weapon Ammo Data (See 0x6ce0e8)
    """

    EU_INGAME_WORM_INVENTORY_INSTANCES_ARRAY_1 = dword(0x6ce05c)
    """
    [32-bit Pointer] (EU) Ingame | Worm Inventory Instances Array [1]
    """

    EU_INGAME_WORM_INVENTORY_INSTANCES_ARRAY_2 = dword(0x6ce060)
    """
    [32-bit Pointer] (EU) Ingame | Worm Inventory Instances Array [2]
    """

    EU_INGAME_WORM_INVENTORY_INSTANCES_ARRAY_3 = dword(0x6ce064)
    """
    [32-bit Pointer] (EU) Ingame | Worm Inventory Instances Array [3]
    """

    EU_INGAME_WORM_INVENTORY_INSTANCES_ARRAY_4 = dword(0x6ce068)
    """
    [32-bit Pointer] (EU) Ingame | Worm Inventory Instances Array [4]
    """

    EU_INGAME_WORM_INVENTORY_INSTANCES_ARRAY_5 = dword(0x6ce06c)
    """
    [32-bit Pointer] (EU) Ingame | Worm Inventory Instances Array [5]
    """

    EU_INGAME_WORM_INVENTORY_INSTANCES_ARRAY_6 = dword(0x6ce070)
    """
    [32-bit Pointer] (EU) Ingame | Worm Inventory Instances Array [6]
    """

    EU_INGAME_WORM_INVENTORY_INSTANCES_ARRAY_7 = dword(0x6ce074)
    """
    [32-bit Pointer] (EU) Ingame | Worm Inventory Instances Array [7]
    """

    EU_INGAME_WORM_INVENTORY_INSTANCES_ARRAY_8 = dword(0x6ce078)
    """
    [32-bit Pointer] (EU) Ingame | Worm Inventory Instances Array [8]
    """

    EU_INGAME_WORM_INVENTORY_INSTANCES_ARRAY_9 = dword(0x6ce07c)
    """
    [32-bit Pointer] (EU) Ingame | Worm Inventory Instances Array [9]
    """

    EU_INGAME_WORM_INVENTORY_INSTANCES_ARRAY_10 = dword(0x6ce080)
    """
    [32-bit Pointer] (EU) Ingame | Worm Inventory Instances Array [10]
    """

    EU_INGAME_WORM_INVENTORY_INSTANCES_ARRAY_11 = dword(0x6ce084)
    """
    [32-bit Pointer] (EU) Ingame | Worm Inventory Instances Array [11]
    """

    EU_INGAME_WORM_INVENTORY_INSTANCES_ARRAY_12 = dword(0x6ce088)
    """
    [32-bit Pointer] (EU) Ingame | Worm Inventory Instances Array [12]
    """

    EU_INGAME_WORM_INVENTORY_INSTANCES_ARRAY_13 = dword(0x6ce08c)
    """
    [32-bit Pointer] (EU) Ingame | Worm Inventory Instances Array [13]
    """

    EU_INGAME_WORM_INVENTORY_INSTANCES_ARRAY_14 = dword(0x6ce090)
    """
    [32-bit Pointer] (EU) Ingame | Worm Inventory Instances Array [14]
    """

    EU_INGAME_WORM_INVENTORY_INSTANCES_ARRAY_15 = dword(0x6ce094)
    """
    [32-bit Pointer] (EU) Ingame | Worm Inventory Instances Array [15]
    """

    EU_INGAME_TEAM_DATA_INSTANCES_ARRAY = dword(0x6ce0d8)
    """
    [32-bit Pointer] (EU) Ingame |  Team Data Instances Array [0]
    (DRM::g_pTeamInstances)
    +0x4
    ++0x1c = [32-bit Pointer] TeamDataContainer
    +++0x14 = [32-bit Pointer] Flag GFX Name
    +++0x18 = [32-bit] Score Points
    +++0x1c = [32-bit Pointer] Team Name
    +++0x20 = [32-bit Boolean] Is Local
    +++0x24 = [8-bit] Skill
    +++0x28 = [32-bit Boolean] Is Crate Spy Active
    +++0x2c = [32-bit Boolean] Team Surrendered
    +++0x30 = [8-bit] Worms Count End
    +++0x31 = [8-bit] Grave Index
    +++0x32 = [8-bit] Rounds Won
    +++0x34 = [32-bit Boolean] Is AI Controlled
    +++0x38 = [32-bit Boolean] CPU Attack Disabled
    +++0x3c = [8-bit] Allied Group
    +++0x40 = [32-bit Boolean] Team Must Survive
    +++0x44 = [8-bit] Team Color
    --- 0x0 = Red
    --- 0x1 = Blue
    --- 0x2 = Green
    --- 0x3 = Yellow
    --- * = Black
    +++0x45 = [8-bit] Worms Count Start
    +++0x48 = [32-bit Boolean] Is Active
    """

    EU_INGAME_TEAM_DATA_INSTANCES_ARRAY_1 = dword(0x6ce0dc)
    """
    [32-bit Pointer] (EU) Ingame |  Team Data Instances Array [1]
    """

    EU_INGAME_TEAM_DATA_INSTANCES_ARRAY_2 = dword(0x6ce0e0)
    """
    [32-bit Pointer] (EU) Ingame |  Team Data Instances Array [2]
    """

    EU_INGAME_TEAM_DATA_INSTANCES_ARRAY_3 = dword(0x6ce0e4)
    """
    [32-bit Pointer] (EU) Ingame |  Team Data Instances Array [3]
    """

    EU_TEAM_INSTANCES_INVENTORY_ARRAY = dword(0x6ce0e8)
    """
    [32-bit Pointer] (EU) Team Instances Inventory Array [0]
    (DRM::g_pTeamInventoryInstances)
    This is the most commonly used inventory in missions, note that the final ammo count for a given worm can be different, all inventory types are summed up as such:
    Final Inventory = Alliance Inventory + Team Inventory + Worm Inventory
    +0x4
    ++0x1c = [32-bit Pointer] WeaponInventory
    --- An ammo value of 0xff means infinite ammo
    +++0x14 = [8-bit] Ammo | Old Woman
    +++0x15 = [8-bit] Ammo | Mad Cow
    +++0x16 = [8-bit] Ammo | Sheep Strike (Unused)
    +++0x17 = [8-bit] Ammo | Gas Canister
    +++0x18 = [8-bit] Ammo | Petrol Bomb
    +++0x19 = [8-bit] Ammo | Bridge Kit
    +++0x1a = [8-bit] Ammo | Sheep
    +++0x1b = [8-bit] Ammo | Earthquake
    +++0x1c = [8-bit] Ammo | Homing Pidgeon
    +++0x1d = [8-bit] Ammo | Mortar
    +++0x1e = [8-bit] Ammo | Homing Missile
    +++0x1f = [8-bit] Ammo | Fire Punch
    +++0x20 = [8-bit] Ammo | Bazooka
    +++0x21 = [8-bit] Ammo | Prod
    +++0x22 = [8-bit] Ammo | Baseball Bat
    +++0x23 = [8-bit] Ammo | Uzi
    +++0x24 = [8-bit] Ammo | Shotgun
    +++0x25 = [8-bit] Ammo | Landmine
    +++0x26 = [8-bit] Ammo | Blowpipe
    +++0x27 = [8-bit] Ammo | Holy Hand Grenade
    +++0x28 = [8-bit] Ammo | Dynamite
    +++0x29 = [8-bit] Ammo | Airstrike
    +++0x2a = [8-bit] Ammo | Cluster Grenade
    +++0x2b = [8-bit] Ammo | Grenade
    +++0x2c = [8-bit] Ammo | Viking Axe
    +++0x2d = [8-bit] Ammo | Concrete Donkey
    +++0x2e = [8-bit] Ammo | Teleport
    +++0x2f = [8-bit] Ammo | Binoculars
    +++0x30 = [8-bit] Ammo | Sticky Bomb
    +++0x31 = [8-bit] Ammo | Mega Mine
    +++0x32 = [8-bit] Ammo | Doctor's Strike
    +++0x33 = [8-bit] Ammo | Lottery Strike
    +++0x34 = [8-bit] Ammo | Banana Bomb
    +++0x35 = [8-bit] Ammo | Freeze
    +++0x36 = [8-bit] Ammo | Change Worm
    +++0x37 = [8-bit] Ammo | Surrender
    +++0x38 = [8-bit] Ammo | Skip Go
    +++0x39 = [8-bit] Ammo | Jetpack
    +++0x3a = [8-bit] Ammo | Redbull
    +++0x3b = [8-bit] Ammo | Laser Sight (Unused)
    +++0x3c = [8-bit] Ammo | Quick Walk
    +++0x3d = [8-bit] Ammo | Low Gravity
    +++0x3e = [8-bit] Ammo | Scales of Justice
    +++0x3f = [8-bit] Ammo | Parachute
    +++0x40 = [8-bit] Ammo | Ninja Rope
    +++0x41 = [8-bit] Ammo | Mine Strike (Unused)
    +++0x42 = [8-bit] Ammo | Girder
    +++0x43 = [8-bit] Ammo | Super Sheep
    +++0x44 = [8-bit] Ammo | Magic Bullet (Unused)
    +++0x45 = [8-bit] Ammo | Armageddon (Unused)
    +++0x46 = [8-bit] Ammo | Nuclear Bomb
    """

    EU_TEAM_INSTANCES_INVENTORY_ARRAY_1 = dword(0x6ce0ec)
    """
    [32-bit Pointer] (EU) Team Instances Inventory Array [1]
    """

    EU_TEAM_INSTANCES_INVENTORY_ARRAY_2 = dword(0x6ce0f0)
    """
    [32-bit Pointer] (EU) Team Instances Inventory Array [2]
    """

    EU_TEAM_INSTANCES_INVENTORY_ARRAY_3 = dword(0x6ce0f4)
    """
    [32-bit Pointer] (EU) Team Instances Inventory Array [3]
    """

    EU_TEAM_PERSIST_INSTANCES_ARRAY = dword(0x6ce0f8)
    """
    [32-bit Pointer] (EU) Team Persist Instances Array [0]
    (DRM::g_pTeamPersistInstances)
    Most likely used for storing scores between rounds in multiplayer games
    +0x4
    ++0x1c = [32-bit Pointer] TeamPersistDataContainer
    +++0x14 = [32-bit] Rounds Won
    """

    EU_TEAM_PERSIST_INSTANCES_ARRAY_1 = dword(0x6ce0fc)
    """
    [32-bit Pointer] (EU) Team Persist Instances Array [1]
    """

    EU_TEAM_PERSIST_INSTANCES_ARRAY_2 = dword(0x6ce100)
    """
    [32-bit Pointer] (EU) Team Persist Instances Array [2]
    """

    EU_TEAM_PERSIST_INSTANCES_ARRAY_3 = dword(0x6ce104)
    """
    [32-bit Pointer] (EU) Team Persist Instances Array [3]
    """

    EU_ALLIANCE_INSTANCES_INVENTORY_ARRAY = dword(0x6ce108)
    """
    [32-bit Pointer] (EU) Alliance Instances Inventory Array [0]
    (DRM::g_pAllianceInventoryInstances)
    Shared inventory between teams of the same color, mostly used for multiplayer
    +0x4
    ++0x1c = [32-bit Pointer] WeaponInventory
    +++0x14 = [50 bytes] Weapon Ammo Data (See 0x6ce0e8)
    """

    EU_ALLIANCE_INSTANCES_INVENTORY_ARRAY_1 = dword(0x6ce10c)
    """
    [32-bit Pointer] (EU) Alliance Instances Inventory Array [1]
    """

    EU_ALLIANCE_INSTANCES_INVENTORY_ARRAY_2 = dword(0x6ce110)
    """
    [32-bit Pointer] (EU) Alliance Instances Inventory Array [2]
    """

    EU_ALLIANCE_INSTANCES_INVENTORY_ARRAY_3 = dword(0x6ce114)
    """
    [32-bit Pointer] (EU) Alliance Instances Inventory Array [3]
    """

    EU_CONTROLLER_BUTTON_PRESSED_PRIMARY = byte(0x6cfc80)
    """
    [8-bit Bitfield] (EU) Controller | Button Pressed Primary
    bit0 = L2
    bit1 = R2
    bit2  = L1
    bit3 = R1
    bit4 = Triangle
    bit5 = O
    bit6 = X
    bit7 = Square
    """

    EU_CONTROLLER_BUTTON_PRESSED_SECONDARY = byte(0x6cfc81)
    """
    [8-bit Bitfield] (EU) Controller | Button Pressed Secondary
    bit0 = Select
    bit1 = L3
    bit2  = R3
    bit3 = Start
    bit4 = D-Pad Up
    bit5 = D-Pad Right
    bit6 = D-Pad Down
    bit7 = D-Pad Left
    """

    US_XMEMORYMANAGER_ARENALIST = (0x784c18)
    """
    [80 bytes] (US) XMemoryManager | ArenaList
    Base array of 20 pointers for each of the 20 memory arenas.
    Arenas are always allocated at the same address every time and it can be very valuable to learn their regions for memory digging and understanding in which memory region is the address of a value you are looking for.

    List of arena regions in order:
    0x7a4400-0x898640 = XString
    0x89a680-0x8a2680 = XDxFieldManager.Data      
    0x8a2700-0x8aa700 = XDxFieldManager.Descriptor
    0x8aa780-0x15104c0 = MField
    0x1510500-0x180a080 = XContainer
    0x180a100-0x183a100 = XLua
    0x183a180-0x1b0a4f0 = AnimArena
    0x0 = ps2gl.DMA (Unused)
    0x0 = ps2gl.DList (Unused)
    0x1b12580-0x1ba4d40 = PS2.DisplayList
    0x1ba4d80-0x1ba6d80 = CameraArena
    0x1ba6e00-0x1baae00 = OtherStuffArena
    0x1baae80-0x1bace80 = ScriptArena
    0x1bacf00-0x1baef00 = MessageRelayArena
    0x1baef80-0x1bb1f80 = ParticleEmmiter
    0x1bb2000-0x1bf2000 = ParticleObjects
    0x1bf2080-0x1bf8080 = InputArena
    0x1bf8100-0x1c78100 = LandArena
    0x1c78180-0x1c7a180 = ObjectRegArena
    0x1c7a200-0x1cbc0b0 = AiArena
    """

    US_INGAME_WORM_DATA_INSTANCES_ARRAY = dword(0x79dc00)
    """
    [32-bit Pointer] (US) Ingame | Worm Data Instances Array [0]
    (DRM::g_pWormInstances)
    +0x4
    ++0x1c = [32-bit Pointer] WormDataContainer
    +++0x50 = [32-bit Float] X Position
    +++0x54 = [32-bit Float] Y Position
    +++0x58 = [32-bit Float] Z Position
    +++0x6c = [32-bit Pointer] SFX Bank Name
    +++0x68 = [32-bit] Weapon Herd
    +++0x70 = [32-bit] Weapon Fuse
    +++0x74 = [32-bit Float] Weapon Angle
    +++0x78 = [32-bit] Pending Poison Damage
    +++0x7C = [32-bit Float] Slope Angle
    +++0x80 = [32-bit] Animation State
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
    +++0x88 = [32-bit] Poison Rate
    +++0x8c = [32-bit Pointer] Name
    +++0x90 = [32-bit Float] Gun Wobble Yaw
    +++0x94 = [32-bit Float] Gun Wobble Pitch
    +++0x9c = [32-bit] Current Health
    +++0xa0 = [32-bit] Initial Health
    +++0xa4 = [32-bit] Pending Damage
    +++0xa8 = [16-bit] CPU Action Radius
    +++0xaa = [16-bit] Worm Health
    +++0xb4 = [32-bit Boolean] Is Quick Walking
    +++0xb8 = [32-bit Boolean] Is Hat Wearer
    +++0xbc = [32-bit Boolean] Is Allowed To Take Turn
    +++0xc0 = [32-bit Boolean] Is Parachute Spawn
    +++0xc4 = [32-bit Boolean] Artillary Mode
    +++0xc8 = [32-bit Boolean] Is After Touching?
    +++0xcc = [32-bit Boolean] Is Vital
    +++0xd0 = [32-bit Boolean] Place Worm At Position?
    +++0xd4 = [8-bit] CPU Fixed Weapon
    +++0xd5 = [8-bit] Team Index
    +++0xd8 = [32-bit Boolean] Weapon is Bounce Max
    +++0xdc = [32-bit Boolean] Is Active
    +++0xf8 = [32-bit Boolean] Has Drunk Redbull
    +++0x100 = [32-bit Boolean] Is Emotional
    +++0x104 = [32-bit Boolean] Is Teleport In
    """

    US_INGAME_WORM_DATA_INSTANCES_ARRAY_1 = dword(0x79dc04)
    """
    [32-bit Pointer] (US) Ingame | Worm Data Instances Array [1]
    """

    US_INGAME_WORM_DATA_INSTANCES_ARRAY_2 = dword(0x79dc08)
    """
    [32-bit Pointer] (US) Ingame | Worm Data Instances Array [2]
    """

    US_INGAME_WORM_DATA_INSTANCES_ARRAY_3 = dword(0x79dc0c)
    """
    [32-bit Pointer] (US) Ingame | Worm Data Instances Array [3]
    """

    US_INGAME_WORM_DATA_INSTANCES_ARRAY_4 = dword(0x79dc10)
    """
    [32-bit Pointer] (US) Ingame | Worm Data Instances Array [4]
    """

    US_INGAME_WORM_DATA_INSTANCES_ARRAY_5 = dword(0x79dc14)
    """
    [32-bit Pointer] (US) Ingame | Worm Data Instances Array [5]
    """

    US_INGAME_WORM_DATA_INSTANCES_ARRAY_6 = dword(0x79dc18)
    """
    [32-bit Pointer] (US) Ingame | Worm Data Instances Array [6]
    """

    US_INGAME_WORM_DATA_INSTANCES_ARRAY_7 = dword(0x79dc1c)
    """
    [32-bit Pointer] (US) Ingame | Worm Data Instances Array [7]
    """

    US_INGAME_WORM_DATA_INSTANCES_ARRAY_8 = dword(0x79dc20)
    """
    [32-bit Pointer] (US) Ingame | Worm Data Instances Array [8]
    """

    US_INGAME_WORM_DATA_INSTANCES_ARRAY_9 = dword(0x79dc24)
    """
    [32-bit Pointer] (US) Ingame | Worm Data Instances Array [9]
    """

    US_INGAME_WORM_DATA_INSTANCES_ARRAY_10 = dword(0x79dc28)
    """
    [32-bit Pointer] (US) Ingame | Worm Data Instances Array [10]
    """

    US_INGAME_WORM_DATA_INSTANCES_ARRAY_11 = dword(0x79dc2c)
    """
    [32-bit Pointer] (US) Ingame | Worm Data Instances Array [11]
    """

    US_INGAME_WORM_DATA_INSTANCES_ARRAY_12 = dword(0x79dc30)
    """
    [32-bit Pointer] (US) Ingame | Worm Data Instances Array [12]
    """

    US_INGAME_WORM_DATA_INSTANCES_ARRAY_13 = dword(0x79dc34)
    """
    [32-bit Pointer] (US) Ingame | Worm Data Instances Array [13]
    """

    US_INGAME_WORM_DATA_INSTANCES_ARRAY_14 = dword(0x79dc38)
    """
    [32-bit Pointer] (US) Ingame | Worm Data Instances Array [14]
    """

    US_INGAME_WORM_DATA_INSTANCES_ARRAY_15 = dword(0x79dc3c)
    """
    [32-bit Pointer] (US) Ingame | Worm Data Instances Array [15]
    """

    US_INGAME_WORM_INVENTORY_INSTANCES_ARRAY = dword(0x79dc40)
    """
    [32-bit Pointer] (US) Ingame | Worm Inventory Instances Array [0]
    (DRM::g_pWormInventoryInstances)
    +0x4
    ++0x1c = [32-bit Pointer] WeaponInventory
    +++0x14 = [50 bytes] Weapon Ammo Data (See 0x79dcd0)
    """

    US_INGAME_WORM_INVENTORY_INSTANCES_ARRAY_1 = dword(0x79dc44)
    """
    [32-bit Pointer] (US) Ingame | Worm Inventory Instances Array [1]
    """

    US_INGAME_WORM_INVENTORY_INSTANCES_ARRAY_2 = dword(0x79dc48)
    """
    [32-bit Pointer] (US) Ingame | Worm Inventory Instances Array [2]
    """

    US_INGAME_WORM_INVENTORY_INSTANCES_ARRAY_3 = dword(0x79dc4c)
    """
    [32-bit Pointer] (US) Ingame | Worm Inventory Instances Array [3]
    """

    US_INGAME_WORM_INVENTORY_INSTANCES_ARRAY_4 = dword(0x79dc50)
    """
    [32-bit Pointer] (US) Ingame | Worm Inventory Instances Array [4]
    """

    US_INGAME_WORM_INVENTORY_INSTANCES_ARRAY_5 = dword(0x79dc54)
    """
    [32-bit Pointer] (US) Ingame | Worm Inventory Instances Array [5]
    """

    US_INGAME_WORM_INVENTORY_INSTANCES_ARRAY_6 = dword(0x79dc58)
    """
    [32-bit Pointer] (US) Ingame | Worm Inventory Instances Array [6]
    """

    US_INGAME_WORM_INVENTORY_INSTANCES_ARRAY_7 = dword(0x79dc5c)
    """
    [32-bit Pointer] (US) Ingame | Worm Inventory Instances Array [7]
    """

    US_INGAME_WORM_INVENTORY_INSTANCES_ARRAY_8 = dword(0x79dc60)
    """
    [32-bit Pointer] (US) Ingame | Worm Inventory Instances Array [8]
    """

    US_INGAME_WORM_INVENTORY_INSTANCES_ARRAY_9 = dword(0x79dc64)
    """
    [32-bit Pointer] (US) Ingame | Worm Inventory Instances Array [9]
    """

    US_INGAME_WORM_INVENTORY_INSTANCES_ARRAY_10 = dword(0x79dc68)
    """
    [32-bit Pointer] (US) Ingame | Worm Inventory Instances Array [10]
    """

    US_INGAME_WORM_INVENTORY_INSTANCES_ARRAY_11 = dword(0x79dc6c)
    """
    [32-bit Pointer] (US) Ingame | Worm Inventory Instances Array [11]
    """

    US_INGAME_WORM_INVENTORY_INSTANCES_ARRAY_12 = dword(0x79dc70)
    """
    [32-bit Pointer] (US) Ingame | Worm Inventory Instances Array [12]
    """

    US_INGAME_WORM_INVENTORY_INSTANCES_ARRAY_13 = dword(0x79dc74)
    """
    [32-bit Pointer] (US) Ingame | Worm Inventory Instances Array [13]
    """

    US_INGAME_WORM_INVENTORY_INSTANCES_ARRAY_14 = dword(0x79dc78)
    """
    [32-bit Pointer] (US) Ingame | Worm Inventory Instances Array [14]
    """

    US_INGAME_WORM_INVENTORY_INSTANCES_ARRAY_15 = dword(0x79dc7c)
    """
    [32-bit Pointer] (US) Ingame | Worm Inventory Instances Array [15]
    """

    US_INGAME_TEAM_DATA_INSTANCES_ARRAY = dword(0x79dcc0)
    """
    [32-bit Pointer] (US) Ingame |  Team Data Instances Array [0]
    (DRM::g_pTeamInstances)
    +0x4
    ++0x1c = [32-bit Pointer] TeamDataContainer
    +++0x14 = [32-bit Pointer] Flag GFX Name
    +++0x18 = [32-bit] Score Points
    +++0x1c = [32-bit Pointer] Team Name
    +++0x20 = [32-bit Boolean] Is Local
    +++0x24 = [8-bit] Skill
    +++0x28 = [32-bit Boolean] Is Crate Spy Active
    +++0x2c = [32-bit Boolean] Team Surrendered
    +++0x30 = [8-bit] Worms Count End
    +++0x31 = [8-bit] Grave Index
    +++0x32 = [8-bit] Rounds Won
    +++0x34 = [32-bit Boolean] Is AI Controlled
    +++0x38 = [32-bit Boolean] CPU Attack Disabled
    +++0x3c = [8-bit] Allied Group
    +++0x40 = [32-bit Boolean] Team Must Survive
    +++0x44 = [8-bit] Team Color
    --- 0x0 = Red
    --- 0x1 = Blue
    --- 0x2 = Green
    --- 0x3 = Yellow
    --- * = Black
    +++0x45 = [8-bit] Worms Count Start
    +++0x48 = [32-bit Boolean] Is Active
    """

    US_INGAME_TEAM_DATA_INSTANCES_ARRAY_1 = dword(0x79dcc4)
    """
    [32-bit Pointer] (US) Ingame |  Team Data Instances Array [1]
    """

    US_INGAME_TEAM_DATA_INSTANCES_ARRAY_2 = dword(0x79dcc8)
    """
    [32-bit Pointer] (US) Ingame |  Team Data Instances Array [2]
    """

    US_INGAME_TEAM_DATA_INSTANCES_ARRAY_3 = dword(0x79dccc)
    """
    [32-bit Pointer] (US) Ingame |  Team Data Instances Array [3]
    """

    US_TEAM_INSTANCES_INVENTORY_ARRAY = dword(0x79dcd0)
    """
    [32-bit Pointer] (US) Team Instances Inventory Array [0]
    (DRM::g_pTeamInventoryInstances)
    This is the most commonly used inventory in missions, note that the final ammo count for a given worm can be different, all inventory types are summed up as such:
    Final Inventory = Alliance Inventory + Team Inventory + Worm Inventory
    +0x4
    ++0x1c = [32-bit Pointer] WeaponInventory
    --- An ammo value of 0xff means infinite ammo
    +++0x14 = [8-bit] Ammo | Old Woman
    +++0x15 = [8-bit] Ammo | Mad Cow
    +++0x16 = [8-bit] Ammo | Sheep Strike (Unused)
    +++0x17 = [8-bit] Ammo | Gas Canister
    +++0x18 = [8-bit] Ammo | Petrol Bomb
    +++0x19 = [8-bit] Ammo | Bridge Kit
    +++0x1a = [8-bit] Ammo | Sheep
    +++0x1b = [8-bit] Ammo | Earthquake
    +++0x1c = [8-bit] Ammo | Homing Pidgeon
    +++0x1d = [8-bit] Ammo | Mortar
    +++0x1e = [8-bit] Ammo | Homing Missile
    +++0x1f = [8-bit] Ammo | Fire Punch
    +++0x20 = [8-bit] Ammo | Bazooka
    +++0x21 = [8-bit] Ammo | Prod
    +++0x22 = [8-bit] Ammo | Baseball Bat
    +++0x23 = [8-bit] Ammo | Uzi
    +++0x24 = [8-bit] Ammo | Shotgun
    +++0x25 = [8-bit] Ammo | Landmine
    +++0x26 = [8-bit] Ammo | Blowpipe
    +++0x27 = [8-bit] Ammo | Holy Hand Grenade
    +++0x28 = [8-bit] Ammo | Dynamite
    +++0x29 = [8-bit] Ammo | Airstrike
    +++0x2a = [8-bit] Ammo | Cluster Grenade
    +++0x2b = [8-bit] Ammo | Grenade
    +++0x2c = [8-bit] Ammo | Viking Axe
    +++0x2d = [8-bit] Ammo | Concrete Donkey
    +++0x2e = [8-bit] Ammo | Teleport
    +++0x2f = [8-bit] Ammo | Binoculars
    +++0x30 = [8-bit] Ammo | Sticky Bomb
    +++0x31 = [8-bit] Ammo | Mega Mine
    +++0x32 = [8-bit] Ammo | Doctor's Strike
    +++0x33 = [8-bit] Ammo | Lottery Strike
    +++0x34 = [8-bit] Ammo | Banana Bomb
    +++0x35 = [8-bit] Ammo | Freeze
    +++0x36 = [8-bit] Ammo | Change Worm
    +++0x37 = [8-bit] Ammo | Surrender
    +++0x38 = [8-bit] Ammo | Skip Go
    +++0x39 = [8-bit] Ammo | Jetpack
    +++0x3a = [8-bit] Ammo | Redbull
    +++0x3b = [8-bit] Ammo | Laser Sight (Unused)
    +++0x3c = [8-bit] Ammo | Quick Walk
    +++0x3d = [8-bit] Ammo | Low Gravity
    +++0x3e = [8-bit] Ammo | Scales of Justice
    +++0x3f = [8-bit] Ammo | Parachute
    +++0x40 = [8-bit] Ammo | Ninja Rope
    +++0x41 = [8-bit] Ammo | Mine Strike (Unused)
    +++0x42 = [8-bit] Ammo | Girder
    +++0x43 = [8-bit] Ammo | Super Sheep
    +++0x44 = [8-bit] Ammo | Magic Bullet (Unused)
    +++0x45 = [8-bit] Ammo | Armageddon (Unused)
    +++0x46 = [8-bit] Ammo | Nuclear Bomb
    """

    US_TEAM_INSTANCES_INVENTORY_ARRAY_1 = dword(0x79dcd4)
    """
    [32-bit Pointer] (US) Team Instances Inventory Array [1]
    """

    US_TEAM_INSTANCES_INVENTORY_ARRAY_2 = dword(0x79dcd8)
    """
    [32-bit Pointer] (US) Team Instances Inventory Array [2]
    """

    US_TEAM_INSTANCES_INVENTORY_ARRAY_3 = dword(0x79dcdc)
    """
    [32-bit Pointer] (US) Team Instances Inventory Array [3]
    """

    US_TEAM_PERSIST_INSTANCES_POINTER_ARRAY = dword(0x79dce0)
    """
    [32-bit Pointer] (US) Team Persist Instances Pointer Array [0]
    (DRM::g_pTeamPersistInstances)
    Most likely used for storing scores between rounds in multiplayer games
    +0x4
    ++0x1c = [32-bit Pointer] TeamPersistDataContainer
    +++0x14 = [32-bit] Rounds Won
    """

    US_TEAM_PERSIST_INSTANCES_POINTER_ARRAY_1 = dword(0x79dce4)
    """
    [32-bit Pointer] (US) Team Persist Instances Pointer Array [1]
    """

    US_TEAM_PERSIST_INSTANCES_POINTER_ARRAY_2 = dword(0x79dce8)
    """
    [32-bit Pointer] (US) Team Persist Instances Pointer Array [2]
    """

    US_TEAM_PERSIST_INSTANCES_POINTER_ARRAY_3 = dword(0x79dcec)
    """
    [32-bit Pointer] (US) Team Persist Instances Pointer Array [3]
    """

    US_ALLIANCE_INSTANCES_INVENTORY_ARRAY = dword(0x79dcf0)
    """
    [32-bit Pointer] (US) Alliance Instances Inventory Array [0]
    (DRM::g_pAllianceInventoryInstances)
    Shared inventory between teams of the same color, mostly used for multiplayer
    +0x4
    ++0x1c = [32-bit Pointer] WeaponInventory
    +++0x14 = [50 bytes] Weapon Ammo Data (See 0x79dcd0)
    """

    US_ALLIANCE_INSTANCES_INVENTORY_ARRAY_1 = dword(0x79dcf4)
    """
    [32-bit Pointer] (US) Alliance Instances Inventory Array [1]
    """

    US_ALLIANCE_INSTANCES_INVENTORY_ARRAY_2 = dword(0x79dcf8)
    """
    [32-bit Pointer] (US) Alliance Instances Inventory Array [2]
    """

    US_ALLIANCE_INSTANCES_INVENTORY_ARRAY_3 = dword(0x79dcfc)
    """
    [32-bit Pointer] (US) Alliance Instances Inventory Array [3]
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

    US_CONTROLLER_BUTTON_PRESSED_PRIMARY = byte(0x79fcc0)
    """
    [8-bit Bitfield] (US) Controller | Button Pressed Primary
    bit0 = L2
    bit1 = R2
    bit2  = L1
    bit3 = R1
    bit4 = Triangle
    bit5 = O
    bit6 = X
    bit7 = Square
    """

    US_CONTROLLER_BUTTON_PRESSED_SECONDARY = byte(0x79fcc1)
    """
    [8-bit Bitfield] (US) Controller | Button Pressed Secondary
    bit0 = Select
    bit1 = L3
    bit2  = R3
    bit3 = Start
    bit4 = D-Pad Up
    bit5 = D-Pad Right
    bit6 = D-Pad Down
    bit7 = D-Pad Left
    """

    US_INGAME_CURRENT_ACTIVE_WORM_ID = dword(0x153dd1c)
    """
    [32-bit] (US) Ingame | Current Active Worm ID
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

    US_GAME_STATUS_IS_IN_INGAME_CUTSCENE = dword(0x15703bc)
    """
    [32-bit] (US) Game Status | Is in ingame cutscene
    0x0 = False
    0x1 = True
    """

    EU_INGAME_CURRENT_LUA_SCRIPT_NAME = (0x18005b0)
    """
    [16-bytes BE ASCII] (EU) Ingame | Current LUA Script Name
    0x00000000 = Uninitialized
    0xdddddddd = Uninitialized
    0x7475746f7269616c3100 = "tutorial1" | Atlantis Training Facility
    0x7475746f7269616c3200 = "tutorial2" | Down in the Dumps
    0x5475746f7269616c3300 = "Tutorial3" | Return to Chateau Assassin
    0x5475746f7269616c3400 = "Tutorial4" | The Mighty Kong
    0x7475746f7269616c3500 = "tutorial5" | Test Tubes
    0x64726976696e6700 = "driving" | The Driving Range
    0x6464617900 = "dday" | D-Day
    0x43726174654272697461696e00 = "CrateBritain" | Crate Britain
    0x67726176657961726400 = "graveyard" | Grave Danger
    0x6c65656b00 = "leek" | A Leek in a Vegetable Patch
    0x49434500 = "ICE" | Ice, Ice, Maybe
    0x436f6c6c69646500 = "Collide" | When Annelids Collide
    0x72756d00 = "rum" | Rum Deal
    0x637275737400 = "crust" | Earn Your Crust
    0x6170706c65636f726500 = "applecore" | Apple Core Island
    0x68656c746572736b656c74657200 = "helterskelter" | Helter Skelter
    0x63686572727900 = "cherry" | Take My Cherry
    0x636c65616e00 = "clean" | In Space, No-One Can Hear You Clean
    0x74696d6265727300 = "timbers" | Shiver Me Timbers
    0x46414c4c494e4700 = "FALLING" | Falling For You
    0x63726f70636972636c6500 = "cropcircle" | Crop Circle
    0x7472656576696c6c61676500 = "treevillage" | Tree Village Trouble
    0x6c616e64696e6700 = "landing" | Movie Mayhem
    0x6265616e7374616c6b00 = "beanstalk" | Worm and the Beanstalk
    0x5343484f4f4c5300 = "SCHOOLS" | School's in for Summer
    0x686967687374616b657300 = "highstakes" | High Stakes
    0x6e6f74706300 = "notpc" | A Quick Fix
    0x636f6f70656400 = "cooped" | All Cooped Up
    0x545249414c00 = "TRIAL" | Trial of the Damned
    0x53484f57444f574e00 = "SHOWDOWN" | Showdown at the OK Corale Reef
    0x706c6169636500 = "plaice" | Plaice Holder
    0x686f6f6b6c696e6500 = "hookline" | Hook, Line, and Skimmer
    0x66756e6661697200 = "funfair" | Nobody Rides For Free
    0x5065676173757300 = "Pegasus" | Hold Until Relieved
    0x626f6c646c7900 = "boldly" | To Boldly Go
    0x62616c6c6f6f6e00 = "balloon" | Beautiful Balloon
    0x636f756e74696e67736865657000 = "countingsheep" | A Good Nights Sleep
    0x425245414b4641535400 = "BREAKFAST" | Beefcake Breakfast Brawl
    0x686f6c6964617900 = "holiday" | Costa Del Danger
    0x7061636b00 = "pack" | Ragnarok and Roll
    0x414c49454e00 = "ALIEN" | Alien Juice Suckers
    0x54617267657448756e7400 = "TargetHunt" | Shotgun Challenge 1
    0x54617267657448756e743200 = "TargetHunt2" | Shotgun Challenge 2
    0x484f4d494e4700 = "HOMING" | Shotgun Challenge 3
    0x53686565703100 = "Sheep1" | Super Sheep Challenge 1
    0x53686565703200 = "Sheep2" | Super Sheep Challenge 2
    0x54617267657448756e743400 = "TargetHunt4" | Super Sheep Challenge 3
    0x637261746566756e00 = "cratefun" | Jet Pack Challenge 1
    0x6a65747061636b6368616c6c3200 = "jetpackchall2" | Jet Pack Challenge 2
    0x6a65747061636b6368616c6c3300 = "jetpackchall3" | Jet Pack Challenge 3
    0x43687574653100 = "Chute1" | Parachute Challenge 1
    0x63687574653200 = "chute2" | Parachute Challenge 2
    0x63687574653300 = "chute3" | Parachute Challenge 3
    0x44656174686d617463683100 = "Deathmatch1" | Deathmatch Challenge 1
    0x44656174686d617463683200 = "Deathmatch2" | Deathmatch Challenge 2
    0x44656174686d617463683300 = "Deathmatch3" | Deathmatch Challenge 3
    0x44656174686d617463683400 = "Deathmatch4" | Deathmatch Challenge 4
    0x44656174686d617463683500 = "Deathmatch5" | Deathmatch Challenge 5
    0x44656174686d617463683600 = "Deathmatch6" | Deathmatch Challenge 6
    0x44656174686d617463683700 = "Deathmatch7" | Deathmatch Challenge 7
    0x44656174686d617463683800 = "Deathmatch8" | Deathmatch Challenge 8
    0x44656174686d617463683900 = "Deathmatch9" | Deathmatch Challenge 9
    0x44656174686d61746368313000 = "Deathmatch10" | Deathmatch Challenge 10
    0x737464767300 = "stdvs" | Multiplayer Game
    0x6174747261637400 = "attract" | Attract Mode
    """

    US_INGAME_CURRENT_LUA_SCRIPT_NAME = (0x180c5f8)
    """
    [16-bytes BE ASCII] (US) Ingame | Current LUA Script Name
    0x00000000 = Uninitialized
    0xdddddddd = Uninitialized
    0x7475746f7269616c3100 = "tutorial1" | Atlantis Training Facility
    0x7475746f7269616c3200 = "tutorial2" | Down in the Dumps
    0x5475746f7269616c3300 = "Tutorial3" | Return to Chateau Assassin
    0x5475746f7269616c3400 = "Tutorial4" | The Mighty Kong
    0x7475746f7269616c3500 = "tutorial5" | Test Tubes
    0x64726976696e6700 = "driving" | The Driving Range
    0x6464617900 = "dday" | D-Day
    0x43726174654272697461696e00 = "CrateBritain" | Crate Britain
    0x67726176657961726400 = "graveyard" | Grave Danger
    0x6c65656b00 = "leek" | A Leek in a Vegetable Patch
    0x49434500 = "ICE" | Ice, Ice, Maybe
    0x436f6c6c69646500 = "Collide" | When Annelids Collide
    0x72756d00 = "rum" | Rum Deal
    0x637275737400 = "crust" | Earn Your Crust
    0x6170706c65636f726500 = "applecore" | Apple Core Island
    0x68656c746572736b656c74657200 = "helterskelter" | Helter Skelter
    0x63686572727900 = "cherry" | Take My Cherry
    0x636c65616e00 = "clean" | In Space, No-One Can Hear You Clean
    0x74696d6265727300 = "timbers" | Shiver Me Timbers
    0x46414c4c494e4700 = "FALLING" | Falling For You
    0x63726f70636972636c6500 = "cropcircle" | Crop Circle
    0x7472656576696c6c61676500 = "treevillage" | Tree Village Trouble
    0x6c616e64696e6700 = "landing" | Movie Mayhem
    0x6265616e7374616c6b00 = "beanstalk" | Worm and the Beanstalk
    0x5343484f4f4c5300 = "SCHOOLS" | School's in for Summer
    0x686967687374616b657300 = "highstakes" | High Stakes
    0x6e6f74706300 = "notpc" | A Quick Fix
    0x636f6f70656400 = "cooped" | All Cooped Up
    0x545249414c00 = "TRIAL" | Trial of the Damned
    0x53484f57444f574e00 = "SHOWDOWN" | Showdown at the OK Corale Reef
    0x706c6169636500 = "plaice" | Plaice Holder
    0x686f6f6b6c696e6500 = "hookline" | Hook, Line, and Skimmer
    0x66756e6661697200 = "funfair" | Nobody Rides For Free
    0x5065676173757300 = "Pegasus" | Hold Until Relieved
    0x626f6c646c7900 = "boldly" | To Boldly Go
    0x62616c6c6f6f6e00 = "balloon" | Beautiful Balloon
    0x636f756e74696e67736865657000 = "countingsheep" | A Good Nights Sleep
    0x425245414b4641535400 = "BREAKFAST" | Beefcake Breakfast Brawl
    0x686f6c6964617900 = "holiday" | Costa Del Danger
    0x7061636b00 = "pack" | Ragnarok and Roll
    0x414c49454e00 = "ALIEN" | Alien Juice Suckers
    0x54617267657448756e7400 = "TargetHunt" | Shotgun Challenge 1
    0x54617267657448756e743200 = "TargetHunt2" | Shotgun Challenge 2
    0x484f4d494e4700 = "HOMING" | Shotgun Challenge 3
    0x53686565703100 = "Sheep1" | Super Sheep Challenge 1
    0x53686565703200 = "Sheep2" | Super Sheep Challenge 2
    0x54617267657448756e743400 = "TargetHunt4" | Super Sheep Challenge 3
    0x637261746566756e00 = "cratefun" | Jet Pack Challenge 1
    0x6a65747061636b6368616c6c3200 = "jetpackchall2" | Jet Pack Challenge 2
    0x6a65747061636b6368616c6c3300 = "jetpackchall3" | Jet Pack Challenge 3
    0x43687574653100 = "Chute1" | Parachute Challenge 1
    0x63687574653200 = "chute2" | Parachute Challenge 2
    0x63687574653300 = "chute3" | Parachute Challenge 3
    0x44656174686d617463683100 = "Deathmatch1" | Deathmatch Challenge 1
    0x44656174686d617463683200 = "Deathmatch2" | Deathmatch Challenge 2
    0x44656174686d617463683300 = "Deathmatch3" | Deathmatch Challenge 3
    0x44656174686d617463683400 = "Deathmatch4" | Deathmatch Challenge 4
    0x44656174686d617463683500 = "Deathmatch5" | Deathmatch Challenge 5
    0x44656174686d617463683600 = "Deathmatch6" | Deathmatch Challenge 6
    0x44656174686d617463683700 = "Deathmatch7" | Deathmatch Challenge 7
    0x44656174686d617463683800 = "Deathmatch8" | Deathmatch Challenge 8
    0x44656174686d617463683900 = "Deathmatch9" | Deathmatch Challenge 9
    0x44656174686d61746368313000 = "Deathmatch10" | Deathmatch Challenge 10
    0x737464767300 = "stdvs" | Multiplayer Game
    0x6174747261637400 = "attract" | Attract Mode
    """

    EU_LUA_SCRIPT_INIT_POINTER = dword(0x1b55290)
    """
    [32-bit Pointer] (EU) LUA Script Init Pointer
    0x0 = Unloaded
    * = Loaded
    """

    US_LUA_SCRIPT_INIT_POINTER = dword(0x1bacf10)
    """
    [32-bit Pointer] (US) LUA Script Init Pointer
    0x0 = Unloaded
    * = Loaded
    """

    EU_HASHMAP_LSCHSTICKY = dword(0x1ce3704)
    """
    [32-bit Pointer] (EU) Hashmap | L.Sch.Sticky
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x14 = [32-bit] Unlock Type
    --- 0x0 = Voice
    --- 0x1 = Scheme
    --- 0x2 = Weapon
    --- 0x3 = Challenge
    --- 0x4 = Wormapedia
    --- 0x5 = Landscape
    +++0x18 = [32-bit Pointer ASCII] Unlock Text
    +++0x1c = [32-bit Boolean] Is Locked | Scheme: Sticky Wars
    """

    EU_HASHMAP_ELAPSEDROUNDTIME = dword(0x1ce37b4)
    """
    [32-bit Pointer] (EU) Hashmap | ElapsedRoundTime
    +0x4
    ++0x1c = [32-bit] Elapsed Round Time in milliseconds
    """

    EU_HASHMAP_LLFUNFAIR = dword(0x1ce3898)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.Funfair
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Nobody Rides For Free
    """

    EU_HASHMAP_LWNUKE = dword(0x1ce3c08)
    """
    [32-bit Pointer] (EU) Hashmap | L.W.Nuke
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Weapon: Nuclear Bomb
    """

    EU_HASHMAP_LSHORROR = dword(0x1ce3d28)
    """
    [32-bit Pointer] (EU) Hashmap | L.S.Horror
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Voice: Horror
    """

    EU_HASHMAP_LLHELTER = dword(0x1ce3d98)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.Helter
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Helter Skelter
    """

    EU_HASHMAP_LPHORROR = dword(0x1ce3e6c)
    """
    [32-bit Pointer] (EU) Hashmap | L.P.Horror
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: The Horror Theme
    """

    EU_HASHMAP_LLTREE = dword(0x1ce3e74)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.Tree
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Tree Village Trouble
    """

    EU_HASHMAP_ACTIVEWORMINDEX = dword(0x1ce3ef0)
    """
    [32-bit Pointer] (EU) Hashmap | ActiveWormIndex
    +0x4
    ++0x1c = [32-bit] Current Active Worm ID
    """

    EU_HASHMAP_LLLANDING = dword(0x1ce4004)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.Landing
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Movie Mayhem
    """

    EU_HASHMAP_GAMEOVERGAMETYPE = dword(0x1ce4094)
    """
    [32-bit Pointer] (EU) Hashmap | GameOver.GameType
    Initialized at game start contradictory to the key name.
    NOT reliable for missions/tutorial/challenges because it gets uninitialized when restarting a mission after failure.
    +0x4
    ++0x1c [32-bit Pointer] Game.Type
    +++0x0 [32-bit BE ASCII] Game Type String
    --- 0x5475746f = Tutorial
    --- 0x43616d70 = Campaign
    --- 0x4368616c = Challenge
    --- 0x51756963 = Quick
    --- 0x4d756c74 = Multiplayer
    """

    EU_HASHMAP_LLDDAY = dword(0x1ce40a4)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.DDay
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: D-Day
    """

    EU_HASHMAP_LLTUBES = dword(0x1ce40bc)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.Tubes
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Test Tubes
    """

    EU_HASHMAP_LCJP1 = dword(0x1ce4138)
    """
    [32-bit Pointer] (EU) Hashmap | L.C.JP1
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Jet Pack Challenge 1
    """

    EU_HASHMAP_LCJP2 = dword(0x1ce413c)
    """
    [32-bit Pointer] (EU) Hashmap | L.C.JP2
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Jet Pack Challenge 2
    """

    EU_HASHMAP_LCJP3 = dword(0x1ce4140)
    """
    [32-bit Pointer] (EU) Hashmap | L.C.JP3
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Jet Pack Challenge 3
    """

    EU_HASHMAP_CURRENTTEAMINDEX = dword(0x1ce4240)
    """
    [32-bit Pointer] (EU) Hashmap | CurrentTeamIndex
    +0x4
    ++0x1c = [32-bit] Index of the currently playing team
    """

    EU_HASHMAP_LLGRAVEYARD = dword(0x1ce4418)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.Graveyard
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Grave Danger
    """

    EU_HASHMAP_LSGRAMPS = dword(0x1ce451c)
    """
    [32-bit Pointer] (EU) Hashmap | L.S.Gramps
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Voice: Grandpa
    """

    EU_HASHMAP_LLCOOPED = dword(0x1ce4560)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.Cooped
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: All Cooped Up
    """

    EU_HASHMAP_LLCRATEBRITAIN = dword(0x1ce4658)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.CrateBritain
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Crate Britain
    """

    EU_HASHMAP_LSMAD = dword(0x1ce4680)
    """
    [32-bit Pointer] (EU) Hashmap | L.S.Mad
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Voice: Madchester
    """

    EU_HASHMAP_LLCHATEAU = dword(0x1ce46d4)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.Chateau
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Return to Chateau Assassin
    """

    EU_HASHMAP_LPBEATBOX = dword(0x1ce4710)
    """
    [32-bit Pointer] (EU) Hashmap | L.P.Beatbox
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: Spadge and Music
    """

    EU_HASHMAP_LPPROTO = dword(0x1ce473c)
    """
    [32-bit Pointer] (EU) Hashmap | L.P.Proto
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: Worms 3D Prototype
    """

    EU_HASHMAP_LLAPPLE = dword(0x1ce48b4)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.Apple
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Apple Core Island
    """

    EU_HASHMAP_LCSHOTGUN2 = dword(0x1ce48f8)
    """
    [32-bit Pointer] (EU) Hashmap | L.C.Shotgun2
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Shotgun Challenge 2
    """

    EU_HASHMAP_LCSHOTGUN3 = dword(0x1ce4900)
    """
    [32-bit Pointer] (EU) Hashmap | L.C.Shotgun3
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Shotgun Challenge 3
    """

    EU_HASHMAP_LPLOST = dword(0x1ce4c60)
    """
    [32-bit Pointer] (EU) Hashmap | L.P.Lost
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: The Lost Missions...
    """

    EU_HASHMAP_LLICE = dword(0x1ce4e14)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.Ice
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Ice, Ice, Maybe
    """

    EU_HASHMAP_LSCHSNIPING = dword(0x1ce4ebc)
    """
    [32-bit Pointer] (EU) Hashmap | L.Sch.Sniping
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Scheme: Sniper
    """

    EU_HASHMAP_LPGIRAFFE = dword(0x1ce4ef4)
    """
    [32-bit Pointer] (EU) Hashmap | L.P.Giraffe
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: That Angular Chap...
    """

    EU_HASHMAP_MCACURRENTMISSIONTYPE = dword(0x1ce4f14)
    """
    [32-bit Pointer] (EU) Hashmap | MCa.CurrentMissionType
    +0x4
    ++0x1c = [32-bit] Selected Mission Type
    -- 0x0 = Campaign
    -- 0x3 = Tutorial
    -- 0x4 = Challenge
    -- Cannot be used alone to distinguish actual missions and quick/multiplayer games
    """

    EU_HASHMAP_MCACURRENTMISSION = dword(0x1ce4f50)
    """
    [32-bit Pointer] (EU) Hashmap | MCa.CurrentMission
    +0x4
    ++0x1c = [32-bit] Selected Mission Index
    -- Current mission in order from the menu, starts at 0, relative to the game type (Tutorial, Mission, Challenge)
    -- Not reliable for Challenges as they can be unlocked in any order
    """

    EU_HASHMAP_TRIGGERCOLLECTOR = dword(0x1ce4fb8)
    """
    [32-bit Pointer] (EU) Hashmap | Trigger.Collector
    Used in various missions to detect triggers such as Tutorial1 secret and capture point index in Hold Until Relief
    +0x04
    ++0x1C = [32-bit] Trigger.Collector
    -- 0xffffffff = Untriggered
    """

    EU_HASHMAP_LWBRIDGEK = dword(0x1ce518c)
    """
    [32-bit Pointer] (EU) Hashmap | L.W.BridgeK
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Weapon: Bridge Kit
    """

    EU_HASHMAP_LPSALLY = dword(0x1ce52c4)
    """
    [32-bit Pointer] (EU) Hashmap | L.P.Sally
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: The Sally Army
    """

    EU_HASHMAP_LPFOOLS = dword(0x1ce545c)
    """
    [32-bit Pointer] (EU) Hashmap | L.P.Fools
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: Fakes and April Fools
    """

    EU_HASHMAP_LPTAPPER = dword(0x1ce5528)
    """
    [32-bit Pointer] (EU) Hashmap | L.P.Tapper
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: Enough in-jokes?
    """

    EU_HASHMAP_LWSSHEEP = dword(0x1ce55b0)
    """
    [32-bit Pointer] (EU) Hashmap | L.W.SSheep
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Weapon: Super Sheep
    """

    EU_HASHMAP_GAMENEXTLEVEL = dword(0x1ce55c0)
    """
    [32-bit Pointer] (EU) Hashmap | Game.NextLevel
    +0x4
    ++0x1c = [32-bit Pointer] Next Level ID
    +++0x0 = [9-bytes BE ASCII] Level ID String
    ---  0x46452e4c6576656c2e = "FE.Level."
    +++0x9 = [ASCII] Level ID Discriminator
    """

    EU_HASHMAP_LSLOVER = dword(0x1ce5858)
    """
    [32-bit Pointer] (EU) Hashmap | L.S.Lover
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Voice: French Lover
    """

    EU_HASHMAP_LPDARKSIDE = dword(0x1ce59d4)
    """
    [32-bit Pointer] (EU) Hashmap | L.P.Darkside
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: Darkside
    """

    EU_HASHMAP_LPPETE = dword(0x1ce5ad8)
    """
    [32-bit Pointer] (EU) Hashmap | L.P.Pete
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: Boggy Pete
    """

    EU_HASHMAP_LPCHATTER = dword(0x1ce5bcc)
    """
    [32-bit Pointer] (EU) Hashmap | L.P.Chatter
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: Chatter
    """

    EU_HASHMAP_LLALIEN = dword(0x1ce5cb8)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.Alien
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Alien Juice Suckers
    """

    EU_HASHMAP_CRATEINDEX = dword(0x1ce5d90)
    """
    [32-bit Pointer] (EU) Hashmap | Crate.Index
    +0x4
    ++0x1c = [32-bit] Crate Index used to spawn crates in missions
    """

    HASHMAP_GAMELOGICCURRENTSCRIPT = dword(0x1ce5da0)
    """
    [32-bit Pointer] Hashmap | GameLogic.CurrentScript
    +0x4
    ++0x1c = [32-bit Pointer] Current Script Name String
    """

    EU_HASHMAP_LPLANDD = dword(0x1ce5e80)
    """
    [32-bit Pointer] (EU) Hashmap | L.P.LandD
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: Lightside and Darkside
    """

    EU_HASHMAP_LAND_FILE = dword(0x1ce60e8)
    """
    [32-bit Pointer] (EU) Hashmap | Land File
    +0x4
    ++0x1c [32-bit Pointer] Currently loaded XOM map filename
    """

    EU_HASHMAP_LSCHPRO = dword(0x1ce61bc)
    """
    [32-bit Pointer] (EU) Hashmap | L.Sch.Pro
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Scheme: Pro
    """

    EU_HASHMAP_LLHIGH = dword(0x1ce6370)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.High
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: High Stakes
    """

    EU_HASHMAP_LCSS1 = dword(0x1ce63f4)
    """
    [32-bit Pointer] (EU) Hashmap | L.C.SS1
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Super Sheep Challenge 1
    """

    EU_HASHMAP_LCSS2 = dword(0x1ce63f8)
    """
    [32-bit Pointer] (EU) Hashmap | L.C.SS2
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Super Sheep Challenge 2
    """

    EU_HASHMAP_LCSS3 = dword(0x1ce63fc)
    """
    [32-bit Pointer] (EU) Hashmap | L.C.SS3
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Super Sheep Challenge 3
    """

    EU_HASHMAP_LLTIMBERS = dword(0x1ce643c)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.Timbers
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Shiver Me Timbers
    """

    EU_HASHMAP_LWMADCOW = dword(0x1ce656c)
    """
    [32-bit Pointer] (EU) Hashmap | L.W.MadCow
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Weapon: Mad Cow
    """

    EU_HASHMAP_LSCHALL = dword(0x1ce6660)
    """
    [32-bit Pointer] (EU) Hashmap | L.Sch.All
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Scheme: All Action
    """

    EU_HASHMAP_LLLEEK = dword(0x1ce6740)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.Leek
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: A Leek in a Vegetable Patch
    """

    EU_HASHMAP_LLRAGNA = dword(0x1ce6794)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.Ragna
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Ragnarok and Roll
    """

    EU_HASHMAP_FCSGAMEOVER = dword(0x1ce67c8)
    """
    [32-bit Pointer] (EU) Hashmap | FCS.GameOver
    +0x4
    ++0x1c = [32-bit Boolean] Game Over
    """

    EU_HASHMAP_LLHOLIDAY = dword(0x1ce6854)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.Holiday
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Costa Del Danger
    """

    EU_HASHMAP_LLCRATEFUN = dword(0x1ce6a08)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.Cratefun
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Jet Pack Challenge 1
    """

    EU_HASHMAP_LPPINBALL = dword(0x1ce6a10)
    """
    [32-bit Pointer] (EU) Hashmap | L.P.Pinball
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: Addiction 2?
    """

    EU_HASHMAP_LSCHWBNG = dword(0x1ce6a1c)
    """
    [32-bit Pointer] (EU) Hashmap | L.Sch.WBnG
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Scheme: Sinking BnG
    """

    EU_HASHMAP_LCDM1 = dword(0x1ce6ba4)
    """
    [32-bit Pointer] (EU) Hashmap | L.C.DM1
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Deathmatch Challenge 1
    """

    EU_HASHMAP_LCDM2 = dword(0x1ce6ba8)
    """
    [32-bit Pointer] (EU) Hashmap | L.C.DM2
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Deathmatch Challenge 2
    """

    EU_HASHMAP_LCDM3 = dword(0x1ce6bac)
    """
    [32-bit Pointer] (EU) Hashmap | L.C.DM3
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Deathmatch Challenge 3
    """

    EU_HASHMAP_LCDM4 = dword(0x1ce6bb0)
    """
    [32-bit Pointer] (EU) Hashmap | L.C.DM4
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Deathmatch Challenge 4
    """

    EU_HASHMAP_LCDM5 = dword(0x1ce6bb4)
    """
    [32-bit Pointer] (EU) Hashmap | L.C.DM5
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Deathmatch Challenge 5
    """

    EU_HASHMAP_LCDM6 = dword(0x1ce6bb8)
    """
    [32-bit Pointer] (EU) Hashmap | L.C.DM6
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Deathmatch Challenge 6
    """

    EU_HASHMAP_LCDM7 = dword(0x1ce6bbc)
    """
    [32-bit Pointer] (EU) Hashmap | L.C.DM7
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Deathmatch Challenge 7
    """

    EU_HASHMAP_LCDM8 = dword(0x1ce6bc4)
    """
    [32-bit Pointer] (EU) Hashmap | L.C.DM8
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Deathmatch Challenge 8
    """

    EU_HASHMAP_LCDM9 = dword(0x1ce6bc8)
    """
    [32-bit Pointer] (EU) Hashmap | L.C.DM9
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Deathmatch Challenge 9
    """

    EU_HASHMAP_MCABESTGOLD = dword(0x1ce6bf0)
    """
    [32-bit Pointer] (EU) Hashmap | MCa.BestGold
    +0x4
    ++0x1c = [32-bit] Gold time record in milliseconds of selected challenge
    """

    EU_HASHMAP_LPPINK = dword(0x1ce6c6c)
    """
    [32-bit Pointer] (EU) Hashmap | L.P.Pink
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: Pink Beard
    """

    EU_HASHMAP_LLSHOWDOWN = dword(0x1ce6ca8)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.Showdown
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Showdown at the OK Corale Reef
    """

    EU_HASHMAP_MCALASTGAMETIME = dword(0x1ce6de8)
    """
    [32-bit Pointer] (EU) Hashmap | MCa.LastGameTime
    +0x4
    ++0x1c = [32-bit] Received medal or challenge time
    -- In Campaign:
    -- 0x0 = None
    -- 0x1 = Bronze
    -- 0x2 = Silver
    -- 0x3 = Gold
    -- In Challenge: Time measured in milliseconds
    """

    EU_HASHMAP_LCDM10 = dword(0x1ce6e10)
    """
    [32-bit Pointer] (EU) Hashmap | L.C.DM10
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Deathmatch Challenge 10
    """

    EU_HASHMAP_LPBRIGHT = dword(0x1ce6e20)
    """
    [32-bit Pointer] (EU) Hashmap | L.P.Bright
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: Brightside
    """

    EU_HASHMAP_LLATLANTIS = dword(0x1ce6e4c)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.Atlantis
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Atlantis Training Facility
    """

    EU_HASHMAP_LSVILLAIN = dword(0x1ce6eb8)
    """
    [32-bit Pointer] (EU) Hashmap | L.S.Villain
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Voice: Super Villain
    """

    EU_HASHMAP_LPLIGHTSIDE = dword(0x1ce6fe8)
    """
    [32-bit Pointer] (EU) Hashmap | L.P.Lightside
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: Lightside
    """

    EU_HASHMAP_LPDONKEY = dword(0x1ce7014)
    """
    [32-bit Pointer] (EU) Hashmap | L.P.Donkey
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: Concrete Donkey
    """

    EU_HASHMAP_LPSTORY = dword(0x1ce7198)
    """
    [32-bit Pointer] (EU) Hashmap | L.P.Story
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: The Worms Story
    """

    EU_HASHMAP_LLPLAICE = dword(0x1ce7248)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.Plaice
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Plaice Holder
    """

    EU_HASHMAP_LLCRUST = dword(0x1ce7260)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.Crust
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Earn Your Crust
    """

    EU_HASHMAP_LLCOLLIDE = dword(0x1ce7324)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.Collide
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: When Annelids Collide
    """

    EU_HASHMAP_LCP1 = dword(0x1ce7504)
    """
    [32-bit Pointer] (EU) Hashmap | L.C.P1
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Parachute Challenge 1
    """

    EU_HASHMAP_LCP2 = dword(0x1ce7508)
    """
    [32-bit Pointer] (EU) Hashmap | L.C.P2
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Parachute Challenge 2
    """

    EU_HASHMAP_LCP3 = dword(0x1ce750c)
    """
    [32-bit Pointer] (EU) Hashmap | L.C.P3
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Parachute Challenge 3
    """

    EU_HASHMAP_LWEQUAKE = dword(0x1ce7694)
    """
    [32-bit Pointer] (EU) Hashmap | L.W.EQuake
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Weapon: Earthquake
    """

    EU_HASHMAP_LLCOUNTING = dword(0x1ce77fc)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.Counting
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: A Good Nights Sleep
    """

    EU_HASHMAP_LLKONG = dword(0x1ce781c)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.Kong
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: The Mighty Kong
    """

    EU_HASHMAP_DATATEAMBARRACKS = dword(0x1ce7820)
    """
    [32-bit Pointer] (EU) Hashmap | DATA.TeamBarracks
    +0x4
    ++0x1c = [32-bit Pointer] TeamDataColective
    +++0x14 = [32-bit Pointer] XomContainerArray | High Scores
    ++++0x40 = [32-bit Pointer] HighScoreData | Shotgun Challenge 1
    +++++0x14 = [32-bit] Bronze Time in milliseconds
    +++++0x18 = [32-bit Pointer] Bronze Player Name
    +++++0x1c = [32-bit] Silver Time in milliseconds
    +++++0x20 = [32-bit Pointer] Silver Player Name
    +++++0x24 = [32-bit] Gold Time in milliseconds
    +++++0x28 = [32-bit Pointer] Gold Player Name
    ++++0x44 = [32-bit Pointer] HighScoreData | Shotgun Challenge 2
    ++++0x48 = [32-bit Pointer] HighScoreData | Shotgun Challenge 3
    ++++0x4c = [32-bit Pointer] HighScoreData | Super Sheep Challenge 1
    ++++0x50 = [32-bit Pointer] HighScoreData | Super Sheep Challenge 2
    ++++0x54 = [32-bit Pointer] HighScoreData | Super Sheep Challenge 3
    ++++0x58 = [32-bit Pointer] HighScoreData | Jet Pack Challenge 1
    ++++0x5c = [32-bit Pointer] HighScoreData | Jet Pack Challenge 2
    ++++0x60 = [32-bit Pointer] HighScoreData | Jet Pack Challenge 3
    ++++0x64 = [32-bit Pointer] HighScoreData | Parachute Challenge 1
    ++++0x68 = [32-bit Pointer] HighScoreData | Parachute Challenge 2
    ++++0x6c = [32-bit Pointer] HighScoreData | Parachute Challenge 3
    ++++0x70 = [32-bit Pointer] HighScoreData | Deathmatch Challenge 1
    ++++0x74 = [32-bit Pointer] HighScoreData | Deathmatch Challenge 2
    ++++0x78 = [32-bit Pointer] HighScoreData | Deathmatch Challenge 3
    ++++0x7c = [32-bit Pointer] HighScoreData | Deathmatch Challenge 4
    ++++0x80 = [32-bit Pointer] HighScoreData | Deathmatch Challenge 5
    ++++0x84 = [32-bit Pointer] HighScoreData | Deathmatch Challenge 6
    ++++0x88 = [32-bit Pointer] HighScoreData | Deathmatch Challenge 7
    ++++0x8c = [32-bit Pointer] HighScoreData | Deathmatch Challenge 8
    ++++0x90 = [32-bit Pointer] HighScoreData | Deathmatch Challenge 9
    ++++0x94 = [32-bit Pointer] HighScoreData | Deathmatch Challenge 10

    +++0x18 = [32-bit Pointer] XomContainerArray | Teams Array
    ++++0x40 = [32-bit Pointer] StoredTeamData | Team 1
    +++++0x14 = [32-bit Pointer] Player ID (String)
    +++++0x18 = [32-bit Pointer] Speech ID (String)
    +++++0x1c = [32-bit Pointer] Flag ID (String)
    +++++0x20 = [32-bit] Special Weapon ID
    +++++0x24 = [32-bit] Grave ID
    +++++0x28 = [32-bit] Skill ID
    +++++0x2c = [32-bit] New Team?
    +++++0x30 = [32-bit] Tutorial Progression
    ----- 0x0 = None
    ----- 0x1 = Completed Atlantis Training Facility
    ----- 0x2 = Completed Down in the Dumps
    ----- 0x3 = Completed Return to Chateau Assassin
    ----- 0x4 = Completed The Mighty Kong
    ----- 0x5 = Completed Test Tubes
    ----- 0x6 = Completed The Driving Range (Not possible)
    +++++0x34 = [32-bit Pointer] XomContainerArray | Campaign Array
    ++++++0x40 = [32-bit Pointer] CampaignData | D-Day
    +++++++0x14 = [32-bit] Retries
    +++++++0x18 = [32-bit] Medal
    ------- 0x0 = None
    ------- 0x1 = Bronze
    ------- 0x2 = Silver
    ------- 0x3 = Gold
    ++++++0x44 = [32-bit Pointer] CampaignData | Crate Britain
    ++++++0x48 = [32-bit Pointer] CampaignData | Grave Danger
    ++++++0x4c = [32-bit Pointer] CampaignData | A Leek in a Vegetable Patch
    ++++++0x50 = [32-bit Pointer] CampaignData | Ice, Ice, Maybe
    ++++++0x54 = [32-bit Pointer] CampaignData | When Annelids Collide
    ++++++0x58 = [32-bit Pointer] CampaignData | Rum Deal
    ++++++0x5c = [32-bit Pointer] CampaignData | Earn Your Crust
    ++++++0x60 = [32-bit Pointer] CampaignData | Apple Core Island
    ++++++0x64 = [32-bit Pointer] CampaignData | Helter Skelter
    ++++++0x68 = [32-bit Pointer] CampaignData | Take My Cherry
    ++++++0x6c = [32-bit Pointer] CampaignData | In Space, No-One Can Hear You Clean
    ++++++0x70 = [32-bit Pointer] CampaignData | Shiver Me Timbers
    ++++++0x74 = [32-bit Pointer] CampaignData | Falling For You
    ++++++0x78 = [32-bit Pointer] CampaignData | Crop Circle
    ++++++0x7c = [32-bit Pointer] CampaignData | Tree Village Trouble
    ++++++0x80 = [32-bit Pointer] CampaignData | Movie Mayhem
    ++++++0x84 = [32-bit Pointer] CampaignData | Worm and the Beanstalk
    ++++++0x88 = [32-bit Pointer] CampaignData | School's in for Summer
    ++++++0x8c = [32-bit Pointer] CampaignData | High Stakes
    ++++++0x90 = [32-bit Pointer] CampaignData | A Quick Fix
    ++++++0x94 = [32-bit Pointer] CampaignData | All Cooped Up
    ++++++0x98 = [32-bit Pointer] CampaignData | Trial of the Damned
    ++++++0x9c = [32-bit Pointer] CampaignData | Showdown at the OK Corale Reef
    ++++++0xa0 = [32-bit Pointer] CampaignData | Plaice Holder
    ++++++0xa4 = [32-bit Pointer] CampaignData | Hook, Line, and Skimmer
    ++++++0xa8 = [32-bit Pointer] CampaignData | Nobody Rides For Free
    ++++++0xac = [32-bit Pointer] CampaignData | Hold Until Relieved
    ++++++0xb0 = [32-bit Pointer] CampaignData | To Boldly Go
    ++++++0xb4 = [32-bit Pointer] CampaignData | Beautiful Balloon
    ++++++0xb8 = [32-bit Pointer] CampaignData | A Good Nights Sleep
    ++++++0xbc = [32-bit Pointer] CampaignData | Beefcake Breakfast Brawl
    ++++++0xc0 = [32-bit Pointer] CampaignData | Costa Del Danger
    ++++++0xc4 = [32-bit Pointer] CampaignData | Ragnarok and Roll
    ++++++0xc8 = [32-bit Pointer] CampaignData | Alien Juice Suckers
    +++++0x38 = [32-bit Pointer] Worms Array
    +++++0x3c = [32-bit Pointer] Team Name
    +++++0x40 = [32-bit Boolean] Profile Selected

    ++++0x44 = [32-bit Pointer] StoredTeamData | Team 2
    ++++0x48 = [32-bit Pointer] StoredTeamData | Team 3
    ++++0x4c = [32-bit Pointer] StoredTeamData | Team 4
    ++++0x50 = [32-bit Pointer] StoredTeamData | Team 5
    ++++0x54 = [32-bit Pointer] StoredTeamData | Team 6
    ++++0x58 = [32-bit Pointer] StoredTeamData | Team 7
    ++++0x5c = [32-bit Pointer] StoredTeamData | Team 8
    ++++0x60 = [32-bit Pointer] StoredTeamData | Team 9
    ++++0x64 = [32-bit Pointer] StoredTeamData | Team 10
    ++++0x68 = [32-bit Pointer] StoredTeamData | Team 11
    ++++0x6c = [32-bit Pointer] StoredTeamData | Team 12
    ++++0x70 = [32-bit Pointer] StoredTeamData | Team 13
    ++++0x74 = [32-bit Pointer] StoredTeamData | Team 14
    ++++0x78 = [32-bit Pointer] StoredTeamData | Team 15
    ++++0x7c = [32-bit Pointer] StoredTeamData | Team 16
    ++++0x80 = [32-bit Pointer] StoredTeamData | Team 17
    ++++0x84 = [32-bit Pointer] StoredTeamData | Team 18
    ++++0x88 = [32-bit Pointer] StoredTeamData | Team 19
    ++++0x8c = [32-bit Pointer] StoredTeamData | Team 20
    """

    EU_HASHMAP_LLSCHOOLS = dword(0x1ce787c)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.Schools
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: School's in for Summer
    """

    EU_HASHMAP_LWBANANA = dword(0x1ce7954)
    """
    [32-bit Pointer] (EU) Hashmap | L.W.Banana
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Weapon: Banana Bomb
    """

    EU_HASHMAP_LLCROP = dword(0x1ce79d0)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.Crop
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Crop Circle
    """

    EU_HASHMAP_LLCHERRY = dword(0x1ce79f4)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.Cherry
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Take My Cherry
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

    US_HASHMAP_LLGRAVEYARD = dword(0x1cfb808)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Graveyard
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Grave Danger
    """

    LANDSCAPE_SELECTION_INDESTRUCTABLE_TERRAIN = dword(0x1cfb8dc)
    """
    [32 Bit Pointer] Landscape Selection | Indestructable Terrain
    +0x04
    ++0x1C = [32 Bit] Indestructable Terrain
    --- 00 = Inactive
    --- 01 = Active
    """

    US_HASHMAP_LPTAPPER = dword(0x1cfb978)
    """
    [32-bit Pointer] (US) Hashmap | L.P.Tapper
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: Enough in-jokes?
    """

    US_HASHMAP_CRATEINDEX = dword(0x1cfba10)
    """
    [32-bit Pointer] (US) Hashmap | Crate.Index
    +0x4
    ++0x1c = [32-bit] Crate Index used to spawn crates in missions
    """

    US_HASHMAP_LLCHERRY = dword(0x1cfba54)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Cherry
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Take My Cherry
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

    US_HASHMAP_LSMAD = dword(0x1cfbc00)
    """
    [32-bit Pointer] (US) Hashmap | L.S.Mad
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Voice: Madchester
    """

    US_HASHMAP_LLTUBES = dword(0x1cfbc80)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Tubes
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Test Tubes
    """

    POINTER_TO_MUSIC = dword(0x1cfbd7c)
    """
    [32-bit] Pointer to Music
    +0x04 
    ++0x1c | Music Volume [Float]
    """

    US_HASHMAP_LLALIEN = dword(0x1cfbde8)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Alien
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Alien Juice Suckers
    """

    US_HASHMAP_LWEQUAKE = dword(0x1cfbec4)
    """
    [32-bit Pointer] (US) Hashmap | L.W.EQuake
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Weapon: Earthquake
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

    US_HASHMAP_CURRENTTEAMINDEX = dword(0x1cfbf90)
    """
    [32-bit Pointer] (US) Hashmap | CurrentTeamIndex
    +0x4
    ++0x1c = [32-bit] Index of the currently playing team
    """

    US_HASHMAP_LLKONG = dword(0x1cfc04c)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Kong
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: The Mighty Kong
    """

    US_HASHMAP_LLCROP = dword(0x1cfc070)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Crop
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Crop Circle
    """

    US_HASHMAP_LPPETE = dword(0x1cfc248)
    """
    [32-bit Pointer] (US) Hashmap | L.P.Pete
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: Boggy Pete
    """

    US_HASHMAP_FCSGAMEOVER = dword(0x1cfc2b8)
    """
    [32-bit Pointer] (US) Hashmap | FCS.GameOver
    +0x4
    ++0x1c = [32-bit Boolean] Game Over
    """

    US_HASHMAP_LCJP1 = dword(0x1cfc334)
    """
    [32-bit Pointer] (US) Hashmap | L.C.JP1
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Jet Pack Challenge 1
    """

    US_HASHMAP_LCJP2 = dword(0x1cfc338)
    """
    [32-bit Pointer] (US) Hashmap | L.C.JP2
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Jet Pack Challenge 2
    """

    US_HASHMAP_LCJP3 = dword(0x1cfc34c)
    """
    [32-bit Pointer] (US) Hashmap | L.C.JP3
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Jet Pack Challenge 3
    """

    US_HASHMAP_LLLANDING = dword(0x1cfc38c)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Landing
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Movie Mayhem
    """

    US_HASHMAP_LLCRATEBRITAIN = dword(0x1cfc3a8)
    """
    [32-bit Pointer] (US) Hashmap | L.L.CrateBritain
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Crate Britain
    """

    US_HASHMAP_ACTIVEWORMINDEX = dword(0x1cfc410)
    """
    [32-bit Pointer] (US) Hashmap | ActiveWormIndex
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

    P1_WORM_DATA_1 = dword(0x1cfc434)
    """
    [32 Bit Pointer] P1 Worm Data [2]
    """

    P1_WORM_DATA_2 = dword(0x1cfc438)
    """
    [32 Bit Pointer] P1 Worm Data [3]
    """

    P1_WORM_DATA_3 = dword(0x1cfc43c)
    """
    [32 Bit Pointer] P1 Worm Data [4]
    """

    P1_WORM_DATA_4 = dword(0x1cfc440)
    """
    [32 Bit Pointer] P1 Worm Data [5]
    """

    P1_WORM_DATA_5 = dword(0x1cfc444)
    """
    [32 Bit Pointer] P1 Worm Data [6]
    """

    ROUND_TIMER = dword(0x1cfc458)
    """
    [32 Bit Pointer] Round Timer
    +0x04
    ++0x1C = [32 Bit] Round Timer
    """

    US_HASHMAP_LWNUKE = dword(0x1cfc460)
    """
    [32-bit Pointer] (US) Hashmap | L.W.Nuke
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Weapon: Nuclear Bomb
    """

    GAME_OPTION_ROUND_TIME_DISPLAY = dword(0x1cfc708)
    """
    [32 Bit Pointer] Game Option | Round Time Display
    +0x04
    ++0x1C = [32 Bit] Game Option Check
    --- 00 = Inactive
    --- 01 = Active
    """

    US_HASHMAP_LCDM10 = dword(0x1cfc770)
    """
    [32-bit Pointer] (US) Hashmap | L.C.DM10
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Deathmatch Challenge 10
    """

    US_HASHMAP_LPBEATBOX = dword(0x1cfc910)
    """
    [32-bit Pointer] (US) Hashmap | L.P.Beatbox
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: Spadge and Music
    """

    US_HASHMAP_LLCOOPED = dword(0x1cfca80)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Cooped
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: All Cooped Up
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

    US_HASHMAP_LLTIMBERS = dword(0x1cfcd3c)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Timbers
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Shiver Me Timbers
    """

    US_HASHMAP_LPPINBALL = dword(0x1cfce60)
    """
    [32-bit Pointer] (US) Hashmap | L.P.Pinball
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: Addiction 2?
    """

    US_HASHMAP_LLSHOWDOWN = dword(0x1cfcf68)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Showdown
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Showdown at the OK Corale Reef
    """

    US_HASHMAP_MCACURRENTMISSION = dword(0x1cfcfa8)
    """
    [32-bit Pointer] (US) Hashmap | MCa.CurrentMission
    +0x4
    ++0x1c = [32-bit] Selected Mission Index
    -- Current mission in order from the menu, starts at 0, relative to the game type (Tutorial, Mission, Challenge)
    -- Not reliable for Challenges as they can be unlocked in any order
    """

    US_HASHMAP_LSVILLAIN = dword(0x1cfcfe8)
    """
    [32-bit Pointer] (US) Hashmap | L.S.Villain
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Voice: Super Villain
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

    US_HASHMAP_LSCHSNIPING = dword(0x1cfd250)
    """
    [32-bit Pointer] (US) Hashmap | L.Sch.Sniping
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Scheme: Sniper
    """

    GAME_OPTION_HEALTH_CRATE_CHANCE = dword(0x1cfd2c4)
    """
    [32 Bit Pointer] Game Option | Health Crate Chance
    +0x04
    ++0x1C = [32 Bit] Health Crate Chance
    """

    US_HASHMAP_LSHORROR = dword(0x1cfd378)
    """
    [32-bit Pointer] (US) Hashmap | L.S.Horror
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Voice: Horror
    """

    US_HASHMAP_LPPINK = dword(0x1cfd3dc)
    """
    [32-bit Pointer] (US) Hashmap | L.P.Pink
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: Pink Beard
    """

    US_HASHMAP_LPHORROR = dword(0x1cfd4b8)
    """
    [32-bit Pointer] (US) Hashmap | L.P.Horror
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: The Horror Theme
    """

    US_HASHMAP_LSCHALL = dword(0x1cfd5a0)
    """
    [32-bit Pointer] (US) Hashmap | L.Sch.All
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Scheme: All Action
    """

    US_HASHMAP_LPLIGHTSIDE = dword(0x1cfd5c4)
    """
    [32-bit Pointer] (US) Hashmap | L.P.Lightside
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: Lightside
    """

    US_HASHMAP_LCP1 = dword(0x1cfd634)
    """
    [32-bit Pointer] (US) Hashmap | L.C.P1
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Parachute Challenge 1
    """

    US_HASHMAP_LCP2 = dword(0x1cfd638)
    """
    [32-bit Pointer] (US) Hashmap | L.C.P2
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Parachute Challenge 2
    """

    US_HASHMAP_LCP3 = dword(0x1cfd63c)
    """
    [32-bit Pointer] (US) Hashmap | L.C.P3
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Parachute Challenge 3
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

    US_HASHMAP_MCABESTGOLD = dword(0x1cfd688)
    """
    [32-bit Pointer] (US) Hashmap | MCa.BestGold
    +0x4
    ++0x1c = [32-bit] Gold time record in milliseconds of selected challenge
    """

    US_HASHMAP_LCSHOTGUN2 = dword(0x1cfd778)
    """
    [32-bit Pointer] (US) Hashmap | L.C.Shotgun2
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Shotgun Challenge 2
    """

    US_HASHMAP_LCSHOTGUN3 = dword(0x1cfd77c)
    """
    [32-bit Pointer] (US) Hashmap | L.C.Shotgun3
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Shotgun Challenge 3
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

    US_HASHMAP_LLHELTER = dword(0x1cfdbb8)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Helter
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Helter Skelter
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

    US_HASHMAP_LLAPPLE = dword(0x1cfdf04)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Apple
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Apple Core Island
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

    US_HASHMAP_LLICE = dword(0x1cfe14c)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Ice
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Ice, Ice, Maybe
    """

    US_HASHMAP_LWBRIDGEK = dword(0x1cfe19c)
    """
    [32-bit Pointer] (US) Hashmap | L.W.BridgeK
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Weapon: Bridge Kit
    """

    GAME_OPTION_FALL_DAMAGE = dword(0x1cfe1a0)
    """
    [32 Bit Pointer] Game Option | Fall Damage
    +0x04
    ++0x1C = [32 Bit] Game Option Check
    --- 00 = Inactive
    --- 01 = Active
    """

    US_HASHMAP_LLCOLLIDE = dword(0x1cfe584)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Collide
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: When Annelids Collide
    """

    US_HASHMAP_LCSS1 = dword(0x1cfe5f4)
    """
    [32-bit Pointer] (US) Hashmap | L.C.SS1
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Super Sheep Challenge 1
    """

    US_HASHMAP_LCSS2 = dword(0x1cfe5f8)
    """
    [32-bit Pointer] (US) Hashmap | L.C.SS2
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Super Sheep Challenge 2
    """

    US_HASHMAP_LCSS3 = dword(0x1cfe5fc)
    """
    [32-bit Pointer] (US) Hashmap | L.C.SS3
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Super Sheep Challenge 3
    """

    US_HASHMAP_LLSCHOOLS = dword(0x1cfe7bc)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Schools
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: School's in for Summer
    """

    US_HASHMAP_LLPLAICE = dword(0x1cfe7c8)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Plaice
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Plaice Holder
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

    US_HASHMAP_LLCRATEFUN = dword(0x1cfe8f0)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Cratefun
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Jet Pack Challenge 1
    """

    US_HASHMAP_LPSALLY = dword(0x1cfe914)
    """
    [32-bit Pointer] (US) Hashmap | L.P.Sally
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: The Sally Army
    """

    GAME_OPTION_PLACEMENT = dword(0x1cfeaa8)
    """
    [32 Bit Pointer] Game Option | Placement
    +0x04
    ++0x1C = [32 Bit] Game Option Check
    --- 00 = Random
    --- 01 = Manual
    """

    US_HASHMAP_LLCHATEAU = dword(0x1cfecc4)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Chateau
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Return to Chateau Assassin
    """

    US_HASHMAP_ELAPSEDROUNDTIME = dword(0x1cfed48)
    """
    [32-bit Pointer] (US) Hashmap | ElapsedRoundTime
    +0x4
    ++0x1c = [32-bit] Elapsed Round Time in milliseconds
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

    US_HASHMAP_MCALASTGAMETIME = dword(0x1cfee50)
    """
    [32-bit Pointer] (US) Hashmap | MCa.LastGameTime
    +0x4
    ++0x1c = [32-bit] Received medal or challenge time
    -- In Campaign:
    -- 0x0 = None
    -- 0x1 = Bronze
    -- 0x2 = Silver
    -- 0x3 = Gold
    -- In Challenge: Time measured in milliseconds
    """

    US_HASHMAP_LSGRAMPS = dword(0x1cfefc0)
    """
    [32-bit Pointer] (US) Hashmap | L.S.Gramps
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Voice: Grandpa
    """

    US_HASHMAP_LLLEEK = dword(0x1cff29c)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Leek
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: A Leek in a Vegetable Patch
    """

    US_HASHMAP_LPPROTO = dword(0x1cff36c)
    """
    [32-bit Pointer] (US) Hashmap | L.P.Proto
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: Worms 3D Prototype
    """

    US_HASHMAP_LLTREE = dword(0x1cff404)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Tree
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Tree Village Trouble
    """

    US_HASHMAP_MCACURRENTMISSIONTYPE = dword(0x1cff508)
    """
    [32-bit Pointer] (US) Hashmap | MCa.CurrentMissionType
    +0x4
    ++0x1c = [32-bit] Selected Mission Type
    -- 0x0 = Campaign
    -- 0x3 = Tutorial
    -- 0x4 = Challenge
    -- Cannot be used to distinguish actual missions and quick/multiplayer games
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

    US_HASHMAP_LLHOLIDAY = dword(0x1cff6d4)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Holiday
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Costa Del Danger
    """

    GAME_OPTION_UTILITY_CRATE_CHANCE = dword(0x1cff744)
    """
    [32 Bit Pointer] Game Option | Utility Crate Chance
    +0x04
    ++0x1C = [32 Bit] Utility Crate Chance
    """

    GAME_OPTION_UTILITY_CRATE_CHANCE_1 = dword(0x1cff74c)
    """
    [32 Bit Pointer] Game Option | Utility Crate Chance
    +0x04
    ++0x1C = [32 Bit] Landscape Seed
    """

    US_HASHMAP_LSCHSTICKY = dword(0x1cff914)
    """
    [32-bit Pointer] (US) Hashmap | L.Sch.Sticky
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Scheme: Sticky Wars
    """

    US_HASHMAP_LLATLANTIS = dword(0x1cffb40)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Atlantis
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Atlantis Training Facility
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

    US_HASHMAP_LLHIGH = dword(0x1cffb50)
    """
    [32-bit Pointer] (US) Hashmap | L.L.High
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: High Stakes
    """

    US_HASHMAP_LLCOUNTING = dword(0x1cffb8c)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Counting
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: A Good Nights Sleep
    """

    US_HASHMAP_LWSSHEEP = dword(0x1cffd30)
    """
    [32-bit Pointer] (US) Hashmap | L.W.SSheep
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Weapon: Super Sheep
    """

    US_HASHMAP_LPGIRAFFE = dword(0x1cffe44)
    """
    [32-bit Pointer] (US) Hashmap | L.P.Giraffe
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: That Angular Chap...
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

    US_HASHMAP_GAMEOVERGAMETYPE = dword(0x1cfff84)
    """
    [32-bit Pointer] (US) Hashmap | GameOver.GameType
    Initialized at game start contradictory to the key name.
    NOT reliable for missions/tutorial/challenges because it gets uninitialized when restarting a mission after failure.
    +0x4
    ++0x1c [32-bit Pointer] Game.Type
    +++0x0 [32-bit BE ASCII] Game Type String
    --- 0x5475746f = Tutorial
    --- 0x43616d70 = Campaign
    --- 0x4368616c = Challenge
    --- 0x51756963 = Quick
    --- 0x4d756c74 = Multiplayer
    """

    US_HASHMAP_LLDDAY = dword(0x1cfff94)
    """
    [32-bit Pointer] (US) Hashmap | L.L.DDay
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: D-Day
    """

    POINTER_TO_SFX = dword(0x1cfffd0)
    """
    [32-bit] Pointer to SFX
    +0x04 
    ++0x1c | SFX Volume [Float]
    """

    US_HASHMAP_LPSTORY = dword(0x1d00014)
    """
    [32-bit Pointer] (US) Hashmap | L.P.Story
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: The Worms Story
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

    US_HASHMAP_LPCHATTER = dword(0x1d001c4)
    """
    [32-bit Pointer] (US) Hashmap | L.P.Chatter
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: Chatter
    """

    US_HASHMAP_LSLOVER = dword(0x1d002f8)
    """
    [32-bit Pointer] (US) Hashmap | L.S.Lover
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Voice: French Lover
    """

    US_HASHMAP_LPLOST = dword(0x1d00380)
    """
    [32-bit Pointer] (US) Hashmap | L.P.Lost
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: The Lost Missions...
    """

    US_HASHMAP_LLCRUST = dword(0x1d00400)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Crust
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Earn Your Crust
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

    US_HASHMAP_LPDARKSIDE = dword(0x1d00608)
    """
    [32-bit Pointer] (US) Hashmap | L.P.Darkside
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: Darkside
    """

    US_HASHMAP_LCDM1 = dword(0x1d00834)
    """
    [32-bit Pointer] (US) Hashmap | L.C.DM1
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Deathmatch Challenge 1
    """

    US_HASHMAP_LCDM2 = dword(0x1d00838)
    """
    [32-bit Pointer] (US) Hashmap | L.C.DM2
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Deathmatch Challenge 2
    """

    US_HASHMAP_LCDM3 = dword(0x1d0083c)
    """
    [32-bit Pointer] (US) Hashmap | L.C.DM3
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Deathmatch Challenge 3
    """

    US_HASHMAP_LCDM4 = dword(0x1d00840)
    """
    [32-bit Pointer] (US) Hashmap | L.C.DM4
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Deathmatch Challenge 4
    """

    US_HASHMAP_LCDM5 = dword(0x1d0084c)
    """
    [32-bit Pointer] (US) Hashmap | L.C.DM5
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Deathmatch Challenge 5
    """

    US_HASHMAP_LCDM6 = dword(0x1d00850)
    """
    [32-bit Pointer] (US) Hashmap | L.C.DM6
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Deathmatch Challenge 6
    """

    US_HASHMAP_LCDM7 = dword(0x1d00854)
    """
    [32-bit Pointer] (US) Hashmap | L.C.DM7
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Deathmatch Challenge 7
    """

    US_HASHMAP_LCDM8 = dword(0x1d00858)
    """
    [32-bit Pointer] (US) Hashmap | L.C.DM8
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Deathmatch Challenge 8
    """

    US_HASHMAP_LCDM9 = dword(0x1d0085c)
    """
    [32-bit Pointer] (US) Hashmap | L.C.DM9
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Challenge: Deathmatch Challenge 9
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

    US_HASHMAP_TRIGGERCOLLECTOR = dword(0x1d009f8)
    """
    [32-bit Pointer] (US) Hashmap | Trigger.Collector
    Used in various missions to detect triggers such as Tutorial1 secret and capture point index in Hold Until Relief
    +0x04
    ++0x1C = [32-bit] Trigger.Collector
    -- 0xffffffff = Untriggered
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

    US_HASHMAP_LLRAGNA = dword(0x1d00bf4)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Ragna
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Ragnarok and Roll
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

    US_HASHMAP_LLFUNFAIR = dword(0x1d00ef8)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Funfair
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Nobody Rides For Free
    """

    US_HASHMAP_LWMADCOW = dword(0x1d0100c)
    """
    [32-bit Pointer] (US) Hashmap | L.W.MadCow
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Weapon: Mad Cow
    """

    US_HASHMAP_LSCHWBNG = dword(0x1d01010)
    """
    [32-bit Pointer] (US) Hashmap | L.Sch.WBnG
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Scheme: Sinking BnG
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

    US_HASHMAP_LWBANANA = dword(0x1d01134)
    """
    [32-bit Pointer] (US) Hashmap | L.W.Banana
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Weapon: Banana Bomb
    """

    US_HASHMAP_LPDONKEY = dword(0x1d01154)
    """
    [32-bit Pointer] (US) Hashmap | L.P.Donkey
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: Concrete Donkey
    """

    US_HASHMAP_LPFOOLS = dword(0x1d011bc)
    """
    [32-bit Pointer] (US) Hashmap | L.P.Fools
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: Fakes and April Fools
    """

    US_HASHMAP_LPLANDD = dword(0x1d01280)
    """
    [32-bit Pointer] (US) Hashmap | L.P.LandD
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: Lightside and Darkside
    """

    US_HASHMAP_LPBRIGHT = dword(0x1d01284)
    """
    [32-bit Pointer] (US) Hashmap | L.P.Bright
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: Brightside
    """

    US_HASHMAP_LSCHPRO = dword(0x1d0142c)
    """
    [32-bit Pointer] (US) Hashmap | L.Sch.Pro
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Scheme: Pro
    """

    US_FLOWCONTROLSERVICE_GAME_STATE = byte(0x1dbe668)
    """
    [8-bit] (US) FlowControlService | Game State
    bit0 = ?
    bit1 = Ingame
    bit2 = Fade In/Out
    bit3 = Loading (Phase 2)
    bit4 = Loading (Phase 1)
    bit5 = ?
    bit6 = FMV
    bit7 = ?

    Useful masks:
    - Is Ingame: & 0x4e == 0x2
    - Is Loading: & 0x1c > 0x0
    - Is In Menu: & 0x5e == 0x0
    """

    US_FLOWCONTROLSERVICE_GAME_STATE_2 = byte(0x1dbe669)
    """
    [8-bit] (US) FlowControlService | Game State 2
    bit0 = Paused
    bit1 = Paused Alt (1 frame delay)
    bit2 = Attract Mode
    """

    US_FLOWCONTROLSERVICE_ATTRACT_MODE_POINTER = dword(0x1dbe678)
    """
    [32-bit Pointer] (US) FlowControlService | Attract Mode Pointer
    Pointer related to Attract mode
    0x0 = Disabled
    * = Enabled
    """

    EU_FLOWCONTROLSERVICE_GAME_STATE = byte(0x1e00280)
    """
    [8-bit] (EU) FlowControlService | Game State
    bit0 = ?
    bit1 = Ingame
    bit2 = Fade In/Out
    bit3 = Loading (Phase 2)
    bit4 = Loading (Phase 1)
    bit5 = ?
    bit6 = FMV
    bit7 = ?

    Useful masks:
    - Is Ingame: & 0x4e == 0x2
    - Is Loading: & 0x1c > 0x0
    - Is In Menu: & 0x5e == 0x0
    """

    EU_FLOWCONTROLSERVICE_GAME_STATE_2 = byte(0x1e00281)
    """
    [8-bit] (EU) FlowControlService | Game State 2
    bit0 = Paused
    bit1 = Paused Alt (1 frame delay)
    bit2 = Attract Mode
    """

    EU_FLOWCONTROLSERVICE_ATTRACT_MODE_POINTER = dword(0x1e00290)
    """
    [32-bit Pointer] (EU) FlowControlService | Attract Mode Pointer
    Pointer related to Attract mode
    0x0 = Disabled
    * = Enabled
    """

