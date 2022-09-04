import logging as log

import pygame
import pygame.freetype

from . import colours
from .action import Action


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
        self.btns: list[tuple[pygame.Rect, Action]] = []

    def display(self):
        # clear the screen
        self.screen.fill(colours.BG_COLOUR)
        # make buttons
        buttons: list[tuple[str, Action]] = [
            ("Play", Action.PLAY),  # TODO
            ("Leaderboard", Action.LEADERBOARD),
            ("How to play", Action.HOW_TO_PLAY),
            ("Quit", Action.QUIT),
        ]
        # draw main buttons
        for idx, (text, action) in enumerate(buttons):
            y = (70 * idx) + 300
            self.btns.append(
                (
                    pygame.draw.rect(
                        self.screen, colours.BTN_COLOUR, (200, y, 400, 50)
                    ),
                    action,
                )
            )
            self.font.render_to(self.screen, (210, y + 10), text, colours.TXT_COLOUR)

        self.title_font.render_to(
            self.screen, (210, 100), "Minesweeper", colours.TXT_COLOUR
        )
        # update the screen
        pygame.display.update()
        log.debug("made main menu")

    def handle_event(self, event: pygame.event.Event) -> Action:
        log.debug("handling event in main menu")
        if event.type == pygame.QUIT:
            return Action.QUIT

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # left click
                for btn in self.btns:
                    if btn[0].collidepoint(event.pos):
                        return btn[1]

        return Action.NO_OP
