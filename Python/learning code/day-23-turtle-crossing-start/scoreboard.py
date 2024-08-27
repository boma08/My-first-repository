from turtle import Turtle

FONT = ("Courier", 12, "normal")
POSITION = (-280, 280)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        self.update_score()

    def increase_score(self):
        self.level += 1
        self.clear()

    def update_score(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.write("Game over!", align="center", font=FONT)
