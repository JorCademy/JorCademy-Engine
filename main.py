# Python
import asyncio
import os

# Pygame
import pygame
from pygame.locals import *

import components.support.input as inp
# Game
import events
import game
import slitherzenith as sz
from components.support import settings
from components.support.settings import fps, base_dir
from components.timer.timer_manager import update_timers

__debug = False

# Splash screen
__splash_screen_timer = 3000

# Set app icon
icon_path = os.path.join(base_dir,
                         "assets", "icons",
                         "slitherzenith_black.png")
pygame_icon = pygame.image.load(icon_path)
pygame.display.set_icon(pygame_icon)

# Setup game
game.setup()

# pygame setup
flags = pygame.DOUBLEBUF | pygame.HWSURFACE
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
screen = pygame.display.set_mode(sz.screen_size, flags, 16)
pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])

# Controller
joysticks = {}

# Setup game loop
clock = pygame.time.Clock()
running = 1

# Set amount of audio channels
pygame.mixer.set_num_channels(32)


def __debug_log(msg: str) -> None:
    """
    Print debug message when in debug mode

    :param msg: The message to print
    :return: None
    """
    if __debug:
        print(msg)


def __render_objects_on_screen() -> None:
    """
    Render objects in draw buffer

    :return: None
    """
    for obj in sz.__draw_buffer:
        obj.draw(screen)


def __handle_keyboard_events(event_args: pygame.event) -> None:
    """
    Handle keyboard events

    :param event_args: The event arguments
    :return: None
    """
    events.handle_keyboard_input(event_args)

    if not (event_args.type == KEYDOWN or event_args.type == KEYUP):
        return
    key = events.key_to_str(event_args.key)
    if event_args.type == KEYDOWN:
        sz.__key_status[key] = True
    elif event_args.type == KEYUP:
        sz.__key_status[key] = False


def __handle_mouse_events(event_args: pygame.event) -> None:
    """
    Handle mouse events

    :param event_args: The event arguments
    :return: None
    """
    events.handle_mouse_input(event_args)

    # Wheel event
    if event_args.type == MOUSEWHEEL:
        __debug_log("Wheel")
        if event_args.y > 0:
            sz.__scroll_up = True
        elif event_args.y < 0:
            sz.__scroll_down = True

    # Motion event
    if event_args.type == MOUSEMOTION:
        __debug_log("Movement")
        sz.mouse_position = event_args.pos

    # Stop execution when no mouse event detected
    if not (event_args.type == MOUSEBUTTONDOWN or
            event_args.type == MOUSEBUTTONUP):
        return

    # Fetch pressed button (if possible)
    button = events.button_to_str(event_args.button)
    if event_args.type == MOUSEBUTTONDOWN or event_args.type == MOUSEBUTTONUP:
        __debug_log(f"Received {button} event")

    # Button event
    if event_args.type == MOUSEBUTTONDOWN:
        sz.__mouse_status[button] = True
    elif event_args.type == MOUSEBUTTONUP:
        sz.__mouse_status[button] = False


def __handle_controller_events(event_args: pygame.event) -> None:
    """
    Handle controller events

    :param event_args: The event arguments
    :return: None
    """
    responsive_buttons = [0, 1, 2, 3, 11, 12, 13, 14]

    # Button down event
    if event_args.type == pygame.JOYBUTTONDOWN:
        if event_args.button in responsive_buttons:
            sz.__nintendo_switch_button_status[event_args.button] = True

    # Button up event
    elif event_args.type == pygame.JOYBUTTONUP:
        if event_args.button in responsive_buttons:
            sz.__nintendo_switch_button_status[event_args.button] = False


def __show_splash_screen() -> None:
    """
    Show the splash screen with an initial size and slower resizing.

    :return: None
    """
    # Show white backdrop color
    screen.fill((255, 255, 255))

    # Load splash screen
    splash_screen_path = os.path.join(base_dir,
                                      "assets",
                                      "sprites",
                                      "slitherzenith_banner.png")
    splash_screen = pygame.image.load(splash_screen_path)

    # Calculate initial scale factor based on the smaller of width and height
    screen_aspect_ratio = screen.get_width() / screen.get_height()
    image_aspect_ratio = splash_screen.get_width() / splash_screen.get_height()
    if screen_aspect_ratio > image_aspect_ratio:
        initial_scale_factor = (screen.get_height() /
                                splash_screen.get_height() * 0.5)
    else:
        initial_scale_factor = (screen.get_width() /
                                splash_screen.get_width() * 0.5)

    # Calculate initial width and height
    initial_width = int(splash_screen.get_width() * initial_scale_factor)
    initial_height = int(splash_screen.get_height() * initial_scale_factor)

    # Calculate scaling factor based on time elapsed
    scale_factor = min((3000 - __splash_screen_timer) / 3000 * 0.6, 0.6)

    # Smooth scale the splash screen image
    scaled_splash_screen = pygame.transform.smoothscale(splash_screen, (
        int(initial_width + initial_width * scale_factor),
        int(initial_height + initial_height * scale_factor)))

    # Calculate alpha value
    alpha = 1
    if __splash_screen_timer > 2000:
        alpha = 1 - (__splash_screen_timer - 2000) / 1000

    # Calculate position to center the scaled splash screen image
    screen_center_x = screen.get_width() // 2
    screen_center_y = screen.get_height() // 2
    scaled_splash_screen_rect = scaled_splash_screen.get_rect(
        center=(screen_center_x, screen_center_y))

    # Draw splash screen
    scaled_splash_screen.set_alpha(int(alpha * 255))
    screen.blit(scaled_splash_screen, scaled_splash_screen_rect)



async def main() -> None:
    """
    Application entry point

    :return: None
    """
    global running
    global __splash_screen_timer

    # Game loop
    while running:

        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            __handle_keyboard_events(event)
            __handle_mouse_events(event)
            __handle_controller_events(event)

            # Handle hot plugging
            if event.type == pygame.JOYDEVICEADDED:
                # This event will be generated when the program starts for
                # every joystick, filling up the list without needing to
                # create them manually.
                joy = pygame.joystick.Joystick(event.device_index)
                sz.__nintendo_switch_joystick[joy.get_instance_id()] = joy
                print(f"Joystick {joy.get_instance_id()} connencted")

            if event.type == pygame.JOYDEVICEREMOVED:
                del joysticks[event.instance_id]
                print(f"Joystick {event.instance_id} disconnected")

            # Quit game
            if event.type == pygame.QUIT:
                running = 0

        # Show splash screen
        if __splash_screen_timer > 0 and sz.get_splash_screen_enabled():
            __show_splash_screen()
            __splash_screen_timer -= clock.tick(fps)
            pygame.display.flip()
            continue

        # fill the screen with a color to wipe away anything from last frame
        pygame.display.set_caption(sz.screen_title)
        screen.fill(sz.background_color)

        # Update mouse position
        sz.mouse_position = pygame.mouse.get_pos()

        # Get elapsed time between frames
        delta_time = clock.tick(fps) / 1000.0
        settings.delta_time = delta_time

        # Update & render game
        game.update()
        game.draw()
        __render_objects_on_screen()
        update_timers()

        # Update input timer
        if not inp.clickable:
            inp.click_timer += delta_time
            if inp.click_timer >= inp.click_delay:
                inp.clickable = True
                inp.click_timer = 0

        # flip() the display to put your work on screen
        pygame.display.flip()
        sz.__draw_buffer.clear()
        await asyncio.sleep(0)

    pygame.quit()
    return


asyncio.run(main())
