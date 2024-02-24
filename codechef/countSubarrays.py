for i in range(int(input())):
    n=int(input())
    p=input().split()
    for i in range(n):
        p[i]=int(p[i])
    sum=0
    psumLst=[0]
    for i in p:
        sum+=i
        psumLst.append(sum)
    zeroLst=[0]*(n+1)
    for i in range(n+1):
        for j in range(i+1,n+1):
            diff=psumLst[j]-psumLst[i]
            if(diff>n):
                break
            else:
                zeroLst[diff]+=1
    print(*zeroLst[1:])        
    