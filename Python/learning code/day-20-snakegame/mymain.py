from turtle import Screen, Turtle
import time
from mysnake import Mysnake
from my_food import Food
from my_score_board import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Mysnake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True


while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # Detect collision with food
    if snake.snake_body[0].distance(food) < 15:
        snake.extend_snake()
        food.refresh_food()
        scoreboard.increase_score()

    if (snake.snake_body[0].xcor() > 280 or snake.snake_body[0].xcor() < -280 or snake.snake_body[0].ycor() > 280 or
            snake.snake_body[0].ycor() < -280):
        game_on = False
        scoreboard.end_game()

    for seg in snake.snake_body[1:]:  # slicing the list
        if snake.snake_body[0].distance(seg) < 10:
            game_on = False
            scoreboard.end_game()


screen.exitonclick()
