t=int(input())
for i in range(t):
    n=int(input())
    a=input().split()
    lst=[]
    for i in a:
        lst.append(int(i))
    lst1=[]    
    for i in range(1,n):
        for j in lst[i:]:
           
            lst1.append(lst[i-1]*j)
    print(sum(lst1))        
