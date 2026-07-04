# Arbitrary arguments
# *args - allows you to pass multiple non-key arguments
# **kwargs allows you to pass multiple keyword arguments * unpacking order

#def add(*nums):
#    sum = 0
#    for num in nums:
#        sum += num
#    return sum
#
#total = add(1,2,3,4,5)
#print(total)

#def displayName(*args):
#    for arg in args:
#        print(arg, end=" ")
#
#displayName("Void", "Tzyu", "Nova")

#def printAddress(**kwargs):
#    for key, value in kwargs.items():
#        print(f"{key}: {value}")
#
#print(printAddress( street="123 Fake St.", 
#                    city="Uknown Galaxy", 
#                    zip="9999"))

def shippingLabel(*names, **details):
    print("Reciever: ", end=" ")
    for name in names:
        print(name, end=" ")
        
    print()
    
    print("------Details------")
    for key, value in details.items():
        print(f"{key}: {value}")

shippingLabel( "Dr.", "Voidsu", "Vyz", "I",
                street="777 Universal St.",
                city="Neptune City",
                address="Nepturtical 9999",
                zip="1111")
