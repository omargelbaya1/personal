from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen  = Screen()
screen.tracer(0)

rscore=ScoreBoard(270)
lscore=ScoreBoard(-270)

rpaddle =  Paddle(350)
lpaddle =  Paddle(-350)
ball = Ball()

screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")

screen.listen()
screen.onkey(key="Up",fun=rpaddle.up)
screen.onkey(key="Down",fun=rpaddle.down)
screen.onkey(key="w",fun=lpaddle.up)
screen.onkey(key="s",fun=lpaddle.down)

game_is_on=True

speed_of_ball=0.2

while game_is_on:
    screen.update()
    ball.moving_ball()
    time.sleep(speed_of_ball)

    if ball.ycor() > 280 or ball.ycor()<-280:
        ball.bounce_y()
        speed_of_ball *= 0.9

    if ball.distance(rpaddle) < 50 and ball.xcor() > 320 or  ball.distance(lpaddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        speed_of_ball *= 0.9

    if ball.xcor() > 380:
        ball.reset_position()
        lscore.increase_score()
        speed_of_ball = 0.2

    if ball.xcor()<-340:
        ball.reset_position()
        rscore.increase_score()
        speed_of_ball = 0.2



screen.exitonclick()