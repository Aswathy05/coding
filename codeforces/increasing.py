t=int(input())
for k in range(t):
    n=int(input())
    s=input().split()
    dist=set(s)
    if(len(dist)<n):
        print("no")
    else:
        print("yes")    