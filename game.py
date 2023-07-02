from jorcademy import *

angle = 0


def setup() -> None:
    screen(800, 600)


def draw() -> None:
    global angle
    #text((128, 0, 128), 600, 300, 200, 100, angle)
    ellipse((255, 255, 255), 400, 300, 1, 1)
    angle += 1
