from turtle import Turtle

class PaddleTwo(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.goto(360, 0)
        self.color("white")
        self.shape("square")
        self.shapesize(1,4)
    def move_up(self):
        print(self.ycor())
        if self.ycor() < 245 :
            self.setheading(90)
            self.forward(20)

    def move_down(self):
        if self.ycor() > -245 :
            self.setheading(270)
            self.forward(20)
