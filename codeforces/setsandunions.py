t=int(input())
for i in range(t):
    n=int(input())
    s=[]
    for i in range(n):
        x=input().split()
        s.append(x)
       
   
    if(len(s)==1):
        print(0)
    else:    
        mini=min(s)
        s.remove(mini)
        union=[] 
        for i in range(len(s)):
            for j in range(len(s[i])):
                if(s[i][j] not in union):
                    union.append(s[i][j])
        print(len(union))