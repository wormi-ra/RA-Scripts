// Dragon's Lair
// #ID = 1668

StageLookup = {
    0x00: "The Drawbridge",
    0x01: "The Entrance Hall",
    0x02: "The Gold Mines",
    0x03: "The Hall of the Grim Reaper",
    0x05: "The Dragon's Lair",
    0x06: "The Elevator",
    0x07: "The Treasury",
    0x08: "The Dungeon",
    0x63: "The Dragon's Lair",
}

WeaponLookup = {
    0x00: "🔪Dagger",
    0x01: "🪓Axe",
    0x02: "🔥Fireball",
}

PlayerLookup = {
    0x00: "P1",
    0x01: "P2",
}

PauseLookup = {
    0x01: "⏸️ ",
}

DigitLookup = {
    0xf6: "0",
    0xf7: "1",
    0xf8: "2",
    0xf9: "3",
    0xfa: "4",
    0xfb: "5",
    0xfc: "6",
    0xfd: "7",
    0xfe: "8",
    0xff: "9",
}

CHEAT = byte(0x032b)
STAGE = byte(0x05a9)
STAGE_PROGRESS = byte(0x05aa)
WEAPON = byte(0x05ab)
PLAYER = byte(0x0666)

HIGH_SCORE = 0x05de
P1_SCORE = 0x059d
P2_SCORE = 0x05af
LIVES = 0x05a5
GOLD = 0x05a2

function get_score(addr, length, offset = 0xf6) {
    score = 0
    digits = {
        1: 1,
        2: 10,
        3: 100,
        4: 1000,
        5: 10000,
    }
    for i in range(0, length - 1) {
        score = score + (byte(addr + i) - offset) * digits[length - i]
    }
    return score
}

function on_high_score() {
    addr = 0x05de
    dcond = true
    for i in range(0, 4) {
        dcond = dcond && byte(addr + i) < 10
    }
    cond = false
    for i in range(0, 4) {
        cond = cond || ((byte(addr + i)) != prev(byte(addr + i)) && byte(addr + i) != 0)
    }
    return dcond && cond
}

function ingame() {
    return (
        byte(0x063b) == 0 &&
        byte(0x0320) == 1 &&
        PLAYER == prev(PLAYER)
    )
}

function paused() {
    return prev(byte(0x0303)) != byte(0x0303)
}

function on_weapon_get(weapon) {
    return ingame() && prev(WEAPON) < 3 && prev(WEAPON) != weapon && WEAPON == weapon
}

leaderboard(
    title = "High Score",
    description = "Submit the highest score",
    id = 172123,
    start = on_high_score() && CHEAT == 0,
    cancel = always_false(),
    value = get_score(HIGH_SCORE, 5, offset = 0),
    submit = always_true(),
    format = "VALUE"
)

achievement(
    title = "Hack and Slash", points = 5,
    description = "Obtain the Axe weapon",
    id = 12000, badge = "11864",
    trigger = on_weapon_get(1) && CHEAT == 0
)

achievement(
    title = "A Wizard Is You", points = 5,
    description = "Obtain the Fireball weapon",
    id = 11999, badge = "11865",
    trigger = on_weapon_get(2) && CHEAT == 0
)

achievement(
    title = "The Quest for the Stolen Fortune", points = 10,
    description = "Collect the Lizard King's gold in the Treasury",
    id = 12002, badge = "11862",
    trigger = (
        ingame() &&
        STAGE == 7 &&
        get_score(GOLD, 3) > prev(get_score(GOLD, 3)) &&
        CHEAT == 0
    )
)

achievement(
    title = "The Trap for Tortured Souls", points = 10,
    description = "Defeat the prisoners and escape the Dungeon",
    id = 12001, badge = "11863",
    trigger = (
        ingame() &&
        prev(STAGE) == 8 &&
        STAGE == 6 &&
        CHEAT == 0
    )
)

achievement(
    title = "Mordroc's Castle", points = 5, type="progression",
    description = "Get past the Drawbridge and enter the Entrance Hall",
    id = 12007, badge = "11857",
    trigger = (
        ingame() &&
        prev(STAGE_PROGRESS) == 0 &&
        STAGE_PROGRESS == 1 &&
        CHEAT == 0
    )
)

achievement(
    title = "Hallway of the Big Striped Snake", points = 5, type="progression",
    description = "Defeat the Snake and leave the Entrance Hall",
    id = 12006, badge = "11858",
    trigger = (
        ingame() &&
        STAGE_PROGRESS == 1 &&
        prev(STAGE) == 1 &&
        STAGE == 6 &&
        CHEAT == 0
    )
)

