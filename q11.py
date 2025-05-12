# 11.Create a class Shape with a method area(). Inherit Circle and Square classes from Shape and implement their respective area calculations.

import math

class Shape:

    def area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    

class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
    

circle = Circle(4)
square = Square(6)

print("Area of Circle: ", round(circle.area(),3))
print("Area of Square: ", square.area())