from turtle import Turtle

ALIGNMENT="center"
FONT=("Arial",24,"normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,270)
        self.score = 0
        self.high_score = self.current_score_from_file()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",False,ALIGNMENT,FONT)

    def increase_score(self):
        self.score +=1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
            self.write_to_file()
        self.score=0
        self.update_score()

    def write_to_file(self):
        with open("data.txt", mode='a') as file:
                file.write(f"\nHighest score is {self.high_score}")

    def current_score_from_file(self):
        with open("data.txt") as file:
            contents=file.read()
            return int(contents[0])

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",False,ALIGNMENT,FONT)


