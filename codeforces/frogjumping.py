t=int(input())
for i in range(t):
    lst=input().split()
    a=int(lst[0])
    b=int(lst[1])
    k=int(lst[2])
    if(k%2==0):
        print(((k//2)*a)-((k//2)*b))
    else:
        print((((k//2)+1)*a)-(k//2)*b)    