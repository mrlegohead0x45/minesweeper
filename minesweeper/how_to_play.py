import logging as log
from pathlib import Path

import pygame
import pygame.freetype

from . import colours
from .action import Action


class HowToPlay:
    def __init__(
        self,
        font: pygame.freetype.Font,
        title_font: pygame.freetype.Font,
        screen: pygame.Surface,
    ):
        self.font = font
        self.title_font = title_font
        self.screen = screen
        self.file_path = (
            Path(__file__).parent.parent / "assets" / "text" / "how_to_play.txt"
        )

    def display(self):
        log.debug("displaying how to play")
        # clear the screen
        self.screen.fill(colours.BG_COLOUR)
        # create back button in top left
        self.back_button = pygame.Rect(25, 25, 100, 50)
        # back_button.center = (50, 50)
        pygame.draw.rect(self.screen, colours.BTN_COLOUR, self.back_button)
        self.font.render_to(self.screen, (40, 40), "Back", colours.TXT_COLOUR)
        # create text box in middle
        text_box = pygame.Rect(200, 100, 400, 400)
        pygame.draw.rect(self.screen, colours.BTN_COLOUR, text_box)
        # read in text from file
        text = self.file_path.read_text()
        # TODO: render text to screen (wrapped)

        pygame.display.update()

    def handle_event(self, event: pygame.event.Event) -> Action:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:  # left click
                if self.back_button.collidepoint(event.pos):
                    log.debug("howtoplay clicked back button")
                    return Action.MAIN_MENU

        return Action.NO_OP
