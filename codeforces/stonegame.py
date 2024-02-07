t=int(input())
for i in range(t):
    n=int(input())
    a=input().split()
    lst=[]
    for j in a:
        lst.append(int(j))
    maxi=max(lst)    
    mini=min(lst)
    for j in range(1,n):
        if(lst[j-1]==maxi):
            maxind=j
        if(lst[j-1]==mini):
            minind=j
    count=0        
    print(maxind,minind)
    if(maxind>len(a)-maxind):
        count+=(len(a) -maxind) 
    else:
        count+=maxind    
    if(minind>len(a)-minind):
        count+=(len(a) -minind) 
    else:
        count+=minind    
    print(count)    
              