from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from dotted import Dotted
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Sliding Game Thing")
screen.tracer(0)

screen.listen()
ball = Ball()
paddle = Paddle(350,0)
paddle2 = Paddle(-350,0)
scoreboard = Scoreboard()
dotted = Dotted()

screen.onkey(paddle.go_up, "Up")
screen.onkey(paddle.go_down, "Down")

screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")


is_on = True
while is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(paddle) < 40 and ball.xcor() > 320 or ball.distance(paddle2) < 40 and ball.xcor() < -320:
        ball.x_bounce()

    if ball.xcor() > 380: #or ball.xcor() < -380:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()

    if scoreboard.l_score >= 5:
        scoreboard.goto(0,0)
        scoreboard.write("Left Player wins",align ="center", font=("Courier",30,"normal"))
        is_on = False
    elif scoreboard.r_score >= 5:
        scoreboard.goto(0, 0)
        scoreboard.write("Right Player wins", align="center", font=("Courier", 30, "normal"))
        is_on = False


screen.exitonclick()