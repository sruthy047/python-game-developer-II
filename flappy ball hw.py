import pgzrun
from random import randint

TITLE="Flappy Ball"
WIDTH=800
HEIGHT=600

R=randint(0,255)
G=randint(0,255)
B=randint(0,255)
CLR=R,G,B

GRAVITY=2000.0

class Ball():
    def __init__(self,initial_x,initial_y,rad,color):
        self.x=initial_x
        self.y=initial_y
        self.vx=200
        self.vy=0
        self.radius=rad
        self.clr=color

    def draw(self):
        pos=(self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,self.clr)

ball=Ball(50,100,40,"red")
ball2=Ball(100,100,20,"blue")
def draw():
    screen.clear()
    ball.draw()
    ball2.draw()
def update(dt):
    uy=ball.vy
    ball.vy=ball.vy+GRAVITY*dt
    ball.y=ball.y+(uy + ball.vy) * 0.5 * dt

    if ball.y > HEIGHT - ball.radius:  
        ball.y = HEIGHT - ball.radius  
        ball.vy = -ball.vy * 0.9 

    
    ball.x += ball.vx * dt
    if ball.x > WIDTH - ball.radius or ball.x < ball.radius:
        ball.vx = -ball.vx

    uy=ball2.vy
    ball2.vy=ball2.vy+GRAVITY*dt
    ball2.y=ball2.y+(uy + ball2.vy) * 0.5 * dt

    if ball2.y > HEIGHT - ball2.radius:  
        ball2.y = HEIGHT - ball2.radius  
        ball2.vy = -ball2.vy * 0.9 

    
    ball2.x += ball2.vx * dt
    if ball2.x > WIDTH - ball2.radius or ball2.x < ball2.radius:
        ball2.vx = -ball2.vx



def on_key_down(key):
    
    if key == keys.SPACE:
        ball.vy = -500
    if key == keys.SPACE:
        ball2.vy = -200

pgzrun.go()