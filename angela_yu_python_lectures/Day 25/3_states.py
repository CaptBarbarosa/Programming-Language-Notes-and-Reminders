import pandas as pd
import turtle
# Turtle works with .gif file

screen = turtle.Screen()
screen.title("U.S.A. states Exercise")

screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

"""
def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
"""


answer = True
correct_guesses = 0
while answer!= "Exit" and correct_guesses != 50:

    answer = screen.textinput(title="Enter a state", prompt="What's another state ")
    data = pd.read_csv("50_states.csv")
    states = data.state.to_list()

    if answer in states:
        correct_guesses += 1
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.pu()
        coordinate_x = data[data.state == answer].x.values[0]
        coordinate_y = data[data.state == answer].y.values[0]
        tim.goto(coordinate_x, coordinate_y)
        tim.write(answer)
    
screen.bye()










turtle.mainloop()