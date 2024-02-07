t=int(input())
lst=[]
for i in range(t):
    n=int(input())
    lst.append(n)
count=0    
for i in range(0,len(lst)-1):
    if(int(lst[i])!=int(lst[i+1])):
        count+=1
print(count+1)            