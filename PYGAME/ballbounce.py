import pygame
import math

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
YELLOW   = (232,255,0)
SKY      = (0,192,255,)
BROWN    =(60,0,0)

size = (700, 500)
screen = pygame.display.set_mode(size)
done=False

# Starting position of the rectangle
rect_x = 50
rect_y = 50
 
# Speed and direction of rectangle
rect_change_x = 5
rect_change_y = 5
 
# -------- Main Program Loop -----------
while done == False:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the rectangle
    pygame.draw.rect(screen, RED, [rect_x, rect_y, 100, 100])

 
    # Move the rectangle starting point
    rect_x += rect_change_x
    rect_y += rect_change_y
    if rect_y > 450:
        rect_change_y = rect_change_y * -1