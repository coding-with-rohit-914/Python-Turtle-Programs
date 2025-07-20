from turtle import *
import colorsys as cs
bgcolor("black")
pensize(3)
h=0.2

for i in range(1000):
    c=cs.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.004
    fd(i)
    rt(75)
    fd(100)
    rt(120)

hideturtle()
done()