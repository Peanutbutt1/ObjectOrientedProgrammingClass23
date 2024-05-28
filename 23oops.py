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

# Now if we make another class we can make them interact with each other 
# Lets make a function where different dance festivals are organised and students can take part in them.
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
    
    def add_student(self, name, Event_name):
        count = 0
        while(count < 2):
            if name in self.name and Event_name in self.event:
                self.event[Event_name].appent(name)
            elif ((name in self.name and Event_name in self.event) == 1):
                print("No name matched pls try again.")
                count += 1
            else:
                print("Error (too much wrong names)")
                return 1
    
    def get_chart(self, event_name):
        for student in self.event["Veer Savarkar"]:
            






















