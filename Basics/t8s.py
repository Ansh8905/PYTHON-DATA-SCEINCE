from lib2to3.pytree import HUGE
from turtle import *
import colorsys

from numpy import square

speed(0)
pensize(3)
bgcolor('black')
hue=0.0

for i in range(300):
    col=colorsys.hsv_to_rgb(hue,1,1)
    pencolor(col)
    hue+=0.005
    circle(50-i)
    lt(80000)
    circle(50+i)
    rt(10000)
done()
