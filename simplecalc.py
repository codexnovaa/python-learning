operator = input("Select an operator(+, -, *, /, %)")
num1 = float(input("Please enter your first number: "))
num2 = float(input("Please enter your second number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 2))
elif operator == "-":
    result = num1 - num2
    print(round(result, 2))
elif operator == "*":
    result = num1 * num2
    print(round(result, 2))
elif operator == "/":
    result = num1 / num2
    print(round(result, 2))
elif operator == "%":
    result = num1 % num2
    print(result)
else:
    print("Please select an operator")