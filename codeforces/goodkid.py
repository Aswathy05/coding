t=int(input())
for i in range(t):
    n=int(input())
    s=input().split()
    lst=[]
    for i in s:
        lst.append(int(i))
    mini=min(lst)
    
    for i in range(n):
        if(lst[i]==mini):
            
            lst[i]+=1
            lst[i]=lst[i]
            break
    
    prod=1    
    for i in lst:
        prod*=i
    print(prod)       