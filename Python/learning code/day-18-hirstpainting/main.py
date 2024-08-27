import turtle as t
import random

t.colormode(255)
turtle = t.Turtle()
screen = t.Screen()

rgb_color_list = [(88, 253, 166), (42, 18, 177), (213, 237, 90), (250, 139, 85),
                  (108, 148, 250), (244, 110, 206), (236, 245, 254), (167, 1, 143), (160, 14, 1), (117, 82, 248),
                  (4, 212, 97), (3, 139, 62), (251, 67, 36), (235, 38, 138), (9, 107, 195), (183, 182, 252),
                  (208, 104, 6),
                  (35, 34, 252), (45, 242, 51), (191, 31, 151), (96, 248, 252), (6, 209, 215), (237, 157, 215),
                  (30, 28, 108), (107, 6, 65), (109, 18, 5), (243, 168, 155), (212, 118, 22), (5, 115, 34),
                  (0, 119, 121),
                  (138, 23, 240)]
turtle.penup()
turtle.hideturtle()
turtle.backward(250)
turtle.right(90)
turtle.forward(250)
turtle.left(90)
print(turtle.position())

x = -250
y = -250
for steps in range(10):
    for _ in range(10):
        turtle.dot(20, random.choice(rgb_color_list))
        turtle.forward(50)
    y += 50
    turtle.goto(x, y)

screen.exitonclick()
