my_dict = { 'name': 'jack' , 'age': 26}

print(my_dict['name'])
print(my_dict.get('age'))

#print(my_dict['address'])

print(my_dict.get('address'))

#uodate
my_dict['age'] = 27
print(my_dict)

#add item 
my_dict ['address'] = 'downtown'
print(my_dict)


#create a dictionary
squares = {1: 1,2: 4, 3:9,  4:16 , 5:25}
print(squares.pop(4))
print(squares.popitem())
print(squares.clear())


squares = {1: 1,2: 4, 3:9,  4:16 , 5:25}
#only keys 
for i in squares:
    print(i)
#only values using i as keys 
for i in squares:
    print(squares[i])
#using items () fumctions to get both key and value 
for k,v in squares.items():
    print(k,v)

