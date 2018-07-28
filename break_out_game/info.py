import pygame
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN =  (0  , 255, 0  )
PURPLE = (155, 89, 182 )
ORANGE = (230, 126, 34 )
YELLOW = (255, 255, 0  )

# Set the height and width of the screen
SCREEN_WIDTH  = 600
SCREEN_HEIGHT = 400

# set values used for platform stuff
PLATFORM_UNIT_WIDTH = 25
PLATFORM_UNIT_HEIGHT = 10
PLATFORM_DIM = [PLATFORM_UNIT_WIDTH, PLATFORM_UNIT_HEIGHT]
PLATFORM_HEIGHT = SCREEN_HEIGHT - 50

# set values for brick stuff
BRICK_WIDTH = 30
BRICK_HEIGHT = 10
BRICK_DIM = [BRICK_WIDTH, BRICK_HEIGHT]
BRICK_GAP = 3

# set values for ball stuff
BALL_SIZE = 10
BALL_VELOCITY = 2
BALL_START = (20, 20)
BALL_DEST = (180, 220)

# initialize universal screen object
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# list of all sprites
all_sprites_list = pygame.sprite.Group()

# List of each platform piece
platform_pieces_list = pygame.sprite.Group()

# list of all bricks
brick_list = pygame.sprite.Group()

# lists of all edges
top_edge_list = pygame.sprite.Group()
bottom_edge_list = pygame.sprite.Group()
left_edge_list = pygame.sprite.Group()
right_edge_list = pygame.sprite.Group()

# iteration of the game loop
tick = 0

# bool for game loop
playing = True

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# score
score = 0


def check_brick_collision(ball):
    global score
    #bool to prevent double brick break from tigerring the axis inversion twice, thus nullifying it
    collision = False
    edge_collision_list = pygame.sprite.spritecollide(ball, top_edge_list, False)
    for e in edge_collision_list:
        if not collision:
            collision = True
            ball.hit_edge(e.bounce_ball() )
        key = e.get_id_num()
        top_edge_list.update(   'remove', e.get_id_num() )
        bottom_edge_list.update('remove', e.get_id_num() )
        left_edge_list.update(  'remove', e.get_id_num() )
        right_edge_list.update( 'remove', e.get_id_num() )

        score += 1
        
        for s in iter(all_sprites_list):
            if s.get_id_num() == key:
                s.kill()

    collision = False
    edge_collision_list = pygame.sprite.spritecollide(ball, bottom_edge_list, False)
    for e in edge_collision_list:
        if not collision:
            collision = True
            ball.hit_edge(e.bounce_ball() )
        key = e.get_id_num()
        top_edge_list.update(   'remove', e.get_id_num() )
        bottom_edge_list.update('remove', e.get_id_num() )
        left_edge_list.update(  'remove', e.get_id_num() )
        right_edge_list.update( 'remove', e.get_id_num() )
        
        score += 1
        
        for s in iter(all_sprites_list):
            if s.get_id_num() == key:
                s.kill()

    collision = False
    edge_collision_list = pygame.sprite.spritecollide(ball, left_edge_list, False)
    for e in edge_collision_list:
        if not collision:
            collision = True
            ball.hit_edge(e.bounce_ball() )
        key = e.get_id_num()
        top_edge_list.update(   'remove', e.get_id_num() )
        bottom_edge_list.update('remove', e.get_id_num() )
        left_edge_list.update(  'remove', e.get_id_num() )
        right_edge_list.update( 'remove', e.get_id_num() )
        
        score += 1
        
        for s in iter(all_sprites_list):
            if s.get_id_num() == key:
                s.kill()

    collision = False
    edge_collision_list = pygame.sprite.spritecollide(ball, right_edge_list, False)
    for e in edge_collision_list:
        if not collision:
            collision = True
            ball.hit_edge(e.bounce_ball() )
        key = e.get_id_num()
        top_edge_list.update(   'remove', e.get_id_num() )
        bottom_edge_list.update('remove', e.get_id_num() )
        left_edge_list.update(  'remove', e.get_id_num() )
        right_edge_list.update( 'remove', e.get_id_num() )
        
        score += 1
        
        for s in iter(all_sprites_list):
            if s.get_id_num() == key:
                s.kill()                
                
    return score
