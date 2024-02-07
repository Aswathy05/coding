t=int(input())
for i in range(t):
    lst=input().split()
    n=int(lst[0])
    x=int(lst[1])
    amt=n*x
    if(len(str(amt))==5):
        print("yes")
    else:
        print("no")    