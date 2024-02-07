t=int(input())
for k in range(t):
    x=input().split()
    n=int(x[0])
    k=int(x[1])
    l=int(x[2])
    lst1=[]
    for j in range(n):
        y=input().split()
        mi=int(y[0])
        li=int(y[1])
        if(l==li):
            lst1.append(mi)  
    if(len(lst1)!=0):    
        count=0
        for i in range(k):
            count+=max(lst1)
            lst1.remove(max(lst1))  
        print(count)   
    else:
        print(-1)       

