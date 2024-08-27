from turtle import Turtle


class Mysnake():

    def __init__(self):
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        x_coordinate = 0
        y_coordinate = 0
        for _ in range(3):
            snake = Turtle()
            snake.penup()
            snake.shape("square")
            snake.color("white")
            snake.setx(x_coordinate)
            snake.sety(y_coordinate)
            x_coordinate -= 20
            self.snake_body.append(snake)

    def reset_snake(self):
        for snake in self.snake_body:
            snake.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()

    def extend_snake(self):
        snake = Turtle()
        snake.penup()
        snake.shape("square")
        snake.color("white")
        snake_heading = self.snake_body[len(self.snake_body) - 1].heading()
        if snake_heading == 0:
            snake.setx(self.snake_body[len(self.snake_body) - 1].xcor() + 20)
            snake.sety(self.snake_body[len(self.snake_body) - 1].ycor())
        elif snake_heading == 90:
            snake.sety(self.snake_body[len(self.snake_body) - 1].ycor() + 20)
            snake.setx(self.snake_body[len(self.snake_body) - 1].xcor())
        elif snake_heading == 180:
            snake.setx(self.snake_body[len(self.snake_body) - 1].xcor() - 20)
            snake.sety(self.snake_body[len(self.snake_body) - 1].ycor())
        elif snake_heading == 270:
            snake.sety(self.snake_body[len(self.snake_body) - 1].ycor() - 20)
            snake.setx(self.snake_body[len(self.snake_body) - 1].xcor())

        self.snake_body.append(snake)


    def move_snake(self):
        x1 = self.snake_body[0].xcor()
        y1 = self.snake_body[0].ycor()
        self.snake_body[0].forward(20)

        for i in range(1, len(self.snake_body)):
            x2 = self.snake_body[i].xcor()
            y2 = self.snake_body[i].ycor()
            self.snake_body[i].goto(x1, y1)
            x1 = x2
            y1 = y2

    def up(self):
        snake_heading = self.snake_body[0].heading()
        if snake_heading == 0:
            self.snake_body[0].left(90)
        elif snake_heading == 180:
            self.snake_body[0].right(90)

    def down(self):
        snake_heading = self.snake_body[0].heading()
        if snake_heading == 0:
            self.snake_body[0].right(90)
        elif snake_heading == 180:
            self.snake_body[0].left(90)

    def left(self):
        snake_heading = self.snake_body[0].heading()
        if snake_heading == 90:
            self.snake_body[0].left(90)
        elif snake_heading == 270:
            self.snake_body[0].right(90)

    def right(self):
        snake_heading = self.snake_body[0].heading()
        if snake_heading == 90:
            self.snake_body[0].right(90)
        elif snake_heading == 270:
            self.snake_body[0].left(90)

