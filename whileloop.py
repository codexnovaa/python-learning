#While loop

#name = input("Please enter your name: ")

#while name == "":
    #print("You did not enter any name!")
    #name = input("Please enter your name: ")
#print(f"Hello there! {name}")

try:
    age = int(input("Please enter your age: "))
    
    while age <= 0:
        print("Invalid age") 
        age = int(input("Please enter your age: "))
    
    if age >= 60:
        print("You are a Senior Citizen.") 
    elif age >= 18:
        print("You are an adult.")
    elif age <= 17:
        print("You are a minor.")
    
except ValueError as e:
    print(str(e))