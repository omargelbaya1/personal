import random
import turtle
from turtle import Turtle , Screen

turtle.colormode(255)
tim= Turtle()
tim.shape("turtle")
tim.color("red")
tim.speed(400)
tim.pensize(1)

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0,255)
    t = (r, g, b)
    return t

for _ in range(361):
    tim.color(random_colour())
    tim.circle(100)
    tim.right(5)

screen=Screen()
screen.exitonclick()




def turtle_shape(side_length,angle_of_side):
    rand_colour = random.choice(colors)
    tim.color(rand_colour)
    for _ in range(side_length):
        tim.forward(100)
        tim.right(angle_of_side)
        tim.forward(100)
def increasing_sides():
    for i in range(4,20):
        turtle_shape(i,(360/i))