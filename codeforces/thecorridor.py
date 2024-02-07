t=int(input())
for i in range(t):
    n=int(input())
    dict={}
    key,value=[],[]
    for i in range(n):
        lst=input().split()
        d=int(lst[0])
        s=int(lst[1])
        key.append(d)
        value.append(s)
        dict[d]=s
    dict=sorted(dict)
    for i in dict:
        numRoom=i
        firstTrapSec=dict[i]   
        break
    if(firstTrapSec%2==0):
        ans=(firstTrapSec//2)-1
    else:
        ans=firstTrapSec//2  
    for i in key:
        print(key,value,dict[i],dict[dict[2]])
        if(dict[i]<ans):
            print(ans)
            ans=dict[i]
    print(ans,"inga")        
    if(ans<=0):
        print(numRoom,"here")
    else:
        print(numRoom-1+ans,"HERE")       