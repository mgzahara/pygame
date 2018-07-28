import pygame, random, math
from projectile import *
from info       import *

pygame.init()

BLACK = (0  , 0  , 0  )
WHITE = (255, 255, 255)
RED   = (255, 0  , 0  )
GREEN = (0  , 255, 0  )
BLUE  = (0  , 0  , 255)
#SCREEN_WIDTH = 700
#SCREEN_HEIGHT = 400
PLATFORM_WIDTH = 50

#unnecessary
#base = pygame.Surface([25, 25])
#base.fill(BLUE)
#base_rect = base.get_rect()

all_sprites_list = pygame.sprite.Group()
ball = Projectile((150, 100), (180, 200), 3, 10, RED)
all_sprites_list.add(ball)

tick = 0
clock = pygame.time.Clock()
spawn_rate = 60
#screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
playing = True


while playing:
#    keys = pygame.key.get_pressed()
    tick += 1
    mouse_x, mouse_y = pygame.mouse.get_pos()

#    all_sprites_list.add(ball)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            playing = False

#        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
#            pos = pygame.mouse.get_pos()
            
#            bullet = Projectile(base_rect, pos, 5, 5, RED)
            # Add the bullet to the lists
#            all_sprites_list.add(bullet)

    #determine where to put everything
    all_sprites_list.update()
    #clear screen
    screen.fill(WHITE)
    #draw each obj here

    left_edge = mouse_x - PLATFORM_WIDTH
    right_edge = mouse_x + PLATFORM_WIDTH

    #draw platform at mouse_x
    pygame.draw.line(screen, BLACK, (left_edge, SCREEN_HEIGHT - 50), (right_edge, SCREEN_HEIGHT - 50), 10)
    #draw blue box for ref
#    screen.blit(base, (100, 100))
    #draw all sprites
    all_sprites_list.draw(screen)
    #render
    pygame.display.flip()
    #set refresh rate
    clock.tick(60)

pygame.quit()
