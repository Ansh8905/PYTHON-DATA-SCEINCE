x = [1,2,3,4,5,6,7,8,1,2,2,]


x2 = list (map(lambda i: i**2, x))

x3 = tuple(map(lambda i : i**3, x))


print(x2)
print(x3)

y= ['apple', 'banana' , 'cheery']
z= [ 'pie', 'shake', 'jam']

words= set(map(lambda a,b: a+'-' +b, y,z))
print(words)


# single line inputn with multiple values


numbers =list(map(int, input('enter 10 numbers:').split()))
print(numbers)

