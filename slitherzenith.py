from typing import Tuple
from components.support import settings
from primitives import *

# Game settings
screen_size: tuple = (400, 400)
screen_title: str = "SlitherZenith"
background_color: tuple = (255, 255, 255)
__draw_buffer: list = []
__splash_screen_enabled: bool = True

# Initialize audio component
pygame.mixer.init()

# Create type aliases
color = Tuple[int, int, int]

# ==== Keyboard input ====

__key_status = {}

# === Nintendo Switch controller input ===

__nintendo_switch_button_status = {
    0: False,  # A
    1: False,  # B
    2: False,  # X
    3: False,  # Y
    4: False,  # - (MINUS)
    5: False,  # HOME
    6: False,  # + (PLUS)
    9: False,  # PLUS
    11: False,  # D_UP
    12: False,  # D_DOWN
    13: False,  # D_LEFT
    14: False,  # D_RIGHT
}
__nintendo_switch_joystick = {}


def is_key_down(key: str) -> bool:
    """
    Get whether a specific key is down

    :param key: The key to check
    :return: Whether the key is down
    """
    if key in __key_status:
        return __key_status[key]
    else:
        return False


def is_nintendo_switch_pro_button_down(button: int) -> bool:
    """
    Get whether a specific Switch button is down

    :param button: The button to check
    :return: Whether the button is down
    """
    if button in __nintendo_switch_button_status:
        return __nintendo_switch_button_status[button]
    else:
        return False


def vibrate_nintendo_switch_pro(duration: float) -> None:
    """
    Vibrate the Nintendo Switch Pro controller

    :param duration: The duration of the vibration
    :return: None
    """
    try:
        __nintendo_switch_joystick[0].rumble(1.0, 1.0, int(duration * 1000))
    except KeyError:
        print("No Nintendo Switch Pro controller detected.")


# ==== Mouse input ====

__mouse_status = {}
__scroll_up: bool = False
__scroll_down: bool = False
mouse_position = pygame.Vector2(0, 0)


def is_mouse_button_down(button: str) -> bool:
    """
    Get whether a specific mouse button is down

    :param button: The button to check
    :return: Whether the button is down
    """
    if button in __mouse_status:
        return __mouse_status[button]
    else:
        return False


def is_scrolling_up() -> bool:
    """
    Get whether the player is scrolling up

    :return: Whether the player is scrolling up
    """
    return __scroll_up


# Get whether the player is scrolling down
def is_scrolling_down() -> bool:
    """
    Get whether the player is scrolling down

    :return: Whether the player is scrolling down
    """
    return __scroll_down


# Change screen size
def screen(width: int, height: int) -> None:
    """
    Change screen size

    :param width: The width of the screen
    :param height: The height of the screen
    :return: None
    """
    global screen_size
    screen_size = (width, height)


# Get screen width
def get_screen_width() -> int:
    """
    Get screen width

    :return: The width of the screen
    """
    return screen_size[0]


def get_screen_height() -> int:
    """
    Get screen height

    :return: The height of the screen
    """
    return screen_size[1]


def title(t: str) -> None:
    """
    Change screen title

    :param t: The new title
    :return: None
    """
    global screen_title
    screen_title = t


def icon(name: str) -> None:
    """
    Change screen icon

    :param name: The name of the icon
    :return: None
    """
    app_icon = pygame.image.load("./assets/" + name)
    pygame.display.set_icon(app_icon)


def backdrop(c: color) -> None:
    """
    Change screen background color

    :param c: The new background color
    :return: None
    """
    global background_color
    __draw_buffer.clear()
    background_color = c


# Draw a circle
def ellipse(c: color, x: float, y: float, w: float, h: float, rotation=0) \
        -> None:
    """
    Draw a circle

    :param c: The color of the ellipse
    :param x: The x-coordinate of the ellipse
    :param y: The y-coordinate of the ellipse
    :param w: The width of the ellipse
    :param h: The height of the ellipse
    :param rotation: The rotation of the ellipse
    :return: None
    """
    e = Ellipse(c, x, y, w, h, rotation)
    __draw_buffer.append(e)


def rect(c: color, x: float, y: float, w: float, h: float, rotation=0) -> None:
    """
    Draw a rectangle

    :param c: The color of the rectangle
    :param x: The x-coordinate of the rectangle
    :param y: The y-coordinate of the rectangle
    :param w: The width of the rectangle
    :param h: The height of the rectangle
    :param rotation: The rotation of the rectangle
    :return: None
    """
    r = Rectangle(c, x, y, w, h, rotation)
    __draw_buffer.append(r)


def text(content: str,
         size: int,
         c: color,
         x: float,
         y: float,
         font="Nunito",
         rotation=0) -> None:
    """
    Draw text

    :param content: The content of the text
    :param size: The size of the text
    :param c: The color of the text
    :param x: The x-coordinate of the text
    :param y: The y-coordinate of the text
    :param font: The font of the text
    :param rotation: The rotation of the text
    :return: None
    """
    # Fetch font
    try:
        font = pygame.font.Font("./assets/" + font, size)
    except FileNotFoundError:
        font = pygame.font.SysFont(font, size)

    # Draw font
    text_surface = font.render(content, True, c)
    t = Text(content, text_surface, c, x, y, text_surface.get_width(),
             text_surface.get_height(), size, font, rotation)
    __draw_buffer.append(t)


def load_image(path: str) -> pygame.Surface:
    """
    Load an image

    :param path: The path of the image
    :return: The image
    """
    full_path = "assets/" + path
    try:
        return pygame.image.load(full_path).convert_alpha()
    except pygame.error as e:
        print(f"Error loading image '{full_path}': {e}")


def image(surface: pygame.Surface, x: float, y: float, scale: float,
          flipped=False, rotation=0) -> None:
    """
    Draw an image

    :param surface: The image to draw
    :param x: The x-coordinate of the image
    :param y: The y-coordinate of the image
    :param scale: The scale of the image
    :param flipped: Whether the image is flipped
    :param rotation: The rotation of the image
    :return: None
    """
    i = Image(surface, scale, x, y, flipped, rotation)
    __draw_buffer.append(i)


def load_sound(path: str) -> pygame.mixer.Sound:
    """
    Load a sound

    :param path: The path of the sound
    :return: The sound
    """
    sound = Exception
    try:
        sound = pygame.mixer.Sound(path)
    except pygame.error:
        print(f"Error: Audio {path} could not be loaded.")
    return sound


def play_sound(sound, p_volume=1.0) -> None:
    """
    Play a sound

    :param sound: The sound to play
    :param p_volume: The volume of the sound
    :return: None
    """
    try:
        sound.set_volume(p_volume * settings.volume)
        if sound.get_num_channels() == 0:
            pygame.mixer.find_channel().play(sound)
    except pygame.error:
        print("Error: Audio could not be played.")


def sleep(msec: int) -> None:
    """
    Sleep for a certain amount of time

    :param msec: The amount of time to sleep
    :return: None
    """
    pygame.time.wait(msec)


def set_cursor_visible(visible: bool) -> None:
    """
    Set the cursor to be visible

    :param visible: Whether the cursor is visible
    :return: None
    """
    pygame.mouse.set_visible(visible)


def set_splash_screen_enabled(enabled: bool) -> None:
    """
    Set the splash screen to be enabled

    :param enabled: Whether the splash screen is enabled
    :return: None
    """
    global __splash_screen_enabled
    __splash_screen_enabled = enabled


def get_splash_screen_enabled() -> bool:
    """
    Get whether the splash screen is enabled

    :return: Whether the splash screen is enabled
    """
    return __splash_screen_enabled
