t=int(input())
for j in range(t):
    x=int(input())
    count=0
    for i in range(9,0,-1):
        if(x%i==0):
            count+=(i-1)*10
            break
    i=1111
    res=0
    while(i>0):
        if(x%i==0):
            res=1
        if(res==1):
            count+=len(str(i))
        i = (i//10)
    print(count)
    
    
