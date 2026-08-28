import json
import csv
#Python writing files (.txt, .json, .csv)

#txtData = "hello!"
#employees = ["SpongeBob", "Squidward", "Void", "Galaxy"]
#employee = {
#    "name": "Void",
#    "age": 27,
#    "job": "Engineer"
#}

employees = [["Name", "Age", "Job"], 
             ["Spongebob", 18, "Engineer"],
             ["Galaxy", 19, "Mechanic"],
             ["Void", 18, "Scientist"]]
filePath = "C:/Users/jusxm/OneDrive/Pictures/Desktop/test2.csv"

try:
    with open(file=filePath, mode="w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"json file {filePath} was created.")
except FileExistsError:
    print("This file already exist!")