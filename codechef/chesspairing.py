t=int(input())
for i in range(t):
    n,x=(int(i) for i in input().split())
    total=n
    rated=x
    unrated=2*n-x
    if(rated>unrated):
        print(rated-unrated)
    else:
        print(0)    
