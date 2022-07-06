import logging as log

import pygame

log.basicConfig(level=log.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

log.debug("initialising pygame")
pygame.init()
log.debug("pygame initialised")


class MinesweeperGame:
    def __init__(self):
        log.debug("creating game")
        self.running = True

    def run(self):
        log.debug("running game")

        pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Minesweeper")

        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)

            # self.on_loop()
            # self.on_render()

        self.cleanup()

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.QUIT:
            self.running = False

    def cleanup(self):
        log.debug("cleaning up game")
        pygame.quit()


def main():
    game = MinesweeperGame()
    game.run()


if __name__ == "__main__":
    main()
