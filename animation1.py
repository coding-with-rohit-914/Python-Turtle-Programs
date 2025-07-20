from turtle import*
bgcolor("black")
speed(0)
for i in range(140):
    color("green")
    right(1)
    backward(1)
    for j in range(1):
        right(2)
        circle(110)
        hideturtle()
done()

# from sketchpy import library
# myObject = library.tom_holland()
# myObject.draw()