'''
a=int(input("enter the number :"))
b=int(input("enter the number :"))
c=int(input("enter the number :"))

average=(a+b+c)/3

a=int(input("enter the number :"))
b=int(input("enter the number :"))
c=int(input("enter the number :"))

average=(a+b+c)/3'''

#to avoid this we have to create function.

#Function defination
def avg():
    a=int(input("enter the number :"))
    b=int(input("enter the number :"))
    c=int(input("enter the number :"))

    average=(a+b+c)/3
    print(average)


avg() #Function call.
avg()
