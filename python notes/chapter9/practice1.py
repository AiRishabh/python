'''Create student class that takes name & marks of 3 subjects as arguments in constructor.
Then create a method to print the average.'''

class Student:
    def __init__ (self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print(f"hi , {self.name}, your avg score is {sum/3}")

s1=Student("Rishabh",[75,65,80])
s1.get_avg()

#lets change the name.
s1.name="rohit"
s1.get_avg()