#Who is taller? Alice(x) or bob(y)
T=int(input())
for i in range(T):
    a=input()
    lst=a.split()
    x=int(lst[0])
    y=int(lst[1])
    if(x>y):
        print("A")
    if(y>x):
        print("B")    