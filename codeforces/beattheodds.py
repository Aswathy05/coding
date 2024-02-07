t=int(input())
for k in range(t):
    n=int(input())
    a=input().split()
    lst=[]
    for j in a:
        lst.append(int(j))
    i=0    
    count=0
    while(i<n-1):
        if(lst[i]%2==0 and lst[i+1]%2!=0):
            count+=1
            i+=2
        elif(lst[i]%2!=0 and lst[i+1]%2==0):
            count+=1
            i+=2
        i+=1
    print(count)            
