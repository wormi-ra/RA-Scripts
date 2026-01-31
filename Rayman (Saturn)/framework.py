from pycheevos.models.set import Achievement, AchievementSet, Leaderboard
from pycheevos.core.condition import Condition
from pycheevos.core.helpers import Flag
from collections import OrderedDict

class achievement_set:
    def __init__(self, assets, author = ""):
        self.assets = assets
        self.author = author
        self.logic = OrderedDict()
        self.leaderboards = OrderedDict()
    
    def clean_logic(self, conditions: list[Condition]) -> list[Condition]:
        """Removes useless AND_NEXT flags when not used in a hitcount or reset context"""
        ands = []
        for cond in conditions:
            if cond.flag == Flag.AND_NEXT:
                ands.append(cond)
                continue
            if cond.flag in [Flag.RESET_IF, Flag.RESET_NEXT_IF, Flag.PAUSE_IF] or cond.hits > 0:
                ands = []
            if cond.flag in [Flag.NONE, Flag.TRIGGER, Flag.MEASURED_IF]:
                for and_cond in ands:
                    and_cond.flag = cond.flag
                ands = []
        return conditions

    def __call__(self, cls):
        _save = cls.save
        def save(set: AchievementSet, *args, **kwargs):
            i = 0
            for _, method in cls.__dict__.items():
                if hasattr(method, "_ach_id"):
                    if method._ach_id is None:
                        method._ach_id = 1000000 + i
                    self.logic[method._ach_id] = method
                if hasattr(method, "_lb_id"):
                    if method._lb_id is None:
                        method._lb_id = 1000000 + i
                    self.leaderboards[method._lb_id] = method
                i += 1

            for id, func in self.logic.items():
                if id in self.assets.achievements:
                    ach: Achievement = self.assets.achievements[id]
                else:
                    ach = Achievement(
                        id=id,
                        title=func.__name__,
                        description=func.__doc__,
                        points=0,
                    )
                func(set, ach)
                print(f"{ach.id}: {ach.title}")
                set.add_achievement(ach)
                for group in [ach.core, ach.conditions] + ach.alts:
                    self.clean_logic(group)
                if ach.author == "PyCheevos":
                    ach.author = self.author
            for id, func in self.leaderboards.items():
                if id in self.assets.leaderboards:
                    lb: Leaderboard = self.assets.leaderboards[id]
                else:
                    lb = Leaderboard(
                        id=id,
                        title=func.__name__,
                        description=func.__doc__,
                    )
                func(set, lb)
                print(f"{lb.id}: {lb.title}")
                set.add_leaderboard(lb)
                for group in [*lb.start, *lb.cancel, *lb.submit, *lb.value]:
                    self.clean_logic(group)
            print(f"Generated achievements: {len(set.achievements)}")
            print(f"Generated leaderboards: {len(set.leaderboards)}")
            print(f"Total points: {sum((ach.points for ach in set.achievements))}")
            return _save(set, *args, **kwargs)
        cls.save = save
        return cls


class achievement:
    def __init__(self, id: int | None = None):
        self.id = id

    def __call__(self, func):
        func._ach_id = self.id
        return func

class leaderboard:
    def __init__(self, id: int | None = None):
        self.id = id

    def __call__(self, func):
        func._lb_id = self.id
        return func
