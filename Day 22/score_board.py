from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.sety(250)
        self.score_p1 = 0
        self.score_p2 = 0
        self.color("white")
        self.pensize(4)
        self.update_score("first")

    def update_score(self,won_p):
        if won_p == "p1" :
            self.score_p1 += 1
        elif won_p == "first" :
            pass
        else:
            self.score_p2 += 1
        self.clear()
        self.write(f"{self.score_p1}     {self.score_p2}", False, "center", ("Arial", 25, "normal"))