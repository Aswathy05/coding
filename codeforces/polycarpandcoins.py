t=int(input())
for i in range(t):
    n=int(input())
    x=n//3
    y=n//3+1
    if(x+2*y==n):
        print(x,y)
    elif(y+2*x==n):
        print(y,x) 
    else:
        print(x,x)       