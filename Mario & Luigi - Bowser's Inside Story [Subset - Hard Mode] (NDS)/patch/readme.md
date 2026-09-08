# How to build

### Create venv
```
python3 -m venv .venv

# On Windows
.venv\Scripts\activate

# On Linux
.venv/bin/activate
```

### Install requirements
```
pip3 install -r requirements.txt
```

### Unpack rom (Europe only)
```
mnl-nds-unpack ./path/to/the/original/rom.nds
```

### Decompile event scripts
```
mnlscript-bis-decompile
```

In `scripts\fevent\0207.py` subroutine `sub_0x46` (Line 2039) change:
```python
    set_player_stat(Actors.LUIGI, PlayerStat.GEAR_PIECE_1, 0x4001)
```

To:
```python
    set_player_stat(Actors.LUIGI, PlayerStat.GEAR_PIECE_1, 0x4050)
```

And append this line to the end of the subroutine:
```python
    add_items(0x4050, 1)
```

### Recompile event scripts
```
mnlscript-bis-compile
```

### Run Patcher
```
python3 patch.py
```

### Copy patched data back to the rom
```
cp output/overlay_0011.dec.bin data/overlay.dec/overlay_0011.dec.bin
cp output/arm9.dec.bin data/arm9.dec.bin
```

### Repack rom
```
mnl-nds-pack -r ./path/to/the/original/rom.nds -o ./output/patched_rom.nds
```
