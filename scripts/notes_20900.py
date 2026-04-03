# Code Notes for Game ID 20900
# Source: Smart Importer Sync

from pycheevos.core.helpers import *

# 0x000000: [Notes] [1 byte] Set created with the help of PyCheevos scripts
set_created_with_the_help_of_pycheevos_scripts = byte(0x000000)
#See github below for source code and further information
#https://github.com/wormi-ra/RA-Scripts/tree/main/Rayman%20(Saturn)
#Helpful resources:
#- RayMap
#https://raym.app/maps_r1/index.html?mode=RaymanSaturnUS&folder=r1/saturn_us
#raym.app is a map viewer for every rayman games and versions, it is a great tool to identify level IDs, entity IDs and state IDs in a level
#(source: https://github.com/BinarySerializer/Ray1Map)
#- Ray1 BinarySerializer
#https://github.com/BinarySerializer/BinarySerializer.Ray1/tree/main/src/BinarySerializer.Ray1/DataTypes
#Definition of most data types used in Rayman 1, this repository mostly contains types for the PS1 and PC versions, so not guaranteed to be exact, but most types can be applied to the Saturn version
#Memory layout:
#Most static game variables and useful adresses are found in the high work RAM region (0x100000-0x1fffff)
#The low work RAM region contains entity data at adresses 0x54000 for the first world (Dream forest) and 0x4b000 for the other worlds

# 0x04b000: [28672 bytes] [Array] Entity Data
entity_data = byte(0x04b000)
#Memory range specific to world 2-6 (All except Dream Forest)
#Each entity is 112 bytes long following the same structure
#Entities are different depending on the current map loaded
#Check entity IDs on raym.app
#Calculate the address of a specific entity's property by using the following formula:
#0x4b000 + 112 * EntityId + PropertyOffset
#| [112 bytes] Entity Data Structure
#| 0x10 = [32-bit Pointer] Sprite data
#| 0x14 = [32-bit Pointer] Animation data
#| 0x18 = [32-bit Pointer] Image buffer data
#| 0x1c = [32-bit Pointer] Script related data
#| 0x20 = [32-bit Pointer] Script related data
#| 0x24 = [32-bit Pointer] Script related data
#| 0x28 = [32-bit Pointer] Script related data
#| 0x2c = [16-bit] Position X
#| 0x2e = [16-bit] Position Y
#| 0x30 = [16-bit] Entity ID
#| 0x32 = [16-bit] Camera relative pos X
#| 0x34 = [16-bit] Camera relative pos Y
#| 0x38 = [16-bit] Initial position X
#| 0x3a = [16-bit] Initial position Y
#| 0x3c = [16-bit] Velocity X
#| 0x3e = [16-bit] Velocity Y
#| 0x48 = [16-bit] Follow Y
#| 0x4a = [16-bit] Follow X
#| 0x64 = [8-bit] Animation frame
#| 0x65 = [8-bit] Animation index
#| 0x67 = [8-bit] Animation state
#| - Always use in combination with substate
#| - Check possible values in raym.app
#| 0x69 = [8-bit] Animation substate
#| 0x71 = [8-bit] Health
#| 0x7c = [8-bit] [Bitfield] Flags
#| - Bit5 = Alive
#| - Bit4 = Active
#| - Bit1 = Flip X

