import turtle
from time import perf_counter
import time
def anim(x, y, z):
    data = [x]
    for i in range(1,y):
        a = x.clone()
        a.rt(360/y)
        data.append(a)
        x = a
    for j in range(y):
        color = abs(y/2-j)/(y*0.6)
        for i in data:
            i.rt(360/y)
            i.pencolor(color,1-color,
                color)
            i.fd(z)
def main():
    screen = turtle.Screen()
    screen.bgcolor('black')
    t = turtle.Turtle()
    t.speed(1)
    t.pensize(3)
    screen.tracer(46, 0)
    cont = perf_counter()
    anim(t, 48, 18)
    cont1 = perf_counter()
    dif = cont1 - cont
    time.sleep(2)
    cont = perf_counter()
    while any(t.undobufferentries() 
    for t in screen.turtles()):
        for i in screen.turtles():
            i.undo()
    cont1 = perf_counter()
    return 'runtime: %.4f sec' % (
        dif + cont1 - cont)

if __name__ =='__main__':
    for i in range(3):
        main()
    turtle.mainloop()