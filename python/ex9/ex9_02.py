n=int(input("Enter no. of persons : "))
L1,L2=[],[]
for i in range(n):
    name=input("Enter name : ")
    age=int(input("Enter age : "))
    L1.append(name)
    L2.append(age)
d={}
for i in range(n):
    d[L1[i]]=L2[i]
print(d)