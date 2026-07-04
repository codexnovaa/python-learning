#Concession Menu Program

menu = {
    "pizza": 3.00,
    "nachos": 4.00,
    "fries": 6.00,
    "burger": 5.50,
    "chips": 3.50,
    "soda": 3.00,
    "lemon": 4.50,
}

cart = []
total = 0
print("-----MENU-----")
for key, value in menu.items():
    print(f"{key:7}: {value:.2f}")
print("--------------")

while True:
    food = input("Select the food (press q to quit): ").lower()
    if food.lower() == "q":
        break
    elif menu.get(food) == None:
        print("This food is not on the menu")
    elif menu.get(food) is not None:
        cart.append(food)

print()        
print("-----ORDERED FOODS-----")
for food in cart:
    print(f"{food:7}: {menu[food]:.2f}")
print()

for item in cart:
    total += menu[item]
    
print("-------TOTAL-------")
print(f"The total amount is ${total:.2f}")
print("-------------------")


