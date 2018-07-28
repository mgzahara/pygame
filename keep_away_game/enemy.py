import pygame
from info import *
from projectile import *
from random import randint
class Enemy(Projectile):
    def __init__(self, pos):
        # call parent constructor
        ## start where Enemy was created,
        ## go towards center,
        ## at a certain speed
        r = randint(50, 255)
        g = randint(50, 255)
        b = randint(50, 200)
        Projectile.__init__(self, pos, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), 3, 15, (r, g, b))
        self.pos = pos


    def update(self):
        Projectile.update(self)


def create_enemy():
    # create an enemy off screen
    pos = [1, 2]
    quad = randint(0, 3)
    if quad == 0:
        pos[0] = randint(-15, -5)
        pos[1] = randint(-15, SCREEN_HEIGHT + 15)
        #limit x to the left
    elif quad == 1:
        pos[0] = randint(-15, SCREEN_WIDTH)
        pos[1] = randint(SCREEN_HEIGHT + 5, SCREEN_HEIGHT + 15)
        #limit y below
    elif quad == 2:
        pos[0] = randint(SCREEN_WIDTH + 5, SCREEN_WIDTH + 15)
        pos[1] = randint(SCREEN_HEIGHT - 15, SCREEN_HEIGHT + 15)
        #limit x to the right
    elif quad == 3:
        pos[0] = randint(-15, SCREEN_WIDTH + 15)
        pos[1] = randint(-15, -5)
        #limit y above
        
    e = Enemy(pos)
    return e
#    block_list.add(e)
#    all_sprites_list.add(e)

    
