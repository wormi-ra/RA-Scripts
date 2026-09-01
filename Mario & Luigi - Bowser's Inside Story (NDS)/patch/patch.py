from io import BytesIO
import struct

# from randoglobin (https://github.com/MnL-Modding/Randoglobin)
class EnemyData:
    def __init__(self, input_data):
        data = struct.unpack('<2HIxBh3HI6H2x', input_data)

        self.name      = data[0x0]
        self.script    = data[0x1]
        self.obj_id    = data[0x2]

        self.level     = data[0x3] # cap at 99
        self.HP        = data[0x4] # seemingly no cap
        self.POW       = data[0x5] # cap at 999
        self.DEF       = data[0x6] # cap at 999
        self.SPEED     = data[0x7] # cap at 999

        self.is_spiked = data[0x8] & 0x00000001 != 0
        self.is_flying = data[0x8] & 0x00000004 != 0

        self.fire_damage  = (data[0x8] >>  3) & 0b11
        self.burn_chance  = (data[0x8] >>  8) & 0b11
        self.dizzy_chance = (data[0x8] >> 10) & 0b11
        self.stat_chance  = (data[0x8] >> 12) & 0b11
        self.insta_chance = (data[0x8] >> 14) & 0b11

        self.unk0      = data[0x8] & 0x00010000 != 0
        self.unk1      = data[0x8] & 0x00020000 != 0

        self.EXP       = data[0x9] # cap at 9999
        self.coins     = data[0xA] # cap at 9999
        self.item_1    = data[0xB]
        self.rare_1    = data[0xC]
        self.item_2    = data[0xD]
        self.rare_2    = data[0xE]
    
    def pack(self):
        bitfield = sum([
            int(self.is_spiked) << 0,
            int(self.is_flying) << 2,
            self.fire_damage  <<  3,
            self.burn_chance  <<  8,
            self.dizzy_chance << 10,
            self.stat_chance  << 12,
            self.insta_chance << 14,
            int(self.unk0) << 16,
            int(self.unk1) << 17,
        ])

        return struct.pack(
            '<2HIxBh3HI6H2x',
            self.name,
            self.script,
            self.obj_id,
            self.level,
            self.HP,
            self.POW,
            self.DEF,
            self.SPEED,
            bitfield,
            self.EXP,
            self.coins,
            self.item_1,
            self.rare_1,
            self.item_2,
            self.rare_2,
        )


def challenge_medal_mode(overlay_data, monster_table_offset):
    overlay_data = BytesIO(overlay_data)
    overlay_data.seek(monster_table_offset)
    length_test = overlay_data.read()
    overlay_data.seek(monster_table_offset)
    mon_list = []
    for i in range(len(length_test) // 0x24):
        mon_list.append(EnemyData(overlay_data.read(0x24)))
    overlay_data.seek(monster_table_offset)
    for i in range(len(length_test) // 0x24):
        mon_list[i].HP = round(mon_list[i].HP * 1.5)
        mon_list[i].POW = round(min(mon_list[i].POW * 2.5, 999))
        mon_list[i].DEF = round(min(mon_list[i].DEF * 1.5, 999))
        # mon_list[i].coins = round(min(mon_list[i].coins * 1.5, 9999))
        overlay_data.write(mon_list[i].pack())
    overlay_data.seek(0)
    return overlay_data.read()

def patch_starting_item(arm9_data):
    arm9_data = BytesIO(arm9_data)
    arm9_data.seek(0x4e6dc) # Luigi's starting item
    arm9_data.write(bytes([0x50])) # Challenge Medal
    arm9_data.seek(0)
    return arm9_data.read()

def patch_medal_effect(arm9_data):
    arm9_data = BytesIO(arm9_data)
    arm9_data.seek(0x5054c) # Challenge Medal Effect
    arm9_data.write(bytes([0x0, 0x0])) # Disabled
    arm9_data.seek(0)
    return arm9_data.read()

if __name__=="__main__":
    with open("data/overlay.dec/overlay_0011.dec.bin", mode="rb") as overlay:
        monster_data = overlay.read() # overlay 11
        monster_data = challenge_medal_mode(
            monster_data,
            0x0000E074,
        )
        with open("output/overlay_0011.dec.bin", mode="wb") as overlay:
            overlay.write(monster_data)
    with open("data/arm9.dec.bin", mode="rb") as arm9:
        arm9 = arm9.read()
        arm9 = patch_starting_item(arm9)
        arm9 = patch_medal_effect(arm9)
        with open("output/arm9.dec.bin", mode="wb") as output:
            output.write(arm9)
