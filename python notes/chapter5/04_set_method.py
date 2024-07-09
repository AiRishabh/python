set={1,5,88,5,99,5,"rishabh"}

set.add(420)
print(set,type(set))


#remove(element)

my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  


#discard(element)
'''
Removes the specified element from the set if it is present.
 Does not raise an error if the element is not found.
'''
my_set1 = {1, 2, 3}
my_set1.discard(2)
print(my_set1)  


#clear()
#Removes all elements from the set.

my_set2 = {1, 2, 3}
my_set2.clear()
print(my_set2)  # Output: set()


#union(*others) or | operator

#Returns a new set with elements from the set and all others.

setA = {1, 2, 3}
setB = {3, 4, 5}
setC = setA.union(setB)
print(setC)  


#intersection(*others) or & operator:

setX = {1, 2, 3}
setY = {3, 4, 5}
setZ = setX.intersection(setY)
print(setZ)  



