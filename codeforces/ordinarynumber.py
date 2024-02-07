t=int(input())
for i in range(t):
    n=int(input())
    count=0
    num=0
    for k in range(1,n):
        nu=(num*10)+1      
        for d in range(1,9):
            d+=1
            if(k*d<=n):
                count+=1
    print(count)            
             
            