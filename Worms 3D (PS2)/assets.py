from pycheevos.models.achievement import Achievement
from pycheevos.models.leaderboard import Leaderboard
from pycheevos.core.constants import AchievementType, LeaderboardFormat
from collections import OrderedDict

achievements = OrderedDict({
    1000000: Achievement(
        id=1000000,
        title="""[Debug] Full Unlock""",
        description="""Unlock 100%""",
        points=0,
    ),
})

leaderboards = OrderedDict({
    2000000: Leaderboard(
        id=2000000,
        title="""Gold Trophy Time Tracker""",
        description="""Hold L1 and R1 for 3 seconds in the main menu to activate or deactivate the time tracker for gold trophies""",
        format=LeaderboardFormat.MILLISECS, # Actually centiseconds
    ),
})
