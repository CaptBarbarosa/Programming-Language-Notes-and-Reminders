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

cars = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()
    for car in cars.cars:
        if car.distance(player)<20:
            game_is_on = False
    if player.ycor()>=FINISH_LINE_Y:
        player.go_to_start()
        cars.level_up()
        
        

