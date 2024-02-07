t=int(input())
for i in range(t):
    x,y,z=(int(i) for i in input().split())
    if((z*1440)>=(x*y)):
        print("yes")
    else:
        print("no")    