t=int(input())
for i in range(t):
    X,Y=input().split()
    x,y=int(X),int(Y)
    lhs=(x**4)+4*(y**2)
    rhs=4*(x**2)*y
    if(lhs==rhs):
        print("yes")    
    else:
        print("no")    