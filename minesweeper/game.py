import logging as log

import pygame
import pygame.freetype

from minesweeper.action import Action


class Game:
    def __init__(
        self,
        font: pygame.freetype.Font,
        title_font: pygame.freetype.Font,
        screen: pygame.Surface,
    ):
        self.font = font
        self.title_font = title_font
        self.screen = screen

    def display(self):
        log.debug("displaying game")

    def handle_event(self, event: pygame.event.Event) -> Action:
        return Action.NO_OP
