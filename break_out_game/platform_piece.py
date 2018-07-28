import pygame
from info import *

class PlatformPiece(pygame.sprite.Sprite):
    def __init__(self, color, id_num):
        '''                                                                                     
        color  - (int, int, int) r,g,b values                                                    
        id_num - int unique number to identify an instance                                       
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(PLATFORM_DIM)
        self.image.fill(color)
        self.id_num = id_num
        #must have so we can check collisions
        self.rect = self.image.get_rect()
        self.rect.x = 0
        #change the y after this is finalized
        self.rect.y = PLATFORM_HEIGHT
        
    def get_surface(self):
        return self.image
    def get_id_num(self):
        return self.id_num
    def update_x(self, new_x):
        self.rect.x = new_x
        
