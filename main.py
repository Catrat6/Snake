import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreKeeper

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreKeeper()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.generate_snake()
        snake.bloody_mouth()
        score_board.update_score()



screen.exitonclick()
