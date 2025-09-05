from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.sety(270)
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.pensize(4)
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write(f"GAME OVER\n    Score : {self.score}", False, "center", ("Arial", 24, "normal"))

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score}", False, "center", ("Arial", 15, "normal"))