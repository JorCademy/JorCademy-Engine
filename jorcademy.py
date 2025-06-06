from typing import Tuple

from primitives import *

# Game settings
screen_size: tuple = (400, 400)
screen_title: str = "JorCademy Engine"
background_color: tuple = (0, 0, 0)
__draw_buffer: list = []
audio_channel_count: int = 0
screen = pygame.display.set_mode((100, 100))

# Initialize audio component
pygame.mixer.init()

# Create type aliases
color = Tuple[int, int, int]

# ==== Keyboard input ====

__key_status = {}


# Get whether a specific key is down
def is_key_down(key: str) -> bool:
    if key in __key_status:
        return __key_status[key]
    else:
        return False


# ==== Mouse input ====

__mouse_status = {}
__scroll_up: bool = False
__scroll_down: bool = False
mouse_position: (int, int) = (0, 0)


# Get whether a specific mouse button is down
def is_mouse_button_down(button: str) -> bool:
    if button in __mouse_status:
        return __mouse_status[button]
    else:
        return False


def is_scrolling_up() -> bool:
    return __scroll_up


# Get whether the player is scrolling down
def is_scrolling_down() -> bool:
    return __scroll_down


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
    app_icon = pygame.image.load("./assets/" + name)
    pygame.display.set_icon(app_icon)


# Change screen background color
def backdrop(c: color) -> None:
    global background_color
    __draw_buffer.clear()
    background_color = c


# Draw a circle
def ellipse(c: color, x: float, y: float, w: float, h: float, rotation=0) -> None:
    e = Ellipse(c, x, y, w, h, rotation)
    __draw_buffer.append(e)


# Draw a rectangle
def rect(c: color, x: float, y: float, w: float, h: float, rotation=0) -> None:
    r = Rectangle(c, x, y, w, h, rotation)
    __draw_buffer.append(r)


# Draw a string of text
def text(content: str, size: int, c: color, x: float, y: float, font="Nunito", rotation=0) -> None:
    # Fetch font
    try:
        font = pygame.font.Font("./assets/" + font, size)
    except:
        font = pygame.font.SysFont(font, size)

    # Draw font
    text_surface = font.render(content, True, c)
    w, h = font.size(content)
    t = Text(content, text_surface, c, x, y, w, h, size, font, rotation)
    __draw_buffer.append(t)


# Load an image
def load_image(path: str) -> Image:
    full_path = "assets/" + path
    try:
        return Image(pygame.image.load(full_path).convert_alpha())
    except pygame.error as e:
        print(f"Error loading image {full_path}: {e}")


# Draw an image
def image(img: Image, x: float, y: float, scale=1.0, flipped=False, rotation=0) -> None:
    surface = img.image
    i = Image(surface, scale, x, y, flipped, rotation)
    __draw_buffer.append(i)


# Load new sound
def load_sound(path: str):
    sound = Exception
    try:
        sound = pygame.mixer.Sound(path)
    except:
        print("Error: Audio could not be loaded.")
    return sound


# Wait for new action
def sleep(msec: int):
    pygame.time.wait(msec)
