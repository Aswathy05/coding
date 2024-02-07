T=int(input())
for i in range(T):
    a=input()
    lst=a.split()
    X=int(lst[0])
    Y=int(lst[1])
    if(X>Y):
        print(X-Y)
        