from functools import reduce
import operator
from pycheevos.core.condition import ConditionList
from pycheevos.models.set import AchievementSet, Leaderboard
from pycheevos.models.achievement import Achievement
from pycheevos.core.helpers import *
from pycheevos.core.constants import *

from framework import achievement, achievement_set, leaderboard
from logic import Context, Unlock, Worms3D, XData
from data import UNLOCKS
import assets

@achievement_set(
    assets=assets,
    author="Wormi"
)
class Worms3DSet(AchievementSet):
    def __init__(self):
        super().__init__(
            game_id=21184,
            title="Worms 3D"
        )
        XData.init()

    @achievement()
    def unlock_schemes(self, ctx: Context, ach: Achievement):
        ach.add_alt(group(
            measured_if(Worms3D.check_serial(ctx)),
            Worms3D.is_ingame(ctx),
            ~Worms3D.is_in_attract(ctx),
            measured(Unlock.on_unlock_type(ctx, Unlock.Type.SCHEME))
        ))

    @achievement()
    def unlock_voices(self, ctx: Context, ach: Achievement):
        ach.add_alt(group(
            measured_if(Worms3D.check_serial(ctx)),
            Worms3D.is_ingame(ctx),
            ~Worms3D.is_in_attract(ctx),
            measured(Unlock.on_unlock_type(ctx, Unlock.Type.VOICE))
        ))

    @achievement()
    def unlock_wormapedia(self, ctx: Context, ach: Achievement):
        ach.add_alt(group(
            measured_if(Worms3D.check_serial(ctx)),
            Worms3D.is_ingame(ctx),
            ~Worms3D.is_in_attract(ctx),
            measured(Unlock.on_unlock_type(ctx, Unlock.Type.WORMAPEDIA))
        ))

    @achievement()
    def unlock_landscapes(self, ctx: Context, ach: Achievement):
        ach.add_alt(group(
            measured_if(Worms3D.check_serial(ctx)),
            Worms3D.is_ingame(ctx),
            ~Worms3D.is_in_attract(ctx),
            measured(Unlock.on_unlock_type(ctx, Unlock.Type.LANDSCAPE))
        ))

    @achievement()
    def unlock_mad_cow(self, ctx: Context, ach: Achievement):
        unlock = next(filter(lambda e: e.key == "L.W.MadCow", UNLOCKS))
        ach.add_alt(group(
            Worms3D.check_serial(ctx),
            Worms3D.is_ingame(ctx),
            ~Worms3D.is_in_attract(ctx),
            unlock.on_unlock(ctx),
        ))

    @achievement()
    def unlock_banana(self, ctx: Context, ach: Achievement):
        unlock = next(filter(lambda e: e.key == "L.W.Banana", UNLOCKS))
        ach.add_alt(group(
            Worms3D.check_serial(ctx),
            Worms3D.is_ingame(ctx),
            ~Worms3D.is_in_attract(ctx),
            unlock.on_unlock(ctx),
        ))

    @achievement()
    def unlock_earthquake(self, ctx: Context, ach: Achievement):
        unlock = next(filter(lambda e: e.key == "L.W.EQuake", UNLOCKS))
        ach.add_alt(group(
            Worms3D.check_serial(ctx),
            Worms3D.is_ingame(ctx),
            ~Worms3D.is_in_attract(ctx),
            unlock.on_unlock(ctx),
        ))

    @achievement()
    def unlock_nuke(self, ctx: Context, ach: Achievement):
        unlock = next(filter(lambda e: e.key == "L.W.Nuke", UNLOCKS))
        ach.add_alt(group(
            Worms3D.check_serial(ctx),
            Worms3D.is_ingame(ctx),
            ~Worms3D.is_in_attract(ctx),
            unlock.on_unlock(ctx),
        ))

    @achievement()
    def unlock_ssheep(self, ctx: Context, ach: Achievement):
        unlock = next(filter(lambda e: e.key == "L.W.SSheep", UNLOCKS))
        ach.add_alt(group(
            Worms3D.check_serial(ctx),
            Worms3D.is_ingame(ctx),
            ~Worms3D.is_in_attract(ctx),
            unlock.on_unlock(ctx),
        ))

if __name__=="__main__":
    Worms3DSet().save("output/")
