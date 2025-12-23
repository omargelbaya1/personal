import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1,2)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.penup()
        self.random_value_y=random.randint(-250,250)
        self.value_x=280
        self.goto(self.value_x,self.random_value_y)
        self.speed(400)

    # def moving_car(self):
    #     self.value_x-= MOVE_INCREMENT
    #     self.goto(self.value_x, self.random_value_y)


