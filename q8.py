# 8.Create a class Laptop with private attributes brand and price. Provide getter and setter methods to access and modify these attributes.

class Laptop:

    def __init__(self, brand, price):
        self.__brand = brand
        self.__price = price

    def get_brand(self):
        return self.__brand
    
    def set_brand(self, brand):
        self.__brand = brand

    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Price must be positive value.")
    
    def display(self):
        print("Laptop Brand: ",self.__brand)
        print("Price: ",self.__price)

user1 = Laptop("Dell",50000)
user1.display()

print(user1.get_brand())
print(user1.get_price())

user1.set_brand("Asus")
user1.set_price(89000)
user1.display()
