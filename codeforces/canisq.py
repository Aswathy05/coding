
t=int(input())
for i in range(t):
    n=int(input())
    s=input().split()
    sum=0
    for i in s:
        sum+=int(i)
    if(sum**0.5 == int(sum**0.5)):
        print("yes")
    else:
        print("no")        