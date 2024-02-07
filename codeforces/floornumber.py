t=int(input())
for i in range(t):
    lst=input().split()
    n=int(lst[0])
    x=int(lst[1])
    if(n<=2):
        print(1)
    else:    
        print(((n-3)//x)+2)