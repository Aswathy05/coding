t=int(input())
for i in range(t):
    lst=input().split()
    n=int(lst[0])
    m=int(lst[1])
    k=int(lst[2])
    a=input().split()
    a1=[]
    for i in a:
        a1.append(int(i))
    if((m-max(a1))+1>=k):
        print("yes")    
    else:
        print("no")    