import random
#Simple dice game
#● ┌ ─ ┐ │ └ ┘

dice_art = {
    1: ("┌──────────┐",
        "│          │",
        "│     ●    │",
        "│          │",
        "└──────────┘"),
    
    2: ("┌──────────┐",
        "│ ●        │",
        "│          │",
        "│       ●  │",
        "└──────────┘"),
    
    3: ("┌──────────┐",
        "│        ● │",
        "│     ●    │",
        "│  ●       │",
        "└──────────┘"),
        
    4: ("┌──────────┐",
        "│ ●      ● │",
        "│          │",
        "│ ●      ● │",
        "└──────────┘"),
            
    5: ("┌──────────┐",
        "│ ●      ● │",
        "│     ●    │",
        "│ ●      ● │",
        "└──────────┘"),
    
    6: ("┌──────────┐",
        "│  ●    ●  │",
        "│  ●    ●  │",
        "│  ●    ●  │",
        "└──────────┘"),
}

dice = []
total = 0

dice_input = int(input("Enter the dice number: "))

for input in range(dice_input):
    dice.append(random.randint(1, 6))
    
#for die in range(dice_input):
    #for lineArt in dice_art.get(dice[die]):
        #print(lineArt)
        
for lineArt in range(5):
    for die in dice:
        print(dice_art.get(die)[lineArt], end="")
    print()

for die in range(dice_input):
    total += dice[die]

print(f"Total dice value: {total}")



