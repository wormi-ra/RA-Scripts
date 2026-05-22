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
        Worms3D.init()

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

    #############################
    # Leaderboards              #
    #############################

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

    #############################
    # Leaderboards: Challenge   #
    #############################

    @leaderboard(163408)
    def leaderboard_challenge_shotgun_1(self, ctx: Context, lb: Leaderboard):
        return Missions.TARGETHUNT.generate_leaderboard(ctx, lb)

    @leaderboard(163409)
    def leaderboard_challenge_shotgun_2(self, ctx: Context, lb: Leaderboard):
        return Missions.TARGETHUNT2.generate_leaderboard(ctx, lb)

    @leaderboard(163410)
    def leaderboard_challenge_shotgun_3(self, ctx: Context, lb: Leaderboard):
        return Missions.HOMING.generate_leaderboard(ctx, lb)

    @leaderboard(163411)
    def leaderboard_challenge_sheep_1(self, ctx: Context, lb: Leaderboard):
        return Missions.SHEEP1.generate_leaderboard(ctx, lb)

    @leaderboard(163412)
    def leaderboard_challenge_sheep_2(self, ctx: Context, lb: Leaderboard):
        return Missions.SHEEP2.generate_leaderboard(ctx, lb)

    @leaderboard(163413)
    def leaderboard_challenge_sheep_3(self, ctx: Context, lb: Leaderboard):
        return Missions.TARGETHUNT4.generate_leaderboard(ctx, lb)

    @leaderboard(163414)
    def leaderboard_challenge_jetpack_1(self, ctx: Context, lb: Leaderboard):
        return Missions.CRATEFUN.generate_leaderboard(ctx, lb)

    @leaderboard(163415)
    def leaderboard_challenge_jetpack_2(self, ctx: Context, lb: Leaderboard):
        return Missions.JETPACKCHALL2.generate_leaderboard(ctx, lb)

    @leaderboard(163416)
    def leaderboard_challenge_jetpack_3(self, ctx: Context, lb: Leaderboard):
        return Missions.JETPACKCHALL3.generate_leaderboard(ctx, lb)

    @leaderboard(163417)
    def leaderboard_challenge_parachute_1(self, ctx: Context, lb: Leaderboard):
        return Missions.CHUTE1.generate_leaderboard(ctx, lb)

    @leaderboard(163418)
    def leaderboard_challenge_parachute_2(self, ctx: Context, lb: Leaderboard):
        return Missions.CHUTE2.generate_leaderboard(ctx, lb)

    @leaderboard(163419)
    def leaderboard_challenge_parachute_3(self, ctx: Context, lb: Leaderboard):
        return Missions.CHUTE3.generate_leaderboard(ctx, lb)

    @leaderboard(163420)
    def leaderboard_challenge_dm1(self, ctx: Context, lb: Leaderboard):
        return Missions.DEATHMATCH1.generate_leaderboard(ctx, lb)

    @leaderboard(163421)
    def leaderboard_challenge_dm2(self, ctx: Context, lb: Leaderboard):
        return Missions.DEATHMATCH2.generate_leaderboard(ctx, lb)

    @leaderboard(163422)
    def leaderboard_challenge_dm3(self, ctx: Context, lb: Leaderboard):
        return Missions.DEATHMATCH3.generate_leaderboard(ctx, lb)

    @leaderboard(163423)
    def leaderboard_challenge_dm4(self, ctx: Context, lb: Leaderboard):
        return Missions.DEATHMATCH4.generate_leaderboard(ctx, lb)

    @leaderboard(163424)
    def leaderboard_challenge_dm5(self, ctx: Context, lb: Leaderboard):
        return Missions.DEATHMATCH5.generate_leaderboard(ctx, lb)

    @leaderboard(163425)
    def leaderboard_challenge_dm6(self, ctx: Context, lb: Leaderboard):
        return Missions.DEATHMATCH6.generate_leaderboard(ctx, lb)

    @leaderboard(163426)
    def leaderboard_challenge_dm7(self, ctx: Context, lb: Leaderboard):
        return Missions.DEATHMATCH7.generate_leaderboard(ctx, lb)

    @leaderboard(163427)
    def leaderboard_challenge_dm8(self, ctx: Context, lb: Leaderboard):
        return Missions.DEATHMATCH8.generate_leaderboard(ctx, lb)

    @leaderboard(163428)
    def leaderboard_challenge_dm9(self, ctx: Context, lb: Leaderboard):
        return Missions.DEATHMATCH9.generate_leaderboard(ctx, lb)

    @leaderboard(163429)
    def leaderboard_challenge_dm10(self, ctx: Context, lb: Leaderboard):
        return Missions.DEATHMATCH10.generate_leaderboard(ctx, lb)

    #############################
    # Leaderboards: Missions    #
    #############################

    @leaderboard(163430)
    def leaderboard_rum(self, ctx: Context, lb: Leaderboard):
        return Missions.RUM.generate_leaderboard(ctx, lb)

    @leaderboard(163431)
    def leaderboard_cherry(self, ctx: Context, lb: Leaderboard):
        return Missions.CHERRY.generate_leaderboard(ctx, lb)

    @leaderboard(163432)
    def leaderboard_falling(self, ctx: Context, lb: Leaderboard):
        return Missions.FALLING.generate_leaderboard(ctx, lb)

    @leaderboard(163433)
    def leaderboard_beanstalk(self, ctx: Context, lb: Leaderboard):
        return Missions.BEANSTALK.generate_leaderboard(ctx, lb)

    @leaderboard(163434)
    def leaderboard_trial(self, ctx: Context, lb: Leaderboard):
        return Missions.TRIAL.generate_leaderboard(ctx, lb)

    @leaderboard(163435)
    def leaderboard_plaice(self, ctx: Context, lb: Leaderboard):
        return Missions.PLAICE.generate_leaderboard(ctx, lb)

    @leaderboard(163436)
    def leaderboard_boldly(self, ctx: Context, lb: Leaderboard):
        return Missions.BOLDLY.generate_leaderboard(ctx, lb)

    @leaderboard(163437)
    def leaderboard_countingsheep(self, ctx: Context, lb: Leaderboard):
        return Missions.COUNTINGSHEEP.generate_leaderboard(ctx, lb)

    @leaderboard(163438)
    def leaderboard_costa(self, ctx: Context, lb: Leaderboard):
        return Missions.HOLIDAY.generate_leaderboard(ctx, lb)


if __name__=="__main__":
    Worms3DSet().save("output/")
