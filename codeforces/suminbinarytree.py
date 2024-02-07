t=int(input())
for i in range(t):
    n=int(input())
    i=0
    while(True):
        if(2^i>=n):
            num=2^i
            break
        i+=1    
    print(num)        
