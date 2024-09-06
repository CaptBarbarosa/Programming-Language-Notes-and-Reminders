from turtle import Turtle, Screen
import time

def move_upwards (turtles, screen):
    turtles[0].setheading(90)
    screen.tracer(0)
    for i in range(len(turtles) - 1, 0, -1):
        current_pos = turtles[i - 1].pos()
        turtles[i].pu()
        turtles[i].goto(current_pos)
        turtles[i].pd()
    turtles[0].fd(20)
    screen.update()
    


if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    
    segments = []
    for i in range(3):
        turtle_to_add = Turtle()
        turtle_to_add.color("white")
        turtle_to_add.shape("square")
        turtle_to_add.pu()
        turtle_to_add.pensize(20)
        turtle_to_add.goto(x=20-20*i,y=0)
        segments.append(turtle_to_add) 
    is_game_on = True
    while is_game_on:
        screen.update()
        time.sleep(0.1)
        for seg_num in range(len(segments) -1 , 1, -1):
            new_x = segments[seg_num -1].xcor()
            new_y = segments[seg_num -1].ycor()
            segments[seg_num].goto(new_x, new_y)
        
    screen.exitonclick()
