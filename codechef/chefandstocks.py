t=int(input())
for i in range(t):
    n=int(input())
    x=input().split()
    lst=[]
    for i in x:
        lst.append(int(i))
    lst.remove(min(lst))
    print(sum(lst))    