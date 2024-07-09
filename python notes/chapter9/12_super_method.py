# supe() method decorator is used to access methods of the parent class.

class Car:
    
    def __init__(self,type):
        self.type=type


    @staticmethod
    def start():
        print("car started....")

    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car): 
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
        

car1=ToyotaCar("prius","electric")
print(car1.name)
print(car1.type)
"""In ToyotaCar constructor we doesnt defined a type but it is define
in class constructor even though it will give me error-----> 'ToyotaCar' object has no attribute 'type' 
let's give type in ToyotaCar's constructor. if i write in self.type=type that means it is created attribute inside 
the toyotacar, but i want from the car's constructor(parent class).

to access the car's constructor we have to use super() method."""
