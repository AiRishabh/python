# __init__ Function (constructor)

class Example:
    def __init__ (self): #default constructor, if we could not make it then python automatically made this constructor.
         pass
         '''its take self parameter, also it can take multiple parameter. 
         instead of self we can take any word but in case of simplicity we take self.'''
        

q1=Example() #parantheses use in this, is used for contructor to call.



#parameterized contructor
class Student:
    name="rishabh"
    def __init__(self,name): #its take self parameter, also it can take multiple parameter. instead of self we can take any word but in case of simplicity we take self.
        self.name=name
        

s1=Student("rockstar") #parantheses use in this, is used for contructor to call.
print(s1.name)

s2=Student("Rishabh")
print(s2.name)


class Stu:
    def __init__ (self,name,marks):
        self.name=name
        self.marks=marks

w1=Stu("rishabh",60)
print(w1.name,w1.marks)


w2=Stu("rohit",80)
print(w2.name,w2.marks)
