import turtle
import colorsys
turtle.bgcolor("black")
def spiral():
    turtle.speed(0)
    turtle.hideturtle()
    for i in range(500):
        c=colorsys.hsv_to_rgb(i/500,1,1)
        turtle.color(c)
        turtle.forward(i)
        turtle.left(115)
    turtle.done()
spiral()