import polars as pl
import json

def dump_xdata():
    with open("dump/SLES-XData-Dump.json") as file:
        sles = json.load(file)

    with open("dump/SLUS-XData-Dump.json") as file:
        slus = json.load(file)

    df_eu = pl.DataFrame(schema={
        "key": str,
        "sles": str,
    })
    hashmap = sles["hashmap"]
    for i in range(len(hashmap)):
        base_offset = 0x01ce3700
        if "key" in hashmap[i]:
            key = hashmap[i]["key"].removesuffix("%00")
            df_eu.extend(pl.DataFrame({
                "key": key,
                "sles": hex(base_offset + i * 4),
            }))

    df_us = pl.DataFrame(schema={
        "key": str,
        "slus": str,
    })
    hashmap = slus["hashmap"]
    for i in range(len(hashmap)):
        base_offset = 0x01cfb770
        if "key" in hashmap[i]:
            key = hashmap[i]["key"].removesuffix("%00")
            df_us.extend(pl.DataFrame({
                "key": key,
                "slus": hex(base_offset + i * 4),
            }))

    df = df_us.join(df_eu, on="key", how="inner", nulls_equal=True).sort("key")
    df.write_csv("data/xdata.csv")

def dump_arenas(file):
    with open(file) as file:
        arenaList = json.load(file)["arenaList"]
        for arena in arenaList:
            impl = arena["data"]["impl"]
            addr, size, name = impl["address"], impl["size"], impl["name"].removesuffix("%00")
            print(f"{hex(addr)}-{hex(addr+size)} = {name}")

if __name__=="__main__":
    # dump_xdata()
    # dump_arenas("dump/SLES-Arena-Dump.json")
    dump_arenas("dump/SLUS-Arena-Dump.json")
