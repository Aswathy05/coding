t=int(input())
for j in range(t):
    n=int(input())
    a=input().split()
    dic={}
    for i in a:
        if(i not in dic):
            dic[i]=1
        else:
            dic[i]+=1
    sorteddic = sorted(dic.items(), key= lambda x: x[1])
    print(sorteddic)
    for i in range(len(sorteddic)):
        if(sorteddic[i][1]>=3):
            print(sorteddic[i][0])
            break
    else:
        print(-1)        
    
