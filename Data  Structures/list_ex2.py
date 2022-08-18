x=[2,3,4,5]
y=[6,7,8,9]
z=[]
for i in range (0 , len (x)):
    z.append(x[i] + y[i])
print (z)


#2

x=[2,3,4,5]
y=[6,7,8,9]
z=[]
for i , j in zip (x,y):
    z.append(i+j)
print(z)



#loops
#comprehension(1 line expression)
#lamda expression