import csv
import random

def unlock_notes(skey):
    notes = {}
    with open("data/unlocks.csv") as file:
        for row in csv.DictReader(file):
            key = row["Key"]
            addr = int(row["Address"], 16)
            preunlocked = int(row["PreUnlocked"]) == 1
            if not key.startswith(skey):
                continue
            type, _, name = key.removeprefix("Lock.").partition(".")
            if type == "T":
                type = "Time Bonus"
            if type == "Tash":
                type = "Worm Mustache"
            if type == "Hat":
                type = "Worm Hats"
            if type == "Hands":
                type = "Worm Hands"
            if type == "Sound":
                type = "Sound Banks"
            if type == "Face":
                type = "Worm Spectacles"
            if type == "Set":
                type = "Character Sets"
            if type == "Scheme":
                type = "Game Styles"
            if type == "Weapon":
                type = "Weapons"
            if type == "Award":
                continue
            if type == "EasterEgg":
                continue
            note = f"""
[32-bit Pointer] Hashmap | {key}
+0x4
++0x1c = [32-bit Pointer] LockedContainer
+++0x20 = [32-bit] {type} | {name}{' (Pre-Unlocked)' if preunlocked else ''}
... 0x0 = Locked
... 0x1 = Available
... 0x2 = Unlocked
""".strip().replace("\n", "\\r\\n")
            notes[addr] = note
    return notes

def unlocks():
    with open("data/xdata.csv") as file:
        for row in csv.DictReader(file):
            key = row["key"]
            addr = row["address"]
            if key.startswith("Lock."):
                type, _, name = key.removeprefix("Lock.").partition(".")
                print(f"{key},{type},{addr},FALSE")


def wormpot():
    slots = (
        [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,25,26,34],
        [0,1,2,3,4,5,6,7,9,11,12,13,17,18,19,20,22,25,26,27,31,32,33,34],
        [0,1,2,3,4,5,6,7,17,18,19,20,21,22,24,25,26,28,29,30,34],
    )
    return (random.choice(slots[0]), random.choice(slots[1]), random.choice(slots[2]),)


if __name__=="__main__":
    # notes = unlock_notes("Lock.")
    # with open("output/notes.txt", "w") as file:
    #     for addr, note in dict(sorted(notes.items())).items():
    #         file.write(f'N0:{hex(addr)}:"{note}"\n')
    wins = 0
    rolls = 10000000
    times = []
    for i in range(rolls):
        a,b,c = wormpot()
        if a == b == c:
            wins += 1
    print(wins)
    print(wins / rolls)