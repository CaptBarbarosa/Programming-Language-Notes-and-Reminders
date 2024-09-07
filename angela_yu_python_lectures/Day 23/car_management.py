from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):
        if random.randint(0,3) == 1:
            car_to_add = Turtle("square")
            car_to_add.shapesize(stretch_wid=1, stretch_len=2)
            car_to_add.pu()
            car_to_add.color(random.choice(COLORS))
            y_pos = random.randint(-250,250)
            car_to_add.goto(300, y_pos)
            self.cars.append(car_to_add)
        
    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)
            
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
            

        
