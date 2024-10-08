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
guessed_states = []

while answer!= "Exit" and len(guessed_states) < 50:

    answer = screen.textinput(title="Enter a state", prompt="What's another state ")
    data = pd.read_csv("50_states.csv")
    states = data.state.to_list()

    if answer in states and answer not in guessed_states:
        guessed_states.append(answer)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.pu()
        coordinate_x = data[data.state == answer].x.values[0]
        coordinate_y = data[data.state == answer].y.values[0]
        tim.goto(coordinate_x, coordinate_y)
        tim.write(answer)
    
screen.bye()










turtle.mainloop()