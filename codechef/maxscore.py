t=int(input())
for i in range(t):
    n=int(input())
    s=input().split()
    lst=[]
    for i in s:
        lst.append(int(i))
    one,zero=0,0    
    for i in lst:
        if(i==1):
            one+=1
        else:
            zero+=1        
    if(zero==0 or one==0):
        print(0)
    elif(zero<=one):
        print(zero)
    elif(one<zero):
        print(one)

                