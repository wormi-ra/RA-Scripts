from pycheevos.core.condition import Condition
from pycheevos.models.set import AchievementSet
from pycheevos.models.achievement import Achievement
from pycheevos.core.helpers import *
from pycheevos.core.constants import *

from rich_presence import RaymanRichPresence
from logic import EntityData, LevelInfo, Rayman, delta_check, delta_sources
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
        # progression
        self.add_achievement(self.betilla_punch())
        self.add_achievement(self.betilla_hang())
        self.add_achievement(self.betilla_rings())
        self.add_achievement(self.betilla_helicopter())
        self.add_achievement(self.betilla_run())
        for i in range(8):
            self.add_achievement(self.boss_defeat(i))
        for i in range(17):
            self.add_achievement(self.cage_achievement(i))
        self.add_achievement(self.all_cages())
        # bonus
        for i in range(11):
            self.add_achievement(self.magician_levels(i))
        # challenges
        self.add_achievement(self.ppw_collect_lives())
        # freebies
        self.add_achievement(self.livingstone_grimace())
        self.add_achievement(self.tentacle_flower())
        # cleanup
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

    def all_cages(self) -> Achievement:
        sources = [
            LevelInfo(id).cages
            for id in range(17)
        ]
        return Achievement(
            id=574661,
            title=f"All Cages",
            description=f"Free every Electoons and unlock Mr Dark's Dare",
            type=AchievementType.PROGRESSION,
            points=25
        ).add_core(
            Rayman.is_ingame() &
            delta_sources(sources, 101, 102)
        )

    def magician_levels(self, id: int) -> Achievement:
        cheevos = [
            Achievement(
                id=574649,
                title=f"Pink Plant Woods Magician 1",
                description="Clear the first magician bonus level in Pink Plant Woods",
                points=5,
            ),
            Achievement(
                id=574650,
                title=f"Pink Plant Woods Magician 2",
                description="Clear the second magician bonus level in Pink Plant Woods",
                points=5,
            ),
            Achievement(
                id=574651,
                title=f"The Swamps of Forgetfulness Magician",
                description="Clear the magician bonus level in The Swamps of Forgetfulness",
                points=5,
            ),
            Achievement(
                id=574652,
                title=f"Moskito's Nest Magician",
                description="Clear the magician bonus level in Moskito's Nest",
                points=5,
            ),
            Achievement(
                id=574653,
                title=f"Bongo Hills Magician",
                description="Clear the magician bonus level in Bongo Hills",
                points=5,
            ),
            Achievement(
                id=574654,
                title=f"Allegro Presto Magician",
                description="Clear the magician bonus level in Allegro Presto",
                points=5,
            ),
            Achievement(
                id=574655,
                title=f"The Hard Rocks Magician",
                description="Clear the magician bonus level in The Hard Rocks",
                points=5,
            ),
            Achievement(
                id=574656,
                title=f"Mr Stone's Peaks Magician",
                description="Clear the magician bonus level in Mr Stone's Peaks",
                points=5,
            ),
            Achievement(
                id=574657,
                title=f"Eraser Plains Magician",
                description="Clear the magician bonus level in Eraser Plains",
                points=5,
            ),
            Achievement(
                id=574658,
                title=f"Space Mama's Crater Magician",
                description="Clear the magician bonus level in Space Mama's Crater",
                points=5,
            ),
            Achievement(
                id=574659,
                title=f"Crystal Palace Magician",
                description="Clear the magician bonus level in Crystal Palace",
                points=5,
            ),
        ]
        return cheevos[id].add_core(
            Rayman.is_ingame() &
            Rayman.is_in_level(*LevelInfo.MAGICIAN_LEVELS[id]) &
            delta_check(Memory.BONUS_LEVEL_WIN_CUTSCENE_TIMER, 0xfffe, 0x0000)
        )

    def betilla_punch(self) -> Achievement:
        return Achievement(
            id=574636,
            title="Punch Ability",
            description="Learn the punch ability",
            points=1,
            type=AchievementType.PROGRESSION
        ).add_core(
            Rayman.is_ingame() &
            Rayman.is_in_level(1, 3) &
            delta_check(bit7(Memory.RAYMAN_ABILITIES.address), 0, 1)
        )

    def betilla_hang(self) -> Achievement:
        return Achievement(
            id=574637,
            title="Hang Ability",
            description="Learn the ability to hang onto platforms",
            points=2,
            type=AchievementType.PROGRESSION
        ).add_core(
            Rayman.is_ingame() &
            Rayman.is_in_level(1, 8) &
            delta_check(bit6(Memory.RAYMAN_ABILITIES.address), 0, 1)
        )
    
    def betilla_rings(self) -> Achievement:
        return Achievement(
            id=574638,
            title="Grappling Fist Ability",
            description="Learn the ability to grapple flying rings with your fist",
            points=3,
            type=AchievementType.PROGRESSION
        ).add_core(
            Rayman.is_ingame() &
            Rayman.is_in_level(1, 17) &
            delta_check(bit0(Memory.RAYMAN_ABILITIES.address), 0, 1)
        )

    def betilla_helicopter(self) -> Achievement:
        return Achievement(
            id=574639,
            title="Helicopter Ability",
            description="Learn the helicopter abillity",
            points=4,
            type=AchievementType.PROGRESSION
        ).add_core(
            Rayman.is_ingame() &
            Rayman.is_in_level(2, 11) &
            delta_check(bit5(Memory.RAYMAN_ABILITIES.address), 0, 1)
        )

    def betilla_run(self) -> Achievement:
        return Achievement(
            id=574640,
            title="Run Ability",
            description="Learn the running ability",
            points=5,
            type=AchievementType.PROGRESSION
        ).add_core(
            Rayman.is_ingame() &
            Rayman.is_in_level(3, 11) &
            delta_check(bit7(Memory.RAYMAN_MODIFIERS.address), 0, 1)
        )

    def boss_defeat(self, id: int) -> Achievement:
        cheevos = [
            Achievement(
                id=574641,
                title=f"Bzzit Boss",
                description="Defeat Bzzit in Anguish Lagoon",
                points=5,
                type=AchievementType.PROGRESSION
            ),
            Achievement(
                id=574642,
                title=f"Moskito Boss",
                description="Defeat Moskito in Moskito's Nest",
                points=10,
                type=AchievementType.PROGRESSION
            ),
            Achievement(
                id=574643,
                title=f"Mr Sax Boss",
                description="Defeat Mr Sax in Mr Sax's Hullaballoo",
                points=10,
                type=AchievementType.PROGRESSION
            ),
            Achievement(
                id=574644,
                title=f"Mr Stone Boss",
                description="Defeat Mr Stone in Mr Stone's Peaks",
                points=10,
                type=AchievementType.PROGRESSION
            ),
            Achievement(
                id=574645,
                title=f"Pirate Mama Boss",
                description="Defeat Pirate Mama in Eraser Plains",
                points=5,
                type=AchievementType.PROGRESSION
            ),
            Achievement(
                id=574646,
                title=f"Space Mama Boss",
                description="Defeat Space Mama in Space Mama's Crater",
                points=10,
                type=AchievementType.PROGRESSION
            ),
            Achievement(
                id=574647,
                title=f"Mr Skops Boss",
                description="Defeat Mr Skops in Mr Skops' Stalactites",
                points=10,
                type=AchievementType.PROGRESSION
            ),
            Achievement(
                id=574648,
                title=f"Mr Dark Boss",
                description="Defeat Mr Dark in Mr Dark's Dare",
                points=25,
                type=AchievementType.WIN_CONDITION
            ),
        ]
        bits = [bit7, bit6, bit5, bit4, bit3, bit2, bit1, bit0]
        return cheevos[id].add_core(
            Rayman.is_ingame() &
            delta_check(bits[id](Memory.EVENTS_BOSSES_BEATEN.address), 0, 1)
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
