# 18.Create an abstract class Animal with an abstract method move(). Implement Bird and Fish subclasses with their movement styles.

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def move(self):
        pass  


class Bird(Animal):

    def move(self):
        print("The bird flies in the sky.")


class Fish(Animal):

    def move(self):
        print("The fish swims in the water.")


sparrow = Bird()
goldfish = Fish()

sparrow.move()
goldfish.move()
