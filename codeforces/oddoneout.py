t=int(input())
for i in range(t):
    x,y,z=(int(i) for i in input().split())
    if(x==y):
        print(z)
    elif(y==z):
        print(x)
    else:
        print(y)        