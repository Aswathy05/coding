t=int(input())
for i in range(t):
    x,y=input().split()
    if(int(y)<=int(x)):
        print(2*int(y)+int(x))
    else:
        print(5*int(x))    