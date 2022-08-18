x=[2,3,4,5]
x2=[ i **2 for i in x]
print (x2)
print (x)
y = [2,3,4,5]

z = [ i + j for i , j in zip (x,y)]
print (z)