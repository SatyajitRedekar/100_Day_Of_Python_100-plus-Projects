FONT = ("Courier", 24, "normal")

from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(-260,260)
        self.clear()
        self.level = 1
        self.write(f"Level : {self.level}",font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over !",False,"center",FONT)

    def score_update(self):
        self.level += 1
        self.clear()
        self.write(f"Level : {self.level}",font=FONT)