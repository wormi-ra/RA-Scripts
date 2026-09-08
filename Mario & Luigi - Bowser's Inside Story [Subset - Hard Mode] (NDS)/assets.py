from pycheevos.models.achievement import Achievement
from pycheevos.models.leaderboard import Leaderboard
from pycheevos.core.constants import AchievementType, LeaderboardFormat
from collections import OrderedDict

achievements = OrderedDict({
    634108: Achievement(
        id=634108,
        title="""Tutorial""",
        description="""Defeat Bowser during the tutorial in Hard Mode. The Challenge Medal must stay equipped during every subsequent boss battle""",
        points=1,
        badge="00000",
    ),
})

leaderboards = OrderedDict({
})