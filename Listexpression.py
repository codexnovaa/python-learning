#List comprehension - concise way to create list in python


#double = [num * 2 for num in range(1, 11)]
#triple = [num * 3 for num in range(1, 11)]
#print(double)
#print(triple)

#numbers = [1, -5, 3, -6, -9, 7, 10, 2, 8, 14, 20]
#positiveNums = [num for num in numbers if num >= 0]
#negativeNums = [num for num in numbers if num < 0]
#print(positiveNums)
#print(negativeNums)

#evenNums = [num for num in numbers if num % 2 == 0]
#oddNums = [num for num in numbers if num % 2 != 0]
#print(evenNums)
#print(oddNums)

grades = [75, 74, 72, 80, 95, 92, 87, 89, 97]
passingGrades = [grade for grade in grades if grade >= 75]
failedGrades = [grade for grade in grades if grade < 75]
print(passingGrades)
print(failedGrades)
