t=int(input())
for i in range(t):
    s=input().split()
    n=int(s[0])
    k=int(s[1])
    lst=[]
    while(n>0):
        lst.append((k//n)+1)
        lst.append((k//n))
        k-=((k//n)+(k//n)+1)
        n-=2
    if(k==0 and n==0):
        for i in lst:
            print(i,end=" ")
        print()
    else:
        print(-1)        