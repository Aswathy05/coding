t=int(input())
for i in range(t):
    n=int(input()) #length of the string
    s=input() # UDLR
    x=0
    y=0
    res=0
    for j in s:
        if(j=="U"):
            y+=1
        elif(j=="D"):
            y-=1
        elif(j=="L"):
            x-=1
        else:
            x+=1
        if(x==1 and y==1):
            print("yes")
            res=1
            break
    if(res==0):
        print("no")