import turtle
import random

screen = turtle.Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will will? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
turtle_racers = []

y_axis = 150
color_index = 0
for turtle_obj in range(7):
    t = turtle.Turtle(shape="turtle")
    t.penup()
    t.color(colors[color_index])
    turtle_racers.append(t)
    t.goto(x=-240, y=y_axis)
    color_index += 1
    y_axis -= 50

ref_turtle = turtle.Turtle(shape="turtle")
ref_turtle.color("black")
ref_turtle.penup()
ref_turtle.goto(x=200, y=180)
ref_turtle.right(90)
ref_turtle.pendown()
ref_turtle.forward(360)
ref_turtle.right(180)

if user_bet:
    is_race_on = True

while is_race_on:
    for t in turtle_racers:
        if t.xcor() > 200:
            is_race_on = False
            winner = t.pencolor()
            if winner == user_bet:
                print(f"You have won. The {winner} color is the winner!")
            else:
                print(f"You have lost. The {winner} color is the winner!")
        rand_distance = random.randint(0, 13)
        t.forward(rand_distance)



#the for loop above does the same thing as the series of codes below
# t1 = turtle.Turtle(shape="turtle")
# t1.penup()
# t1.color(colors[0])
# t1.goto(x=-240, y=50)
#
# t2 = turtle.Turtle(shape="turtle")
# t2.penup()
# t2.color(colors[1])
# t2.goto(x=-240, y=100)
#
# t3 = turtle.Turtle(shape="turtle")
# t3.penup()
# t3.color(colors[2])
# t3.goto(x=-240, y=150)
#
# t4 = turtle.Turtle(shape="turtle")
# t4.penup()
# t4.color(colors[3])
# t4.goto(x=-240, y=-50)
#
# t5 = turtle.Turtle(shape="turtle")
# t5.penup()
# t5.color(colors[4])
# t5.goto(x=-240, y=-100)
#
# t6 = turtle.Turtle(shape="turtle")
# t6.penup()
# t6.color(colors[5])
# t6.goto(x=-240, y=-150)
#
# t7 = turtle.Turtle(shape="turtle")
# t7.penup()
# t7.color(colors[6])
# t7.goto(x=-240, y=0)

screen.exitonclick()
