t=int(input())
for i in range(t):
    x,y=(int(i) for i in input().split())
    if((x//y)>20):
        print(20)
    else:
        print(x//y)    