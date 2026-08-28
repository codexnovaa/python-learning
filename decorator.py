# Function that extends the behavior of another function without modifying the base function


def addSprinkles(func):
    def wrapper(*args, **kwargs):
        print("Added Srinkles")
        func(*args, **kwargs)
    return wrapper

def addFudge(func):
    def wrapper(*args, **kwargs):
        print("Added Fudge")
        func(*args, **kwargs)
    return wrapper

@addSprinkles
@addFudge
def getIceCream(flavor):
    print(f"Heres your {flavor} ice cream")
    
getIceCream("vanilla")