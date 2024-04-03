from turtle import Turtle

class ScoreKeeper(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color('#06FA45')
        self.score = 0
        self.write(f"Score: {self.score}", False, "center", ("Arial", 20, "normal"))
    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, "center", ("Arial", 20, "normal"))







