import pygame
import random


# Initialize the game engine
pygame.init()

# Define some colors
WHITE = ((255,255,255))
BLUE = ((0,0,255))
GREEN = ((0,255,0))
RED = ((255,0,0))
BLACK = ((0,0,0))
ORANGE = ((255,100,10))
YELLOW = ((255,255,0))
BLUE_GREEN = ((0,255,170))
MARROON = ((115,0,0))
LIME = ((180,255,100))
PINK = ((255,100,180))
PURPLE = ((240,0,255))
GREY = ((127,127,127))
MAGENTA = ((255,0,230))
BROWN = ((100,40,0))
FOREST_GREEN = ((0,50,0))
NAVY_BLUE= ((0,0,100))
RUST = ((210,150,75))
DANDILION_YELLOW = ((255,200,0))
HIGHLIGHTER = ((255,255,100))
SKY_BLUE = ((0,255,255))
MOONGLOW = ((235,245,255))


done = False
clock = pygame.time.Clock()

screen_x =200
screen_y = 200
size = (screen_x, screen_y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PacMan?")

##--Definetheclasstilewhichisasprite
class Block(pygame.sprite.Sprite):
    #Define the constructor for invader
    def __init__(self,colour,width,height,x_ref,y_ref):
        #Call the sprite constructor
        super().__init__()
        #Create a sprite and fill it with colour
        self.image=pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect=self.image.get_rect()#Set theposition of the player attributes
        self.rect.x=x_ref
        self.rect.y=y_ref

class Player(pygame.sprite.Sprite):
    def __init__(self, s_width, s_length, initial_x):
        super().__init__()
        self.x_val2 = x_val
        self.width = s_width
        self.height = s_length
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(YELLOW), 
        self.rect = self.image.get_rect()
        self.rect.x = initial_x
        self.rect.y = 465

    

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 700:
            self.rect.right = 700

map =[[1,1,1,1,1,1,1,1,1,1], 
    [1,0,0,1,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,1,0,1],
    [1,1,0,1,1,1,1,0,0,1], 
    [1,0,0,0,0,0,1,1,0,1],
    [1,0,1,1,1,0,1,0,0,1],
    [1,0,0,0,1,0,1,1,0,1], 
    [1,0,1,1,1,0,1,0,0,1], 
    [1,0,0,0,0,0,0,0,1,1], 
    [1,1,1,1,1,1,1,1,1,1]]


#Create a list of all sprites
all_sprites_list=pygame.sprite.Group()

#Create a list of tiles for the walls
wall_list=pygame.sprite.Group()

#Create walls on the screen (each tile is 20x20 so alter cords)
for y in range(10):
    for x in range(10):
        if map[x][y]==1:
            my_wall=Block(BLUE,20,20,(x*20),(y*20))
            wall_list.add(my_wall)
            all_sprites_list.add(my_wall)

# -------- Main Program Loop -----------
while done == False:

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
        # Set the screen background
        screen.fill(BLACK)
        #draw 
        wall_list.draw(screen)
   

        #game logic

        pygame.display.flip()

        clock.tick(60)
#end while