# Static method - method that belong to a class rather than any object
# from that class (instance)

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def getInfo(self):
        return f"Name: {self.name} | Position: {self.position}"
    
    @staticmethod
    def isVaildPosition(position):
        validPositions = ["Manager", "Cook", "Waiter", "Janitor"]
        return "Valid Position" if position in validPositions else "Invalid Position"
    
#emp1 = Employee("Void", "Manager")
#print(emp1.getInfo())

print(Employee.isVaildPosition("Manager"))