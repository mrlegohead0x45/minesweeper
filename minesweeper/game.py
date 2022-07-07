import logging as log
from pathlib import Path

import pygame
from attrs import astuple

from .colour import Colour

log.basicConfig(level=log.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

BG_COLOUR = Colour(195, 199, 203)


class MinesweeperGame:
    def __init__(self):
        log.debug("creating game")
        self.running = True
        self.assets_dir = Path(__file__).parent.parent / "assets"

    def run(self):
        log.debug("running game")

        self.display = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Minesweeper")
        pygame.display.set_icon(
            pygame.image.load(str(self.assets_dir / "images" / "icon.png"))
        )

        # self.display = pygame.display.get_surface()
        self.display_menu()

        self.display.fill(astuple(BG_COLOUR))
        pygame.display.update()

        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)

            # self.on_loop()
            # self.on_render()

        self.cleanup()

    def display_menu(self):
        log.debug("displaying menu")

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.QUIT:
            self.running = False

    def cleanup(self):
        log.debug("cleaning up game")
        pygame.quit()
