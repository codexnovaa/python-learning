#Simple compound interest calculator


principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than or equal to zero.")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("rate can't be less than or equal to zero.")
    else:
        break
        
while True:
    time = int(input("Enter the time rate: "))
    if time < 0:
        print("time can't be less than or equal to zero.")
    else:
        break

total = principle * (1 + rate / 100) ** time
print(f"Balance after {time} year/s with the interest rate of {rate:.2f}% is ${total:.2f}.")