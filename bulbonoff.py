import pygame
import time

pygame.init()
WIDTH=600
HEIGHT=600
display_surface=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Bulb ON and OFF")

img=pygame.image.load(r"E:\Sruthi\Python Game Developer II\Lesson 4\on.jpg")
image=pygame.transform.scale(img,(WIDTH,HEIGHT))

while(True):
    font=pygame.font.SysFont("Times New Roman",72)
    text=font.render("ON",True,(0,0,0))
   
    display_surface.fill((255,255,255))
    display_surface.blit(image,(0,0))
    display_surface.blit(text,(210,180))
    
    pygame.display.update()
    time.sleep(2)

    image2=pygame.image.load(r"E:\Sruthi\Python Game Developer II\Lesson 4\off.jpg")
    image2=pygame.transform.scale(image2,(WIDTH,HEIGHT))
    font2=pygame.font.SysFont("Arial",36)
    text3=font2.render("OFF",True,(0,0,0))
    display_surface.fill((255,255,255))
    display_surface.blit(image2,(0,0))
    display_surface.blit(text3,(30,30))
    pygame.display.update()
    time.sleep(2)


