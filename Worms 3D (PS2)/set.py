from functools import reduce
import operator
from pycheevos.core.condition import ConditionList
from pycheevos.models.set import AchievementSet, Leaderboard
from pycheevos.models.achievement import Achievement
from pycheevos.core.helpers import *
from pycheevos.core.constants import *

from framework import achievement, achievement_set, leaderboard
from logic import Context, Controller, GameMode, Mission, Unlock, Worms3D, XData
from data import UNLOCKS, Missions
from memory import Memory
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

    @achievement(610367)
    def wormpot(self, ctx: Context, ach: Achievement):
        reels = [
            XData.get_value(ctx, key)
            for key in ["FE.Wormpot.Reel1", "FE.Wormpot.Reel2", "FE.Wormpot.Reel3"]
        ]
        ach.add_alt(group(
            Worms3D.check_serial(ctx),
            Worms3D.is_in_menu(ctx),
            *[
                # TODO: find a better way to do this in PyCheevos
                reel != delta(dword(0x1c))
                for reel in reels
            ],
        ))

    @achievement(610362)
    def unlock_mad_cow(self, ctx: Context, ach: Achievement):
        unlock = next(filter(lambda e: e.key == "L.W.MadCow", UNLOCKS))
        ach.add_alt(group(
            Worms3D.check_serial(ctx),
            Worms3D.is_ingame(ctx),
            ~Worms3D.is_in_attract(ctx),
            unlock.on_unlock(ctx),
        ))

    @achievement(610366)
    def unlock_ssheep(self, ctx: Context, ach: Achievement):
        unlock = next(filter(lambda e: e.key == "L.W.SSheep", UNLOCKS))
        ach.add_alt(group(
            Worms3D.check_serial(ctx),
            Worms3D.is_ingame(ctx),
            ~Worms3D.is_in_attract(ctx),
            unlock.on_unlock(ctx),
        ))

    @achievement(610364)
    def unlock_earthquake(self, ctx: Context, ach: Achievement):
        unlock = next(filter(lambda e: e.key == "L.W.EQuake", UNLOCKS))
        ach.add_alt(group(
            Worms3D.check_serial(ctx),
            Worms3D.is_ingame(ctx),
            ~Worms3D.is_in_attract(ctx),
            unlock.on_unlock(ctx),
        ))

    @achievement(610363)
    def unlock_banana(self, ctx: Context, ach: Achievement):
        unlock = next(filter(lambda e: e.key == "L.W.Banana", UNLOCKS))
        ach.add_alt(group(
            Worms3D.check_serial(ctx),
            Worms3D.is_ingame(ctx),
            ~Worms3D.is_in_attract(ctx),
            unlock.on_unlock(ctx),
        ))

    @achievement(610365)
    def unlock_nuke(self, ctx: Context, ach: Achievement):
        unlock = next(filter(lambda e: e.key == "L.W.Nuke", UNLOCKS))
        ach.add_alt(group(
            Worms3D.check_serial(ctx),
            Worms3D.is_ingame(ctx),
            ~Worms3D.is_in_attract(ctx),
            unlock.on_unlock(ctx),
        ))

    @achievement(610358)
    def unlock_schemes(self, ctx: Context, ach: Achievement):
        ach.add_alt(group(
            measured_if(Worms3D.check_serial(ctx)),
            Worms3D.is_ingame(ctx),
            ~Worms3D.is_in_attract(ctx),
            measured(Unlock.on_unlock_type(ctx, Unlock.Type.SCHEME))
        ))

    @achievement(610359)
    def unlock_voices(self, ctx: Context, ach: Achievement):
        ach.add_alt(group(
            measured_if(Worms3D.check_serial(ctx)),
            Worms3D.is_ingame(ctx),
            ~Worms3D.is_in_attract(ctx),
            measured(Unlock.on_unlock_type(ctx, Unlock.Type.VOICE))
        ))

    @achievement(610360)
    def unlock_wormapedia(self, ctx: Context, ach: Achievement):
        ach.add_alt(group(
            measured_if(Worms3D.check_serial(ctx)),
            Worms3D.is_ingame(ctx),
            ~Worms3D.is_in_attract(ctx),
            measured(Unlock.on_unlock_type(ctx, Unlock.Type.WORMAPEDIA))
        ))

    @achievement(610361)
    def unlock_landscapes(self, ctx: Context, ach: Achievement):
        ach.add_alt(group(
            measured_if(Worms3D.check_serial(ctx)),
            Worms3D.is_ingame(ctx),
            ~Worms3D.is_in_attract(ctx),
            measured(Unlock.on_unlock_type(ctx, Unlock.Type.LANDSCAPE))
        ))

    @leaderboard(163325)
    def gold_tracker(self, ctx: Context, lb: Leaderboard):
        for g in [lb.start, lb.cancel]:
            if len(g) == 0:
                g.append(group(always_true()))
        lb.set_submit(always_false())
        lb.add_start(group(
            Worms3D.check_serial(ctx),
            Worms3D.is_in_menu(ctx),
            reset_next_if(
                (Controller.button_pressed(ctx, Controller.Button.L1) == 0) |
                (Controller.button_pressed(ctx, Controller.Button.R1) == 0)
            ),
            (
                (Controller.button_pressed(ctx, Controller.Button.L1) == 1) &
                (Controller.button_pressed(ctx, Controller.Button.R1) == 1)
            ).with_hits(ctx.framerate * 2),
        ))
        lb.add_cancel(group(
            Worms3D.check_serial(ctx),
            Worms3D.is_in_menu(ctx),
            reset_next_if(
                (Controller.button_pressed(ctx, Controller.Button.L1) == 0) |
                (Controller.button_pressed(ctx, Controller.Button.R1) == 0)
            ),
            (
                (Controller.button_pressed(ctx, Controller.Button.L1) == 1) &
                (Controller.button_pressed(ctx, Controller.Button.R1) == 1)
            ).with_hits(ctx.framerate * 4),
        ))
        lb.add_value(group(
            measured_if(Worms3D.check_serial(ctx)),
            measured_if(XData.get_value(ctx, "MCa.CurrentMissionType") == GameMode.CHALLENGE),
            measured_if(Worms3D.is_ingame(ctx)),
            measured_if(~string_equals(Mission.current_script(ctx), "stdvs")),
            measured_if(~Worms3D.is_in_attract(ctx)),
            sub_source(XData.get_value(ctx, "ElapsedRoundTime")),
            remember(XData.get_value(ctx, "MCa.BestGold")),
            measured_if(recall() < 0x80000000),
            measured(recall() / value(10)),
        ))
        for mission in Missions.CAMPAIGN:
            lb.add_value(group(
                measured_if(Worms3D.check_serial(ctx)),
                measured_if(mission.is_loaded(ctx)),
                sub_source(XData.get_value(ctx, "ElapsedRoundTime")),
                remember(value(mission.gold)),
                measured_if(recall() < 0x80000000),
                measured(recall() / value(10)),
            ))


if __name__=="__main__":
    Worms3DSet().save("output/")
