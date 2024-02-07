t=int(input())
for i in range(t):
    lst=input().split()
    a=int(lst[0])
    b=int(lst[1])
    c=int(lst[2])
    if(a+b==c):
        print("+")
    else:
        print("-")    