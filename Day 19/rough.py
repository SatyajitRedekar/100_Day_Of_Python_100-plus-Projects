from turtle import Turtle,Screen

turtle = Turtle()
screen = Screen()

def forward():
    turtle.forward(20)

screen.listen()
screen.onkey(key="space",fun=forward)

# positional arg -> call side fun( 1, 2, 3)
# keyword arg -> call side fun(a=1, b=2, c=3)

screen.exitonclick()