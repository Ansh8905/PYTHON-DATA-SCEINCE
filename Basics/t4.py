from turtle import *

side = 6
size = 150
pensize(5)
for i in range (side):
    pencolor('red')
    forward(size)
    for i  in range (6):
        pencolor('blue')
        forward (75)
        left (360/6)
        write(i, font=('Arial' , 14 , 'normal'))
    left(360/side)

mainloop()