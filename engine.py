import pygame
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
pygame_icon = pygame.image.load('assets/jorcademy.png')
pygame.display.set_icon(pygame_icon)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    pygame.display.set_caption(jc.screen_title)
    screen.fill(jc.background_color)

    # Render game
    game.draw()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60


pygame.quit()