from slitherzenith import *
from components.support.settings import *


class Tile:
    """
    A tile
    """

    def __init__(self, surface, pos, index):
        self.surface = surface
        self.x = pos[0]
        self.y = pos[1]
        self.index = index
        self.width = tile_size
        self.height = tile_size

    def draw(self) -> None:
        """
        Draw the tile

        :return: None
        """
        image(self.surface, self.x, self.y, self.width, self.height)
