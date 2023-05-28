from jorcademy import *

RED: color = (255, 0, 0)
GREEN: color = (0, 255, 0)
BLUE: color = (0, 0, 255)


def setup() -> None:
    screen(800, 600)
    backdrop(255, 255, 255)


def draw() -> None:
    ellipse(RED, 400, 300, 100, 200)
    rect(GREEN, 400, 300, 100, 100)
    text("Hell yeah!", BLUE, 400, 100)
