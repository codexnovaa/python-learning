#Python reading files (.txt, .json, csv)
import json
import csv

try:
    filepath = "C:/Users/jusxm/OneDrive/Pictures/Desktop/test2.csv"

    with open(filepath, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[2])
except FileNotFoundError as error:
    print("File didn't exist. Please check carefully.")
except PermissionError as error:
    print("This file don't allow accesss.")