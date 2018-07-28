import pygame, random, math
from ball           import *
from info           import *
from platform_piece import *
from brick          import *
from hud import *

pygame.init()

ball = Ball(BALL_START, BALL_DEST, BALL_VELOCITY, BALL_SIZE, RED)
all_sprites_list.add(ball)

platform_1 = PlatformPiece(BLUE,   1)
platform_2 = PlatformPiece(GREEN,  2)
platform_3 = PlatformPiece(PURPLE, 3)
platform_4 = PlatformPiece(ORANGE, 4)

platform_pieces_list.add(platform_1)
platform_pieces_list.add(platform_2)
platform_pieces_list.add(platform_3)
platform_pieces_list.add(platform_4)

left_edge = 50
top_edge = 100
edge_id = 1
for i in range(10):
    brick_y = top_edge + ((BRICK_HEIGHT + BRICK_GAP) * i)
    for j in range(15):
        brick_x = left_edge + ((BRICK_WIDTH + BRICK_GAP) * j)

        top = Edge( (brick_x, brick_y), 'h', edge_id)
        bottom = Edge( (brick_x, brick_y + BRICK_HEIGHT), 'h', edge_id)
        left = Edge( (brick_x, brick_y), 'v', edge_id)
        right = Edge( (brick_x + BRICK_WIDTH, brick_y), 'v', edge_id)

        edge_id += 1
        
        top_edge_list.add(top)
        bottom_edge_list.add(bottom)
        left_edge_list.add(left)
        right_edge_list.add(right)
        all_sprites_list.add(top)
        all_sprites_list.add(bottom)
        all_sprites_list.add(left)
        all_sprites_list.add(right)
        #new_brick = Brick( (brick_x, brick_y) )
        #brick_list.add(new_brick)
        #all_sprites_list.add(new_brick)

print "number of bricks:", len(brick_list)

while playing:
#    keys = pygame.key.get_pressed()
    tick += 1
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            playing = False

        if event.type == pygame.MOUSEMOTION:
            #update positions of platform pieces - logical positions
            #would be better to use sprite.group.update()
            for p in platform_pieces_list:
                if p.get_id_num() == 1:
                    p.update_x(mouse_x - (PLATFORM_UNIT_WIDTH * 2) )

                elif p.get_id_num() == 2:
                    p.update_x(mouse_x + PLATFORM_UNIT_WIDTH)

                elif p.get_id_num() == 3:
                    p.update_x(mouse_x - PLATFORM_UNIT_WIDTH)

                elif p.get_id_num() == 4:
                    p.update_x(mouse_x)
            
            
    platform_collision_list = pygame.sprite.spritecollide(ball, platform_pieces_list, False)
    if len(platform_collision_list) > 0:
        # here is where you would change the x velocity based on
        # which part of the platform was collided with
        ball.invert_change_y()

    #    brick_collision_list = pygame.sprite.spritecollide(ball, brick_list, False)
    #    for b in brick_collision_list:
    #        print "collision at tick ", tick
    #        print "with len(", len(brick_collision_list), ")"
    #ret line is flawed - call bounce_ball on b
    #        ret = brick_collision_list[0].bounce_ball( ball.get_pos() )
    #        ball.hit_brick(ret)
    #score line is flawed - only add 1
    #        score += len(brick_collision_list)
    #        print "score:", score
    #        brick_list.remove(b)
    #        b.kill()

    score = check_brick_collision(ball)

    #determine where to put everything    
    all_sprites_list.update()
    #clear screen
    screen.fill(WHITE)

    
    #draw new platform pieces - visual positions
    screen.blit(platform_1.get_surface(), (mouse_x - (PLATFORM_UNIT_WIDTH * 2), PLATFORM_HEIGHT))
    screen.blit(platform_2.get_surface(), (mouse_x + PLATFORM_UNIT_WIDTH, PLATFORM_HEIGHT))
    screen.blit(platform_3.get_surface(), (mouse_x - PLATFORM_UNIT_WIDTH, PLATFORM_HEIGHT))
    screen.blit(platform_4.get_surface(), (mouse_x, PLATFORM_HEIGHT))
    #draw all sprites
    all_sprites_list.draw(screen)
    #update score
    text_to_screen(screen, "Score: {0}".format(score), 10, 10)
    #render
    pygame.display.flip()
    #set refresh rate
    clock.tick(60)

pygame.quit()
