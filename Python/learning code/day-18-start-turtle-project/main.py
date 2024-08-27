import turtle
import heroes

turtle.colormode(255)
turtle = turtle.Turtle()
turtle.shape("turtle")


# Draw a square


# def draw_a_square():
#     turtle.forward(200)
#     turtle.right(90)
#     turtle.forward(200)
#     turtle.right(90)
#     turtle.forward(200)
#     turtle.right(90)
#     turtle.forward(200)
#     turtle.right(90)
#
#
# draw_a_square()
# print(heroes.gen())
#
#
# for i in range(4):
#     turtle.pen(pencolor="red")
#     turtle.forward(50)
#     turtle.right(90)
#
# for i in range(5):
#     turtle.pen(pencolor="orange")
#     turtle.forward(50)
#     turtle.right(72)
#
# for i in range(6):
#     turtle.pen(pencolor="yellow")
#     turtle.forward(50)
#     turtle.right(60)
#
# for i in range(7):
#     turtle.pen(pencolor="blue")
#     turtle.forward(50)
#     turtle.right(51.429)
#
# for i in range(8):
#     turtle.pen(pencolor="green")
#     turtle.forward(50)
#     turtle.right(45)
#
# for i in range(9):
#     turtle.pen(pencolor="indigo")
#     turtle.forward(50)
#     turtle.right(40)
#
# for i in range(10):
#     turtle.pen(pencolor="violet")
#     turtle.forward(50)
#     turtle.right(36)

# turtle.penup()
# turtle.right(90)
# turtle.forward(300)
# turtle.right(90)
# turtle.forward(350)
# turtle.right(90)
# turtle.forward(50)
# turtle.right(90)

# for i in range(50):
#     turtle.pendown()
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)

import random
# colours = ["DodgerBlue", "ForestGreen", "Red", "SlateBlue", "Navy", "MediumVioletRed", "BlueViolet", "OrangeRed",
#             "Pink", "Yellow", "DarkCyan", "SlateGray", "Burlywood"]
#
#
# def draw_shape(num_of_sides):
#     angle = 360 / num_of_sides
#     for no_side in range(num_of_sides):
#         turtle.forward(100)
#         turtle.right(angle)
#
#
# for shape in range(3, 11):
#     turtle.color(random.choice(colours))
#     turtle.pensize(5)
#     draw_shape(shape)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

angles = [0, 90, 180, 270]
for moves in range(200):
    turtle.pensize(10)
    turtle.color(random_color())
    turtle.speed(0)
    turtle.forward(50)
    turtle.right(random.choice(angles))


screen = Screen()
screen.exitonclick()
