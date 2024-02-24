for _ in range(int(input())):
    n,m,x,y,l=(int(i) for i in input().split())
    count=0
    x1=x
    y1=y
    x2=x
    y2=y
    while(True):
        x1+=l
        y1+=l
        if(x>=n or x+l>=n):
            continue
        else:
            count+=1
        if(y>=n or y+l>=n):
            continue
        else:
            count+=1
        x2-=l
        y2-=l
        if(x>=n or x-l>=n):
            continue
        else:
            count+=1
        if(y>=n or y-l>=n):
            continue
        else:
            count+=1
    
        
