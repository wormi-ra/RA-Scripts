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

if __name__=="__main__":
    notes = unlock_notes()
    for addr, note in dict(sorted(notes.items())).items():
        print(f'N0:{hex(addr)}:"{note}"')
