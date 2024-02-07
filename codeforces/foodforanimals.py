t=int(input())
for i in range(t):
    lst=input().split()
    a,b,c,x,y=int(lst[0]),int(lst[1]),int(lst[2]),int(lst[3]),int(lst[4])
    if(a>=x and b>=y):
        print("yes")
    elif(a<x and b>=y and (a+c)>=x):
        print("yes")
    elif(a>=x and b<y and (b+c)>=y):
        print("yes")    
    elif(a<x and b<y and (((a+c)-x)+b)>=y):
        print("yes")    
    else:
        print("no")    