# Methods are functions that belong to objects.

class Student:
    college_name= "whatsapp univeristy" 
    def __init__(self,name,marks): #constructor
        self.name=name 
        self.marks=marks 

    def Welcome(self): #creating methods
        print(f"welcome {self.name} ") 

    def Get_marks(self):
        print(f"your marks is {self.marks}") 

s1=Student("Rishabh",60) #creating objects

s1.Welcome()
s1.Get_marks()