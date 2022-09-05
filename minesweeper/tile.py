import pygame
from pygame import Rect


class Tile:
    def __init__(self, rect: Rect = None, is_mine: bool = False):
        self.is_mine = is_mine
        self.rect = rect
        self.is_flagged = False
        self.mines = 0

    # def flag(self):
    #     self.is_flagged = not self.is_flagged # toggle
    #     if self.is_flagged:
    #         pygame.draw.rect()
