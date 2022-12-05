#7. Write a Python script to remove all non int values from a list.
li=["Ramesh",44,77,0,99,11,4.7,True,3+4j,"rahul"]
b=[]
for i in li:
    if type(i)==int:
       b.append(i)
a=b
print(a)      