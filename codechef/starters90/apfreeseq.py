t=int(input())
for i in range(t):
    n=int(input())
    lst=input().split()
    a=int(lst[0])
    b=int(lst[1])
    c=int(lst[2])
    if((b-a)==(c-b)):
        print("no")
    elif((c-b)==(a-c)):
        print("no")
    elif((a-c)==(b-a)):
        print("no")     
    else:
        print("yes")    