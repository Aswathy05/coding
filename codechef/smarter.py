t=int(input())
for i in range(t):
    x=input().split()
    l=int(x[0])
    v1=int(x[1])
    v2=int(x[2])
    if(l/v1==l//v1):
        t1=l//v1
    else:
        t1=(l//v1)+1
    if(l/v2==l//v2):
        t2=l//v2
    else:
        t2=(l//v2)+1
    if(t2<t1):
        print(t1-t2-1)
    else:
        print(-1)       
