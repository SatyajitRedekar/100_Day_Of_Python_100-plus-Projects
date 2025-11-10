import turtle
from turtle import Turtle
import pandas as pd

IMAGE = "indian_map.gif"
screen = turtle.Screen()
screen.title("Indian States Game")
screen.setup(800, 900)

screen.addshape(IMAGE)
turtle.shape(IMAGE)

# --- Load Data ---
data = pd.read_csv("states.csv")
states = data["state"].to_list()

score = 0
guessed_states = []

# todo this code is for detecting the coordinate of the place on map
# def get_mouse_click_coordinate(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coordinate)
# turtle.mainloop()

# --- Function for Input Box ---
def input_score_board():
    answer = screen.textinput(
        title=f"{score}/{len(states)} Guess the State",
        prompt="What's another state name you know? (Type 'Exit' to quit)"
    )
    if answer:
        return answer.strip().title()
    return None

# --- Main Game Loop ---
while len(guessed_states) < len(states):
    ans = input_score_board()
    if ans is None:
        break

    if ans.lower() == "exit":
        missing_states = [state for state in states if state.title() not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv", index=False)
        print("File 'states_to_learn.csv' created with remaining states.")
        break

    # Check if state exists and not already guessed
    if ans in states and ans not in guessed_states:
        guessed_states.append(ans)
        score += 1

        state_data = data[data.state == ans]
        writer_turtle = Turtle()
        writer_turtle.hideturtle()
        writer_turtle.penup()

        x = int(state_data.x.iloc[0])
        y = int(state_data.y.iloc[0])
        writer_turtle.goto(x, y)
        writer_turtle.write(ans, align="center", font=("Arial", 8, "normal"))
    else:
        print(f"Not found or already guessed: {ans}")

# --- Exit ---
screen.exitonclick()
