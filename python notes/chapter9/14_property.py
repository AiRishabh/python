# we use @property decorator on any method in the class to use the method as a property.

# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
#         self.percentage=str(( self.phy + self.chem + self.math)/3)+"%"

# s1=Student(98,78,88)
# print(s1.percentage)

# Note only for me : i copy paste code again for simplicity , i just dont want my code look messy. we have to change within the code itself.
"""suppose student phy mark mistakley type by 98 instead of 86"""
# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
#         self.percentage=str(( self.phy + self.chem + self.math)/3)+"%"
        
#     def againpercentage(self):
#         self.percentage=str(( self.phy + self.chem + self.math)/3)+"%"

# s1=Student(98,78,88)
# s1.phy=86
# print(s1.phy) #it will change the mark but not change the percentage.
# s1.againpercentage()
# print(s1.percentage)


# same thing we can do with help of property.

class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        
    @property
    def percentage(self):
        return str(( self.phy + self.chem + self.math)/3)+"%"
    
s1=Student(98,78,88)
s1.phy=86
print(s1.phy)
print(s1.percentage)