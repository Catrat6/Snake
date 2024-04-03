import random
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.generate_snake()
        self.head = self.segments[0]

    def generate_snake(self):
        for each in STARTING_POSITIONS:
            new_segment = Turtle('square')
            new_segment.penup()
            new_segment.color('white')
            new_segment.goto(each)
            self.segments.append(new_segment)

    def show_segments(self):
        self.head.color('yellow')
        self.segments[1].color('green')

    def clean_movement(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # grab next segments cords
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()

            self.segments[seg_num].goto(new_x, new_y)

    def move(self):
        self.clean_movement()
        self.head.forward(MOVE_DISTANCE)

    def turn(self, direction, degree_of_turn):
        self.clean_movement()
        if direction == 'left':
            self.head.left(degree_of_turn)
        elif direction == 'right':
            self.head.right(degree_of_turn)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)







