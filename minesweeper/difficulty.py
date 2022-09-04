from enum import Enum

import attrs
import pygame
import pygame.freetype

from . import colours
from .action import Action


@attrs.frozen
class Difficulty:
    rows: int = attrs.field()
    columns: int = attrs.field()
    mines: int = attrs.field()


EASY = Difficulty(rows=9, columns=9, mines=10)
MEDIUM = Difficulty(rows=16, columns=16, mines=40)
HARD = Difficulty(rows=16, columns=30, mines=99)


class DifficultyMenu:
    def __init__(
        self,
        font: pygame.freetype.Font,
        title_font: pygame.freetype.Font,
        screen: pygame.Surface,
    ):
        self.font = font
        self.title_font = title_font
        self.screen = screen
        self.btns: list[tuple[pygame.Rect, Action]] = []

    def display(self):
        self.screen.fill(colours.BG_COLOUR)

    def handle_event(self, event: pygame.event.Event) -> Action:
        pass
