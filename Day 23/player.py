STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

import scoreboard as score
from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto_start()
        self.setheading(90)
    def turtle_move(self):
        if self.ycor() <= 280 :
            self.forward(MOVE_DISTANCE)

        elif self.ycor() == 280 :
            score.Scoreboard().score(1)

    def goto_start(self):
        self.goto(STARTING_POSITION)

    def is_on_final_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False
