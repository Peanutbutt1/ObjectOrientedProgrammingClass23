# 23.Object orientated programming in Python
# Introduction: As we have functions of different classes already in python, but we didn't see them as classes
# till now. Like: String, int, char, list, tuple, bool, etc.
# These classes have their own methods and attributes just like we are going to make in our declared classes.
# Syntax: To create an object we will use 'class' keyword, and then a variable name for our object class.
# Then within(indented) that object class we will define any number of methods which that object can perform

class Student:
    def __init__(self, formal_name, roll_no, age, class_):
        self.name = formal_name
        self.roll_no = roll_no
        self.age = age
        self.std = class_

    def print_roll_no(self):
        print(f"The student named {self.name} of class {self.std} has a roll no of {self.roll_no}.")

    def print_age(self):
        print(f"Student's age is {self.age}")

    def class_passing(self):
        self.std = self.std + 1
        self.age = self.age + 1
        print(f"New age is {self.age} and new class/standard is: {self.std}.")

# creating an instance of the student class
rakesh = Student("Rohan", 1005, 16, 8)

# calling the methods to print details
rakesh.print_roll_no()
rakesh.print_age()
rakesh.class_passing()
rakesh.class_passing()
rakesh.class_passing()

# creating another instance of the student class
prakash = Student("Ram Prakash", 1007, 18, 10)

# calling the methods to print details
prakash.print_roll_no()
prakash.print_age()
prakash.class_passing()





















