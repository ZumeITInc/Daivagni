# merge two dictionaries
def Merge(dict1,dict2):
    result = {**dict1,**dict2}
    return result

# Driver code

dict1 = {'a':10,'b':20,'c':50}
dict2 = {'d':41,'e':74,'f':85}
dict3 = Merge(dict1,dict2)
print(dict3)

# merge two dictionaries in python
def Merge(dicti1,dicti2):
    return (dicti1.update(dict2))

# Driver code
dicti1 = {'s':10,'t':25,'o':65,'p':75}
dicti2 = {'s':75,'t':48,'a':15,'r':69}

# This returns None
print(Merge(dicti1,dicti2))

# changes made in dicti2
print(dicti2)