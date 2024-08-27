# this file has the initial code before i extracted code from it to form the snake class
from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

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
    screen.update()
    time.sleep(0.1)
    x1 = snake_body[0].xcor()
    y1 = snake_body[0].ycor()
    snake_body[0].forward(20)

    for i in range(1, len(snake_body)):
        x2 = snake_body[i].xcor()
        y2 = snake_body[i].ycor()
        snake_body[i].goto(x1, y1)
        x1 = x2
        y1 = y2

    snake_body[0].right(90)
screen.exitonclick()
