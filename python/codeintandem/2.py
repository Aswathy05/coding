n = int(input())
lst = []
for i in range(n):
    lst.append(0)
k = int(input())
q = int(input())
for i in range(k):
    l,r,fishes = tuple(input().split())
    l = int(l)
    r = int(r)
    fishes = int(fishes)
    while(l<=r):
        lst[l-1]+=fishes
        l+=1
for i in range(q):
    sum = 0
    l,r = tuple(input().split())
    l= int(l)
    r = int(r)
    while(l<=r):
        sum+=lst[l-1]
        l+=1
    print(sum)
