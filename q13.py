# 13.Modify the Shape class hierarchy to include a display() method that prints shape details. Override this method in Circle and Square.

import math

class Shape:

    def area(self):
        pass

    def display(self):
        print("This is a Shape.")


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def display(self):
        print("Shape: Circle, Radius:", self.radius, "Area:", round(self.area(),3))


class Sqaure(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
    
    def display(self):
        print("Shape: Sqaure, Side:", self.side, "Area:", round(self.area(),3))

    
circle = Circle(4)
square = Sqaure(6)

circle.display()
square.display()