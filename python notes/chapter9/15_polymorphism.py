"""
print(1+2) output-->3
print("rishabh"+"deshpande") output--> (concatenate) rishabhdeshpande
print([1,2,3]+[4,5,6]) output---> (merge) [1,2,3,4,5,6]

conclusion--->
when we adding numerical value by using operator + its add the value.
when we adding strings it get concatenate but not added.
when we adding lists it get merge not added.
that means + operator do different(meaning of + changes) operation according to there data type,this is
we called as operatpr overloading and it is type of polymorphism.
"""


# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img

#     def shownumber(self):
#         print(f"{self.real} i + {self.img} j ")

#     def add(self,num2):
#         newreal=self.real+num2.real
#         newimg=self.img+num2.img
#         return Complex(newreal,newimg)

# num1=Complex(1,3)
# num1.shownumber()

# num2=Complex(2,6)
# num2.shownumber()

# num3=num1.add(num2)
# num3.shownumber()

#lets add this complex number for this we have to create logic. 
#if we do not want to call function, then we have to use dunder function.
#for addition __add__

class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def shownumber(self):
        print(f"{self.real} i + {self.img} j ")

    def __add__(self,num2):
        newreal=self.real+num2.real
        newimg=self.img+num2.img
        return Complex(newreal,newimg)

num1=Complex(1,3)
num1.shownumber()

num2=Complex(2,6)
num2.shownumber()

num3=num1+num2
num3.shownumber()



#for subtraction.

class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def shownumber(self):
        print(f"{self.real} i + {self.img} j ")

    def __sub__(self,num2):
        newreal=self.real-num2.real
        newimg=self.img-num2.img
        return Complex(newreal,newimg)

num1=Complex(1,3)
num1.shownumber()

num2=Complex(2,6)
num2.shownumber()

num3=num1-num2
num3.shownumber()