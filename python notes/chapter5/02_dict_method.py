marks={
    "rishabh":60,
    "rohit":80,
    "manthan":72,
    "fruit":"banana"
    
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"rishabh":90,"riya":100}) #dict is mutable, it affect the original dict.we can add new key:values t the same time.
# print(marks)

'''IMP'''

print(marks.get("manthan"))
print(marks["manthan"])

print(marks.get("santosh"))
print(marks["santosh"])

'''
both give same output but what is the difference b/w them
when we use xyz.get() it gives none if key:value not present in dict.
when we use xyz[] it gives error if if key:value not present in dict.

'''
# print(marks.get("manthan2"))
# print(marks["manthan2"])