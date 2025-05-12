# 10.Create a base class Employee with attributes name and salary. Derive two classes: Manager and Developer, where Manager has an additional attribute team_size and Developer has programming_language.

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name: ", self.name)
        print("Salary: ", self.salary)


class Manager(Employee):

    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def display(self):
        super().display()
        print("Team size: ", self.team_size)


class Developer(Employee):

    def __init__(self, name, salary, programming_lang):
        super().__init__(name, salary)
        self.programming_lang = programming_lang

    def display(self):
        super().display()
        print("Programming Language: ", self.programming_lang)

    
manager = Manager("Rohit", 15000, 10)
developer = Developer("Vedhit", 10000, "Python")

manager.display()
print()
developer.display()