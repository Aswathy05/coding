t=int(input())
for i in range(t):
    n=int(input())
    lst1=input().split()
    a=[]
    for i in lst1:
        a.append(int(i))
    b=[]    
    for i in range(1,n+1):
        b.append(i)
    if(b[0]==a[0]):
        b[0]+=1
        b[0]=b[0]   
    for i in range(1,n):
        while(b[i]==a[i] or b[i]<=b[i-1]):
            b[i]+=1        
            b[i]=b[i]      
    print(max(b))
