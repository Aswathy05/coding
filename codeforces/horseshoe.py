x=input().split()
lst=[]
for i in x:
    if i not in lst:
        lst.append(i)
print(4-len(lst))