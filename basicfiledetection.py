#Basic python file detection

import os

filePath = "C:/Users/jusxm/OneDrive/Pictures/Desktop/testonly"

if os.path.exists(filePath):
    print(f"The location of {filePath} exists")
    
    if os.path.isfile(filePath):
        print("This is a legit file")
    elif os.path.isdir(filePath):
        print('This is a legit folder/directory')
    else:
        print("This is not a file nor folder")
else:
    print(f"The location of {filePath} didn't exists")