"""
 Show how to fire bullets at the mouse.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
"""
import pygame
import math
from projectile import *
from info       import *
from enemy      import *
from player     import *
from hud        import *
from game       import *
from random     import randint

def game_loop():

    global done, tick, enemy_spawn_freq, SCREEN_WIDTH, SCREEN_HEIGHT, screen, all_sprites_list, block_list, bullet_list, clock, score
    player = Player()
    done = False
    all_sprites_list.add(player)
    player.rect.x = SCREEN_WIDTH / 2
    player.rect.y = SCREEN_HEIGHT / 2
    player_collisions = []

    # -------- Main Program Loop -----------
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
            
                # Create the bullet based on where we are, and where we want to go.
                bullet = Projectile(player.rect, pos, 5, 5, (0,0,0))
            
                # Add the bullet to the lists
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
                
        # --- Game logic

        if tick % enemy_spawn_freq == 0:
            create_enemy()
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
                print(score)

        player_collisions = pygame.sprite.spritecollide(player, block_list, True)
        if len(player_collisions) > 0:
            done = True
            
        # --- Draw a frame

        # Clear the screen
        screen.fill(WHITE)
    
        # Draw all the spites
        all_sprites_list.draw(screen)

        #draw score
        text_to_screen(screen, "Score: {0}".format(score), 0, 0)


    
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        
        #    print "tick: ", tick
        #    print "bullets: ", len(bullet_list)
        # --- Limit to 20 frames per second
        clock.tick(60)
#    screen.fill(WHITE)



# --- Create the window

# Initialize Pygame
pygame.init()
game = Game(screen)    
playing = True
end_game_text = "Would you like to try again? (y/n)"
while playing:
    print "playing ", playing
    #    game_loop()#play game
    game.play()
    screen.fill(WHITE)#clear screen
    text_to_screen(screen, end_game_text, SCREEN_WIDTH / 4, 200, size = 25)#play again?
    pygame.display.flip()#render
    valid = False
    while not valid:#only accept valid input
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_y] or keys[pygame.K_n]:
                    valid = True
    #what to do with valid input
    if keys[pygame.K_y]:
        playing = True
    elif keys[pygame.K_n]:
        playing = False


pygame.quit()
