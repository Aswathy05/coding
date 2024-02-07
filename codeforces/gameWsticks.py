n,m=(int(i) for i in input().split())
tot=n+m
count=0
while(True):
    if(n==0 or m==0):
        break
    count+=1
    n-=1
    m-=1
if(count%2==0):
    print("Malvika")
else:
    print("Akshat")    
