t=int(input())
for j in range(t):
    n=int(input())
    lst=[]
    for k in range(1,n+1):
        lst.append(k)  
    i=1
    while(i<len(lst)-1):
        print(i)
        print(lst)
        if(lst[i]==i+1 and (i+1)!=len(lst)):
            lst[i],lst[i+1]=lst[i+1],lst[i]
        if(i+1==len(lst)):
            lst[i],lst[i-1]=lst[i-1],lst[i]  
        i+=1  
    for z in lst:
        print(z,end=" ")
    print()    
            