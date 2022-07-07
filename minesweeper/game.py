import logging as log
from pathlib import Path

import pygame
from attrs import astuple

from .colour import Colour
from .menu import MainMenu

BG_COLOUR = Colour(195, 199, 203)


class MinesweeperGame:
    def __init__(self):
        log.debug("creating game")
        self.running = True
        self.assets_dir = Path(__file__).parent.parent / "assets"
        self.main_menu = MainMenu()

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

    def run(self):
        log.debug("running game")
        self.setup()
        self.main_menu.display(self.screen)

        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)

            # self.on_loop()
            # self.on_render()

        self.cleanup()

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.QUIT:
            self.running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            log.debug(f"mouse button down at {event.pos}")
            # print position
            # pos = pygame.mouse.get_pos()

    def cleanup(self):
        log.debug("cleaning up game")
        pygame.quit()
