# I am a bit dizzy. I will look to this later.


from turtle import Turtle, Screen

def move_upwards (turtles):
    while True:
        turtles[-1].setheading(90)
        turtles[-1].fd(20)

        for i in range(len(turtles)-1):
            turtles[i].goto(turtles[i+1])


if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    
    snake = []
    for i in range(3):
        turtle_to_add = Turtle()
        turtle_to_add.color("white")
        turtle_to_add.shape("square")
        turtle_to_add.pu()
        turtle_to_add.pensize(20)
        turtle_to_add.goto(x=-20+20*i,y=0)
        snake.append(turtle_to_add) 
    is_game_on = True
    while is_game_on:
        screen.listen()
        for segments in snake:
            segments.pu()
            segments.fd(20)
            segments.pd()
            #screen.onkey(key="w", fun=lambda:move_upwards(snake))
        
    screen.exitonclick()
