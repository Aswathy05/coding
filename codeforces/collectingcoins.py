t=int(input())
for i in range(t):
    lst=input().split()
    a=int(lst[0])
    b=int(lst[1])
    c=int(lst[2])
    n=int(lst[3])
    maxi=max(a,b,c)
    n=n-(maxi-a)
    n=n-(maxi-b)
    n=n-(maxi-c)
    if(n>=0):
        if(n%3==0):
            print("yes")
        else:
            print("no")    
    else:
        print("no")    