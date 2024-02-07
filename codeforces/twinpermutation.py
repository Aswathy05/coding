t=int(input())
for i in range(t):
    n=int(input())
    a=input().split()
    lst=[]
    for i in a:
        lst.append(int(i))
    maxi=max(lst)+1    
    lst1=[]
    for i in lst:
        lst1.append(maxi-i)
    for i in lst1:
        print(i,end=" ")
    print()    