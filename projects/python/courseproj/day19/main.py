import random
from turtle import Turtle , Screen
is_race_on=False
screen=Screen()

screen.setup(width=500,height=400)
bet=screen.textinput(prompt="Which turtle do u fancy winning mate??",title="most winningest turtle bruh")
colors=["red","blue","green","yellow","pink","purple"]
if bet:
    is_race_on=True
y=-100
all_turtles=[]
for i in colors:
    new_turtle=Turtle(shape="turtle")
    all_turtles.append(new_turtle)
    new_turtle.color(i)
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y)
    y+=40


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>=230:
            if bet==turtle.pencolor():
                print(f"youve won mate, the best turtle was {turtle.pencolor()}")
                is_race_on=False
            else:
                print(f"ur dumb bro, winning turtle was {turtle.pencolor()}")
                is_race_on=False
        rand_dist=random.randint(0,10)
        turtle.forward(rand_dist)

screen.exitonclick()