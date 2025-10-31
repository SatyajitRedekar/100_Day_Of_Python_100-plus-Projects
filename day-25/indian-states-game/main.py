import turtle
from turtle import Turtle
import pandas as pd

IMAGE = "indian_map.gif"
screen = turtle.Screen()
screen.title("Indian States Game")
screen.setup(800, 900)


screen.addshape(IMAGE)
turtle.shape(IMAGE)

# todo this code is for detecting the coordinate of the place on map
# def get_mouse_click_coordinate(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coordinate)
# turtle.mainloop()

# --- Load Data ---
data = pd.read_csv("states.csv")
states = data["state"].to_list()

score = 0
guessed_states = []

# --- Function for Input Box ---
def input_score_board():
    ans_state = screen.textinput(
        title=f"{score}/{len(states)} Guess the State",
        prompt="What's another state name you know?"
    ).strip().lower()
    return ans_state


# --- Main Game Loop ---
while len(guessed_states) < len(states):
    ans = input_score_board()
    if ans == "exit":
        break

    # Case-insensitive match
    state_data = data[data.state.str.lower() == ans.lower()]

    if not state_data.empty and state_data.state.iloc[0].title() not in guessed_states:
        guessed_states.append(state_data.state.iloc[0].title())
        score += 1

        writer_turtle = Turtle()
        writer_turtle.hideturtle()
        writer_turtle.penup()

        x = int(state_data.x.iloc[0])
        y = int(state_data.y.iloc[0])

        writer_turtle.goto(x, y)
        writer_turtle.write(state_data.state.iloc[0].title(), align="center", font=("Arial", 8, "normal"))
    else:
        print(f"Not found or already guessed: {ans}")

# --- Exit ---
screen.exitonclick()
