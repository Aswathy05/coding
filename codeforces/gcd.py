t=int(input())
for i in range(t):
    n,k =(int(i) for i in input().split())
    max_gcd = n//k
    out = []
    count = 0
    for i in range(1,n+1):
        if(count == k):
            break
        if(i%max_gcd == 0):
            out.append(i)
            count+=1        
    print(*out)