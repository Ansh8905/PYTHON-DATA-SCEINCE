a=1,1,2,3,4,1,5,1,6,1,7,8,1,2,1,2,1][

clean_a = list(filter(lambda i: i != 1 , a))
print(clean_a)

files= ['a.png', 'b.jpg','c.jpg','d.png']
jpeg = list(filter(lambda name: name.endswith('.jpg'),files))
png = list(filter(lambda name: name.endswith('.png'),files))
print(jpeg)
print(png)