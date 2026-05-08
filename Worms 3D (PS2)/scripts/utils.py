import csv

def calculate_levels_hash():
    with open("data/levels.csv") as file:
        levels = {}
        for row in csv.DictReader(file):
            if row["Type"] == "Mission":
                type = 0x0
            elif row["Type"] == "Tutorial":
                type = 0x3
            else:
                continue
            name = row["Name"]
            order = int(row["Order"])
            levels[(100 * type + order)] = name
    return levels

def calculate_challenges_hash():
    with open("data/levels.csv") as file:
        levels = {}
        for row in csv.DictReader(file):
            if row["Land.InitialMaxHeight"] == "":
                continue
            name = row["Filename"]
            height = (int(row["Land.InitialMaxHeight"]))
            bytes = (int.from_bytes(name.encode()[:4]))
            levels[(height + bytes) & 0xffffffff] = row["Name"]
    return levels

def print_dict(d: dict):
    print("{")
    for k, v in d.items():
        print(f"    {hex(k)}: \"{v}\",")
    print("}")

if __name__=="__main__":
    # print_dict(calculate_challenges_hash())
    print_dict(calculate_levels_hash())

