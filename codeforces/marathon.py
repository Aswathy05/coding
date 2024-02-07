t=int(input())
for i in range(t):
    lst=input().split()
    a=int(lst[0])
    count=0
    for i in lst[1:]:
        if(int(i)>a):
            count+=1
    print(count)        