# 0x054000: [28672 bytes] [Array] Entity Data | Dream Forest
entity_data_dream_forest = byte(0x054000)
#Memory range specific to world 1 (Dream Forest)
#Each entity is 112 bytes long following the same structure
#Entities are different depending on the current map loaded
#Check entity IDs on raym.app
#Calculate the address of a specific entity's property by using the following formula:
#0x54000 + 112 * EntityId + PropertyOffset
#| [112 bytes] Entity Data Structure
#| 0x10 = [32-bit Pointer] Sprite data
#| 0x14 = [32-bit Pointer] Animation data
#| 0x18 = [32-bit Pointer] Image buffer data
#| 0x1c = [32-bit Pointer] Script related data
#| 0x20 = [32-bit Pointer] Script related data
#| 0x24 = [32-bit Pointer] Script related data
#| 0x28 = [32-bit Pointer] Script related data
#| 0x2c = [16-bit] Position X
#| 0x2e = [16-bit] Position Y
#| 0x30 = [16-bit] Entity ID
#| 0x32 = [16-bit] Camera relative pos X
#| 0x34 = [16-bit] Camera relative pos Y
#| 0x38 = [16-bit] Initial position X
#| 0x3a = [16-bit] Initial position Y
#| 0x3c = [16-bit] Velocity X
#| 0x3e = [16-bit] Velocity Y
#| 0x48 = [16-bit] Follow Y
#| 0x4a = [16-bit] Follow X
#| 0x64 = [8-bit] Animation frame
#| 0x65 = [8-bit] Animation index
#| 0x67 = [8-bit] Animation state
#| - Always use in combination with substate
#| - Check possible values in raym.app
#| 0x69 = [8-bit] Animation substate
#| 0x71 = [8-bit] Health
#| 0x7c = [8-bit] [Bitfield] Flags
#| - Bit5 = Alive
#| - Bit4 = Active
#| - Bit1 = Flip X

# 0x0a28b2: [16-bit] Cutscene Timer
cutscene_timer = word(0x0a28b2)

# 0x0a28e2: [8-bit] [Boolean] State | Watching Cutscene
state_watching_cutscene = byte(0x0a28e2)
#0x0 = False
#0x1 = True

# 0x18f900: [480 bytes] [Array] Level Info | Pink Plant Woods
level_info_pink_plant_woods = byte(0x18f900)
#| [20 bytes] Level Info Structure
#| 0x00 = [16-bit] Map position X
#| 0x02 = [16-bit] Map position Y
#| 0x04 = [8-bit] Map index up
#| 0x05 = [8-bit] Map index left
#| 0x06 = [8-bit] Map index down
#| 0x07 = [8-bit] Map index right
#| 0x08 = [8-bit] Cages unlocked count
#| 0x09 = [8-bit] [Bitfield] Level state
#| - Bit7 = Unlocked
#| - Bit6 = Visible
#| - Bit5 = Waiting unlock animation
#| 0x0a = [8-bit] Starting map ID
#| 0x0b = [8-bit] World ID
#| 0x1d = [8-bit] Level text color
#| 0x10 = [32-bit Pointer] Level name

# 0x18f914: [20 bytes] Level Info | Anguish Lagoon
level_info_anguish_lagoon = byte(0x18f914)

# 0x18f928: [20 bytes] Level Info | The Swamps of Forgetfulness
level_info_the_swamps_of_forgetfulness = byte(0x18f928)

# 0x18f93c: [20 bytes] Level Info | Moskito's Nest
level_info_moskitos_nest = byte(0x18f93c)

# 0x18f950: [20 bytes] Level Info | Bongo Hills
level_info_bongo_hills = byte(0x18f950)

# 0x18f964: [20 bytes] Level Info | Allegro Presto
level_info_allegro_presto = byte(0x18f964)

# 0x18f978: [20 bytes] Level Info | Gong Heights
level_info_gong_heights = byte(0x18f978)

# 0x18f98c: [20 bytes] Level Info | Mr Sax's Hullaballo
level_info_mr_saxs_hullaballo = byte(0x18f98c)

# 0x18f9a0: [20 bytes] Level Info | Twilight Gulch
level_info_twilight_gulch = byte(0x18f9a0)

# 0x18f9b4: [20 bytes] Level Info | The Hard Rocks
level_info_the_hard_rocks = byte(0x18f9b4)

# 0x18f9c8: [20 bytes] Level Info | Mr Stone's Peaks
level_info_mr_stones_peaks = byte(0x18f9c8)

# 0x18f9dc: [20 bytes] Level Info | Eraser Plains
level_info_eraser_plains = byte(0x18f9dc)

