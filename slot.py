#Simple Slot game
import random
import time

def spinRow():
    symbols = ["🍋","⭐","🔔","🍒","🍉"]

    result = [random.choice(symbols) for symbol in range(3)]
    return result

def printRow(row):
    print(" ".join(row))

def getPayout(row, bet):
    if row[0] == row[1] == row[2]:
        match row[0]:
            case "🍋":
                return bet * 3
            case "⭐":
                return bet * 4
            case "🔔":
                return bet * 5
            case "🍒":
                return bet * 10
            case "🍉":
                return bet * 20        
    else:
        return 0
def main():
    balance = 100
    
    print("---------------------")
    print("VOID Slot Machine")
    print("Symbols: 🍋,⭐,🔔,🍒,🍉")
    print("---------------------")

    while balance > 0:
        try:
            print(f"Current Balance: ₱{balance:,.2f}")
            bet = input("Place your bet amount | press (q) to quit): ")
            if bet == "q":
                break
            else:
                bet = int(bet)
                if bet <= 0:
                    print("Please enter a valid amount")
                    continue
                elif bet > balance:
                    print("Insufficient Balance.")
                    continue            
            
            balance -= bet

            row = spinRow()
            print("Spinning....")
            time.sleep(2)
            printRow(row)
            
            payout = getPayout(row, bet)
            if payout > 0:
                print(f"You won ₱{payout}")
            else:
                print(f"You lose ₱{bet}")
                
            balance += payout
            
        except ValueError as e:
            print(f"{e}. Please enter a valid input.")
            
if __name__ == "__main__":
    main()