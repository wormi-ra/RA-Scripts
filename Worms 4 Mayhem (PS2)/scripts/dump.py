import polars as pl
import json

def dump_xdata():
    with open("dump/W4M-XData-Dump.json") as file:
        sles = json.load(file)

    df = pl.DataFrame(schema={
        "key": str,
        "address": str,
    })
    hashmap = sles["hashmap"]
    for i in range(len(hashmap)):
        base_offset = 0x00de74c0
        if "key" in hashmap[i]:
            key = hashmap[i]["key"].removesuffix("\u0000")
            df.extend(pl.DataFrame({
                "key": key,
                "address": hex(base_offset + i * 4),
            }))

    df = df.sort("key")
    df.write_csv("data/xdata.csv")


if __name__=="__main__":
    dump_xdata()
