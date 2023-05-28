import pygame

# Game settings
screen_size = (100, 100)
screen_title = "JorCademy Engine"
background_color = (0, 0, 0)


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
def circle():
    pass


# Draw a rectangle
def rect():
    pass


# Draw a triangle
def triangle():
    pass


# Draw a string of text
def text():
    pass
