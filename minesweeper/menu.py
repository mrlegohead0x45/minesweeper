import logging as log

import pygame


class MainMenu:
    def __init__(self):
        pass

    def display(self, screen: pygame.Surface):
        # make a rectangle on the screen
        pygame.draw.rect(screen, (118, 128, 137), (100, 100, 200, 200))
        # update the screen
        pygame.display.update()
        log.debug("made rectangle")
