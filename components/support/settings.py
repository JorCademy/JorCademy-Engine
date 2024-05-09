import os
import sys

# Game properties
scale = 1.5
fps = 60
volume = 0.5
clouds = True
delta_time = 1 / fps

# Get the current script's directory
__script_dir = os.path.abspath(os.path.dirname(__file__))

# Navigate two directories up
base_dir = os.path.abspath(
    os.path.join(__script_dir, os.pardir, os.pardir))

# Tile properties
tile_size = int(32 * scale)

# Screen properties
screen_width = int(800 * scale)
screen_height = tile_size * 16
