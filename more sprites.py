import pygame
import random

pygame.init()
pygame.display.set_caption('Rocket in Space')
# Set the height and width of the screen
screen_width=700
screen_height=500
screen = pygame.display.set_mode([screen_width,screen_height])

#Define the Player sprite
#Player starts at (0,0) by default

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"E:\Sruthi\Python Game Developer II\Lesson 8\s1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70,100))
        self.rect = self.image.get_rect()
    # Move the sprite based on keypresses
    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height

#end of the class
class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"E:\Sruthi\Python Game Developer II\Lesson 8\f1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70,100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(0, screen_height - self.rect.height)


#make a group os all the sprites
sprites = pygame.sprite.Group()
foods = pygame.sprite.Group()

def startgame():
    player = Player()
    sprites.add(player)
    food=Food()
    foods.add(food)

    score = 0

# Font for displaying score
    font = pygame.font.Font(None, 36)
    
    #start the game loop
    while True:
        #Look at every event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # if it is quit the game
                pygame.quit() 
                exit(0)
        #Get the set of keys pressed and check for user input
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        collisions = pygame.sprite.spritecollide(player, foods, True)
        if collisions:
            score += len(collisions)
        # Add background image
        screen.blit(pygame.image.load(r"E:\Sruthi\Python Game Developer II\Lesson 8\b.png"),(0,0))

        #draw the sprites
        sprites.draw(screen)
        foods.draw(screen)
        score_text = font.render(f"Score: {score}", True,"black")
        screen.blit(score_text, (10, 10))
    
        pygame.display.update()


startgame()


          
