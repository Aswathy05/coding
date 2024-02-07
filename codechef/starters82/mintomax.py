t=int(input())
for i in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    count=0
    for i in a:
        if(int(i)>int(min(a))):
            count+=1
    print(count)        

    