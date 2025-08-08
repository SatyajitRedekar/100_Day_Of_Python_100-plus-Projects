import random
from turtle import Turtle,Screen

screen = Screen()
screen.setup(width=800, height=600)
turtle = Turtle()
turtle.hideturtle()

colors = ["violet","red","blue","green","brown","yellow","orange","pink","maroon"]
y_cord = [160,120,80,40,0,-40,-80,-120,-160]
all_turtles = []
is_race = False

user_input = screen.textinput(title="make your bet satyajit",prompt="type the color (violet,red,blue,green,brown,yellow,orange,pink,maroon)")
for player in range(9) :
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.shapesize(2)
    new_turtle.color(colors[player])
    new_turtle.goto(x=-360,y=y_cord[player])
    all_turtles.append(new_turtle)

line = Turtle()
line.hideturtle()
line.penup()
line.goto(x=360,y=200)
line.pendown()
line.goto(x=360,y=-200)

if user_input:
    is_race = True
def show_win_popup(result,winner):
            turtle.clear()
            turtle.hideturtle()
            turtle.penup()
            turtle.goto(0, 0)
            turtle.color("green")
            turtle.write(f" 🎉 you {result}! 🎉\n{winner} won game", align="center", font=("Arial", 30, "bold"))

while is_race :

    for player in all_turtles:
        if player.xcor() > 360 :
            is_race = False
            winning_player = player.pencolor()
            if winning_player == user_input:
                show_win_popup("won",winning_player)
            else:
                show_win_popup("lose",winning_player)



        player.fd(random.randint(1,10))



screen.exitonclick()
