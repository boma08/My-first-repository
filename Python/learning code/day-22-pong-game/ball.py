from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        #self.shapesize(20, 20)
        self.color("white")
        self.setx(0)
        self.sety(0)
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.sleep = 0.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.sleep *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.sleep *= 0.9
