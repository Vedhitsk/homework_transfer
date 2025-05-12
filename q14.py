# 14.Create a function calculate_total_price() that takes different objects (Laptop, Mobile, Tablet) and calls their method get_price() to calculate the total price dynamically.

class Product:

    def get_price(self):
        pass  


class Laptop(Product):

    def __init__(self, price):
        self.price = price

    def get_price(self):
        return self.price


class Mobile(Product):

    def __init__(self, price):
        self.price = price

    def get_price(self):
        return self.price


class Tablet(Product):

    def __init__(self, price):
        self.price = price

    def get_price(self):
        return self.price
    

def calculate_total_price(items):
    total = sum(item.get_price() for item in items)
    return total

laptop = Laptop(800)
mobile = Mobile(500)
tablet = Tablet(300)

items = [laptop, mobile, tablet]
total_price = calculate_total_price(items)

print("Total Price:", total_price)