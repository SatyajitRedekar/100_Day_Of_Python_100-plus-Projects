from turtle import Turtle



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.move_speed = 0.1
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        print(f"x : {new_x} , y : {new_y}")
        self.goto(new_x, new_y)

    def bounce(self,move):
        print(f"before the bounce : {self.y_move}")
        if move == "y_move" :
            self.y_move *= -1
        if move == "x_move" :
            self.x_move *= -1
            self.move_speed *= 0.9
        print(f"after the bounce : {self.y_move} ")

    def reset_ball(self):
        self.goto(0,0)
        self.bounce("x_move")
        self.move_speed = 0.1

