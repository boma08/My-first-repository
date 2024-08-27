from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.clear()

    def update_score(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)


