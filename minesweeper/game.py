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

        # assume 9x9 grid
        # for idx, tile in enumerate(self.tiles):
        #     if idx in [0, 8, 72, 80]: # corners
        #         # get

        # r = pygame.draw.rect(self.screen, colours.BTN_COLOUR, (200, 100, 440, 440))

        pygame.display.update()

    def handle_event(self, event: pygame.event.Event) -> Action:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (
                self.back_button.collidepoint(event.pos)
                and event.button == pygame.BUTTON_LEFT
            ):
                return Action.MAIN_MENU

            # get the tile
            tile = None
            idx = -1
            for i, t in enumerate(self.tiles):
                if t.rect.collidepoint(event.pos):
                    tile = t
                    idx = i

            if tile is None or idx == -1:
                return Action.NO_OP

            if event.button == pygame.BUTTON_LEFT:  # reveal
                if tile.is_mine:
                    self.show_all_mines()

                else:
                    # uncover all connected 0 tiles and their adjacent ones
                    if idx == 0:  # tl corner
                        pass
                    elif idx == 8:  # tr corner
                        pass
                    elif idx == 72:  # bl corner
                        pass
                    elif idx == 80:  # br corner
                        pass
                    elif 1 <= idx <= 7:  # top
                        pass
                    elif 73 <= idx <= 79:  # bottom
                        pass
                    elif idx not in [8, 80] and idx - 1 % 9 == 0:  # right edge
                        pass
                    elif idx not in [0, 72] and idx % 9 == 0:  # left edge
                        pass

            elif event.button == pygame.BUTTON_RIGHT:  # flag
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

# down-left -> idx += 10
# assumong 9x9 grid, idx n to all adjacent tiles bar edges, corners etc
######################
# n-10  n-9 n-8
# n-1   n   n+1
# n+8   n+9 n+10
######################


# 0  1  2  3  4  5  6  7  8
# 9  10 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24 25 26
# 27 28 29 30 31 32 33 34 35
# 36 37 38 39 40 41 42 43 44
# 45 46 47 48 49 50 51 52 53
# 54 55 56 57 58 59 60 61 62
# 63 64 65 66 67 68 69 70 71
# 72 73 74 75 76 77 78 79 80
