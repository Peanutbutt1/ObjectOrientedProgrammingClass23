# Inheritence - Lower level classes can inherit methods from upper level class.
# So we will see how we can make classes work together and share methods b\w them
# Lets say we have two similar functioning class objects like- a Subject teacher and a Class teacher

class Class_teacher:
    def __init__(self, name, sub):
        self.name = name
        self.sub = sub

    def ptasks(self):
        print(f"This is the class teacher {self.name} and he takes attendence, teaches and checks diary.")
        
class Subject_teacher:
    def __init__(self, name, sub):
        self.name = name
        self.sub = sub
        
    def ptasks(self):
        print(f"This is the subject teacher {self.name} and he teaches. ")
        
# As you can see in this code above here are two objects doing the same things so what we can do is-

class Teacher:
    def __init__(self, name, sub):
        self.name = name
        self.sub = sub
        
    def ptasks(self):
        print(f"This is the teaher {self.name} about who we don't know much about.")
        
class Class_teacher(Teacher):#we can now give lower level classes, methods of upper level class

    def ptasks(self):
        print(f"This is the class teacher {self.name} and he takes attendence, teaches and checks diary.")
        
class Subject_teacher(Teacher):#same here.(ln 28)
        
    def ptasks(self):
        print(f"This is the subject teacher {self.name} and he teaches. ")
        
# Now if a class doesn't have the attribute we asked it will take it from upper level class
class Subst(Teacher):
    pass

# Now if a class have some more or different attributes from parent of upper class-
class Principle(Teacher):
    def __init__(self, name, sub, office):
        #we should't do self.name = name b\c it can do sth right if we have a big and 
        # multiple shared work or a project b\c maybe upper level class is accessing some database so doing
        # it again will cause disturbance. So we do it like-
        super().__init__(name, sub)
        self.office = office 

    def ptasks(self):
        print(f"This is the principle {self.name} he doesn't teach any subjects but he works on office {self.office}.")
        



















