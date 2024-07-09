# MULTI-LEVEL INHERITANCE

class Car:
    color="narangi"
    @staticmethod
    def start():
        print("car started....")

    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car): 
    def __init__(self,brand):
        self.brand=brand

class fortuner(ToyotaCar):
    def __init__(self,type):
        self.type=type

car1=fortuner("diesel")
print(car1.type)
car1.start()