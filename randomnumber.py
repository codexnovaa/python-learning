import random
#Simple number guessing game 

low_number = 1
high_number = 10
guesses = 0
is_running = True
answer = random.randint(low_number, high_number )
print(answer)

try:
    while is_running:
        guesses  += 1
        guess = int(input(f"Enter your guess between {low_number} - {high_number}: "))
        
        if guess > high_number or guess < low_number:
            print("You number is out of range.")
        elif guess > answer:
            print(f"{answer} is too high")
        elif guess < answer:
            print(f"{answer} is too low")
        else:
            print(f"Congrats! It only takes {guesses} guess to answer it right!"  if guesses == 0 else f"It takes {guesses} guesses to answer it right!")
            is_running = False
except ValueError as e:
    print(e)