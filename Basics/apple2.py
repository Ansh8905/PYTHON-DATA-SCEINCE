amt = int(input('how much kg of apple u want?'))

if amt >= 5:
    price = 80
else:
    price = 90
total  = amt * price
print(f"you have to pay Rs.{total} for {amt} KG. of apples")