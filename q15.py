# 15.Create a class Person with a method introduce(). Override it in subclasses Teacher and Student to print different introductions.

class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello, I am", self.name)


class Teacher(Person):

    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def introduce(self):
        print("Hello, I am", self.name, "and I teach", self.subject)


class Student(Person):

    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def introduce(self):
        print("Hello, I am", self.name, "and I study in grade", self.grade)


teacher = Teacher("Mr. Ashok", "SQL")
student = Student("Vedhit", "12th")

teacher.introduce()
student.introduce()