import time  
import datetime as dte  
import turtle    
tt1 = turtle.Turtle()   
tt2 = turtle.Turtle()  
screen = turtle.Screen()  
screen.bgcolor("pink")  
secs = dte.datetime.now().second  
mins = dte.datetime.now().minute  
hrs = dte.datetime.now().hour  
tt2.pensize(3)  
tt2.color('black')  
tt2.penup()  
tt2.goto(-15, -15)  
tt2.pendown()  
  
for j in range(2):  
   tt2.forward(200)  
   tt2.left(90)  
   tt2.forward(70)  
   tt2.left(90)      
   tt2.hideturtle()    
while True:  
   tt1.hideturtle()  
   tt1.clear()  
   tt1.write(str(hrs).zfill(2)  
            + ":"+str(mins).zfill(2)+":"  
            + str(secs).zfill(2),  
            font=("Callibri Narrow", 37, "bold"))  
   time.sleep(1)  
   secs += 1  
   if secs == 60:  
       secs = 0  
       mins += 1  
   if mins == 60:  
       mins = 0  
       hrs += 1  
   if hrs == 13:  
       hrs = 1  