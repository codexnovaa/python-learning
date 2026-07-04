import time
#Default arguments -- default value for certain parameters


#def netPrice(listPrice, discount = 0, tax = 0.05):
#    return listPrice * (1 - discount) * (1 + tax)

#print(netPrice(500, 0.05))

def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("TIMES UP!")

count(20)
