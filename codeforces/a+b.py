t=int(input())
for i in range(t):
    s=input().split("+")
    lst=[]
    for i in s:
        lst.append(int(i))
    print(sum(lst))    