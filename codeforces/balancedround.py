t=int(input())
for j in range(t):
    x=input().split()
    n,k=int(x[0]),int(x[1])
    a=input().split()
    a1=[]
    for i in a:
        a1.append(int(i))
    a1.sort()   
    anew=[]
    lst=[]
    i=0
    while(i<(n-1)):
        if((a1[i+1]-a1[i])>k):
            lst.append(a1[len(anew):i+1])
            anew=a1[i+1:]    
        i+=1 
    
    if(len(lst)!=0):    
        lst.append(anew) 
    else:
        lst.append(a1)   
    num=[]   
    for i in lst:
        num.append(len(i))   
    if(max(num)==1 and n!=1):
        print(n)  
    else:      
        print(n-max(num))    


                 

