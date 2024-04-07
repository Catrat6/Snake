import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food, SuperFood
from scoreboard import ScoreKeeper, HighScore
from testing_grounds import BombDrop

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

snake = Snake()
food = Food()
food2 = Food()
s_food = SuperFood()
score_board = ScoreKeeper()
high_board = HighScore()
bomb = BombDrop()
bomb_two = BombDrop()
bomb_three = BombDrop()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_is_on = True
game_start = True
chew_count = 0

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if score_board.score < 0:
        game_is_on = False
        score_board.game_over()

    if chew_count > 2:
        bomb.refresh()
        bomb_two.refresh()
        bomb_three.refresh()
        snake.clear_screen_of_snake_parts()
        snake.no_bloody_mouth()
        chew_count = 0

    if snake.head.distance(bomb) < 35 or snake.head.distance(bomb_two) < 35 or snake.head.distance(bomb_three) < 35:
        bomb.refresh()
        bomb_two.refresh()
        bomb_three.refresh()
        snake.remove_segment()
        score_board.bomb_score_down()

    # eat food and update score

    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.update_score()
        snake.extend()
        snake.bloody_mouth()
        chew_count += 1

    if snake.head.distance(food2) < 15:
        food2.refresh()
        score_board.update_score()
        snake.extend()
        snake.bloody_mouth()
        chew_count += 1

    if snake.head.distance(s_food) < 15:
        s_food.refresh()
        score_board.super_food_score_update()
        snake.extend()
        snake.extend()
        snake.extend()
        snake.bloody_mouth()
        chew_count += 1

    # collision detection

    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_on = False
        score_board.game_over()
        x = score_board.read_score()
        high_board.update_high_score(x)

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 6:
            game_is_on = False
            score_board.game_over()
            x = score_board.read_score()
            high_board.update_high_score(x)



screen.exitonclick()
