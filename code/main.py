import pygame
import random
from os.path import join

pygame.init() # initialize the pygame
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # initialize the display surface
pygame.display.set_caption("Spaceship Game")
running = True
x = 720

# import an image surface: spacecraft
path_player = join("..", "images", "player.png")
player_surf = pygame.image.load(path_player).convert_alpha()

# import an image surface: background
path_star = join("..", "images", "star.png")
star_surf = pygame.image.load(path_star).convert_alpha()
star_positions = [(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT)) for i in range(20)]

pygame.display.update() # draw on display surface

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game
    display_surface.fill('gray14')
    display_surface.blit(player_surf, (150, x)) # put 1 surface on another (rectangle)
    x -= 0.5
    # origin point is top left corner, not like cartesian coordinates

    for pos in star_positions:
        display_surface.blit(star_surf, pos)
    
    pygame.display.update() # draw on display surface

    # display graphics, surface in pygame is usually image

pygame.quit() # quit the game