# Multicolor pattern in python found on IG

import turtle

col=['yellow','red','green','orange','white','blue','pink']

t=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor('black')
t.speed(10)

for i in range(150):
    t.color(col[i%7])
    t.forward(i*3)
    t.left(150)
    t.width(2)