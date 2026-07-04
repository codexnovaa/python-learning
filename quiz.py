# Simple Quiz

questions = (   "What planet is known as the Red Planet?",
                "What gas do plants absorb from the atmosphere?",
                "What part of the body pumps blood?",
                "What is the boiling point of water?",
                "What force keeps us on the ground?")
options = (
    ("A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"),
    ("A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"),
    ("A. Brain", "B. Lungs", "C. Heart", "D. Liver"),
    ("A. 50°C", "B. 75°C", "C. 100°C", "D. 150°C"),
    ("A. Magnetism", "B. Gravity", "C. Friction", "D. Electricity")
)
answers = ("B", "C", "C", "C", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input(f"Choose the correct answer (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
            print("Your answer is correct!")
            score += 1
    else:
            print("Your answer is incorrect!")
            print(f"{answers[question_num]} is the correct answer.")
    
    question_num += 1

print("----------------")
print("   FINAL RESULT   ")
print("----------------")

print("Answer keys: ", end="")
for answer in answers:
    print(answer, end="")
print()

print("Guesses:", end="")
for guess in guesses:
    print(guess, end="")
print()

score = int(score / len(questions) * 100)
print(f"Your score in percentage: {score}%")


        