'''
import time
from calendar import isleap

# judge the leap year
def judge_leap_year(year):
    if isleap(year):
        return True
    else:
        return False
    
# returns the number of days in each month
def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and (not leap_year):
        return 28
    
name = input("input your name:")
age = input("input your age:")
localtime = time.localtime(time.time())

year = int(age)
month = year * 12 + localtime.tm_mon
day = 0

begin_year = int(localtime.tm_year) - year
end_year = begin_year + year

# calculate the days
for y in range(begin_year, end_year):
    if (judge_leap_year(y)):
        day = day + 366
    else:
        day = day + 365

leap_year = judge_leap_year(localtime.tm_year)
for m in range(1, localtime.tm_mon):
    day = day + month_days(m, leap_year)

day = day + localtime.tm_mday
print("%s's age is %d years or " % (name, year), end="")
print("%d months or %d days" % (month, day))
'''
'''
import subprocess
data = (
subprocess.check_output(["netsh", "wlan", "show", "profiles"])
.decode("utf-8")
.split("\n")
)
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    results = (
subprocess
.check_output(["netsh", "wlan", "show", "profile", i, "key=clear"])
.decode("utf-8")
.split("\n")
)
results = [b.split(":")[1][1:-1] for b in results if "Key Content" in
b]
try:
    print("{:<30}| {:<}".format(i, results[0]))
except IndexError:
    print("{:<30}| {:<}".format(i, ""))
'''
'''
import tkinter as Tkinter
from datetime import datetime
counter = 0
running = False

def counter_label(label):
    def count():
        if running:
            global counter

# To manage the intial delay.

            if counter == 0:
                display = 'Ready!'
            else:
                tt = datetime.utcfromtimestamp(counter)
                string = tt.strftime('%H:%M:%S')
                display = string

            label['text'] = display

# label.after(arg1, arg2) delays by
# first argument given in milliseconds
# and then calls the function given as second argument.
# Generally like here we need to call the
# function in which it is present repeatedly.
# Delays by 1000ms=1 seconds and call count again.

            label.after(1000, count)
            counter += 1

# Triggering the start of the counter.
    
    count()

# start function of the stopwatch

def Start(label):
    global running
    running = True
    counter_label(label)
    Start['state'] = 'disabled'
    Stop['state'] = 'normal'
    Reset['state'] = 'normal'

# Stop function of the stopwatch

def Stop():
    global running
    Start['state'] = 'normal'
    Stop['state'] = 'disabled'
    Reset['state'] = 'normal'
    running = False

# Reset function of the stopwatch

def Reset(label):
    global counter
    counter = 0

# If reset is pressed after pressing stop.

    if not running:
        Reset['state'] = 'disabled'
        label['text'] = '00:00:00'

# If reset is pressed while the stopwatch is running.

    else:
        label['text'] = '00:00:00'
root = Tkinter.Tk()
root.title("Stopwatch")

# Fixing the window size.

root.minsize(width=250, height=70)
label = Tkinter.Label(root, text='Ready!', fg='black', font='Verdana 30'
'bold')
label.pack()
f = Tkinter.Frame(root)
start = Tkinter.Button(f, text='Start', width=6, command=lambda:
Start(label))
stop = Tkinter.Button(f, text='Stop', width=6, state='disabled',
command=Stop)
reset = Tkinter.Button(f, text='Reset', width=6, state='disabled',
command=lambda: Reset(label))
f.pack(anchor='center', pady=5)
start.pack(side='left')
stop.pack(side='left')
reset.pack(side='left')
root.mainloop()
'''
