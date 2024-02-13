import sys
sys.stdin=open("input.txt","r")
sys.stdout=open("output.txt","w")
t=int(input())
for i in range(t):
    s=input().split()
    sum=0
    for i in s:
        if(int(i)==1):
            sum+=1
    if(sum>=4):
        print("YES")
    else:
        print("NO")            