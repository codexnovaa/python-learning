# Collection - single variable use to store multiple values
# List[] - ordered and changable duplicates are okay!

#                   ----LIST----

#fruits = ["apple", "banana", "banana", "banana", "orange", "grapes"]
#print(fruits)
#print(fruits[0])
#print(len(fruits))
#print("apple" in fruits) -- return boolean value
#print(fruits)

#fruits[0] = "grapes"
#fruits.append("pineapple")
#fruits.insert(1, "grapes")
#fruits.remove("apple")
#fruits.pop()
#fruits.sort()
#fruits.reverse()
#fruits.clear()
#print(fruits.index("banana"))
#print(fruits.count("orange"))
    
#for fruit in fruits:
    #print(fruit, end=" ")

#                   ----SET-----

#fruits = {"apple", "banana", "orange", "grapes", "coconut"}

#print(len(fruits))
#fruits.add("pineapple")
#fruits.remove("banana")
#fruits.pop()
#fruits.clear()
#print(fruits)

#                   ----TUPLE----\

fruits = ("apple", "banana", "orange", "orange", "grapes", "coconut")

print(len(fruits))
print("apple" in fruits)
print(fruits.index("orange"))
print(fruits.count("orange"))

for fruit in fruits:
    print(fruit, end=" ")
