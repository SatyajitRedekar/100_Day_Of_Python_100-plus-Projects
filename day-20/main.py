from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=600, height=600)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.turn_up,key="Up")
screen.onkey(fun=snake.turn_down,key="Down")
screen.onkey(fun=snake.turn_left,key="Left")
screen.onkey(fun=snake.turn_right,key="Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    # collision detection
    if snake.head.distance(food) < 10 :
        print("Food detected")
        food.refresh()
        scoreboard.score += 1
        snake.extend()
        scoreboard.update_score()

    # collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        is_game_on = False

    # collision with tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            is_game_on = False

    snake.move()

screen.exitonclick()
