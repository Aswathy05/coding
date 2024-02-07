t=int(input())
for i in range(t):
    n=int(input())
    a=input().split()
    lst1=[]
    for i in a:
        lst1.append(int(i))
    dic={}
    for i in lst1:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1 
    lst=[]    
    for i in dic:
        if(dic[i]==1):
            lst.append(i)    
    if(len(lst)!=0):
        mini=min(lst)  
        for i in range(n):
            if(mini==lst1[i]):
                print(i+1)      
    else:
        print(-1)
            