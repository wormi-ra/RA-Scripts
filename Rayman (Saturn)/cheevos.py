from pycheevos.core.condition import Condition
from pycheevos.models.set import AchievementSet
from pycheevos.models.achievement import Achievement
from pycheevos.core.helpers import *
from pycheevos.core.constants import *

from rich_presence import RaymanRichPresence
from logic import EntityData, LevelInfo, Rayman, delta_sources
from memory import Memory

import csv

class RaymanSet(AchievementSet):
    def __init__(self):
        super().__init__(
            game_id=20900,
            title="Rayman (Saturn)"
        )
        self.author = "Wormi"

    def clean_logic(self, conditions: list[Condition]) -> list[Condition]:
        """Removes useless AND_NEXT flags when not used in a hitcount or reset context"""
        ands = []
        for cond in conditions:
            if cond.flag == Flag.AND_NEXT:
                ands.append(cond)
                continue
            if cond.flag in [Flag.RESET_IF, Flag.PAUSE_IF] or cond.hits > 0:
                ands = []
        for and_cond in ands:
            and_cond.flag = Flag.NONE
        return conditions

    def generate(self):
        for i in range(17):
            self.add_achievement(self.cage_achievement(i))
        self.add_achievement(self.livingstone_grimace())
        self.add_achievement(self.tentacle_flower())
        self.add_achievement(self.ppw_collect_lives())
        for ach in self.achievements:
            print(ach.title)
            for group in [ach.core, ach.conditions] + ach.alts:
                self.clean_logic(group)
            if ach.author == "PyCheevos":
                ach.author = self.author
        rp = RaymanRichPresence()
        rp.generate()
        self.add_rich_presence(rp)

    def cage_achievement(self, id: int) -> Achievement:
        level = LevelInfo(id)
        return Achievement(
            id=573015 + id,
            title=f"{level.name} Cages",
            description=f"Break all 6 Electoon cages in {level.name}",
            type=AchievementType.PROGRESSION,
            points=5
        ).add_core(
            Rayman.is_ingame() &
            (delta(level.cages) == 5) &
            (level.cages == 6)
        )

    def tentacle_flower(self) -> Achievement:
        entity = EntityData(122, world_id=1)
        return Achievement(
            id=573499,
            title="Tentacle flower",
            description="Defeat the tentacle flower in Moskito's Nest",
            points=2,
        ).add_core(
            Rayman.is_ingame() &
            (Rayman.is_in_level(1, 12)) &
            entity.on_tentacle_defeat()
        )

    def livingstone_grimace(self) -> Achievement:
        cheevo = Achievement(
            id=573033,
            title="Livingstone Grimace", 
            description="Perform a grimace to scare a tall Livingstone",
            type=AchievementType.MISSABLE,
            points=1
        ).add_core([
            reset_if((delta(Memory.STATE_INGAME) == 0) & (Memory.STATE_INGAME == 1)),
            reset_if(delta(Rayman.current_map()) != Rayman.current_map()),
            Rayman.is_ingame() &
            (Rayman.current_world() == 1)
        ])
        with open('data/livingstones.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                entity, map_id = (EntityData(int(row['Entity ID']), world_id=1), int(row['Map ID']))
                cheevo.add_alt([
                    pause_if(Rayman.current_map() != map_id).with_hits(1),
                    entity.on_livingstone_grimace()
                ])
        return cheevo

    def ppw_collect_lives(self) -> Achievement:
        sources = [
            bit7(Memory.COLLECTIBLE_PINK_PLANT_WOODS_1.address),
            bit7(Memory.COLLECTIBLE_PINK_PLANT_WOODS_2.address),
            bit6(Memory.COLLECTIBLE_PINK_PLANT_WOODS_2.address),
            bit7(Memory.COLLECTIBLE_PINK_PLANT_WOODS_4_1.address),
            bit6(Memory.COLLECTIBLE_PINK_PLANT_WOODS_4_1.address),
            bit4(Memory.COLLECTIBLE_PINK_PLANT_WOODS_4_1.address),
            bit5(Memory.COLLECTIBLE_PINK_PLANT_WOODS_4_2.address),
            bit2(Memory.COLLECTIBLE_PINK_PLANT_WOODS_4_2.address),
        ]
        cheevo = Achievement(
            id = 573034,
            title="Pink Plant Woods Challenge", 
            description="Collect all 8 extra lives in Pink Plant Woods", 
            points=5
        ).add_core([
            reset_if(
                (delta(Memory.STATE_INGAME) == 0) &
                (Memory.STATE_INGAME == 1) &
                (Rayman.is_in_level(1, [1, 2, 4]))
            ),
        ]).add_alt([
            pause_if(~(Rayman.is_ingame())).with_hits(1),
            measured(delta_sources(sources, 7, 8))
        ])
        return cheevo


if __name__=="__main__":
    game_set = RaymanSet()
    game_set.generate()
    game_set.save("output/")
