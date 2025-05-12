# 5.Create a class Student with attributes name, roll_number, and marks. Define a method to display the student's details. Instantiate the class and print the details of a student.

class Student:

    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display(self):
        print("\nStudent Details")
        print("Student Name: ", self.name)
        print("Roll Number: ", self.roll_number)
        print("Marks: ", self.marks)

stud = Student("Rahul", 123478, 89)
stud.display()
        