# 17.Create an abstract class Appliance with an abstract method turn_on(). Implement subclasses WashingMachine and Refrigerator with specific functionality.

from abc import ABC, abstractmethod

class Appliance(ABC):

    @abstractmethod
    def turn_on(self):
        pass


class WashingMachine(Appliance):

    def turn_on(self):
        print("Washing Machine is now ON. Starting wash cycle..")

    
class Refrigerator(Appliance):

    def turn_on(self):
        print("Refrigerator is now ON. Cooling system activated..")


washing_machine = WashingMachine()
refrigerator = Refrigerator()

washing_machine.turn_on()
refrigerator.turn_on()