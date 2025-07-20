from turtle import *
from time import sleep
bgcolor('black')
t = [Turtle(), Turtle()]
x=4
color=["yellow", "blue", "red", "orange"]
for index, i in enumerate(t):
    i.speed(0)
    i.color("white")
    i.shapesize(0.5)
    i.width(5)
    i.penup()
    i.seth(90)
    i.forward(230)
    i.seth(-180)
    i.pendown()
    t[0].penup()
    for i in color:
      color(i)
    for i in range(360):
      t[0].forward(x)
      t[0].left(1)
      penup()
      goto([0].pos())
      pendown()
      t[1].forward(2*x)
      t[1].left(2)
      goto(t[1].pos())
done()