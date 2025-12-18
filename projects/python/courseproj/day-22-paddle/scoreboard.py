from turtle import Turtle

ALIGNMENT="center"
FONT=("Arial",24,"normal")

class ScoreBoard(Turtle):
    def __init__(self,xcor):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(xcor, 270)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

