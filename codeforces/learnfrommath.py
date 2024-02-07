n=int(input())
lst=[]
lst.append(n//2)
lst.append(n-(n//2))
for i in lst:
    print(i,end=" ")