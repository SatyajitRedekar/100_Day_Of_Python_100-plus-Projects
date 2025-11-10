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

directions = [0,90,180,270]

while True:
    turtle.pensize(15)
    turtle.pencolor(random_color())
    turtle.forward(30)
    turtle.setheading(random.choice(directions))
    turtle.speed("fast")

screen.exitonclick()