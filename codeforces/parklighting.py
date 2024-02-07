t=int(input())
for i in range(t):
    lst=input().split()
    m,n=int(lst[0]),int(lst[1])
    pdt=m*n
    if(pdt<=2):
        print(1)
    elif(pdt%2==0):
        print((pdt//2))
    else:
        print((pdt//2)+1)   