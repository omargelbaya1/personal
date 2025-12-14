
import colorgram
import random
from turtle import Turtle , Screen
import turtle

turtle.colormode(255)
# colors =colorgram.extract("image.jpg",15)
#
#
# empty_list=[]
# for i  in range(0,15):
#     nice_colour=colors[i]
#     rgb=nice_colour.rgb
#     colour_tuple = (rgb.r,rgb.g,rgb.b)
#     empty_list.append(colour_tuple)
# print(empty_list)

tim=Turtle()
colour_list=[(192, 171, 125), (156, 177, 193), (193, 162, 176), (215, 203, 127), (154, 185, 174), (165, 207, 187), (208, 180, 194), (179, 189, 209), (193, 158, 50), (161, 204, 214), (109, 119, 174)]


tim.width(25)
y=0
tim.penup()

for _ in range(10):
    tim.setpos(-300,y)
    y+=50
    t=turtle.pos()
    print(t)
    for _ in range(10):
        tim.dot(20,random.choice(colour_list))
        tim.forward(50)




screen=Screen()
screen.exitonclick()



