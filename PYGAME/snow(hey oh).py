import pygame
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

pygame.display.set_caption("Snow (hey oh)")

# set screen
size = (800, 500)
screen = pygame.display.set_mode(size)

# Snowflake class
class Snowflake:
    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 500)
        self.size = random.randint(1, 4)
        self.speed = random.randint(1, 5)
        self.speed2=random.randint(-2,2)

    def move(self):
        self.y += self.speed
        self.x +=self.speed2
        if self.y > 500:
            self.y = -self.size
            self.x = random.randint(0, 800)

    def draw(self, screen):
        pygame.draw.circle(screen, white, (self.x, self.y), self.size)
#end of class snow

#-Global Varaibles
done=False
colours = [blue,green,red,purple,pink,orange,blue_green]
snow_group=pygame.sprite.Group()
number_of_flakes=250
# Create snowflakes
snowflakes = [Snowflake() for _ in range(number_of_flakes)]


clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while done == False:

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # Set the screen background
    screen.fill(navy_blue)

    #draw 

    for snowflake in snowflakes:
        snowflake.move()
        snowflake.draw(screen)

    #game logic

    pygame.display.flip()

    clock.tick(60)
#end while