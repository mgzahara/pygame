import pygame
from info import *

class Block(pygame.sprite.Sprite):
    def __init__(self, color, dim, pos):
        # color (int, int, int) rgb color - tuple
        # dim [int, int] width, height - array
        # pos [int, int] x, y position of top left corner-  array
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface(dim)
        self.image.fill(color)
        
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        

    def update(self, *args):
        if len(args) == 2:
            if args[0] == 'move':
                #move terrain in opposite direction of key press
                if args[1] == 'left':
                    self.rect.x += UNIT_SIZE
                elif args[1] == 'right':
                    self.rect.x -= UNIT_SIZE
                elif args[1] == 'up':
                    self.rect.y += UNIT_SIZE
                elif args[1] == 'down':
                    self.rect.y -= UNIT_SIZE
                
class Player(Block):
    def __init__(self, color, dim, pos, maze_pos = [1, -2]):
        # color (int, int, int) rgb color - tuple
        # dim [int, int] width, height - array
        # pos [int, int] x, y position of top left corner - array
        # maze_pos [int, int] indeces into the maze obj in main
        Block.__init__(self, color, dim, pos)

        self.maze_pos_x = maze_pos[0]
        self.maze_pos_y = maze_pos[1]
        

    def update(self, *args):

        if len(args) == 2:
            if args[0] == 'move':
                #move terrain in opposite direction of key press
                if args[1] == 'left':
                    self.maze_pos_y -= 1
                elif args[1] == 'right':
                    self.maze_pos_y += 1
                elif args[1] == 'up':
                    self.maze_pos_x -= 1
                elif args[1] == 'down':
                    self.maze_pos_x += 1
                #print [self.maze_pos_x, self.maze_pos_y]
                return
            
    def get_maze_pos(self):
        return [self.maze_pos_y, self.maze_pos_x]
                
