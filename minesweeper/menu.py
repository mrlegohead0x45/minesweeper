import logging as log

import pygame
import pygame.freetype


class MainMenu:
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
        # make a rectangle on the screen
        #                              r,   g,   b,     x,   y, width, height
        pygame.draw.rect(self.screen, (118, 128, 137), (200, 300, 400, 50))
        pygame.draw.rect(self.screen, (118, 128, 137), (200, 400, 400, 50))
        # draw text on the screen         x,   y,    text,    r,   g,   b
        self.font.render_to(self.screen, (210, 310), "Play", (255, 255, 255))
        self.font.render_to(self.screen, (210, 410), "Leaderboard", (255, 255, 255))
        self.title_font.render_to(
            self.screen, (210, 100), "Minesweeper", (255, 255, 255)
        )
        # update the screen
        pygame.display.update()
        log.debug("made main menu")

    def handle_event(self, event: pygame.event.Event):
        pass
