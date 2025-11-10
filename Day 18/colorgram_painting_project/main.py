import random
import turtle as t

import colorgram
colors = colorgram.extract('hirst.jpg', 30)
colors_list = []
for x in range(30) :
    first_color = colors[x]
    r = first_color.rgb[0]
    g = first_color.rgb[1]
    b = first_color.rgb[2]
    if r >= 230 : # eliminate white color to append
        continue
    else:
        colors_list.append((r,g,b))
print(colors_list)

# colors_list = [
#  (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49),
#  (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22),
#  (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]

turtle = t.Turtle()
screen = t.Screen()

t.colormode(255)
turtle.speed("fastest")
turtle.hideturtle()
turtle.penup()
turtle.setheading(220)
turtle.forward(350)
turtle.setheading(0)
turtle.dot(20,random.choice(colors_list))
i =0
def up() :
    for _ in range(9) :
        turtle.forward(50)
        turtle.dot(20,random.choice(colors_list))
    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(180)
    turtle.dot(20, random.choice(colors_list))

def down():
    for _ in range(9) :
        turtle.forward(50)
        turtle.dot(20,random.choice(colors_list))

for x in range(5) :
   up()
   down()
   if x == 4:
       turtle.setheading(90)
       turtle.forward(50)
       turtle.setheading(0)
   else:
       turtle.setheading(90)
       turtle.forward(50)
       turtle.dot(20, random.choice(colors_list))
       turtle.setheading(0)

screen.exitonclick()





