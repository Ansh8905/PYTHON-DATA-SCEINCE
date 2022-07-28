from typing_extensions import get_overloads


val = int(input('>>Enter a number:'))
if val > 100:
    val = val / 2
else:
    val = val * 2
print('>>The result is :' , val)

# true if condition else false
val = int(input('>>Enter a number:'))
val = val/2 if val>100 else val*2
print('>>The result is :' , val)

name= input ("Enter ur Name")
name = print("Good") if  Name.isalpha() else print ("not good")