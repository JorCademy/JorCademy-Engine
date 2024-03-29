import asyncio
import os

import pygame
from pygame.locals import *

import events
import game
import jorcademy as jc

__debug = False

# Set app icon
icon_path = os.path.join("assets", "icons", "jc_icon.png")
pygame_icon = pygame.image.load(icon_path)
pygame.display.set_icon(pygame_icon)
flags = pygame.DOUBLEBUF | pygame.HWSURFACE

# Init user setup
game.setup()

# pygame setup
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
screen = pygame.display.set_mode(jc.screen_size, flags, 16)

# Setup game loop
clock = pygame.time.Clock()
running = 1

# Set amount of audio channels
pygame.mixer.set_num_channels(32)


# Print debug message when in debug mode
def __debug_log(msg: str):
    if __debug:
        print(msg)


# Render objects in draw buffer
def __render_objects_on_screen() -> None:
    for obj in jc.__draw_buffer:
        obj.draw(screen)


# === Keyboard input === #

def __handle_keyboard_events(event_args: pygame.event):
    events.handle_keyboard_input(event_args)

    if not (event_args.type == KEYDOWN or event_args.type == KEYUP):
        return
    key = events.key_to_str(event_args.key)
    if event_args.type == KEYDOWN:
        jc.__key_status[key] = True
    elif event_args.type == KEYUP:
        jc.__key_status[key] = False


# ==== Mouse input ==== #

def __handle_mouse_events(event_args: pygame.event):
    events.handle_mouse_input(event_args)

    # Wheel event
    if event_args.type == MOUSEWHEEL:
        __debug_log("Wheel")
        if event_args.y > 0:
            jc.__scroll_up = True
        elif event_args.y < 0:
            jc.__scroll_down = True

    # Motion event
    if event_args.type == MOUSEMOTION:
        __debug_log("Movement")
        jc.mouse_position = event_args.pos

    # Stop execution when no mouse event detected
    if not (event_args.type == MOUSEBUTTONDOWN or event_args.type == MOUSEBUTTONUP):
        return

    # Fetch pressed button (if possible)
    button = events.button_to_str(event_args.button)
    if event_args.type == MOUSEBUTTONDOWN or event_args.type == MOUSEBUTTONUP:
        __debug_log(f"Received {button} event")

    # Button event
    if event_args.type == MOUSEBUTTONDOWN:
        jc.__mouse_status[button] = True
    elif event_args.type == MOUSEBUTTONUP:
        jc.__mouse_status[button] = False


# Application entry point
async def main():
    global running

    # Game loop
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            __handle_keyboard_events(event)
            __handle_mouse_events(event)

            # Quit game
            if event.type == pygame.QUIT:
                running = 0

        # fill the screen with a color to wipe away anything from last frame
        pygame.display.set_caption(jc.screen_title)
        screen.fill(jc.background_color)

        # Update mouse position
        jc.mouse_position = pygame.mouse.get_pos()

        # Render game
        game.update()
        __render_objects_on_screen()

        # flip() the display to put your work on screen
        pygame.display.flip()
        jc.__draw_buffer.clear()
        await asyncio.sleep(0)

    pygame.quit()
    return


asyncio.run(main())