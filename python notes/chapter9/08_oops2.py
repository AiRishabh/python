#del keyword

class Student:
    def __init__(self,name):
        self.name=name

s1=Student("rishabh")
print(s1)
del s1
print(s1) #it will give me error



