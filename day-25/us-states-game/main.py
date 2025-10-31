import turtle
from turtle import Turtle
import pandas as pd

# --- Setup screen ---
IMAGE = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S. States Game")

screen.addshape(IMAGE)
turtle.shape(IMAGE)

# --- Load data ---
data = pd.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

# --- Helper function ---
def get_answer():
    return screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="Guess another state's name (or type 'Exit' to quit):"
    )

# --- Main Game Loop ---
while len(guessed_states) < 50:
    answer = get_answer()
    if not answer:
        break

    answer = answer.title()

    if answer == "Exit":
        # Save missing states to CSV
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv", index=False)
        print("File 'states_to_learn.csv' created with remaining states.")
        break

    if answer in all_states and answer not in guessed_states:
        guessed_states.append(answer)
        state_data = data[data.state == answer]

        # Create writer turtle
        writer = Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        writer.write(answer, align="center", font=("Arial", 8, "normal"))

    elif answer in guessed_states:
        print(f"You already guessed {answer}.")
    else:
        print(f"{answer} is not a valid U.S. state name.")

# --- End screen ---
screen.exitonclick()
