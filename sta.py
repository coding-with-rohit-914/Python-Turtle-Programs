import turtle as t
import colorsys
s=t.Screen()
t.title("Python Turtle Art")
t.tracer(2)
t.pensize(2)
t.bgcolor("black")
h=5
t.goto(0,70)

for n in range(260):
    c=colorsys.hsv_to_rgb(h,1,1)
    t.color(c)
    h+=0.007
    for p in range(4):
        t.forward(n)
        t.right(60)
        t.right(60)
    t.right(120)  
    t.hideturtle() 
 
t.done()
