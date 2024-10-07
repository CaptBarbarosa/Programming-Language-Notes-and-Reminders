from turtle import Turtle, Screen
import random

def move(turtle_given):
    distance = random.randint(0, 50)
    turtle_given.fd(distance)
    return distance


if __name__ == "__main__":
    my_screen = Screen()
    my_screen.setup(width=500, height=400)
    user_input = my_screen.textinput(title="Make your bet", prompt="Which turtle will win: Enter the color (Blue, Green, Red, Yellow)")
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    turtles=[]
    i=0
    for color_to_set in colors:
        turtle_to_add = Turtle()
        turtle_to_add.pu()
        turtle_to_add.color(color_to_set)
        turtle_to_add.shape("turtle")
        turtle_to_add.goto(x= -230, y = -160 + 60*i)
        turtle_to_add.pd()
        i+=1
        turtles.append(turtle_to_add)
    
    if user_input:
        is_race_on = True
    while is_race_on:
        for turtle in turtles:
            if turtle.xcor() > 230:
                print("Turtle ",turtle.pencolor()," has won")
                is_race_on=False
                if turtle.pencolor() == user_input:
                    my_screen.title("You have WON !!!")
                else:
                    my_screen.title("You have LOST !!!")
                break
            rand_distance = random.randint(0,20)
            turtle.fd(rand_distance)
    
    
    my_screen.exitonclick()
    

