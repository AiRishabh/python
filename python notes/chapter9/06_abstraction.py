''' Hiding the implementation details of a class and only showing the essential 
features to the user.'''

class car:
    def __init__ (self):
        self.acc=False
        self.brk=False
        self.clutch=False
    
    def start(self):
        self.clutch=True
        self.acc=True
        print("car is started....")

o1=car()
o1.start() # abstraction--> its hide the behind the code.