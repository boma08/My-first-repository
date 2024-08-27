from turtle import Turtle

MOVE_DISTANCE = 10
STARTING_POSITION = (0, -280)
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.reset_position()

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def step_back(self):
        self.backward(MOVE_DISTANCE)

    def move_right(self):
        x = self.xcor() + MOVE_DISTANCE
        y = self.ycor()
        self.goto((x, y))

    def move_left(self):
        x = self.xcor() - MOVE_DISTANCE
        y = self.ycor()
        self.goto((x, y))

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def cross_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
