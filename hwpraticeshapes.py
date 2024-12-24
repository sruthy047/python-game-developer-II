import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Polygon")
screen.fill((255,255,255))
pygame.display.update()
subway_surfer=pygame.image.load(r"E:\Sruthi\Python Game Developer II\Lesson7\subwaysurfer.png")
screen.blit(subway_surfer,(50,50))
font=pygame.font.SysFont("Times New Roman",34)
text=font.render("Polygon Examples",True,(0,0,0))
screen.blit(text,(150,50))

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

pygame.display.update()
class Polygon():
    def __init__(self, color, points):
        self.color = color  # Color of the polygon
        self.points = points  # List of points defining the polygon

    def draw(self):
        pygame.draw.polygon(screen, self.color, self.points, 0)  # 0 for a filled polygon

# Create polygon objects
triangle = Polygon(blue, [(150, 100), (100, 300), (200, 300)])  # A triangle
pentagon = Polygon(red, [(300, 200), (350, 100), (400, 200), (375, 300), (325, 300)])  # A pentagon

# Draw the polygons
triangle.draw()
pentagon.draw()
pygame.display.update()



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check if the user wants to quit
            running = False

# Quit pygame
pygame.quit()
