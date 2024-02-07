t=int(input())
for i in range(t):
    x=input().split()
    n,k=int(x[0]),int(x[1])
    s=input()
    for i in range(n):
        if(s[i]=="B"):
            first=i
            for j in range(n):
                
                if("B" in s[i+1:]):
                    second="hehe"