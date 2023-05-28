from jorcademy import *

x = 400
y = 300


def setup() -> None:
    screen(800, 600)


def draw() -> None:
    global x
    global y

    x += 1
    y += 1
    backdrop((255, 255, 255))
    ellipse((0, 0, 255), x, y, 100, 100)

