t=int(input())
for j in range(t):
    n=int(input())
    dict={}
    for i in range(n):
        x=input().split()
        a=int(x[0])
        b=int(x[1])
        if(a<=10):
            dict[i+1]=b  
    lst=[]        
    for k in dict:
        lst.append(dict[k]) 
    maxi=max(lst)
    for i in dict:
        if(maxi==dict[i]):
            print(i)    