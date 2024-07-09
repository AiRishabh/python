'''self.something is an instnace attribute it will be different for different objects.
it will occupies memory space for each object '''


'''for example we have 4 student but they belong to same college therefore we dont need 
specify them by different object because it will occupies memory for same object that why 
we will create class for same college name this occupies one space in memory for different 
objects this is called as attributes'''


class Student:
    college_name= "whatsapp univeristy" #class attribute,it will store in memory in 1 time because it is common for objects.
    def __init__(self,name,marks): 
        self.name=name #instance attributes , it will take multiple memory space because name, marks ,city etc will be different
        self.marks=marks #instance attributes

a=Student("rishabh",60)
print(a.name,a.marks,a.college_name)

b=Student("rohit",80)
print(b.name,b.marks,b.college_name)