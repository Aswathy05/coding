t=int(input())
for i in range(t):
    lst=input().split()
    n=int(lst[0])
    k=int(lst[1])
    x=int(lst[2])
    wholeSum=((n*(n+1))//2)
    bigSum=((n*(n+1))//2)-(((n-k)*((n-k)+1))//2)#whole
    smallSum=((k*(k+1))//2) #givn
    if(bigSum<x):
        print("NO")        
    elif(bigSum==x or smallSum==x or wholeSum==x):
        print("YES")
    else:
        if(smallSum>x):
            print("NO")
        else:
            print("YES")          

                