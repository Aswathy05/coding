import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
                  
t=int(input())
for j in range(t):
    s,d,k=(int(i) for i in input().split())
    bun = 2*s + 2*d
    cheese = s + 2*d
    patty = s + 2*d
    reqBun = (k+1)
    reqCheese = k
    reqpatty = k
    if(bun>=reqBun and cheese>=reqCheese and patty>=reqpatty):
        print("Case #" + str(j+1) + ": YES")
    else:
        print("Case #" + str(j+1) + ": NO")   

