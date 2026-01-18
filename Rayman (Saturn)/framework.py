from pycheevos.models.set import AchievementSet
from pycheevos.core.condition import Condition
from pycheevos.core.helpers import Flag
from collections import OrderedDict

class achievement_set:
    def __init__(self, assets, author = ""):
        self.assets = assets
        self.author = author
        self.logic = OrderedDict()
    
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

    def __call__(self, cls):
        _save = cls.save
        def save(set: AchievementSet, *args, **kwargs):
            for id, func in self.logic.items():
                ach = self.assets.achievements[id]
                func(set, ach)
                print(f"{id}: {ach.title}")
                set.add_achievement(ach)
                for group in [ach.core, ach.conditions] + ach.alts:
                    self.clean_logic(group)
                if ach.author == "PyCheevos":
                    ach.author = self.author
            print(f"Generated achievements: {len(set.achievements)}")
            print(f"Generated leaderboards: {len(set.leaderboards)}")
            print(f"Total points: {sum((ach.points for ach in set.achievements))}")
            return _save(set, *args, **kwargs)
        cls.save = save
        for _, method in cls.__dict__.items():
            if hasattr(method, "_ach_id"):
                self.logic[method._ach_id] = method
        return cls


class achievement:
    def __init__(self, id):
        self.id = id

    def __call__(self, func):
        func._ach_id = self.id
        return func
