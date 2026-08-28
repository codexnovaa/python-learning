# super() - function used in a child class to call methods from parent class (superclass)

class shape:
    def __init__(self, color, isFilled):
        self.color = color
        self.isFilled = isFilled
        
    def description(self):
        print(f"It is color {self.color} and it is {"filled" if self.isFilled else "not filled"}")

class circle(shape):
    def __init__(self, color, isFilled, radius):
        super().__init__(color, isFilled)
        self.radius = radius

    def describe(self):
        print(f"This cirle has an area of {3.14 * self.radius * self.radius}cm^2")
        super().description()

class triangle(shape):
    def __init__(self, color, isFilled, width, height):
        super().__init__(color, isFilled)
        self.width = width
        self.height = height

class square(shape):
    def __init__(self, color, isFilled, width):
        super().__init__(color, isFilled)
        self.width = width
        
        
circle1 = circle("white", True, 20)
print(circle1.color)
print(circle1.isFilled)
print(circle1.radius)
circle1.describe()