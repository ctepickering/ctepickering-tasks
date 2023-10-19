import pygame
import random
import math
# Define some colors

pygame.init()

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

pygame.display.set_caption("Space invaders")


# set screen
size = (800, 500)
screen = pygame.display.set_mode(size)

# Snowflake class
class invader(pygame.sprite.Sprite):
    #constructor function
    def __init__(self):
        self.size_x = 30
        self.size_y =30
        self.image = pygame.Surface([self.size_x, self.size_y])
        self.rect=self.image.get_rect()
        self.rect.x = random.randint(0, 800)
        self.rect.y = random.randint(-50,0)
        self.size = 20
        self.speed = 1
        self.speed2=0
    #end of con func
    def update(self):
        self.rect.y += self.speed
        self.rect.x +=self.speed2
        if self.rect.y > 500:
            self.rect.y = -self.size
            self.rect.x = random.randint(0, 800)

    def draw(self, screen):
        pygame.draw.rect(screen, blue , [self.rect.x, self.rect.y, self.size_x,self.size_y])
#end of class snow

class Player(pygame.sprite.Sprite) :
    def __init__(self):
        self.size_x = 20
        self.size_y =20
        self.image = pygame.Surface([self.size_x, self.size_y])
        self.rect=self.image.get_rect()
        self.rect.x = 390
        self.rect.y = 470
        self.speed = 5
        self.lives = 5
    def update(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x= self.rect.x-self.speed
        elif key[pygame.K_RIGHT]:
            self.rect.x= self.rect.x+self.speed
        pygame.draw.rect(screen, dandilion_yellow , [self.rect.x, self.rect.y, self.size_x,self.size_y])

class Bullet(pygame.sprite.Sprite) :
    def __init__(self):
        
        self.image = pygame.Surface([2, 5]) 
        self.rect=self.image.get_rect()
        self.bullet_count = 50
        self.rect.x = 400
        self.rect.y = 400
        self.speed = 0
        self.color = black
    def update(self):
        key=pygame.key.get_pressed()
        self.rect.y = self.rect.y-self.speed
        pygame.draw.rect(screen, self.color , [self.rect.x,self.rect.y,2,5])
        if key[pygame.K_SPACE]:
            if self.rect.y >-10:
                self.speed = 5
                self.color =white
            #next i
        #end if

#-Global Varaibles
done=False
colours = [blue,green,red,purple,pink,orange,blue_green]

number_of_invaders=10
invaders = [invader() for _ in range(number_of_invaders)]
player= Player()
clock = pygame.time.Clock()
bullet=Bullet()

#creates a list of the invaders
invader_group=pygame.sprite.Group()
all_sprites_group=pygame.sprite.Group()

# -------- Main Program Loop -----------
while done == False:

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        #creates a list of the invaders
        invader_group=pygame.sprite.Group()
         
 
    # Set the screen background
    screen.fill(black)

    #draw 
    font = pygame.font.SysFont('Calibri', 20, True, False)
    text = font.render("Lives : "+str(player.lives), True, white) 
   
    screen.blit(text, [700,10])
    
    player.update()
    bullet.update()
    for enemy in invaders:
        enemy.update()
        enemy.draw(screen)

    #game logic
    player_hit_group=pygame.sprite.spritecollide(player,invader_group,True)
    for foo in player_hit_group:
        player.lives=player.lives-1
    
    pygame.display.flip()

    clock.tick(60)
#end while