t=int(input())
for j in range(t):
    n=int(input())
    x=input().split()
    lst=[]
    for i in x:
        lst.append(int(i))
    orilst=lst[:]    
    mini1=min(lst)
    lst.remove(mini1)
    mini2=min(lst)
    sum=mini1+mini2
    count=0
    for i in lst:
        if(sum<=i):
            count+=1
            mini3=i
            break
    if(count==1):  
        ind2lst=[] 
        for i in range(n):
            if(orilst[i]==mini1):
                ind1=i+1
            if(orilst[i]==mini2):
                ind2lst.append(i+1)
            if(orilst[i]==mini3):
                ind3=i+1                 
        for i in ind2lst:
            if(i!=ind1):
                ind2=i
                break
        ind=[ind1,ind2,ind3] 
        ind.sort()       
        for i in ind:
            print(i,end=" ")
        print()    
    else:
        print(-1)                   



