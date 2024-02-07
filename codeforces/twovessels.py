t=int(input())
for i in range(t):
    lst=input().split()
    a=int(lst[0])
    b=int(lst[1])
    c=int(lst[2])
    eq=(a+b)/2
    if(a<b):
        a,b=b,a
    extra=eq-b
    if(extra/c==extra//c):
        print(int(extra/c))
    else:
        print(int((extra//c)+1))        