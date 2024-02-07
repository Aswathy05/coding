t=int(input())
for i in range(t):
    n,v=(int(i) for i in input().split())
    vol,value=[],[]
    for i in range(n):
        x,y=(int(i) for i in input().split())
        vol.append(x)
        value.append(y)
        