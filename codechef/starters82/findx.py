t=int(input())
for i in range(t):
    lst=[int(x) for x in input().split()]
    a,b,c,d=lst[0],lst[1],lst[2],lst[3]
    x=0
    
    while((a+x)%b!=(c+x)%d):
        x+=1
    print(x)    
