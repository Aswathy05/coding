t=int(input())
for i in range(t):
    lst=input().split()
    n=int(lst[0])
    m=int(lst[1])
    if(m*36>=n):
        print("yes")
    else:
        print("no")    