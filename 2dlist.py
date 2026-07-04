# 2 Dimensional List

#fruits = ["apple", "banana", "orange"]
#vegetable = ["celery", "carrots", "potatoes"]
#meats = ["chicken", "fish", "turkey"]


#fruits = ["apple", "banana", "orange"]
#vegetable = ["celery", "carrots", "potatoes"]
#meats = ["chicken", "fish", "turkey"]

#print(groceries[0][0].capitalize())

#groceries = [["apple", "banana", "orange"], 
            #["celery", "carrots", "potatoes"], 
            #["chicken", "fish", "turkey"]]

#for category in groceries:
    #for food in category:
        #print(food, end=" ")
    #print()
    
num_pad =   ((1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

