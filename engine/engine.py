import pygame
from pygame.locals import *
import game
import jorcademy as jc

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
        obj.update(screen)


# === Keyboard input === #

def handle_keyboard_events(event_args: pygame.event):
    # Keyboard - DOWN
    if event_args.type == KEYDOWN:
        handle_special_keys_down(event_args)
        handle_wasd_keys_down(event_args)
        handle_arrow_keys_down(event_args)

    # Keyboard - UP
    if event_args.type == KEYUP:
        handle_special_keys_up(event_args)
        handle_wasd_keys_up(event_args)
        handle_arrow_keys_up(event_args)


def handle_special_keys_down(game_event: pygame.event) -> None:
    if game_event.key == K_SPACE:
        game.key_space_down = True


def handle_special_keys_up(game_event: pygame.event) -> None:
    if game_event.key == K_SPACE:
        game.key_space_down = False


def handle_arrow_keys_down(game_event: pygame.event) -> None:
    if game_event.key == K_LEFT:
        game.key_left_down = True
    elif game_event.key == K_RIGHT:
        game.key_right_down = True
    elif game_event.key == K_DOWN:
        game.key_down_down = True
    elif game_event.key == K_UP:
        game.key_up_down = True


def handle_arrow_keys_up(game_event: pygame.event) -> None:
    if game_event.key == K_LEFT:
        game.key_left_down = False
    elif game_event.key == K_RIGHT:
        game.key_right_down = False
    elif game_event.key == K_DOWN:
        game.key_down_down = False
    elif game_event.key == K_UP:
        game.key_up_down = False


def handle_wasd_keys_down(game_event: pygame.event) -> None:
    if game_event.key == K_w:
        game.key_w_down = True
    elif game_event.key == K_a:
        game.key_a_down = True
    elif game_event.key == K_s:
        game.key_s_down = True
    elif game_event.key == K_d:
        game.key_d_down = True


def handle_wasd_keys_up(game_event: pygame.event) -> None:
    if game_event.key == K_w:
        game.key_w_down = False
    elif game_event.key == K_a:
        game.key_a_down = False
    elif game_event.key == K_s:
        game.key_s_down = False
    elif game_event.key == K_d:
        game.key_d_down = False


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
