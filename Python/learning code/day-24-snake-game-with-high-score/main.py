from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # turn off tracer display on screen

snake_body = []
x_coordinate = 0
y_coordinate = 0
game_on = True

for _ in range(3):
    turtle = Turtle()
    turtle.penup()
    turtle.shape("square")
    turtle.color("white")
    turtle.setx(x_coordinate)
    turtle.sety(y_coordinate)
    x_coordinate -= 20
    snake_body.append(turtle)


while game_on:
    screen.update()  # updates the screen to visualise the snake otherwise snake wont be seen due to line 8
    time.sleep(0.1)
    for snake_num in range(len(snake_body) - 1, 0, -1):
        new_x = snake_body[snake_num - 1].xcor()
        new_y = snake_body[snake_num - 1].ycor()
        snake_body[snake_num].goto(new_x, new_y)
    snake_body[0].forward(20)

screen.exitonclick()
