t=int(input())
for i in range(t):
    n=int(input())
    r=input().split()
    up,down=0,0
    for i in range(n):
        if(r[i]=="1"):
            up+=1
        elif(r[i]=="2"):
            down+=1
        else:
            up+=1
    print(up)                