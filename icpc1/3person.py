t=int(input())
for i in range(t):
    n=int(input())
    a,b,c=(int(i) for i in input().split())
    for i in range(n-1):
        u,v=(int(i) for i in input().split())
        if((u==a or u==b or u==c) and (v==a or v==b or v==c)):
            if(u==a or v==a):
                
        else:
            print("DRAW")    