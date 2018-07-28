import pygame, random, math
from projectile import *
from info       import *

pygame.init()

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
        self.rect.y = 100

    def get_surface(self):
        return self.image
    def get_id_num(self):
        return self.id_num
    def update_x(self, new_x):
        self.rect.x = new_x


ball = Projectile((150, 100), (180, 200), 3, 10, RED)
all_sprites_list.add(ball)

platform_1 = PlatformPiece(BLUE,   1)
platform_2 = PlatformPiece(GREEN,  2)
platform_3 = PlatformPiece(PURPLE, 3)
platform_4 = PlatformPiece(ORANGE, 4)

platform_pieces_list.add(platform_1)
platform_pieces_list.add(platform_2)
platform_pieces_list.add(platform_3)
platform_pieces_list.add(platform_4)


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
            #update positions of platform pieces for collisions
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
        ball.invert_change_y()

    #for p in platform_collision_list:
        #print "collision!"
        #print "p: ", p.get_id_num()

#    print "ppl: ", platform_pieces_list
#    print "pcl: ", platform_collision_list
#    print
    #determine where to put everything    
    all_sprites_list.update()
    #clear screen
    screen.fill(WHITE)
    #draw each obj here

    left_edge = mouse_x - PLATFORM_WIDTH
    right_edge = mouse_x + PLATFORM_WIDTH

    #draw platform at mouse_x
    pygame.draw.line(screen, BLACK, (left_edge, SCREEN_HEIGHT - 50), (right_edge, SCREEN_HEIGHT - 50), 10)
    #draw new platform pieces
    screen.blit(platform_1.get_surface(), (mouse_x - (PLATFORM_UNIT_WIDTH * 2), 100))
    screen.blit(platform_2.get_surface(), (mouse_x + PLATFORM_UNIT_WIDTH, 100))
    screen.blit(platform_3.get_surface(), (mouse_x - PLATFORM_UNIT_WIDTH, 100))
    screen.blit(platform_4.get_surface(), (mouse_x, 100))
    #draw all sprites
    all_sprites_list.draw(screen)
    #render
    pygame.display.flip()
    #set refresh rate
    clock.tick(60)

pygame.quit()
