from turtle import Turtle
SNAKE_BODY = [(-20, 0), (-40, 0), (-60, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
    def create_snake(self):
        for cord in SNAKE_BODY:
            new_turtle = Turtle(shape="square")
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.goto(cord)
            self.segment.append(new_turtle)

    def turn_up(self):
        if self.head.heading() != DOWN :
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP :
            self.head.setheading(DOWN)

    def turn_right(self):
        if self.head.heading() != LEFT :
            self.head.setheading(RIGHT)

    def turn_left(self):
        if self.head.heading() != RIGHT :
            self.head.setheading(LEFT)

    def move(self):
        for segment in range(len(self.segment) - 1, 0, -1):
            x = self.segment[segment - 1].xcor()
            y = self.segment[segment - 1].ycor()
            self.segment[segment].goto(x, y)
        self.head.fd(20)

