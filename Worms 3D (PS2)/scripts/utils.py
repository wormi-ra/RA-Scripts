import csv

def calculate_levels_hash():
    with open("data/levels.csv") as file:
        levels = {}
        for row in csv.DictReader(file):
            if row["Type"] == "Campaign":
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

def calculate_state_hash():
    values = []
    lookup = {
        # "ingame": (),
        "cutscene": (),
        "loading": (),
        "menu": (),
    }
    for i in range(0, 0xff):
        i = i & 0x5c
        if i not in values:
            values.append(i)
    for val in values:
        # if val & 0x4e == 0x2:
        #     lookup["ingame"] += (val,)
        if val & 0x40 > 0x0:
            lookup["cutscene"] += (val,)
        elif val & 0x1c > 0x0:
            lookup["loading"] += (val,)
        elif val & 0x5e == 0x0:
            lookup["menu"] += (val,)
    for k, v in lookup.items():
        display = {
            "cutscene": "🎬Watching a movie",
            "loading": "⏳Loading...",
            "menu": "🌐Main Menu"
        }
        print(f"{v}: \"{display[k]}\",")

def generate_unlocks():
    with open("data/unlocks.csv") as file:
        for row in csv.DictReader(file):
            type = {
                "Voice": "Unlock.Type.VOICE",
                "Scheme": "Unlock.Type.SCHEME",
                "Weapon": "Unlock.Type.WEAPON",
                "Challenge": "Unlock.Type.CHALLENGE",
                "Wormapedia": "Unlock.Type.WORMAPEDIA",
                "Landscape": "Unlock.Type.LANDSCAPE",
            }[row["Type"]]
            print(f"Unlock(\"{row['Container']}\", {type}),")

def generate_missions():
    groups = {
        "CAMPAIGN": [],
        "TUTORIAL": [],
        "CHALLENGE": [],
    }
    print("class Missions:")
    with open("data/levels.csv") as file:
        for row in csv.DictReader(file):
            fname = row["Filename"]
            name = row["Name"]
            slug = fname.upper()
            index = int(row["Order"])
            mtype = row["Type"].upper()
            gold = row["Gold Time"]
            if gold != "":
                gold = int(gold)
            else:
                gold = None
            land = row["Land.InitialMaxHeight"]
            if land != "":
                land = hex(int(land))
            else:
                land = None
            if mtype not in groups:
                continue
            groups[mtype].append(slug)
            print(
                f"    {slug} = Mission(\n"
                f"        index={index},\n"
                f"        mtype=GameMode.{mtype},\n"
                f"        name=\"{name}\",\n"
                f"        filename=\"{fname}\",\n"
                f"        gold={gold},\n"
                f"        land_maxheight={land},\n"
                f"        teams=[],\n"
                f"    )"
            )
    print()
    for mtype, missions in groups.items():
        print(f"    {mtype} = [\n        {",\n        ".join(missions)}\n    ]")

def print_dict(d: dict):
    print("{")
    for k, v in d.items():
        print(f"    {hex(k)}: \"{v}\",")
    print("}")

if __name__=="__main__":
    # print_dict(calculate_challenges_hash())
    # print_dict(calculate_levels_hash())
    generate_missions()