# 0x18f9f0: [20 bytes] Level Info | Pencil Pentathlon
level_info_pencil_pentathlon = byte(0x18f9f0)

# 0x18fa04: [20 bytes] Level Info | Space Mama's Crater
level_info_space_mamas_crater = byte(0x18fa04)

# 0x18fa18: [20 bytes] Level Info | Crystal Palace
level_info_crystal_palace = byte(0x18fa18)

# 0x18fa2c: [20 bytes] Level Info | Eat at Joe's
level_info_eat_at_joes = byte(0x18fa2c)

# 0x18fa40: [20 bytes] Level Info | Mr Skops' Stalactites
level_info_mr_skops_stalactites = byte(0x18fa40)

# 0x18fa54: [20 bytes] Level Info | Mr Dark's Dare
level_info_mr_darks_dare = byte(0x18fa54)

# 0x18fa68: [20 bytes] Level Info | Save 1
level_info_save_1 = byte(0x18fa68)

# 0x18fa7c: [20 bytes] Level Info | Save 2
level_info_save_2 = byte(0x18fa7c)

# 0x18fa90: [20 bytes] Level Info | Save 3
level_info_save_3 = byte(0x18fa90)

# 0x18faa4: [20 bytes] Level Info | Save 4
level_info_save_4 = byte(0x18faa4)

# 0x18fab8: [20 bytes] Level Info | Save 5
level_info_save_5 = byte(0x18fab8)

# 0x18facc: [20 bytes] Level Info | Save 6
level_info_save_6 = byte(0x18facc)

# 0x191914: [32-bit ME Pointer & 0x1fffff] Entity Data Pointer | World 1
entity_data_pointer_world_1 = dword(0x191914)
#Always point to 0x54000

# 0x191918: [32-bit ME Pointer & 0x1fffff] Entity Data Pointer | World 2
entity_data_pointer_world_2 = dword(0x191918)
#Always point to 0x4b000

# 0x19191c: [32-bit ME Pointer & 0x1fffff] Entity Data Pointer | World 3
entity_data_pointer_world_3 = dword(0x19191c)
#Always point to 0x4b000

# 0x191920: [32-bit ME Pointer & 0x1fffff] Entity Data Pointer | World 4
entity_data_pointer_world_4 = dword(0x191920)
#Always point to 0x4b000

# 0x191924: [32-bit ME Pointer & 0x1fffff] Entity Data Pointer | World 5
entity_data_pointer_world_5 = dword(0x191924)
#Always point to 0x4b000

# 0x191928: [32-bit ME Pointer & 0x1fffff] Entity Data Pointer | World 6
entity_data_pointer_world_6 = dword(0x191928)
#Always point to 0x4b000

# 0x1a4ba0: [16-bit] Ingame | Freeze Countdown
ingame_freeze_countdown = word(0x1a4ba0)
#Countdown where Rayman cannot move between respawns
#0x0000 = Unfrozen

# 0x1a4ba3: [8-bit] Ingame | Level State
ingame_level_state = byte(0x1a4ba3)
#0x0 = Playing
#0x1 = Cage breaking animation
#0x2 = Exit sign touched
#- Note: Unreliable during Dark Rayman's chase

# 0x1a4ba7: [8-bit] [Boolean] Ingame | Paused
ingame_paused = byte(0x1a4ba7)
#0x0 = False
#0x1 = True

# 0x1a4ca2: [16-bit] Bonus Level | Time Left
bonus_level_time_left = word(0x1a4ca2)
#0xfffe = disabled
#Any other value = Frames left before end of the timer

