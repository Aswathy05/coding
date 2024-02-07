t=int(input())
for i in range(t):
    n,m=(int(i) for i in input().split())
    x=input()
    s=input()
    count=0
    if(s in x):
        print(0)
    else:    
        while(True):
            x=x+x
            count+=1
            if(s in x):
                print(count)
                break
            if(len(x)>m*n and (s not in x)):
                print(-1)
                break
                


