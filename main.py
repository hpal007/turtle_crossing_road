import os
import sys
import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

# Screen size setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title('Turtle Road Crossing Game')
screen.tracer(0)
game_is_on = True

# object
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


def restart_game():
    os.execv(sys.executable, ['python'] + sys.argv)

# keyboard action
screen.listen()
screen.onkey(player.move_forward, 'Up')
screen.onkey(player.move_backward, 'Down')
screen.onkey(restart_game, 'space')

while game_is_on:
    screen.update()
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move_car()

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_score()
        scoreboard.update_scoreboard()

screen.exitonclick()
