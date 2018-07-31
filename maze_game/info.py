import pygame

playing = True

# Define the colors we will use in RGB format
BLACK =  (  0,   0,   0)
WHITE =  (255, 255, 255)
BLUE =   (  0,   0, 255)
GREEN =  (  0, 255,   0)
RED =    (255,   0,   0)
GRAY =   (128, 128, 128)
LIME =   (  0, 255,   0)
PURPLE = (128,   0, 128)
TEAL =   (  0, 128, 128)
YELLOW =  (255, 255,   0)

COLORS = [BLACK, GREEN, RED, GRAY, LIME, PURPLE, TEAL, YELLOW]
#smallest unit of pixels for any object
UNIT_SIZE = 20

SCREEN_WIDTH  = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

#player info
PLAYER_LEFT = (SCREEN_WIDTH  / 2) - (UNIT_SIZE / 2)
PLAYER_TOP  = (SCREEN_HEIGHT / 2) - (UNIT_SIZE / 2)
PLAYER_DIM  = [PLAYER_LEFT, PLAYER_TOP]

starting_rights = 0
inside_maze = False
last_move = ''

#terrain info
#TERRAIN_GAP = 4
TERRAIN_X_START = 10 + (16 * UNIT_SIZE)# 16 + TERRAIN_GAP
TERRAIN_Y_START = 10 + (8  * UNIT_SIZE)# 8 - TERRAIN_GAP


#lists
all_sprites_list = pygame.sprite.Group()
player_list      = pygame.sprite.Group()
terrain_list     = pygame.sprite.Group()

clock = pygame.time.Clock()
winning_pos = [SCREEN_WIDTH, SCREEN_HEIGHT]
