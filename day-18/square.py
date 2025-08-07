from turtle import Turtle,Screen

turtle = Turtle()
screen = Screen()

turtle.color("green")

for num in range(4) :
    turtle.forward(100)
    turtle.right(90)



screen.exitonclick()