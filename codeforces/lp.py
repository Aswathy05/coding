t=int(input())
for i in range(t):
    p,l =(int(i) for i in input().split())
    s=l/p
    if(s>0.75):
        print("YES")
    else:
        print("NO")