from enum import Enum, auto

import pygame
from pygame import Rect


class State(Enum):
    COVERED = auto()
    OPEN = auto()
    FLAGGED = auto()


class Tile:
    def __init__(self, rect: Rect = None, is_mine: bool = False):
        self.is_mine = is_mine
        self.rect = rect
        self.is_flagged = False
        self.open = False
        self.neighbours: list[Tile] = []
        self.mines = 0
        self.state = State.COVERED

    # def flag(self):
    #     self.is_flagged = not self.is_flagged # toggle
    #     if self.is_flagged:
    #         pygame.draw.rect()
