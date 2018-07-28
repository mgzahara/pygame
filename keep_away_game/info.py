import pygame
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

difficulty = 1
enemy_spawn_freq = 60 / difficulty
tick = 0

SCREEN_WIDTH  = 600
SCREEN_HEIGHT = 600
# Set the height and width of the screen

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# --- Sprite lists

# This is a list of every sprite. All blocks and the player block.
all_sprites_list = pygame.sprite.Group()

# List of each block in the game
block_list = pygame.sprite.Group()

# List of each bullet
bullet_list = pygame.sprite.Group()

#bool for game loop
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0
