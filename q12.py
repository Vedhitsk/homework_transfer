# 12.Create a class Vehicle with attributes brand and speed. Derive Car and Bike classes from it and add specific attributes and methods to each.

class Vehicle:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def display(self):
        print("Brand:", self.brand)
        print(f"Speed: {self.speed}km/h")


class Car(Vehicle):

    def __init__(self, brand, speed, num_seats):
        super().__init__(brand, speed)
        self.num_seats = num_seats

    def display(self):
        super().display()
        print("Seater:", self.num_seats)


class Bike(Vehicle):

    def __init__(self, brand, speed, bike_type):
        super().__init__(brand, speed)
        self.bike_type = bike_type

    def display(self):
        super().display()
        print("Bike Type:", self.bike_type)


car = Car("Toyota", 350, 2)
bike = Bike("Suzuki", 250, "Sports")

car.display()
print()
bike.display()