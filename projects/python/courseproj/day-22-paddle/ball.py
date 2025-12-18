from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.yvalue=10
        self.xvalue=10


    def moving_ball(self):
        new_x = self.xcor() + self.xvalue
        new_y = self.ycor() + self.yvalue
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.yvalue  *= -1

    def bounce_x(self):
        self.xvalue  *= -1

    def reset_position(self):
        self.bounce_x()
        self.goto(0,0)






