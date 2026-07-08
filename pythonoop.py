#Simple python oop

class Car:
    def __init__(self, model, year, color, forSale):
        self.model = model
        self.year = year
        self.color = color
        self.forSale = forSale
        
    def driving(self):
        print(f"You are driving a {self.model} car")
    
    def start(self):
        print(f"You start the {self.model} car")
        
    def stop(self):
        print(f"You stop the {self.model} car")
        
car1 = Car("Ferrari", 2026, "Red", False)
car1.driving()