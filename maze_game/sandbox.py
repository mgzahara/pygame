import pygame, random
from hud import *
from info import *
from block import *
from create_maze import *

#start pygame
pygame.init()

maze = make_maze(h=12, w=8)

#make terrain
for i in range(len(maze) ):
    for j in range(len(maze[i]) ):
        if maze[i][j]:
            block_x = TERRAIN_X_START + (UNIT_SIZE * i)
            block_y = TERRAIN_Y_START + (UNIT_SIZE * j)
            #color = COLORS[ random.randint( 0, len( COLORS ) - 1 ) ]
            color = BLACK
            b = Block(color, [UNIT_SIZE] * 2, [block_x, block_y])
            terrain_list.add(b)
            all_sprites_list.add(b)

player = Player(BLUE, [UNIT_SIZE] * 2, PLAYER_DIM)
player_list.add(player)
all_sprites_list.add(player)


while playing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                playing = False

            if inside_maze:
                if event.key == pygame.K_LEFT:
                    all_sprites_list.update('move', 'left')
                    last_move = 'left'
                if event.key == pygame.K_RIGHT:
                    all_sprites_list.update('move', 'right')
                    last_move = 'right'
                if event.key == pygame.K_UP:
                    all_sprites_list.update('move', 'up')
                    last_move ='up'
                if event.key == pygame.K_DOWN:
                    all_sprites_list.update('move', 'down')
                    last_move = 'down'
            else:
                if event.key == pygame.K_RIGHT:
                    starting_rights += 1
                    all_sprites_list.update('move', 'right')
                    last_move = 'right'
                    if starting_rights == 3:
                        inside_maze = True

                    
    #do all the updating
    terrain_collision_list = pygame.sprite.spritecollide(player, terrain_list, False)
    if len(terrain_collision_list) > 0:
        if last_move == 'left':
            all_sprites_list.update('move', 'right')
        if last_move == 'right':
            all_sprites_list.update('move', 'left')
        if last_move == 'up':
            all_sprites_list.update('move', 'down')
        if last_move == 'down':
            all_sprites_list.update('move', 'up')

        #print "colliding with", len(terrain_collision_list), "ojbects"


    #do all the redrawing
    screen.fill(WHITE)
    #draw maze
    terrain_list.draw(screen)
    #draw player
    player_list.draw(screen)
    #draw hud
    text_to_screen(screen, 'player pos: {}'.format(player.get_maze_pos() ), 10, 10)
    
    
    pygame.display.flip()

    #do the 'while key pressed' movement, but set the refresh rate to something really low
    clock.tick(60)

pygame.quit()
