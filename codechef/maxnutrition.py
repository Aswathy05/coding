t=int(input())
for i in range(t):
    n=int(input())
    a1=input().split()
    b1=input().split()
    a,b=[],[]
    for i in a1:
        a.append(int(i))
    for i in b1:
        b.append(int(i))    
    dict={}
    for i in range(n):      
        if(a[i] not in dict):
            dict[a[i]]=b[i]
        elif(a[i] in dict and b[i]>dict[a[i]]):
            dict[a[i]]=b[i]
    sum=0 
    for i in dict:
        if(dict[i]>=0):
            sum+=dict[i]
    print(sum)        