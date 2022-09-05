import logging as log
import random

import pygame
import pygame.freetype

from . import colours
from .action import Action
from .difficulty import EASY
from .tile import Tile

RED = (0xFF, 0, 0)
PURPLE = (114, 7, 135)


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

        number_of_tiles = self.difficulty.rows * self.difficulty.columns
        number_of_safe = number_of_tiles - self.difficulty.mines

        self.tiles = [Tile() for _ in range(number_of_safe)]
        self.tiles.extend([Tile(is_mine=True) for _ in range(self.difficulty.mines)])
        assert len(self.tiles) == number_of_tiles
        random.shuffle(self.tiles)

        i = iter(self.tiles)

        startx = 200
        starty = 80
        # TODO: calculate width from number of tiles
        width = 50
        offset = 5

        # drwa tiles
        for column in range(self.difficulty.columns):  # 0 -> n-1
            for row in range(self.difficulty.rows):
                tile = next(i)
                r = pygame.draw.rect(
                    self.screen,
                    colours.BTN_COLOUR,
                    (
                        startx + (width + offset) * column,
                        starty + (width + offset) * row,
                        width,
                        width,
                    ),
                )
                tile.rect = r

        # r = pygame.draw.rect(self.screen, colours.BTN_COLOUR, (200, 100, 440, 440))

        pygame.display.update()

    def handle_event(self, event: pygame.event.Event) -> Action:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (
                self.back_button.collidepoint(event.pos)
                and event.button == pygame.BUTTON_LEFT
            ):
                return Action.MAIN_MENU

            if event.button == pygame.BUTTON_LEFT:  # reveal
                # TODO: optimise
                for tile in self.tiles:
                    if tile.rect.collidepoint(event.pos):
                        if tile.is_mine:
                            self.show_all_mines()

            elif event.button == pygame.BUTTON_RIGHT:  # flag
                # TODO: optimise
                for tile in self.tiles:
                    if tile.rect.collidepoint(event.pos):
                        tile.is_flagged = not tile.is_flagged
                        tile.rect = pygame.draw.rect(
                            self.screen,
                            (PURPLE if tile.is_flagged else colours.BTN_COLOUR),
                            (
                                tile.rect.x,
                                tile.rect.y,
                                tile.rect.width,
                                tile.rect.width,
                            ),
                        )
                        break

        pygame.display.update()
        return Action.NO_OP

    def show_all_mines(self):
        for tile in self.tiles:
            colour = colours.BTN_COLOUR

            if tile.is_mine and not tile.is_flagged:
                colour = RED

            elif tile.is_mine and tile.is_flagged:
                colour = PURPLE

            # elif tile.is_flagged and not tile.is_mine:
            #     colour = colours.BTN_COLOUR

            tile.rect = pygame.draw.rect(
                self.screen,
                colour,
                (
                    tile.rect.x,
                    tile.rect.y,
                    tile.rect.width,
                    tile.rect.width,
                ),
            )


# 1 -> left
# 2 -> middle
# 3 -> right
# 4 -> up scroll
# 5 -> down scroll
# 6 -> back
# 7 -> forward
