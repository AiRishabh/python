#Write a program to find the greatest of four numbers entered by the user.

a1=int(input("Enter the number : "))

a2=int(input("Enter the number : "))

a3=int(input("Enter the number : "))

a4=int(input("Enter the number : "))

if(a1>a2 and a1>a3 and a1>a4):
    print("a1 is greator than a2,a3,a4 :",a1)

elif(a2>a1 and a2>a3 and a2>a4):
    print("a2 is greator than a1,a3,a4 :",a2)

elif(a3>a1 and 3>a2 and a3>a4):
    print("a2 is greator than a1,a3,a4 :",a3)

elif(a4>a1 and a4>a2 and a4>a3):
    print("a4 is greator than a1,a2,a3 :",a4)