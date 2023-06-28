import pygame
from pygame.locals import *
import game
import jorcademy as jc

# Init user setup
game.setup()

# pygame setup
pygame.init()
screen = pygame.display.set_mode(jc.screen_size)
clock = pygame.time.Clock()
running = True

# Set app icon
pygame_icon = pygame.image.load('assets/jc_icon.png')
pygame.display.set_icon(pygame_icon)


# Render objects in draw buffer
def render_objects_on_screen() -> None:
    for obj in jc.draw_buffer:
        obj.draw(screen)


# === Keyboard input === #

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


# Game loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():

        # Keyboard - DOWN
        if event.type == KEYDOWN:
            handle_special_keys_down(event)
            handle_wasd_keys_down(event) 
            handle_arrow_keys_down(event)

        # Keyboard - UP
        if event.type == KEYUP:
            handle_special_keys_up(event)
            handle_wasd_keys_up(event)
            handle_arrow_keys_up(event) 

        # Quit game
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    pygame.display.set_caption(jc.screen_title)
    screen.fill(jc.background_color)

    # Render game
    game.draw()
    render_objects_on_screen()

    # flip() the display to put your work on screen
    pygame.display.flip()
    jc.draw_buffer.clear()

    clock.tick(60)  # limits FPS to 60


pygame.quit()
