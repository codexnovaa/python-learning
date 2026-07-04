#Simple shopping cart


foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy. Press (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input("Enter the price of the food: "))
        foods.append(food)
        prices.append(price)

print("----YOUR CART----")

for food, price in zip(foods, prices):
    print(f"{food.capitalize()}: ₱{price:.2f}")
    
print("----RECEIPT----")

for cost in prices:
    total += cost

print(f"The total cost of your cart is: ₱{total:.2f}")