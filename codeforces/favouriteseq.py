n = int(input())
for j in range(n):
    x = int(input())
    lst = [int(x) for x in input().split()]
    res=[]
    for i in range(len(lst)//2):
        res.append(lst[i])
        res.append(lst[x-i-1])

    if(x%2==1):
        res.append(lst[x//2])
    for i in res:
        print(i,end=" ")
    print()    