achievement(
    title = "Did You Bring a Candle?", points = 10, type="progression",
    description = "Defeat the Trolls and leave the Gold Mines",
    id = 12005, badge = "11859",
    trigger = (
        ingame() &&
        STAGE_PROGRESS == 2 &&
        prev(STAGE) == 2 &&
        STAGE == 6 &&
        CHEAT == 0
    )
)

achievement(
    title = "Facing Your Faith", points = 10, type="progression",
    description = "Defeat the Grim Reaper and leave the Hall of the Grim Reaper",
    id = 12004, badge = "11860",
    trigger = (
        ingame() &&
        STAGE_PROGRESS == 3 &&
        prev(STAGE) == 3 &&
        STAGE == 6 &&
        CHEAT == 0
    )
)

achievement(
    title = "Our Hero Has Triumphed", points = 10, type="win_condition",
    description = "Defeat Singe the Dragon and rescue Princess Daphne",
    id = 12003, badge = "11861",
    trigger = (
        ingame() &&
        STAGE_PROGRESS == 5 &&
        prev(STAGE) == 5 &&
        STAGE == 0x63 &&
        CHEAT == 0
    )
)

achievement(
    title = "Daring Performance", points = 10,
    description = "Score at least 20,000 points",
    id = 11998, badge = "11866",
    trigger = ingame() && (
        prev(get_score(P1_SCORE, 5)) < 20000 && get_score(P1_SCORE, 5) >= 20000
    ) && CHEAT == 0
)

achievement(
    title = "Return to the Lair", points = 50,
    description = "Defeat Singe the Dragon and beat his high score of 89,999",
    id = 11997, badge = "11867",
    trigger = (
        STAGE == 0x63 &&
        on_high_score() &&
        get_score(HIGH_SCORE, 5, offset = 0) > 89999 &&
        CHEAT == 0
    )
)

achievement(
    title = "Into the Snake Pit", points = 10,
    description = "Defeat the Snake in the Entrance Hall using the Dagger",
    id = 11996, badge = "11868",
    trigger = (
        ingame() &&
        WEAPON == 0 &&
        prev(STAGE) == 1 &&
        trigger_when(STAGE == 6) &&
        CHEAT == 0
    )
)

achievement(
    title = "Death Plateau", points = 10,
    description = "Defeat the Trolls in the Gold Mines using the Dagger",
    id = 11995, badge = "11869",
    trigger = (
        ingame() &&
        WEAPON == 0 &&
        prev(STAGE) == 2 &&
        trigger_when(STAGE == 6) &&
        CHEAT == 0
    )
)

achievement(
    title = "Knocking at Death's Door", points = 25,
    description = "Defeat the Grim Reaper using the Dagger",
    id = 11994, badge = "11870",
    trigger = (
        ingame() &&
        WEAPON == 0 &&
        prev(STAGE) == 3 &&
        trigger_when(STAGE == 6) &&
        CHEAT == 0
    )
)

achievement(
    title = "May You Both Live Happily Ever After...", points = 25,
    description = "Defeat Singe the Dragon using the Dagger",
    id = 11993, badge = "11871",
    trigger = (
        ingame() &&
        WEAPON == 0 &&
        prev(STAGE) == 5 &&
        trigger_when(STAGE == 0x63) &&
        CHEAT == 0
    )
)

rich_presence_display("Playing Dragon's Lair")
rich_presence_conditional_display(
    ingame(),
    "{12}[{13}] Dirk the Daring is in {0} • {1} • ❤️{10}{11} • Score {2}{3}{4}{5}{6} • 💰{7}{8}{9}",
    rich_presence_lookup("Stage", byte(0x0005AA), StageLookup),
    rich_presence_lookup("Weapon", byte(0x0005AB), WeaponLookup),
    rich_presence_lookup("Digit", byte(P1_SCORE), DigitLookup),
    rich_presence_lookup("Digit", byte(P1_SCORE+1), DigitLookup),
    rich_presence_lookup("Digit", byte(P1_SCORE+2), DigitLookup),
    rich_presence_lookup("Digit", byte(P1_SCORE+3), DigitLookup),
    rich_presence_lookup("Digit", byte(P1_SCORE+4), DigitLookup),
    rich_presence_lookup("Digit", byte(GOLD), DigitLookup),
    rich_presence_lookup("Digit", byte(GOLD+1), DigitLookup),
    rich_presence_lookup("Digit", byte(GOLD+2), DigitLookup),
    rich_presence_lookup("Digit", byte(LIVES), DigitLookup),
    rich_presence_lookup("Digit", byte(LIVES+1), DigitLookup),
    rich_presence_lookup("Pause", measured(1, when=paused()), PauseLookup),
    rich_presence_lookup("Player", PLAYER, PlayerLookup)
)
