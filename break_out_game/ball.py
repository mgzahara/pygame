import pygame, math
from info import *

class Ball(pygame.sprite.Sprite):
    """ This class represents the bullet. """
    
    def __init__(self, start_pos, dest_pos, velocity, size, color):
        """ Constructor.
        start_pos - (int, int) tuple denoting starting coordinates
        dest_pos  - (int, int) tuple denoting ending   coordinates
        velocity  - int, speed
        size - int size of one side of the square projectile
        color - (int, int, int) r,g,b color of projectile
        """
        
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        
        # Set up the image for the bullet
        self.image = pygame.Surface([size, size])
        self.image.fill(color)
        self.velocity = velocity
        self.rect = self.image.get_rect()
        
        # Move the bullet to our starting location
        self.rect.x = start_pos[0]
        self.rect.y = start_pos[1]
        
        # Because rect.x and rect.y are automatically converted
        # to integers, we need to create different variables that
        # store the location as floating point numbers. Integers
        # are not accurate enough for aiming.
        self.floating_point_x = start_pos[0]
        self.floating_point_y = start_pos[1]
        
        # Calculate the angle in radians between the start points
        # and end points. This is the angle the bullet will travel.
        x_diff = dest_pos[0] - start_pos[0]
        y_diff = dest_pos[1] - start_pos[1]
        angle = math.atan2(y_diff, x_diff);
        
        # Taking into account the angle, calculate our change_x
        # and change_y. Velocity is how fast the bullet travels.
        self.change_x = math.cos(angle) * self.velocity
        self.change_y = math.sin(angle) * self.velocity
        
    def update(self, *args):
        """ Move the projectile """

        if len(args) > 0:
            return
        
        # The floating point x and y hold our more accurate location.
        self.floating_point_y += self.change_y
        self.floating_point_x += self.change_x
        
        # The rect.x and rect.y are converted to integers.
        self.rect.y = int(self.floating_point_y)
        self.rect.x = int(self.floating_point_x)
        
        # If the bullet hits a screen edge, bounce it
        if self.rect.x < 0 or self.rect.x > SCREEN_WIDTH  - self.image.get_width():
            #invert x velocity
            self.change_x *= -1

        if self.rect.y < 0 or self.rect.y > SCREEN_HEIGHT - self.image.get_height():
            #invert y velocity
            self.change_y *= -1
        return

    def invert_change_x(self):
        self.change_x *= -1
        return
        
    def invert_change_y(self):
        self.change_y *= -1
        return

    def set_change_x(self, new_change_x):
        self.change_x = new_change_x
        return

    def set_change_y(self, new_change_y):
        self.change_y = new_change_y
        return

    def get_pos(self):
#        return (self.floating_point_x, self.floating_point_y)
        return (self.rect.x, self.rect.y)

    def hit_brick(self, inv):
        if inv == 'x':
            self.change_x *= -1
        elif inv == 'y':
            self.change_y *= -1
        elif inv == 'xy':
            self.change_x *= -1
            self.change_y *= -1
        print "inv:", inv
        print
        return
    #    def set_velocity(self, v):
    #        self.change_x = (self.change_x / self.velocity) * v
    #        self.change_y = (self.change_y / self.velocity) * v
    #        self.veocity = v
    #        return
    def hit_edge(self, edge_orientation):
        if edge_orientation == 'h':
            #collided w/ top or bottom
            self.change_y *= -1
        elif edge_orientation == 'v':
            #collided w/ left or right
            self.change_x *= -1
        else:
            #something else
            print "ball.hit_edge() received bad arguement:", edge_orientation
        return

    def get_id_num(self):
        pass
