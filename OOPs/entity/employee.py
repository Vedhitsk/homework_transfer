class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def display(self):
        print(f"Name: {self.name}\nSalary: {self.__salary}")

    