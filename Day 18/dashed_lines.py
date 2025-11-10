import turtle as t

turtle = t.Turtle()
screen = t.Screen()
turtle.color("blue")

for _ in range(50) :
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)

screen.exitonclick()