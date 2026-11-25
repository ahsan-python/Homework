"""Creating of a class"""
class Student:
    def __init__(self, name, Grade):
        self.name = name #Attributes
        self.Grade = Grade #Attributes

    def Study(self, hours):
        return(f"{self.name} studies this many {hours}"):
s1 = Student("Bilal" , "A")
s2 = Student("Zainab" , "A*")
