#Iterable object/collection that can return its elements one at a time, 
#allowing it to be iterated over in a loop


myDictionary = {
    "A": 1,
    "B": 2,
    "C": 3
}

for key, val in myDictionary.items():
    print(key, val)