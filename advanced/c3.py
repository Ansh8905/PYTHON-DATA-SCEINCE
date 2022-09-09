from turtle import color
from unicodedata import name

from numpy import size


class Fruit:
    color = 'red'
    taste = 'sweet'

class Veg:
    size = 'small'
    age = 'fresh'

class GM(Fruit, Veg):
    name = 'GM-122'

g = GM()

print(g.name)
print(g.color)
print(g.taste)
print(g.size)
print(g.age)


#2


class Calculation1:
    def Sumation(self,a,b):
        return a+b;
class Calculation2:
    def Multiplication(self,a,b):
        return a*b;
class Derived(Calculation1,Calculation2):
    def Divide(self,a,b):
        return a/b;
d = Derived()
print(d.Sumation(10,20))
print(d.Multiplication(10,20))
print(d.Divide(10,20))