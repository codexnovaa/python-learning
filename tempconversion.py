#Simple Temperature Conversion

try:
    unit = input("The temperature is Celcius or Fahrenheit? (C/F): )")
    temp = float(input("Enter the temperature: "))
    
    if unit.lower() == "c":
        result = round((temp * 9/5) + 32, 2)
        print(f"The temperature in Fahrenheiit is {round(result, 2)}°F")
    elif unit.lower() == "f":
        result = round((temp - 32) * 5/9, 2)
        print(f"The temperature in Celcius is {round(result, 2)}°C")
    
except ValueError as e:
    print(e)