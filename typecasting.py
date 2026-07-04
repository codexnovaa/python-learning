#Converting a variable from one data type to another
#Functions str(), int(), float(), bool()

name = ""
age = 17
height = 5.6
isStudent = True


if name == "":
    print("Please enter a name")
elif len(name) <= 2:
    print("Your name needs to be atleast 3 characters")
else:
    print(name)
