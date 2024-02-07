s="aabb"
dict={}
for i in range(len(s)):
    if(s[i] not in dict):
        dict[s[i]]=1
    elif(s[i] in dict):
        dict[s[i]]+=1       
for i in dict:
    if(dict[i]==1):
        for j in range(len(s)):
            if(s[j]==i):
                print(j)
                count=1
                break
        if(count==1):
            break    
else:
    print(-1)                   
        