# Basic Class and Object Concepts
# --------------------------------------------
# 3.Create a class Car with attributes brand, model, and year. Instantiate an object of this class and print its details.

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_details(self):
        print(f"Car Details: {self.brand} {self.model} {self.brand}")

car_details = Car("Toyota", "GR8", 2019)

car_details.display_details()
