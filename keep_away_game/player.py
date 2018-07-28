import pygame
from info import *


class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """
    
    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        
        self.rect = self.image.get_rect()
