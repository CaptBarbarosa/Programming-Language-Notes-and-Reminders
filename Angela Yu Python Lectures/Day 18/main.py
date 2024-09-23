from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")

for i in range(10, 2, -1):#Up to decagon
    angle = 360/i
    for j in range(i):
        for k in range(12):
            timmy_the_turtle.penup()
            timmy_the_turtle.fd(4)
            timmy_the_turtle.pendown()
            timmy_the_turtle.fd(4)
        #timmy_the_turtle.fd(100)
        timmy_the_turtle.right(angle)
timmy_the_turtle.clear()


    

my_screen = Screen()
my_screen.exitonclick()