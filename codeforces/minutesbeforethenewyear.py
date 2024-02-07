t=int(input())
for i in range(t):
    lst=input().split()
    h=int(lst[0])
    m=int(lst[1])
    hm=h*60+m
    print(1440-hm)