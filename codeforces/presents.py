t=int(input())
p=input().split()
dic={}
for i in range(0,len(p)):
    dic[int(p[i])]=i+1  
lst1=sorted(dic.items())
for i in range(len(lst1)):
    print(lst1[i][1], end=" ")