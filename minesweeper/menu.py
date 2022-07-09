import logging as log

import pygame
import pygame.freetype

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
        # make buttons
        buttons: list[tuple[str, Action]] = [
            ("Play", Action.PLAY),
            ("Leaderboard", Action.LEADERBOARD),
            ("Credits", Action.CREDITS),
            ("Quit", Action.QUIT),
        ]
        for idx, (text, action) in enumerate(buttons):
            y = (70 * idx) + 300
            self.btns.append(
                (
                    pygame.draw.rect(self.screen, (118, 128, 137), (200, y, 400, 50)),
                    action,
                )
            )
            self.font.render_to(self.screen, (210, y + 10), text, (255, 255, 255))

        self.title_font.render_to(
            self.screen, (210, 100), "Minesweeper", (255, 255, 255)
        )
        # update the screen
        pygame.display.update()
        log.debug("made main menu")

    def handle_event(self, event: pygame.event.Event) -> Action:
        if event.type == pygame.QUIT:
            return Action.QUIT

        if event.type == pygame.MOUSEBUTTONDOWN:
            for btn in self.btns:
                if btn[0].collidepoint(event.pos):
                    return btn[1]

        return Action.NO_OP
