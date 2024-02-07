t=int(input())
for i in range(t):
    a=input().split()
    first=int(a[0])
    last=int(a[1])
    num=int(a[2])
    add=0
    i=0
    lst=[last]
    for i in range(num-1):
        i+=1
        last-=i
        lst.append(last)
    
    if(lst[len(lst)-1])<first:
        print(-1)
    else:    
        lst=lst[::-1]
        lst[0] = first
        for i in lst:
            print(i, end=" ")
        print()    