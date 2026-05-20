from turtle import *

class Sprite(Turtle):
    def __init__(self, x, y , step, shape, color):
        super().__init__()
        self.penup()
        self.goto(x, y)
        self.step=step
        self.color(color)
        self.shape(shape)
    def move_left(self):
        self.goto (self.xcor()- self.step, self.ycor())
    def move_right(self):
        self.goto (self.xcor()+ self.step, self.ycor())
    def move_up(self):
        self.goto (self.xcor(), self.ycor()+self.step)
    def move_down(self):
        self.goto(self.xcor(), self.ycor()-self.step)
    def is_collid(self, other):
        if self.xcor() - other.xcor() <10 and self.ycor() - other.ycor() <10:
            return True 
        else: False
    def enemy_move(self):
        if abs(self.xcor())> 300:
            self.step *= -1
        self.goto(self.xcor() + self.step, self.ycor())
    def is_colide(self, other):
        dist=self.distance(other.xcor(), other.ycor())
        if dist < 30:
            return  True
        else: return False

player = Sprite(0, -100, 10, 'circle', 'orange')
enemy1 = Sprite(7, 0, 5, 'square', 'red')
enemy2 = Sprite(4, 70, 15, 'square', 'red')
goal = Sprite(0, 120, 20, 'triangle', 'green')

ss=player.getscreen()
ss.listen()
ss.onkey(player.move_up, 'Up')
ss.onkey(player.move_down, 'Down')
ss.onkey(player.move_left, 'Left')
ss.onkey(player.move_right, 'Right')                    

while True:
    enemy1.enemy_move()
    enemy2.enemy_move()
    if player.is_colide(goal):
        player.goto(0,-100)
    if player.is_colide(enemy2) or player.is_colide(enemy1):
        break 

print('ОУ ТЫ ПРОИГРАЛ')