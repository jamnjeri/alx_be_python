import math

class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        raise NotImplementedError("Subclasses should implement this method")

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        area = self.length * self.width
        return area 

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi * self.radius ** 2
        return area