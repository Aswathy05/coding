t=int(input())
for i in range(t):
    n=int(input())
    lst=[]
    for i in range(n):
        lst.append(2*i+1)
    for i in lst:
        print(i,end=" ")    
    print()