t=int(input())
for j in range(t):
    n=int(input())
    s=input()
    dic={}
    for i in s:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1  
    count=0          
    for i in dic:
        if((dic[i])%2!=0):
            count+=1   
    if(count<=1):      
        for k in dic:
            if(dic[k]>1):
                print(dic[k]-1)
    else:
        print(0)        
