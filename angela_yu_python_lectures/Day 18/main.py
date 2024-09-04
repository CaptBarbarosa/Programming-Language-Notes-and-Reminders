from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

for i in range(10, 2, -1):#Up to decagon
    angle = 360/i
    for j in range(i):
        timmy_the_turtle.fd(100)
        timmy_the_turtle.right(angle)

my_screen = Screen()
my_screen.exitonclick()