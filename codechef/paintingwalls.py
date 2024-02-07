t=int(input())
for i in range(t):
    x,y,z=(int(i) for i in input().split())
    area=x*y
    wallArea=z//2
    print(wallArea//area)