import logging as log
from enum import Enum
from pathlib import Path

import pygame
import pygame.freetype
from attrs import astuple

from . import colours
from .action import Action
from .game import Game
from .how_to_play import HowToPlay
from .leaderboard import Leaderboard
from .menu import MainMenu


class ScreenLocation(Enum):
    MAIN_MENU = 0
    GAME = 1
    LEADERBOARD = 2
    HOW_TO_PLAY = 3


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
        self.screen.fill(colours.BG_COLOUR)
        pygame.display.update()
        log.debug("filled screen")

        self.text_font = pygame.freetype.Font(
            str(self.assets_dir / "fonts" / "Ubuntu-Regular.ttf"), 20
        )
        self.title_font = pygame.freetype.Font(
            str(self.assets_dir / "fonts" / "Ubuntu-Regular.ttf"), 50
        )
        self.main_menu = MainMenu(self.text_font, self.title_font, self.screen)
        self.game = Game(self.text_font, self.title_font, self.screen)
        self.leaderboard = Leaderboard(self.text_font, self.title_font, self.screen)
        self.how_to_play = HowToPlay(self.text_font, self.title_font, self.screen)
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
            return

        handlers = {
            ScreenLocation.MAIN_MENU: self.main_menu.handle_event,
            ScreenLocation.GAME: self.game.handle_event,
            ScreenLocation.LEADERBOARD: self.leaderboard.handle_event,
            ScreenLocation.HOW_TO_PLAY: self.how_to_play.handle_event,
        }

        action = handlers[self.location](event)

        self.take_action(action)

        if event.type == pygame.MOUSEBUTTONDOWN:
            log.debug("mouse button down at %s", event.pos)

    def take_action(self, action: Action):
        if action == Action.QUIT:
            self.running = False
            return

        d = {
            Action.MAIN_MENU: (ScreenLocation.MAIN_MENU, self.main_menu.display),
            Action.PLAY: (ScreenLocation.GAME, self.game.display),
            Action.LEADERBOARD: (ScreenLocation.LEADERBOARD, self.leaderboard.display),
            Action.HOW_TO_PLAY: (ScreenLocation.HOW_TO_PLAY, self.how_to_play.display),
        }

        if action == Action.PLAY:
            self.location = ScreenLocation.GAME
            self.game.display()
            return

        if action == Action.LEADERBOARD:
            self.location = ScreenLocation.LEADERBOARD
            self.leaderboard.display()
            return

        if action == Action.HOW_TO_PLAY:
            self.location = ScreenLocation.HOW_TO_PLAY
            self.how_to_play.display()
            return

        if action == Action.MAIN_MENU:
            self.location = ScreenLocation.MAIN_MENU
            self.main_menu.display()
            return

    def cleanup(self):
        log.debug("cleaning up game")
        pygame.quit()
