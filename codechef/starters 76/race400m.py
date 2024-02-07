T=int(input())
for i in range(T):
    a=input()
    lst=a.split()
    x=int(lst[0])
    y=int(lst[1])
    z=int(lst[2])
    if(x<y and x<z):
        print("ALICE")
    elif(y<x and y<z):
        print("BOB")
    else:
        print("CHARLIE")        