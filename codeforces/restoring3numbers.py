x=input()
lst=x.split()
lst = [int(x) for x in lst]
x4=max(lst)
lst.remove(x4)
x1=lst[0]    
x2=lst[1]
x3=lst[2]
lst1=[]
lst1.append(x4-x1)
lst1.append(x4-x2)
lst1.append(x4-x3)
for i in lst1:
    print(i, end=" ")
