#syntax
#def fun_name0([parameter]):
#         statements
#            [return exppression]

#defining
def hello():
    print('👋hello👋')
    print('world🌍')

#calling or using
hello()
hello()

def greetings(message):
    print('👋', message)

greetings('world')
greetings('halo animals')
greetings('baonjour anis')
greetings('namste dosto')


def calc_area(w,h):
    area = w*h
    print('area:', area)


calc_area(10, 20)
calc_area(30000000000000, 400000)
calc_area(59999, 69999999999999999999999999999)


#siple module
def add(x, y):
    add = x+y
    print ('add:', add)


add (4, 3)
add  (773789372, 7827928090287299 )




def calc_area_v2(w, h):
    area = w * h
    return area

#display
print (calc_area_v2(10, 12))
print (calc_area_v2(4, 5))

# storing returm valuues in a expression
ans = calc_area_v2(10, 20)
print(ans)

#using return values in a expression
ans = calc_area_v2(3, 5)+calc_area_v2(50 , 30)
print(ans)