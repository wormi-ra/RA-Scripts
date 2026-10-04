from pycheevos.models.achievement import Achievement
from pycheevos.models.leaderboard import Leaderboard
from pycheevos.core.constants import AchievementType, LeaderboardFormat
from collections import OrderedDict

achievements = OrderedDict({
    642019: Achievement(
        id=642019,
        title="""tutorial""",
        description="""Complete the Tutorial missions""",
        points=5,
        badge="00000",
    ),
    642020: Achievement(
        id=642020,
        title="""prog_construction""",
        description="""Complete the Construction story chapter""",
        points=10,
        badge="00000",
        type=AchievementType.PROGRESSION,
    ),
    642021: Achievement(
        id=642021,
        title="""prog_camelot""",
        description="""Complete the Camelot story chapter""",
        points=10,
        badge="00000",
        type=AchievementType.PROGRESSION,
    ),
    642022: Achievement(
        id=642022,
        title="""prog_wild_west""",
        description="""Complete the Wild West story chapter""",
        points=10,
        badge="00000",
        type=AchievementType.PROGRESSION,
    ),
    642023: Achievement(
        id=642023,
        title="""prog_arabian""",
        description="""Complete the Arabian story chapter""",
        points=10,
        badge="00000",
        type=AchievementType.PROGRESSION,
    ),
    642024: Achievement(
        id=642024,
        title="""prog_prehistoric""",
        description="""Complete the Prehistoric story chapter""",
        points=25,
        badge="00000",
        type=AchievementType.WIN_CONDITION,
    ),
    642025: Achievement(
        id=642025,
        title="""unlocks_sounds""",
        description="""Buy every Sound Banks from the shop""",
        points=5,
        badge="00000",
    ),
    642026: Achievement(
        id=642026,
        title="""unlocks_maps""",
        description="""Buy every Maps from the shop""",
        points=5,
        badge="00000",
    ),
    642027: Achievement(
        id=642027,
        title="""unlocks_hats""",
        description="""Buy every Worm Hats from the shop""",
        points=5,
        badge="00000",
    ),
    642028: Achievement(
        id=642028,
        title="""unlocks_face""",
        description="""Buy every Worm Spectacles from the shop""",
        points=5,
        badge="00000",
    ),
    642029: Achievement(
        id=642029,
        title="""unlocks_hands""",
        description="""Buy every Worm Hands from the shop""",
        points=5,
        badge="00000",
    ),
    642030: Achievement(
        id=642030,
        title="""unlocks_mustaches""",
        description="""Buy every Worm Mustaches from the shop""",
        points=5,
        badge="00000",
    ),
    642031: Achievement(
        id=642031,
        title="""unlocks_weapons""",
        description="""Buy every Weapons from the shop""",
        points=5,
        badge="00000",
    ),
    642032: Achievement(
        id=642032,
        title="""unlocks_game_styles""",
        description="""Buy every Game Styles from the shop""",
        points=5,
        badge="00000",
    ),
    642033: Achievement(
        id=642033,
        title="""unlocks_sets""",
        description="""Buy every Character Sets from the shop""",
        points=25,
        badge="00000",
    ),
    642034: Achievement(
        id=642034,
        title="""Wholesome Coins Are Worth Half a Coin""",
        description="""Obtain a reward from spinning 3 identical reels on the Wormpot""",
        points=5,
        badge="00000",
    ),
})

leaderboards = OrderedDict({
    174176: Leaderboard(
        id=174176,
        title="""Warning: Achievements Unsupported""",
        description="""Your emulator might be unsupported, please contact the set developper with a save state attached to your message""",
        format=LeaderboardFormat.VALUE,
        lower_is_better=False,
    ),
})