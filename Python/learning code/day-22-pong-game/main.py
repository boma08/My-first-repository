from turtle import Screen

from paddle import Paddle
from ball import Ball
import time
from score import Score
from game_over import Endgame


screen = Screen()
screen.tracer(0)
screen.listen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
right_score = Score((80, 250))
left_score = Score((-80, 250))
end_game = Endgame()


screen.onkey(right_paddle.up, key="Up")
screen.onkey(right_paddle.down, key="Down")
screen.onkey(left_paddle.up, key="w")
screen.onkey(left_paddle.down, key="s")

game_on = True
while game_on:
    time.sleep(ball.sleep)
    screen.update()
    ball.move()

    # detecting collision with screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detecting collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_x()
        right_score.increase_score()
        right_score.update_score()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        left_score.increase_score()
        left_score.update_score()

    # detecting when paddle misses ball
    if ball.xcor() > right_paddle.xcor() + 2 or ball.xcor() < left_paddle.xcor() < + 2:
        end_game.end_of_game()
        game_on = False


screen.exitonclick()
