import pygame
import random
from os.path import join

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        path_player = join("..", "images", "player.png")
        self.image = pygame.image.load(path_player).convert_alpha()
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/1.2))

pygame.init() # initialize the pygame
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # initialize the display surface
pygame.display.set_caption("Spaceship Game")
running = True
clock = pygame.time.Clock() # initialize clock

player = Player()


# import an image surface: spacecraft
# path_player = join("..", "images", "player.png")
# player_surf = pygame.image.load(path_player).convert_alpha()
# player_rect = player_surf.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/1.2)) # calculate position
# player_direction = pygame.math.Vector2(0, 0) # 2d direction of player
# player_speed = 300 # speed of movement

# import an image surface: background
path_star = join("..", "images", "star.png")
star_surf = pygame.image.load(path_star).convert_alpha()
star_positions = [(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT)) for i in range(20)]

# import an image rectangle: meteor
path_meteor = join("..", "images", "meteor.png")
meteor_surf = pygame.image.load(path_meteor).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

# import an image rectangle: laser
path_laser = join("..", "images", "laser.png")
laser_surf = pygame.image.load(path_laser).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20, WINDOW_HEIGHT - 20))

pygame.display.update() # draw on display surface

while running:
    dt = clock.tick() / 1000

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
        #     print(1)
        # if event.type == pygame.MOUSEMOTION:
        #     player_rect.center = event.pos
    
    # input
    # keys = pygame.key.get_pressed()
    # fire = pygame.key.get_just_pressed()
    # if fire[pygame.K_SPACE]:
    #     print("shoot")
    # player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    # player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
    # player_direction = player_direction.normalize() if player_direction else player_direction
    # player_rect.center += player_direction * player_speed * dt

    # draw the game
    display_surface.fill('gray14')

    for pos in star_positions:
        display_surface.blit(star_surf, pos)

    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)
    # display_surface.blit(player_surf, player_rect)
    display_surface.blit(player.image, player.rect)

    pygame.display.update()

pygame.quit() # quit the game