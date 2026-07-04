import time
#Nested loop - loop inside of another loop

#for x in range(3):
    #for y in range(1, 11):
        #print(y, end="-")

rows = int(input("Enter rows: "))
columns = int(input("Enter columns: "))
symbol = input("Enter symbol: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
        time.sleep(1)
    print() 