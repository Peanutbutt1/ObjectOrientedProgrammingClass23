# 23.Object orientated programming in Python (Part 1)ss
# Introduction: As we have functions of different classes already in python, but we didn't see them as classes -
# till now. Like: String, int, char, list, tuple, bool, etc.
# Class provide a rather organised and easy to handle code.
# These classes have their own methods and attributes just like we are going to make in our declared classes.
# Syntax: To create an object we will use 'class' keyword, and then a variable name for our object class.
# Then within(indented) that object class we will define any number of methods which that object can perform

class Student:
    def __init__(self, formal_name, roll_no, age, class_):
        self.name = formal_name
        self.roll_no = roll_no
        self.age = age
        self.class_ = class_

    def details(self):
        print(f"Hi! there this is student {self.name}, roll no- {self.roll_no}, age {self.age} and class {self.class_}")

    def passing(self):
        self.age += 1
        self.class_ += 1

    def __del__(self):
        pass

    def sp_details(self, det):
        if det == "name":
            print(self.name)
        elif det == "age":
            print(self.age)
        elif det == "roll_no":
            print(self.roll_no)
        elif det == "class_":
            print(self.class_)


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

    def add_student(self, S, event_name):
        if event_name in self.event:
            self.event[event_name].append(S)
        else:
            print("Error! event name doesn't exist.")

    def get_chart(self, event_name):
        if event_name in self.event:
            print(f"Students in event {event_name}: ")
            for S in self.event[event_name]:
                print(S.name + ", Whose class is ", end='')
                S.sp_details("class_")
        else:
            print("Event doesn't exist.")


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

S1.details()
S2.details()
S5.details()
S1.passing()
S1.passing()
S1.passing()
S1.passing()
print("After passing new details: ")
S1.details()
S1.details()
del S7

Function = Annual_function(2024)

Function.add_student(S1, "Veer Savarkar")
Function.add_student(S2, "Veer Savarkar")
Function.add_student(S3, "Bhagat Singh")
Function.add_student(S6, "Mangal Pandey")
Function.add_student(S5, "Bhagat Singh")
Function.add_student(S9, "Bhagat Singh")
Function.add_student(S8, "Mangal Pandey")
Function.add_student(S10, "Veer Savarkar")


Function.get_chart("Veer Savarkar")
Function.get_chart("Bhagat Singh")
Function.get_chart("Mangal Pandey")




            






















