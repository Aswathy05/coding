t=int(input())
for i in range(t):
    x=input()
    lst=x.split()
    a=int(lst[0])
    b=int(lst[1])
    q=a//b
    step=b*(q+1)-a
    if(a/b==a//b):
        print("0")
    else:
        print(step)    