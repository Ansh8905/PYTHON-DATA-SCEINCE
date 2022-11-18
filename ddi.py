a=int(input("enter a number="))
if(a==1):
    print("no is prime if wala")
for i in range(2,a+1):
    if(a%i==0):
        print("number is not prime for wala")
        break
    else:
        print ("number is prime for wala")
        break
else:
    print("no is not prime if wala")
    


