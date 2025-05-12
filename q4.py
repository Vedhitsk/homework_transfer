# 4.Write a class Rectangle that takes length and breadth as parameters. Create a method to calculate the area of the rectangle. Instantiate two rectangles and compare their areas.

class Rectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth
        
r1 = Rectangle(30, 20)
r2 = Rectangle(10, 5)

if r1.area() > r2.area():
    print("First Rectangle have Large area.")
else:
    print("Second Rectangle have Large area.")
