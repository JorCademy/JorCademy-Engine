from slitherzenith import *
from Components.Support.settings import *


class Tile:

    def __init__(self, surface, pos, index):
        self.surface = surface
        self.x = pos[0]
        self.y = pos[1]
        self.index = index
        self.width = tile_size
        self.height = tile_size

    def draw(self):
        image(self.surface, self.x, self.y, self.width, self.height)
