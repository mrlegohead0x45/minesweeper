import logging as log

import pygame

from minesweeper.game import MinesweeperGame

log.basicConfig(level=log.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

log.debug("initialising pygame")
pygame.init()
log.debug("pygame initialised")


def main():
    game = MinesweeperGame()
    game.run()


if __name__ == "__main__":
    main()
