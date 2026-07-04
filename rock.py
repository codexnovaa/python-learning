import random
#Rock, paper, scissor simple game

player_score = 0
computer_score = 0
computer_choices = ["rock", "paper", "scissor"]
is_running = True

def show_score():
        print("------SCORE BOARD------")
        print(f"PLAYER SCORE: {player_score:4}")
        print(f"COMPUTER SCORE: {computer_score:2}")         

while is_running:
    computer_choice = random.choice(computer_choices)
    player_choice = input("Enter your answer (rock, paper, scissor) --- (press q) to quit): ").lower()
    result = ""
    if player_choice == "q":
        show_score()
        is_running = False
        break
    
    if player_choice == computer_choice:
        print("It's A Tie!")
        continue
    
    if player_choice not in computer_choices:
        print("Invalid Input. Please choose only between (rock, paper, scissor)")
    else:
        match player_choice:
            case "rock":
                if computer_choice == "scissor":
                    player_score += 1
                    print("You win!")
                else:
                    computer_score += 1
                    print("You lose!")
            case "paper":
                if computer_choice == "rock":
                    player_score += 1
                    print("You win!")
                else:
                    computer_score += 1
                    print("You lose!")
            case "scissor":
                if computer_choice == "paper":
                    player_score += 1
                    print("You win!")
                else:
                    computer_score += 1
                    print("You lose!")
    
    print("_____CHOICE_____")
    print(f"PLAYER: {player_choice}")
    print(f"COMPUTER: {computer_choice}")

