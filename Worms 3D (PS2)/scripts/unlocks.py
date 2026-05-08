import csv

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