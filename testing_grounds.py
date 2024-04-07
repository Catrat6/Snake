from turtle import Turtle
import random

class BombDrop(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('red')
        self.shapesize(3, 3)
        self.penup()
        self.random_y = random.randint(-300, 300)
        self.random_x = random.randint(-300, 300)
        self.goto(self.random_y, self.random_x)

    def refresh(self):
        self.random_y = random.randint(-300, 300)
        self.random_x = random.randint(-300, 300)
        self.goto(self.random_y, self.random_x)







