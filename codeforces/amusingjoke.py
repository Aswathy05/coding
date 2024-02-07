guest=input()
host=input()
str1=input()
lst1,lst2=[],[]
for i in guest+host:
    lst1.append(i)
for i in str1:
    lst2.append(i)
lst1.sort()
lst2.sort()
if(lst1==lst2):
    print("YES")
else:
    print("NO")    
