from turtle import *
from time import sleep

bgcolor("black")
t1 = Turtle()
t2 = Turtle()
x = 6
t1.shapesize(0.3)
t1.pu()
t1.seth(90)
t1.fd(350)
t1.seth(-180)
t1.pd()

delay(0)
speed(50)
t1.ht()
t2.ht()

sleep(4)

colors = ["red", "blue", "green", "yellow"]

for color in colors:
    t1.color(color)
    for i in range(360):
        t1.fd(x)
        t1.lt(1)
        pu()
        goto(t1.pos())
        pd()
        t2.fd(2 * x)
        t2.lt(2)
        goto(t2.pos())

done()