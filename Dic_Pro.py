# Difininig Dictionary

d2 = {"idno":101,"name":"sri","marks":[65,35,75,85,64,95]}
print("idno:",d2["idno"])
print("name:",d2["name"])
print("marks",d2["marks"])
print("total marks:",sum(d2["marks"]))
print("max marks",max(d2["marks"]))
print("min marks",min(d2["marks"]))
print("first 3 marks:",d2["marks"][0:3])
print("last 3 marks",d2["marks"][3:6])


# recursive function
counter=0
def display():
    global counter
    counter+=1
    print(counter)
    display()
display()

import copy as cp
l1=[[10,20,],[25,30],[35,40]]
l2=cp.deepcopy(l1)
print("before")
print(l1)
print(l2)
#modification
l2[0][1]="python"
print("after")
print(l1)
print(l2)