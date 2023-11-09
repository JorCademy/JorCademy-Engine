from Components.Support.support import *
from Components.TileMap.tile import Tile


def read_tile_map(csv_filename: str, tile_set_filename: str) -> [Tile]:
    level_data = import_level_data(csv_filename)
    level_length = len(level_data[0] * tile_size)
    tile_set = import_tile_set(tile_set_filename)
    environment = []

    # Initial y-coordinate of tile
    y = tile_size / 2

    # Read tiles into tiles list
    for row in level_data:
        # Initial x-coordinate of tile
        x = tile_size / 2

        for tile in row:
            # Get tile image
            tile_image = tile_set[tile]

            # Create tile object
            tile_object = Tile(tile_image, x, y)

            # Add tile to environment
            environment.append(tile_object)

            # Increment x-coordinate
            x += tile_size

        # Increment y-coordinate
        y += tile_size

    return environment
