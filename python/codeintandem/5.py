s=input()
dic={}
for i in s:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
sorteddic = sorted(dic.items(), key= lambda x: x[1])
lst=[]
for i in range(len(sorteddic)):
    lst.append(sorteddic[i][1])   
maxi=max(lst)   
a=[]
for i in range(len(sorteddic)):
    if(sorteddic[i][1]==maxi):
        a.append(sorteddic[i][0])
print(min(a))        



