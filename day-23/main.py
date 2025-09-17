import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(fun=player.turtle_move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car = random.randint(0,6)
    cars.create_car(car)

#   detecting the collision
    for car in cars.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            score.game_over()

#   detect crossing the game
    if player.is_on_final_line():
        player.goto_start()
        cars.level_up()
        score.score_update()

screen.exitonclick()