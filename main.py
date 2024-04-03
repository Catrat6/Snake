import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreKeeper, HighScore

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

snake = Snake()
food = Food()
food2 = Food()
score_board = ScoreKeeper()
high_board = HighScore()

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

    # eat food and update score

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.bloody_mouth()
        score_board.update_score()
        snake.extend()

    if snake.head.distance(food2) < 15:
        food2.refresh()
        snake.bloody_mouth()
        score_board.update_score()
        snake.extend()

    # collision detection

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score_board.game_over()
        x = score_board.read_score()
        high_board.update_high_score(x)


screen.exitonclick()
