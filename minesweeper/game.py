import logging as log
from enum import Enum
from pathlib import Path

import pygame
import pygame.freetype
from attrs import astuple

from .colour import Colour
from .menu import MainMenu

BG_COLOUR = Colour(195, 199, 203)


class ScreenLocation(Enum):
    MAIN_MENU = 0
    GAME = 1
    LEADERBOARD = 2


class MinesweeperGame:
    def __init__(self):
        log.debug("creating game")
        self.running = True
        self.assets_dir = Path(__file__).parent.parent / "assets"

    def setup(self):
        log.debug("setting up game")
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Minesweeper")
        pygame.display.set_icon(
            pygame.image.load(str(self.assets_dir / "images" / "icon.png"))
        )
        log.debug("set icon, name")
        # self.display = pygame.display.get_surface()
        self.screen.fill(astuple(BG_COLOUR))
        pygame.display.update()
        log.debug("filled screen")

        self.text_font = pygame.freetype.SysFont("monospace", 20)
        self.title_font = pygame.freetype.SysFont("monospace", 50)
        self.main_menu = MainMenu(self.text_font, self.title_font, self.screen)
        self.location = ScreenLocation.MAIN_MENU

    def run(self):
        log.debug("running game")
        self.setup()
        self.main_menu.display()

        while self.running:
            try:
                for event in pygame.event.get():
                    self.handle_event(event)

            except KeyboardInterrupt:
                self.running = False
            # self.on_loop()
            # self.on_render()

        self.cleanup()

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.QUIT:
            self.running = False

        if self.location == ScreenLocation.MAIN_MENU:
            self.main_menu.handle_event(event)
            # print position
            # pos = pygame.mouse.get_pos()

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     log.debug("mouse button down at %s", event.pos)

    def cleanup(self):
        log.debug("cleaning up game")
        pygame.quit()