# 0x1a509e: [8-bit] Level Select | Current Level ID
level_select_current_level_id = byte(0x1a509e)
#0x00 = Pink Plant Woods
#0x01 = Anguish Lagoon
#0x02 = The Swamps of Forgetfulness
#0x03 = Moskito's Nest
#0x04 = Bongo Hills
#0x05 = Allegro Presto
#0x06 = Gong Heights
#0x07 = Mr Sax's Hullaballo
#0x08 = Twilight Gulch
#0x09 = The Hard Rocks
#0x0a = Mr Stone's Peaks
#0x0b = Eraser Plains
#0x0c = Pencil Pentathlon
#0x0d = Space Mama's Crater
#0x0e = Crystal Palace
#0x0f = Eat at Joe's
#0x10 = Mr Skops' Stalactites
#0x11 = Mr Dark's Dare
#0x12 = Save 1
#0x13 = Save 2
#0x14 = Save 3
#0x15 = Save 4
#0x16 = Save 5
#0x17 = Save 6

# 0x1a50c7: [8-bit] [Boolean] State | In Level Select
state_in_level_select = byte(0x1a50c7)
#0x0 = False
#0x1 = True

# 0x1a5b11: [8-bit] Total Cages Unlocked
total_cages_unlocked = byte(0x1a5b11)
#0x66 = All Unlocked (102)

# 0x1a5b12: [16-bit] Ingame | Frame counter
ingame_frame_counter = word(0x1a5b12)
#Pauses when rayman is not in control, in menu, during pause, breaking cages, loading...

# 0x1a5c2f: [8-bit] Bonus Level | Tings
bonus_level_tings = byte(0x1a5c2f)

# 0x1a6cc4: [16-bit] Level Select | Destination Level ID
level_select_destination_level_id = word(0x1a6cc4)
#The level ID Rayman is walking towards in the level select

# 0x1a6cc8: [8-bit] [Boolean] State | Title Screen
state_title_screen = byte(0x1a6cc8)
#0x0 = False
#0x1 = True

# 0x1a6cf0: [8-bit] [Boolean] State | Loading
state_loading = byte(0x1a6cf0)
#0x0 = False
#0x1 = True

# 0x1a6d18: [8-bit] Ingame | Current world
ingame_current_world = byte(0x1a6d18)
#0x1 = The Dream Forest
#0x2 = Band Land
#0x3 = Blue Mountains
#0x4 = Picture City
#0x5 = The Cave of Skops
#0x6 = Candy Chateau

# 0x1a6d20: Number of Lives (16-bit)
number_of_lives = word(0x1a6d20)

# 0x1a6d27: Number of Tings (8-bit)
number_of_tings = byte(0x1a6d27)

# 0x1a6d4c: [16-bit] Rayman | Position X
rayman_position_x = word(0x1a6d4c)

# 0x1a6d4e: [16-bit] Rayman | Position Y
rayman_position_y = word(0x1a6d4e)

# 0x1a6d5c: [16-bit] Rayman | Velocity X
rayman_velocity_x = word(0x1a6d5c)

# 0x1a6d5e: [16-bit] Rayman | Velocity Y
rayman_velocity_y = word(0x1a6d5e)

# 0x1a6d87: [8-bit] Rayman | Animation State
rayman_animation_state = byte(0x1a6d87)
#Always use in combination with substate
#Check possible values in raym.app

# 0x1a6d89: [8-bit] Rayman | Animation Substate
rayman_animation_substate = byte(0x1a6d89)

# 0x1a6d91: [8-bit] Rayman | Hitpoints
rayman_hitpoints = byte(0x1a6d91)
#0x0 = 1 hp
#0x1 = 2 hp
#0x2 = 3 hp
#0x3 = 4 hp
#0x4 = 5 hp

# 0x1a6d9c: [8-bit] Rayman | Flags
rayman_flags = byte(0x1a6d9c)
#Bit5 = Alive
#Bit4 = Active
#Bit1 = Flip X

# 0x1a6eb1: [8-bit] [Boolean] State | Game Over
state_game_over = byte(0x1a6eb1)
#0x0 = False
#0x1 = True
#True when on the game over screen, as well as the ending cutscene and credits

# 0x1a6f0a: [16-bit] Rayman | Respawn Position X
rayman_respawn_position_x = word(0x1a6f0a)
#Not reliable if the player uses a checkpoint, as the value can vary slightly depending on Rayman's position at the time he used the checkpoint

