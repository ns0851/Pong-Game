from turtle import Turtle
angle = 0
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.setheading(45)
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.05
        
    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x,new_y)

    def bounce(self):
        self.move_y *= -1

    def x_bounce(self):
        self.move_x *= -1
        self.move_speed *= 0.9
        self.speed()

    def reset(self):
        self.goto(0,0)
        self.x_bounce()
        self.move_speed = 0.05

