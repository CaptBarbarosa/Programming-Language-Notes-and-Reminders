from turtle import Turtle, Screen

tim = Turtle()
tim.color("red")
my_screen = Screen()

def move_forwards():
    tim.fd(10)

my_screen.listen()
#It is continuously listens and when we press the "d" key, it execute move_forwards function.
my_screen.onkey(key="d", fun=move_forwards)


my_screen.exitonclick()