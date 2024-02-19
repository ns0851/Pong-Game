from turtle import Turtle

class Dotted(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        for _ in range(45):
            if _ >= 15:
                self.setheading(270)
            else:
                self.setheading(90)
            self.forward(10)
            self.color("white")
            self.forward(10)
            self.color("black")

