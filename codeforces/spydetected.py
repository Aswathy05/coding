t=int(input())
for j in range(t):
    n=int(input())
    a=input().split()
    if(a[0]!=a[1] and a[1]==a[2]):
        print(1)
    elif(a[len(a)-1]!=a[len(a)-2] and a[len(a)-2]==a[len(a)-3]):
        print(len(a))    
    else:    
        for i in range(1,n-1):
            if(a[i]!=a[i-1]):
                if(a[i]!=a[i+1]):
                    print(i+1)
                    break          

        
        