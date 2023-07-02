import pygame
from primitives import *
from typing import Tuple

# Game settings
screen_size: tuple = (100, 100)
screen_title: str = "JorCademy Engine"
background_color: tuple = (0, 0, 0)
draw_buffer: list = []
audio_channel_count: int = 0

# Initialize audio component
pygame.mixer.init()

# Create type aliases
color = Tuple[int, int, int]

# ==== Keyboard input ====

# WASD keys
key_w_down: bool = False 
key_a_down: bool = False 
key_s_down: bool = False 
key_d_down: bool = False 

# Arrow keys
key_up_down: bool = False 
key_down_down: bool = False 
key_left_down: bool = False
key_right_down: bool = False 

# Other keys
key_space_down: bool = False


# Change screen size
def screen(width: int, height: int) -> None:
    global screen_size
    screen_size = (width, height)


# Change screen title
def title(t: str) -> None:
    global screen_title
    screen_title = t


# Change app icon
def icon(name: str) -> None:
    app_icon = pygame.image.load("assets/" + name)
    pygame.display.set_icon(app_icon)


# Change screen background color
def backdrop(c: color) -> None:
    global background_color
    draw_buffer.clear()
    background_color = c


# Draw a circle
def ellipse(c: color, x: float, y: float, w: float, h: float, rotation=0) -> None:
    e = Ellipse(c, x, y, w, h, rotation)
    draw_buffer.append(e)


# Draw a rectangle
def rect(c: color, x: float, y: float, w: float, h: float, rotation=0) -> None:
    r = Rectangle(c, x, y, w, h, rotation)
    draw_buffer.append(r)


# Draw a string of text
def text(content: str, c: color, x: float, y: float, rotation=0) -> None:
    font = pygame.font.Font(None, 48)
    text_surface = font.render(content, True, c)
    t = Text(content, text_surface, c, x, y, None, None, rotation)
    draw_buffer.append(t)


# Draw an image
def image(url: str, x: float, y: float, scale: float, rotation=0) -> None:
    i = Image(url, scale, x, y, rotation)
    draw_buffer.append(i)


# Load new sound
def load_sound(path: str):
    global audio_channel_count
    sound: Audio = Audio(audio_channel_count, path)
    audio_channel_count += 1
    return pygame.mixer.Sound(sound.filepath)


# Play audio
def play_sound(audio_obj: Audio):
    sound = pygame.mixer.Sound("assets/" + audio_obj.filepath)
    if not pygame.mixer.Channel(audio_obj.channel).get_busy():
        pygame.mixer.Channel(audio_obj.channel).play(sound)


# Wait for new action
def sleep(msec: int):
    pygame.time.wait(msec)
