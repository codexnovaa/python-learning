#Weight conversion


try:
    weight = float(input("Enter your weight: "))
    unit = input("Kilograms or Pounds? (K or L): ")

    if unit.lower() == "k":
        result = weight * 2.205
        print(f"Your weight is {round(result, 2)}Lbs")
    elif unit.lower() == "l":
        result = weight / 2.205
        print(f"Your weight is {round(result, 2)}Kgs")
    else:
        print("unit invalid")
except ValueError as error:
    print(error)
    




