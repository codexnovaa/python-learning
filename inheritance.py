#Class inheritance -- allows a class to inherit attributes and methods from another class
                    # helps with code  reusability and extensibility

class Animal:
    def __init__(self, name):
        self.name = name
        self.isAlive = True
        
    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name} is sleeping")
        
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing")

class Bird(Animal):
    def chirp(self):
        print(f"{self.name} is chirping")

dog1 = Dog("Chocomuchumilonica")
cat1 = Cat("Orange jijusuu")
bird1 = Bird("Bruno")

dog1.bark()
cat1.meow()
bird1.chirp()


