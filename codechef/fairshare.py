t=int(input())
for i in range(t):
    n,k=(int(i) for i in input().split())
    print(n-k*(n//(k+1)))