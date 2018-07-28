import pygame, math
from random import randint
from projectile import *
#from enemy      import *
#from player     import *
#from hud        import *

class Game():
    def __init__(self, screen):
        #initialize all variables
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        self.screen = screen
        self.SCREEN_WIDTH  = self.screen.get_width()
        self.SCREEN_HEIGHT = self.screen.get_height()



        
    def play(self):
#        difficulty = 1
        tick = 0     
        done = False
        all_sprites_list = pygame.sprite.Group()
        block_list = pygame.sprite.Group()
        bullet_list = pygame.sprite.Group()
        player_collisions = []
        clock = pygame.time.Clock()
        score = 0
        player = Player()
        player.rect.x = self.SCREEN_WIDTH / 2
        player.rect.y = self.SCREEN_HEIGHT / 2
        enemy_spawn_freq = 60# / difficulty

        all_sprites_list.add(player)
        
        while not done:
            # --- Event Processing
            tick += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Fire a bullet if the user clicks the mouse button
                    
                    # Get the mouse position
                    pos = pygame.mouse.get_pos()
                    
                    mouse_x = pos[0]
                    mouse_y = pos[1]
                    
                    bullet = Projectile(player.rect, pos, 5, 5, (0,0,0))
                    # Add the bullet to the lists
                    all_sprites_list.add(bullet)
                    bullet_list.add(bullet)



            if tick % enemy_spawn_freq == 0:
                e = create_enemy()
                block_list.add(e)
                all_sprites_list.add(e)  
                    
                # Call the update() method on all the sprites
            all_sprites_list.update()

                # Calculate mechanics for each bullet
            for bullet in bullet_list:
                # See if it hit a block
                block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
                        
                    # For each block hit, remove the bullet and add to the score
                for block in block_hit_list:
                    bullet_list.remove(bullet)
                    all_sprites_list.remove(bullet)
                    score += 1
                    #check for player collisions
            player_collisions = pygame.sprite.spritecollide(player, block_list, True)
            if len(player_collisions) > 0:
                        #player got hit
                done = True
                # Clear the screen
            self.screen.fill(self.WHITE)
                    
            # Draw all the sprites
            all_sprites_list.draw(self.screen)
                    
            #draw score
            text_to_screen(self.screen, "Score: {0}".format(score), 0, 0)
            
            pygame.display.flip()
            
            clock.tick(60)
        
