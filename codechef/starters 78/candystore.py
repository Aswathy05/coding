t=int(input())
for i in range(t):
    a=input()
    lst=a.split()
    x=int(lst[0])       #daily goal
    y=int(lst[1])       #number of chocolates actually sold
    if(y>x):
        print(x+(y-x)*2)
    else:
        print(y)    