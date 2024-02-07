import sys
sys.stdin=open("input.txt","r")
sys.stdout=open("output.txt","w")
for i in range(int(input())):
    n,m,k=(int(i) for i in input().split())
    nLst=input().split()
    mLst=input().split()
    for i in range(n):
        nLst[i]=int(nLst[i])
    for i in range(m):
        mLst[i]=int(mLst[i])
    nkLst,mkLst=[],[]
    for i in range(1,k+1):
        for j in range(n):
            if(nLst[j]==i):
                nkLst.append(i)
        for j in range(m):
            if(mLst[j]==i):
                mkLst.append(i)
    for i in range(1,k+1):
        if(i in nLst and i not in mLst):
            lst.appe         

