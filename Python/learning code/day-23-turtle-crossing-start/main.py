import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from game_over import Endgame

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
player = Player()
car_manager = CarManager()
sleep = 0.1
scoreboard = Scoreboard()
endgame = Endgame()


screen.listen()
screen.onkey(player.move_forward, "Up")
screen.onkey(player.step_back, "Down")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(sleep)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            endgame.end_of_game()

    if player.cross_finish_line():
        player.reset_position()
        car_manager.level_up()
        scoreboard.increase_score()
        scoreboard.update_score()


screen.exitonclick()
