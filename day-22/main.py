
from turtle import Turtle, Screen
from paddle_one import PaddleOne
from paddle_two import PaddleTwo
from score_board import ScoreBoard
from ball import Ball
import time

score = ScoreBoard()

screen = Screen()
turtle = Turtle()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong Game By Satyajit Redekar")

player_one = PaddleOne()
player_two = PaddleTwo()

def line() :
    screen.tracer(0)
    turtle.penup()
    turtle.goto(0,300)
    turtle.pendown()
    turtle.setheading(270)
    turtle.speed("fastest")
    turtle.hideturtle()
    turtle.color("white")
    for _ in range(11) :
        turtle.pendown()
        turtle.forward(48)
        turtle.penup()
        turtle.forward(8)


line()
ball = Ball()

screen.update()

# player one thing
screen.listen()
screen.onkey(fun=player_one.move_up,key="w")
screen.onkey(fun=player_one.move_down,key="s")

# player two thing
screen.onkey(fun=player_two.move_up,key="Up")
screen.onkey(fun=player_two.move_down,key="Down")

game_is_on = True
i = 0.1
while game_is_on:
    time.sleep(i)
    screen.update()
    ball.move()

    # detecting collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce("y_move")
    elif ball.distance(player_one) < 50 and (ball.xcor() > 340 or ball.xcor() < -340) :
        ball.bounce("x_move")
    elif ball.distance(player_two) < 50 and (ball.xcor() > 340 or ball.xcor() < -340) :
        ball.bounce("x_move")
    elif ball.xcor() > 380 :
        score.update_score("p1")
        ball.goto(0, 0)
    elif ball.xcor() < -380 :
        score.update_score("p2")
        ball.goto(0, 0)







screen.exitonclick()