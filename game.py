from jorcademy import *

RED: color = (255, 0, 0)
GREEN: color = (0, 255, 0)
BLUE: color = (0, 0, 255)


def setup() -> None:
    screen(800, 600)
    backdrop((255, 255, 255))


def draw() -> None:
    image('jorcademy.png', 400, 260, 0.4)
    text("Think diffewent, UwU", (0, 0, 0), 400, 400)
    pass 
