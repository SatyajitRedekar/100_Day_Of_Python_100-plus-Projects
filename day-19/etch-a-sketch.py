from turtle import Turtle,Screen

turtle = Turtle()
screen = Screen()

def forwards():
    turtle.forward(10)
def backwards():
    turtle.backward(10)
def clock_wise():
    turtle.right(10)
def anti_clock():
    turtle.left(10)
def clear():
    turtle.reset()

screen.listen()
screen.onkey(key="w",fun=forwards)
screen.onkey(key="s",fun=backwards)
screen.onkey(key="a",fun=clock_wise)
screen.onkey(key="d",fun=anti_clock)
screen.onkey(key="c",fun=clear)


screen.exitonclick()