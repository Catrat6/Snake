from turtle import Turtle

def load_high_score():
    with open("high_score.txt", "r") as file:
        return int(file.read())

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
    def super_food_score_update(self):
        self.clear()
        self.score += 3
        self.write(f"Score: {self.score}", False, "center", ("Arial", 20, "normal"))

    def bomb_score_down(self):
        self.clear()
        self.score -= 3
        self.write(f"Score: {self.score}", False, "center", ("Arial", 20, "normal"))


    def read_score(self):
        return self.score
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", ("Arial", 20, "normal"))

class HighScore(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(220, -280)
        self.color('#06FA45')
        self.high_score = load_high_score()
        self.write(f"High Score: {self.high_score}", False, "center", ("Arial", 14, "normal"))

    def update_high_score(self, score):
        if score > self.high_score:
            self.high_score = score
            with open("high_score.txt", "w") as file:
                file.write(str(score))





