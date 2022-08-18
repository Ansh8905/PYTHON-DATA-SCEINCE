#tupples with mixed  datatypes
my_tuple = (1 , "Hello" , 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [ 8,4,6], (1,2,3))
print(my_tuple)

#tuples

my_tuple = 3, 4, 5, "Apple"
print(my_tuple)

#access tuple element ussing indexing
my_tuple =('o' 't' 'h' 'j' 'k' 'l' 'b' 'a' )
print(my_tuple[0])
print(my_tuple[5])

#nested tuple
n_tuple = ("mouse", [ 8,4,6], (1,2,3))
#nested index
print(n_tuple[0][3])
print(n_tuple[1][1])


#accessing tuple element ussing slicing
my_tuple =('o' 't' 'h' 'j' 'k' 'l' 'b' 'a' 'd' 'w' 'q' 'e' 'n' 'm' )
print(my_tuple[1:4])
print(my_tuple[:-7])
print(my_tuple[7:])
print(my_tuple[:])

#concatenation
print((1,2,3) + (4,5,6))
#repeat
print(("Repeat",) * 3)


my_tuple = ('a' ,'p' ,' p' ,'l')