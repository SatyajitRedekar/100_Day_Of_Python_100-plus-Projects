from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.random_y = None
        self.random_x = None
        self.speed("fastest")
        self.shape("square")
        self.color("green")
        self.shapesize(1)
        self.penup()
        self.refresh()

    def refresh(self):
        self.random_x = random.randint(-280, 280)
        self.random_y = random.randint(-280, 280)
        self.goto(self.random_x, self.random_y)