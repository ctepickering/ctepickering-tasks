import pygame

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
YELLOW   = (232,255,0)
SKY      = (0,192,255,)
BROWN    =(60,0,0)
# Loop until the user clicks the close button.
done = False
#stores value of pi
PI = 3.141592653
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
size = (700, 500)
screen = pygame.display.set_mode(size)
xval = 0
yval = 200
multi= 0.9
colour=SKY
sun=YELLOW
count=1
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # --- Game logic should go here
    xval=xval+1
    if xval> size[0] :
        xval = -50
        yval = 220
        if count%2 !=0:
            colour=BLACK
            sun = WHITE
            pygame.draw.ellipse(screen,WHITE,[10,40,5,5])
            pygame.draw.ellipse(screen,WHITE,[300,20,5,5])
            count = count +1

        else:
            colour=SKY
            sun=YELLOW
            count =count+1
        #endif
    elif xval> 310 :
        yval=yval+0.5
    else :
        yval =yval-0.5

    #end if
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command
    screen.fill(colour)
    # --- Drawing code should go here
    pygame.draw.ellipse(screen,sun,[xval,yval,70,70])

    pygame.draw.rect(screen,GREEN,[0,300,700,200])
    pygame.draw.rect(screen,BLUE,[250,220,200,200])
    pygame.draw.polygon(screen, BROWN, [[350,150], [200,240], [500,240]])
    pygame.draw.rect(screen,WHITE,[275,250,50,60])
    pygame.draw.rect(screen,WHITE,[375,250,50,60])
    pygame.draw.rect(screen,BLACK,[275,250,50,60], 3)
    pygame.draw.rect(screen,BLACK,[375,250,50,60], 3)
    pygame.draw.rect(screen,BROWN,[325,350,50,70])
    pygame.draw.rect(screen,BLACK,[325,350,50,70], 3)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
    #next
#endwhile