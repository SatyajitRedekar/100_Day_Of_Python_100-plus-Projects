import turtle
from turtle import Turtle

import pandas as pd

IMAGE = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S. States Game")

screen.addshape(IMAGE) # this will add to the resources
turtle.shape(IMAGE) # this uses the image to the project

score = 0
data = pd.read_csv("50_states.csv")
states = data["state"].to_list()


# todo 1: input box update
# show score on the title
# repeat the input box
def input_score_board() :
    ans_states = screen.textinput(title=f"{score}/50 Guess the State", prompt="What's another state name you know")
    return ans_states.lower()

guessed_states = []

while len(guessed_states) < 50:
    ans = input_score_board()
    if ans is None:
        break

    for state in states:
        if state.lower() == ans and ans.title() not in guessed_states:
            guessed_states.append(ans.title())
            score += 1

            writer_turtle = Turtle()
            writer_turtle.hideturtle()
            writer_turtle.penup()

            state_data = data[data.state == ans.title()]
            x = int(state_data.x.iloc[0])
            y = int(state_data.y.iloc[0])

            writer_turtle.goto(x, y)
            writer_turtle.write(ans.title(), align="center", font=("Arial", 8, "normal"))
            break



screen.exitonclick()