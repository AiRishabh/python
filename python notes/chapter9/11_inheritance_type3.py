class A: #parent class
    varA="welcome to class A"

class B: #parent class
    varB="welcome to class B"

class C(A,B): #child class
    varC="welcome to class C"

a=C()
print(C.varA)
print(C.varB)
print(C.varC)