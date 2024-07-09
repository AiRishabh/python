''' 
                         *****INHERITANCE*****
When one class(child/derived) derives the properties & methods of another 
 class(parent/base).
 
'''

# INHERITANCE TYPE 1 (SINGLE INHERITANCE)

class Car: #SINGLE PARENT CLASS
    color="narangi"
    @staticmethod
    def start():
        print("car started....")

    @staticmethod
    def stop():
        print("car stopped")

#SINGLE CHILD CLASS
class ToyotaCar(Car): #we inherited the car property, if use car method in toyotacar class it will not give me error.
    def __init__(self,name):
        self.name=name

car1=ToyotaCar("fortuner")
print(car1.start())
print(car1.color)