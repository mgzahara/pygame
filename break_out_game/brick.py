import pygame
from info import *

### NEXT IDEA FOR PROPER COLLISION
### create a sub-sprite for each side
### accept the ball object as an arguement
### check the ball's collision with each
### inform ball to bounce off apropriately

class Brick(pygame.sprite.Sprite):
    def __init__(self, pos, color = YELLOW):
        '''
        pos   - (int, int) x, y coordinates to place brick
        color - (int, int, int) r,g,b values
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(BRICK_DIM)
        self.image.fill(color)
#        self.id_num = id_num
        # logical location/size for collision
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        ### CREATE AN EDGE CLASS AND INSTANTIATE IT HERE FOR EACH EDGE
        ### SIMLIARLY TO HOW THE ABOVE SURFACE IS CREATED
        
        # top and bottom edges are the same dimensions, but in different locations
        self.top_edge    = pygame.Surface( [BRICK_WIDTH, 1] )
        self.bottom_edge = pygame.Surface( [BRICK_WIDTH, 1] )
        # set their locations now

        # left and right edges are the same dimensions, but in different locations
        self.left_edge  = pygame.Surface( [1, BRICK_HEIGHT] )
        self.right_edge = pygame.Surface( [1, BRICK_HEIGHT] )
        # set their locations now





        
    def get_surface(self):
        return self.image

    def bounce_ball(self, ball_pos):
        inversion = 'q'
        left   = self.rect.x
        right  = self.rect.x + self.image.get_width()
        top    = self.rect.y
        bottom = self.rect.y + self.image.get_height()
        bools = [0] * 8
        #0 - left
        #1 - top/left
        #2 - top
        #3 - top/right
        #4 - right
        #5 - bottom/right
        #6 - bottom
        #7 - bottom/left

        # cardinal directions
        bools[0] = ball_pos[0] <  left
        bools[2] = ball_pos[1] <  top
        bools[4] = ball_pos[0] >= right
        bools[6] = ball_pos[1] >= bottom
        # others
        bools[1] = bools[0] and bools[2]
        bools[3] = bools[2] and bools[4]
        bools[5] = bools[4] and bools[6]
        bools[7] = bools[6] and bools[0]

        if not bools[1] and bools[3] and bools[5] and bools[7]:
            # not in a corner zone
            if bools[0] or bools[4]:
                return 'x'
            if bools[2] or bools[6]:
                return 'y'
        else:
            # IS in a corner zone
            if bools[1]:
                #top/left
                ref_pos = [self.rect.x, self.rect.y]
                x_diff = abs(ball_pos[0] - ref_pos[0])
                y_diff = abs(ball_pos[1] - ref_pos[1])

                if min(x_diff, y_diff) == y_diff:
                    return 'x'
                elif min(x_diff, y_diff) == x_diff:
                    return 'y'
                else:
                    return 'xy'
                
            elif bools[3]:
                #top/right
                ref_pos = [self.rect.x + self.image.get_width(), self.rect.y]
                x_diff = abs(ball_pos[0] - ref_pos[0])
                y_diff = abs(ball_pos[1] - ref_pos[1])

                if min(x_diff, y_diff) == y_diff:
                    return 'x'
                elif min(x_diff, y_diff) == x_diff:
                    return 'y'
                else:
                    return 'xy'
                
            elif bools[5]:
                #bottom/right
                ref_pos = [self.rect.x + self.image.get_width(), self.rect.y + self.image.get_height()]
                x_diff = abs(ball_pos[0] - ref_pos[0])
                y_diff = abs(ball_pos[1] - ref_pos[1])

                if min(x_diff, y_diff) == y_diff:
                    return 'y'
                elif min(x_diff, y_diff) == x_diff:
                    return 'x'
                else:
                    return 'xy'
                
            elif bools[7]:
                #bottom/left
                ref_pos = [self.rect.x, self.rect.y + self.image.get_height()]
                x_diff = abs(ball_pos[0] - ref_pos[0])
                y_diff = abs(ball_pos[1] - ref_pos[1])

                #the only way to be in this zone is if it hit dead on the corner, or hit the bottom
                if x_diff == 0 and y_diff == 0:
                    return 'xy'
                else:
                    return 'y'


        return inversion





class Edge(pygame.sprite.Sprite):
    def __init__(self, pos, orientation, id_num, color = BLACK):
        '''
        pos   - (int, int) x, y coordinates to place brick
        orientation - (string/char) 'h' or 'v' for horizontal or vertical
        color - (int, int, int) r,g,b values
        '''
        pygame.sprite.Sprite.__init__(self)
        if orientation == 'h':
            #horizontal edge
            self.image = pygame.Surface([BRICK_WIDTH, 1])
        elif orientation == 'v':
            #vertical edge
            self.image = pygame.Surface([1, BRICK_HEIGHT])
        else:
            #not specified
            self.image = pygame.Surface(BRICK_DIM)
            
        self.image.fill(color)
        self.id_num = id_num
        self.orientation = orientation
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def get_surface(self):
        return self.image

    def get_id_num(self):
        return self.id_num
    
    def bounce_ball(self):
        return self.orientation

    def update(self, *args):
        if len(args) == 2 and args[0] == 'remove':
            if args[0] == self.id_num:
                return self
