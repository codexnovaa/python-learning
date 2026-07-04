#Simple bank exercise


def showBalance(balance):
    print("--------------")
    print(f"Current Balance Amount: ₱{balance:,.2f}")
    print("--------------")
    

def deposit():
    print("--------------")
    amount = float(input("Enter an amount to be deposited: "))
    if amount <= 0:
        print("Error! Please enter a valid amount")
        return 0
    question = input("Press 1 to Proceed | Press 2 to Cancel: ")
    if question == "1":
        return amount
    elif question == "2":
        return 0
    else:
        print("Invalid Input")
        return 0
    print("--------------")

def withdraw(balance):
    print("--------------")
    amount = float(input("Enter an amount to be withdrawn: "))
    if amount > balance:
        print("Insufficient Balance.")
        return 0
    elif amount < 0:
        print("Please input a valid amount")
        return 0
    else:
        question = input("Press 1 to Proceed | Press 2 to Cancel: ")
        if question == "1":
            return amount
        elif question == "2":
            return 0
        else:
            print("Invalid Input")
            return 0
    print("--------------")

def main():
    balance = 0
    isRunning = True

    while isRunning:
        print("**************")
        print("   VOID BANK  ")
        print("**************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option (1 - 4): ")

        match choice:
            case "1":
                showBalance(balance)
            case "2":
                balance += deposit()
                print("Successfully Deposited")
                print("Thank you, have a nice day!")
            case "3":
                balance -= withdraw(balance)
                print("Successfully Windrawn")
                print("Thank you, have a nice day!")
            case "4":
                isRunning = False
            case _:
                print("Invalid Input")

if __name__ == "__main__":
    main()