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

#lives = 5
end = ""
text_font = pygame.font.SysFont(None, 30)
font = pygame.font.SysFont(None, 30)
screen_x =600
screen_y = 500
size = (screen_x, screen_y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
#classes go here
class Bullet(pygame.sprite.Sprite):
    def __init__(self, b_width , b_length):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = b_width
        self.rect.centery = b_length
    def update(self) :
        self.rect.y = self.rect.y - 5

#endclass
class spaceship(pygame.sprite.Sprite):
    def __init__(self, s_width, s_length, initial_x):
        super().__init__()
        self.x_val2 = x_val2
        self.width = s_width
        self.height = s_length
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE), 
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

        

class Invader(pygame.sprite.Sprite):
    def __init__(self, I_width, I_height ):
        super().__init__()
        self.width = I_width
        self.height = I_height
        self.speed = random.randrange(1,3)
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,600)
        self.rect.y = 0
        self.horizontalspeed = -1

    def update(self):
        if self.rect.y >= -50 :
            self.rect.y = self.rect.y - self.horizontalspeed
        if self.rect.y > screen_y:
            self.rect.y = -50
            
       


#global variables
x_val2 = 350
enemy_count = 5
x_val = 0
y_val = 200
x_offset = 1
pi= 3.141592652
counter = 0
end = ""
score = 0

#create sprite groups
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
invader_sprites = pygame.sprite.Group()
spaceship_sprite = pygame.sprite.Group()

# create player spaceship
player = spaceship(40 , 30 , x_val2)
spaceship_sprite.add(player)

#set the enemy count
Invader_Num = enemy_count


 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullet = Bullet(player.rect.centerx, player.rect.top)
            bullets.add(bullet)
            all_sprites.add(bullet)
    
    if len(invader_sprites) < Invader_Num:
        Invader_width = 30
        Invader_Length = 30 
        enemy = Invader(Invader_width, Invader_Length)
        invader_sprites.add(enemy)
        all_sprites.add(enemy)
        score = score + 1
    # --- Game logic should go here

    #check for collisions
    hits = pygame.sprite.groupcollide(invader_sprites, bullets, True, True)
    
    #update game objects
    all_sprites.update()
    spaceship_sprite.update()

    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    
    
    screen.fill(BLACK)
    
    #draw stuff here:
    all_sprites.draw(screen)
    spaceship_sprite.draw(screen)
    
    #messages at the top 
    realscore = score - 5
    score_count = font.render("Enemies Hit: " + str(realscore), True, WHITE)

    screen.blit(score_count, [10,10])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
#endwhile
pygame.quit()