# Event the interrupts the program

try:
    number = int(input("Enter a number: "))
    result = number / 2
    print(result)
except ZeroDivisionError as error:
    print(f"Cannot divide by 0 - {error} ")
except ValueError as error:
    print(f"Invalid Value - {error}")
except Exception as error:
    print(f"Something went wrong! - {error}")
finally:
    print("You need to clean up here")