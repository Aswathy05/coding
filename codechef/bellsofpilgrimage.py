t=int(input())
for i in range(t):
    lst=input().split()
    n=int(lst[0])
    x=int(lst[1])
    k=int(lst[2])
    p=int(lst[3])
    for i in range(1,k+1):
        if(i<=x):
            p+=10
        elif(i>x):
            p+=5   
    if(k==n):
        p+=20
    print(p)                