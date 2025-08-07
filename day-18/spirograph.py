import random
import turtle as t

turtle = t.Turtle()
screen = t.Screen()
t.colormode(255)

def random_color():
    r = random.choice(range(255))
    g = random.choice(range(255))
    b = random.choice(range(255))
    return r,g,b

degree = 0

def draw_spirograph(gap_size) :
    for _ in range(int(360/gap_size)):
        turtle.speed("fastest")
        turtle.pencolor(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + gap_size)

draw_spirograph(5)

screen.exitonclick()