t=int(input())
for j in range(t):
    n=int(input())
    count=0
    lst=[]
    for i in range(1,n+1):
        lst.append(2**i)  
    print(lst)   
    i=0
    a,b=[],[]
    while(True):
        print(lst,"1")
        if(len(lst)==2):
            a.append(lst[0])
            b.append(lst[0])
            break
        else:    
            a.extend((lst[0],lst[len(lst)-1])) 
            lst.remove(lst[0])
            lst.remove(lst[len(lst)-1])
        print(lst,"2")
        if(len(lst)==2):
            a.append(lst[0])
            b.append(lst[0])
            break
        else:    
            b.extend((lst[0],lst[len(lst)-1])) 
            lst.remove(lst[0])
            lst.remove(lst[len(lst-1)])
    print(a,b)
        