# 0x1a6f0c: [16-bit] Rayman | Respawn Position Y
rayman_respawn_position_y = word(0x1a6f0c)
#Can be used reliably for checkpoints

# 0x1a702b: [8-bit] [Boolean] State | Map Ready
state_map_ready = byte(0x1a702b)
#0x0 = False
#0x1 = True
#Insuring all entities in the map are loaded if value is 0x1 and level select is 0x0

# 0x1a7046: [16-bit] General | Frame counter
general_frame_counter = word(0x1a7046)
#Pauses during loading times

# 0x1a8593: [8-bit] Rayman | Continues
rayman_continues = byte(0x1a8593)
#0x5 = Starting value

# 0x1a97c1: [8-bit] [Boolean] Boss Victory Trigger
boss_victory_trigger = byte(0x1a97c1)
#0x0 = False
#0x1 = True
#Only changes when defeating bosses.
#Set to 0x1 to instantly win any level

# 0x1a97c2: [16-bit] Life Counter Screen Animation
life_counter_screen_animation = word(0x1a97c2)
#0xffff = Inactive

# 0x1a9f40: [8-bit] Loading | World
loading_world = byte(0x1a9f40)
#0x1 = The Dream Forest
#0x2 = Band Land
#0x3 = Blue Mountains
#0x4 = Picture City
#0x5 = The Cave of Skops
#0x6 = Candy Chateau

# 0x1a9ff4: [8-bit] [Boolean] State | Demo play
state_demo_play = byte(0x1a9ff4)
#0x0 = False
#0x1 = True

# 0x1ab013: [8-bit] Bonus Level | Tings left
bonus_level_tings_left = byte(0x1ab013)

# 0x1ab07f: [8-bit] [Boolean] Rayman | Is Punching
rayman_is_punching = byte(0x1ab07f)
#0x0 = False
#0x1 = True

# 0x1ab090: [16-bit] Bonus Level | Win cutscene timer
bonus_level_win_cutscene_timer = word(0x1ab090)
#0x0000 = Inactive
#0x0001 - 0x0111 = Active cutscene timer
#0xffe0 - 0xfffe = Pre-cutscene timer

# 0x1ab0a2: [8-bit] State | Current Save File
state_current_save_file = byte(0x1ab0a2)
#0x0 = Main menu
#0x1 = Save 1
#0x2 = Save 2
#0x3 = Save 3

# 0x1ab630: [16-bit] Ingame | Map Timer High
ingame_map_timer_high = word(0x1ab630)
#Frames spent playing on the current map
#Resets on death and map changes
#Add the high value with the low value together to obtain the total time as a 32-bit using the following formula:
#High * 0x10000 + Low

# 0x1ab632: [16-bit] Ingame | Map Timer Low
ingame_map_timer_low = word(0x1ab632)
#Frames spent playing on the current map
#Resets on death and map changes
#Add the high value with the low value together to obtain the total time as a 32-bit using the following formula:
#High * 0x10000 + Low

# 0x1ab662: [8-bit] Loading | Map ID
loading_map_id = byte(0x1ab662)
#Map ID specific to the current world
#Matches the ID from raym.app (eg. JUN002 = Map ID 0x02 etc.)
#Changes when loading map
#Can be unreliable?

# 0x1ab978: [8-bit] Loading | Next Map ID
loading_next_map_id = byte(0x1ab978)
#Map ID specific to the current world
#Matches the ID from raym.app (eg. JUN002 = Map ID 0x02 etc.)
#Changes when a map change is requested
#when hitting a sign for example

# 0x1ac286: [8-bit] Ingame | Map ID
ingame_map_id = byte(0x1ac286)
#Map ID specific to the current world
#Matches the ID from raym.app (eg. JUN002 = Map ID 0x02 etc.)
#Changes when the level is actually loaded

# 0x1ac2c1: [8-bit] [Bitfield] Collectible | Pink Plant Woods 1
collectible_pink_plant_woods_1 = byte(0x1ac2c1)
#Bit7 = Life

