import csv
import polars as pl


def unlock_notes():
    notes = {}
    unlocks = pl.read_csv("data/unlocks.csv")
    with open("data/xdata.csv") as file:
        for row in csv.DictReader(file):
            key = row["key"]
            if not key.startswith("L."):
                continue
            # try:
            name, type = unlocks.filter(pl.col("Key") == key).select("Name", "Type").row(0)
            # except:
            #     print(f"Key not found: {key}")
            #     continue
            for region in ["EU", "US"]:
                note = \
f"""
[32-bit Pointer] ({region}) Hashmap | {key}
+0x4
++0x1c = [32-bit Pointer] LockedContainer
+++0x1c = [32-bit Boolean] Is Locked | {type}: {name}
""".strip().replace("\n", "\\r\\n")
                addr = int({
                    "EU": row["sles"],
                    "US": row["slus"],
                }[region], 16)
                notes[addr] = note
    return notes

def level_notes():
    with open("data/levels.csv") as file:
        for row in csv.DictReader(file):
            b = (row["Filename"] + "\0").encode()
            filename = row["Filename"]
            name = row["Name"]
            print(f"\"{filename}\" = {name}")

def land_maxheight():
    with open("data/levels.csv") as file:
        for row in csv.DictReader(file):
            # b = (row["Filename"] + "\0").encode()
            height = row["Land.InitialMaxHeight"]
            if height != "":
                name = row["Name"]
                print(f"-- {hex(int(height))} = {name}")

def script_hash():
    from logic import Lua
    with open("data/levels.csv") as file:
        for row in csv.DictReader(file):
            filename = row["Filename"]
            name = row["Name"]
            print(f"{hex(int(Lua.string_hash(filename)))} = {filename} ({name})")

def landscapes():
    df = pl.read_csv("data/landscapes.csv")
    df = df.sort(pl.col("Land.InitialMaxHeight"))
    for row in df.iter_rows(named=True):
        name = row["Name"]
        h = row["Land.InitialMaxHeight"]
        print(f"--- {h} = {name}")

if __name__=="__main__":
    # notes = unlock_notes()
    # for addr, note in dict(sorted(notes.items())).items():
    #     print(f'N0:{hex(addr)}:"{note}"')
    landscapes()
