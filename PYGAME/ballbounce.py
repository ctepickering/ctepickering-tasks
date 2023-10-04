import pygame
import math
import random

# Define some colors
white = ((255,255,255))
blue = ((0,0,255))
green = ((0,255,0))
red = ((255,0,0))
black = ((0,0,0))
orange = ((255,100,10))
yellow = ((255,255,0))
blue_green = ((0,255,170))
marroon = ((115,0,0))
lime = ((180,255,100))
pink = ((255,100,180))
purple = ((240,0,255))
gray = ((127,127,127))
magenta = ((255,0,230))
brown = ((100,40,0))
forest_green = ((0,50,0))
navy_blue = ((0,0,100))
rust = ((210,150,75))
dandilion_yellow = ((255,200,0))
highlighter = ((255,255,100))
sky_blue = ((0,255,255))
light_gray = ((200,200,200))
dark_gray = ((50,50,50))
tan = ((230,220,170))
coffee_brown =((200,190,140))
moon_glow = ((235,245,255))
colours = [blue,green,red,yellow,purple,pink,orange,blue_green]
size = (700, 500)
screen = pygame.display.set_mode(size)
done=False

# Starting position of the rectangle
rect_x = 50
rect_y = 50
count=0
# Speed and direction of rectangle
x_change = 10
y_change = 10
clock = pygame.time.Clock()
random1=blue
# -------- Main Program Loop -----------
while done == False:

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # Set the screen background
    screen.fill(random1)
    # Draw the rectangle
    pygame.draw.rect(screen, white, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(screen, black, [rect_x, rect_y, 50, 50], 3)

 
    # Move the rectangle starting point
    rect_x = rect_x + x_change
    rect_y = rect_y + y_change
    if rect_y > 450 or rect_y < 0:
        y_change = y_change * -1
        random1= random.choice(colours)
    elif rect_x > 650 or rect_x <0:
        x_change = x_change * -1
        random1= random.choice(colours)
    pygame.display.flip()

    clock.tick(60)
#end while