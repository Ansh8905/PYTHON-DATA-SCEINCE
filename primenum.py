num = int(input("Enter A Number:"))
if num >1:
    for i in range(2,num):
        if(num % i )==0:
            print (num ,"is not a prime number")
            break
    else:
        print(num ,"num is a prime number")
