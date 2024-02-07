t=int(input())
for i in range(t):
    n=int(input())
    s=input().split()
    lst=[]
    for i in s:
        lst.append(int(i))
    for i in range(1,n-2):
        if((lst[i-1]+lst[i])!=(lst[i+1]+lst[i+2])):
            print("YES")
            break
    else:
        print("NO")     