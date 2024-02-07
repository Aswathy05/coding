#if sum>6 print(yes)
t=int(input())
for i in range(t):
    a=input()
    lst=a.split()
    x=int(lst[0])
    y=int(lst[1])
    if(x+y>6):
        print("yes")
    else:
        print("no")