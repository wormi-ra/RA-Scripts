import json

BASE_ADDR = 0xde74c0

if __name__=="__main__":
    output = []
    with open("data/20526-Notes.json") as file:
        notes = json.load(file)
    for note in notes:
        addr = int(note["Address"], 16)
        if addr not in range(BASE_ADDR, BASE_ADDR + 8000*4):
            continue
        offset = addr - BASE_ADDR
        lines: list[str] = note["Note"].splitlines()
        lines[0] = f"{hex(offset)} = {lines[0].replace('] Hashmap | ', '] ')}"
        for i in range(len(lines)):
            prefix = "." if lines[i][0] == "." else "+"
            lines[i] = f"{prefix * 2}{lines[i]}"
        output += lines
    with open("output/chungus.txt", "w") as file:
        file.write(
            "[32-bit Pointer] XDataResourceManager\n"
            "+0x18 = [32-bit Pointer] Pointer to Hashmap\n"
            "++0x0 = [8000x4 bytes] [Array] XDataResource Hashmap\n"
            ".. Array of 8000 32-bit pointers in a deterministic order based on their key name\n"
            ".. Should always point to $0xde74c0 with a regular PCSX2 config\n"
            ".. but some users seems to have the address shifted in some cases so we have to use this base pointer\n"
            ".. Some pointers can be null because there is more reserved slots than actual keys\n"
            ".. Dump of all keys with their associated base pointers:\n"
            ".. https://github.com/wormi-ra/RA-Scripts/blob/main/Worms%204%20Mayhem%20(PS2)/data/xdata.csv\n"
            "++|0x0 = [32-bit Pointer] XDataResourceDescriptor\n"
            "++|+0x4 = [32-bit Pointer] XDataResourceDetails\n"
            "++|++0x18 = [32-bit Pointer] Key\n"
            "++|+++0x0 = [ASCII] Key String\n"
            "++|++0x1c = [32-bit] Data\n"
            "..... Can be a pointer or a value depending on resource type\n"
            "..... Individual code notes are duplicated at $0xde74c0 - $0xdef1c0 for convenience\n"
        )
        file.write("\n".join(output))

