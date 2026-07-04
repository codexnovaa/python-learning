#Exercise 2 Simple Shopping

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input(f"How many {item} would you like?: "))
total = price * quantity

print(f"You have bought {quantity}x {item}")
print(f"The total amount is ${round(total, 2)}")