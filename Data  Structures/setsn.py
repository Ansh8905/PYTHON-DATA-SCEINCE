my_set =  { 1, 2 ,3,4, 5,2, 3}
print(my_set)


my_set = set[(1, 2 ,3,4, 5,2, 3)]
print(my_set)


#my_set = { 1 ,2 ,[3,4]}     error

#initialise my set
my_set = {1, 3}
print(my_set)

#dd an element 
my_set.add(2)
print(my_set)

#add multiple element
my_set.update([2,3.4])
print(my_set)

#ad list and set
my_set.update([4,5] , { 1, 6 , 8})
print(my_set)


#initialise my set
my_set = {1,3,4,5,6}
print(my_set)

#discaerd an element


my_set.discard(4)
print(my_set)

#pop a randon iyem
my_set.pop()
print(my_set)

my_set.remove(6)
print(my_set)

my_set.clear()
print(my_set)