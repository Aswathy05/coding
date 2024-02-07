n=int(input())
lst=[]
for i in range(n):
    x=input().split()
    h,a=int(x[0]),int(x[1])
    lst.append((h,a))
lst1,lst2=[],[]    
for i in range(len(lst)):
    lst1.append(lst[i][0])
    lst2.append(lst[i][1]) 
count=0    
for i in lst1:
    for j in lst2:
        if(i==j):
            count+=1
print(count)        

