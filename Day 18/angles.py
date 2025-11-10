import random
import turtle as t

turtle = t.Turtle()
screen = t.Screen()
turtle.color("blue")

colors = [
    "red", "green", "blue", "yellow", "orange", "purple", "pink",
    "black", "white", "gray", "brown", "cyan", "magenta", "lime",
    "navy", "teal", "maroon", "olive", "gold", "silver"
]


for num in range(3,10) :
    for _ in range(num) :
        turtle.color(random.choice(colors))
        turtle.forward(80)
        turtle.right(360/num)

screen.exitonclick()