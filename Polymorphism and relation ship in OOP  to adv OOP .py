"""Creating of a class"""
class Student:
    def __init__(self, name, Grade):
        self.name = name #Attributes
        self.Grade = Grade #Attributes

    def Study(self, hours):
        return(f"{self.name} studies this many {hours}"):
s1 = Student("Bilal" , "A")
s2 = Student("Zainab" , "A*")
"""Step 2: Encapsulation (Data Hiding & Controlled Access)"""
class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner #Attributes
        self.balance = balance #Attributes
        
