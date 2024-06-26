import random
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 15
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

NEON_COLORS = [
    "#ff6eff", "#ff00ff", "#cc00ff", "#9900ff", "#6600ff",
    "#3300ff", "#0000ff", "#0033ff", "#0066ff", "#0099ff",
    "#00ccff", "#00ffff", "#00ffcc", "#00ff99", "#00ff66",
    "#00ff33", "#00ff00", "#33ff00", "#66ff00", "#99ff00"
]

class Snake:

    def __init__(self):
        self.segments = []
        self.broken_snake_bits = []
        self.generate_snake()
        self.head = self.segments[0]

    def generate_snake(self):
        for each in STARTING_POSITIONS:
            self.add_segment(each)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.penup()
        new_segment.color('#06FA45')
        new_segment.goto(position)
        self.segments.append(new_segment)

    def remove_segment(self):
        snake_bits = self.segments[2:]
        del self.segments[2:]
        for each in snake_bits:
            each.color('red')
        self.broken_snake_bits.extend(snake_bits)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def clear_screen_of_snake_parts(self):
        for each in self.broken_snake_bits:
            each.hideturtle()

    def rainbow_segments(self):
        for each in self.segments:
            each.color(random.choice(NEON_COLORS))

    def solid_color_change_segment(self):
        a = random.choice(NEON_COLORS)
        for each in self.segments:
            each.color(a)

    def bloody_mouth(self):
        self.head.color('red')

    def no_bloody_mouth(self):
        self.head.color("#06FA45")

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






