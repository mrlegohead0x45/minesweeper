import enum


class Action(enum.Enum):
    NO_OP = 0
    QUIT = 1
    PLAY = 2
    LEADERBOARD = 3
    HOW_TO_PLAY = 4
    MAIN_MENU = 5
    DIFFICULTY_MENU = 6
