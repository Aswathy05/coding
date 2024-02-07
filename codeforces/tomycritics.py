t=int(input())
for i in range(t):
    x=input().split()
    a=int(x[0])
    b=int(x[1])
    c=int(x[2])
    if((a+b)>=10 or (b+c)>=10 or (a+c)>=10):
        print("YES")
    else:
        print("NO")  