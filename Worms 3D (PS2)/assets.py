from pycheevos.models.achievement import Achievement
from pycheevos.models.leaderboard import Leaderboard
from pycheevos.core.constants import AchievementType, LeaderboardFormat
from collections import OrderedDict

achievements = OrderedDict({
    610367: Achievement(
        id=610367,
        title="""Let's Go Gambling!""",
        description="""Spin the Wormpot slots machine""",
        points=1,
        badge="00000",
    ),
    610362: Achievement(
        id=610362,
        title="""Bovine Artillery""",
        description="""Unlock the Mad Cow""",
        points=5,
        badge="00000",
    ),
    610366: Achievement(
        id=610366,
        title="""When Sheeps Fly""",
        description="""Unlock the Super Sheep""",
        points=5,
        badge="00000",
    ),
    610364: Achievement(
        id=610364,
        title="""Ancient Ritual""",
        description="""Unlock the Earthquake""",
        points=5,
        badge="00000",
    ),
    610363: Achievement(
        id=610363,
        title="""The Soft Fruit of Doom""",
        description="""Unlock the Banana Bomb""",
        points=5,
        badge="00000",
    ),
    610365: Achievement(
        id=610365,
        title="""The Nuclear Test""",
        description="""Unlock the Nuclear Bomb""",
        points=10,
        badge="00000",
    ),
    610358: Achievement(
        id=610358,
        title="""Options!""",
        description="""Unlock all 5 unlockable gameplay schemes""",
        points=10,
        badge="00000",
    ),
    610359: Achievement(
        id=610359,
        title="""Super Villain""",
        description="""Unlock all 5 unlockable worm voices""",
        points=10,
        badge="00000",
    ),
    610360: Achievement(
        id=610360,
        title="""The Art of War""",
        description="""Unlock all 18 unlockable Wormapedia entries""",
        points=25,
        badge="00000",
    ),
    610361: Achievement(
        id=610361,
        title="""Globe Trotter""",
        description="""Unlock all 29 unlockable multiplayer landscapes""",
        points=50,
        badge="00000",
    ),
})

leaderboards = OrderedDict({
    163325: Leaderboard(
        id=163325,
        title="""Gold Trophy Time Tracker""",
        description="""Hold L1 and R1 for 3 seconds in the main menu to activate or deactivate the time tracker for gold trophies""",
        format=LeaderboardFormat.MILLISECS,
        lower_is_better=False,
    ),
})