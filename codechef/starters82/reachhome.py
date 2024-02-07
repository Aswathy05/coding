t=int(input())
for i in range(t):
    a=input()
    lst=a.split()
    x=int(lst[0])
    y=int(lst[1])
    if(x*5>=y):
        print("yes")
    else:
        print("no")    