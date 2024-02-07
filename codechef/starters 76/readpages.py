T=int(input())
for i in range(T):
    a=input()
    lst=a.split()
    n=int(lst[0])
    x=int(lst[1])
    y=int(lst[2])
    if(x*y>=n):
        print("yes")
    else:
        print("no")    