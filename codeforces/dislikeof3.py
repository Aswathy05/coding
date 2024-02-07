t=int(input())
for j in range(t):
    k=int(input())
    lst=[]
    i=0
    while(len(lst)<k): 
        i+=1
        if(i%3==0 or i%10==3):
            continue
        else:
            lst.append(i)    
    print(lst[len(lst)-1])        
