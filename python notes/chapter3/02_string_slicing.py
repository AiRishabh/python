#A string in python can be sliced for getting a part of the strings.
name="Rishabh" #0123456 start with 0 and negative string -7 -6 -5 -4 -3 -2 -1 start with -1
#note----------> String is immutable.(can not be replace)
print(len(name))

'''The index in a string starts from 0 to (length -1) in Python. In order to slice a string, 
we use the following syntax:'''

# xyz=name[index_start_included:index_last_excluded]
character1=name[1]
print(character1)
print(name[0:5])
print(name[1:3])

