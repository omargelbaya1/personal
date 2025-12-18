from turtle import Turtle



class Paddle(Turtle):
    def __init__(self,xcor):
        super().__init__()
        self.shape("square")
        self.color('white')
        self.penup()
        self.shapesize(5, 1)
        self.xcor=xcor
        self.current_y = 0
        self.goto(xcor, self.current_y)

    def up(self):
        if self.current_y < 230:
            self.current_y+=20
            self.goto(self.xcor,self.current_y)

    def down(self):
        if self.current_y > -230:
            self.current_y-=20
            self.goto(self.xcor,self.current_y)

