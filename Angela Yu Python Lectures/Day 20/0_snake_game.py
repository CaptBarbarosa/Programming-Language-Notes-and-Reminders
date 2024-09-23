from turtle import Turtle, Screen
import time

current_direction = None

def move_upwards(turtles, screen):
    global current_direction
    if current_direction == 'up':
        turtles[0].setheading(90)  
        screen.tracer(0)
        for i in range(len(turtles) - 1, 0, -1):
            current_pos = turtles[i - 1].pos()
            turtles[i].pu()
            turtles[i].goto(current_pos)
            turtles[i].pd()
        turtles[0].fd(20)
        screen.update()
        screen.ontimer(lambda: move_upwards(turtles, screen), 100)

def move_downwards(turtles, screen):
    global current_direction
    if current_direction == 'down':
        turtles[0].setheading(270)
        screen.tracer(0)
        for i in range(len(turtles) - 1, 0, -1):
            current_pos = turtles[i - 1].pos()
            turtles[i].pu()
            turtles[i].goto(current_pos)
            turtles[i].pd()
        turtles[0].fd(20)
        screen.update()
        screen.ontimer(lambda: move_downwards(turtles, screen), 100)

def move_leftwards(turtles, screen):
    global current_direction
    if current_direction == 'left':
        turtles[0].setheading(180)
        screen.tracer(0)
        for i in range(len(turtles) - 1, 0, -1):
            current_pos = turtles[i - 1].pos()
            turtles[i].pu()
            turtles[i].goto(current_pos)
            turtles[i].pd()
        turtles[0].fd(20)
        screen.update()
        screen.ontimer(lambda: move_leftwards(turtles, screen), 100)

def move_rightwards(turtles, screen):
    global current_direction
    if current_direction == 'right':
        turtles[0].setheading(0)
        screen.tracer(0)
        for i in range(len(turtles) - 1, 0, -1):
            current_pos = turtles[i - 1].pos()
            turtles[i].pu()
            turtles[i].goto(current_pos)
            turtles[i].pd()
        turtles[0].fd(20)
        screen.update()
        screen.ontimer(lambda: move_rightwards(turtles, screen), 100)

def start_moving_up(turtles, screen):
    global current_direction
    current_direction = 'up'
    move_upwards(turtles, screen)

def start_moving_down(turtles, screen):
    global current_direction
    current_direction = 'down'
    move_downwards(turtles, screen)

def start_moving_left(turtles, screen):
    global current_direction
    current_direction = 'left'
    move_leftwards(turtles, screen)

def start_moving_right(turtles, screen):
    global current_direction
    current_direction = 'right'
    move_rightwards(turtles, screen)

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.tracer(0)

    segments = []
    for i in range(3):
        turtle_to_add = Turtle()
        turtle_to_add.color("white")
        turtle_to_add.shape("square")
        turtle_to_add.pu()
        turtle_to_add.goto(x=20 - 20 * i, y=0)
        segments.append(turtle_to_add)

    screen.update()

    screen.listen()
    screen.onkey(lambda: start_moving_up(segments, screen), "w")
    screen.onkey(lambda: start_moving_down(segments, screen), "s")
    screen.onkey(lambda: start_moving_left(segments, screen), "a")
    screen.onkey(lambda: start_moving_right(segments, screen), "d")

    is_game_on = True
    while is_game_on:
        time.sleep(0.1)
        screen.update()

    screen.exitonclick()
