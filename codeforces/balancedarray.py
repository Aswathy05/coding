t=int(input())
for i in range(t):
    n=int(input())
    if((n/2)%2!=0):
        print("no")
    else:
        print("yes")
        lst=[]   
        sum_even,sum_odd=0,0
        for j in range(1,n+1):
            if(j%2==0):
                lst.append(j)
                sum_even+=j    
        for j in range(1,n-1):
            if(j%2!=0):
                lst.append(j)
                sum_odd+=j 
        lst.append(sum_even-sum_odd) 
        for j in lst:
            print(j,end=" ")
        print()
                    
                        