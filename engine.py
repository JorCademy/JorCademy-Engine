import pygame
from pygame.locals import *
import game
import jorcademy as jc
import events

# Set app icon
pygame_icon = pygame.image.load('./assets/icons/jc_icon.png')
pygame.display.set_icon(pygame_icon)

# Init user setup
game.setup()

# pygame setup
pygame.init()
screen = pygame.display.set_mode(jc.screen_size)
clock = pygame.time.Clock()
running = True


# Render objects in draw buffer
def render_objects_on_screen() -> None:
    for obj in jc.draw_buffer:
        obj.draw(screen)


# === Keyboard input === #

def handle_keyboard_events(event_args: pygame.event):
    events.handle_input(event_args)

    if not (event_args.type == KEYDOWN or event_args.type == KEYUP):
        return
    key = events.key_to_str(event_args.key)
    if event_args.type == KEYDOWN:
        jc.key_status[key] = True
    elif event_args.type == KEYUP:
        jc.key_status[key] = False




# ==== Mouse input ==== #

def handle_mouse_input(event_args: pygame.event):
    # Mouse - DOWN
    if event_args.type == MOUSEBUTTONDOWN:
        if event_args.button == 1:
            game.mouse_left_down = True
        elif event_args.button == 2:
            game.mouse_right_down = True

    # Mouse - UP
    if event_args.type == MOUSEBUTTONUP:
        if event_args.button == 1:
            game.mouse_left_down = False
        elif event_args.button == 2:
            game.mouse_right_down = False

    # Mouse - WHEEL
    if event_args.type == MOUSEWHEEL:
        if event_args.y > 0:
            game.scroll_up = True
        elif event_args.y < 0:
            game.scroll_down = True

    # Mouse - MOTION
    if event_args.type == MOUSEMOTION:
        game.mouse_position = event_args.pos


# Game loop
while running:
    game.scroll_down = False
    game.scroll_up = False

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        handle_keyboard_events(event)
        handle_mouse_input(event)

        # Quit game
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    pygame.display.set_caption(jc.screen_title)
    screen.fill(jc.background_color)

    # Render game
    game.update()
    render_objects_on_screen()

    # flip() the display to put your work on screen
    pygame.display.flip()
    jc.draw_buffer.clear()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
