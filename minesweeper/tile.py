from pygame import Rect


class Tile:
    def __init__(self, rect: Rect, is_mine: bool = False):
        self.is_mine = is_mine
        self.rect = rect

    def explode(self):
        pass

    def reveal(self):
        if self.is_mine:
            self.explode()

        else:
            pass
