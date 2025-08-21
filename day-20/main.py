from turtle import Turtle, Screen
from snake import Snake
import time


screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=600, height=600)

snake = Snake()

screen.listen()
screen.onkey(fun=snake.turn_up,key="Up")
screen.onkey(fun=snake.turn_down,key="Down")
screen.onkey(fun=snake.turn_left,key="Left")
screen.onkey(fun=snake.turn_right,key="Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
