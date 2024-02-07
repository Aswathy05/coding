t=int(input())
for i in range(t):
    x=input().split()
    a=int(x[0])
    b=int(x[1])
    amt=a+(b*2)
    if(a==0):
        print(1)
    elif(b==0 and a<2):
        print(2)
    else:
        print(amt+1)    
