t=int(input())
for i in range(t):
    lst=input().split()
    a=int(lst[0])
    b=int(lst[1])
    longside=max(a,b)
    smolside=min(a,b)
    if(2*smolside>=longside):
        print((smolside*2)**2)
    else:
        print((longside)**2)    
        