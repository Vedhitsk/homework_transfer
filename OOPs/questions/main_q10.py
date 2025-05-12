import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from entity.employee import Employee
from entity.manager import Manager
from entity.developer import Developer

if __name__ == "__main__":

    emp1 = Employee("Vedhit", 50000)
    emp2 = Manager("Rohit", 70000, 12)
    emp3 = Developer("Naman", 90000, "python")

    emp1.display()
    emp2.display()
    emp3.display()
