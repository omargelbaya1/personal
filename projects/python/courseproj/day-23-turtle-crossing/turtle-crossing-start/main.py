import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard(-270,270,"red","Level")
player = Player()

screen.listen()
screen.onkey(key="Up",fun=player.move)

game_is_on = True



cars_list = []

def create_cars():
    for __ in range(0,7):
        new_car_test= CarManager()
        cars_list.append(new_car_test)

create_cars()

while game_is_on:
    time.sleep(0.1)
    screen.update()

    speed_increase=40

    if player.ycor() > 280:
        player.goto(0,-200)
        scoreboard.increase_score()
        create_cars()
        speed_increase+=10

    random_dist= random.randint(0,speed_increase)
    car= random.choice(cars_list)
    car.forward(random_dist)


    if player.distance(car) < 20:
        game_over = Scoreboard(-50,0,"black","GAME OVER")
        game_is_on=False


screen.exitonclick()