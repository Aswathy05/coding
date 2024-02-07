t=int(input())
for i in range(t):
    x=input().split()
    k=int(x[1])
    s=input().split()
    for i in s:
        if(int(i)==k):
            print("yes")
            break
    else:
        print("no")    