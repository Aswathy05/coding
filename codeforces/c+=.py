t=int(input())
for i in range(t):
    a,b,n=[int(x) for x in input().split()]
    count=0
    if(b>a):
        a,b=b,a
    while(b<=n):
        b+=a
        count+=1
    print(count)        

