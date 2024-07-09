# A class method decorator is bound to the class & receives the class as an implicit first argument.

# Note: static method can't access or modify class state and generally for utility.

#staric method does not change class attributes but class method does.

#lets change the class attributes 

# class person:
#     name="something"

#     def changename(self,name):
#         self.name=name

# p1=person()
# p1.changename("rishabh")

# print(p1.name)
# print(person.name) #it will not change the class attribute b/c our def changename function creating new attribute for itself.

#there are direct and indirect way to change the class attribute.

# 1) person.name (indirectly changing)

# class person:
#     name="something"

#     def changename(self,name):
#         person.name=name

# p1=person()
# p1.changename("rishabh")

# print(p1.name)
# print(person.name)


#2) class method (directly change the class attributes)

class person:
    name="something"

    @classmethod
    def changename(cls,name): #cls reffering to class (we can write inplace of cls but it reffer to the class)
        cls.name=name 
        
p1=person()
p1.changename("india")

print(p1.name)
print(person.name)