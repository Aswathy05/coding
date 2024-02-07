t=int(input())
lst="abcdefghijklmnopqrstuvwxyz"
for i in range(t):
    n=int(input())
    s=list(input())
    maxi=max(s)
    count=0
    for i in lst:
        count+=1
        if(i==maxi):
            print(count)

    