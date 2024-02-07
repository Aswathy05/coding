n=int(input())
a=input().split()
lst=[]
for i in a:
    lst.append(int(i))
count=0
for j in lst:
    count+=int(max(lst))-int(j)
print(count)    