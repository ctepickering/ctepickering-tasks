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

block_xsize1=120
block_xsize2=120
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

user_y2=190
user_y = 190
follow_y=190
# Speed and direction of rectangle
x_change = 5 or 10
y_change = 4
follow_change = 3
#starting background colour
random1=blue
#sets number of lives
lives=0
lives2=0
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
    text = font.render(str(lives2), True, black) 
   
    screen.blit(text, [590,10])
    font2 = pygame.font.SysFont('Calibri', 50, True, False)
    text2 = font2.render(str(lives), True, black) 
    
    screen.blit(text2, [190,10])

    #displays winner at end
    endmessage = font.render(end, True, black)
    screen.blit(endmessage, [230,100])
    #draw the barriers
    player=pygame.draw.rect(screen, black, [20, user_y2, 20, block_xsize1])
    pygame.draw.rect(screen, black, [760, user_y, 20, block_xsize2])
    
    # Move barriers
    key=pygame.key.get_pressed()
    if key[pygame.K_UP]:
        user_y=user_y-5
    elif key[pygame.K_DOWN]:
        user_y=user_y+5
    #endif
    key2=pygame.key.get_pressed()
    if key2[pygame.K_w]:
        user_y2=user_y2-5
    elif key2[pygame.K_s]:
        user_y2=user_y2+5
    #endif
    
    rect_x = rect_x + x_change
    rect_y = rect_y + y_change
    #to bounce off barriers
    if rect_x==40 or rect_x==740 :
        if rect_y >= user_y2  and rect_y <= user_y2 + block_xsize1 or rect_y >= user_y  and rect_y <= user_y + block_xsize2:
            x_change = x_change * -1
            score =score+1
            random1= random.choice(colours)
    #to bounce off side wall
    if rect_y > 480 or rect_y < 0:
        y_change = y_change * -1
        random1= random.choice(colours)
    elif rect_x > 780 :
       rect_x = 40
       rect_y = user_y+40 
       lives = lives+1
    elif rect_x <0:
        rect_x = 740
        rect_y = user_y2+40
        lives2 = lives2+1
    pygame.display.flip()
    #ends after 5 lives have been used
    if lives == 5:
        rect_x = 380
        rect_y = 230
        x_change=0
        y_change=0
        end = "Left player wins!"
    elif lives2 == 5:
        rect_x = 380
        rect_y = 230
        x_change=0
        y_change=0
        end = "Right player wins!"
        random1=white
    #end if
    clock.tick(60)
#end while