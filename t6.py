from tracemalloc import start
from turtle import *
speed(0)
start = 500
goto(-150, -150)
while start > 0 :
    forward(start)
    left(360/6)
    start -=1
    write (start , font = ('arial' ,8 , 'normal' ))

mainloop()