#Simple hangman game

import random

words = ["apple", "orange", "banana", "pineapple", "coconut"]

hangmanArt = {
    0: ("     ", 
        "     ", 
        "     "),
    
    1: ("  O  ", 
        "     ", 
        "     "),
    
    2: ("  O  ", 
        "  |  ", 
        "     "),
    
    3: ("  O  ", 
        " /|  ", 
        "     "),
        
    4: ("  O  ", 
        " /|\\", 
        "     "),
            
    5: ("  O  ", 
        " /|\\", 
        " /   "),
                
    6: ("  O   ", 
        " /|\\ ", 
        " / \\ "),
}


def displayMan(wrongGuesses):
    for line in hangmanArt[wrongGuesses]:
        print(line)

def displayHint(hint):
    print(" ".join(hint))

def displayAnswer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrongGuesses = 0
    guessedLetters = set()
    isRunning = True
    
    while isRunning:
        displayMan(wrongGuesses)
        displayHint(hint)
        guess = input("Please enter a guess letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input.")
        else:
            if guess in guessedLetters:
                print(f"{guess} is already guessed.")
                continue
            
            guessedLetters.add(guess)
            
            if guess in answer:
                for i in range(len(answer)):
                    if answer[i] == guess:
                        hint[i] = guess
            else: 
                wrongGuesses += 1
            
            if "_" not in hint:
                print("YOU WIN!")
                print("-------------------------")
                print("SUMMARY OF GUESSES")
                print(f"Guessed Letters: {" ".join(guessedLetters)}")
                print("")
                print("ANSWER")
                displayAnswer(answer)
                print("-------------------------")
                isRunning = False
            elif wrongGuesses >= len(hangmanArt) - 1:
                print("YOU LOSE!")
                print("-------------------------")
                print("SUMMARY OF GUESSES")
                print(f"Guessed Letters: {" ".join(guessedLetters)}")
                print("")
                print("ANSWER")
                displayAnswer(answer)
                print("-------------------------")
                isRunning = False
                
if __name__ == "__main__":
    main()