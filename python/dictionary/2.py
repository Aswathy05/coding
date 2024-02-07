n=int(input("Enter the number of persons:"))
lst1,lst2=[],[]
for i in range(n):
    name=input("Enter the name:")
    age=int(input("Enter the age:"))
    lst1.append(name)
    lst2.append(age)
dict={}    
for i in range(n):
    dict[lst1[i]]=lst2[i]
print(dict)            

        