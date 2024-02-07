t=int(input())
for i in range(t):
    n=input()
    lst=n.split()
    a=int(lst[0])
    b=int(lst[1])
    c=int(lst[2])
    x=int(lst[3])
    if(a+b>=x or a+c>=x or b+c>=x):
        print("yes")
    else:
        print("no")            