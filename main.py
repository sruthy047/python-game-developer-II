import pygame
import random
from pygame.locals import*
import time

import pygame.locals

pygame.init()
pygame.display.set_caption("Recycle Marathon")
screen_width = 900
screen_height=700
screen=pygame.display.set_mode([screen_width,screen_height])

def changebackground(img):
    background=pygame.image.load(img)
    bg=pygame.transform.scale(background,(screen_width,screen_height))
    screen.blit(bg,(0,0))

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('E:/Sruthi/Python Game Developer II/Lesson 10/images/bin.png').convert_alpha()
        self.image=pygame.transform.scale(self.image,(40,60))
        self.rect=self.image.get_rect()

class Recyclable(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image=pygame.image.load(img).convert_alpha()
        self.image=pygame.transform.scale(self.image,(30,30))
        self.rect=self.image.get_rect()

class Non_Recyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("E:/Sruthi/Python Game Developer II/Lesson 10/images/plastic.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(40,40))
        self.rect=self.image.get_rect()

images=["E:/Sruthi/Python Game Developer II/Lesson 10/images/item1.png","E:/Sruthi/Python Game Developer II/Lesson 10/images//item2.png","E:/Sruthi/Python Game Developer II/Lesson 10/images/item3.png"]

item_list=pygame.sprite.Group()
allsprites=pygame.sprite.Group()
plastic_list=pygame.sprite.Group()

for i in range(60):
    item=Recyclable(random.choice(images))
    item.rect.x=random.randrange(screen_width)
    item.rect.y=random.randrange(screen_height)
    item_list.add(item)
    allsprites.add(item)

for i in range(15):
    plastic=Non_Recyclable()
    plastic.rect.x=random.randrange(screen_width)
    plastic.rect.y=random.randrange(screen_height)
    plastic_list.add(plastic)
    allsprites.add(plastic)

bin=Bin()
allsprites.add(bin)

WHITE=(255,255,255)
RED=(255,0,0)

playing=True
score=0
clock=pygame.time.Clock()
start_time=time.time()
myFont=pygame.font.SysFont("Cursive",25)
timingFont=pygame.font.SysFont("Times New Roman",25)
text=myFont.render("Score = ",str(0),True,WHITE)


while playing:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing=False

    timeElapsed= time.time()-start_time
    if timeElapsed>=60:
        if score>50:
            text=myFont.render("Bin loot successfully",True,RED)
            #changebackground("winscreen.png")
        else:
            text=myFont.render("Better luck next time",True,WHITE)
            #changeBackground("losescreen.png")
        screen.blit(text,(250,50))
    else:
        changebackground("E:/Sruthi/Python Game Developer II/Lesson 10/images/bground.png")
        countDown=timingFont.render("Time Left: "+str(60-int(timeElapsed)),True,WHITE)
        screen.blit(countDown,(20,10))

        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if bin.rect.y>0:
                bin.rect.y-=5
        if keys[pygame.K_DOWN]:
            if bin.rect.y<630:
                bin.rect.y+=5
        if keys[pygame.K_LEFT]:
            if bin.rect.x>0:
                bin.rect.x-=5
        if keys[pygame.K_RIGHT]:
            if bin.rect.x<850:
                bin.rect.x+=5
        
        item_hit_list= pygame.sprite.spritecollide(bin,item_list,True)
        plastic_hit_list=pygame.sprite.spritecollide(bin,plastic_list,True)

        for item in item_hit_list:
            score+=1
            text=myFont.render("Score=",str(score),True,WHITE)
        for plastic in plastic_hit_list:
            score-=5
            text=myFont.render("Score=",str(score),True,WHITE)
        screen.blit(text,(20,50))

        allsprites.draw(screen)

    pygame.display.update()
pygame.quit()
