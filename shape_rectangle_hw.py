import pygame
pygame.init()

screen=pygame.display.set_mode((600,600))
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
screen.fill(white)
w=2
pygame.display.update()
class Rect():
    w=2
    def __init__(self,color,dimensions):
        self.rect_surf = screen
        self.rect_color = color
        self.rect_dimensions=dimensions

    def draw(self):
        self.Draw_Rect = pygame.draw.rect(self.rect_surf, self.rect_color, self.rect_dimensions,self.w)
    def grow(self,wc):
        self.w=self.w+wc
        self.Draw_Rect = pygame.draw.rect(self.rect_surf, self.rect_color, self.rect_dimensions,self.w)

greenRect=Rect(green,(50,20,100,100))
greenRect.draw()


while(1):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((255,255,255))
            greenRect.draw()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill((255,255,255))
            greenRect.grow(2)
            pygame.display.update()


