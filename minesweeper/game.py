import logging as log

import pygame
import pygame.freetype

from . import colours
from .action import Action
from .difficulty import EASY
from .tile import Tile


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
        # clear the screen
        self.screen.fill(colours.BG_COLOUR)
        # create back button in top left
        self.back_button = pygame.Rect(25, 25, 100, 50)
        pygame.draw.rect(self.screen, colours.BTN_COLOUR, self.back_button)
        self.font.render_to(self.screen, (40, 40), "Back", colours.TXT_COLOUR)

        ######################
        self.difficulty = EASY  # TODO: actually get the diffuculty
        ######################

        # make four buttons in the middle
        # self.buttons = [

        #     pygame.Rect(200, 100, 400, 400),
        #     pygame.Rect(200, 200, 400, 400),

        # pseudo
        # tiles = []

        # loop col:
        #     loop row:
        #         rect = rect(coords from row, col)
        #         append new tile(rect, random choice(true, false))

        number_of_tiles = self.difficulty.rows * self.difficulty.columns
        number_of_safe = number_of_tiles - self.difficulty.mines

        for _ in range(number_of_safe):
            pass

        r = pygame.draw.rect(self.screen, colours.BTN_COLOUR, (200, 100, 440, 440))

        pygame.display.update()

    def handle_event(self, event: pygame.event.Event) -> Action:
        return Action.NO_OP