# 0x1ac2e0: [8-bit] [Bitfield] Collectible | Pink Plant Woods 2
collectible_pink_plant_woods_2 = byte(0x1ac2e0)
#Bit7 = Life
#Bit6 = Life

# 0x1ac321: [8-bit] [Bitfield] Collectible | Pink Plant Woods 4-1
collectible_pink_plant_woods_4_1 = byte(0x1ac321)
#Bit7 = Life
#Bit6 = Life
#Bit4 = Life

# 0x1ac323: [8-bit] [Bitfield] Collectible | Pink Plant Woods 4-2
collectible_pink_plant_woods_4_2 = byte(0x1ac323)
#Bit5 = Life
#Bit2 = Life

# 0x1ac7e2: [8-bit] [Bitfield] Collectible | The Hard Rocks 1-1
collectible_the_hard_rocks_1_1 = byte(0x1ac7e2)
#Bit5 = Life

# 0x1ac7e4: [8-bit] [Bitfield] Collectible | The Hard Rocks 1-2
collectible_the_hard_rocks_1_2 = byte(0x1ac7e4)
#Bit1 = Life

# 0x1ac806: [8-bit] [Bitfield] Collectible | The Hard Rocks 2
collectible_the_hard_rocks_2 = byte(0x1ac806)
#Bit1 = Life

# 0x1ac823: [8-bit] [Bitfield] Collectible | The Hard Rocks 3-2
collectible_the_hard_rocks_3_2 = byte(0x1ac823)
#Bit0 = Life

# 0x1ac825: [8-bit] [Bitfield] Collectible | The Hard Rocks 3-3
collectible_the_hard_rocks_3_3 = byte(0x1ac825)
#Bit7 = Life

# 0x1ac827: [8-bit] [Bitfield] Collectible | The Hard Rocks 3-1
collectible_the_hard_rocks_3_1 = byte(0x1ac827)
#Bit1 = Life

# 0x1acf2a: [8-bit] [Bitfield] Events | NPCs
events_npcs = byte(0x1acf2a)
#Bit7 = Unused flag that skips Bongo Hills 6
#Bit6 = Got firefly from Joe
#Bit5 = Plugged light switch in Eat at Joe's
#Bit4 = Helped Musician in Mr Stone's Peaks

# 0x1acf2b: [8-bit] [Bitfield] Events | Bosses beaten
events_bosses_beaten = byte(0x1acf2b)
#Bit7 = Bzzit
#Bit6 = Moskito
#Bit5 = Mr Sax
#Bit4 = Mr Stone
#Bit3 = Pirate Mama
#Bit2 = Space Mama
#Bit1 = Mr Skops
#- Note: this flag gets enabled at the beginning of Skop's fight instead of when he is defeated
#Bit0 = Mr Dark

# 0x1acfc4: [8-bit] [Bitfield] Rayman | Modifiers
rayman_modifiers = byte(0x1acfc4)
#Bit7 = Unlocked run ability
#Bit6 = Mini Rayman
#Bit5 = Firefly light
#Bit4 = Infinite run
#Bit3 = Begin infinite run
#Bit2 = Reverse controls (Unused?)
#Bit1 = Reverse controls
#Bit0 = Unused death animation

# 0x1acfc5: [8-bit] [Bitfield] Rayman | Abilities
rayman_abilities = byte(0x1acfc5)
#Bit7 = Punch
#Bit6 = Hang
#Bit5 = Helicopter
#Bit4 = Super helicopter
#Bit3 = Unused
#Bit2 = Unused
#Bit1 = Seed
#Bit0 = Grappling

# 0x1acfcc: [16-bit] Rayman | Helicopter timer
rayman_helicopter_timer = word(0x1acfcc)
#0xffff = not in helicopter state

# 0x1ad022: [16-bit] [Boolean] Level Transition Trigger
level_transition_trigger = word(0x1ad022)
#0x0 = False
#0x1 = True
#Switches between ingame and level select when set to 0x1
