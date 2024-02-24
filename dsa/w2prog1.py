#three square theorem
def threesq(x):
    a=3
    b=1
    global n
    n=(4**a)*(8*b+7)
    while(True):
        print("a:",a,"b:",b)
        for i in range(b):
            for j in range(a): 
                n=(4**i)*(8*j+7)
                print(n,1)
                if(n==x):
                    return(False)            
        else:
            if(b>12 and n>x):
                return(True)
            else:
                b+=1
for i in range(int(input())):
    print(threesq(int(input())))

  