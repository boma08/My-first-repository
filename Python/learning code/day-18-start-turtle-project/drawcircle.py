import turtle as t
import random

t.colormode(255)
screen = t.Screen()
turtle = t.Turtle()
turtle.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


heading = 0
for circles in range(73):
    turtle.setheading(heading)
    turtle.color(random_color())
    turtle.circle(radius=100)
    heading += 5



screen.exitonclick()
