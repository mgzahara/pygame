# Import a library of functions called 'pygame'
import pygame, hud
from math import pi

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK =  (  0,   0,   0)
WHITE =  (255, 255, 255)
BLUE =   (  0,   0, 255)
GREEN =  (  0, 255,   0)
RED =    (255,   0,   0)
GRAY =   (128, 128, 128)
LIME =   (  0, 255,   0)
PURPLE = (128,   0, 128)
TEAL =   (  0, 128, 128)
YELOW =  (255, 255,   0)


# Set the height and width of the screen
size = [400, 300]
screen = pygame.display.set_mode(size)
circle_pos = [0,0]
circle_mov = 5

pygame.display.set_caption("Move the circle with the arrow keys!")

#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

while not done:
    keys = pygame.key.get_pressed() 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
    
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
    if keys[pygame.K_UP]:
        circle_pos[1] = circle_pos[1] - circle_mov
    if keys[pygame.K_DOWN]:
        circle_pos[1] = circle_pos[1] + circle_mov
    if keys[pygame.K_LEFT]:
        circle_pos[0] = circle_pos[0] - circle_mov
    if keys[pygame.K_RIGHT]:
        circle_pos[0] = circle_pos[0] + circle_mov
            
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
    
    # Clear the screen and set the screen background
    screen.fill(WHITE)
    
    # Draw a circle
    pygame.draw.circle(screen, BLUE, circle_pos, 40)

    #HUD
    hud.text_to_screen(screen, "pos: {0}".format(circle_pos), 0, 0)
    
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
    
# Be IDLE friendly
pygame.quit()
