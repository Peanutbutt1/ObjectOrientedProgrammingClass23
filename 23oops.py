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
        self.std += 1
        self.age += 1
        print(f"New age is {self.age} and new class/standard is: {self.std}.")


class Annual_function:
    def __init__(self, name):
        self.name = name
        self.event = {
            "Veer Savarkar": [],
            "Bhagat Singh": [],
            "Nathuram Godse": [],
            "Mangal Pandey": [],
            "Subhash Chandra Bose": [],
            "Chandrashekhar Azad": []
        }

    def add_student(self, student, event_name):
        if event_name in self.event:
            self.event[event_name].append(student)
        else:
            print("Error: Event name does not exist.")

    def get_chart(self, event_name):
        if event_name in self.event:
            print(f"Students in Event - {event_name}:")
            for student in self.event[event_name]:
                print(student.name)
        else:
            print("Error: Event name does not exist.")


# Create Student objects
S1 = Student("S1", 1001, 16, 8)
S2 = Student("S2", 1002, 17, 8)
S3 = Student("S3", 1003, 17, 8)
S4 = Student("S4", 1004, 19, 9)
S5 = Student("S5", 1005, 17, 8)
S6 = Student("S6", 1006, 16, 8)
S7 = Student("S7", 1007, 18, 9)
S8 = Student("S8", 1008, 19, 8)
S9 = Student("S9", 1009, 16, 9)
S10 = Student("S10", 1010, 15, 8)
S11 = Student("S11", 1011, 17, 9)
S12 = Student("S12", 1012, 16, 9)

# Create Annual_function object
Function = Annual_function(2024)

# Add students to events
Function.add_student(S1, "Veer Savarkar")
Function.add_student(S2, "Veer Savarkar")
Function.add_student(S3, "Bhagat Singh")

# Get chart of students in an event
Function.get_chart("Veer Savarkar")
Function.get_chart("Bhagat Singh")



# creating an instance of the student class
#rakesh = Student("Rohan", 1005, 16, 8)

# calling the methods to print details
#rakesh.print_roll_no()
#rakesh.print_age()
#rakesh.class_passing()
#rakesh.class_passing()
#rakesh.class_passing()

# creating another instance of the student class
#prakash = Student("Ram Prakash", 1007, 18, 10)

# calling the methods to print details
#prakash.print_roll_no()
#prakash.print_age()
#prakash.class_passing()




            






















