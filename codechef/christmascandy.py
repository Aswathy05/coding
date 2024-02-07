t=int(input())
for i in range(t):
    n=int(input())
    a=input().split()
    lst=[]
    for i in a:
        lst.append(int(i))
    count=0    
    lsti,lstj=[],[]
    maxi=lst[0]
    for i in range(n):
        
        if(lst[i]>maxi):
            maxi=lst[i]
        
        if(lst[i]<maxi):
            count+=1
    print(count)                   