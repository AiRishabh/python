'''  ***** private (like) attributes and methods. *****

Private attributes & methods are meant to be used only within the class 
and are not accessible from outside the class.

'''
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.acc_pass=acc_pass

a1=Account(123456,9858964)
print(a1.acc_no)
print(a1.acc_pass)

'''since the password is publically available so we to make it private for that we have to
give two underscore like this __acc_pass'''

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass

a1=Account(123456,9858964)
print(a1.acc_no)
print(a1.__acc_pass) #it will give error that 'Account' object has no attribute '__acc_pass'.