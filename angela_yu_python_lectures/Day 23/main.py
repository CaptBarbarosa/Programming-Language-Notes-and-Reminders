import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_management import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()

screen.onkey(player.move_upwards, "Up")
screen.onkey(player.move_backwards, "Down")

game_is_on = True
while player.ycor()<FINISH_LINE_Y:
    time.sleep(0.1)
    screen.update()

