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
    [32-bit Boolean] (EU) State Check | In Menu
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

    US_XDATARESOURCEMANAGER = dword(0x6ad854)
    """
    [32-bit Pointer] (US) XDataResourceManager
    +0x18 = [32-bit Pointer] Pointer to Hashmap | XDataResourceDescriptor
    - Array of 6000 32-bit pointers in a deterministic order based on their key name
    - Always point to 0x1cfb770
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

    US_SERIAL = dword_be(0x6b294c)
    """
    [32-bit BE ASCII] (US) Serial
    (cdrom0:\\SLUS_208.94;1)
    0x534c5553 = SLUS
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
    ---- 0x00 = Waiting (End of turn?)
    ---- 0x01 = Walking
    ---- 0x02 = About to jump
    ---- 0x03 = Jump
    ---- 0x06 = Backflip
    ---- 0x07 = Bonk
    ---- 0x08 = Explosion recoil
    ---- 0x09 = Head in ground
    ---- 0x0a = Idle (Own turn)
    ---- 0x0d = Drowning
    ---- 0x0e = Using Jetpack
    ---- 0x0f = Using Ninja rope
    ---- 0x11 = Touching ground?
    ---- 0x13 = Using Parachute
    ---- 0x15 = Waiting (Own team turn?)
    ---- 0x16 = Waiting (Enemy team turn?)
    ---- 0x1b = Stunned
    ---- 0x22 = Waiting (During projectile launch)?
    ---- 0x24 = Frontflip
    ---- 0x25 = Using teleporter
    ---- 0x26 = Falling
    +++0x84 = [32-bit] Equipped Weapon ID
    ---- 0x00 = Bazooka
    ---- 0x01 = Grenade
    ---- 0x02 = Cluster Bomb
    ---- 0x04 = Dynamite
    ---- 0x07 = Land Mine
    ---- 0x08 = Shotgun
    ---- 0x09 = Uzi
    ---- 0x0a = Baseball Bat
    ---- 0x0b = Prod
    ---- 0x0d = Fire Punch
    ---- 0x0e = Homing Missile
    ---- 0x0f = Mortar
    ---- 0x12 = Sheep
    ---- 0x14 = Petrol Bomb
    ---- 0x15 = Gas Canister
    ---- 0x22 = Sticky Bomb
    ---- 0x23 = Binoculars
    ---- 0x27 = Girder
    ---- 0x29 = Ninja Rope
    ---- 0x2a = Parachute
    ---- 0x2f = Teleport
    ---- 0x30 = Jet Pack
    ---- 0x31 = Skip Go
    ---- 0x32 = Surrender
    ---- 0x33 = Worm Select
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
    ---- 0x0 = Red
    ---- 0x1 = Blue
    ---- 0x2 = Green
    ---- 0x3 = Yellow
    ---- * = Black
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
    ---- 0x00 = Waiting (End of turn?)
    ---- 0x01 = Walking
    ---- 0x02 = About to jump
    ---- 0x03 = Jump
    ---- 0x06 = Backflip
    ---- 0x07 = Bonk
    ---- 0x08 = Explosion recoil
    ---- 0x09 = Head in ground
    ---- 0x0a = Idle (Own turn)
    ---- 0x0d = Drowning
    ---- 0x0e = Using Jetpack
    ---- 0x0f = Using Ninja rope
    ---- 0x11 = Touching ground?
    ---- 0x13 = Using Parachute
    ---- 0x15 = Waiting (Own team turn?)
    ---- 0x16 = Waiting (Enemy team turn?)
    ---- 0x1b = Stunned
    ---- 0x22 = Waiting (During projectile launch)?
    ---- 0x24 = Frontflip
    ---- 0x25 = Using teleporter
    ---- 0x26 = Falling
    +++0x84 = [32-bit] Equipped Weapon ID
    ---- 0x00 = Bazooka
    ---- 0x01 = Grenade
    ---- 0x02 = Cluster Bomb
    ---- 0x04 = Dynamite
    ---- 0x07 = Land Mine
    ---- 0x08 = Shotgun
    ---- 0x09 = Uzi
    ---- 0x0a = Baseball Bat
    ---- 0x0b = Prod
    ---- 0x0d = Fire Punch
    ---- 0x0e = Homing Missile
    ---- 0x0f = Mortar
    ---- 0x12 = Sheep
    ---- 0x14 = Petrol Bomb
    ---- 0x15 = Gas Canister
    ---- 0x22 = Sticky Bomb
    ---- 0x23 = Binoculars
    ---- 0x27 = Girder
    ---- 0x29 = Ninja Rope
    ---- 0x2a = Parachute
    ---- 0x2f = Teleport
    ---- 0x30 = Jet Pack
    ---- 0x31 = Skip Go
    ---- 0x32 = Surrender
    ---- 0x33 = Worm Select
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
    ---- 0x0 = Red
    ---- 0x1 = Blue
    ---- 0x2 = Green
    ---- 0x3 = Yellow
    ---- * = Black
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

    US_STATE_CHECK_TITLE_SCREEN_ACTIVE = dword(0x79eb40)
    """
    [32-bit Boolean] (US) State Check | Title Screen Active
    """

    US_STATE_CHECK_IN_MENU = dword(0x79eb44)
    """
    [32-bit Boolean] (US) State Check | In Menu
    """

    US_STATE_CHECK_IN_GAME = dword(0x79eb50)
    """
    [32-bit Boolean] (US) State Check | In Game
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

    US_GAME_STATUS_IS_IN_INGAME_CUTSCENE = dword(0x15703bc)
    """
    [32-bit] (US) Game Status | Is in ingame cutscene
    0x0 = False
    0x1 = True
    """

    EU_LUA_STATE_STACK_TOP = dword(0x17f2e18)
    """
    [32-bit Pointer] (EU) Lua State | Stack Top
    First free slot in the stack
    """

    EU_LUA_STATE_BASE = dword(0x17f2e1c)
    """
    [32-bit Pointer] (EU) Lua State | Base
    Base of current function
    """

    EU_LUA_STATE_GLOBAL_STATE = dword(0x17f2e20)
    """
    [32-bit Pointer] (EU) Lua State | Global State
    +0x0 = [32-bit Pointer] String Hashtable
    +0x8 = [32-bit] String Hashtable | Number of elements
    +0x10 = [32-bit] String Hashtable | Size Allocated
    +0x18 = [32-bit] RootGC
    -- List of all collectable objects
    """

    EU_LUA_STATE_CALL_INFO = dword(0x17f2e24)
    """
    [32-bit Pointer] (EU) Lua State | Call Info
    Call info for current function
    """

    EU_LUA_STATE_STACK_LAST = dword(0x17f2e28)
    """
    [32-bit Pointer] (EU) Lua State | Stack Last
    Last free slot in the stack
    """

    EU_LUA_STATE_STACK_BASE = dword(0x17f2e2c)
    """
    [32-bit Pointer] (EU) Lua State | Stack Base
    """

    EU_LUA_STATE_STACK_SIZE = dword(0x17f2e30)
    """
    [32-bit] (EU) Lua State | Stack Size
    """

    EU_LUA_STATE_END_CALL_INFO = dword(0x17f2e34)
    """
    [32-bit Pointer] (EU) Lua State | End Call Info
    Points after end of ci array
    """

    EU_LUA_STATE_BASE_CALL_INFO = dword(0x17f2e38)
    """
    [32-bit Pointer] (EU) Lua State | Base Call Info
    Array of CallInfo's
    """

    EU_LUA_STATE_CALL_INFO_SIZE = word(0x17f2e3c)
    """
    [16-bit] (EU) Lua State | Call Info Size
    Size of Base Call Info array
    """

    EU_LUA_STATE_NESTED_C_CALLS = word(0x17f2e3e)
    """
    [16-bit] (EU) Lua State | Nested C Calls
    Number of nested C calls
    """

    EU_LUA_STATE_TABLE_OF_GLOBALS = dword(0x17f2e54)
    """
    [32-bit Pointer] (EU) Lua State | Table of Globals
    Always point to 0x17f31c0
    +0x0 = [32-bit Pointer] Next Element
    +0x7 = [8-bit] LSizeNode
    -- Refer to $0x017f31c7
    +0x8 = [32-bit Pointer] Meta Table
    +0xc = [32-bit Pointer] Array Part
    +0x10 = [32-bit Pointer] Global Node Vector
    -- Refer to $0x17f31d0
    +0x14 = [32-bit Pointer] First Free Node
    +0x18 = [32-bit Pointer] GCList
    +0x1c = [32-bit Pointer] Size of Array Part
    """

    EU_LUA_GLOBAL_TABLE_LSIZENODE = byte(0x17f31c7)
    """
    [8-bit] (EU) Lua Global Table | LSizeNode
    Log2 of the size of the vector
    Most missions starts at 7 or 8 once initialized and never exceeds 8
    0x0 = 0
    0x1 = 1
    0x2 = 2
    0x3 = 4
    0x4 = 8
    0x5 = 16
    0x6 = 32
    0x7 = 64
    0x8 = 128
    0x9 = 256
    0xa = 512
    0xb = 1024
    0xc = 2048
    0xd = 4096 (Theoretical max before memory runs out)
    """

    EU_LUA_GLOBAL_TABLE_NODE_VECTOR = dword(0x17f31d0)
    """
    [32-bit Pointer] (EU) Lua Global Table | Node Vector
    Hashmap of all global variables instanciated in the script, implemented as a chained scatter table.
    Read more about the implementation at https://www.lua.org/doc/jucs05.pdf (Page 4)
    Source code: https://www.lua.org/source/5.0/ltable.c.html

    Each node is 20 bytes long and follow this structure:
    | +0x0 = [32-bit] Key type (always 4 for strings)
    | +0x4 = [32-bit Pointer] Pointer to key string
    | ++0x0 = [ASCII] Key string
    | ++0xfffffffc = [32-bit] String length
    | ++0xfffffff8 = [32-bit] String hash
    | ++0x8 = [32-bit] = Value type (Always 3 for numbers)
    | ++0xc = [32-bit Float] = Value
    | --- Lua numbers are stored as float even if interpreted as integers
    | ++0x10 = [32-bit Pointer] = Next node

    The offset of a given node is calculated using the following formula:
    (StringHash % (1 << LSize)) * 20
    StringHash being the precomputed Lua string hash of said variable and LSize being the Log2 size of the vector (see $0x017f31c7)
    This means that the offset varies depending on the vector size (which is a power of two and can only grow as the script runs) but these offsets can be precalculated and checked against in alt groups for each LSize value.

    The hashmap deals with hash clashes by creating a node in the next empty slot and by appending it to the linked list of it's actual slot. That means you are not guaranteed to find the variable you are looking for in the calculated slot directly, but you are guaranteed to find it if you follow the linked list.
    Fortunately, clashes are rare by design and should never exceed a linked list of depth 2 for any given slot.

    All pointer chains below are based on testing and are specific to each script being currently run.
    Hopefully the chains are deterministic as these variables are initialized at the start of the script and should never be garbage collected.
    Offsets are consistent between EU and USA versions.

    +0x20 = [32-bit Float] Costa Del Danger | MineNumber (LSize 1-8)
    -- "MineNumber" variable from "holiday.lua"
    +0x268
    ++0xc = [32-bit Float] Driving Range | TargetNumber (LSize 5-7)
    --- "TargetNumber" variable from "driving.lua"
    --- Ranges from 1.0 to 15.0
    +0x740
    ++0xc = [32-bit Float] School | Easter Egg (LSize 7-8)
    --- "EasterEgg" variable from "SCHOOLS.lua"
    --- 0.0 = No basket
    --- 1.0 = First basket
    --- 2.0 = Second basket
    +0x920
    ++0xc = [32-bit Float] A Quick Fix | Team17 Easter Egg (LSize 7-10)
    --- "Team17" variable from "notpc.lua"
    --- 0.0 = Default value
    --- 100000.0 = T
    --- 110000.0 = TE
    --- 111000.0 = TEA
    --- 111100.0 = TEAM
    --- 111110.0 = TEAM1
    --- 111111.0 = TEAM17
    +0xb4c = [32-bit Float] Showdown | CrateNumber (LSize 8)
    -- "CrateNumber" variable from "SHOWDOWN.lua"
    -- 1.0 = Donkey Crate
    -- 2.0 = Easter Egg
    +0x1280
    ++0xc = [32-bit Float] Nobody Rides For Free | TicketBoothDestroyed (LSize 8-12)
    --- "TicketBoothDestroyed" variable from "funfair.lua"
    --- 0.0 = False
    --- 1.0 = True
    +0x12e0 = [32-bit Float] Graveyard | TriggerIndex (LSize 8-12)
    -- "TriggerIndex" variable from "graveyard.lua"
    -- 9.0 = Easter Egg
    """

    EU_INGAME_CURRENT_LUA_SCRIPT_HASH = dword(0x18005a8)
    """
    [32-bit] (EU) Ingame | Current LUA Script Hash
    0x00000000 = Uninitialized
    0xdddddddd = No script loaded
    0x4d884e4d = tutorial1 (Atlantis Training Facility)
    0xe059c1ce = tutorial2 (Down in the Dumps)
    0x796efc55 = Tutorial3 (Return to Chateau Assassin)
    0x9166854b = Tutorial4 (The Mighty Kong)
    0x98d2e8ca = tutorial5 (Test Tubes)
    0xf4a542f6 = driving (The Driving Range)
    0x8c96ec = dday (D-Day)
    0xa2c82545 = CrateBritain (Crate Britain)
    0x665fe3f6 = graveyard (Grave Danger)
    0x75cdd4 = leek (A Leek in a Vegetable Patch)
    0x2a361 = ICE (Ice, Ice, Maybe)
    0x1c37e844 = Collide (When Annelids Collide)
    0x3417d = rum (Rum Deal)
    0x11bd853a = crust (Earn Your Crust)
    0x51aefa4a = applecore (Apple Core Island)
    0x8be523b4 = helterskelter (Helter Skelter)
    0xafe262f5 = cherry (Take My Cherry)
    0x10530c6f = clean (In Space, No-One Can Hear You Clean)
    0x99727cd0 = timbers (Shiver Me Timbers)
    0xf95e9e91 = FALLING (Falling For You)
    0xe52395ca = cropcircle (Crop Circle)
    0x369832aa = treevillage (Tree Village Trouble)
    0xf4a6179c = landing (Movie Mayhem)
    0xad602956 = beanstalk (Worm and the Beanstalk)
    0xbf359705 = SCHOOLS (School's in for Summer)
    0x1e6dea78 = highstakes (High Stakes)
    0x11cc0f09 = notpc (A Quick Fix)
    0x76dc359c = cooped (All Cooped Up)
    0xe9a91aa = TRIAL (Trial of the Damned)
    0xab409627 = SHOWDOWN (Showdown at the OK Corale Reef)
    0x4a099be8 = plaice (Plaice Holder)
    0x751f79c9 = hookline (Hook, Line, and Skimmer)
    0x4fc95563 = funfair (Nobody Rides For Free)
    0x3709f4b1 = Pegasus (Hold Until Relieved)
    0x9cf66df1 = boldly (To Boldly Go)
    0x2ec3734 = balloon (Beautiful Balloon)
    0xde191d7f = countingsheep (A Good Nights Sleep)
    0xa4f675a = BREAKFAST (Beefcake Breakfast Brawl)
    0xce3787ce = holiday (Costa Del Danger)
    0x75fbb1 = pack (Ragnarok and Roll)
    0xeb94d71 = ALIEN (Alien Juice Suckers)
    0xc5b5cccd = TargetHunt (Shotgun Challenge 1)
    0x4dd3575c = TargetHunt2 (Shotgun Challenge 2)
    0x45c54185 = HOMING (Shotgun Challenge 3)
    0xaeed8ea = Sheep1 (Super Sheep Challenge 1)
    0xfc7259f8 = Sheep2 (Super Sheep Challenge 2)
    0x9e1d76e5 = TargetHunt4 (Super Sheep Challenge 3)
    0x3629ec94 = cratefun (Jet Pack Challenge 1)
    0xab55da97 = jetpackchall2 (Jet Pack Challenge 2)
    0xa43f4a1b = jetpackchall3 (Jet Pack Challenge 3)
    0xba5e49c = Chute1 (Parachute Challenge 1)
    0xfc6b191b = chute2 (Parachute Challenge 2)
    0xe27338ed = chute3 (Parachute Challenge 3)
    0x2befed54 = Deathmatch1 (Deathmatch Challenge 1)
    0x59ec1d1b = Deathmatch2 (Deathmatch Challenge 2)
    0x9297c549 = Deathmatch3 (Deathmatch Challenge 3)
    0xc96921d = Deathmatch4 (Deathmatch Challenge 4)
    0x69a68f4b = Deathmatch5 (Deathmatch Challenge 5)
    0xddfff265 = Deathmatch6 (Deathmatch Challenge 6)
    0x7cfff16 = Deathmatch7 (Deathmatch Challenge 7)
    0xeabd81c2 = Deathmatch8 (Deathmatch Challenge 8)
    0xa2b8d30b = Deathmatch9 (Deathmatch Challenge 9)
    0x2c80b4b2 = Deathmatch10 (Deathmatch Challenge 10)
    0x12f25978 = stdvs (Multiplayer Game)
    0x3be80eb5 = attract (Attract Mode)
    """

    EU_INGAME_CURRENT_LUA_SCRIPT_NAME = (0x18005b0)
    """
    [16 bytes BE ASCII] (EU) Ingame | Current LUA Script Name
    The first 5 bytes are always overwritten with 0xdd upon exiting a level
    0x00000000 = Uninitialized
    0xdddddddd = Uninitialized
    "tutorial1" = Atlantis Training Facility
    "tutorial2" = Down in the Dumps
    "Tutorial3" = Return to Chateau Assassin
    "Tutorial4" = The Mighty Kong
    "tutorial5" = Test Tubes
    "driving" = The Driving Range
    "dday" = D-Day
    "CrateBritain" = Crate Britain
    "graveyard" = Grave Danger
    "leek" = A Leek in a Vegetable Patch
    "ICE" = Ice, Ice, Maybe
    "Collide" = When Annelids Collide
    "rum" = Rum Deal
    "crust" = Earn Your Crust
    "applecore" = Apple Core Island
    "helterskelter" = Helter Skelter
    "cherry" = Take My Cherry
    "clean" = In Space, No-One Can Hear You Clean
    "timbers" = Shiver Me Timbers
    "FALLING" = Falling For You
    "cropcircle" = Crop Circle
    "treevillage" = Tree Village Trouble
    "landing" = Movie Mayhem
    "beanstalk" = Worm and the Beanstalk
    "SCHOOLS" = School's in for Summer
    "highstakes" = High Stakes
    "notpc" = A Quick Fix
    "cooped" = All Cooped Up
    "TRIAL" = Trial of the Damned
    "SHOWDOWN" = Showdown at the OK Corale Reef
    "plaice" = Plaice Holder
    "hookline" = Hook, Line, and Skimmer
    "funfair" = Nobody Rides For Free
    "Pegasus" = Hold Until Relieved
    "boldly" = To Boldly Go
    "balloon" = Beautiful Balloon
    "countingsheep" = A Good Nights Sleep
    "BREAKFAST" = Beefcake Breakfast Brawl
    "holiday" = Costa Del Danger
    "pack" = Ragnarok and Roll
    "ALIEN" = Alien Juice Suckers
    "TargetHunt" = Shotgun Challenge 1
    "TargetHunt2" = Shotgun Challenge 2
    "HOMING" = Shotgun Challenge 3
    "Sheep1" = Super Sheep Challenge 1
    "Sheep2" = Super Sheep Challenge 2
    "TargetHunt4" = Super Sheep Challenge 3
    "cratefun" = Jet Pack Challenge 1
    "jetpackchall2" = Jet Pack Challenge 2
    "jetpackchall3" = Jet Pack Challenge 3
    "Chute1" = Parachute Challenge 1
    "chute2" = Parachute Challenge 2
    "chute3" = Parachute Challenge 3
    "Deathmatch1" = Deathmatch Challenge 1
    "Deathmatch2" = Deathmatch Challenge 2
    "Deathmatch3" = Deathmatch Challenge 3
    "Deathmatch4" = Deathmatch Challenge 4
    "Deathmatch5" = Deathmatch Challenge 5
    "Deathmatch6" = Deathmatch Challenge 6
    "Deathmatch7" = Deathmatch Challenge 7
    "Deathmatch8" = Deathmatch Challenge 8
    "Deathmatch9" = Deathmatch Challenge 9
    "Deathmatch10" = Deathmatch Challenge 10
    "stdvs" = Multiplayer Game
    "attract" = Attract Mode
    """

    US_LUA_GLOBAL_TABLE_LSIZENODE = byte(0x180a4ff)
    """
    [8-bit] (US) Lua Global Table | LSizeNode
    Log2 of the size of the vector
    Most missions starts at 7 or 8 once initialized and never exceeds 8
    0x0 = 0
    0x1 = 1
    0x2 = 2
    0x3 = 4
    0x4 = 8
    0x5 = 16
    0x6 = 32
    0x7 = 64
    0x8 = 128
    0x9 = 256
    0xa = 512
    0xb = 1024
    0xc = 2048
    0xd = 4096 (Theoretical max before memory runs out)
    """

    US_LUA_GLOBAL_TABLE_NODE_VECTOR = dword(0x180a508)
    """
    [32-bit Pointer] (US) Lua Global Table | Node Vector
    Hashmap of all global variables instanciated in the script, implemented as a chained scatter table.
    Read more about the implementation at https://www.lua.org/doc/jucs05.pdf (Page 4)
    Source code: https://www.lua.org/source/5.0/ltable.c.html

    Each node is 20 bytes long and follow this structure:
    | +0x0 = [32-bit] Key type (always 4 for strings)
    | +0x4 = [32-bit Pointer] Pointer to key string
    | ++0x0 = [ASCII] Key string
    | ++0xfffffffc = [32-bit] String length
    | ++0xfffffff8 = [32-bit] String hash
    | ++0x8 = [32-bit] = Value type (Always 3 for numbers)
    | ++0xc = [32-bit Float] = Value
    | --- Lua numbers are stored as float even if interpreted as integers
    | ++0x10 = [32-bit Pointer] = Next node

    The offset of a given node is calculated using the following formula:
    (StringHash % (1 << LSize)) * 20
    StringHash being the precomputed Lua string hash of said variable and LSize being the Log2 size of the vector (see $0x0180a4ff)
    This means that the offset varies depending on the vector size (which is a power of two and can only grow as the script runs) but these offsets can be precalculated and checked against in alt groups for each LSize value.

    The hashmap deals with hash clashes by creating a node in the next empty slot and by appending it to the linked list of it's actual slot. That means you are not guaranteed to find the variable you are looking for in the calculated slot directly, but you are guaranteed to find it if you follow the linked list.
    Fortunately, clashes are rare by design and should never exceed a linked list of depth 2 for any given slot.

    All pointer chains below are based on testing and are specific to each script being currently run.
    Hopefully the chains are deterministic as these variables are initialized at the start of the script and should never be garbage collected.
    Offsets are consistent between EU and USA versions.

    +0x20 = [32-bit Float] Costa Del Danger | MineNumber (LSize 1-8)
    -- "MineNumber" variable from "holiday.lua"
    +0x268
    ++0xc = [32-bit Float] Driving Range | TargetNumber (LSize 5-7)
    --- "TargetNumber" variable from "driving.lua"
    --- Ranges from 1.0 to 15.0
    +0x740
    ++0xc = [32-bit Float] School | Easter Egg (LSize 7-8)
    --- "EasterEgg" variable from "SCHOOLS.lua"
    --- 0.0 = No basket
    --- 1.0 = First basket
    --- 2.0 = Second basket
    +0x920
    ++0xc = [32-bit Float] A Quick Fix | Team17 Easter Egg (LSize 7-10)
    --- "Team17" variable from "notpc.lua"
    --- 0.0 = Default value
    --- 100000.0 = T
    --- 110000.0 = TE
    --- 111000.0 = TEA
    --- 111100.0 = TEAM
    --- 111110.0 = TEAM1
    --- 111111.0 = TEAM17
    +0xb4c = [32-bit Float] Showdown | CrateNumber (LSize 8)
    -- "CrateNumber" variable from "SHOWDOWN.lua"
    -- 1.0 = Donkey Crate
    -- 2.0 = Easter Egg
    +0x1280
    ++0xc = [32-bit Float] Nobody Rides For Free | TicketBoothDestroyed (LSize 8-12)
    --- "TicketBoothDestroyed" variable from "funfair.lua"
    --- 0.0 = False
    --- 1.0 = True
    +0x12e0 = [32-bit Float] Graveyard | TriggerIndex (LSize 8-12)
    -- "TriggerIndex" variable from "graveyard.lua"
    -- 9.0 = Easter Egg
    """

    US_INGAME_CURRENT_LUA_SCRIPT_HASH = dword(0x180c5f0)
    """
    [32-bit] (US) Ingame | Current LUA Script Hash
    0x00000000 = Uninitialized
    0xdddddddd = No script loaded
    0x4d884e4d = tutorial1 (Atlantis Training Facility)
    0xe059c1ce = tutorial2 (Down in the Dumps)
    0x796efc55 = Tutorial3 (Return to Chateau Assassin)
    0x9166854b = Tutorial4 (The Mighty Kong)
    0x98d2e8ca = tutorial5 (Test Tubes)
    0xf4a542f6 = driving (The Driving Range)
    0x8c96ec = dday (D-Day)
    0xa2c82545 = CrateBritain (Crate Britain)
    0x665fe3f6 = graveyard (Grave Danger)
    0x75cdd4 = leek (A Leek in a Vegetable Patch)
    0x2a361 = ICE (Ice, Ice, Maybe)
    0x1c37e844 = Collide (When Annelids Collide)
    0x3417d = rum (Rum Deal)
    0x11bd853a = crust (Earn Your Crust)
    0x51aefa4a = applecore (Apple Core Island)
    0x8be523b4 = helterskelter (Helter Skelter)
    0xafe262f5 = cherry (Take My Cherry)
    0x10530c6f = clean (In Space, No-One Can Hear You Clean)
    0x99727cd0 = timbers (Shiver Me Timbers)
    0xf95e9e91 = FALLING (Falling For You)
    0xe52395ca = cropcircle (Crop Circle)
    0x369832aa = treevillage (Tree Village Trouble)
    0xf4a6179c = landing (Movie Mayhem)
    0xad602956 = beanstalk (Worm and the Beanstalk)
    0xbf359705 = SCHOOLS (School's in for Summer)
    0x1e6dea78 = highstakes (High Stakes)
    0x11cc0f09 = notpc (A Quick Fix)
    0x76dc359c = cooped (All Cooped Up)
    0xe9a91aa = TRIAL (Trial of the Damned)
    0xab409627 = SHOWDOWN (Showdown at the OK Corale Reef)
    0x4a099be8 = plaice (Plaice Holder)
    0x751f79c9 = hookline (Hook, Line, and Skimmer)
    0x4fc95563 = funfair (Nobody Rides For Free)
    0x3709f4b1 = Pegasus (Hold Until Relieved)
    0x9cf66df1 = boldly (To Boldly Go)
    0x2ec3734 = balloon (Beautiful Balloon)
    0xde191d7f = countingsheep (A Good Nights Sleep)
    0xa4f675a = BREAKFAST (Beefcake Breakfast Brawl)
    0xce3787ce = holiday (Costa Del Danger)
    0x75fbb1 = pack (Ragnarok and Roll)
    0xeb94d71 = ALIEN (Alien Juice Suckers)
    0xc5b5cccd = TargetHunt (Shotgun Challenge 1)
    0x4dd3575c = TargetHunt2 (Shotgun Challenge 2)
    0x45c54185 = HOMING (Shotgun Challenge 3)
    0xaeed8ea = Sheep1 (Super Sheep Challenge 1)
    0xfc7259f8 = Sheep2 (Super Sheep Challenge 2)
    0x9e1d76e5 = TargetHunt4 (Super Sheep Challenge 3)
    0x3629ec94 = cratefun (Jet Pack Challenge 1)
    0xab55da97 = jetpackchall2 (Jet Pack Challenge 2)
    0xa43f4a1b = jetpackchall3 (Jet Pack Challenge 3)
    0xba5e49c = Chute1 (Parachute Challenge 1)
    0xfc6b191b = chute2 (Parachute Challenge 2)
    0xe27338ed = chute3 (Parachute Challenge 3)
    0x2befed54 = Deathmatch1 (Deathmatch Challenge 1)
    0x59ec1d1b = Deathmatch2 (Deathmatch Challenge 2)
    0x9297c549 = Deathmatch3 (Deathmatch Challenge 3)
    0xc96921d = Deathmatch4 (Deathmatch Challenge 4)
    0x69a68f4b = Deathmatch5 (Deathmatch Challenge 5)
    0xddfff265 = Deathmatch6 (Deathmatch Challenge 6)
    0x7cfff16 = Deathmatch7 (Deathmatch Challenge 7)
    0xeabd81c2 = Deathmatch8 (Deathmatch Challenge 8)
    0xa2b8d30b = Deathmatch9 (Deathmatch Challenge 9)
    0x2c80b4b2 = Deathmatch10 (Deathmatch Challenge 10)
    0x12f25978 = stdvs (Multiplayer Game)
    0x3be80eb5 = attract (Attract Mode)
    """

    US_INGAME_CURRENT_LUA_SCRIPT_NAME = (0x180c5f8)
    """
    [16 bytes BE ASCII] (US) Ingame | Current LUA Script Name
    The first 5 bytes are always overwritten with 0xdd upon exiting a level
    0x00000000 = Uninitialized
    0xdddddddd = Uninitialized
    "tutorial1" = Atlantis Training Facility
    "tutorial2" = Down in the Dumps
    "Tutorial3" = Return to Chateau Assassin
    "Tutorial4" = The Mighty Kong
    "tutorial5" = Test Tubes
    "driving" = The Driving Range
    "dday" = D-Day
    "CrateBritain" = Crate Britain
    "graveyard" = Grave Danger
    "leek" = A Leek in a Vegetable Patch
    "ICE" = Ice, Ice, Maybe
    "Collide" = When Annelids Collide
    "rum" = Rum Deal
    "crust" = Earn Your Crust
    "applecore" = Apple Core Island
    "helterskelter" = Helter Skelter
    "cherry" = Take My Cherry
    "clean" = In Space, No-One Can Hear You Clean
    "timbers" = Shiver Me Timbers
    "FALLING" = Falling For You
    "cropcircle" = Crop Circle
    "treevillage" = Tree Village Trouble
    "landing" = Movie Mayhem
    "beanstalk" = Worm and the Beanstalk
    "SCHOOLS" = School's in for Summer
    "highstakes" = High Stakes
    "notpc" = A Quick Fix
    "cooped" = All Cooped Up
    "TRIAL" = Trial of the Damned
    "SHOWDOWN" = Showdown at the OK Corale Reef
    "plaice" = Plaice Holder
    "hookline" = Hook, Line, and Skimmer
    "funfair" = Nobody Rides For Free
    "Pegasus" = Hold Until Relieved
    "boldly" = To Boldly Go
    "balloon" = Beautiful Balloon
    "countingsheep" = A Good Nights Sleep
    "BREAKFAST" = Beefcake Breakfast Brawl
    "holiday" = Costa Del Danger
    "pack" = Ragnarok and Roll
    "ALIEN" = Alien Juice Suckers
    "TargetHunt" = Shotgun Challenge 1
    "TargetHunt2" = Shotgun Challenge 2
    "HOMING" = Shotgun Challenge 3
    "Sheep1" = Super Sheep Challenge 1
    "Sheep2" = Super Sheep Challenge 2
    "TargetHunt4" = Super Sheep Challenge 3
    "cratefun" = Jet Pack Challenge 1
    "jetpackchall2" = Jet Pack Challenge 2
    "jetpackchall3" = Jet Pack Challenge 3
    "Chute1" = Parachute Challenge 1
    "chute2" = Parachute Challenge 2
    "chute3" = Parachute Challenge 3
    "Deathmatch1" = Deathmatch Challenge 1
    "Deathmatch2" = Deathmatch Challenge 2
    "Deathmatch3" = Deathmatch Challenge 3
    "Deathmatch4" = Deathmatch Challenge 4
    "Deathmatch5" = Deathmatch Challenge 5
    "Deathmatch6" = Deathmatch Challenge 6
    "Deathmatch7" = Deathmatch Challenge 7
    "Deathmatch8" = Deathmatch Challenge 8
    "Deathmatch9" = Deathmatch Challenge 9
    "Deathmatch10" = Deathmatch Challenge 10
    "stdvs" = Multiplayer Game
    "attract" = Attract Mode
    """

    EU_MESSAGERELAY_POINTER = dword(0x1b55290)
    """
    [32-bit Pointer] (EU) MessageRelay Pointer
    0x0 = Unloaded
    * = Loaded
    """

    US_MESSAGERELAY_POINTER = dword(0x1bacf10)
    """
    [32-bit Pointer] (US) MessageRelay Pointer
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

    EU_HASHMAP_QLRET = dword(0x1ce3780)
    """
    [32-bit Pointer] (EU) Hashmap | Q.LRet
    +0x4
    ++0x1c = [32-bit] Game Option | Retreat Time
    --- Time measured in milliseconds
    --- 0x0 = 0 Seconds
    --- 0xbb8 = 3 Seconds
    --- 0x1388 = 5 Seconds
    --- 0x2710 = 10 Seconds
    """

    EU_HASHMAP_ELAPSEDROUNDTIME = dword(0x1ce37b4)
    """
    [32-bit Pointer] (EU) Hashmap | ElapsedRoundTime
    +0x4
    ++0x1c = [32-bit] Elapsed Round Time in milliseconds
    """

    EU_HASHMAP_JETPACKFUEL = dword(0x1ce3810)
    """
    [32-bit Pointer] (EU) Hashmap | Jetpack.Fuel
    +0x4
    ++0x1c = [32-bit] Jetpack Fuel
    """

    EU_HASHMAP_LLFUNFAIR = dword(0x1ce3898)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.Funfair
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Nobody Rides For Free
    """

    EU_HASHMAP_WATERLEVEL = dword(0x1ce39b0)
    """
    [32-bit Pointer] (EU) Hashmap | Water.Level
    +0x4
    ++0x1c = [32-bit] Water Level
    --- 0x0 = Default level
    """

    EU_HASHMAP_QHOT = dword(0x1ce3b00)
    """
    [32-bit Pointer] (EU) Hashmap | Q.Hot
    +0x4
    ++0x1c = [32-bit Boolean] Game Option | Hot Seat Timer
    --- Time measured in milliseconds
    --- 0x0 = 0 Seconds
    --- 0x1388 = 5 Seconds
    --- 0x2710 = 10 Seconds
    --- 0x3a98 = 15 Seconds
    """

    EU_HASHMAP_QUCHANCE = dword(0x1ce3b74)
    """
    [32-bit Pointer] (EU) Hashmap | Q.UChance
    +0x4
    ++0x1c = [32-bit] Game Option | Utility Crate Chance
    """

    EU_HASHMAP_LANDINITIALMAXHEIGHT = dword(0x1ce3b90)
    """
    [32-bit Pointer] (EU) Hashmap | Land.InitialMaxHeight
    +0x4
    ++0x1c = [32-bit Float] Current map's initial max height
    -- Unique value to each map, used in conjunction with the script name to determine the current challenge in the RP
    -- 0x44113984 = Shotgun Challenge 1
    -- 0x452b799b = Shotgun Challenge 2
    -- 0x444731d8 = Shotgun Challenge 3
    -- 0x453f9645 = Super Sheep Challenge 1
    -- 0x4415ee12 = Super Sheep Challenge 2
    -- 0x440b8bdc = Super Sheep Challenge 3
    -- 0x43e75e17 = Jet Pack Challenge 1
    -- 0x44082017 = Jet Pack Challenge 2
    -- 0x447aa8dc = Jet Pack Challenge 3
    -- 0x452b799b = Parachute Challenge 1
    -- 0x44ab25d0 = Parachute Challenge 2
    -- 0x4507f262 = Parachute Challenge 3
    -- 0x43d8a364 = Deathmatch Challenge 1
    -- 0x43c9ceab = Deathmatch Challenge 2
    -- 0x44074e83 = Deathmatch Challenge 3
    -- 0x43fa352b = Deathmatch Challenge 4
    -- 0x43cff6eb = Deathmatch Challenge 5
    -- 0x43c0b331 = Deathmatch Challenge 6
    -- 0x43f0dfac = Deathmatch Challenge 7
    -- 0x442bd166 = Deathmatch Challenge 8
    -- 0x43d4fde2 = Deathmatch Challenge 9
    -- 0x440b9c29 = Deathmatch Challenge 10
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

    EU_HASHMAP_QDTIME = dword(0x1ce3d34)
    """
    [32-bit Pointer] (EU) Hashmap | Q.DTime
    +0x4
    ++0x1c = [32-bit Boolean] Game Option | Round Time Display
    """

    EU_HASHMAP_LLHELTER = dword(0x1ce3d98)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.Helter
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Helter Skelter
    """

    EU_HASHMAP_QHCHANCE = dword(0x1ce3e04)
    """
    [32-bit Pointer] (EU) Hashmap | Q.HChance
    +0x4
    ++0x1c = [32-bit] Game Option | Health Crate Chance
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

    EU_HASHMAP_FELANDSPACE = dword(0x1ce3f74)
    """
    [32-bit Pointer] (EU) Hashmap | FE.Land.Space
    +0x4
    ++0x1c = [32-bit] Landscape Selection | Land Distance
    --- 0x0 = 0%
    --- 0x1 = 50%
    --- 0x2 = 100%
    """

    EU_HASHMAP_LLLANDING = dword(0x1ce4004)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.Landing
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Movie Mayhem
    """

    EU_HASHMAP_TURNTIMEREMAINING = dword(0x1ce403c)
    """
    [32-bit Pointer] (EU) Hashmap | TurnTimeRemaining
    +0x4
    ++0x1c = [32-bit] Ingame | Turn Time Remaining
    --- Time measured in milliseconds
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

    EU_HASHMAP_QTELIN = dword(0x1ce4198)
    """
    [32-bit Pointer] (EU) Hashmap | Q.TelIn
    +0x4
    ++0x1c = [32-bit] Game Option | Placement
    --- 0x0 = Random
    --- 0x1 = Manual
    """

    EU_HASHMAP_MCAGAMEAWARDED = dword(0x1ce41e0)
    """
    [32-bit Pointer] (EU) Hashmap | MCa.GameAwarded
    +0x4
    ++0x1c = [32-bit Boolean] Game Awarded
    --- Changes to 0x1 when entering the result screen if mission successful
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

    EU_HASHMAP_QFALL = dword(0x1ce4510)
    """
    [32-bit Pointer] (EU) Hashmap | Q.Fall
    +0x4
    ++0x1c = [32-bit Boolean] Game Option | Fall Damage Setting
    """

    EU_HASHMAP_LSGRAMPS = dword(0x1ce451c)
    """
    [32-bit Pointer] (EU) Hashmap | L.S.Gramps
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Voice: Grandpa
    """

    EU_HASHMAP_FELANDTIME = dword(0x1ce4544)
    """
    [32-bit Pointer] (EU) Hashmap | FE.Land.Time
    +0x4
    ++0x1c = [32-bit] Landscape Selection | Time of Day
    --- 0x0 = Day
    --- 0x1 = Rain
    --- 0x2 = Night
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

    EU_HASHMAP_AUDIOVOLMUSIC = dword(0x1ce498c)
    """
    [32-bit Pointer] (EU) Hashmap | Audio.Vol.Music
    +0x4
    ++0x1c = [32-bit Float] Settings | Music Volume
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

    EU_HASHMAP_AUDIOVOLSFX = dword(0x1ce4ef0)
    """
    [32-bit Pointer] (EU) Hashmap | Audio.Vol.Sfx
    +0x4
    ++0x1c = [32-bit Float] Settings | SFX Volume
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
    ++0x1c = [32-bit] Trigger.Collector
    --- 0xffffffff = Untriggered
    """

    EU_HASHMAP_QWHEALTH = dword(0x1ce5110)
    """
    [32-bit Pointer] (EU) Hashmap | Q.WHealth
    +0x4
    ++0x1c = [32-bit] Game Option | Worm Health
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

    EU_HASHMAP_QWCHANCE = dword(0x1ce5364)
    """
    [32-bit Pointer] (EU) Hashmap | Q.WChance
    +0x4
    ++0x1c = [32-bit] Game Option | Weapon Crate Chance
    """

    EU_HASHMAP_QOBJ = dword(0x1ce5398)
    """
    [32-bit Pointer] (EU) Hashmap | Q.Obj
    +0x4
    ++0x1c = [32-bit] Game Option | Objects
    --- 0x0 = None Active
    --- 0x1 = Mine Only
    --- 0x2 = Oil Drum Only
    --- 0x3 = All Active
    """

    EU_HASHMAP_FELANDSOBJECTS = dword(0x1ce53dc)
    """
    [32-bit Pointer] (EU) Hashmap | FE.Land.SObjects
    +0x4
    ++0x1c = [32-bit] Landscape Selection | Small Objects
    --- 0x0 = 0%
    --- 0x1 = 33%
    --- 0x2 = 67%
    --- 0x3 = 100%
    """

    EU_HASHMAP_FELANDLOBJECTS = dword(0x1ce541c)
    """
    [32-bit Pointer] (EU) Hashmap | FE.Land.LObjects
    +0x4
    ++0x1c = [32-bit] Landscape Selection | Object Quantity
    --- 0x0 = 0%
    --- 0x1 = 33%
    --- 0x2 = 67%
    --- 0x3 = 100%
    """

    EU_HASHMAP_AUDIOVOLAMBIENT = dword(0x1ce5420)
    """
    [32-bit Pointer] (EU) Hashmap | Audio.Vol.Ambient
    +0x4
    ++0x1c = [32-bit Float] Settings | Ambient Volume
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

    EU_HASHMAP_ROUNDTIME = dword(0x1ce5544)
    """
    [32-bit Pointer] (EU) Hashmap | RoundTime
    +0x4
    ++0x1c = [32-bit] Ingame | Initial Round Time
    --- Time measured in milliseconds
    """

    EU_HASHMAP_FELANDSIZE = dword(0x1ce5554)
    """
    [32-bit Pointer] (EU) Hashmap | FE.Land.Size
    +0x4
    ++0x1c = [32-bit] Landscape Selection | Land Block Size
    --- 0x0 = 0%
    --- 0x1 = 17%
    --- 0x2 = 33%
    --- 0x3 = 50%
    --- 0x4 = 67%
    --- 0x5 = 83%
    --- 0x6 = 100%
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
    +++0x0 = [9 bytes BE ASCII] Level ID String
    ---  0x46452e4c6576656c2e = "FE.Level."
    +++0x9 = [ASCII] Level ID Discriminator
    """

    EU_HASHMAP_QRTIME = dword(0x1ce5644)
    """
    [32-bit Pointer] (EU) Hashmap | Q.RTime
    +0x4
    ++0x1c = [32-bit] Game Option | Round Time
    --- Values measured in milliseconds
    --- 0x0 = 0 Minutes
    --- 0x493e0 = 5 Minutes
    --- 0x927c0 = 10 Minutes
    --- 0xdbba0 = 15 Minutes
    --- 0x124f80 = 20 Minutes
    --- 0x16e360 = 25 Minutes
    --- 0x1b7740 = 30 Minutes
    """

    EU_HASHMAP_QHCRATE = dword(0x1ce56b4)
    """
    [32-bit Pointer] (EU) Hashmap | Q.HCrate
    +0x4
    ++0x1c = [32-bit] Game Option | Health Amount
    """

    EU_HASHMAP_SAVELANGUAGE = dword(0x1ce57a4)
    """
    [32-bit Pointer] (EU) Hashmap | SAVE.Language
    +0x4
    ++0x1c = [32-bit] Selected Language
    -- 0x0 = English
    -- 0x3 = French
    -- 0x4 = German
    -- 0x5 = Italian
    -- 0x9 = Spanish
    """

    EU_HASHMAP_LSLOVER = dword(0x1ce5858)
    """
    [32-bit Pointer] (EU) Hashmap | L.S.Lover
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Voice: French Lover
    """

    EU_HASHMAP_QSTOCK = dword(0x1ce593c)
    """
    [32-bit Pointer] (EU) Hashmap | Q.Stock
    +0x4
    ++0x1c = [32-bit]  Game Option | Stockpiling
    --- 0x0 = Inactive
    --- 0x1 = Active
    --- 0x2 = Anti
    """

    EU_HASHMAP_FELANDHEIGHT = dword(0x1ce5980)
    """
    [32-bit Pointer] (EU) Hashmap | FE.Land.Height
    +0x4
    ++0x1c = [32-bit] Landscape Selection | Land Height
    --- 0x0 = 0%
    --- 0x1 = 25%
    --- 0x2 = 50%
    --- 0x3 = 75%
    --- 0x4 = 100%
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

    EU_HASHMAP_QWSEL = dword(0x1ce5b80)
    """
    [32-bit Pointer] (EU) Hashmap | Q.WSel
    +0x4
    ++0x1c = [32-bit Boolean] Game Option | Worm Select
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

    EU_HASHMAP_FELANDBRIDGES = dword(0x1ce5cfc)
    """
    [32-bit Pointer] (EU) Hashmap | FE.Land.Bridges
    +0x4
    ++0x1c = [32-bit] Landscape Selection | Bridges
    --- 0x0 = 0%
    --- 0x1 = 33%
    --- 0x2 = 67%
    --- 0x3 = 100%
    """

    EU_HASHMAP_CRATEINDEX = dword(0x1ce5d90)
    """
    [32-bit Pointer] (EU) Hashmap | Crate.Index
    +0x4
    ++0x1c = [32-bit] Crate Index used to spawn crates in missions
    """

    EU_HASHMAP_GAMELOGICCURRENTSCRIPT = dword(0x1ce5da0)
    """
    [32-bit Pointer] (EU) Hashmap | GameLogic.CurrentScript
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

    EU_HASHMAP_FELANDAMOUNT = dword(0x1ce6090)
    """
    [32-bit Pointer] (EU) Hashmap | FE.Land.Amount
    +0x4
    ++0x1c = [32-bit] Landscape Selection | Land Amount
    --- 0x0 = 0%
    --- 0x1 = 14%
    --- 0x2 = 29%
    --- 0x3 = 43%
    --- 0x4 = 57%
    --- 0x5 = 71%
    --- 0x6 = 86%
    --- 0x7 = 100%
    """

    EU_HASHMAP_FEWORMPOTREEL1 = dword(0x1ce60b8)
    """
    [32-bit Pointer] (EU) Hashmap | FE.Wormpot.Reel1
    +0x4
    ++0x1c = [32-bit] Wormpot | Reel 1
    --- 0x0 = Crates Everywhere
    --- 0x2 = Super Animal Weapons
    --- 0x3 = Super Firearms
    --- 0x4 = Super Explosives
    --- 0x5 = Super Hand to Hand Combat
    --- 0x6 = Super Cluster Weapons
    --- 0x7 = Energy or Enemy
    --- 0x8 = Max Fall Damage
    --- 0x9 = Power Cluster Weapons
    --- 0xa = Power Explosives
    --- 0xb = Power Firearms
    --- 0xc = Power Hand to Hand
    --- 0xf = Max Health Drops
    --- 0x10 = No Retreat, No Surrender
    --- 0x11 = Nothing
    --- 0x13 = Worms Only Drown
    --- 0x14 = Power Animals
    --- 0x15 = Specialist Worms
    --- 0x17 = X2 Damage
    --- 0x18 = Wind Affects Weapons
    --- 0x1a = Crate Drops Only
    """

    EU_HASHMAP_FEWORMPOTREEL2 = dword(0x1ce60bc)
    """
    [32-bit Pointer] (EU) Hashmap | FE.Wormpot.Reel2
    +0x4
    ++0x1c = [32-bit] Wormpot | Reel 2
    --- 0x0 = Crates Everywhere
    --- 0x2 = Super Animal Weapons
    --- 0x3 = Super Firearms
    --- 0x4 = Super Explosives
    --- 0x5 = Super Hand to Hand Combat
    --- 0x6 = Super Cluster Weapons
    --- 0x7 = Energy or Enemy
    --- 0x8 = Max Fall Damage
    --- 0x9 = Power Cluster Weapons
    --- 0xa = Power Explosives
    --- 0xb = Power Firearms
    --- 0xc = Power Hand to Hand
    --- 0xf = Max Health Drops
    --- 0x10 = No Retreat, No Surrender
    --- 0x11 = Nothing
    --- 0x13 = Worms Only Drown
    --- 0x14 = Power Animals
    --- 0x15 = Specialist Worms
    --- 0x17 = X2 Damage
    --- 0x18 = Wind Affects Weapons
    --- 0x1a = Crate Drops Only
    """

    EU_HASHMAP_LANDFILE = dword(0x1ce60e8)
    """
    [32-bit Pointer] (EU) Hashmap | Land.File
    +0x4
    ++0x1c = [32-bit Pointer] Loaded .XOM Land Filename
    """

    EU_HASHMAP_FEWORMPOTREEL3 = dword(0x1ce60f0)
    """
    [32-bit Pointer] (EU) Hashmap | FE.Wormpot.Reel3
    +0x4
    ++0x1c = [32-bit] Wormpot | Reel 3
    --- 0x0 = Crates Everywhere
    --- 0x2 = Super Animal Weapons
    --- 0x3 = Super Firearms
    --- 0x4 = Super Explosives
    --- 0x5 = Super Hand to Hand Combat
    --- 0x6 = Super Cluster Weapons
    --- 0x7 = Energy or Enemy
    --- 0x8 = Max Fall Damage
    --- 0x9 = Power Cluster Weapons
    --- 0xa = Power Explosives
    --- 0xb = Power Firearms
    --- 0xc = Power Hand to Hand
    --- 0xf = Max Health Drops
    --- 0x10 = No Retreat, No Surrender
    --- 0x11 = Nothing
    --- 0x13 = Worms Only Drown
    --- 0x14 = Power Animals
    --- 0x15 = Specialist Worms
    --- 0x17 = X2 Damage
    --- 0x18 = Wind Affects Weapons
    --- 0x1a = Crate Drops Only
    """

    EU_HASHMAP_LSCHPRO = dword(0x1ce61bc)
    """
    [32-bit Pointer] (EU) Hashmap | L.Sch.Pro
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Scheme: Pro
    """

    EU_HASHMAP_QWATER = dword(0x1ce6348)
    """
    [32-bit Pointer] (EU) Hashmap | Q.Water
    +0x4
    ++0x1c = [32-bit] Game Option | Sudden Death Water Setting
    --- 0x0 = Inactive
    --- 0x1 = Slow Speed
    --- 0x2 = Medium Speed
    --- 0x3 = Fast Speed
    """

    EU_HASHMAP_LLHIGH = dword(0x1ce6370)
    """
    [32-bit Pointer] (EU) Hashmap | L.L.High
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: High Stakes
    """

    EU_HASHMAP_QMFUSE = dword(0x1ce6374)
    """
    [32-bit Pointer] (EU) Hashmap | Q.MFuse
    +0x4
    ++0x1c = [32-bit] Game Option | Mine Fuse Setting
    --- 0x0 = Instant
    --- 0x1 = Random
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

    EU_HASHMAP_QSDEATH = dword(0x1ce6850)
    """
    [32-bit Pointer] (EU) Hashmap | Q.SDeath
    +0x4
    ++0x1c = [32-bit] Game Option | Sudden Death
    --- 0x0 = Round Time Expiry Triggers Sudden Death
    --- 0x1 = 1 Health Point Sudden Death
    --- 0x2 = Sudden Death Rises Water
    --- 0x3 = No Sudden Death
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

    EU_HASHMAP_TURNTIME = dword(0x1ce6a74)
    """
    [32-bit Pointer] (EU) Hashmap | TurnTime
    +0x4
    ++0x1c = [32-bit] Ingame | Turn Time Setting
    --- Time measured in milliseconds
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

    EU_HASHMAP_TRIGGERINDEX = dword(0x1ce6d00)
    """
    [32-bit Pointer] (EU) Hashmap | Trigger.Index
    +0x4
    ++0x1c = [32-bit] Last Triggered Index
    """

    EU_HASHMAP_MCALASTGAMETIME = dword(0x1ce6de8)
    """
    [32-bit Pointer] (EU) Hashmap | MCa.LastGameTime
    +0x4
    ++0x1c = [32-bit] Received medal or challenge time
    --- In Campaign:
    --- 0x0 = None
    --- 0x1 = Bronze
    --- 0x2 = Silver
    --- 0x3 = Gold
    --- In Challenge: Time measured in milliseconds
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

    EU_HASHMAP_FELANDREALSEED = dword(0x1ce6f00)
    """
    [32-bit Pointer] (EU) Hashmap | FE.Land.RealSeed
    +0x4
    ++0x1c = [32-bit] Landscape Selection | Landscape Seed
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

    EU_HASHMAP_FELANDIND = dword(0x1ce722c)
    """
    [32-bit Pointer] (EU) Hashmap | FE.Land.Ind
    +0x4
    ++0x1c = [32-bit Boolean] Landscape Selection | Indestructable Terrain
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

    EU_HASHMAP_QWINS = dword(0x1ce72ac)
    """
    [32-bit Pointer] (EU) Hashmap | Q.Wins
    +0x4
    ++0x1c = [32-bit] Game Option | Number of Round Wins
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

    EU_HASHMAP_QTTIME = dword(0x1ce76a4)
    """
    [32-bit Pointer] (EU) Hashmap | Q.TTime
    +0x4
    ++0x1c = [32-bit] Game Option | Turn Time
    --- Time measured in milliseconds
    --- 0x3a98 = 15 Seconds
    --- 0x4e20 = 20 Seconds
    --- 0x7530 = 30 Seconds
    --- 0xafc8 = 45 Seconds
    --- 0xea60 = 60 Seconds
    --- 0x15f90 = 90 Seconds
    """

    EU_HASHMAP_ROUNDTIMEREMAINING = dword(0x1ce776c)
    """
    [32-bit Pointer] (EU) Hashmap | RoundTimeRemaining
    +0x4
    ++0x1c = [32-bit] Ingame | Round Time Remaining
    --- Time measured in milliseconds
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
    ++++0x18 = [32-bit] Array Size
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
    ------ Campaign array is populated as missions are unlocked, that means we need to check the array size before accessing certain missions otherwise the pointer will point to garbage data
    ++++++0x18 = [32-bit] Array Size
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

    US_HASHMAP_QWATER = dword(0x1cfb7f8)
    """
    [32-bit Pointer] (US) Hashmap | Q.Water
    +0x4
    ++0x1c = [32-bit] Game Option | Sudden Death Water Setting
    --- 0x0 = Inactive
    --- 0x1 = Slow Speed
    --- 0x2 = Medium Speed
    --- 0x3 = Fast Speed
    """

    US_HASHMAP_LLGRAVEYARD = dword(0x1cfb808)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Graveyard
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Grave Danger
    """

    US_HASHMAP_TRIGGERINDEX = dword(0x1cfb850)
    """
    [32-bit Pointer] (US) Hashmap | Trigger.Index
    +0x4
    ++0x1c = [32-bit] Last Triggered Index
    """

    US_HASHMAP_FELANDIND = dword(0x1cfb8dc)
    """
    [32-bit Pointer] (US) Hashmap | FE.Land.Ind
    +0x4
    ++0x1c = [32-bit Boolean] Landscape Selection | Indestructable Terrain
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

    US_HASHMAP_AUDIOVOLMUSIC = dword(0x1cfbd7c)
    """
    [32-bit Pointer] (US) Hashmap | Audio.Vol.Music
    +0x4
    ++0x1c = [32-bit Float] Settings | Music Volume
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

    US_HASHMAP_QSTOCK = dword(0x1cfbf20)
    """
    [32-bit Pointer] (US) Hashmap | Q.Stock
    +0x4
    ++0x1c = [32-bit]  Game Option | Stockpiling
    --- 0x0 = Inactive
    --- 0x1 = Active
    --- 0x2 = Anti
    """

    US_HASHMAP_QRTIME = dword(0x1cfbf44)
    """
    [32-bit Pointer] (US) Hashmap | Q.RTime
    +0x4
    ++0x1c = [32-bit] Game Option | Round Time
    --- Values measured in milliseconds
    --- 0x0 = 0 Minutes
    --- 0x493e0 = 5 Minutes
    --- 0x927c0 = 10 Minutes
    --- 0xdbba0 = 15 Minutes
    --- 0x124f80 = 20 Minutes
    --- 0x16e360 = 25 Minutes
    --- 0x1b7740 = 30 Minutes
    """

    US_HASHMAP_QWCHANCE = dword(0x1cfbf84)
    """
    [32-bit Pointer] (US) Hashmap | Q.WChance
    +0x4
    ++0x1c = [32-bit] Game Option | Weapon Crate Chance
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

    US_HASHMAP_ROUNDTIMEREMAINING = dword(0x1cfc458)
    """
    [32-bit Pointer] (US) Hashmap | RoundTimeRemaining
    +0x4
    ++0x1c = [32-bit] Ingame | Round Time Remaining
    --- Time measured in milliseconds
    """

    US_HASHMAP_LWNUKE = dword(0x1cfc460)
    """
    [32-bit Pointer] (US) Hashmap | L.W.Nuke
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Weapon: Nuclear Bomb
    """

    US_HASHMAP_QDTIME = dword(0x1cfc708)
    """
    [32-bit Pointer] (US) Hashmap | Q.DTime
    +0x4
    ++0x1c = [32-bit Boolean] Game Option | Round Time Display
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

    US_HASHMAP_DATATEAMBARRACKS = dword(0x1cfcb3c)
    """
    [32-bit Pointer] (US) Hashmap | DATA.TeamBarracks
    +0x4
    ++0x1c = [32-bit Pointer] TeamDataColective

    +++0x14 = [32-bit Pointer] XomContainerArray | High Scores
    ++++0x18 = [32-bit] Array Size
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
    ------ Campaign array is populated as missions are unlocked, that means we need to check the array size before accessing certain missions otherwise the pointer will point to garbage data
    ++++++0x18 = [32-bit] Array Size
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

    US_HASHMAP_QSDEATH = dword(0x1cfd150)
    """
    [32-bit Pointer] (US) Hashmap | Q.SDeath
    +0x4
    ++0x1c = [32-bit] Game Option | Sudden Death
    --- 0x0 = Round Time Expiry Triggers Sudden Death
    --- 0x1 = 1 Health Point Sudden Death
    --- 0x2 = Sudden Death Rises Water
    --- 0x3 = No Sudden Death
    """

    US_HASHMAP_LSCHSNIPING = dword(0x1cfd250)
    """
    [32-bit Pointer] (US) Hashmap | L.Sch.Sniping
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Scheme: Sniper
    """

    US_HASHMAP_QHCHANCE = dword(0x1cfd2c4)
    """
    [32-bit Pointer] (US) Hashmap | Q.HChance
    +0x4
    ++0x1c = [32-bit] Game Option | Health Crate Chance
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

    US_HASHMAP_MCABESTGOLD = dword(0x1cfd688)
    """
    [32-bit Pointer] (US) Hashmap | MCa.BestGold
    +0x4
    ++0x1c = [32-bit] Gold time record in milliseconds of selected challenge
    """

    US_HASHMAP_ROUNDTIME = dword(0x1cfd744)
    """
    [32-bit Pointer] (US) Hashmap | RoundTime
    +0x4
    ++0x1c = [32-bit] Ingame | Initial Round Time
    --- Time measured in milliseconds
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

    US_HASHMAP_FELANDSOBJECTS = dword(0x1cfd8fc)
    """
    [32-bit Pointer] (US) Hashmap | FE.Land.SObjects
    +0x4
    ++0x1c = [32-bit] Landscape Selection | Small Objects
    --- 0x0 = 0%
    --- 0x1 = 33%
    --- 0x2 = 67%
    --- 0x3 = 100%
    """

    US_HASHMAP_FELANDLOBJECTS = dword(0x1cfd93c)
    """
    [32-bit Pointer] (US) Hashmap | FE.Land.LObjects
    +0x4
    ++0x1c = [32-bit] Landscape Selection | Object Quantity
    --- 0x0 = 0%
    --- 0x1 = 33%
    --- 0x2 = 67%
    --- 0x3 = 100%
    """

    US_HASHMAP_MCAGAMEAWARDED = dword(0x1cfd9c0)
    """
    [32-bit Pointer] (US) Hashmap | MCa.GameAwarded
    +0x4
    ++0x1c = [32-bit Boolean] Game Awarded
    --- Changes to 0x1 when entering the result screen if mission successful
    """

    US_HASHMAP_TURNTIME = dword(0x1cfdb4c)
    """
    [32-bit Pointer] (US) Hashmap | TurnTime
    +0x4
    ++0x1c = [32-bit] Ingame | Turn Time Setting
    --- Time measured in milliseconds
    """

    US_HASHMAP_LLHELTER = dword(0x1cfdbb8)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Helter
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Helter Skelter
    """

    US_HASHMAP_TURNTIMEREMAINING = dword(0x1cfdccc)
    """
    [32-bit Pointer] (US) Hashmap | TurnTimeRemaining
    +0x4
    ++0x1c = [32-bit] Ingame | Turn Time Remaining
    --- Time measured in milliseconds
    """

    US_HASHMAP_QWINS = dword(0x1cfdd3c)
    """
    [32-bit Pointer] (US) Hashmap | Q.Wins
    +0x4
    ++0x1c = [32-bit] Game Option | Number of Round Wins
    """

    US_HASHMAP_LLAPPLE = dword(0x1cfdf04)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Apple
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Apple Core Island
    """

    US_HASHMAP_QWHEALTH = dword(0x1cfdf90)
    """
    [32-bit Pointer] (US) Hashmap | Q.WHealth
    +0x4
    ++0x1c = [32-bit] Game Option | Worm Health
    """

    US_HASHMAP_QWSEL = dword(0x1cfe0a0)
    """
    [32-bit Pointer] (US) Hashmap | Q.WSel
    +0x4
    ++0x1c = [32-bit Boolean] Game Option | Worm Select
    """

    US_HASHMAP_QMFUSE = dword(0x1cfe0c4)
    """
    [32-bit Pointer] (US) Hashmap | Q.MFuse
    +0x4
    ++0x1c = [32-bit] Game Option | Mine Fuse Setting
    --- 0x0 = Instant
    --- 0x1 = Random
    """

    US_HASHMAP_LLICE = dword(0x1cfe14c)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Ice
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Ice, Ice, Maybe
    """

    US_HASHMAP_LANDINITIALMAXHEIGHT = dword(0x1cfe180)
    """
    [32-bit Pointer] (US) Hashmap | Land.InitialMaxHeight
    +0x4
    ++0x1c = [32-bit Float] Current map's initial max height
    -- Unique value to each map, used in conjunction with the script name to determine the current challenge in the RP
    -- 0x44113984 = Shotgun Challenge 1
    -- 0x452b799b = Shotgun Challenge 2
    -- 0x444731d8 = Shotgun Challenge 3
    -- 0x453f9645 = Super Sheep Challenge 1
    -- 0x4415ee12 = Super Sheep Challenge 2
    -- 0x440b8bdc = Super Sheep Challenge 3
    -- 0x43e75e17 = Jet Pack Challenge 1
    -- 0x44082017 = Jet Pack Challenge 2
    -- 0x447aa8dc = Jet Pack Challenge 3
    -- 0x452b799b = Parachute Challenge 1
    -- 0x44ab25d0 = Parachute Challenge 2
    -- 0x4507f262 = Parachute Challenge 3
    -- 0x43d8a364 = Deathmatch Challenge 1
    -- 0x43c9ceab = Deathmatch Challenge 2
    -- 0x44074e83 = Deathmatch Challenge 3
    -- 0x43fa352b = Deathmatch Challenge 4
    -- 0x43cff6eb = Deathmatch Challenge 5
    -- 0x43c0b331 = Deathmatch Challenge 6
    -- 0x43f0dfac = Deathmatch Challenge 7
    -- 0x442bd166 = Deathmatch Challenge 8
    -- 0x43d4fde2 = Deathmatch Challenge 9
    -- 0x440b9c29 = Deathmatch Challenge 10
    """

    US_HASHMAP_LWBRIDGEK = dword(0x1cfe19c)
    """
    [32-bit Pointer] (US) Hashmap | L.W.BridgeK
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Weapon: Bridge Kit
    """

    US_HASHMAP_QFALL = dword(0x1cfe1a0)
    """
    [32-bit Pointer] (US) Hashmap | Q.Fall
    +0x4
    ++0x1c = [32-bit Boolean] Game Option | Fall Damage Setting
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

    US_HASHMAP_QHOT = dword(0x1cfe8c0)
    """
    [32-bit Pointer] (US) Hashmap | Q.Hot
    +0x4
    ++0x1c = [32-bit Boolean] Game Option | Hot Seat Timer
    --- Time measured in milliseconds
    --- 0x0 = 0 Seconds
    --- 0x1388 = 5 Seconds
    --- 0x2710 = 10 Seconds
    --- 0x3a98 = 15 Seconds
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

    US_HASHMAP_QTELIN = dword(0x1cfeaa8)
    """
    [32-bit Pointer] (US) Hashmap | Q.TelIn
    +0x4
    ++0x1c = [32-bit] Game Option | Placement
    --- 0x0 = Random
    --- 0x1 = Manual
    """

    US_HASHMAP_AUDIOVOLAMBIENT = dword(0x1cfec00)
    """
    [32-bit Pointer] (US) Hashmap | Audio.Vol.Ambient
    +0x4
    ++0x1c = [32-bit Float] Settings | Ambient Volume
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

    US_HASHMAP_FELANDHEIGHT = dword(0x1cfee44)
    """
    [32-bit Pointer] (US) Hashmap | FE.Land.Height
    +0x4
    ++0x1c = [32-bit] Landscape Selection | Land Height
    --- 0x0 = 0%
    --- 0x1 = 25%
    --- 0x2 = 50%
    --- 0x3 = 75%
    --- 0x4 = 100%
    """

    US_HASHMAP_MCALASTGAMETIME = dword(0x1cfee50)
    """
    [32-bit Pointer] (US) Hashmap | MCa.LastGameTime
    +0x4
    ++0x1c = [32-bit] Received medal or challenge time
    --- In Campaign:
    --- 0x0 = None
    --- 0x1 = Bronze
    --- 0x2 = Silver
    --- 0x3 = Gold
    --- In Challenge: Time measured in milliseconds
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

    US_HASHMAP_SAVELANGUAGE = dword(0x1cff5c8)
    """
    [32-bit Pointer] (US) Hashmap | SAVE.Language
    +0x4
    ++0x1c = [32-bit] Selected Language
    -- 0x0 = Unselected
    -- 0x1 = US English
    -- 0x3 = French
    """

    US_HASHMAP_LLHOLIDAY = dword(0x1cff6d4)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Holiday
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Costa Del Danger
    """

    US_HASHMAP_QUCHANCE = dword(0x1cff744)
    """
    [32-bit Pointer] (US) Hashmap | Q.UChance
    +0x4
    ++0x1c = [32-bit] Game Option | Utility Crate Chance
    """

    US_HASHMAP_FELANDREALSEED = dword(0x1cff74c)
    """
    [32-bit Pointer] (US) Hashmap | FE.Land.RealSeed
    +0x4
    ++0x1c = [32-bit] Landscape Selection | Landscape Seed
    """

    US_HASHMAP_LSCHSTICKY = dword(0x1cff914)
    """
    [32-bit Pointer] (US) Hashmap | L.Sch.Sticky
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Scheme: Sticky Wars
    """

    US_HASHMAP_JETPACKFUEL = dword(0x1cffa20)
    """
    [32-bit Pointer] (US) Hashmap | Jetpack.Fuel
    +0x4
    ++0x1c = [32-bit] Jetpack Fuel
    """

    US_HASHMAP_LLATLANTIS = dword(0x1cffb40)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Atlantis
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Atlantis Training Facility
    """

    US_HASHMAP_FELANDSIZE = dword(0x1cffb44)
    """
    [32-bit Pointer] (US) Hashmap | FE.Land.Size
    +0x4
    ++0x1c = [32-bit] Landscape Selection | Land Block Size
    --- 0x0 = 0%
    --- 0x1 = 17%
    --- 0x2 = 33%
    --- 0x3 = 50%
    --- 0x4 = 67%
    --- 0x5 = 83%
    --- 0x6 = 100%
    """

    US_HASHMAP_FELANDSPACE = dword(0x1cffb48)
    """
    [32-bit Pointer] (US) Hashmap | FE.Land.Space
    +0x4
    ++0x1c = [32-bit] Landscape Selection | Land Distance
    --- 0x0 = 0%
    --- 0x1 = 50%
    --- 0x2 = 100%
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

    US_HASHMAP_LANDFILE = dword(0x1cfff04)
    """
    [32-bit Pointer] (US) Hashmap | Land.File
    +0x4
    ++0x1c = [32-bit Pointer] Loaded .XOM Land Filename
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

    US_HASHMAP_AUDIOVOLSFX = dword(0x1cfffd0)
    """
    [32-bit Pointer] (US) Hashmap | Audio.Vol.Sfx
    +0x4
    ++0x1c = [32-bit Float] Settings | SFX Volume
    """

    US_HASHMAP_LPSTORY = dword(0x1d00014)
    """
    [32-bit Pointer] (US) Hashmap | L.P.Story
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Wormapedia: The Worms Story
    """

    US_HASHMAP_FELANDAMOUNT = dword(0x1d00040)
    """
    [32-bit Pointer] (US) Hashmap | FE.Land.Amount
    +0x4
    ++0x1c = [32-bit] Landscape Selection | Land Amount
    --- 0x0 = 0%
    --- 0x1 = 14%
    --- 0x2 = 29%
    --- 0x3 = 43%
    --- 0x4 = 57%
    --- 0x5 = 71%
    --- 0x6 = 86%
    --- 0x7 = 100%
    """

    US_HASHMAP_QOBJ = dword(0x1d00158)
    """
    [32-bit Pointer] (US) Hashmap | Q.Obj
    +0x4
    ++0x1c = [32-bit] Game Option | Objects
    --- 0x0 = None Active
    --- 0x1 = Mine Only
    --- 0x2 = Oil Drum Only
    --- 0x3 = All Active
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

    US_HASHMAP_FELANDTIME = dword(0x1d005c4)
    """
    [32-bit Pointer] (US) Hashmap | FE.Land.Time
    +0x4
    ++0x1c = [32-bit] Landscape Selection | Time of Day
    --- 0x0 = Day
    --- 0x1 = Rain
    --- 0x2 = Night
    """

    US_HASHMAP_QHCRATE = dword(0x1d00604)
    """
    [32-bit Pointer] (US) Hashmap | Q.HCrate
    +0x4
    ++0x1c = [32-bit] Game Option | Health Amount
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

    US_HASHMAP_FEWORMPOTREEL1 = dword(0x1d00864)
    """
    [32-bit Pointer] (US) Hashmap | FE.Wormpot.Reel1
    +0x4
    ++0x1c = [32-bit] Wormpot | Reel 1
    --- 0x0 = Crates Everywhere
    --- 0x2 = Super Animal Weapons
    --- 0x3 = Super Firearms
    --- 0x4 = Super Explosives
    --- 0x5 = Super Hand to Hand Combat
    --- 0x6 = Super Cluster Weapons
    --- 0x7 = Energy or Enemy
    --- 0x8 = Max Fall Damage
    --- 0x9 = Power Cluster Weapons
    --- 0xa = Power Explosives
    --- 0xb = Power Firearms
    --- 0xc = Power Hand to Hand
    --- 0xf = Max Health Drops
    --- 0x10 = No Retreat, No Surrender
    --- 0x11 = Nothing
    --- 0x13 = Worms Only Drown
    --- 0x14 = Power Animals
    --- 0x15 = Specialist Worms
    --- 0x17 = X2 Damage
    --- 0x18 = Wind Affects Weapons
    --- 0x1a = Crate Drops Only
    """

    US_HASHMAP_FEWORMPOTREEL2 = dword(0x1d00868)
    """
    [32-bit Pointer] (US) Hashmap | FE.Wormpot.Reel2
    +0x4
    ++0x1c = [32-bit] Wormpot | Reel 2
    --- 0x0 = Crates Everywhere
    --- 0x2 = Super Animal Weapons
    --- 0x3 = Super Firearms
    --- 0x4 = Super Explosives
    --- 0x5 = Super Hand to Hand Combat
    --- 0x6 = Super Cluster Weapons
    --- 0x7 = Energy or Enemy
    --- 0x8 = Max Fall Damage
    --- 0x9 = Power Cluster Weapons
    --- 0xa = Power Explosives
    --- 0xb = Power Firearms
    --- 0xc = Power Hand to Hand
    --- 0xf = Max Health Drops
    --- 0x10 = No Retreat, No Surrender
    --- 0x11 = Nothing
    --- 0x13 = Worms Only Drown
    --- 0x14 = Power Animals
    --- 0x15 = Specialist Worms
    --- 0x17 = X2 Damage
    --- 0x18 = Wind Affects Weapons
    --- 0x1a = Crate Drops Only
    """

    US_HASHMAP_FEWORMPOTREEL3 = dword(0x1d0086c)
    """
    [32-bit Pointer] (US) Hashmap | FE.Wormpot.Reel3
    +0x4
    ++0x1c = [32-bit] Wormpot | Reel 3
    --- 0x0 = Crates Everywhere
    --- 0x2 = Super Animal Weapons
    --- 0x3 = Super Firearms
    --- 0x4 = Super Explosives
    --- 0x5 = Super Hand to Hand Combat
    --- 0x6 = Super Cluster Weapons
    --- 0x7 = Energy or Enemy
    --- 0x8 = Max Fall Damage
    --- 0x9 = Power Cluster Weapons
    --- 0xa = Power Explosives
    --- 0xb = Power Firearms
    --- 0xc = Power Hand to Hand
    --- 0xf = Max Health Drops
    --- 0x10 = No Retreat, No Surrender
    --- 0x11 = Nothing
    --- 0x13 = Worms Only Drown
    --- 0x14 = Power Animals
    --- 0x15 = Specialist Worms
    --- 0x17 = X2 Damage
    --- 0x18 = Wind Affects Weapons
    --- 0x1a = Crate Drops Only
    """

    US_HASHMAP_TRIGGERCOLLECTOR = dword(0x1d009f8)
    """
    [32-bit Pointer] (US) Hashmap | Trigger.Collector
    Used in various missions to detect triggers such as Tutorial1 secret and capture point index in Hold Until Relief
    +0x04
    ++0x1c = [32-bit] Trigger.Collector
    --- 0xffffffff = Untriggered
    """

    US_HASHMAP_QLRET = dword(0x1d00ac0)
    """
    [32-bit Pointer] (US) Hashmap | Q.LRet
    +0x4
    ++0x1c = [32-bit] Game Option | Retreat Time
    --- Time measured in milliseconds
    --- 0x0 = 0 Seconds
    --- 0xbb8 = 3 Seconds
    --- 0x1388 = 5 Seconds
    --- 0x2710 = 10 Seconds
    """

    US_HASHMAP_LLRAGNA = dword(0x1d00bf4)
    """
    [32-bit Pointer] (US) Hashmap | L.L.Ragna
    +0x4
    ++0x1c = [32-bit Pointer] LockedContainer
    +++0x1c = [32-bit Boolean] Is Locked | Landscape: Ragnarok and Roll
    """

    US_HASHMAP_QTTIME = dword(0x1d00e84)
    """
    [32-bit Pointer] (US) Hashmap | Q.TTime
    +0x4
    ++0x1c = [32-bit] Game Option | Turn Time
    --- Time measured in milliseconds
    --- 0x3a98 = 15 Seconds
    --- 0x4e20 = 20 Seconds
    --- 0x7530 = 30 Seconds
    --- 0xafc8 = 45 Seconds
    --- 0xea60 = 60 Seconds
    --- 0x15f90 = 90 Seconds
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

    US_HASHMAP_FELANDBRIDGES = dword(0x1d010fc)
    """
    [32-bit Pointer] (US) Hashmap | FE.Land.Bridges
    +0x4
    ++0x1c = [32-bit] Landscape Selection | Bridges
    --- 0x0 = 0%
    --- 0x1 = 33%
    --- 0x2 = 67%
    --- 0x3 = 100%
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

    US_HASHMAP_WATERLEVEL = dword(0x1d011a0)
    """
    [32-bit Pointer] (US) Hashmap | Water.Level
    +0x4
    ++0x1c = [32-bit] Water Level
    --- 0x0 = Default level
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

