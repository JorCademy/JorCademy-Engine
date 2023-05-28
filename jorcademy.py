import pygame
from primitives import *
from typing import Tuple

# Game settings
screen_size = (100, 100)
screen_title = "JorCademy Engine"
background_color = (0, 0, 0)
draw_buffer = []

# Create type aliases
color = Tuple[int, int, int]


# Change screen size
def screen(width: int, height: int) -> (int, int):
    global screen_size
    screen_size = (width, height)


# Change screen title
def title(t: str):
    global screen_title
    screen_title = t


# Change screen background color
def backdrop(r: int, g: int, b: int):
    global background_color
    background_color = (r, g, b)


# Draw a circle
def ellipse(c: (int, int, int), x: float, y: float, w: float, h: float):
    e = Ellipse(c, x, y, w, h)
    draw_buffer.append(e)


# Draw a rectangle
def rect(c: (int, int, int), x: float, y: float, w: float, h: float):
    r = Rectangle(c, x, y, w, h)
    draw_buffer.append(r)


# Draw a string of text
def text(content: str, c: (int, int, int), x: float, y: float):
    font = pygame.font.Font(None, 48)
    text_surface = font.render(content, True, c)
    t = Text(content, text_surface, c, x, y, None, None)
    draw_buffer.append(t)





