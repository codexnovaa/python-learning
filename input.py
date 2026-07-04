#Input function = A function that promts and let the user to enter a data and returs data as string

name = input("Please enter your name: ")
age = input("Please enter your age: ")


if not age.isdigit():
    print("String are not allowed")
    
else:
    age = int(age)
    
    if age > 100:
        print(f"You are awesome {name}")
    elif age >= 60:
        print(f"You are a Senior Citizen {name}")
    elif age >= 18:
        print(f"You are an adult {name}")
    else:
        print(f"You are a minor {name}")
    