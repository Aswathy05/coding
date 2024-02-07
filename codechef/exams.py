t=int(input())
for i in range(t):
    x,y,z=(int(i) for i in input().split())
    if(z>(x*y)/2):
        print("yes")
    else:
        print("no")    