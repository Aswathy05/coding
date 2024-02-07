t=int(input())
for j in range(t):
    n=int(input())
    a=input().split()
    lst=[]
    for i in a:
        lst.append(int(i))
    mini=min(lst)    
    count=0
    for i in lst:
        if(i!=mini):
            count+=i-mini
    print(count)        
