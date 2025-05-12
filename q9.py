# 9.Create a class Animal with a method make_sound(). Derive subclasses Dog and Cat from it, and override make_sound() to print respective sounds.

class Animal:

    def make_sound(self):
        print("Default sound")


class Dog(Animal):

    def make_sound(self):
        print("Woof!")


class Cat(Animal):

    def make_sound(self):
        print("Meow!")


animal = Animal()
dog = Dog()
cat = Cat()

animal.make_sound()
dog.make_sound()
cat.make_sound()