from turtle import Turtle, Screen

def move_forwards(tim):
    tim.forward(10)

def move_backwards(tim):
    tim.backward(10)

def turn_left(tim):
    new_heading = tim.heading()+10
    tim.setheading(new_heading)
    

def turn_right(tim):
    new_heading = tim.heading()-10
    tim.setheading(new_heading)
    
def clear(tim):
    tim.home()
    tim.clear()

if __name__ == "__main__":
    my_screen = Screen()
    tim = Turtle()
    
    my_screen.listen()
    # Use a lambda to pass the tim argument correctly
    my_screen.onkey(key="a", fun=lambda: move_backwards(tim))
    my_screen.onkey(key="d", fun=lambda: move_forwards(tim))
    my_screen.onkey(key="w", fun=lambda: turn_left(tim))
    my_screen.onkey(key="s", fun=lambda: turn_right(tim))
    my_screen.onkey(key="c", fun=lambda: clear(tim))

    my_screen.exitonclick()
