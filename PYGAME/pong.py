import pygame
import random

# Initialize the game engine
pygame.init()

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

#screen dimensions
size = (800, 500)
#defines screen
screen = pygame.display.set_mode(size)
#sets done to false so the program loops
done=False
clock = pygame.time.Clock()

pygame.display.set_caption("Pong by Charlie")
# Starting position of the rectangle
rect_x = 380
rect_y = 230

user_y = 190
follow_y=190
# Speed and direction of rectangle
x_change = 5
y_change = 5
follow_change = 3
#starting background colour
random1=blue
#sets number of lives
lives=5
end = ""
score=0
# -------- Main Program Loop -----------
while done == False:

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
    
    # Set the screen background
    screen.fill(random1)
    # Draw the rectangle
    pygame.draw.rect(screen, white, [rect_x, rect_y, 20, 20])
    pygame.draw.rect(screen, black, [rect_x, rect_y, 20, 20], 2)

    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 50, True, False)
    text = font.render("Lives : " +str(lives), True, black) 
    # Put the image of the text on the screen at 250x250
    screen.blit(text, [315,10])

    # Select the font to use, size, bold, italics
    font2 = pygame.font.SysFont('Calibri', 25, True, False)
    text2 = font2.render("Score : " +str(score), True, black) 
    # Put the image of the text on the screen at 250x250
    screen.blit(text2, [10,10])

    endmessage = font.render(end, True, black)
    screen.blit(endmessage, [270,100])
    #draw the barriers
    player=pygame.draw.rect(screen, black, [20, user_y, 20, 120])
    pygame.draw.rect(screen, black, [760, user_y, 20, 120])
    
    # Move barriers
    key=pygame.key.get_pressed()
    if key[pygame.K_UP]:
        user_y=user_y-5
    elif key[pygame.K_DOWN]:
        user_y=user_y+5
    #endif
    
    rect_x = rect_x + x_change
    rect_y = rect_y + y_change
    #to bounce off barriers
    if rect_x==40 or rect_x ==740 :
        if ((user_y > rect_y and user_y < (rect_y + 120))or ((user_y + 120) > rect_y and (user_y + 120) < (rect_y + 120))):
            x_change = x_change * -1
            score =score+1
            random1= random.choice(colours)
    #to bounce off side wall
    if rect_y > 480 or rect_y < 0:
        y_change = y_change * -1
        random1= random.choice(colours)
    elif rect_x > 780 or rect_x <0:
       rect_x = 380
       rect_y = 230 
       lives = lives-1
    pygame.display.flip()
    #ends after 5 lives have been used
    if lives == 0:
        rect_x = 380
        rect_y = 230
        x_change=0
        y_change=0
        end = "GAME OVER"

    #end if
    clock.tick(60)
#end while