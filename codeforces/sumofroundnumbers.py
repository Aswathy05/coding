t=int(input())
for j in range(t):
    n=int(input())
    s=str(n)
    num=0
    for i in s[::-1]:
        if(i!="0"):
            print(int(i)*(10**num), end=' ')
        num+=1
    print()
    '''
    lst=[]
    while(n>0):
        r=n%10
        n=n//10
        lst.append(r)
    lst1=[]      
    for i in range(len(lst)-1,-1,-1):
        if(lst[i]==0):
            continue
        else:
            lst1.append(lst[i]*(10**i))
    print(len(lst1))          
    for k in lst1:
        print(k,end=" ")
    print()
   '''

