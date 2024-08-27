from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Endgame(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 0)

    def end_of_game(self):
        self.write("Game Over!", align=ALIGNMENT, font=FONT)
