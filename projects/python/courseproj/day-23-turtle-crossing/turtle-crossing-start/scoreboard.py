from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT= "left"

class Scoreboard(Turtle):
    def __init__(self,xx,yy,color,text):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color(color)
        self.xx=xx
        self.yy=yy
        self.text = text
        self.goto(self.xx, self.yy)
        self.score = 0
        self.update_score()


    def update_score(self):
        self.write(f"{self.text} {self.score}", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()




