from turtle import Turtle, Screen
import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color
    
tom_the_turtle = Turtle()
tom_the_turtle.shape("turtle")
tom_the_turtle.speed("fastest")
my_screen = Screen()
my_screen.colormode(255)

directions= [0, 90, 180, 270]
tom_the_turtle.pensize(15)
while True:
    tom_the_turtle.color(random_color())
    tom_the_turtle.fd(50)
    tom_the_turtle.setheading(random.choice(directions))
    

my_screen.exitonclick()
