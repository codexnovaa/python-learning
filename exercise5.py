#Validate user input exercise
# username is no more than 12 characters
# username must not contain spaces
# username must not contain digits


username = input("Enter your username: ")
identity = input("Select your identity (M/F))")

if len(username) > 12:
    print("Username must contain only of 12 characters.")
elif not username.find(" ") == -1:
    print("Username can't contain any spaces")
elif not username.isalpha():
    print("Username can't contain any numbers")
else:
    if identity.lower() == "m":
        print(f"A pleasant day, Mr. {username}")
    elif identity.lower() == "f":
        print(f"A pleasant day, Ms. {username}")
    else:
        print(f"A pleasent day, {username}")
    